# Problem Boundary and Hook Discipline

## Contents

1. Boundary contract
2. Boundary layers
3. Problem-to-solution chain
4. Term dependency order
5. Section and paragraph hooks
6. Passive-voice house style
7. Diagnostic examples
8. Final audit

## 1. Boundary contract

Define the problem before the method is named. A complete boundary contract states:

1. **Target:** the exact phenomenon, task, or failure being studied.
2. **Available evidence:** the inputs that may legitimately be used.
3. **Output unit:** what is predicted, selected, generated, or estimated, including its granularity.
4. **Operating setting:** the temporal, spatial, data, supervision, and deployment conditions under which the formulation holds.
5. **Required assumptions:** the correspondence, observability, independence, stationarity, or annotation assumptions needed by the method.
6. **Closest adjacent task:** the formulation most likely to be confused with the target problem.
7. **Empirical boundary:** the datasets, protocols, architectures, populations, and metrics that support the reported claim.
8. **Claim boundary:** the strongest conclusion that can be supported inside those conditions.

Use positive scope. State what is studied and under which conditions. Mention an exclusion only when a nearby alternative would otherwise change the scientific meaning.

Prefer:

> Vision-centric audio-visual segmentation is considered under synchronized audio and video, with a binary sounding-object mask predicted for each frame. The scope is restricted to scenes in which evidence for selecting among visually plausible objects is provided by the soundtrack.

Avoid:

> Many general audio-visual problems exist, but they are not all considered here, and no claim is made that the method applies universally.

The first version closes the problem. The second version negotiates with unspecified objections.

## 2. Boundary layers

The same boundary must be expressed at four levels without being repeated verbatim.

### 2.1 Scientific boundary

Place the scientific boundary in the introduction. Identify the failure, the source of ambiguity, and the class of settings in which the failure matters.

### 2.2 Formal boundary

Place the operational contract at the beginning of problem setup. Define inputs, outputs, prediction unit, notation, and assumptions before equations or modules are introduced.

### 2.3 Empirical boundary

Place benchmark, split, metric, baseline, and protocol scope in experimental setup. Restrict empirical verbs to this evidence.

### 2.4 External-validity boundary

Place untested populations, deployment conditions, or failure regimes in discussion or limitations. Connect each limitation to a mechanism rather than to generic caution.

Do not let these layers conflict. A broad introduction cannot be supported by a narrow experiment unless the claim is explicitly narrowed.

## 3. Problem-to-solution chain

Require this dependency order:

```text
task boundary
→ unresolved failure inside that boundary
→ mechanism producing the failure
→ information or capability missing from current methods
→ design requirement
→ functional concept satisfying the requirement
→ formal method or module name
→ operation and information flow
→ experiment testing the claimed role
→ conclusion bounded by the evidence
```

No element may be introduced only because it exists in the implementation. Each module must inherit a need from the preceding diagnosis.

Use a “why now?” test. At the first appearance of every paragraph, module, experiment, and technical term, ask:

> Which earlier sentence makes this item necessary or intelligible at this point?

If no exact sentence can be identified, a hook is missing. Add the missing motivation or move the item to a position after its prerequisite.

## 4. Term dependency order

### 4.1 Hook-before-term rule

Every nonstandard technical term must have a prior hook. A hook is an earlier statement that establishes the phenomenon, requirement, object, or relation to be named.

Use this sequence:

```text
familiar problem concept
→ specific unmet requirement
→ functional description
→ formal term and acronym
→ mathematical symbol
→ downstream use
```

Example:

> Motion must first be tested for agreement with the soundtrack before it can guide localization. To perform this verification, a Spectral--Kinematic Alignment (SKA) module is introduced. A resonance map \(R\) is then produced by SKA and is used for query initialization.

Here, audio--motion agreement hooks the functional concept; the function hooks the module name; the module hooks the symbol; the symbol is available before downstream use.

Avoid:

> SKA produces \(R\), which is passed to MPQG for AVQ initialization.

No problem, function, symbol, or downstream acronym has been made available to the reader.

### 4.2 Definition-before-use rule

Define before substantive use:

- task variants and benchmark subsets;
- custom concepts and coined distinctions;
- method and module names;
- acronyms;
- symbols and tensors;
- nonstandard metrics;
- experimental interventions;
- scope-specific uses of familiar words.

A parenthetical expansion is a definition only when the underlying concept is already motivated. Expanding an acronym does not explain why the concept exists.

For acronyms, “define before use” also means “define exactly once.” The abstract and main body share one ledger: if the first expansion occurs in the abstract, only the acronym may appear in every later section, caption, and table note. A separately submitted supplement or checklist maintains its own ledger so that it remains self-contained. Record and remove every repeated expansion.

### 4.3 Term ledger

Build and audit this ledger:

| Term | Type | Prior hook | First and only definition | Later form | Dependencies | First substantive use |
|---|---|---|---|---|---|---|
| ... | concept/module/symbol/metric/dataset | section and sentence | section and sentence | stable acronym or term | earlier terms | section and sentence |

No row may contain an empty prior hook, a definition after first substantive use, or a second acronym expansion. Sort terms topologically by their dependencies.

### 4.4 Stable naming

Use one label for one concept after definition. Do not alternate technical identifiers to create lexical variety. When a longer noun phrase is needed, retain the head term:

```text
spectral--kinematic alignment
→ the alignment mechanism
→ this alignment response
```

Do not replace it with unrelated heads such as strategy, process, block, or paradigm.

## 5. Section and paragraph hooks

### 5.1 Section handoff

