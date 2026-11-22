

# How it works

AgentCore optimization connects failure patterns from online or batch insights to validated improvements through a repeatable cycle. Both sources provide Agent Insights with evaluation and sample-session details that you can use to select traces for a recommendation.

A typical iteration follows these steps:

1.  **Find a failure pattern:** Enable the default Agent Insight Store, then run `Builtin.FailureAnalysis` in an online or batch evaluation. An online Insight Evaluator generates Agent Insights that update as it processes live traffic. A batch Insight Evaluator generates point-in-time insights for the selected dataset. Review the Agent Insight’s root causes, suggested fixes, affected-session count, and sample sessions, and inspect the corresponding traces to confirm the pattern. For more information, see [Insights](insights.md).

1.  **Select the traces and optimization goal:** Use the application, source evaluation, timestamps, and sample sessions from the Agent Insight to choose a [trace source for the recommendation](optimization-recommendations.md#recommendations-trace-sources). You can select the corresponding time range in CloudWatch Logs, provide session spans, or reference a related completed batch evaluation. For a system prompt recommendation, also select one numerical evaluator that measures the behavior you want to improve. `Builtin.FailureAnalysis` explains the failure pattern but isn’t a numerical optimization signal.

1.  **Generate a recommendation:** Provide the current system prompt or tool descriptions and the selected traces to the Recommendations API. The service returns an optimized configuration and an explanation of what changed and why.

1.  **(Optional) Package as a configuration bundle:** Create a bundle version with the recommended configuration. A bundle is a versioned, immutable snapshot of an agent’s configuration (system prompts, model IDs, tool descriptions) that can be dynamically changed without code deployments. Configuration bundles are useful when you want to decouple agent behavior from code; they are not required. You can also validate changes by deploying to a separate runtime endpoint.

1.  **Validate with an A/B test:** Split production traffic between the current agent (control) and the improved version (treatment) through AgentCore Gateway. Online evaluation scores each session and reports results with statistical significance. A/B tests support two patterns:
   +  **Configuration bundle variants:** Same runtime, different bundle versions. Use when the change is purely configuration (prompt, model ID, tool descriptions).
   +  **Target-based variants:** Different gateway targets pointing to different runtime endpoints. Use when the change includes code changes, a framework upgrade, or when you want to compare entirely different agent implementations. Each variant can have its own online evaluation configuration.

1.  **Route traffic to the winning variant and repeat:** Route 100% of traffic to the winning variant. Continue evaluating the new baseline. Online evaluation insights can show whether the original failure pattern stops recurring and identify the next pattern to investigate.