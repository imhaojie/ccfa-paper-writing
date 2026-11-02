# Revision and Review Protocol

## Contents

1. Revision modes
2. Full-paper workflow
3. Anti-defensive transformations
4. Review severity
5. Scorecard
6. Hard failure gates
7. Final submission checklist

## 1. Revision modes

### Structural rewrite

Use when the thesis is obscured, sections have the wrong function, or evidence appears before its motivating question.

Permit:

- reordering paragraphs and subsections;
- merging repetitive material;
- rewriting contribution framing;
- moving limitations;
- selecting fewer, stronger results for the abstract.

Do not alter facts.

### Prose polish

Use when structure is sound. Improve:

- topic sentences;
- logical hooks;
- directness;
- sentence length;
- parenthetical density;
- terminology;
- data presentation.

Do not introduce new scientific claims.

### Locked-layout micro-edit

Use when page count and line breaks are sensitive. Make minimal lexical changes, compile after each small group, and visually inspect affected pages.

### Review only

Diagnose without changing files. Give evidence, severity, and a concrete revision direction.

## 2. Full-paper workflow

### Step 1: Inventory authoritative sources

Record:

- locked manuscript source;
- latest experiment ledger;
- official dataset and metric definitions;
- figure and table source;
- venue template;
- code/configuration source.

Resolve disagreements before rewriting.

### Step 2: Recover the thesis

Write one sentence each for:

- task;
- problem boundary;
- unresolved failure;
- cause of failure;
- core idea;
- mechanism;
- strongest evidence;
- scope.

If any sentence is unavailable, the manuscript has a narrative or evidence gap.

### Step 3: Lock the problem boundary

Record:

- target phenomenon or task;
- available inputs and prediction output;
- prediction unit and granularity;
- operating setting and required assumptions;
- closest adjacent task;
- empirical scope;
- maximum supported claim.

Check that the abstract, introduction, problem setup, experiments, and conclusion express compatible versions of this boundary.

### Step 4: Build the term dependency ledger

For every technical concept, module, acronym, symbol, metric, dataset, and intervention, record:

- its earlier conceptual hook;
- its first and only definition;
- its required later form;
- prerequisite terms;
- first substantive use.

Move or rewrite any item whose hook is empty or whose first use precedes its definition. For acronyms, audit the abstract and main body as one scope and remove every repeated expansion from later sections, captions, and table notes. Treat a separately submitted supplement or checklist as a new self-contained scope. Sort dependent terms topologically.

### Step 5: Build a section map

For each section, state:

- the question it answers;
- the evidence or reasoning it contains;
- the question it creates next.
- the exact term or concept passed to the following section.

Delete content that does not advance this chain.

#### Section-granularity gate

- Keep each major section at two to four substantive subsections by default.
- Permit a fifth subsection only in Method or Experiments when it answers a distinct scientific question and contains enough material to justify separation.
- Do not use `\subsubsection` in a short conference main paper.
- Do not replace third-level headings with many `\paragraph{}` commands or bold run-in labels; use at most three run-in mini-headings within one subsection.
- Do not create a heading for one sentence, one implementation detail, one table reference, or one isolated result.
- Merge adjacent units that share the same inherited question, evidence, or implication.
- Keep the Introduction and Conclusion unfragmented unless the venue or paper length clearly requires otherwise.
- Organize Related Work by at most three conceptual themes rather than by individual methods.

### Step 6: Build the claim–evidence ledger

Check every abstract, contribution, introduction, result, and conclusion claim against a table, figure, equation, citation, or explicit reasoning chain.

### Step 7: Rewrite by dependency

Fix in this order:

1. problem boundary;
2. thesis;
3. term dependency order;
4. section order and handoffs;
5. paragraph jobs and hooks;
6. claim calibration;
7. passive voice and sentence logic;
8. wording;
9. layout.

Do not polish sentences that may be deleted or moved.

### Step 8: Run deterministic audits

Run:

```bash
python3 scripts/audit_prose.py path/to/paper.tex
```

Review every high-severity finding and sample medium findings. Treat authorial first person as a low-severity preference prompt: retain it when clarity is improved, and revise it when the occurrence is routine or repetitive. Review active-voice findings manually because only obvious transitive constructions can be detected reliably. Ignore false positives only after explaining why the original construction is necessary.

