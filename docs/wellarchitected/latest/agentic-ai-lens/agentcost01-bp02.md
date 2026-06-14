# AGENTCOST01-BP02 Optimize multi-agent collaboration cost through efficient handoff patterns

In multi-agent systems, the largest hidden cost is redundant context
that travels with every handoff. Structured handoff messages and
shared memory keep coordination cost proportional to task complexity
rather than conversation length.

**Desired outcome:**

- You have handoff messages carrying only the task specification,
  relevant facts, and constraints, not full conversation
  transcripts.
- You have collaborating agents sharing common context through a
  managed memory layer instead of re-transmitting it on every
  handoff.
- You track per-handoff and per-workflow coordination costs as
  distinct metrics.

**Common anti-patterns:**

- Passing full conversation history in every handoff, causing
  input token cost to scale with conversation length regardless of
  relevance to the receiving agent.
- Building deep supervisor hierarchies where multi-level nesting
  adds orchestration model invocations at each layer, so
  coordination cost exceeds execution value.
- Skipping shared memory for collaborating agents, re-transmitting
  common facts in every agent's context window and causing linear
  cost growth with agent count.
- Running multi-agent workflows without handoff cost tracking,
  reducing the risk of identification of workflows where
  coordination overhead has grown disproportionate to the
  execution work.

**Benefits of establishing this best
practice:**

- Coordination overhead stays proportional to task complexity
  rather than conversation length or agent count.
- Shared memory removes redundant context transmission, reducing
  per-handoff token cost.
- Per-handoff cost visibility enables data-driven tuning of
  multi-agent interaction patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The most expensive thing an agent can send is context the receiver
already has (or doesn't need). Every handoff that copies the full
conversation across the boundary pays again for information that
never changed. Treat handoff messages as structured summaries
containing the task specification, relevant facts, and constraints
the worker must respect.
[Amazon
Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") enables write-once, read-many
patterns where one agent stores a fact under a session ID and
actor ID, and every collaborator reads it without re-embedding it
in their own prompt.
[Amazon
Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") adds the corresponding discipline
on the tool side, using MCP-compatible Semantic Tool Selection to
present only tools relevant to the current intent rather than the
full catalog.

Context distillation means that a small model call or a Lambda
function can compress incoming context into the minimum sufficient
information for the next agent's task before the handoff crosses
the boundary. The cost of the distillation call is typically less
than the cost of repeatedly transmitting untrimmed context through
deeper workflows.

Every supervisor-worker layer adds at least one inference for
delegation and one for synthesis. Hierarchies deeper than three
levels compound that overhead quickly, and most deep hierarchies
can be flattened by replacing intermediate supervisors with direct
worker-to-worker communication through the AgentCore Runtime
Agent-to-Agent protocol. The diagnostic metric is the
orchestration-to-execution token ratio. Supervisors should consume
no more than 20% of total workflow tokens, leaving 80% for workers
doing execution. A ratio that drifts above 20% means coordination
has grown disproportionate to work.

Visibility is a prerequisite for these patterns.
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") provides distributed
tracing so agent-to-agent communication costs appear as their own
category rather than hidden inside aggregate workflow cost.
[Amazon
Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") runs in real time against
live tool-call traces and as offline test suites in CI/CD
pipelines, so redundant or unnecessary invocations are caught
early.

### Implementation steps

1. **Design structured handoff
   messages:** Replace full conversation history with
   a summary object containing the task specification, relevant
   facts, and the constraints the receiving agent must respect.
   Version the message schema so receivers can reject malformed
   handoffs.
2. **Insert context distillation at
   boundaries:** Add a small-model call or Lambda
   function that extracts minimum sufficient context before
   each handoff, so input tokens at transitions reflect current
   task needs rather than accumulated history.
3. **Configure shared memory with
   ownership rules:** Provision
   [Amazon
   Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") accessible to all
   collaborating agents, and document which agent owns writes
   to each namespace so shared state has a clear provenance.
4. **Flatten deep hierarchies:**
   Audit multi-agent workflows for supervisor-worker depth
   greater than three levels, and replace intermediate
   supervisors with direct worker-to-worker communication
   through the AgentCore Runtime Agent-to-Agent protocol where
   the routing can be made explicit.
5. **Expose specialized agents through
   Gateway:** Publish agents as tools through
   [Amazon
   Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") MCP server capabilities,
   and turn on Semantic Tool Selection so collaborating agents
   see only tools relevant to the current request.
6. **Evaluate tool-call efficiency in CI
   and in production:** Run
   [Amazon
   Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") against live tool-call
   traces to flag inefficient usage at runtime, and against
   offline test suites in the CI/CD pipeline to catch
   regressions before deployment.
7. **Track the orchestration-to-execution
   ratio:** Tag every invocation with workflow-id and
   agent-role, build CloudWatch dashboards that display the
   supervisor-to-worker token ratio per workflow, and configure
   AWS Budgets alerts when orchestration overhead exceeds 20%
   of total workflow token cost.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01 Use
  the reflection pattern to design efficient agent reasoning
  loops](agentcost01-bp01.md "agentcost01-bp01.md")
- [AGENTCOST01-BP03
  Implement cost-effective patterns like hybrid supervisor for
  multi-agent coordination](agentcost01-bp03.md "agentcost01-bp03.md")
- [AGENTCOST01-BP04 Design
  agent hierarchies and delegation patterns that reduce
  coordination overhead](agentcost01-bp04.md "agentcost01-bp04.md")
- [AGENTCOST05-BP02
  Implement distributed cost tracing for multi-agent
  workflows](agentcost05-bp02.md "agentcost05-bp02.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md")
- [Amazon
  Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md")
- [Amazon
  Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md")
- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [Amazon
  Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md")
- [Agentic
  AI patterns and workflows on AWS](../../../prescriptive-guidance/latest/agentic-ai-patterns/introduction.md "../../../prescriptive-guidance/latest/agentic-ai-patterns/introduction.md")

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA "https://www.youtube.com/watch?v=-N4v6-kJgwA")
- [AWS re:Invent 2024 - Balance cost, performance & reliability
  for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE "https://www.youtube.com/watch?v=Lwvv8Q33eeE")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Multi-agent
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts")
- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Evaluations
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
