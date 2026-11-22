

# Insight evaluators

Insight evaluators are built-in evaluators that explain agent behavior instead of only scoring it. Like other built-in evaluators, they run on each session. In addition, they let the service look across sessions and group related findings into *insights*.

Use an insight evaluator when you want to know *why* your agent behaves as it does, not only how well it performed. For example, a quality score can tell you that 20 percent of sessions did not reach their goal, while an insight evaluator can tell you which failure patterns account for those sessions and what to change.

Insight evaluators have the following characteristics:
+  **Per-session results:** Each evaluator writes a result for each session to CloudWatch Logs and metrics, like any session-level evaluator.
+  **Insights across sessions:** The service groups findings from evaluated sessions into insights. Each insight describes a pattern, the root causes behind it, and suggested fixes.
+  **Combine with other evaluators:** You can run an insight evaluator alone or together with other built-in or custom evaluators.

Insight evaluators work with online and batch evaluations:
+ In an online evaluation, an Insight Evaluator generates [Agent Insights](online-evaluations-insights.md) from sampled live traffic when the default Agent Insight Store is enabled and active.
+ In a batch evaluation, an Insight Evaluator generates point-in-time `insightResults` for the selected dataset. See [Insights in batch evaluation](batch-evaluations-insights.md).

When the default Agent Insight Store is enabled and active, the Agent Insights APIs surface findings from both sources. The [Insights](insights.md) documentation explains the common access model.

The following insight evaluators are available:


| Evaluator | Description | 
| --- | --- | 
|  `Builtin.FailureAnalysis`  | Finds failures in each session, traces them to spans, determines the root cause of each failure, and groups the findings across sessions into insights. See [Failure analysis evaluator](builtin-failure-analysis.md). | 

**Topics**
+ [Failure analysis evaluator](builtin-failure-analysis.md)