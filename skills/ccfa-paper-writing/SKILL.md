---
name: ccfa-paper-writing
description: Draft, restructure, review, and polish English CCF-A AI conference papers with claim-forward, evidence-led prose, explicit problem boundaries, dependency-ordered terminology, passive-dominant style, restrained authorial first person, compact section hierarchies, visually full lines, fully occupied pages, and mandatory page-by-page VLM inspection of the rendered PDF. Use for manuscripts or sections in LaTeX, Markdown, text, or PDF, especially when prose is defensive, parenthetical, list-like, number-dense, report-like, logically loose, repetitive, unhooked, first-person-heavy, uses prose “VS,” leaves short terminal lines or page whitespace, creates oversized gaps below figure or table captions, or fragments sections into many headings. Preserve facts, claims, necessary limitations, venue rules, and locked content while making the paper rigorous, coherent, visually balanced, and submission-ready.
---

# CCF-A Paper Writing

Write as a researcher advancing and testing an argument, not as an author negotiating with an imagined reviewer.

## Load the standard

Read the following resources before substantive work:

1. Always read `references/writing-standard.md`.
2. Always read `references/problem-boundary-and-hooks.md`.
3. Read `references/section-playbook.md` when drafting or revising any paper section.
4. Read `references/revision-and-review.md` for a full-paper audit, restructuring task, review report, or final submission pass.
5. Read `references/rendered-layout-audit.md` whenever a compiled PDF is provided, can be produced, or layout is part of the request. Its page-by-page VLM gate is mandatory for a final submission pass.
6. Run `scripts/audit_prose.py` on local `.tex`, `.md`, or `.txt` manuscripts when available. Treat its findings as prompts for judgment, not automatic errors.

## Non-negotiable principles

