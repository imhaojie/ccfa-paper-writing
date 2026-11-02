# CCF-A AI Paper Writing Standard

## Contents

1. Authorial posture
2. Narrative architecture and problem boundary
3. Claim and evidence calibration
4. Anti-defensive writing
5. Paragraph, terminology, and logical cohesion
6. Sentence-level standards and passive voice
7. Parentheses, acronyms, numbers, and comparisons
8. Technical presentation
9. Necessary limitations
10. Source synthesis and conflict decisions

## 1. Authorial posture

Write with calm authority. The paper earns confidence through a precise problem, a coherent mechanism, and decisive evidence. It does not earn confidence through adjectives, apology, reviewer flattery, or exhaustive qualification.

The default unit of scientific prose is:

```text
claim → reason or mechanism → evidence → implication
```

Prefer:

> Object-hypothesis initialization is altered by audio-conditioned motion, and the effect is observed before mask decoding.

Avoid:

> It is worth noting that our method may potentially have some effect on query initialization.

The first sentence states a testable point. The second spends words protecting an undefined possibility.

## 2. Narrative architecture and problem boundary

### 2.1 Paper-level dependency graph

Every major section must answer a question created by the preceding section:

1. Why does the task matter?
2. What exact problem is being solved, and where is its boundary?
3. What specific failure remains inside that boundary?
4. Why is that failure produced by current methods?
5. What design requirement follows?
6. How is the requirement satisfied by the proposed method?
7. Which experiment tests each part of the explanation?
8. What general principle survives beyond the benchmark?

The method must feel inevitable after the introduction. The experiments must feel necessary after the method.

### 2.2 Boundary contract

Before the solution is named, define:

- the target phenomenon or task;
- the available inputs and prediction output;
- the prediction unit and granularity;
- the operating setting and required assumptions;
- the closest adjacent task that could be confused with the formulation;
- the benchmark and protocol scope supporting the claims.

The boundary must be stated positively. The studied regime should be named directly instead of being surrounded by universal disclaimers. Use `problem-boundary-and-hooks.md` to build the complete boundary and term ledgers.

### 2.3 One central thesis

Express the paper’s thesis in one sentence containing:

- the target problem;
- the causal or structural diagnosis;
- the proposed idea;
- the principal benefit.

Module names are not a thesis. “Modules A, B, and C are proposed” describes inventory. Explain the unifying idea that makes A, B, and C necessary.

### 2.4 Scientific tension

Strong introductions expose a tension, not merely a missing component:

```text
Existing strength → corresponding blind spot → unresolved consequence
```

Example:

> Precise boundaries are recovered by strong appearance priors, but visually salient objects unrelated to the observed sound can also be favored.

This is stronger than “Existing methods do not use optical flow” because it explains why the omission matters.

### 2.5 Section granularity

Use the shallowest hierarchy that makes the argument recoverable in one pass. A major section should normally contain two to four substantive subsections. A fifth subsection is permitted only in Method or Experiments when it answers a distinct scientific question that cannot be integrated cleanly elsewhere.

Do not use `\subsubsection` in a short conference main paper. Do not recreate a third level through a sequence of `\paragraph{}` commands, bold run-in labels, or one-paragraph mini-sections. Within one subsection, use no more than three run-in mini-headings, and retain them only when each introduces a substantial multi-sentence unit.

The Introduction and Conclusion should normally remain unfragmented. Related Work should be organized around at most three conceptual themes rather than one heading per paper family. Contribution lists should normally contain three claims. Merge neighboring headings when they inherit the same question, use the same evidence, or can be connected by a topic sentence.

## 3. Claim and evidence calibration

### 3.1 Evidence ladder

| Evidence | Appropriate language | Inappropriate leap |
|---|---|---|
| A table reports a stable difference | improves, exceeds, reduces | proves the mechanism |
| Matched ablation isolates a component | attributes, isolates, shows the component contributes | proves universal necessity |
| Intervention breaks a correspondence | supports dependence on that correspondence | proves causal grounding in all settings |
| Multiple diagnostics agree | supports, narrows the explanation | guarantees |
| Qualitative examples illustrate behavior | illustrates, visualizes | demonstrates dataset-wide prevalence |
| Limited benchmark evidence | on these benchmarks, in this setting | generally, universally |

### 3.2 Claim ledger

Before polishing, record each important claim:

| ID | Claim | Direct evidence | Alternative explanation tested? | Scope | Wording |
|---|---|---|---|---|---|
| C1 | ... | Table/Figure/Eq. | yes/no | dataset and condition | shows/supports/suggests |

