---
name: lumen-research
description: Guide evidence-led AI research from literature and idea evaluation through experiment design, result analysis, scientific writing, peer review, and rebuttal. Use when the user requests a research task or a connected research workflow; select only the stages needed and preserve the user's scope.
---

# Lumen Research

Turn a research question into a traceable argument: define the problem, examine the closest evidence, test a concrete hypothesis, and communicate only what the results support. Adapt this workflow to the user's task rather than forcing every project through a full pipeline.

## Start with the user's actual request

Identify the requested deliverable, available materials, constraints, stage of research, and authoritative versions. Read project instructions and relevant existing materials. For submitted or locked documents, treat the submitted PDF as the record and do not edit it unless explicitly authorized. If local sources disagree, report the discrepancy rather than silently choosing a favorable result.

Choose the smallest relevant reference set:

- Literature, problem definition, idea generation, novelty: `references/discovery.md`.
- Experiments, diagnostics, statistics, and resource management: `references/experiments.md`.
- Manuscripts, CCF-A-style narrative, and visual presentation: `references/writing.md`.
- Critical review, response strategy, and rebuttal: `references/review-rebuttal.md`.

For a connected request, combine the relevant references in dependency order. Deliver useful partial analysis when essential evidence is missing; identify the missing evidence and its effect on the conclusion.

## Research principles

1. **Make the question precise.** Identify the task, inputs, outputs, assumptions, setting, and scope. Define a concept before relying on it and connect each technical term to an earlier motivation.
2. **Track claims to evidence.** For important claims record the source, comparison, dataset, metric, setting, and limitation. Separate observation, interpretation, and hypothesis; never fabricate citations, data, experimental runs, or provenance.
3. **Compare against the closest alternatives.** Examine shared and differing assumptions, mechanisms, datasets, and evaluation protocols before claiming novelty or superiority. Distinguish absence of evidence from evidence of absence.
4. **Design tests that could change the conclusion.** Identify the alternative explanation and the smallest informative control. A negative result is evidence, not a failure to hide.
5. **Respect the evidence hierarchy.** Prefer original papers, official datasets, code, and raw results where available. Treat summaries and agent output as leads rather than proof. Mark unverified claims and assumptions.
6. **Write for scientific understanding.** Lead with the finding, explain its mechanism, give relevant evidence and connect it to the research question. Use precise scope, not defensive disclaimers or inflated claims. Preserve meaningful limitations.
7. **Stay within authorized work.** Analysis does not authorize starting jobs, changing files, publishing, or sending messages. When the user requests implementation, use the stated budget and environment; never infer permission from a lack of response. Do not expose secrets or private review material.
8. **Keep outputs reproducible and portable.** Record sources, versions, configuration, sampling units, relevant aggregation and uncertainty, and limits of verification. Avoid hard-coded model names, accounts, server paths, or tool dependencies.

## Execution and output

Begin with the user's question, not a mandatory ceremony. For a literature or novelty task, use available search and read original sources; identify search date and coverage, and explicitly state if access is limited. For a numerical task, recalculate relevant statistics from available data and show units and rounding. For review and rebuttal, map each concern to an exact claim and evidence before drafting. For writing, retain locked facts and verify claims against the authoritative record.

Provide the requested artifact first when practical. Include the most relevant evidence, specific uncertainty, and actionable next steps. Do not claim a paper is verified, reproducible, or submission-ready beyond checks actually performed. Follow current venue and platform rules when they are relevant and verifiable.
