

# AGENTOPS04-BP03 Develop fallback behavior and error handling for tool invocations
<a name="agentops04-bp03"></a>

 Tools failing is a reality in modern architectures. The question is whether the agent degrades gracefully to an alternative, falls back to a manual process, or returns an error and halts. Well-designed fallback chains and automatic cutoffs keep tool failures from becoming agent failures. 

 **Desired outcome:** 
+  When tools fail or become unavailable, agents degrade gracefully to alternative tools, degraded-mode operations, or manual process escalation. 
+  Automatic cutoffs help prevent cascading failures from propagating through the agent environment. 
+  Retry strategies with exponential backoff handle transient errors transparently without amplifying load on degraded systems. 
+  Per-tool success rates, latency, and error patterns are monitored in real time so degradation is detected before it impacts users. 

 **Common anti-patterns:** 
+  Implementing identical retry strategies for all tools regardless of failure characteristics, applying aggressive retries to permanently failed tools or insufficient retries to transiently degraded ones. 
+  Operating without automatic cutoffs, so agents repeatedly invoke degraded tools that consistently time out, wasting time and resources on calls unlikely to succeed. 
+  Having no fallback path when a tool fails, forcing the agent to return an error to the user or halt the workflow entirely. 
+  Treating tool runbooks as optional documentation, so operators start from scratch on each incident. 

 **Benefits of establishing this best practice:** 
+  Per-tool monitoring with error pattern analysis gives deep visibility into tool reliability across the catalog. 
+  Operational runbooks help drive consistent incident response, reducing mean time to resolution and helping prevent ad-hoc responses that introduce new problems. 
+  Automatic cutoffs break cascading failures at their source rather than allowing them to propagate across agents. 
+  Graceful degradation through fallback chains maintains business continuity during partial outages. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automatic cutoffs are the single most effective control for helping prevent cascading failure. When a tool starts returning errors above a threshold, continuing to invoke it compounds the problem. The agent wastes time, the tool gets more load, and upstream latency climbs while nothing is accomplished. An automatic cutoff transitions the tool from normal operation to blocked when error rates exceed a threshold (for example, 50% errors in a 60-second window) or when timeouts exceed a threshold (for example, 5 consecutive timeouts). It transitions to probing after a configurable recovery interval (for example, 30 seconds). Apply the state machine to every external dependency rather than the ones that have already caused incidents. 

 Retry and timeout policies should be per-tool rather than global. Exponential backoff with jitter handles transient errors without amplifying the problem. Fallback chains, like primary to secondary to degraded-mode to manual escalation, give the agent a path forward when the primary tool is unavailable for critical operations. The fallback order should live in the tool registry so it evolves with the tool inventory rather than embedded in each agent's code. 

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks invocation count, success rate, error rate by type, and latency percentiles on a per-tool basis. Composite alarms correlate multiple metrics. A tool with rising latency and increasing timeout rate is a tool approaching cutoff, regardless of whether either signal would fire an alarm individually. The composite view often catches degradation earlier than single-metric thresholds would. 

 Develop operational runbooks for the top five most common tool failure scenarios, and generate weekly SLA reports shared with tool owners so reliability trends stay visible. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement automatic cutoffs:** Configure error rate and timeout thresholds for the transition from normal to blocked, plus probing recovery timeouts, for every external dependency. 

1.  **Define per-tool timeout and retry policies:** Use exponential backoff with jitter appropriate to each tool's failure characteristics. 

1.  **Build fallback chains for critical tools:** Store fallback order in the tool registry so chains evolve with the tool inventory rather than being hardcoded in each agent. 

1.  **Monitor per-tool health through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html):** Use composite alarms that correlate multiple metrics for earlier detection. 

1.  **Develop operational runbooks for common tool failure scenarios:** Include diagnostic steps and escalation paths so operators start from a known baseline. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS04-BP01 Implement tool registry and catalog management](agentops04-bp01.html) 
+  [AGENTOPS04-BP02 Establish standardized tool integration protocols (MCP, A2A)](agentops04-bp02.html) 
+  [AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations](agentops05-bp01.html) 
+  [AGENTPERF06-BP02 Implement efficient tool invocation patterns](agentperf06-bp02.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 
+  [Planning for failure: How to make generative AI workloads more resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/) 
+  [Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 