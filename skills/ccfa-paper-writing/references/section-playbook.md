# Section Playbook for CCF-A AI Papers

## Contents

0. Global section hierarchy
1. Title
2. Abstract
3. Introduction
4. Related work
5. Problem setup and method
6. Experiments
7. Discussion and limitations
8. Conclusion
9. Figures, tables, and captions
10. Contribution statements

## 0. Global section hierarchy

Keep the hierarchy shallow enough that the paper reads as a continuous argument rather than a technical report assembled from small points.

- Keep a major section at two to four substantive subsections by default.
- Allow five subsections only in Method or Experiments when every subsection answers a distinct scientific question.
- Do not use `\subsubsection` in a short conference main paper.
- Use no more than three `\paragraph{}` or bold run-in mini-headings inside one subsection, and retain them only for substantial multi-sentence units.
- Keep the Introduction and Conclusion continuous rather than subdivided.
- Organize Related Work around no more than three conceptual themes.
- Do not create a heading for a single sentence, implementation setting, table pointer, or isolated score.
- Merge adjacent headings whenever a topic sentence and a logical bridge can express the relation more clearly.

## 1. Title

Make the title communicate the scientific idea, not the module inventory.

Prefer:

```text
[Core mechanism] for [task or setting]
```

or:

```text
[Conceptual distinction]: [Method or task]
```

Avoid:

- three acronyms joined by plus signs;
- “A Novel Framework for…” without the novelty;
- claims such as “Universal,” “Robust,” or “Efficient” without broad evidence;
- title punctuation that creates two unrelated promises.

## 2. Abstract

### 2.1 Function

The abstract is a compressed argument, not a miniature technical report.

Use six rhetorical moves:

1. **Bounded task and stakes:** one sentence naming the setting in which the claim holds.
2. **Specific failure inside that boundary:** one sentence.
3. **Core insight:** one sentence.
4. **Mechanism:** one or two sentences.
5. **Decisive evidence:** one or two sentences.
6. **Scientific implication:** one sentence.

The exact sentence count may vary. Preserve this dependency order.

### 2.2 Data discipline

- Use at most two or three headline quantitative facts.
- Select the result that best demonstrates the central claim.
- Do not list all datasets and both metrics unless the venue or task requires it.
- Do not report implementation settings, seeds, thresholds, or compute in the abstract unless they are the contribution.

### 2.3 Language discipline

- No citations.
- No contribution bullets.
- Keep acronym definitions to those needed for the compressed argument. Each first occurrence uses `Full Term (ACR)`, and every acronym defined here remains abbreviated throughout the main body.
- Avoid `VS`, slash-separated score pairs, and strings of module names.
- Avoid authorial first person unless a specific authorial decision cannot be expressed as clearly without it.
- Use passive constructions for transitive contribution, method, experiment, and result statements.
- Avoid caveat-led endings.
- End with what the evidence teaches, not “extensive experiments demonstrate effectiveness.”

### 2.4 Abstract test

After reading only the abstract, a reviewer should answer:

- What failure is being solved?
- Under which setting and assumptions is the problem defined?
- What is the central idea?
- Why should it work?
- What evidence is decisive?
- What broader lesson follows?

## 3. Introduction

### 3.1 Recommended paragraph sequence

**Paragraph 1 — Task and current strength.** Establish why the problem matters and what current systems already do well.

**Paragraph 2 — Problem boundary and precise unresolved failure.** Define the target, evidence, output unit, setting, and closest confusable task. Then expose the contradiction, blind spot, or failure mechanism inside that boundary.

**Paragraph 3 — Insight and design requirements.** Introduce the observation that resolves the failure. Derive two or three requirements before naming any method, module, or acronym. These requirements become the hooks for the method overview.

**Paragraph 4 — Method overview.** Explain how the proposed method satisfies those requirements. Name each component only after its functional role has been hooked. Keep the unifying mechanism visible.

**Paragraph 5 — Evidence preview.** State the strongest result and the diagnostic evidence that tests the explanation.

**Contribution list — Three items by default.** A fourth item is permitted only when it represents an independent scientific contribution rather than an implementation detail. Each item states a contribution, its mechanism or evidence, and its value.

### 3.2 Research gap