If a claim lacks direct evidence, either add evidence, narrow it, move it to a hypothesis, or remove it.

### 3.3 Comparative claims

Name the comparator and protocol. “State of the art” requires a complete and fair comparison under compatible settings. If settings differ, state the exact basis of comparison.

Prefer absolute percentage-point differences for bounded metrics. Use relative improvements only when the denominator and interpretation are useful.

## 4. Anti-defensive writing

### 4.1 Defensive patterns

Flag these patterns:

- repeated statements of what the paper does not claim;
- contribution paragraphs beginning with limitations;
- hedge stacks: “may potentially suggest,” “could possibly”;
- apology-like framing: “we acknowledge,” “we admit,” “unfortunately”;
- anticipatory rebuttal to objections not raised by the evidence;
- negative contribution statements: “our goal is not X but Y”;
- caveats repeated in the abstract, introduction, results, and conclusion;
- “to be clear,” “of course,” “it should be noted that”;
- claims weakened because the author fears criticism rather than because the evidence is uncertain.

### 4.2 Positive scope

Replace negative scope with the population or condition actually studied.

| Defensive | Claim-forward |
|---|---|
| We do not claim applicability to every architecture. | The design is evaluated on the VCT architecture. |
| This should not be interpreted as universal causal grounding. | Matched audio–motion correspondence is identified by the interventions as the operative signal in the tested setting. |
| Our goal is not to replace appearance features. | Appearance features are preserved, while competing hypotheses are verified with motion. |

### 4.3 Proper placement

- Put task scope in problem setup.
- Put data and protocol restrictions in experimental setup.
- Put failure modes and external-validity limits in limitations.
- Put a qualification next to a claim only when omitting it would make that sentence false.
- Do not place routine caveats in contribution bullets or the final sentence of the conclusion.

### 4.4 “Not X but Y”

Use contrast only when it carries the core conceptual distinction:

> Motion is treated as evidence to be verified, rather than as another feature stream.

Delete it when Y can stand alone:

> An audio-conditioned verification mechanism is identified.

## 5. Paragraph, terminology, and logical cohesion

### 5.1 One paragraph, one job

Label every paragraph with a private margin note:

- establish problem;
- identify failure;
- derive requirement;
- explain mechanism;
- report finding;
- interpret finding;
- delimit scope.

Split paragraphs with multiple unrelated labels. Merge paragraphs that repeat the same label without advancing it.

### 5.2 Topic sentence

The first sentence should normally state the paragraph’s answer, not announce its contents.

Prefer:

> The gain grows as source ambiguity increases.

Avoid:

> Table 4 presents results for scenes with different numbers of sources.

### 5.3 Logical hooks

Connect sentences through:

- repeated technical nouns;
- explicit referents such as “this spatial gate”;
- cause and consequence;
- comparison along the same axis;
- question and answer;
- general claim followed by specific evidence.

Apply a strict hook-before-term rule. Every technical concept, module, acronym, symbol, metric, dataset, and experimental intervention must be motivated or defined by earlier text before substantive use. A module name must be preceded by the failure or functional requirement that makes it necessary. A symbol must be preceded by the quantity that it represents.

Each paragraph must receive one concept from earlier text, advance it, and pass one consequence, requirement, or question forward. The next paragraph must pick up that element through exact terminology or an unambiguous noun phrase. A transition word alone does not create a hook.

Do not use transition words as decoration. Verify:

- **however / whereas / although / despite**: a real contrast or violated expectation exists;
- **therefore / thus / consequently**: the preceding statement logically entails or motivates the next;
- **because / since / due to**: the cause attaches to the correct proposition;
- **compared with**: both sides compare the same property at the same level.

### 5.4 Pronouns and participles

Replace ambiguous “this,” “it,” and “they” with the relevant noun.

Avoid introductory participial constructions when they encourage active voice or obscure agency. When one is retained, ensure that its understood subject matches the grammatical subject:

> When matched audio is used, unrelated motion is suppressed by the model.

Not:

> Using matched audio, unrelated motion is suppressed by the model.

## 6. Sentence-level standards and passive voice

### 6.1 Voice

Apply a passive-dominant house style. Minimize authorial first person throughout the manuscript, supplementary material, captions, and footnotes. Prefer impersonal or passive formulations to `we`, `our`, `us`, `ours`, and `ourselves`, but do not prohibit those forms.

Retain first person sparingly when it materially improves clarity, especially when an explicit authorial decision must be distinguished from model behavior, dataset properties, or empirical evidence. Do not retain it merely to announce routine actions such as proposing, evaluating, showing, or observing.

