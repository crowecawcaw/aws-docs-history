

# AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery
<a name="agentrel07-bp03"></a>

 Correlating logs across services by hand is slow, and during an incident slow is worse than expensive. Distributed tracing across all components with agent-specific annotations gives operators the full request path in one view and turns broad restarts into targeted recovery actions. 

 **Desired outcome:** 
+  You have distributed tracing across every agent component with agent-specific annotations. 
+  You propagate trace context through synchronous and asynchronous communication boundaries. 
+  You correlate traces, metrics, and logs in a unified view that surfaces root causes quickly. 

 **Common anti-patterns:** 
+  Tracing only at the application boundary without propagating context through internal service calls. 
+  Skipping correlation of traces with logs and metrics, reducing the risk of unified analysis during incidents. 
+  Omitting agent-specific annotations that make filtering by agent ID, task type, or model used possible. 

 **Benefits of establishing this best practice:** 
+  Root causes surface quickly because the request flow is visible end to end. 
+  Mean time to recovery drops because trace data drives targeted actions instead of broad restarts. 
+  Latency bottlenecks become visible, enabling proactive performance optimization. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures the full execution path of each agent invocation through OpenTelemetry-compatible telemetry. Turn it on across every agent component, not only the outer boundary, so the trace actually spans the request end to end. Without component-level coverage, traces have gaps where invisible work happens, which is exactly where debugging slows down during an incident. 

 Annotations are what make traces searchable at the scale of real systems. Agent-specific tags, agent ID, task type, model ID, workflow ID, let you filter traces to a specific agent or failure scenario instead of grepping through an undifferentiated stream. Instrument Strands Agents framework-level traces to capture reasoning steps, tool invocations, and their outcomes in a unified trace view, because the agent's internal decisions are where most of the interesting signals live. 

 Context propagation is the detail that decides whether asynchronous paths are visible. For queue-based communication, propagate trace headers through message attributes so traces continue across queue boundaries. Without propagation, the trace ends at the producer and a new trace starts at the consumer, and the fact that they relate is lost. Create trace-based alerting through Amazon CloudWatch that correlates traces, metrics, and logs in a unified view, so a trace anomaly, a metric spike, and a log error appear together rather than separately. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable AgentCore Observability with OpenTelemetry tracing:** Turn on [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) across every agent component. 

1.  **Add agent-specific annotations:** Tag traces with agent ID, task type, and model ID so filtering during incidents is possible. 

1.  **Propagate trace context across boundaries:** Include synchronous and asynchronous paths, with message attributes for queue-based communication. 

1.  **Instrument Strands Agents framework-level traces:** Capture reasoning steps and tool invocations in the unified trace view. 

1.  **Create CloudWatch dashboards that correlate traces, metrics, and logs:** Build one unified view so incident response works on signal. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL07-BP01 Design workflows in stages with incremental recovery](agentrel07-bp01.html) 
+  [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](agentrel07-bp02.html) 
+  [AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing](agentrel08-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Strands Agents Traces](https://strandsagents.com/docs/user-guide/observability-evaluation/traces/) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k) 
+  [AWS re:Invent 2024 - Observability for Reliable Agentic AI with Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk) 
+  [AWS re:Invent 2024 - Build observable AI agents with Strands, AgentCore, and Datadog (AIM233)](https://www.youtube.com/watch?v=mOAd8grR1BU) 

 **Related workshops:** 
+  [Diving Deep into Bedrock AgentCore - Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 