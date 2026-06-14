# AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing

Request-boundary telemetry can't distinguish between normal
variation and genuine degradation. Stage-level telemetry across the
full processing lifecycle gives operators the signal they need to
activate graceful degradation at the right time rather than too
early or too late.

**Desired outcome:**

- You have stage-level telemetry across context retrieval, model
  inference, tool execution, and response generation.
- You capture LLM-specific data, token counts, inference latency,
  finish reason, on every model call.
- You have CloudWatch dashboards with stage-level widgets and
  composite alarms that drive automated degradation activation.

**Common anti-patterns:**

- Implementing telemetry only at the request boundary without
  instrumenting individual processing stages.
- Omitting LLM-specific telemetry, token counts, inference
  latency, output quality. That is essential for detecting
  model-related degradation.
- Treating telemetry as a post-deployment concern rather than
  designing it into the architecture from the start.

**Benefits of establishing this best
practice:**

- Degradation detection is accurate because telemetry covers every
  processing stage.
- Degradation decisions are informed by which stage is actually
  under pressure.
- Incident response is faster through pre-built dashboards that
  expose the signals immediately.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") captures agent-specific
telemetry through OpenTelemetry-compatible instrumentation. This
includes tool invocation traces, model interaction details, and
memory access patterns. Stage-level instrumentation is what
distinguishes this from generic request logging. A single latency
metric at the request boundary can't tell you whether slowness
came from retrieval, inference, tool execution, or response
parsing.

LLM-specific telemetry deserves its own emphasis. Enable
[Amazon
Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md") to capture full request
and response data for every LLM call, including token counts,
latency, and finish reason. A spike in output token counts or a
shift in finish-reason distribution often precedes a visible
quality regression by hours. Without the logs, those early signals
are invisible.

The metric set needs structure. For each processing stage define a
standard set. Context retrieval tracks latency and result count.
Model inference tracks latency, token counts, and model ID. Tool
execution tracks call count, latency, and error rate. Response
generation tracks output validation pass rate. Build Amazon CloudWatch dashboards with stage-level widgets and a composite
health summary so operators can see the full lifecycle at a
glance.
[Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") on the key metrics establishes
baselines automatically, removing the need to hand-tune
thresholds. Composite alarms across multiple stages detect
degradation patterns that span boundaries and trigger automated
degradation activation when the composite health signal drops.

### Implementation steps

1. **Enable AgentCore Observability with
   stage-level telemetry:** Instrument context
   retrieval, inference, tool execution, and response
   generation. Use
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") for collection.
2. **Enable Amazon Bedrock model
   invocation logging:** Capture token counts,
   latency, and finish reason for every LLM call through
   [Amazon
   Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md").
3. **Build CloudWatch dashboards with
   stage-level widgets:** Include a composite health
   summary so operators see the full lifecycle at a glance.
4. **Configure CloudWatch Anomaly
   Detection on key metrics:** Use
   [Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") for automatic baseline
   modeling.
5. **Create composite alarms:**
   Combine multi-stage signals to trigger automated degradation
   activation.

## Resources

**Related best practices:**

- [AGENTREL07-BP03
  Implement distributed tracing to track system dependencies and
  facilitate recovery](agentrel07-bp03.md "agentrel07-bp03.md")
- [AGENTREL08-BP01
  Establish consistent configuration management practices](agentrel08-bp01.md "agentrel08-bp01.md")
- [AGENTREL08-BP03
  Architect agent systems with resource isolation and contention
  mitigation](agentrel08-bp03.md "agentrel08-bp03.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [Build
  trustworthy AI agents with Amazon Bedrock AgentCore
  Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/ "https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/")
- [Amazon
  Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md")
- [Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