Use passive constructions for transitive contribution, method, experiment, and result statements:

> SKA is compared with capacity-matched fusion controls.

> Optical flow is precomputed with frozen RAFT.

> Audio-consistent motion is selected by the proposed alignment mechanism.

> A 2.2-point improvement is observed under the matched control.

Prefer an agentless passive when the actor is obvious. Use a `by` phrase only when the agent itself carries information. Copular, existential, and genuinely intransitive clauses may remain because no grammatical passive is available. Do not use this exception for an avoidable active transitive action.

Reject empty passive meta-framing such as “it is believed,” “it can be seen,” or “it should be noted.” Place the scientific object or evidence in subject position instead.

### 6.2 Verbs

Prefer specific verbs:

- uses, selects, aligns, constrains, initializes, suppresses;
- improves, reduces, preserves, isolates, exposes;
- shows, supports, indicates, suggests.

Avoid empty verbs plus nouns:

- “conducts an improvement of” → “improves”;
- “performs the calculation of” → “computes”;
- “provides an explanation of” → “explains.”

### 6.3 Modifiers

Delete intensifiers that evidence already supplies: significantly, substantially, remarkably, notably, highly. Keep them only when quantitatively defined or contrastively useful.

Avoid novelty adjectives as substitutes for novelty: novel, new, first, unprecedented. State the actual distinction.

### 6.4 Tense

- Use present tense for the paper’s argument, method behavior, equations, tables, and established knowledge.
- Use past tense for completed experimental actions when temporal completion matters.
- Use present perfect sparingly for a research trend extending to the present.
- Keep tense locally consistent.

### 6.5 Lexical consistency

Use one name for one concept. Do not alternate among method, approach, scheme, framework, and solution merely for elegance. Variation is useful for ordinary prose, not for technical identifiers.

Prefer familiar precise words over ornate synonyms. “Use” is often better than “exploit” or “resort to.”

## 7. Parentheses, acronyms, numbers, and comparisons

### 7.1 Parentheses

A parenthesis should contain optional information. If the content carries the argument, integrate it into the sentence.

Avoid:

> The method improves MS3 (the multi-source subset) by 5.9 points (73.50 VS 67.60) under the matched protocol (five seeds).

Prefer:

> Under the five-seed matched protocol, Jaccard on the multi-source subset is improved by 5.9 points, from 67.60 to 73.50.

Guideline: normally use at most one substantive parenthesis per sentence. Mathematical indices and citations do not count.

### 7.2 Acronyms

Define every acronym exactly once within each independently submitted or independently read artifact:

> To verify motion against the soundtrack, Spectral–Kinematic Alignment (SKA) is introduced. Motion is then selected by SKA using the audio representation.

At the first occurrence, use `Full Term (ACR)`. At every later occurrence, use only `ACR`. The abstract and main body are one continuous definition scope, so an acronym defined in the abstract must not be expanded again in the Introduction, Related Work, Method, captions, or table notes. A separately submitted supplement or checklist begins a new scope because it must be independently readable.

The functional need must be hooked before the name is given. Do not define several module names in one sentence. Do not repeat an expansion to remind the reader, at a section boundary, or to make a caption sound self-contained. If a shortened form is used only once, omit it and write the full term. Bibliographic titles, mathematical symbols, conventional units, and official identifiers that are not used as prose abbreviations are not treated as acronym definitions.

Maintain an acronym ledger with the full term, short form, first-definition location, and all later uses. Search the entire artifact after editing; any second occurrence of the full-term-plus-parenthetical pattern is an error.

### 7.3 Numbers

- Abstract: keep only decisive headline results; avoid a dataset-by-dataset ledger.
- Introduction: use one or two values to establish scale, then defer details.
- Experiments: use values that answer the subsection question.
- Discussion and conclusion: prefer the finding or implication unless one value is essential.

Never transcribe an entire table into prose.

### 7.4 Comparisons

Avoid `VS`, `vs.`, and slash notation in running prose.

Prefer:

> A 2.2-point Jaccard advantage over cross-attention is obtained by SKA.

Use tables for dense paired scores.

## 8. Technical presentation