Each section must receive one question and pass one question forward:

| Section | Received question | Question passed forward |
|---|---|---|
| Introduction | Why does the task matter? | How can the derived requirements be implemented? |
| Method | Which mechanism satisfies the requirements? | Does each claimed role hold empirically? |
| Experiments | Which evidence tests those roles? | What principle and boundary follow? |
| Discussion | What explanation survives the evidence? | What conclusion is justified? |

The last paragraph of a section should make the next section expected without announcing document structure mechanically.

### 5.2 Paragraph handoff

Every paragraph must contain:

1. a concept received from earlier text;
2. one new claim or function;
3. reasoning or evidence;
4. a term, consequence, or question that can be continued next.

The next paragraph must pick up that passed element through exact lexical repetition or an unambiguous noun phrase.

### 5.3 Sentence hook

A sentence may be connected through:

- repeated technical terminology;
- explicit cause and effect;
- a general claim followed by evidence;
- a requirement followed by a mechanism;
- an operation followed by its consequence;
- a comparison along an unchanged axis.

The following do not constitute a hook by themselves:

- `this`, `it`, `they`, or `such` without an explicit noun;
- `however`, `therefore`, or `moreover`;
- a newly introduced acronym;
- chronological words such as `then` or `next`;
- a citation with no grammatical claim.

## 6. Passive-voice house style

### 6.1 First-person restraint

Minimize authorial first person in manuscript prose:

- `we`, `our`, `us`, `ours`, `ourselves`;
- `I`, `my`, `mine`, `myself`;
- possessive expressions such as `our method`, `our results`, or `our experiments`.

This preference applies to the abstract, main paper, supplementary material, captions, footnotes, and checklist prose written by the authors. Literal quotations and bibliographic titles are excluded.

First person may be retained when an explicit authorial decision would otherwise be confused with model behavior, dataset properties, or evidence, or when a passive rewrite would become materially longer or ambiguous. Each retained occurrence must serve that function. Routine phrases such as `we propose`, `we evaluate`, `our method`, and `our results` should still be rewritten.

### 6.2 Passive construction

Use passive constructions for transitive scientific actions whenever a natural passive form exists.

| Active construction | Required house style |
|---|---|
| We propose an alignment module. | An alignment module is proposed. |
| The method selects audio-consistent motion. | Audio-consistent motion is selected by the method. |
| We evaluate the model on AVSBench. | The model is evaluated on AVSBench. |
| The experiments show a consistent gain. | A consistent gain is observed across the experiments. |
| Our method outperforms VCT by 5.9 points. | VCT is exceeded by 5.9 points under the matched protocol. |

Prefer an agentless passive when the actor is obvious:

> Optical flow is precomputed with frozen RAFT.

Use a `by` phrase only when the agent carries information:

> Competing motion regions are ranked by the audio-conditioned alignment score.

### 6.3 Grammatical boundary

Do not force an invalid passive construction. Copular, existential, and genuinely intransitive clauses may be retained:

> The setting is challenging.

> Two failure modes remain.

> Performance increases as source ambiguity grows.

These clauses do not encode an avoidable authorial or method action. All transitive contribution, method, experiment, and result clauses should remain passive.

### 6.4 Passive does not justify weak prose

Avoid empty or defensive passives:

- `It is believed that`;
- `It should be noted that`;
- `It can be seen that`;
- `It is generally considered that`.

The evidence or object should be placed in subject position:

> A 2.2-point improvement is observed under the capacity-matched control.

## 7. Diagnostic examples

### 7.1 Boundary and hook failure

Weak:

> A Motion-Prompted Query Generator (MPQG) is introduced. It generates queries from a resonance map.

The reader has not been told why motion should affect queries or where the resonance map originates.

Strong:

> Localization must be influenced by verified motion before mask decoding. For this purpose, object-query initialization is conditioned on the previously defined resonance map. This operation is implemented by a Motion-Prompted Query Generator (MPQG).

The localization requirement hooks query initialization; the existing resonance map hooks the input; the function hooks the module name.

### 7.2 Broken paragraph chain

Weak:

> Audio-visual segmentation is affected by distractors. Optical flow is computed with RAFT. Three datasets are used.

The sentences belong to different reasoning levels and no dependency is created.

Strong:

> Ambiguity is created by visually salient distractors because the sounding object cannot be identified from appearance alone. Motion is therefore introduced as candidate evidence, and a dense flow field is precomputed with frozen RAFT. Whether the identified ambiguity is resolved by this evidence is evaluated on single- and multi-source benchmarks.

Each sentence receives and advances the same ambiguity-to-evidence chain.

## 8. Final audit

Before submission, verify:

- [ ] The scientific, formal, empirical, and claim boundaries agree.
- [ ] The target, inputs, output unit, setting, and required assumptions are explicit.
- [ ] The closest confusable task is distinguished where necessary.
- [ ] Each method component is preceded by a failure or design requirement.
- [ ] Each technical term has a nonempty prior hook.
- [ ] Each acronym is expanded exactly once at its first occurrence in the artifact and is never re-expanded after the abstract or at a section boundary.
- [ ] Each symbol is defined before substantive use.
- [ ] The term ledger is topologically ordered.
- [ ] Each paragraph receives an earlier concept and passes one forward.
- [ ] Section endings create the question answered next.
- [ ] Ambiguous pronouns and ornamental transitions have been removed.
- [ ] Authorial first person has been minimized, and every retained occurrence improves clarity.
- [ ] Natural passive constructions are used for transitive scientific actions.
- [ ] Passive voice has not introduced empty meta-framing.