1. **Advance one central claim.** Build the paper around a problem, a failure mechanism, a design response, and evidence that tests the response.
2. **Define the problem boundary.** State the target, inputs, output unit, operating setting, required assumptions, adjacent tasks excluded from the claim, and empirical scope before the solution is presented.
3. **Order concepts by dependency.** Give every technical term, module, symbol, metric, or dataset a prior conceptual hook. A later term must be motivated or defined by earlier text.
4. **Make the chain continuous.** Let each section and paragraph answer a question created by the preceding unit and create the question answered next.
5. **Use a passive-dominant house style.** Minimize authorial first person, including `we`, `our`, and `us`, but do not ban it. Prefer passive constructions for transitive contribution, method, experiment, and result statements whenever a natural passive form exists. Retain first person only when it makes an authorial choice materially clearer or avoids an unnatural, ambiguous passive.
6. **Lead with the point.** Put the claim or finding before qualification, table references, or caveats.
7. **Explain why.** A paper is not a manual. For every design choice, state the problem it addresses, the mechanism it introduces, and the expected consequence.
8. **Interpret evidence.** Do not merely enumerate scores. State the finding, give only the evidence needed to support it, explain the mechanism or implication, and connect it to the paper’s thesis.
9. **Calibrate rather than retreat.** Match verbs to evidence strength. Replace vague hedging and disclaimers with a precise population, setting, comparison, or evidential scope.
10. **Preserve necessary limits.** Keep limitations that affect validity, interpretation, deployment, ethics, or reproducibility. State them once in the section where they matter.
11. **Protect facts.** Never alter experimental values, splits, method definitions, citations, or claims merely to improve prose. Flag contradictions instead.
12. **Prefer semantic clarity over decoration.** Do not swap technical terms for synonyms merely to create variety. Do not inflate vocabulary.
13. **Use venue rules as hard constraints.** Preserve required templates, anonymity, page limits, and official terminology.
14. **Enforce visually full lines.** Inspect the rendered PDF rather than source-code wrapping. Running prose is expected to fill the available measure; nonterminal lines should reach both margins under normal justification, and paragraph-final lines must be near-full. Reject any terminal line containing only one or two words or leaving a conspicuously large unused span. Repair it through a small, meaningful, fact-preserving expansion or recast of that paragraph. Never use filler, forced line breaks, invisible text, font or margin changes, global looseness, or spacing tricks.
15. **Fill every page deliberately.** Every submitted page must reach the intended bottom boundary and appear intentionally full inside the official text block. Reject avoidable blank regions, short columns, sparse final pages, isolated headings, and float placement that leaves visible holes. In a two-column paper, the column bottoms should normally differ by no more than one or two body-text lines. Repair a sparse page by slightly expanding the responsible paragraph, caption, protocol explanation, or evidence interpretation with scientifically useful content; never pad or move the same blank region to another page.
16. **Keep the section hierarchy compact.** A major section should normally contain two to four substantive subsections; five is the upper limit for a genuinely complex Method or Experiments section. Do not use third-level headings in a short conference main paper, and do not recreate them through many `\paragraph{}` or bold mini-headings. Merge neighboring points that answer the same scientific question.
17. **Require a page-by-page VLM layout audit.** After every layout-affecting revision, compile the complete artifact, rasterize every page, and inspect every rendered page with a vision-capable model. A log-only, text-only, source-only, page-count-only, or sampled-page check is insufficient. The main paper, references, supplementary material, and checklist must each be inspected when they are submitted. Do not call the layout finished if any page was skipped or if visual tooling was unavailable.
18. **Control caption-to-text whitespace.** The visible gap between the bottom of a figure or table caption and the next running text must not exceed one body-text line. If the region is too large, first expand the caption with useful self-contained information such as the comparison, protocol, reading key, or bounded takeaway. If needed, revise the adjacent paragraph or legal float placement next. Never modify template geometry or insert manual negative spacing.
19. **Define each acronym exactly once.** Within each independently submitted or independently read artifact, write the full term followed immediately by its acronym in parentheses at the first occurrence, then use only the acronym thereafter. The abstract and main body form one continuous scope: never re-expand an acronym in the Introduction after defining it in the abstract. Apply the same rule to headings, running text, captions, and table notes. Treat a separately submitted supplement or checklist as a new scope only because it must stand alone. If a shortened form occurs only once, omit the acronym and retain the full term. Bibliographic titles, mathematical symbols, conventional units, and official identifiers that are not used as prose abbreviations are not acronym definitions.

## Build the argument before editing sentences

Construct this narrative spine:

```text
Important task
→ concrete unresolved failure
→ why existing approaches produce that failure
→ design requirement implied by the diagnosis
→ proposed mechanism satisfying the requirement
→ controlled evidence testing that mechanism
→ broader implication and bounded scope
```

Reject a draft that only follows:

```text
background → module A → module B → module C → many numbers
```

Before rewriting, create a claim–evidence ledger:

| Claim | Evidence | Valid scope | Proper verb | Best section |
|---|---|---|---|---|
| What the paper wants the reader to believe | Exact experiment, derivation, or observation | Dataset, model, condition, or assumption | shows / supports / suggests | Abstract, introduction, experiments, or limitations |

Remove or narrow claims without evidence. Surface decisive evidence earlier.

Create two additional ledgers:

| Boundary field | Required content |
|---|---|
| Target | Exact phenomenon or task being studied |
| Inputs and output | Available evidence and prediction unit |
| Setting and assumptions | Conditions under which the formulation holds |
| Adjacent exclusions | Closely confusable tasks not covered by the claim |
| Empirical scope | Benchmarks, protocols, and populations supporting the claim |

| Term | Prior hook | First and only definition | Later form | Dependencies | First substantive use |
|---|---|---|---|---|---|
| Every nonstandard concept, acronym, module, symbol, metric, and dataset | Earlier problem, requirement, or familiar concept | Exact defining sentence and artifact location | Acronym or stable short form only | Terms that must already be known | First sentence that relies on it |

Reorder or rewrite any term whose prior hook is empty. For every acronym, search the complete artifact for later expansions and remove them; do not reset the ledger after the abstract.