### Step 9: Validate artifacts

For LaTeX:

- compile from a clean directory;
- check undefined references and citations;
- check overfull boxes;
- inspect embedded fonts;
- render every page and apply the mandatory page-by-page VLM protocol in `rendered-layout-audit.md`;
- compare locked content;
- verify tables against the experiment ledger.

Compilation logs, extracted text, page counts, and contact sheets do not replace individual-page visual inspection. Every submitted page must be opened at readable resolution and judged by a vision-capable model. Record page-specific pass or fail status for line fullness, bottom occupancy, column balance, float placement, caption-to-text gaps, and visual section fragmentation.

#### Rendered line-fullness gate

Inspect the actual PDF rather than the `.tex` line lengths.

- Apply the gate to running prose, contribution bullets, limitations, conclusions, and figure or table captions in both the main paper and supplementary material.
- Reject any paragraph-final line containing only one or two lexical words.
- Prefer a near-full terminal line that reaches the right margin or leaves no more than approximately the width of one or two ordinary words.
- Exempt section headings, display equations, table cells, algorithms, bibliography entries, and intentionally short figure labels.
- Repair the prose first: add or remove a few scientifically useful words, recast the clause, or redistribute a sentence while preserving the paragraph’s rhetorical job.
- Merge or split a paragraph only when the resulting paragraph structure remains logically justified.
- Preserve all numbers, citations, technical definitions, claims, and locked wording.
- Do not use padding, redundant evidence, defensive qualifications, manual line breaks, invisible text, `\hspace`, `\vspace`, font scaling, margin changes, or global looseness as a workaround.
- Recompile after every small group of edits. Inspect the affected page, adjacent pages, column bottoms, and displaced floats; then perform a final pass over every page.

#### Full-page occupancy gate

Render and inspect every page of the main paper, supplementary material, and references at the final template size.

- Reject any avoidable blank region inside the official text block.
- Reject a two-column page whose columns end at visibly different heights; target a difference of no more than approximately one or two body-text lines.
- Reject a page whose content stops materially above the prescribed bottom boundary.
- Reject a sparse final page, an isolated heading at a column bottom, and a float-only page with large accidental gaps.
- Check the page before and after every full-width figure, table, `\clearpage`, bibliography boundary, and supplementary float block.
- Fill space only with scientifically useful evidence, explanation, implementation detail, protocol information, interpretation, or a more informative caption.
- Prefer reflowing and regrouping existing material before adding new prose.
- Reposition floats only within the venue’s permitted placement rules.
- Do not add filler, duplicate claims or numbers, invent citations, alter page geometry, change fonts, compress figures unnaturally, or use manual vertical-spacing tricks.
- After every change, rerender the complete PDF. A repair fails if it transfers the blank region, creates a new short terminal line, changes a locked result, or fragments the section structure.

#### Caption-to-text gap gate

- Inspect the visible region below every figure and table caption.
- Keep the caption-to-running-text gap within one body-text line.
- When a larger hole is visible, first expand the caption with missing comparison, protocol, reading-key, metric, or bounded-takeaway information.
- If the caption is already self-contained, improve the adjacent scientific explanation or reposition the float within official venue rules.
- Never use `\vspace`, negative spacing, font scaling, margin changes, or duplicated claims to close the gap.
- Recompile and inspect the page, its neighbors, and every displaced float.

## 3. Anti-defensive transformations

### 3.1 Disclaimer to positive claim

Before:

> We do not attempt to build a general theory of multimodal grounding.

After:

> Source ambiguity in vision-centric segmentation is studied through audio-conditioned motion.

### 3.2 Hedge stack to evidence scope

Before:

> These results may potentially suggest that the module could improve grounding.

After:

> The role of the module in audio grounding on MS3 is supported by the matched interventions.

### 3.3 Caveat-led result to finding-led result

Before:

> Although the benchmark is limited, it is worth noting that our model still achieves a 5.9-point improvement.

After:

> Jaccard is improved by 5.9 points on MS3. The evaluation remains limited to the AVSBench family.

### 3.4 Table narration to interpretation

Before:

> VCT obtains 67.60, SKA obtains 70.45, SKA+MPQG obtains 72.65, and the full model obtains 73.50.

After:

