# Legacy system integration

Agents that integrate with existing systems through adapter
patterns and abstraction interfaces preserve legacy system
stability while enabling automation of established workflows.
These systems might not be optimized for agent interactions and
might require support for protocols such as MCP or A2A. How do
agents integrate effectively without impacting the reliability of
established processes?

| AGENTREL06: How do agents integrate effectively with<br>existing systems without impacting the reliability of<br>established processes? |
| --------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                         |

## Capability intent

- Legacy systems are reached through adapter interfaces that
  expose agent-native tool contracts, so agents don't need to
  understand the protocols behind them.
- Legacy systems are protected from agent-native invocation
  patterns through rate limiting and access control applied at
  the adapter layer.
- Every legacy dependency has a defined fallback path, so
  legacy outages cause reduced capability rather than complete
  agent failure.
- Agent operations with side effects are idempotent, so
  retry-based recovery is safe and doesn't produce duplicate
  transactions or inconsistent state.
- Operators can disable and re-enable individual capabilities
  at runtime without redeployment, and each capability has a
  tested fallback behavior that activates when it is toggled
  off.
- Resilience mechanisms are exercised regularly through fault
  injection and game days, so gaps are discovered in testing
  rather than during production incidents.

## Maturity levels

These levels summarize what each stage of maturity looks like
for legacy system integration as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents call legacy systems directly without adapter<br>layers, so legacy error codes and protocol quirks leak<br>into agent logic. There are no explicit fallbacks, so<br>legacy outages cascade into complete agent failure.<br>Retries are applied without idempotency, which can<br>produce duplicate transactions, and disabling a<br>problematic capability requires redeployment. Resilience<br>is assumed rather than tested.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2     | Emerging  | Integration adapters are introduced for the most<br>critical legacy systems, exposing tool interfaces that<br>translate to legacy protocols internally. One-time<br>fallbacks are added after the first outages reveal the<br>need, and retries start using idempotency keys for a<br>small set of high-risk operations. Teams occasionally<br>run manual failure tests before major releases.<br>Telemetry on adapter health is partial and varies by<br>system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 3     | Defined   | Adapters are registered in<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") with a canonical error<br>taxonomy, so agents handle legacy failures consistently.<br>Each legacy dependency has a matched fallback strategy:<br>cache-based for reference data, queue-based for<br>transactional operations through<br>[Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md"), and graceful degradation for real-time data.<br>Idempotency is implemented through<br>[Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") conditional writes and TTL-based<br>expiration, and capability toggling through<br>[Amazon<br>Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md") Cedar policies allows<br>runtime control.<br>[AWS Fault Injection Service](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md") experiments run on a<br>defined schedule. |
| 4     | Proactive | Legacy integration health is monitored through<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") with alarms that<br>trigger automatic cutoffs using<br>[AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") circuit breaker logic, and recovery probes<br>re-enable access when systems recover. Idempotency keys<br>propagate through multi-step workflows and are passed to<br>external systems that support native idempotency.<br>Fallback behaviors are tested alongside primary<br>implementations, and fallback activation rates feed a<br>continuous prioritization of legacy reliability<br>investment. FIS experiments are part of CI/CD, and<br>quarterly game days validate runbooks under realistic<br>conditions.                                                                                                                                                                                                                                                                                                                                                                           |
| 5     | Optimized | Adapter patterns, fallback strategies, and idempotency<br>mechanisms are standardized across the organization and<br>continuously refined based on operational data.<br>Capability toggles, fallback activation rates, and<br>legacy health trends are integrated into decision-making<br>for legacy modernization investment. Self-healing<br>behavior (automatic cutoff, graceful degradation, and<br>recovery) is the default, and game days rehearse<br>multi-system failures rather than single-service<br>outages. The organization publishes internal patterns<br>for agent-to-legacy integration and shares benchmarks<br>across teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Common issues to watch for

- Agents couple directly to legacy interfaces without adapter
  layers, so legacy protocol changes ripple through agent code
  and every agent handles legacy error codes in its own way.
- Legacy dependencies are assumed to have the reliability of
  cloud-based services, so no fallback paths exist and a
  single legacy outage causes complete agent failure.
- Retries are applied without idempotency guarantees, so
  recovery from transient failures creates duplicate
  transactions, corrupted state, or silent inconsistency.
- Disabling a problematic capability requires code changes and
  redeployment, which extends time-to-remediation during
  incidents and discourages cutting off misbehaving features.
- Automatic cutoffs open on failure but never close after
  recovery because no probe re-enables access, leaving
  capability degraded long after the legacy system is healthy
  again.
- Resilience mechanisms are never exercised, so fallback
  paths, runbooks, and alerting are only tested for the first
  time during a real incident.

###### Best practices

- [AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems](agentrel06-bp01.md "agentrel06-bp01.md")
- [AGENTREL06-BP02 Establish fallback mechanisms for legacy system degradation](agentrel06-bp02.md "agentrel06-bp02.md")
- [AGENTREL06-BP03 Regularly test degraded system performance](agentrel06-bp03.md "agentrel06-bp03.md")
- [AGENTREL06-BP04 Implement idempotent task execution patterns](agentrel06-bp04.md "agentrel06-bp04.md")
- [AGENTREL06-BP05 Implement dynamic capability toggling](agentrel06-bp05.md "agentrel06-bp05.md")
