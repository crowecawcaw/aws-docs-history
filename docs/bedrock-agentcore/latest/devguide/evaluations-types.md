# Evaluation types

AgentCore Evaluations provides two evaluation types, which differ in when and how the
evaluation is performed:

###### Topics

- [Online evaluation](#online-evaluation-type "#online-evaluation-type")
- [On-demand evaluation](#on-demand-evaluation-type "#on-demand-evaluation-type")

## Online evaluation

Online evaluation continuously monitors the quality of deployed agents using live
production traffic. Unlike one-off evaluation in development environments, it
provides continuous performance assessment across multiple criteria, enabling
persistent monitoring in production.

Online evaluation consists of three main components. First, session sampling and
filtering allows you to configure specific rules to evaluate agent interactions. You
can set percentage-based sampling to evaluate a portion of all sessions (for
example, 10%) or define conditional filters for more targeted evaluation. Second,
you can choose from multiple evaluation methods including creating new [Custom evaluators](custom-evaluators.md "custom-evaluators.md"), using existing
custom evaluators, or selecting from [Built-in evaluators](evaluators.md#built-in-evaluators "evaluators.md#built-in-evaluators"). Finally, the monitoring and analysis
capabilities lets you view aggregated scores in dashboards, track quality trends
over time, investigate low-scoring sessions, and analyze complete interaction flows
from input to output.

## On-demand evaluation

On-demand evaluation provides a flexible way to evaluate specific agent
interactions by directly analyzing a chosen set of spans. Unlike online evaluation
which continuously monitors production traffic, on-demand evaluation lets you
perform targeted assessments of selected interactions at any time.

With on-demand evaluation, you specify the exact spans or traces you want to
evaluate by providing their span or trace IDs. You can then apply the same
comprehensive evaluation methods available in online evaluation, including [Custom evaluators](custom-evaluators.md "custom-evaluators.md") or [Built-in evaluators](evaluators.md#built-in-evaluators "evaluators.md#built-in-evaluators"). This
evaluation type is particularly useful when you need to try out your own custom
evaluator, investigate specific customer interactions, validate fixes for reported
issues, or analyze historical data for quality improvements. Once you submit the
evaluation request, the service processes only the spans and traces you specify and
returns detailed results for your analysis.

This evaluation type complements online evaluation by offering precise control
over which interactions to assess, making it an effective tool for focused quality
analysis and issue investigation. It is also well suited for early stages of the
agent development lifecycle, such as build-time testing.