> Most of the gain is obtained before boundary refinement: 5.05 of the final 5.90 Jaccard points are contributed by SKA and MPQG.

### 3.5 Module inventory to scientific role

Before:

> We introduce SKA, MPQG, and BRM.

After:

> Motion is first verified against the soundtrack by the framework. The verified response is then used to initialize object hypotheses while appearance cues are preserved; boundary refinement is applied only after localization.

### 3.6 Parenthetical report to grammatical prose

Before:

> Our method performs best on MS3 (73.50 VS 67.60, +5.90).

After:

> On MS3, Jaccard is improved from 67.60 to 73.50, and a 5.90-point gain over VCT is obtained.

### 3.7 Unhooked term to dependency-ordered introduction

Before:

> MPQG uses the resonance map to initialize queries.

After:

> Localization must be influenced by verified motion before mask decoding. Accordingly, object-query initialization is conditioned on the previously defined resonance map. This operation is implemented by the Motion-Prompted Query Generator (MPQG).

### 3.8 First person and active voice to passive house style

Before:

> We evaluate our method on AVSBench, and our model outperforms VCT by 5.9 points.

After:

> The proposed method is evaluated on AVSBench, where VCT is exceeded by 5.9 points.

## 4. Review severity

### Critical

- numerical contradiction;
- unsupported headline claim;
- wrong experimental protocol;
- broken anonymity;
- missing citation for a central borrowed idea;
- invalid logical or causal conclusion;
- source and PDF mismatch.

### Major

- problem boundary is absent, inconsistent, or broader than the evidence;
- a method component has no earlier failure or design requirement;
- dependent concepts are introduced out of order;
- central terminology is used before it is defined;
- thesis obscured by module inventory;
- research gap is only “feature X has not been used”;
- experiments do not test the proposed mechanism;
- related work is a paper list;
- results are data narration without interpretation;
- limitations dominate high-impact sections;
- comparison is unfair or underspecified.

### Minor

- undefined or repeatedly expanded acronym;
- local technical term lacks an earlier hook;
- authorial first person is routine, repetitive, or unnecessary;
- an avoidable active transitive clause violates the passive house style;
- excessive parentheses;
- prose `VS`;
- vague pronoun;
- weak topic sentence;
- repeated sentence;
- ornamental transition;
- inconsistent notation or tense.

## 5. Scorecard

Score out of 100.

| Dimension | Points | Full-credit standard |
|---|---:|---|
| Problem boundary, thesis, and narrative | 20 | Explicit scope and one coherent problem–mechanism–evidence chain |
| Claim–evidence alignment | 20 | Every main claim is supported and calibrated |
| Section function and dependency | 15 | Each section answers the inherited question and passes one forward |
| Term order and paragraph cohesion | 15 | Terms are hooked before use; one connected job is performed per paragraph |
| Method rationale | 10 | Design choices are motivated and interpreted |
| Experimental reasoning | 10 | Controls test claims; prose explains findings |
| Directness and anti-defensiveness | 5 | Claim-forward with necessary limits only |
| Language and technical presentation | 5 | Passive-dominant style, restrained first person, clear terminology, notation, captions, and formatting |

Interpretation:

- **90–100:** submission-ready prose and argument;
- **80–89:** strong, with localized revision needed;
- **70–79:** readable but contains a major narrative or evidence weakness;
- **below 70:** substantial restructuring required.

A hard failure gate overrides the numeric score.

## 6. Hard failure gates

Do not call the paper ready if any remains:

- the problem boundary is missing or inconsistent across sections;
- a central method term is introduced before its motivating requirement;
- a central technical term, symbol, metric, or dataset is used before definition;
- avoidable active transitive constructions remain in contribution, method, experiment, or result statements;
- a main result differs across abstract, table, and conclusion;
- a central acronym or metric is undefined;
- “state of the art” is asserted without comparable evidence;
- a causal verb exceeds the experiment design;
- the method is described without its rationale;
- the experiment section contains tables but no interpretation;
- the conclusion introduces a new claim;
- the final PDF has clipping, overflow, broken figures, or unresolved references;
- a running-prose or caption paragraph ends with only one or two words, or has a clearly avoidable sparse terminal line in the rendered PDF;
- any submitted page contains an avoidable blank region, a materially short column, a sparse final page, an isolated heading, or visibly unbalanced float placement;
- any figure or table caption is followed by more than one body-text line of whitespace before running prose;
- any current PDF page was not individually inspected with a vision-capable model after the final reflow;
- a major section is fragmented into more than four subsections without a justified Method or Experiments exception, or third-level and run-in headings are used as a list of small points;
- locked content changed without authorization.

