#!/usr/bin/env python3
"""Heuristic prose audit for English AI conference manuscripts.

The script never edits input files. It detects patterns that deserve human
review; a finding is not automatically an error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SEVERITY_RANK = {"low": 1, "medium": 2, "high": 3}

SKIP_ENVIRONMENTS = {
    "equation",
    "equation*",
    "align",
    "align*",
    "gather",
    "gather*",
    "multline",
    "multline*",
    "table",
    "table*",
    "figure",
    "figure*",
    "algorithm",
    "algorithm*",
    "thebibliography",
}

PHRASE_RULES = [
    (
        "DEFENSIVE_DISCLAIMER",
        "high",
        re.compile(
            r"\b(?:we|this (?:paper|work|study)) (?:do|does) not "
            r"(?:claim|attempt|intend|aim|seek)\b|"
            r"\bnot intended to\b|\bthis is not to say\b|"
            r"\bshould not be (?:taken|interpreted) as\b",
            re.I,
        ),
        "Replace negative self-limitation with the positive scope or claim.",
    ),
    (
        "WEAK_META_FRAMING",
        "medium",
        re.compile(
            r"\b(?:it is worth noting that|it should be noted that|"
            r"to be clear|of course|we acknowledge that|we admit that|"
            r"interestingly|notably)\b",
            re.I,
        ),
        "Lead with the finding or limitation itself; remove meta-commentary.",
    ),
    (
        "APOLOGETIC_LIMITATION",
        "medium",
        re.compile(
            r"\b(?:our method is not perfect|although (?:this|the) "
            r"(?:study|work|paper) has limitations|despite (?:these|the) limitations)\b",
            re.I,
        ),
        "State the concrete failure condition and mechanism without apology.",
    ),
    (
        "PROSE_VERSUS",
        "medium",
        re.compile(r"\bvs\.?\b|\bversus\b", re.I),
        "Use a grammatical comparison in prose; reserve compact labels for tables.",
    ),
    (
        "REPORTING_LEAD",
        "medium",
        re.compile(
            r"^(?:table|figure|fig\.)\s*\S*\s+(?:shows|presents|reports|lists)|"
            r"^(?:the )?(?:experimental )?results (?:are|were) "
            r"(?:shown|summarized|reported|presented)",
            re.I,
        ),
        "Start with the finding, then cite the table or figure as evidence.",
    ),
]

HEDGE_MODAL_PATTERN = re.compile(r"\b(?:may|might|could)\b", re.I)
HEDGE_ADVERB_PATTERN = re.compile(
    r"\b(?:possibly|potentially|perhaps|arguably)\b",
    re.I,
)
HEDGE_EPISTEMIC_PATTERN = re.compile(
    r"\b(?:seem(?:s|ed)?|appear(?:s|ed)?)\b",
    re.I,
)
FIRST_PERSON_PATTERN = re.compile(
    r"\b(?:[Ww]e|[Oo]ur|[Oo]urs|[Oo]urselves|[Uu]s|"
    r"[Ii]|[Mm]y|[Mm]ine|[Mm]yself)\b"
)
ACTIVE_TRANSITIVE_PATTERN = re.compile(
    r"\b(?:"
    r"(?:this|the)\s+(?:paper|study|work|analysis)\s+"
    r"(?:proposes|presents|introduces|develops|studies|investigates|"
    r"examines|evaluates|reports|shows|demonstrates)|"
    r"(?:the|this|proposed)\s+"
    r"(?:method|model|framework|approach|system|module|component|network|"
    r"design|mechanism|encoder|decoder)\s+"
    r"(?:uses|selects|computes|produces|generates|extracts|aligns|fuses|"
    r"combines|preserves|suppresses|initializes|predicts|improves|"
    r"outperforms|achieves|shows|demonstrates|provides|enables|allows|"
    r"addresses|introduces)|"
    r"(?:the\s+)?(?:experiment|experiments|result|results|ablation|ablations|"
    r"evaluation|evaluations)\s+"
    r"(?:show|shows|demonstrate|demonstrates|confirm|confirms|reveal|reveals|"
    r"support|supports|indicate|indicates)|"
    r"(?-i:[A-Z][A-Z0-9-]{1,})\s+"
    r"(?:uses|selects|computes|produces|generates|extracts|aligns|fuses|"
    r"combines|preserves|suppresses|initializes|predicts|improves|"
    r"outperforms|achieves|shows|demonstrates|provides|enables|allows|"
    r"addresses|introduces|raises|reduces)"
    r")\b",
    re.I,
)
NEGATION_PATTERN = re.compile(
    r"\b(?:not|no|neither|nor|without|lack(?:s|ed|ing)?|cannot|can't|won't)\b",
    re.I,
)
CONCESSION_PATTERN = re.compile(
    r"\b(?:although|though|however|nevertheless|nonetheless|despite|while)\b",
    re.I,
)
INTERPRETATION_PATTERN = re.compile(
    r"\b(?:because|therefore|thus|hence|indicat(?:e|es|ed)|"
    r"suggest(?:s|ed)?|support(?:s|ed)?|consistent with|"
    r"attribute(?:s|d)?|explain(?:s|ed)?|reveal(?:s|ed)?|"
    r"imply|implies|mechanism|accounts? for|shows? that)\b",
    re.I,
)
NUMBER_PATTERN = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:%|×|x)?")
WORD_PATTERN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*")
ACRONYM_DEFINITION_PATTERN = re.compile(r"\(([A-Z][A-Z0-9-]{1,})\)")
MIXED_ACRONYM_DEFINITION_PATTERN = re.compile(
    r"\(([A-Z][A-Za-z0-9]*(?:-[A-Z][A-Za-z0-9]*)+)\)"
)
ACRONYM_TOKEN_PATTERN = re.compile(r"\b[A-Z][A-Z0-9-]*[A-Z0-9]\b")
ACRONYM_ALLOWLIST = {
    "IEEE",
    "ACM",
    "NVIDIA",
    "MATH",
    "REFERENCE",
    "CITATIONTOKEN",
}
SECTION_PATTERN = re.compile(
    r"\\(?:section|subsection|subsubsection|paragraph)\*?\{([^{}]+)\}"
)
BEGIN_ENV_PATTERN = re.compile(r"\\begin\{([^{}]+)\}")
END_ENV_PATTERN = re.compile(r"\\end\{([^{}]+)\}")
HEADING_PATTERN = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")


@dataclass(frozen=True)
class Segment:
    file: str
    line: int
    section: str
    text: str
    original: str


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    file: str
    line: int
    section: str
    message: str
    excerpt: str


def remove_tex_comment(line: str) -> str:
    return re.split(r"(?<!\\)%", line, maxsplit=1)[0]


def clean_tex(text: str) -> str:
    text = re.sub(r"\\(?:cite|citep|citet|citealp|citeauthor)\*?(?:\[[^\]]*\])?\{[^{}]*\}", " CITATIONTOKEN ", text)
    text = re.sub(r"\$\$.*?\$\$", " MATH ", text, flags=re.S)
    text = re.sub(r"\$[^$]*\$", " MATH ", text)
    text = re.sub(r"\\\[[\s\S]*?\\\]", " MATH ", text)
    text = re.sub(r"\\(?:ref|eqref|autoref|cref|Cref)\{[^{}]*\}", " REFERENCE ", text)
    text = re.sub(r"\\(?:textbf|textit|emph|mathrm|mathbf|operatorname)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("~", " ")
    text = re.sub(r"\\[%&_#{}]", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", text).strip()


def clean_plain(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> list[str]:
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
    return [part.strip() for part in parts if part.strip()]


def excerpt(text: str, limit: int = 220) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def read_segments(path: Path) -> list[Segment]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    is_tex = path.suffix.lower() == ".tex"
    has_document = is_tex and any("\\begin{document}" in line for line in lines)
    in_document = not has_document
    section = "Document"
    skip_stack: list[str] = []
    buffer: list[str] = []
    original_buffer: list[str] = []
    start_line = 1
    segments: list[Segment] = []

    def flush() -> None:
        nonlocal buffer, original_buffer, start_line
        raw = " ".join(buffer)
        cleaned = clean_tex(raw) if is_tex else clean_plain(raw)
        if cleaned:
            segments.append(
                Segment(
                    file=str(path),
                    line=start_line,
                    section=section,
                    text=cleaned,
                    original="\n".join(original_buffer),
                )
            )
        buffer = []
        original_buffer = []

    for number, raw_line in enumerate(lines, start=1):
        line = remove_tex_comment(raw_line) if is_tex else raw_line

        if is_tex:
            if "\\begin{document}" in line:
                in_document = True
                continue
            if "\\end{document}" in line:
                flush()
                break
            if not in_document:
                continue

            if "\\begin{abstract}" in line:
                flush()
                section = "Abstract"
                continue
            if "\\end{abstract}" in line:
                flush()
                section = "Body"
                continue

            section_match = SECTION_PATTERN.search(line)
            if section_match:
                flush()
                section = clean_tex(section_match.group(1)) or "Untitled"
                continue

            for env in BEGIN_ENV_PATTERN.findall(line):
                if env in SKIP_ENVIRONMENTS:
                    flush()
                    skip_stack.append(env)
            if skip_stack:
                for env in END_ENV_PATTERN.findall(line):
                    if skip_stack and env == skip_stack[-1]:
                        skip_stack.pop()
                continue
        else:
            heading_match = HEADING_PATTERN.match(line)
            if heading_match:
                flush()
                section = heading_match.group(1)
                continue

        if not line.strip():
            flush()
            start_line = number + 1
            continue

        if not buffer:
            start_line = number
        buffer.append(line)
        original_buffer.append(raw_line)

    flush()
    return segments


def add_finding(
    findings: list[Finding],
    segment: Segment,
    code: str,
    severity: str,
    message: str,
    sample: str,
) -> None:
    findings.append(
        Finding(
            code=code,
            severity=severity,
            file=segment.file,
            line=segment.line,
            section=segment.section,
            message=message,
            excerpt=excerpt(sample),
        )
    )


def audit_segment(segment: Segment, findings: list[Finding]) -> None:
    paragraph = segment.text
    sentences = split_sentences(paragraph)
    section_lower = segment.section.lower()

    if "abstract" in section_lower and re.search(
        r"\\(?:cite|citep|citet|citealp|citeauthor)", segment.original
    ):
        add_finding(
            findings,
            segment,
            "CITATION_IN_ABSTRACT",
            "high",
            "Remove citations from the abstract.",
            segment.original,
        )

    for sentence in sentences:
        lower = sentence.lower()

        if FIRST_PERSON_PATTERN.search(sentence):
            add_finding(
                findings,
                segment,
                "AUTHORIAL_FIRST_PERSON",
                "low",
                "Consider an impersonal or passive rewrite; retain first person only when it materially improves clarity.",
                sentence,
            )

        if ACTIVE_TRANSITIVE_PATTERN.search(sentence):
            add_finding(
                findings,
                segment,
                "ACTIVE_TRANSITIVE_VOICE",
                "medium",
                "Recast the transitive scientific action passively and place the object or evidence in subject position.",
                sentence,
            )

        for code, severity, pattern, message in PHRASE_RULES:
            if pattern.search(sentence):
                add_finding(findings, segment, code, severity, message, sentence)

        hedge_modals = HEDGE_MODAL_PATTERN.findall(sentence)
        hedge_adverbs = HEDGE_ADVERB_PATTERN.findall(sentence)
        hedge_epistemics = HEDGE_EPISTEMIC_PATTERN.findall(sentence)
        hedge_total = hedge_modals + hedge_adverbs + hedge_epistemics
        hedge_stack = (
            len(hedge_adverbs) >= 2
            or bool(hedge_modals and hedge_adverbs)
            or len(hedge_total) >= 3
        )
        if hedge_stack:
            add_finding(
                findings,
                segment,
                "HEDGE_STACK",
                "high",
                "Name the source of uncertainty and use one calibrated qualifier.",
                sentence,
            )
        elif hedge_total and any(
            key in section_lower for key in ("abstract", "conclusion", "contribution")
        ):
            add_finding(
                findings,
                segment,
                "HEADLINE_HEDGE",
                "low",
                "Check whether the headline claim can use a precise scope instead of a modal hedge.",
                sentence,
            )

        if len(NEGATION_PATTERN.findall(sentence)) >= 3:
            add_finding(
                findings,
                segment,
                "NEGATION_DENSITY",
                "medium",
                "Rewrite around what holds or what the method targets.",
                sentence,
            )

        if re.search(r"\bnot\b.{0,90}\bbut\b", lower):
            add_finding(
                findings,
                segment,
                "REFLEXIVE_NOT_BUT",
                "low",
                "Keep the not-X-but-Y contrast only if the distinction is scientifically central.",
                sentence,
            )

        word_count = len(WORD_PATTERN.findall(sentence))
        if word_count > 50:
            add_finding(
                findings,
                segment,
                "LONG_SENTENCE",
                "low",
                f"Sentence has {word_count} words; check whether one logical relation should become a new sentence.",
                sentence,
            )

        parenthetical_count = min(sentence.count("("), sentence.count(")"))
        parenthetical_chars = sum(len(match) for match in re.findall(r"\([^()]*\)", sentence))
        if parenthetical_count >= 2 or (
            len(sentence) > 0 and parenthetical_chars / len(sentence) > 0.24
        ):
            add_finding(
                findings,
                segment,
                "PARENTHESIS_DENSITY",
                "medium",
                "Promote important parenthetical content into grammatical prose.",
                sentence,
            )

        number_count = len(NUMBER_PATTERN.findall(sentence.replace("CITATIONTOKEN", "")))
        if "abstract" in section_lower:
            threshold = 4
        elif "experimental setup" in section_lower or "implementation" in section_lower:
            threshold = 8
        else:
            threshold = 6
        if INTERPRETATION_PATTERN.search(sentence):
            threshold += 2
        if number_count >= threshold:
            add_finding(
                findings,
                segment,
                "NUMERIC_DUMP",
                "medium",
                "Keep only the numbers needed for the sentence's finding; leave dense values to the table.",
                sentence,
            )

    acronym_definitions = ACRONYM_DEFINITION_PATTERN.findall(paragraph)
    if len(acronym_definitions) >= 3:
        add_finding(
            findings,
            segment,
            "ACRONYM_BURST",
            "medium",
            "Distribute acronym definitions and keep the unifying idea visible.",
            paragraph,
        )

    if len(CONCESSION_PATTERN.findall(paragraph)) >= 3:
        add_finding(
            findings,
            segment,
            "CONCESSION_DENSITY",
            "medium",
            "Check whether repeated contrast and concession are creating defensive prose.",
            paragraph,
        )

    if all(re.search(rf"\b{word}\b", paragraph, re.I) for word in ("first", "second", "third")):
        add_finding(
            findings,
            segment,
            "LISTY_PARAGRAPH",
            "low",
            "Check whether the paragraph is an inventory that should be organized by one claim.",
            paragraph,
        )

    numeric_sentences = sum(
        bool(NUMBER_PATTERN.search(sentence) or re.search(r"\b(?:table|fig(?:ure)?\.)\s*\S+", sentence, re.I))
        for sentence in sentences
    )
    if (
        len(sentences) >= 3
        and numeric_sentences >= 3
        and not INTERPRETATION_PATTERN.search(paragraph)
    ):
        add_finding(
            findings,
            segment,
            "TABLE_NARRATION",
            "medium",
            "The paragraph reports several values or table references without an explicit interpretation.",
            paragraph,
        )


def normalize_sentence(sentence: str) -> str:
    value = sentence.lower()
    value = re.sub(r"\b(?:table|figure|fig\.)\s*\S+", " reference ", value)
    value = NUMBER_PATTERN.sub(" number ", value)
    value = re.sub(r"[^a-z]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def audit_acronym_order(segments: list[Segment], findings: list[Finding]) -> None:
    defined: set[str] = set()
    reported: set[str] = set()

    for segment in segments:
        definition_starts = {
            match.start(1): match.group(1)
            for match in ACRONYM_DEFINITION_PATTERN.finditer(segment.text)
        }
        for mixed_match in MIXED_ACRONYM_DEFINITION_PATTERN.finditer(segment.text):
            for component in re.finditer(r"\b[A-Z][A-Z0-9]{1,}\b", mixed_match.group(1)):
                definition_starts[
                    mixed_match.start(1) + component.start()
                ] = component.group(0)
        for match in ACRONYM_TOKEN_PATTERN.finditer(segment.text):
            token = match.group(0)
            if match.start() in definition_starts:
                if token in defined:
                    add_finding(
                        findings,
                        segment,
                        "ACRONYM_REDEFINITION",
                        "medium",
                        f"{token} was already defined in this artifact; retain only the acronym here.",
                        segment.text,
                    )
                defined.add(token)
                continue
            if (
                token in ACRONYM_ALLOWLIST
                or re.fullmatch(r"A\d+(?:--A\d+)*", token)
                or re.fullmatch(r"Q\d+", token)
                or token in defined
                or token in reported
            ):
                continue
            add_finding(
                findings,
                segment,
                "ACRONYM_BEFORE_DEFINITION",
                "medium",
                f"Define and conceptually hook {token} before its first substantive use.",
                segment.text,
            )
            reported.add(token)


def audit(paths: Iterable[Path]) -> list[Finding]:
    findings: list[Finding] = []
    sentence_index: dict[str, tuple[Segment, str]] = {}

    for path in paths:
        segments = read_segments(path)
        audit_acronym_order(segments, findings)
        for segment in segments:
            audit_segment(segment, findings)
            for sentence in split_sentences(segment.text):
                normalized = normalize_sentence(sentence)
                if len(normalized.split()) < 12:
                    continue
                previous = sentence_index.get(normalized)
                if previous:
                    add_finding(
                        findings,
                        segment,
                        "DUPLICATE_SENTENCE",
                        "medium",
                        f"Substantially duplicates a sentence near line {previous[0].line}.",
                        sentence,
                    )
                else:
                    sentence_index[normalized] = (segment, sentence)

    return sorted(
        findings,
        key=lambda item: (
            -SEVERITY_RANK[item.severity],
            item.file,
            item.line,
            item.code,
        ),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit English paper prose without modifying the input."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument(
        "--min-severity",
        choices=("low", "medium", "high"),
        default="low",
        help="Hide findings below this severity.",
    )
    parser.add_argument(
        "--fail-on",
        choices=("none", "low", "medium", "high"),
        default="none",
        help="Return exit code 1 when a finding at or above this severity exists.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    missing = [str(path) for path in args.paths if not path.is_file()]
    if missing:
        print("Missing input file(s): " + ", ".join(missing), file=sys.stderr)
        return 2

    findings = audit(args.paths)
    minimum = SEVERITY_RANK[args.min_severity]
    visible = [item for item in findings if SEVERITY_RANK[item.severity] >= minimum]
    counts = Counter(item.severity for item in findings)

    if args.json:
        payload = {
            "summary": {
                "files": len(args.paths),
                "findings": len(findings),
                "high": counts["high"],
                "medium": counts["medium"],
                "low": counts["low"],
            },
            "findings": [asdict(item) for item in visible],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(
            "Audit summary: "
            f"{len(findings)} finding(s) "
            f"[high={counts['high']}, medium={counts['medium']}, low={counts['low']}]"
        )
        if not visible:
            print("No findings at the selected severity.")
        for item in visible:
            print(
                f"\n[{item.severity.upper()}] {item.code} "
                f"{item.file}:{item.line} ({item.section})"
            )
            print(f"  {item.message}")
            print(f"  {item.excerpt}")

    if args.fail_on != "none":
        threshold = SEVERITY_RANK[args.fail_on]
        if any(SEVERITY_RANK[item.severity] >= threshold for item in findings):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
