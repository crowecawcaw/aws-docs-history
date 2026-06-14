# Strategic performance planning and measurement

Agentic AI systems introduce novel performance dimensions beyond
traditional infrastructure metrics, including reasoning latency,
token throughput, tool invocation efficiency, time-to-first-token,
and overall task completion time. Strategic performance planning
requires defining measurable success criteria with per-phase
latency budgets, implementing thorough telemetry across the
reasoning pipeline, systematically profiling overall latency to
identify bottlenecks, and establishing performance testing
practices that validate agent responsiveness under load. Without
deliberate performance planning, organizations risk deploying
agents that appear functional but fail to meet latency,
throughput, or quality expectations at scale.

For agent maturity models and lifecycle governance, see
[AGENTOPS03-BP01](agentops03-bp01.md "agentops03-bp01.md").
For business metrics feedback loops, see
[AGENTOPS02-BP04](agentops02-bp04.md "agentops02-bp04.md").
For agent evaluation frameworks, see
[AGENTOPS06-BP02](agentops06-bp02.md "agentops06-bp02.md").

| AGENTPERF01: How do you plan strategically for agent<br>performance and establish measurement practices? |
| -------------------------------------------------------------------------------------------------------- |
|                                                                                                          |

## Capability intent

- Performance success criteria are defined as measurable
  service level objectives per agent workload, covering
  latency (including time-to-first-token and end-to-end
  completion), throughput, quality, and efficiency dimensions
  that agent-specific reasoning, tool use, and multi-agent
  coordination introduce.
- End-to-end latency budgets are decomposed into per-phase
  allocations across context retrieval, inference, tool
  invocation, and inter-agent coordination, so that drift is
  attributable to the phase causing it rather than diagnosed
  during an incident.
- Distributed telemetry captures every agent execution as a
  session, trace, and span hierarchy aligned with
  OpenTelemetry generative AI semantic conventions, so
  reasoning-pipeline operations are individually observable
  and correlatable.
- Production traffic is profiled on a defined cadence to
  decompose end-to-end latency into per-phase contributions,
  with optimization effort ranked by contribution multiplied
  by addressable variance rather than by contribution alone.
- Success criteria, telemetry, and phase-level alerts feed
  CI/CD quality gates and regression alarms, so performance
  posture stays aligned with production behavior as prompts,
  tools, and models drift.

## Maturity levels

These levels summarize what each stage of maturity looks like
for strategic performance planning and measurement as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Performance targets are aspirational rather than<br>measurable, with no per-workload KPIs and only<br>infrastructure metrics in place. Telemetry is limited to<br>runtime logs and<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") duration metrics, and end-to-end<br>latency is the only signal monitored. Performance<br>regressions are discovered through user reports rather<br>than observability, and criteria are revisited only<br>after incidents.                                                                                                                                                                                                                                          |
| 2     | Emerging  | Latency and throughput targets are documented for<br>flagship workloads, and basic traces flow through<br>[AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") or CloudWatch. Agent-specific metrics (task<br>completion, tokens per task) are emitted but are not<br>currently tied to alerts or SLOs. Per-phase<br>decomposition is one-time rather than encoded in<br>criteria, and profiling happens reactively after the<br>first incident.                                                                                                                                                                                                                                                                                                                   |
| 3     | Defined   | Every production workload has structured service level<br>objectives with service level indicators, thresholds,<br>attainment goals, and intervals managed through<br>[Amazon CloudWatch Application Signals](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.md").<br>OpenTelemetry-compatible telemetry through the<br>[AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction "https://aws-otel.github.io/docs/introduction") populates the CloudWatch<br>generative AI observability surface, and per-phase<br>latency budgets are allocated from the end-to-end<br>target. Profiling runs against production traffic and<br>per-phase percentile metrics are published. |
| 4     | Proactive | Phase-level<br>[CloudWatch<br>anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") and burn-rate alarms fire on<br>drift before end-to-end SLOs are exceeded, with<br>composite alarms correlating signals to reduce noise.<br>SLOs are gated in CI/CD through automated load and<br>evaluation tests, and<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") validates quality<br>as part of the pipeline. Per-phase profiles are<br>refreshed on a defined cadence and optimization targets<br>are ranked by contribution and addressable variance.                  |
| 5     | Optimized | Success criteria, per-phase budgets, and thresholds are<br>recalibrated continuously from production telemetry<br>rather than through manual review cycles.<br>Evaluation-set-driven quality gates and cost-per-task<br>ceilings travel with every release, and profiling feeds<br>the architecture roadmap. The organization contributes<br>performance measurement patterns and reasoning-cost<br>profiles back to its communities of practice and tunes<br>targets from data rather than launch-time assumption.                                                                                                                                                                                                                                                                                              |

## Common issues to watch for

- Teams define success criteria in infrastructure terms and
  miss agent-specific dimensions such as reasoning latency,
  token efficiency, tool accuracy, and time-to-first-token, so
  the criteria can't detect the regressions that actually
  affect users.
- Single latency targets are applied across streaming and
  non-streaming agents, or across interactive and batch
  workloads, which either over-provisions some agents or sets
  unachievable goals for others.
- Telemetry is added after launch and leaves gaps in trace
  continuity across agent boundaries, tool invocations, and
  asynchronous operations, which makes performance
  investigations collapse into guesswork.
- End-to-end latency is measured without per-phase
  decomposition, so optimization effort lands on phases that
  contribute little to the tail rather than on the phase that
  actually bounds user-visible performance.
- Success criteria, telemetry, and profiling are treated as
  launch-time artifacts rather than as artifacts revisited on
  a cadence, which lets agent drift erode KPIs silently until
  users notice.

###### Best practices

- [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.md "agentperf01-bp01.md")
- [AGENTPERF01-BP02 Implement comprehensive performance telemetry](agentperf01-bp02.md "agentperf01-bp02.md")
- [AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets](agentperf01-bp03.md "agentperf01-bp03.md")
