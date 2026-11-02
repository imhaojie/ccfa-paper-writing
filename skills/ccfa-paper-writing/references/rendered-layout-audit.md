# Rendered-PDF VLM Layout Audit

## Contents

1. Purpose and scope
2. Hard visual gates
3. Rendering protocol
4. Page-by-page VLM inspection
5. Line-fullness gate
6. Page-occupancy and column-balance gate
7. Figure and table caption gate
8. Section-fragmentation gate
9. Repair order
10. Reflow loop
11. Audit record
12. Completion rule

## 1. Purpose and scope

Treat visual quality as a property of the compiled PDF, not of the source. LaTeX source length, compilation success, page count, box warnings, and extracted text cannot establish that a page is visually full or that its lines and floats are balanced.

Apply this audit whenever a PDF is supplied, a manuscript can be compiled, or the user requests polishing, final formatting, page filling, line filling, float adjustment, or submission readiness. Inspect every submitted artifact:

- main paper;
- references;
- supplementary material;
- reproducibility checklist;
- appendix or response PDF when separately submitted.

No page may be sampled or skipped. A contact sheet supports global comparison but never replaces individual-page inspection.

## 2. Hard visual gates

A page fails when any of the following is visible:

- a running-prose or caption paragraph ends with only one or two lexical words;
- a paragraph-final line leaves a conspicuously large unused span;
- a nonterminal prose line is short because of an avoidable forced break or malformed layout;
- a column stops materially above its neighbor or above the intended bottom boundary;
- a page contains an avoidable blank region inside the official text block;
- the final body, reference, or supplementary page is visibly sparse;
- a section heading is stranded at the bottom of a column;
- figure or table placement leaves a large accidental hole;
- the gap from the bottom of a caption to the following running text exceeds one body-text line;
- a page is visually fragmented by too many subsection, run-in, bold, or bullet-like mini-headings;
- a local repair merely transfers whitespace or a short line to another page.

Do not declare the artifact finished while any gate fails.

## 3. Rendering protocol

1. Identify the authoritative source and official venue template.
2. Compile the complete artifact from the authoritative source.
3. Confirm that citations, references, fonts, figures, and equations resolve.
4. Rasterize every page at a resolution high enough for body text and caption line endings to be legible. Use approximately 140--200 DPI for individual-page inspection.
5. Optionally create a lower-resolution contact sheet for global page-density comparison.
6. Preserve page numbers in filenames so every observation maps to an exact page.
7. Inspect the new images. Do not reuse images rendered before the latest text or float change.

If a vision-capable model or page-image inspection tool is unavailable, report that the visual gate remains incomplete. Do not substitute PDF text extraction or compilation logs.

## 4. Page-by-page VLM inspection

For every page image, instruct the vision-capable model to inspect the complete text block and answer:

1. Does content reach the intended bottom boundary?
2. Are two-column bottoms aligned within approximately one or two body-text lines?
3. Does any running-prose or caption paragraph end in only one or two words?
4. Does any paragraph-final line leave an obviously large unused width?
5. Is any heading stranded or separated from its paragraph?
6. Is any float surrounded by an accidental blank region?
7. Is the caption followed by running text within one body-text line?
8. Does the page read as a continuous argument, or is it fragmented into too many visual mini-sections?
9. Would a local prose or caption expansion fix the issue without changing facts?

Record an explicit pass or fail for each page. Name the column, paragraph, caption, or heading responsible for every failure.

## 5. Line-fullness gate

Normal justified body lines should visually occupy the complete column width. Inspect all running-prose and caption lines, with special attention to paragraph endings because LaTeX does not justify the final line.

Reject:

- one- or two-word terminal lines;
- terminal lines that occupy only a small part of the column;
- a short line caused by a manual break;
- a sparse contribution bullet or caption ending;
- a repair that adds words with no scientific function.

Repair the responsible paragraph through one of these operations:

1. add a short mechanism explanation;
2. make an implicit referent explicit;
3. clarify the comparison axis or protocol;
4. state a bounded implication supported by existing evidence;
5. replace a compressed parenthesis with grammatical prose;
6. recast the final sentence so its information wraps more evenly.

Preserve all numerical values, citations, definitions, technical names, and claim strength. Do not add filler, duplicate evidence, invent qualifications, force line breaks, alter fonts or margins, or use spacing commands.