## Use the paragraph contract

Give each paragraph one job and usually four moves:

1. **Claim:** state the paragraph’s point.
2. **Mechanism or reason:** explain why the claim should hold.
3. **Evidence or specification:** provide the decisive detail.
4. **Implication or bridge:** state what follows and connect to the next paragraph.

Do not force all four moves when two or three suffice. Never mix a contribution, three caveats, an unrelated implementation detail, and a future-work remark in one paragraph.

Use lexical continuity as the default hook: repeat the exact technical concept, use a clear noun phrase such as “this alignment mechanism,” and make causal or contrast transitions only when the relation is real. Do not rely on `this`, `it`, a transition word, or a module name to introduce an unseen concept. Before each new term, establish why the concept is needed; then name and define it.

## Remove defensive writing

Classify each qualification before editing:

- unnecessary disclaimer;
- necessary scope condition;
- methodological limitation;
- evidence-based uncertainty;
- useful conceptual contrast;
- redundant clarification.

Delete unnecessary disclaimers. Convert negative scope to positive scope:

```text
Weak: We do not claim that the method works in every situation.
Strong: The scope is restricted to scenes in which visually plausible sources can be disambiguated by motion.
```

State a real limitation once:

```text
Semantically similar candidates moving in synchrony cannot be reliably separated by the pooled audio representation.
```

Do not scatter variants of “does not prove,” “should not be interpreted as,” or “we acknowledge” through the abstract, introduction, results, and conclusion.

## Match language to evidence

Use:

- **shows / demonstrates / establishes** for direct measurements or controlled tests;
- **supports** for converging evidence that rules out plausible alternatives;
- **indicates** for a stable empirical pattern;
- **suggests / is consistent with** for a mechanism inferred rather than directly identified;
- **may / could** only when the uncertainty itself is real and named.

Do not strengthen a claim beyond the design. Do not weaken a well-supported claim merely to sound cautious.

## Control report-like style

- Replace prose `VS`, `vs.`, and slash-heavy score pairs with grammatical comparisons or a table.
- Define each acronym exactly once as `Full Term (ACR)` at its first occurrence, then use only `ACR`; do not re-expand it when the abstract gives way to the Introduction.
- Keep parenthetical content auxiliary. Promote important information into the sentence.
- In an abstract, use at most the few headline values needed to establish the result.
- In results prose, do not recite every table cell. Select the comparison that answers the subsection question.
- Prefer “A 5.9-point Jaccard improvement over VCT is obtained on MS3” to “73.50 VS 67.60 (+5.90).”
- Avoid contribution lists that name modules without explaining their scientific role.
- Avoid sentence openings such as “Table 2 shows,” “It is worth noting that,” or “Interestingly.” Lead with the finding.

## Execute the revision workflow

1. **Lock the evidence.** Record authoritative sources for numbers, dataset facts, names, and claims.
2. **Lock the problem boundary.** Complete the boundary ledger and keep claims inside it.
3. **Build the term dependency order and acronym ledger.** Complete the term ledger, move each hook before the term that depends on it, record the first and only expansion of every acronym across the whole artifact, and replace every later expansion with the short form.
4. **Diagnose the paper.** Identify the thesis, failure mechanism, evidence chain, and missing logical links.
5. **Fix section functions and granularity.** Reorder or merge sections before polishing sentences. Keep major sections at two to four substantive subsections, with at most five in Method or Experiments when each answers a distinct scientific question.
6. **Fix paragraph jobs and bridges.** Give every paragraph a topic claim, an earlier hook, and a question or concept passed forward.
7. **Rewrite claim-forward and passive-dominant.** Reduce unnecessary first person and avoidable active constructions; remove throat-clearing, defensive framing, list-like exposition, and redundant comparisons.
8. **Audit logic.** Verify every causal, contrastive, concessive, comparative, and referential relation.
9. **Audit evidence.** Check every result sentence against its table or source.
10. **Audit language.** Run the bundled prose auditor, then judge each finding in context.
11. **Run the rendered-PDF VLM gate.** Compile the complete artifact, rasterize every page at readable resolution, inspect a contact sheet for global flow, and inspect every page individually with a vision-capable model. Mark each page pass or fail for line fullness, page-bottom occupancy, column balance, float placement, caption-to-text gaps, stranded headings, and section fragmentation. Repair failed pages with meaningful local prose or caption changes, recompile, inspect the affected page and its neighbors, and finish with another complete page-by-page pass.
12. **Re-read as a reviewer.** Ask whether the boundary, novelty, mechanism, evidence, term definitions, and scope can be recovered in one pass.

