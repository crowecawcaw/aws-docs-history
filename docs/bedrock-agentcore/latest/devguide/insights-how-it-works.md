

# How Insights works

For online evaluations, Insights uses the results of the `Builtin.FailureAnalysis` evaluator to find recurring failure patterns in sampled live traffic.

For each selected session, AgentCore:
+ Runs `Builtin.FailureAnalysis` and writes the session result with the other online evaluation results.
+ Compares new failure findings with patterns for the agent identified by `serviceName`.
+ Adds related findings to an existing pattern or creates a new pattern.
+ Stores each pattern as an Agent Insight in the default Agent Insight Store.

AgentCore updates these Agent Insights as the online evaluation processes more evidence.

The generated analysis is advisory. Review the sample sessions and traces before you change an agent.

## Online and batch sources
<a name="insights-online-and-batch"></a>

Batch evaluations can run the same Insight Evaluator, but they generate point-in-time insights for the selected dataset. The following table compares the two sources.


| Source | Pattern behavior | Where results appear | 
| --- | --- | --- | 
| Online evaluation | Agent Insights update as the evaluator processes sampled live sessions. AgentCore groups patterns at the agent level by `serviceName`. | Session results appear with the other online evaluation results. Use `applicationName` in the Agent Insights APIs to list and read the patterns. It represents the same OpenTelemetry service name (`service.name`) that the online evaluation configures as `serviceName`. | 
| Batch evaluation | Batch insights describe one completed evaluation and don’t update continuously. |  `GetBatchEvaluation` returns the grouped findings in `insightResults`. The Agent Insights APIs also provide access to these findings by `batchEvaluationId`. | 

The default Agent Insight Store starts disabled. Enable it and wait until it is active before Insight Evaluators can add findings. Disabling the Store doesn’t stop the evaluation or its session-level results.

## What an Agent Insight contains
<a name="insights-result-fields"></a>

 `ListAgentInsights` returns summaries. `GetAgentInsight` also returns detailed root causes and sample sessions. The following table describes the primary fields.


| Field | Description | 
| --- | --- | 
|  `agentInsightId`, `applicationName`  | The stable identifiers for an Agent Insight. The ID is scoped to the application. | 
|  `type`  | The analysis type. Agent Insights currently returns `FAILURE`. | 
|  `name`, `description`  | Generated display content that summarizes the recurring failure. | 
|  `createdAt`, `updatedAt`, `lastSeenAt`  | Timestamps for creation, the latest update, and the latest contributing observation. | 
|  `affectedSessionCount`  | The number of sessions represented by the current pattern. | 
|  `archiveStatus`  | Whether the Agent Insight appears in the `ACTIVE` or `ARCHIVED` view. | 
|  `customerMetadataStatus`  | Whether AgentCore can read the encrypted generated content. | 
|  `batchEvaluationId`  | The source batch evaluation, when applicable. | 
|  `rootCauses`, `sampleSessions`  | Detailed explanations, suggested fixes, and representative sessions. | 

Names are display labels and can change. Use `agentInsightId` together with `applicationName` when you need to identify the same Agent Insight across API calls.

For complete request and response syntax, see [ListAgentInsights](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListAgentInsights.html) and [GetAgentInsight](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetAgentInsight.html) in the *Amazon Bedrock AgentCore API Reference*.