A gap is not “nobody used feature X.” A useful gap explains:

- what existing systems optimize;
- what information they therefore miss or misuse;
- which observed failure follows;
- why a new design principle is needed.

### 3.3 Novelty

Describe novelty relationally:

> Motion is injected as another feature stream by existing fusion methods. In the proposed design, audio is instead used to select motion before query initialization.

Avoid “To the best of our knowledge” unless the novelty search is recent and comprehensive.

### 3.4 Contribution bullets

Use this internal template:

```text
Problem or missing capability → proposed idea → mechanism → demonstrated value
```

Do not write:

1. We propose Module A.
2. We propose Module B.
3. Experiments show effectiveness.

The first two are implementation inventory; the third is expected, not a scientific contribution.

## 4. Related work

### 4.1 Organize by scientific axis

Group prior work by:

- assumption;
- information source;
- coupling mechanism;
- supervision;
- failure mode;
- evaluation setting.

Do not list papers chronologically unless history itself matters.

### 4.2 Cluster paragraph

Use:

1. category thesis;
2. representative approaches;
3. shared strength;
4. shared limitation relevant to this paper;
5. precise distinction of the proposed work.

Do not attack prior work. Show how its design goal differs.

### 4.3 Citation style

Integrate citations grammatically. Do not begin a sentence with `[12]` or `\cite{...}`. Avoid one citation per sentence when several works support the same category claim.

### 4.4 Related-work table

Use a table only when several methods can be compared along stable, meaningful axes. Do not use checkmarks for vague properties or criteria chosen solely to make the proposed method dominate.

## 5. Problem setup and method

### 5.1 Begin with the contract

Define:

- target task and closest adjacent formulation;
- inputs and outputs;
- prediction unit and granularity;
- operating setting and supervision regime;
- essential notation;
- assumptions required by the method.
- empirical and claim scope inherited from the introduction.

Do not front-load every symbol. Introduce notation near first use, but only after the represented quantity has been explained in words.

### 5.2 Overview before details

The overview explains:

- the diagnosed failure;
- the information flow;
- each component’s scientific role;
- where the proposed behavior enters the pipeline.

The architecture figure should make this logic visible.

Use dependency order:

```text
failure → requirement → functional operation → module name → symbol → downstream use
```

No module or symbol may appear before its failure, requirement, or represented quantity has been established.

### 5.3 Module paragraph

For each component, answer:

1. What failure does it address?
2. What does it compute?
3. Why does that computation address the failure?
4. What information does it pass downstream?
5. What happens in the weak-evidence or boundary case?

Do not write a sequence of tensor operations without rationale.

### 5.4 Equations

Before an equation, state its purpose. After it:

- define new symbols;
- interpret the operation;
- explain the design consequence.

Punctuate the equation according to its sentence role. Never leave an equation as an unexplained artifact.

### 5.5 Architecture names

Use acronyms to reduce repetition, not to manufacture novelty. Introduce only names that recur and refer to stable concepts.

Hook the function before the name:

> Audio consistency must be established before motion is allowed to guide localization. For this purpose, Spectral--Kinematic Alignment (SKA) is introduced.

If SKA was already expanded in the abstract, write only `SKA` here and in every subsequent section. Do not restart acronym definitions at the Introduction or Method.

## 6. Experiments

### 6.1 Evidence map

Map each research question to evidence:

| Question | Minimum evidence |
|---|---|
| Does the method improve the task? | Main benchmark comparison |
| Which component contributes? | Matched ablation |
| Is the proposed mechanism responsible? | Intervention or representation diagnostic |
| Is the gain a capacity artifact? | Capacity- or compute-matched control |
| Where does the effect enter? | Intermediate metric or visualization |
| When does it work or fail? | Stratified analysis and failure cases |
| Is the result stable? | Multiple seeds, uncertainty, or paired statistics |
| What does it cost? | Parameters, FLOPs, latency, and deployment assumptions |

Do not add experiments only to increase table count. Each experiment must close a claim.

### 6.2 Experimental setup

Report:

- datasets and official splits;
- metrics and aggregation;
- baselines and fairness controls;
- training budget and selection policy;
- hardware and software when relevant;
- seeds and uncertainty;
- test-time augmentation, ensembling, and preprocessing;
- public code/data status when claimed.

