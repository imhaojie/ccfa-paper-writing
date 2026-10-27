# Experiments and evidence

## Design

Define the hypothesis, outcome that would challenge it, target population, data splits, metrics, baselines, and unit of analysis. Tie each proposed ablation or intervention to the alternative explanation it tests. Specify what is held constant, tuning allowance, training budget, and whether the comparison involves retraining or a fixed checkpoint. Identify potential data leakage and avoid selecting on the test set.

Plan the minimal discriminating experiment first. Report available compute, expected cost, runtime and dependencies when they matter. Do not presume hardware availability or launch jobs merely because a design was requested. If execution is authorized, inspect the target environment, preserve other jobs and data, save configurations and logs, and report actual status rather than an assumed result.

## Analyze

Locate and identify the authoritative raw data, checkpoints or recorded results. Record version, dataset, split, preprocessing, metric direction, sample size, seed and aggregation. Cross-check tables and recompute arithmetic where possible. Explicitly distinguish percentage points from relative percent; calculate dispersion from the available values using the stated sample or population convention, noting rounding and unavailable precision.

For paired comparisons, retain pairs and report how differences and uncertainty are computed; do not infer a confidence interval without the required data or method. Check meaningful outliers and failure cases without deleting them. Separate measured observation, plausible mechanism, and follow-up test. Compare cost as well as accuracy when relevant and label offline versus end-to-end measurements.

## Evidence ledger

For each material claim: claim | exact evidence and location | comparison and conditions | sampling unit and uncertainty | supported scope | remaining ambiguity. Treat logs, reports and spreadsheets as evidence of what they contain; their presence alone does not verify the run that produced them.