- Do not cite references in the abstract.
- Do not begin a sentence with a bare citation.
- Define every acronym exactly once at first occurrence, then use only the acronym; never reset the definition state after the abstract.
- Establish a prior conceptual hook before every nonstandard term, acronym, module, symbol, metric, or dataset.
- Punctuate display equations as parts of sentences.
- Keep notation identical across prose, equations, figures, and tables.
- Use vector figures where possible and inspect them at high zoom.
- Write self-contained captions that state the comparison, protocol, and reading key.
- Avoid identical sentences across the abstract, introduction, and conclusion; keep the idea, change the rhetorical function.
- Use available page space for evidence, explanation, or readability, not padding.
- Treat a venue’s official template as authoritative over generic formatting preferences.

### 8.1 Rendered line fullness

The final line of each running-prose paragraph or caption is a visual quality gate. A terminal line containing only one or two words is forbidden. The preferred terminal line reaches the right margin or leaves no more than approximately one or two ordinary words of unused horizontal width.

Apply this rule to the compiled PDF, because source-code line lengths do not predict typeset wrapping. Repair a sparse ending with a small, meaningful rephrasing that preserves the claim, evidence, terminology, citations, and numerical values. Do not add filler, repeat a claim, invent a qualification, force a manual line break, hide text, alter margins or fonts, or use spacing commands merely to manipulate the line.

After each repair, recompile and inspect the affected page, its neighboring page, and any displaced floats. A local improvement is invalid if it creates a new sparse ending, column imbalance, or page-level blank region elsewhere.

### 8.2 Full-page occupancy and column balance

Every page in the submitted main paper, supplementary material, and references must appear deliberately full inside the venue’s official text block. Reject:

- a column that ends visibly above its neighbor;
- a large blank region below prose, a figure, or a table;
- a heading stranded at the bottom of a column;
- a sparse final content or reference page;
- a float-only page with poorly distributed tables or figures;
- manual page breaks that create unused space.

In a two-column layout, the two columns should normally terminate within approximately one or two body-text lines of each other and close to the template’s bottom boundary. Float-only pages should be packed or distributed so that their whitespace is visually balanced rather than appearing accidental.

Repair page occupancy in this order: improve scientifically useful explanation or interpretation, reflow existing prose, revise informative captions, reposition floats within venue rules, regroup short subsections, and rebalance material across adjacent pages. Never invent evidence, duplicate a claim, add empty transition prose, add irrelevant citations, shrink or enlarge fonts, alter margins, or manipulate vertical spacing merely to fill a page.

The entire PDF must be rendered again after each page-level repair. A page is not fixed when the same whitespace has merely moved elsewhere.

### 8.3 Mandatory VLM inspection and caption gaps

The rendered artifact must be inspected page by page with a vision-capable model. Compilation logs, source review, text extraction, page counts, and contact sheets are insufficient. Open every page at readable resolution and judge line endings, bottom occupancy, column balance, headings, floats, caption spacing, and visual fragmentation. After any reflow, render every page again; earlier page images are stale.

The visible gap between the bottom of a figure or table caption and the following running text must not exceed one body-text line. When a larger blank region is observed, expand the caption with useful self-contained information about the comparison, protocol, reading key, metric, or bounded takeaway. If the caption is already complete, revise the adjacent explanation or legal float placement. Do not alter template spacing or use manual vertical-space commands.

## 9. Necessary limitations

A strong limitation has four parts:

1. the condition;
2. the mechanism causing the limitation;
3. the observed consequence;
4. a plausible direction, only if technically grounded.

Example:

> When synchronous motion is exhibited by several semantically similar objects, little instance-level evidence is provided by the pooled audio token. A narrower gain is therefore observed in this regime, motivating temporally resolved or instance-conditioned audio representations.

Avoid apology and generic future work:

> Our method is not perfect, and more work is needed.

## 10. Source synthesis and conflict decisions

This standard synthesizes:

- Kiterlin, *Anti-Defensive Writing* (MIT): claim-forward prose, positive scope, precise hedging, and disciplined placement of limitations.
- Zhang Lin, *Information-Oriented English Scientific Writing* (2024-10-22): reviewer-aware completeness, paper-not-manual reasoning, section functions, experimental interpretation, logical hooks, and technical presentation.

Apply the following modern AI-conference resolutions:

- Apply passive voice as the preferred house style for transitive scientific actions, and minimize rather than prohibit authorial first person.
- Preserve copular, existential, and genuinely intransitive clauses when no grammatical passive exists.
- Replace synonym substitution for elegance with terminological consistency and plain precision.
- Fill every permitted page with evidence, explanation, protocol detail, or interpretation; never use padding to satisfy the page-fullness requirement.
- Replace indiscriminate transition-word use with verified logical relations.
- Preserve failure-case analysis, but present it as mechanism-based scope rather than apology.
