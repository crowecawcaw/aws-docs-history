

# Experiments
<a name="omni-agents-experiments"></a>

An experiment tells you whether a change made your agent better or worse before you ship it. It works by controlling the variables: the same dataset and the same evaluators run against two or more agent versions, so a difference in scores can only come from the change you made.

Available in the IDE extension only.

**What you can compare**

A "version" in an experiment is any variant of your agent you can run: a new prompt version, a different model, a changed tool, or a reworked orchestration step. Change one thing per experiment where you can. If a variant changes the prompt and the model at once, the scores cannot tell you which change mattered.

**To run an experiment**

1. In the IDE extension, choose a dataset to run against. Use one with a baseline score, so you know what you are comparing to. See [Datasets](omni-agents-datasets.md).

1. Select the agent versions or configurations to compare, and the evaluators to apply. Keep the evaluators identical across versions.

1. Run the experiment. Each version runs every test case in the dataset, and the evaluators score each run.

1. Compare the results: the aggregate scores first, then the per-case results.

**Read the per-case results, not only the average**

An aggregate score can hide a trade-off: a variant that improves the average while breaking cases that used to pass may be worse than the number suggests. Look at the cases that changed direction (improved and regressed) and open the traces behind the regressions to see what the new version did differently. Add a regressed case to your dataset so that later versions are measured against it. See [Datasets](omni-agents-datasets.md).