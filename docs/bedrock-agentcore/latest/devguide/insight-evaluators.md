

# Insight evaluators
<a name="insight-evaluators"></a>

Insight evaluators are built-in evaluators that explain agent behavior instead of only scoring it. Like other built-in evaluators, they run on each session. In addition, they let the service look across sessions: after the sessions are evaluated, the service groups related findings into *insights* and returns them with the evaluation results.

Use an insight evaluator when you want to know *why* your agent behaves as it does, not only how well it performed. For example, a quality score can tell you that 20 percent of sessions did not reach their goal, while an insight evaluator can tell you which failure patterns account for those sessions and what to change.

Insight evaluators have the following characteristics:
+  **Per-session results:** Each evaluator writes a result for each session to CloudWatch Logs and metrics, like any session-level evaluator.
+  **Insights across sessions:** The service groups the findings from all evaluated sessions into insights. Each insight describes a pattern, the root causes behind it, and suggested fixes.
+  **Combine with other evaluators:** You can run an insight evaluator alone or together with other built-in or custom evaluators.

**Note**  
Currently, only the batch evaluation APIs support insight evaluators. For how to run an insight evaluator and read the insights, see [Insights in batch evaluation](batch-evaluations-insights.md).

The following insight evaluators are available:


| Evaluator | Description | 
| --- | --- | 
|  `Builtin.FailureAnalysis`  | Finds failures in each session, traces them to spans, determines the root cause of each failure, and groups the findings across sessions into insights. See [Failure analysis evaluator](builtin-failure-analysis.md). | 

**Topics**
+ [Failure analysis evaluator](builtin-failure-analysis.md)