## 6. Page-occupancy and column-balance gate

Every page must appear deliberately filled to the official bottom boundary. In two-column layouts, target column bottoms within one or two body-text lines.

Inspect especially:

- the page before and after a full-width figure or table;
- the page where a major section starts;
- the last body page;
- the bibliography transition;
- the last reference page;
- float-only supplementary pages;
- pages affected by `\clearpage`, `\newpage`, or float barriers.

Repair occupancy by adding or improving scientifically useful content in the exact region causing the hole. Preferred material includes mechanism interpretation, protocol details required for reproducibility, a sharper comparison explanation, a failure-mode mechanism, or a self-contained caption. Recompile immediately because one added phrase can move floats or paragraphs across pages.

Do not manipulate page geometry, font size, baseline spacing, column spacing, global looseness, or hidden content. Do not add irrelevant citations to fill a reference page.

## 7. Figure and table caption gate

A caption is part of the scientific argument. It should state:

- what is shown;
- the comparison or experimental protocol;
- how rows, columns, colors, symbols, or panels are read;
- the metric or aggregation when necessary;
- the bounded takeaway that the figure or table directly supports.

The visible gap between the bottom of the caption and the next running paragraph must not exceed one body-text line. When a large region appears:

1. expand the caption first with missing self-contained information;
2. keep the added statement factual and supported by the displayed artifact;
3. revise the immediately adjacent explanation if the caption is already complete;
4. adjust float placement only through options permitted by the official template;
5. re-render the page and its neighbors.

Never fill the region with a duplicated result, an unsupported interpretation, manual `\vspace`, negative spacing, font scaling, or template modification.

## 8. Section-fragmentation gate

Count both semantic and visual subdivisions.

- Use two to four substantive subsections per major section by default.
- Permit five only in Method or Experiments when every subsection answers a distinct scientific question.
- Avoid `\subsubsection` in a short conference paper.
- Avoid sequences of `\paragraph{}`, bold run-in labels, or one-paragraph mini-sections.
- Avoid consecutive short bullets that make the manuscript resemble a technical report.

The VLM pass must also judge the rendered rhythm. Even a formally legal hierarchy fails when a page is dominated by frequent headings with only a few lines beneath each. Merge units that inherit the same question, evidence, or implication.

## 9. Repair order

Apply repairs in this order:

1. remove unnecessary fragmentation and merge related mini-sections;
2. expand or recast the exact paragraph with a sparse ending;
3. improve the scientific completeness of a caption;
4. add missing mechanism, protocol, or interpretation to the responsible local passage;
5. reflow existing prose without changing its claim;
6. reposition a float within venue rules;
7. if no content-preserving repair exists, report the unresolved failure and do not mark the layout complete.

Prefer a small local edit. Do not broadly rewrite a stable page merely to move one line.

## 10. Reflow loop

For each repair group:

1. edit only the identified source region;
2. compile the complete PDF;
3. check build diagnostics;
4. rasterize the changed PDF again;
5. inspect the affected page;
6. inspect the preceding and following pages;
7. inspect every float whose position changed;
8. confirm that no blank region or short line was transferred elsewhere.

After all local failures are repaired, rasterize and inspect every page again. The final global pass is mandatory because page flow is coupled.

## 11. Audit record

Use a concise page ledger:

| Artifact | Page | Line fullness | Bottom occupancy | Column balance | Caption gap | Fragmentation | Action | Final status |
|---|---:|---|---|---|---|---|---|---|
| Main | 1 | pass/fail | pass/fail | pass/fail | pass/fail/N/A | pass/fail | exact local repair | pass/fail |

Do not expose unnecessary internal reasoning. Report the exact pages changed, the type of repair, and whether the final complete pass succeeded.

## 12. Completion rule

Call the layout complete only when:

- every current PDF page has been inspected by a vision-capable model;
- every ledger row passes;
- each running-prose and caption ending is visually near-full;
- every page reaches the intended bottom boundary;
- two-column bottoms are acceptably aligned;
- caption-to-text gaps stay within one body-text line;
- no page is fragmented into excessive shallow units;
- no repair changed facts, evidence, citations, numerical values, or venue formatting.

If any item is unavailable or unresolved, state that the visual layout is not yet fully validated.