## 7. Final submission checklist

### Narrative

- [ ] The title expresses the idea.
- [ ] The abstract contains one bounded task, one failure, one idea, one mechanism, decisive evidence, and one implication.
- [ ] The introduction defines the scientific boundary and derives the method from the failure.
- [ ] The formal problem setup defines inputs, output unit, assumptions, and the closest adjacent task.
- [ ] Contribution bullets describe scientific value.
- [ ] The conclusion states a principle, not a module list.
- [ ] Major sections normally contain two to four substantive subsections; only a justified Method or Experiments section contains five.
- [ ] No short main-paper section is fragmented by `\subsubsection`, excessive `\paragraph{}` headings, bold mini-headings, or one-point subsections.
- [ ] The Introduction and Conclusion remain coherent continuous sections, and Related Work uses no more than three conceptual themes.

### Dependency and terminology

- [ ] Every section answers a question created earlier and passes one question or concept forward.
- [ ] Every paragraph receives an earlier concept and passes one forward.
- [ ] Every component is preceded by the failure or requirement that motivates it.
- [ ] Every technical term has an earlier conceptual hook.
- [ ] Every acronym is expanded exactly once at its first occurrence in each independent artifact; the ledger is not reset after the abstract.
- [ ] Every symbol, metric, dataset, and intervention is defined before substantive use.
- [ ] Terminology follows a topologically valid dependency order.

### Evidence

- [ ] Every headline number matches the authoritative result source.
- [ ] Every component claim maps to an ablation or diagnostic.
- [ ] Alternative explanations are tested where claimed.
- [ ] Multiple runs and uncertainty are stated when available.
- [ ] Limitations match observed failure modes.

### Style

- [ ] `We`, `our`, `us`, and other authorial first person have been minimized; each retained occurrence serves clarity.
- [ ] Transitive contribution, method, experiment, and result statements use passive constructions.
- [ ] No empty passive meta-framing has been introduced.
- [ ] No unnecessary disclaimers in the abstract or contributions.
- [ ] No hedge stacks.
- [ ] No prose `VS`.
- [ ] No table-cell recitation.
- [ ] Parentheses contain only auxiliary information.
- [ ] Technical terms remain consistent.
- [ ] Causal and contrast transitions are logically valid.

### Presentation

- [ ] Acronyms are written as `Full Term (ACR)` at first occurrence and only as `ACR` afterward, including across the abstract-to-Introduction boundary.
- [ ] Symbols are defined once.
- [ ] Equations are punctuated and interpreted.
- [ ] Captions are self-contained.
- [ ] Figures remain sharp and legible.
- [ ] Every page has been rendered and visually inspected at the final template size.
- [ ] Every current page image has been inspected individually with a vision-capable model; no page was accepted from a contact sheet alone.
- [ ] No running-prose, contribution-bullet, or caption paragraph ends with only one or two words.
- [ ] Paragraph-final lines are near-full and leave at most about one or two ordinary words of unused width whenever a fact-preserving revision can achieve it.
- [ ] Line-fullness repairs contain no filler, repeated claims, unsupported qualifications, or typographic tricks.
- [ ] Fixing a line has not created a new sparse ending, float displacement, column imbalance, or page-level blank region.
- [ ] Every submitted main-paper, supplementary, and reference page is visually full within the official text block.
- [ ] Two-column bottoms are nearly aligned, normally within one or two body-text lines.
- [ ] No sparse final page, isolated bottom-of-column heading, large accidental gap, or poorly distributed float-only page remains.
- [ ] The gap below every figure or table caption and before the next running text is no more than one body-text line.
- [ ] Page-filling revisions add only useful scientific content or improve reflow; no filler, duplicated claim, irrelevant citation, geometry change, or spacing trick has been used.
- [ ] Citations and references resolve.
- [ ] The PDF obeys the venue template and page policy.
- [ ] The manuscript and supplementary material compile independently when required.
