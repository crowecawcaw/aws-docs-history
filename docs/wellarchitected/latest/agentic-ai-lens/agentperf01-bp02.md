# AGENTPERF01-BP02 Implement comprehensive performance telemetry

A single agent request fans out into chains of inference calls,
parallel tool invocations, memory lookups, and inter-agent
communications. Infrastructure-only monitoring can't determine by
itself which of those contributes to a slow or expensive response.
Agent-aware telemetry decomposes execution into observable,
attributable operations so that performance decisions are grounded
in measured behavior.

**Desired outcome:**

- You have a complete distributed trace for every agent execution
  that decomposes total latency into its constituent operations.
- You have real-time dashboards that provide visibility into agent
  performance trends, with the resulting metrics feeding the
  alerting layer.
- You have historical telemetry data that supports capacity
  planning, model selection decisions, and architecture
  optimization through data-driven analysis.

**Common anti-patterns:**

- Relying only on infrastructure-level metrics such as function
  duration or API gateway latency without instrumenting the
  agent's reasoning pipeline, making it impossible to distinguish
  between slow inference and slow tool calls.
- Treating telemetry as an afterthought, producing gaps in trace
  continuity across agent boundaries, tool invocations, and
  asynchronous operations.
- Collecting telemetry data without establishing baselines,
  thresholds, or alerts, creating a data lake of metrics that
  nobody monitors or acts upon.

**Benefits of establishing this best
practice:**

- Fine-grained performance data directs engineering effort toward
  the operations that materially contribute to end-to-end latency,
  helping prevent wasted cycles on components with negligible
  impact on user experience.
- Span-level attribution reduces mean-time-to-resolution for
  production incidents by pinpointing whether slow responses
  originate in inference, tool calls, retrieval, or inter-agent
  coordination.
- Historical telemetry data supports informed model selection,
  routing, and capacity planning by comparing latency, token, and
  cost profiles across models and architectures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Comprehensive agent telemetry means capturing metrics, traces, and
logs, as well as structuring them so every step of the reasoning
pipeline is individually attributable. If any step of the agent's
multiple and unique operations is opaque, performance
investigations become less data-based and therefore less useful.

