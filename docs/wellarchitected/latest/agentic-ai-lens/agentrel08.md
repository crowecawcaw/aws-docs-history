# Graceful degradation and configuration management

Agents that detect degradation accurately through thorough
telemetry and maintain consistent configuration across all
instances make informed decisions about when to activate graceful
degradation. Consistent configuration management helps agents have
reliable, up-to-date information about capabilities and
limitations across the agent environment.

| AGENTREL08: How do agents determine when and where<br>graceful degradation is appropriate? |
| ------------------------------------------------------------------------------------------ |
|                                                                                            |

## Capability intent

- Agent configuration lives in a central, versioned,
  schema-validated source, so every instance runs the same
  current settings and drift is detected automatically.
- Configuration changes roll out gradually with automatic
  rollback, and sensitive values are held in encrypted
  parameter storage with fine-grained access control.
- Stage-level telemetry covers every phase of agent processing
  (context retrieval, inference, tool execution, response
  generation), so degradation decisions are informed rather
  than reactive.
- Anomaly detection and composite alarms combine signals
  across stages into a single useful health state, triggering
  graceful degradation automatically.
- Resource isolation separates high-priority user-facing
  agents from background workloads, and contention is detected
  through composite scores before it causes failures.
- Memory utilization is tracked per tier (in-context,
  short-term session, long-term persistent) with automated
  responses for summarization, pruning, and consolidation
  before exhaustion produces silent failures.

## Maturity levels

These levels summarize what each stage of maturity looks like
for graceful degradation and configuration management as a
whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Configuration is hardcoded in agent code, so every<br>parameter change requires a redeployment. Telemetry<br>exists only at the request boundary, which hides<br>stage-level degradation. Agents share a single resource<br>pool, so any workload spike degrades every tenant.<br>Memory utilization is monitored only at the<br>infrastructure level, and in-context exhaustion produces<br>silent failures. Graceful degradation is activated<br>manually, if at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2     | Emerging  | Configuration is centralized but managed manually, with<br>one-time versioning and limited schema validation. Basic<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") metrics capture inference latency and<br>error rate, but stage-level telemetry is partial.<br>Resource isolation is informal, with heavy workloads<br>sometimes placed on separate infrastructure. Memory<br>growth is tracked for a few known-leaky components, and<br>degradation responses are scripted but triggered by<br>operators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3     | Defined   | Runtime configuration is managed through a central<br>service such as<br>[AWS AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md") with JSON Schema validation and gradual<br>rollout, and secrets live in<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") or<br>[Parameter<br>Store SecureString parameters](../../../systems-manager/latest/userguide/parameter-store-about.md "../../../systems-manager/latest/userguide/parameter-store-about.md").<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") captures<br>stage-level telemetry, and<br>[Amazon<br>Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md") records per-call<br>token counts and latency. Priority tiers have separate<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") instances, and memory<br>utilization is tracked per tier with alarms at 80%<br>context-window utilization.                               |
| 4     | Proactive | [CloudWatch<br>anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") establishes baselines<br>automatically, and<br>[CloudWatch<br>composite alarms](../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm_How_To.md "../../../AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm_How_To.md") combine multi-stage signals into<br>automated graceful degradation. Resource contention is<br>detected through composite scores that combine<br>concurrency, token consumption, and queue depths, and<br>mitigation is automated through<br>[Amazon<br>Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md").<br>[Amazon<br>Bedrock Provisioned Throughput](../../../bedrock/latest/userguide/prov-throughput.md "../../../bedrock/latest/userguide/prov-throughput.md") gives<br>latency-sensitive agents dedicated capacity. Memory<br>growth is analyzed through<br>[CloudWatch<br>Metric Math](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md"), and summarization, pruning, and<br>consolidation responses are automated. Drift monitoring<br>alerts on configuration fleets running mixed versions. |
| 5     | Optimized | Degradation policies and configuration patterns are<br>continuously refined based on operational data.<br>Composite health scores, anomaly thresholds, and<br>automated mitigation rules are tuned from observed<br>outcomes rather than intuition. Memory management<br>responses are self-healing across all tiers, and<br>resource allocation adjusts dynamically based on<br>priority and observed demand. The organization publishes<br>reusable telemetry and configuration patterns internally<br>and shares benchmarks on graceful degradation<br>effectiveness across teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Common issues to watch for

- Configuration is hardcoded or partially centralized, so
  parameter changes require redeployment and configuration
  drift between instances is detected only through downstream
  failures.
- Configuration changes are applied without validation or
  staged rollout, which lets misconfigured values reach
  production and degrade agent behavior instantly.
- Telemetry is captured only at the request boundary, so a
  rise in overall latency or error rate provides no signal
  about which processing stage is responsible.
- All agents share a single resource pool and upstream quota,
  so a high-volume background agent degrades the latency of
  user-facing agents and throttling cascades across workloads.
- Memory monitoring stops at infrastructure metrics, so
  in-context exhaustion and gradual memory leaks produce
  silent output degradation with no leading indicator.
- Static alarm thresholds either fire too often during routine
  traffic shifts or miss gradual degradation, so graceful
  degradation activates reactively rather than proactively.

###### Best practices

- [AGENTREL08-BP01 Establish consistent configuration management practices](agentrel08-bp01.md "agentrel08-bp01.md")
- [AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing](agentrel08-bp02.md "agentrel08-bp02.md")
- [AGENTREL08-BP03 Architect agent systems with resource isolation and contention mitigation](agentrel08-bp03.md "agentrel08-bp03.md")
- [AGENTREL08-BP04 Track agent memory utilization metrics](agentrel08-bp04.md "agentrel08-bp04.md")
