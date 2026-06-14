# AGENTREL04-BP04 Implement resilient control planes for agent coordination

A control plane that fails takes every agent with it. Applying the
same reliability principles used on agents, redundancy, durable
state, and loose coupling, to the coordination infrastructure keeps
workflows running during brief outages and preserves state across
restarts.

**Desired outcome:**

- You deploy agents on managed, highly available execution
  infrastructure with multi-AZ redundancy.
- You persist workflow state durably so the control plane can
  recover without losing progress.
- You design agents to complete in-flight work during brief
  control plane outages rather than failing immediately.

**Common anti-patterns:**

- Implementing the control plane as a single point of failure
  without redundancy, so outages take down the entire multi-agent
  system.
- Holding control plane state in ephemeral memory, losing
  coordination state whenever the control plane restarts.
- Coupling agent execution tightly to control plane availability,
  reducing the ability for agents to complete in-progress work
  during brief outages.

**Benefits of establishing this best
practice:**

- Multi-agent workflows keep running through control plane
  component failures.
- Durable state persistence reduces workflow state loss during
  outages.
- Loose coupling keeps agents productive during brief control
  plane unavailability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AgentCore Runtime is designed as a regional service. Architect
your agents assuming the underlying compute is distributed across
Availability Zones, but validate this assumption for your specific
workload by confirming endpoint behavior during AZ impairment
(e.g., using AZ-isolated canary deployments). Don't rely solely on
service-level redundancy. Implement your own cross-AZ resilience
patterns (multi-AZ deployment of agent orchestrators, regional
failover for stateful components) to maintain availability targets
independent of any single service's internal architecture.

Durable state keeps recovery clean.
[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") persists execution state at every
transition, providing built-in retry, error handling, and
resume-from-failure semantics for workflows that need explicit
state machines. Without durable state, every control plane restart
requires agents to recover the coordination context themselves,
which is error-prone and often incomplete.

Loose coupling is the third property, and the hardest to build in
after the fact. Agents should complete in-flight tasks
independently if the control plane is briefly unavailable, rather
than failing immediately on loss of connectivity. Heartbeat
mechanisms let agents periodically report status so the control
plane can detect missed heartbeats and reassign tasks, catching
the cases where an agent has genuinely stopped responding. Monitor
the AgentCore Runtime /ping endpoint for each
agent as the liveness signal, and configure the orchestration
layer to reassign tasks when agents stop responding. Composite
alarms through
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") aggregate signals across
coordination components. Regular disaster recovery exercises
validate that automated failover actually works when you need it.

### Implementation steps

1. **Deploy agents on AgentCore
   Runtime:** Use
   [Amazon
   Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") as the primary execution
   infrastructure for its built-in multi-AZ redundancy.
2. **Use AWS Step Functions for explicit
   workflow state machines:** Run workflows on
   [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") for durable state persistence and
   automatic recovery.
3. **Use AgentCore Gateway for agent
   discovery and invocation:** Route agent calls
   through
   [Amazon
   Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") for its built-in
   availability characteristics.
4. **Design agents to complete in-flight
   work during brief control plane outages:** Avoid
   patterns that require constant control plane connectivity.
5. **Implement agent liveness detection
   through the AgentCore Runtime /ping
   endpoint:** Monitor the endpoint for each agent and
   reassign tasks through the orchestration layer when agents
   stop responding.
6. **Run regular disaster recovery
   exercises:** Use
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") composite alarms and
   periodic DR drills to validate automated failover.

## Resources

**Related best practices:**

- [AGENTREL04-BP01
  Implement the arbiter agent pattern for coordinated
  multi-agent systems](agentrel04-bp01.md "agentrel04-bp01.md")
- [AGENTREL04-BP02 Classify
  agents with a thorough capability taxonomy](agentrel04-bp02.md "agentrel04-bp02.md")
- [AGENTREL04-BP03
  Implement fallback mechanisms and graceful degradation for
  collaborative workflows](agentrel04-bp03.md "agentrel04-bp03.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md")
- [Amazon
  Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md")
- [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md")
- [Agentic
  AI patterns and workflows on AWS](../../../prescriptive-guidance/latest/agentic-ai-patterns/introduction.md "../../../prescriptive-guidance/latest/agentic-ai-patterns/introduction.md")
- [Build
  resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents "https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents")

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
  with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc "https://www.youtube.com/watch?v=wqmeZOT6mmc")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
