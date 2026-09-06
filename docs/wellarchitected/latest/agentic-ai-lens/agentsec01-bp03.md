

# AGENTSEC01-BP03 Monitor for hallucination propagation
<a name="agentsec01-bp03"></a>

 A single hallucinated fact stored as memory becomes ground truth for every agent that reads it next. Continuous grounding checks and confidence scoring keep fabricated content from entering memory or cascading across a multi-agent workflow. 

 **Desired outcome:** 
+  You detect false information before it propagates through agent memory or cascades across multi-agent workflows. 
+  You use confidence scoring to surface low-certainty outputs for validation, and fact-checking to help prevent hallucinated data from being stored as ground truth. 
+  When hallucination propagation is detected, affected memory entries are flagged or quarantined, and downstream agents are notified to discard potentially corrupted context. 

 **Common anti-patterns:** 
+  Storing model outputs directly into memory without a confidence threshold or grounding check, letting hallucinated facts persist and influence future decisions. 
+  Relying on the generating model to self-report uncertainty, which produces confident-sounding assessments even for fabricated content. 
+  Failing to propagate hallucination flags to downstream agents that consume shared memory, so corrupted context silently spreads through the workflow and each agent amplifies the error. 
+  Not logging hallucination detection events, reducing the risk of measurement of frequency or impact and blocking teams from tuning detection thresholds or identifying systemic patterns. 

 **Benefits of establishing this best practice:** 
+  Early detection catches hallucinated outputs before they propagate to downstream agents and compound into systemic errors. 
+  Confidence scoring gives a quantitative basis for deciding whether outputs are safe to store and act on. 
+  Ongoing monitoring surfaces new hallucination patterns for threshold tuning and rule refinement over time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Hallucinations compound. A fabricated fact stored during one session is retrieved as context in the next, and the second agent, reasoning on that input, produces a second output that looks self-consistent with a false premise. In multi-agent systems the problem is worse because each downstream consumer treats shared memory as ground truth. The design response is to catch fabrications at the point they are about to enter memory, flag them with evidence, and propagate that flag to anything that already read the affected context. 

 [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding is the first layer. It scores each model output against a provided reference context and rejects or flags anything below the threshold. Safety-critical applications run with higher thresholds, and creative tasks can run with lower ones. Pair contextual grounding with an LLM-as-a-Judge pattern for complex reasoning chains: route outputs through a secondary model invocation that receives the original context, the agent's output, and a structured evaluation prompt, and returns a confidence assessment. Keyword matching alone isn't sufficient at this layer. The judge catches contradictions and unsupported claims that simple filters miss. 

 [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) gives the check a natural home. The long-term memory consolidation process retrieves semantically similar existing memories and uses an LLM to decide whether to add, update, or skip new information, and outdated memories are marked as INVALID rather than deleted. That produces an immutable trail you can walk to trace how hallucinated content entered and propagated. Running grounding checks before create\_event helps keep fabrications out of the extraction pipeline, and custom memory strategy overrides let you bake grounding validation into the extraction and consolidation prompts for your domain. 

 Detection without traceability is expensive. Enable Amazon Bedrock model invocation logging and build Amazon CloudWatch Logs Insights queries that look for hallucination indicators (references to non-existent resources, contradictory statements within a single response, outputs that deviate significantly from input context). [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides a session, trace, and span hierarchy that lets you correlate a session-level anomaly back to the specific span where the hallucinated content originated. AgentCore emits default span data for memory resources, viewable in Amazon CloudWatch Logs and Amazon CloudWatch Application Signals, and session-level metrics are available on the CloudWatch generative AI observability page. For deeper visibility, instrument agent code with AWS Distro for OpenTelemetry (ADOT) to capture custom metrics for grounding scores, confidence thresholds, and validation outcomes at each step. 

 The circuit breaker keeps a single hallucination from cascading. When detection fires in one agent, flag every memory entry that agent wrote during the current session for re-validation before downstream agents consume it, and broadcast the detection event through Amazon EventBridge so every agent in the workflow can discard potentially corrupted context. Tag memory entries with confidence scores and grounding results so the evidence basis for every decision is auditable. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure contextual grounding thresholds per use case:** Set [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding thresholds that match each agent's risk profile, with higher thresholds for safety-critical applications and lower ones for creative tasks. 

1.  **Add an LLM-as-a-Judge step for high-stakes outputs:** Route outputs through a secondary model invocation that evaluates factual consistency against the original context before the output is committed to memory. 

1.  **Run grounding checks before create\_event:** Apply grounding validation at the [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) event ingestion boundary, so hallucinated content is filtered before reaching the long-term extraction and consolidation pipeline. 

1.  **Use custom memory strategy overrides for domain-specific grounding:** Incorporate grounding validation logic into the extraction and consolidation prompts through custom strategy overrides where your domain has specific factuality requirements. 

1.  **Enable Amazon Bedrock model invocation logging:** Turn on Amazon Bedrock model invocation logging and create Amazon CloudWatch Logs Insights queries that detect references to non-existent resources, contradictory statements, and significant deviations from input context. 

1.  **Alarm on output-consistency anomalies:** Configure Amazon CloudWatch anomaly detection on output-consistency metrics to baseline normal patterns and alert on deviations that suggest systematic hallucination. 

1.  **Instrument with ADOT and AgentCore Observability:** Use AWS Distro for OpenTelemetry to capture custom spans for grounding scores and validation outcomes, and use the session/trace/span hierarchy in [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to correlate detections back to the originating interaction. 

1.  **Wire a circuit breaker for propagation:** When a hallucination fires, flag every memory entry from the current session and broadcast the detection event through Amazon EventBridge so downstream agents can discard potentially corrupted context. 

1.  **Tag memory entries with evidence:** Store confidence scores and grounding check results alongside each memory entry to produce an auditable record of the evidence basis for agent decisions. 

1.  **Review detection logs periodically:** Tune thresholds, update detection rules, and identify systemic patterns by reviewing hallucination detection logs on a regular cadence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC01-BP01 Implement memory isolation and integrity controls](agentsec01-bp01.html) 
+  [AGENTSEC01-BP02 Validate and sanitize memory inputs](agentsec01-bp02.html) 
+  [AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage](agentsec05-bp01.html) 
+  [AGENTREL05-BP03 Ground agent cognition in real information](agentrel05-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock Guardrails contextual grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-grounding.html) 
+  [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) 
+  [AgentCore Observability: Sessions, traces, and spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) 
+  [Amazon Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) 
+  [Building smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/) 

 **Related services:** 
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 