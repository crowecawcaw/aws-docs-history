# Secure agent memory and state

One reason agentic AI is effective is the ability to perform
long-running tasks. To achieve a goal, agents need to store
context, tasks, and results. Agent memory systems can be targeted
to introduce false information or influence agent decisions, so
securing memory and state helps maintain agent integrity.

| AGENTSEC01: How do you secure agentic memory and securely<br>manage state between agents? |
| ----------------------------------------------------------------------------------------- |
|                                                                                           |

## Capability intent

- Agent memory is partitioned along the isolation axes that
  matter for the workload, with each principal restricted to
  the namespaces its task requires.
- Tamper detection runs on every memory read, and an
  append-only versioned history supports forensic replay when
  a poisoning attempt is suspected.
- Every write path into memory, including user inputs, tool
  outputs, inter-agent messages, and consolidation, passes
  through a layered validation pipeline before data reaches
  the store.
- Hallucinations are detected and contained before they
  cascade across sessions or propagate to downstream agents in
  a multi-agent workflow.
- Memory operations are monitored continually, and anomalous
  access or injection signals are routed to the incident
  response pipeline for review.

## Maturity levels

These levels summarize what each stage of maturity looks like
for secure agent memory and state as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Memory is shared across agents, users, or sessions with<br>no namespace partitioning, stored without encryption,<br>and written without validation. Hallucinations propagate<br>unchecked, cross-session contamination is<br>indistinguishable from normal operation, and there is no<br>tamper detection on reads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2     | Emerging  | Memory is partitioned per session or per user with basic<br>identity and access management (IAM) scoping on the<br>store, and encryption at rest is turned on. Syntactic<br>validation checks types, lengths, and formats before<br>memory writes, and memory events flow to centralized<br>logs. Detection is largely reactive and depends on human<br>review.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3     | Defined   | Memory resources use hierarchical namespace schemas, for<br>example<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") with per-actor and<br>per-session placeholders, to partition data<br>automatically. Multi-layer validation combines schema<br>checks with<br>[Amazon<br>Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") for policy enforcement and<br>personally identifiable information (PII) filtering, and<br>[contextual<br>grounding checks](../../../bedrock/latest/userguide/guardrails-contextual-grounding-check.md "../../../bedrock/latest/userguide/guardrails-contextual-grounding-check.md") run on high-stakes outputs<br>before consolidation. |
| 4     | Proactive | Cryptographic integrity verification using HMAC<br>signatures backed by<br>[AWS KMS](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") runs on every memory read. All write paths<br>share the same validation pipeline, including tool<br>outputs and inter-agent messages. Anomaly detection in<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") alarms on unusual access patterns, and<br>a hallucination circuit breaker broadcasts through<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") to quarantine affected entries across<br>downstream agents.                                          |
| 5     | Optimized | Memory architecture is validated through routine<br>red-team exercises that simulate poisoning and<br>propagation. Validation policies and grounding<br>thresholds adapt based on observed patterns, and<br>detection signals feed directly into automated<br>containment. Memory governance is codified and<br>auditable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Common issues to watch for

- Shared namespaces treated as the default rather than an
  explicit design decision, so one affected session can read
  or overwrite context that belongs to a different user or
  tenant.
- Validation applied only at the public API boundary, whereas
  tool outputs, inter-agent messages, and consolidation writes
  bypass the pipeline. This creates a blind spot for content
  that originates inside the agent system.
- Model outputs written directly into long-term memory without
  grounding checks, so hallucinated facts persist across
  sessions and compound because each agent builds its
  reasoning chain on fabricated context from earlier runs.
- Monitoring that captures memory events but routes no signals
  into alerts or incident response, so poisoning and
  propagation are discovered only during post-incident review.
- Memory access policies that are set once at deployment and
  never revisited, so permissions drift as the agent system
  evolves and the least-privilege posture decays over time.

###### Best practices

- [AGENTSEC01-BP01 Implement memory isolation and integrity controls](agentsec01-bp01.md "agentsec01-bp01.md")
- [AGENTSEC01-BP02 Validate and sanitize memory inputs](agentsec01-bp02.md "agentsec01-bp02.md")
- [AGENTSEC01-BP03 Monitor for hallucination propagation](agentsec01-bp03.md "agentsec01-bp03.md")