[OpenTelemetry
(OTel)](https://opentelemetry.io/ "https://opentelemetry.io/") is the portable substrate for this instrumentation,
and its
[generative
AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/ "https://opentelemetry.io/docs/specs/semconv/gen-ai/") define standard attributes for LLM
operations, model, input and output tokens, request parameters,
and finish reasons so that spans remain comparable across
frameworks, models, and runtimes. Using these conventions rather
than framework-specific schemas keeps telemetry portable when an
agent moves between Amazon Bedrock AgentCore Runtime, AWS Lambda,
Amazon ECS, Amazon EKS, or self-hosted infrastructure, and helps
prevent a rewrite every time the deployment target changes.

Agent telemetry has a natural three-tier hierarchy documented in
[AgentCore
Observability](../../../bedrock-agentcore/latest/devguide/observability-telemetry.md "../../../bedrock-agentcore/latest/devguide/observability-telemetry.md").

1. A _session_ represents a complete user
   conversation
2. A _trace_ represents one request-response
   cycle within the session
3. _Spans_ represent discrete operations
   inside a trace, a reasoning iteration, an LLM call, a tool
   invocation, a memory lookup, a retrieval query, or an
   inter-agent handoff

Organizing telemetry against this hierarchy turns an opaque slow
agent signal into an attributable execution tree where each span
carries its own latency, token counts, error status, and
contextual attributes. Session identifiers must flow through every
span so a trace can be linked back to its conversation, and trace
context must propagate across agent and tool boundaries using the
[W3C Trace
Context](https://www.w3.org/TR/trace-context/ "https://www.w3.org/TR/trace-context/") standard so asynchronous and multi-service
workflows remain a single connected graph.

Instrumentation approaches differ by runtime, but the resulting
telemetry should look the same. For agents on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), the runtime auto-instruments
agent code and emits OTel-compatible traces, runtime metrics
(invocations, session count, latency, errors, CPU and memory
usage), and structured logs to Amazon CloudWatch without
additional work.

For agents on other runtimes, the
[AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction") exports traces, metrics,
and logs to CloudWatch using the same semantic conventions so both
populations appear in a unified observability surface.

Framework-level instrumentation libraries such as OpenInference,
OpenLLMetry, OpenLit, and Traceloop emit the reasoning-pipeline
spans, reasoning iterations, prompt and response content,
tool-selection decisions, that generic runtime instrumentation
can't see. Select a framework based on the agent framework in use
(for example, Strands Agents, LangChain, LangGraph, CrewAI, or
LlamaIndex).

On the ingestion side,
[Amazon CloudWatch Transaction Search](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md") ingests 100 percent of spans
as structured logs in the aws/spans log group
and indexes a configurable percentage as trace summaries,
supporting end-to-end trace search without forcing sampling at the
span level. Enabling
[CloudWatch
Application Signals](../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md "../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md") on Amazon Bedrock API calls
automatically populates OTel GenAI attributes,
gen_ai.system,
gen_ai.request.model,
gen_ai.usage.input_tokens,
gen_ai.usage.output_tokens,
gen_ai.response.finish_reasons, so token, cost,
and finish-reason analysis is available without hand-written
spans.

Some signals may not be captured implicitly, such as task success
and failure rate, cache hit rate, tool-selection accuracy,
time-to-first-token, and cost per task. For these signals, emit
them as CloudWatch custom metrics from the agent or the OTel
collector, dimensioned uniformly (agent ID, workflow, environment,
task type, model ID) so they can be correlated with the spans they
originated from and consumed by dashboards, SLOs, and anomaly
detection downstream.

### Implementation steps

1. **Define a standardized telemetry
   schema:** Document the span types the agent will
   emit (reasoning iteration, LLM inference, tool invocation,
   memory operation, retrieval, inter-agent handoff) and the
   required attributes for each, aligning LLM spans with the
   [OpenTelemetry
   generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/ "https://opentelemetry.io/docs/specs/semconv/gen-ai/") and agent spans
   with the
   [GenAI
   agent span conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/ "https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/"). Specify a consistent set of
   metric dimensions, agent ID, workflow, environment, task
   type, model ID, that every custom metric and span must carry
   so signals remain correlatable across the stack.
2. **Instrument the reasoning pipeline
   across every execution layer:** Wrap reasoning
   iterations, LLM inference, tool invocations, memory
   operations, retrieval queries, and inter-agent handoffs as
   OpenTelemetry spans. For agents on Amazon Bedrock AgentCore
   Runtime, the runtime auto-instruments agent code when
   [AgentCore
   Observability](../../../bedrock-agentcore/latest/devguide/observability-configure.md "../../../bedrock-agentcore/latest/devguide/observability-configure.md") is enabled. For agents on other
   runtimes, use the
   [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction") together with a
   framework-specific instrumentation library (OpenInference,
   OpenLLMetry, OpenLit, or Traceloop) so reasoning-pipeline
   spans are captured rather than only request-level spans.
3. **Propagate trace and session context
   across every boundary:** Carry
   [W3C
   Trace Context](https://www.w3.org/TR/trace-context/ "https://www.w3.org/TR/trace-context/") headers through every outbound call the
   agent makes, tool invocations, retrieval queries,
   inter-agent handoffs, asynchronous queue-backed work, so a
   single user request produces a single connected trace rather
   than disconnected fragments. Propagate the session
   identifier through OpenTelemetry baggage so every span in a
   conversation can be linked back to its session for
   conversation-level analysis.
4. **Enable CloudWatch ingestion for
   spans and Amazon Bedrock API attributes:** Complete
   the one-time setup for
   [CloudWatch
   Transaction Search](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.md") so 100 percent of spans are
   ingested as structured logs and a configurable percentage
   are indexed as trace summaries. Enable
   [CloudWatch
   Application Signals with GenAI attribute support](../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md "../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md") to
   auto-populate OTel GenAI attributes on Amazon Bedrock API
   calls so token, model, and finish-reason data is captured
   without custom instrumentation.
5. **Emit custom metrics for signals not
   captured natively:** Publish task success and
   failure rate, cache hit rate, tool-selection accuracy,
   time-to-first-token, and cost per task as
   [CloudWatch
   custom metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md") from the agent runtime or the OTel
   collector, using the standard dimension set defined in step
6. Without these, observability tooling can display
   infrastructure and inference signals but can't answer
   product-level questions about agent quality or unit
   economics.
7. **Build the observability
   surface:** Use the
   [Amazon CloudWatch generative AI observability dashboard](../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md "../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md") to
   provide session, trace, and agent views for incident triage
   and trend analysis, and publish composed dashboards for
   per-workflow, per-model, and per-tenant slices using the
   standard dimension set.

## Resources

**Related best practices:**

- [AGENTPERF01-BP01 Define
  performance-aligned success criteria for agent
  workloads](agentperf01-bp01.md "agentperf01-bp01.md")
- [AGENTPERF01-BP03
  Profile end-to-end agent latency and identify optimization
  targets](agentperf01-bp03.md "agentperf01-bp03.md")
- [AGENTOPS05-BP01
  Establish end-to-end tracing and telemetry for agent
  operations](agentops05-bp01.md "agentops05-bp01.md")
- [AGENTOPS05-BP05
  Create workflow-specific dashboards for operational
  health](agentops05-bp05.md "agentops05-bp05.md")
- [AGENTCOST05-BP02
  Implement distributed cost tracing for multi-agent
  workflows](agentcost05-bp02.md "agentcost05-bp02.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [Blog:
  Build trustworthy AI agents with Amazon Bedrock AgentCore
  Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/ "https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/")
- [Amazon CloudWatch generative AI observability](../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md "../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md")
- [CloudWatch
  Application Signals: Troubleshoot generative AI applications
  with OpenTelemetry GenAI attributes](../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md "../../../AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.md")
- [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction")
- [Blog:
  Observing agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/")

**Related videos:**

- [AWS re:Invent 2024 - Observability for Reliable Agentic AI with
  Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk "https://www.youtube.com/watch?v=qJxF4XfMLhk")

**Related examples:**

- [GitHub:
  Amazon Bedrock AgentCore samples, Observability
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability")

**Related tools:**

- [Strands
  Agents](https://strandsagents.com/ "https://strandsagents.com/")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-monitoring/ "https://aws.amazon.com/cloudwatch/features/application-monitoring/")
- [AWS Distro for
  OpenTelemetry (ADOT)](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/")
