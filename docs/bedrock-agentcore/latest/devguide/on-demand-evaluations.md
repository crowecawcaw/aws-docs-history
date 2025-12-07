# On-demand evaluation

On-demand evaluation provides a flexible way to evaluate specific agent interactions by
directly analyzing a chosen set of spans. Unlike online evaluation which continuously
monitors production traffic, on-demand evaluation lets you perform targeted assessments of
selected interactions at any time.

With on-demand evaluation, you specify the exact spans or traces you want to evaluate by
providing their span or trace IDs. You can then apply the same comprehensive evaluation
methods available in online evaluation, including [Custom evaluators](custom-evaluators.md "custom-evaluators.md") or [Built-in evaluators](built-in-evaluators-overview.md "built-in-evaluators-overview.md"). This evaluation type is particularly
useful when you need to investigate specific customer interactions, validate fixes for
reported issues, or analyze historical data for quality improvements. Once you submit the
evaluation request, the service processes only the specified spans and provides detailed
results for your analysis.

This evaluation type complements online evaluation by offering precise control over which
interactions to evaluate, making it an effective tool for focused quality assessment and
issue investigation.

###### Topics

- [IAM permissions for on-demand
  evaluation](iam-permissions-on-demand.md "iam-permissions-on-demand.md")
- [Getting started with on-demand
  evaluation](getting-started-on-demand.md "getting-started-on-demand.md")
- [Understanding input spans](understanding-input-spans.md "understanding-input-spans.md")