## Run the mandatory rendered-PDF VLM gate

Use the procedure in `references/rendered-layout-audit.md` without sampling:

1. Compile the authoritative source with the official venue template.
2. Render every PDF page to an image at a resolution sufficient to read body text and captions.
3. Use a contact sheet only to locate global imbalance; it does not replace individual-page inspection.
4. Inspect every page image with a vision-capable model and record page-specific failures.
5. For each short terminal line or local hole, slightly expand or recast the responsible paragraph with scientifically useful content while preserving every fact, number, citation, claim, and definition.
6. For a large region below a figure or table caption, first make the caption more self-contained and informative. Keep the remaining caption-to-text separation within approximately one body-text line.
7. Recompile after each small repair group. Reinspect the changed page, both neighboring pages, and all displaced floats.
8. After local repairs pass, rerender and re-inspect every page of every submitted PDF. A previous image is invalid after reflow.

Do not report “no whitespace,” “balanced,” “submission-ready,” or an equivalent conclusion without this visual pass. If a vision-capable inspection path is unavailable, report that layout validation remains incomplete.

## Choose the correct output mode

### Draft

Produce finished prose and a short note listing assumptions that materially affect the content.

### Revise

Preserve the author’s scientific intent and facts. Return the revised text first. Summarize only material structural or claim changes.

### Review

Do not silently rewrite. Report:

- the paper’s current thesis and evidence chain;
- high-impact failures in narrative, claim support, logic, or style;
- exact locations and concise revisions;
- a score using `references/revision-and-review.md`.

### Final submission pass

Make only low-risk edits unless authorized to restructure. Verify data, citations, equations, notation, captions, page limits, and section granularity. Then apply the mandatory rendered-PDF VLM gate to every page, including references and separate submitted artifacts.

## Respect locked content

When the user locks a source, section, result, or layout:

- treat it as immutable;
- edit only explicitly authorized regions;
- compare the final artifact with the locked source;
- report every material change;
- never use prose polishing as permission to change a scientific claim.

## Completion standard

Do not call the manuscript finished until:

- the central contribution is identifiable without reconstructing it from module names;
- the problem boundary is explicit before the proposed solution;
- every technical term has an earlier hook and is defined before substantive use;
- every acronym is expanded exactly once at its first occurrence in each independent artifact, with no reset or repeated expansion between the abstract and main body;
- each section and paragraph continues a visible dependency chain;
- each main claim has visible evidence;
- the abstract and introduction are not caveat-led;
- the method explains rationale, not only operations;
- experiment prose interprets rather than inventories;
- limitations are concentrated and specific;
- authorial first person is rare and individually justified, while avoidable active transitive clauses have been rewritten passively;
- terminology and notation are stable;
- the bundled audit has been reviewed;
- every submitted PDF has been freshly rendered and every page has been inspected individually with a vision-capable model;
- no running-prose or caption paragraph ends with only one or two words, and terminal lines are visually near-full;
- every submitted page is visually full to the intended bottom boundary, with no avoidable blank region, short column, sparse final page, or poorly distributed float;
- the visible region below every figure or table caption is followed by running text within one body-text line;
- sections are organized into a small number of substantive units rather than many shallow subsections, mini-headings, or list-like fragments;
- all page-specific failures have been repaired and the final full-PDF VLM pass succeeds.
