# AGENTREL05-BP01 Design modular, fault-tolerant agentic reasoning components

A monolithic reasoning pipeline fails completely whenever any stage
fails. Splitting cognition into modular stages with clear interfaces
and stage-specific fallbacks lets an agent keep reasoning, with
reduced quality, even when one stage is degraded.

**Desired outcome:**

- You have the reasoning pipeline decomposed into modular stages
  with explicit input/output schemas.
- You have stage-specific fallbacks that activate automatically
  when error rates climb.
- You log the retrieval tier and model tier used in each
  invocation so quality analysis is possible after the fact.

**Common anti-patterns:**

- Running agent cognition as a monolithic pipeline where any
  component failure causes complete cognition failure.
- Skipping interfaces between reasoning components, reducing the
  ability for independent testing and replacement.
- Treating all reasoning components as equally critical without
  distinguishing essential from quality-enhancing components.

**Benefits of establishing this best
practice:**

- Partial cognition survives individual component failures through
  modular fault isolation.
- Reasoning components can be optimized or replaced independently,
  without full pipeline rewrites.
- Clear component boundaries isolate the source of errors and
  speed up debugging.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The first architectural decision is where the stage boundaries go.
Useful boundaries for most agents are context retrieval, prompt
construction, model inference, output parsing, and action
selection. Each stage has a narrow contract: inputs, outputs, and
the error conditions it signals. Deploy each stage on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with its own error handling and
fallback behavior. Without this decomposition, all errors appear
as generic reasoning failures, making debugging difficult. Clear
stage boundaries enable precise error identification and faster
resolution.

Tiering is where the stages earn their modularity. For context
retrieval, primary tier uses
[Amazon
Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") for semantic search, with fallback
to simpler retrieval methods when the primary is unavailable. For
model inference, implement model tier fallback using
[Bedrock
cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") for availability, substituting
alternative models when the primary is degraded. For multimodal
agents,
[Amazon
Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md") preprocesses documents, images,
audio, and video as a distinct reasoning stage before text-based
reasoning, with independent fallbacks per modality.

Track per-stage error rates, latency, and fallback activation
frequency through
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"). Configure alarms that
trigger automatic cutoffs when stage health degrades. The cutoff
activates the fallback immediately rather than waiting for the
next failed invocation. Log the retrieval tier and model tier used
in each invocation so you can see, months later, which tier
produced the answer and whether the fallback path is being taken
more often than expected.

### Implementation steps

1. **Decompose the reasoning pipeline
   into distinct stages:** Define explicit
   input/output schemas and deploy each stage on
   [Amazon
   Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md").
2. **Implement automatic cutoffs between
   stages:** Activate stage-specific fallbacks when
   error rates exceed thresholds.
3. **Build tiered context
   retrieval:** Use
   [Amazon
   Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") as primary with progressively
   simpler fallbacks.
4. **Implement model tier
   fallback:** Use
   [Bedrock
   cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") for availability during
   primary model degradation.
5. **Monitor per-stage health:**
   Track error rates, latency, and fallback activation through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") with alarms that
   trigger automatic cutoffs.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
  Establish modular, fault-isolated layers](agentrel01-bp02.md "agentrel01-bp02.md")
- [AGENTREL05-BP02
  Facilitate reliable adaptation through evaluation-driven
  improvement cycles](agentrel05-bp02.md "agentrel05-bp02.md")
- [AGENTREL05-BP03 Ground
  agent cognition in real information](agentrel05-bp03.md "agentrel05-bp03.md")

**Related documents:**

- [Amazon
  Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md")
- [Amazon
  Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md")
- [Amazon
  Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md")
- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [AWS fail-fast pattern](../../../prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.md "../../../prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.md")
- [Strands
  Agents Agent Loop](https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/ "https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/")

**Related videos:**

- [AWS re:Invent 2024 - Using Strands Agents to build autonomous,
  self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk "https://www.youtube.com/watch?v=RQfW7eQsXqk")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Runtime
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime")

**Related tools:**

- [Strands
  Agents](https://strandsagents.com/ "https://strandsagents.com/")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
