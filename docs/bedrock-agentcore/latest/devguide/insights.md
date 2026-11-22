

# Insights: Find recurring agent failures

**Legacy Insights preview is deprecated**  
Amazon Bedrock AgentCore stopped accepting new report-oriented batch and recurring Insights jobs on October 16, 2026. Existing recurring jobs stopped generating reports after October 30, 2026. Historical batch results and recurring reports remain available for now. The legacy Preview experience is deprecated and will be removed in a future release.  
For current Insights workflows, use [Insights in online evaluation](online-evaluations-insights.md) for ongoing analysis of live agent traffic or [Insights in batch evaluation](batch-evaluations-insights.md) for point-in-time analysis of a selected dataset.

Amazon Bedrock AgentCore Insights identifies recurring failure patterns in live agent traffic. Add the `Builtin.FailureAnalysis` Insight Evaluator to an online evaluation to group related findings at the agent level and update them as the evaluation processes new evidence.

Each pattern is available as an Agent Insight with root causes, suggested fixes, an affected-session count, and sample sessions. The Agent Insights APIs let you list, read, archive, and restore these findings.

Batch evaluations can also use `Builtin.FailureAnalysis`. They produce point-in-time insights for the selected dataset rather than updating findings as new traffic arrives. When the default Agent Insight Store is enabled and active, the Agent Insights APIs provide a common access model for both sources. For a comparison, see [Online and batch sources](insights-how-it-works.md#insights-online-and-batch).

**Note**  
Insights uses the inference behavior of AgentCore Evaluations. Depending on the source Region, built-in evaluator requests can be processed in another Region. For the current routing and data-processing behavior, see [Cross region inference](evaluations-cross-region-inference.md).

Each AWS account has one default Agent Insight Store in each supported AWS Region. The Store starts disabled. Enable it before Insight Evaluators can add Agent Insights from online or batch evaluations.