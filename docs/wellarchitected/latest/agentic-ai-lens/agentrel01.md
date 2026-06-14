# Predictable agent behavior

Agents combine compute, memory, cognition, and orchestration
components, and each component is a point where a workflow can
fail. Organizations that run agents on resilient messaging,
modular fault isolation, and adaptive provisioning spend less time
repairing infrastructure and more time improving agent
capabilities.

| AGENTREL01: How do I develop reliable agentic systems? |
| ------------------------------------------------------ |
|                                                        |

## Capability intent

- Agent-to-agent and agent-to-system communication runs
  through a durable messaging substrate, so transient failures
  are absorbed through persistence, retry, and dead-letter
  handling rather than cascading across the workflow.
- Compute, memory, cognition, and orchestration operate as
  independent layers with well-defined contracts, so a surge
  or failure in one layer stays contained and the remaining
  layers keep operating in a known degraded mode.
- Specialized agents each own a single capability, their own
  state, and a narrow permission scope, so failures are
  isolated to the agent that encountered them and the broader
  environment continues running.
- Inter-agent communication follows a consistent taxonomy of
  message schemas, versioned endpoints, error formats, and
  retry policies, so agents compose into workflows without
  custom translation layers between every pair.
- Compute, inference, and model-tier allocation adapt in real
  time to workload and capacity signals, so agents maintain
  steady performance under variable load without manual
  capacity planning.

## Maturity levels

These levels summarize what each stage of maturity looks like
for predictable agent behavior as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents call each other directly over synchronous<br>channels with ad-hoc message formats and no durable<br>queue between them. A single slow or failing agent<br>cascades into the rest of the workflow, and there is no<br>consistent way to trace which hop lost a message.<br>Capacity is provisioned statically, so demand spikes<br>cause throttling and low-demand periods waste resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2     | Emerging  | Teams have introduced a messaging layer (typically<br>[Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") and<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")) for the most critical agent-to-agent<br>paths, and dead-letter queues catch repeated failures.<br>Agents run on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with basic layer<br>separation, and on-demand<br>[Amazon<br>Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") inference absorbs most capacity<br>variability. Communication schemas are documented but<br>not uniformly enforced.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3     | Defined   | Durable messaging is the default for agent-to-agent and<br>agent-to-system communication, with schemas registered<br>in<br>[EventBridge<br>Schema Registry](../../../eventbridge/latest/userguide/eb-schema-registry.md "../../../eventbridge/latest/userguide/eb-schema-registry.md") and workflows orchestrated<br>through<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md"). Specialized agents run as<br>single-purpose actors on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with scoped IAM roles,<br>communicate through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") or the<br>[A2A<br>protocol](../../../bedrock-agentcore/latest/devguide/runtime-a2a.md "../../../bedrock-agentcore/latest/devguide/runtime-a2a.md"), and expose per-agent metrics through<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"). Tiered model<br>selection routes simple tasks to smaller models and<br>reasoning-heavy work to larger ones. |
| 4     | Proactive | Fail-fast logic, fallback behaviors, and runtime<br>capability toggling are enforced automatically at layer<br>boundaries, and<br>[Amazon<br>Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md") enforces standardized<br>access control at the gateway boundary through<br>[Cedar](https://docs.cedarpolicy.com/ "https://docs.cedarpolicy.com/")<br>policies.<br>[Cross-Region<br>inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") is the default for production agents,<br>and<br>[Bedrock<br>Provisioned Throughput](../../../bedrock/latest/userguide/prov-throughput.md "../../../bedrock/latest/userguide/prov-throughput.md") underwrites<br>latency-sensitive paths. Contract tests in CI/CD help<br>prevent protocol regressions, and scheduled scaling<br>pre-provisions capacity ahead of known demand patterns.                                                                                                                                                                                                                                                                                                                                                                             |
| 5     | Optimized | The messaging substrate, layer isolation, inter-agent<br>contracts, and capacity allocation are continuously<br>recalibrated from observability data rather than revised<br>on a fixed review cadence. New workflows inherit the<br>resilience pattern by default through reusable templates<br>and shared services, and the organization contributes<br>its agent reliability patterns (messaging topology,<br>fail-fast envelopes, tiered model routing) back to its<br>communities of practice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Common issues to watch for

- Teams wire up agent-to-agent communication over direct
  synchronous calls and only discover the coupling when one
  agent's latency or failure takes the whole workflow down.
- Agent architectures ship as a single service rather than as
  separate compute, memory, cognition, and orchestration
  layers, so an issue in any component forces a full restart
  instead of a contained fix.
- Specialized agents accrete unrelated tools and broader
  system prompts over time, expanding their failure radius and
  making issues harder to reproduce as responsibilities blur.
- Message schemas, error formats, and retry policies are
  defined per agent pair rather than across the agent fleet,
  so every new agent introduces its own translation layer and
  every change risks breaking a downstream consumer.
- Capacity is provisioned for the worst case rather than
  adapted to demand. Peak traffic still produces throttling
  despite idle headroom elsewhere, and low-demand periods pay
  for unused capacity.

###### Best practices

- [AGENTREL01-BP01 Implement a resilient messaging layer](agentrel01-bp01.md "agentrel01-bp01.md")
- [AGENTREL01-BP02 Establish modular, fault-isolated layers](agentrel01-bp02.md "agentrel01-bp02.md")
- [AGENTREL01-BP03 Design specialized agents following actor model principles](agentrel01-bp03.md "agentrel01-bp03.md")
- [AGENTREL01-BP04 Standardize communication protocols](agentrel01-bp04.md "agentrel01-bp04.md")
- [AGENTREL01-BP05 Implement adaptive provisioning](agentrel01-bp05.md "agentrel01-bp05.md")
