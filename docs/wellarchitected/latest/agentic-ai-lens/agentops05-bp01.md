# AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations

When an agent produces an unexpected output, the investigation is
only as good as the telemetry. Distributed tracing that captures the
full execution path (reasoning, tool calls, memory operations, and
model invocations) enables precise reconstruction of every decision
and action.

**Desired outcome:**

- Every agent run produces a complete distributed trace covering
  the flow from request to response across all services and
  agents.
- Teams can reconstruct the exact sequence of operations for any
  run, enabling rapid debugging and targeted optimization.
- Real-time telemetry dashboards give operational teams continuous
  visibility into agent health.
- Trace data is retained on a defined policy for post-operations
  analysis and compliance.

**Common anti-patterns:**

- Instrumenting only infrastructure metrics (Lambda duration, API Gateway latency) without capturing agent-specific spans for
  reasoning steps, tool invocations, and memory operations.
- Implementing tracing without propagating trace context across
  agent boundaries, producing disconnected trace fragments that
  can't be correlated into end-to-end workflows.
- Capturing telemetry without standardized schemas, making it
  impossible to query consistently across agents or compare
  behavior across versions.
- Retaining traces forever because no one defined a policy, or
  retaining them too briefly to support quarterly trend analysis.

**Benefits of establishing this best
practice:**

- Distributed tracing makes agent operations like decisions and
  actions queryable.
- Detailed telemetry provides the empirical foundation for
  optimization, identifying bottlenecks and validating
  improvements with data.
- Trace context propagation across agent boundaries makes
  multi-agent workflow debugging tractable.
- Standardized schemas enable cross-agent comparison and
  version-over-version regression analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") is the default telemetry
service for agents on AgentCore Runtime. Its
OpenTelemetry-compatible instrumentation automatically captures
LLM inference calls, tool invocations, and memory operations
without requiring each agent to add its own spans. For agents
built on Strands Agents or custom frameworks, the agent loop
itself needs instrumentation. OpenTelemetry spans wrapping each
operation phase make the trace complete.

Trace context propagation separates useful traces from fragmented
ones. W3C Trace Context propagation across all agent boundaries
maintains continuity in distributed workflows, so a request that
passes through five agents produces one trace with five spans, not
five disconnected traces. Without propagation, multi-agent
debugging becomes manual correlation by timestamp, which scales
poorly and produces incorrect answers when concurrent requests
overlap.

Standardized span schemas produce queryable data from your
telemetry. Each span type needs defined fields, like model ID and
token counts for inference, tool name and latency for invocations,
and iteration count for reasoning. Store telemetry in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") Logs with structured JSON so dashboards and
queries work against named fields. Configure sampling to capture
100% of error traces and a configurable percentage of successful
traces. This balances visibility with cost, and errors are not
dropped.

### Implementation steps

1. **Instrument agents with OpenTelemetry
   spans:** Deploy on
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") or add manual
   instrumentation covering all operation phases (reasoning,
   tool calls, memory operations).
2. **Propagate W3C Trace Context across
   agent boundaries:** Carry trace context forward on
   every agent-to-agent, agent-to-tool, and agent-to-service
   call.
3. **Define standardized telemetry
   schemas:** Specify fields for each span type, and
   log in structured JSON for efficient
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") Logs queries.
4. **Build end-to-end
   dashboards:** Visualize agent performance with
   drill-down to individual trace components.
5. **Set retention policies:**
   Balance visibility with storage cost, with different tiers
   for operational, compliance, and debug telemetry.

## Resources

**Related best practices:**

- [AGENTOPS05-BP02 Monitor
  agent behavior patterns and detect anomalies](agentops05-bp02.md "agentops05-bp02.md")
- [AGENTOPS05-BP03
  Implement structured logging and comprehensive audit
  trails](agentops05-bp03.md "agentops05-bp03.md")
- [AGENTOPS04-BP03
  Develop fallback behavior and error handling for tool
  invocations](agentops04-bp03.md "agentops04-bp03.md")
- [AGENTPERF01-BP02
  Implement comprehensive performance telemetry](agentperf01-bp02.md "agentperf01-bp02.md")
- [AGENTREL07-BP03
  Implement distributed tracing to track system dependencies and
  facilitate recovery](agentrel07-bp03.md "agentrel07-bp03.md")

**Related documents:**

- [Getting
  started with Amazon Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability-get-started.md "../../../bedrock-agentcore/latest/devguide/observability-get-started.md")
- [Operationalizing
  agentic AI on AWS](../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.md "../../../prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.md")
- [Observing
  agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/")
- [Observability
  and monitoring for serverless agentic AI on AWS](../../../prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.md "../../../prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.md")

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
  OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k "https://www.youtube.com/watch?v=wWQgawUPr1k")
- [AWS re:Invent 2024 - Observability for Reliable Agentic AI with
  Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk "https://www.youtube.com/watch?v=qJxF4XfMLhk")
- [AWS re:Invent 2024 - Build observable AI agents with Strands,
  AgentCore, and Datadog (AIM233)](https://www.youtube.com/watch?v=mOAd8grR1BU "https://www.youtube.com/watch?v=mOAd8grR1BU")
- [AWS 2025 - Strands Agents Observability, Evaluation, &
  Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE "https://www.youtube.com/watch?v=VgN-6_tmQHE")

**Related workshops:**

- [Getting
  started with Amazon Bedrock AgentCore, Lab 4: Deploy to
  Production](https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime "https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime")
- [Diving
  Deep into Bedrock AgentCore, Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability "https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability")

**Related tools:**

- [Strands
  Agents](https://strandsagents.com/ "https://strandsagents.com/")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [AWS X-Ray](https://aws.amazon.com/xray/ "https://aws.amazon.com/xray/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
