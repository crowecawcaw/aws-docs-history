

# Batch evaluation

Batch evaluation runs evaluators against multiple agent sessions in a single job with server-side orchestration. Unlike on-demand evaluation where you collect spans and call the Evaluate API yourself, batch evaluation handles session discovery, span collection, and scoring entirely on the service side. You submit a job, and the service processes all matching sessions and returns aggregate results.

A batch evaluation can also create the sessions it evaluates. You pass a published dataset and an AgentCore Runtime endpoint. The service runs each scenario in the dataset against your agent, and then evaluates the results. See [Run a dataset evaluation with AgentCore Evaluations](batch-evaluations-dataset.md).

Use batch evaluation when you need to:
+  **Measure a baseline** before making changes to your agent’s prompt, tools, or model.
+  **Validate improvements** by comparing scores before and after a configuration change.
+  **Run regression tests** across a curated set of sessions, or across the scenarios in a dataset.
+  **Monitor quality periodically** across production sessions from a specific time window.

<a name="batch-evaluations-how-it-works"></a> **How it works** 

A batch evaluation job follows this flow:

1.  **You start a job** by specifying a session source (where to find agent sessions) and an evaluation configuration (which evaluators to run). Optionally, you provide ground truth metadata for reference-based scoring.

1.  **The service discovers sessions** from CloudWatch Logs based on the log groups and filters you specify. For an AgentCore-run dataset evaluation, the service first runs each scenario against your Runtime endpoint, and then evaluates the sessions it created.

1.  **The service runs evaluators** against each discovered session. Each evaluator scores each session independently. If ground truth is provided, evaluators that support reference-based scoring use it.

1.  **You poll for results.** The job transitions through `PENDING` → `IN_PROGRESS` → `COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, or `STOPPED`. If you stop a job, it moves to `STOPPING` before `STOPPED`. When complete, the response includes aggregate summaries with per-evaluator average scores, session counts, and token usage.

1.  **Per-session detail** is available in CloudWatch Logs at the location specified in `outputDataConfig` in the response.

<a name="batch-evaluations-comparison"></a> **Comparison with other evaluation types** 


| Aspect | On-demand | Online | Batch | 
| --- | --- | --- | --- | 
| Trigger | Caller-initiated, synchronous | Continuous, event-driven | Caller-initiated, asynchronous | 
| Session source | Caller provides spans inline | Watches a log group | Service discovers from CloudWatch Logs, or creates sessions by running a dataset against a Runtime endpoint | 
| Scope | Single session | All sessions matching sampling rules | Multiple sessions (time range, session IDs, or full log group), or every scenario in a dataset version | 
| Ground truth | Via `evaluationReferenceInputs`  | Not supported | Via `sessionMetadata` with inline ground truth, or from the dataset’s scenarios | 
| Results | Synchronous response | CloudWatch metrics and dashboards | Aggregate summaries with per-evaluator averages, plus per-session detail in CloudWatch | 
| Use case | Dev-time spot checks, CI/CD | Production monitoring | Baseline measurement, pre/post comparison, regression testing | 

**Topics**
+ [Prerequisites](batch-evaluations-prereqs.md)
+ [Getting started with batch evaluation](batch-evaluations-getting-started.md)
+ [Start batch evaluation](batch-evaluations-start.md)
+ [Run a dataset evaluation with AgentCore Evaluations](batch-evaluations-dataset.md)
+ [Manage batch evaluations](batch-evaluations-manage.md)
+ [Understanding results and output](batch-evaluations-results.md)
+ [Insights in batch evaluation](batch-evaluations-insights.md)
+ [Batch evaluation encryption](batch-evaluations-encryption.md)