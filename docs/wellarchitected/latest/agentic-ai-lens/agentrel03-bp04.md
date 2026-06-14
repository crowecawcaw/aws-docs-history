# AGENTREL03-BP04 Implement graceful degradation for memory and state operations

Treating every memory failure as fatal turns recoverable issues into
total outages. An explicit degradation hierarchy with documented
modes and automatic recovery keeps agents partially useful and
transparent about their reduced state.

**Desired outcome:**

- You have a memory degradation hierarchy with distinct
  operational modes and documented behaviors for each.
- You transition modes automatically based on memory health
  signals, and recover to full mode when stores return.
- You communicate degradation state to users and orchestration
  systems so they know what to expect.

**Common anti-patterns:**

- Treating all memory failures as fatal, producing complete
  unavailability for conditions that could be handled with reduced
  functionality.
- Failing to communicate degraded memory state to users, who then
  get confused when responses lack expected context.
- Implementing degradation without a recovery path, leaving agents
  in degraded mode indefinitely after primary stores return.

**Benefits of establishing this best
practice:**

- Partial service availability persists through memory store
  failures instead of becoming a full outage.
- Users and orchestrators see transparent indications of current
  capability.
- Full capability returns automatically when memory stores come
  back online.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with the mode hierarchy. Three modes cover most agent
workloads. Full mode has all memory tiers available. Session-only
mode operates without long-term memory, using only session
context. Stateless mode has both tiers unavailable and processes
each request independently. For each mode, define the agent's
behavior explicitly:

- In session-only mode, inform users that previous session
  context is unavailable
- In stateless mode, request all necessary context within the
  current interaction.

Without this definition, the fallback path is whatever the code
happens to do, which is rarely what you want during an incident.

Health signals drive the transitions.
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") and Amazon CloudWatch
together track memory store availability and error rates.
Configure automated mode transitions when health degrades below
thresholds you set in advance, and automatic recovery when stores
return. For short-term memory degradation, in-process fallback
caches let the current session continue.
[Amazon
Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") session management maintains
working context even when long-term stores are degraded, which
keeps most conversations coherent through a partial outage.

Communicate degradation state through structured status indicators
so users and downstream systems understand the current
limitations. "I don't have access to your previous
conversations right now" is a better experience than an
agent that silently pretends it does and hallucinates. The same
signals feed orchestration systems that might choose to route
requests elsewhere or surface a banner to users.

### Implementation steps

1. **Define a memory degradation
   hierarchy with documented modes:** Specify full,
   session-only, and stateless modes, with the agent behavior
   each mode dictates.
2. **Implement automated mode
   transitions:** Trigger transitions through health
   metrics from
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") and Amazon CloudWatch.
3. **Maintain in-process fallback caches
   for short-term memory:** Allow active sessions to
   continue when short-term memory degrades.
4. **Communicate degradation state to
   users:** Surface structured status indicators so
   users see the reduced capability instead of guessing.
5. **Configure automatic recovery
   detection:** Return agents to full mode when stores
   become available, without operator intervention.

## Resources

**Related best practices:**

- [AGENTREL03-BP01 Design
  an information classification model to identify short-term and
  long-term memories](agentrel03-bp01.md "agentrel03-bp01.md")
- [AGENTREL03-BP02
  Architect fault-tolerant memory stores with redundancy and
  failover](agentrel03-bp02.md "agentrel03-bp02.md")
- [AGENTREL08-BP04
  Track agent memory utilization metrics](agentrel08-bp04.md "agentrel08-bp04.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md")
- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")
- [Build
  resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents "https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Memory
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