Separate validation choices from test evaluation.

### 6.3 Results paragraph

Use:

1. **Finding:** answer the subsection question.
2. **Evidence:** cite the decisive values or trend.
3. **Interpretation:** explain why the result occurs.
4. **Boundary:** state an exception only if it changes the conclusion.
5. **Bridge:** connect to the next experiment.

Example:

> The improvement is attributed to audio-conditioned selection rather than generic fusion capacity. A 2.2-point Jaccard advantage over the strongest capacity-matched alternative is obtained by SKA on MS3. Because the same modalities and comparable parameter counts are provided to both models, the spatial selection mechanism is isolated by the difference. Dependence on matched audio–motion correspondence is tested next.

### 6.4 Do not narrate tables

Avoid:

> Method A obtains 71.2, Method B obtains 72.3, and our method obtains 73.5. On F-score, the values are…

Prefer:

> The strongest baseline is exceeded by 1.2 Jaccard points, with the largest margin observed in multi-source scenes.

Use the table for the rest.

### 6.5 Ablations

Use matched configurations. Name each configuration clearly. Attribute gains only when the comparison isolates the claimed factor.

Avoid “each module is effective” as the sole interpretation. Explain how the progression matches the proposed mechanism.

### 6.6 Failure cases

Show representative failures, identify their mechanism, and delimit the affected regime. Do not begin with “our method is not perfect.” Do not promise generic future work.

## 7. Discussion and limitations

### 7.1 Discussion

Synthesize across experiments:

- what mechanism best explains the evidence;
- which alternative explanations were ruled out;
- which were not;
- what principle generalizes beyond the implementation.

Do not repeat results section by section.

### 7.2 Limitations

Prioritize limits that:

- change interpretation;
- define the deployment boundary;
- expose a missing signal or assumption;
- identify an important untested generalization.

Use mechanism-based limits, not generic humility.

## 8. Conclusion

Use one compact paragraph:

1. restate the bounded problem and idea;
2. summarize the mechanism;
3. state the strongest empirical conclusion within the evaluated scope;
4. state the broader design principle.

Do not:

- repeat the abstract sentence for sentence;
- list every module and dataset;
- add new claims;
- end with a defensive caveat;
- append a generic “future work will improve performance.”

## 9. Figures, tables, and captions

### 9.1 Figures

- Use vector graphics when possible.
- Make the reading order explicit.
- Use consistent notation, colors, and typography.
- Avoid decorative boxes that do not encode structure.
- Ensure labels remain legible at final print size.

### 9.2 Tables

- Put the comparison question in the caption.
- Separate incomparable protocols.
- State whether values are means, best runs, or single checkpoints.
- Mark best values consistently and avoid visual clutter.
- Do not overload a table with every diagnostic if grouping improves comprehension.

### 9.3 Captions

A caption should identify:

- what is shown;
- the comparison or protocol;
- how to read colors, rows, or columns;
- the main purpose, without claiming more than the figure supports.

Captions and table notes share the main artifact's acronym ledger. Use only the acronym if it has already been expanded in running text; if the first occurrence truly falls in a caption, define it there and use only the acronym afterward.

Inspect captions in the rendered PDF with a vision-capable model. The following running text must begin within one body-text line below the caption. If a larger blank region remains, first make the caption more self-contained by adding missing protocol, reading-key, metric, or bounded-takeaway information. Recompile and inspect the affected page and its neighbors; do not use manual spacing commands or template changes.

## 10. Contribution statements

A contribution is one of:

- a new scientific formulation or problem diagnosis;
- a mechanism or method that realizes a new capability;
- an evaluation protocol or dataset that reveals behavior unavailable from standard metrics;
- a substantive empirical finding or design principle.

Implementation details are not independent contributions unless they enable a new capability and are technically nontrivial.

Before finalizing a contribution, ask:

- Is it specific?
- Is it distinguishable from prior work?
- Is it supported later in the paper?
- Does it explain value, not only existence?
- Could a reviewer map it to an experiment or formal result?
- Is its key terminology hooked and defined earlier?
- Is unnecessary authorial first person avoided, and is the preferred passive construction used?
