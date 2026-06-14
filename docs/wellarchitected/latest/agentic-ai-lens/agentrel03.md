# Agent memory and state management

Agents that classify, persist, and recover memory reliably deliver
consistent behavior across sessions and maintain functionality
even during component failures. Agent memory is beholden to the
same reliability considerations of any data store. How do you
support returning the right information, and how does the agent
behave when state is unavailable?

| AGENTREL03: How do you support agent memory and state<br>remaining reliably accessible throughout the agent<br>lifecycle? |
| ------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                           |

## Capability intent

- Agent memory is explicitly classified by scope and
  persistence, so short-term session context never
  contaminates long-term knowledge and retrieval is
  predictable across task types.
- Memory stores are redundant and have automated failover
  paths, so individual component failures produce degraded but
  usable memory rather than complete outages.
- Long-running workflows persist checkpoints at stage
  boundaries and resume from the last known-good state after
  interruption, rather than restarting from zero.
- Agents detect degraded memory conditions, transition into
  well-defined reduced modes, and communicate their current
  capabilities transparently to users and orchestration
  systems.
- Memory and state health are instrumented as first-class
  telemetry, so retrieval quality, failover activations, and
  checkpoint lifecycle are observable and operationally
  tunable.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent memory and state management as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Agent memory sits in a single undifferentiated store<br>with no classification, no retention policy, and no<br>failover plan. Long-running workflows restart from zero<br>on any failure because no state is persisted between<br>steps. Memory outages are indistinguishable from agent<br>outages because there is no degraded mode to fall back<br>to, and memory health is reviewed only after an<br>incident.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2     | Emerging  | Teams have separated short-term and long-term memory,<br>typically using<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") session-scoped and<br>persistent namespaces. Basic retention policies are in<br>place for short-term memory, and some long-running<br>workflows persist checkpoint state explicitly.<br>Redundancy and failover rely on managed service<br>defaults, and failure modes are tested only as part of<br>major release readiness reviews.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3     | Defined   | A documented memory taxonomy (session context,<br>persistent knowledge, episodic records) drives<br>classification at ingestion time, and<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") supplements agent memory<br>with organizational corpora for retrieval-augmented<br>generation. Multi-step workflows are orchestrated<br>through<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") or equivalent state machines with<br>idempotent steps, so recovery is a cheap replay from the<br>last checkpoint.<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") reports retrieval<br>quality and checkpoint health, and mode transitions for<br>graceful degradation follow written runbooks. |
| 4     | Proactive | Fail-fast logic routes memory access to fallback stores<br>or in-process caches when primary stores misbehave, and<br>read-through caches serve long-term memories during<br>temporary unavailability. Mode transitions for graceful<br>degradation (full, session-only, stateless) are<br>automated from memory health metrics, and recovery<br>detection returns agents to full mode without human<br>intervention.<br>[AWS Fault Injection Service](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md") experiments against the<br>memory layer run on a schedule, and checkpoint lifecycle<br>is managed through TTL-based expiration rather than<br>manual cleanup.                                                                                                                                                                                                                                                                                  |
| 5     | Optimized | Memory classification, retention, and checkpoint<br>policies are tuned continuously from observability data<br>rather than through periodic reviews. Cross-agent shared<br>memory, tiered retrieval, and reranking strategies are<br>recalibrated on measured retrieval quality, and<br>chaos-engineering results drive design changes in memory<br>topology rather than one-time fixes. Memory-related<br>failure modes surface in telemetry and dashboards before<br>they affect users, and the organization contributes<br>memory and state patterns back to its internal<br>communities of practice.                                                                                                                                                                                                                                                                                                                                                                                   |

## Common issues to watch for

- Teams store all agent memory in a single undifferentiated
  tier, so retrieval returns stale intermediate reasoning
  alongside stable domain facts and degrades task quality
  silently.
- Long-running workflows lack checkpointing, so any transient
  failure forces a full restart and the workflow pays its full
  cost every time something goes wrong.
- Workflow steps are not idempotent, so checkpoint-based
  replay produces duplicate side effects rather than safely
  resuming work.
- Memory outages are treated as agent outages because there is
  no degradation hierarchy, and users see confusing errors
  instead of clearly communicated reduced capability.
- Failover paths exist only on paper, and gaps in redundancy
  and recovery are discovered during production incidents
  because fault-injection testing isn't part of the release
  process.

###### Best practices

- [AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories](agentrel03-bp01.md "agentrel03-bp01.md")
- [AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover](agentrel03-bp02.md "agentrel03-bp02.md")
- [AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery](agentrel03-bp03.md "agentrel03-bp03.md")
- [AGENTREL03-BP04 Implement graceful degradation for memory and state operations](agentrel03-bp04.md "agentrel03-bp04.md")
