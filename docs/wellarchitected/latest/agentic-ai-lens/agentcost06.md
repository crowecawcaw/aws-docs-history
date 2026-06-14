# Agent discovery and deployment cost optimization

Teams that optimize agent lifecycle infrastructure through
lightweight discovery, efficient versioning, and warm
initialization help keep operational overhead from growing faster
than the agent fleet itself. Agent infrastructure costs can
escalate through inefficient discovery mechanisms, version
proliferation, and cold start penalties.

| AGENTCOST06: How do you optimize agent discovery,<br>registry, and deployment costs? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

## Capability intent

- Agent discovery runs on consumption-based infrastructure, so
  registry costs track actual query and write activity rather
  than a fixed overhead for the fleet.
- Metadata caching serves most capability lookups without
  re-reading the registry, keeping read costs proportional to
  the rate of registry change rather than the rate of
  invocation.
- Agent versioning stores shared dependencies once and retires
  unused versions automatically, so storage costs stay
  contained as the agent fleet evolves.
- Deployments use weighted traffic routing on shared
  infrastructure, so blue/green and canary rollouts don't pay
  twice for parallel environments.
- Frequently invoked agents reuse warm sessions with cached
  initialization artifacts, and infrequent agents scale to
  zero to avoid idle capacity charges.
- Cold start rates, cache hit rates, and per-version storage
  are instrumented and reviewed, giving owners the signal to
  address cost drivers before they scale with the fleet.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent discovery and deployment cost optimization as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent discovery, versioning, and initialization are<br>handled one-time. Teams deploy heavyweight service mesh<br>or custom registries without evaluating<br>consumption-based alternatives. Container versions<br>accumulate in<br>[Amazon ECR](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md") without lifecycle policies, and cold starts<br>are absorbed on every invocation because session<br>lifetimes, caching, and session affinity are not<br>configured. Cost visibility is limited to account-level<br>billing, so expensive patterns grow silently as the<br>fleet expands.                                                                                                                                                                                                                                                                                                                                                                                       |
| 2     | Emerging  | Managed discovery such as<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") is adopted for<br>tool-based agent collaboration. Custom registries, where<br>needed, use consumption-based storage such as<br>[Amazon DynamoDB on-demand capacity](../../../amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.md#HowItWorks.OnDemand "../../../amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.md#HowItWorks.OnDemand"). Version retention<br>policies are defined but enforced manually. Warm session<br>patterns are applied to a small number of high-frequency<br>agents, and cold start rates are tracked for those<br>agents.                                                                                                                                                                                                                                                        |
| 3     | Defined   | Gateway or a consumption-based registry is the standard,<br>and metadata caching with configurable TTLs is used<br>across the fleet.<br>[Amazon ECR lifecycle policies](../../../AmazonECR/latest/userguide/LifecyclePolicies.md "../../../AmazonECR/latest/userguide/LifecyclePolicies.md") delete unused images<br>automatically, and container base layers are shared so<br>ECR deduplicates them across agent versions. Weighted<br>endpoint routing is used for blue/green and canary<br>deployments on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md"). Persistent filesystem<br>caching amortizes initialization across sessions, and<br>cold start and initialization costs are measured per<br>agent type through<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"). |
| 4     | Proactive | Discovery, versioning, and initialization cost metrics<br>are dashboarded in<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") and reviewed on a routine cadence.<br>Canary promotion is automated using<br>cost-per-task-completion alongside error rate and<br>latency, driven from<br>[AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") promotion logic. Session affinity routing<br>is implemented in the orchestration layer, and<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") is configured for lazy<br>loading so agents fetch only essential startup context.<br>Cost anomalies on discovery, deployment, or<br>initialization trigger alerts automatically.                                                                                                            |
| 5     | Optimized | Discovery, deployment, and initialization patterns are<br>continuously refined based on operational data. Agent<br>version vending is fully self-service with cost-aware<br>guardrails, and cold start rates sit below 10% across<br>the fleet. Retention, promotion, and warm pool policies<br>are self-healing and driven by observed usage. The<br>organization publishes reusable agent and container<br>patterns internally, and shares benchmarks on discovery,<br>versioning, and initialization cost efficiency across<br>teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Common issues to watch for

- Organizations deploy heavyweight service mesh infrastructure
  for simple capability lookups, paying fixed monthly costs
  for features the agent fleet doesn't use.
- Teams put the registry on the critical path for every
  invocation, repeatedly re-reading capability metadata
  instead of caching it, so read costs grow linearly with
  invocation volume.
- Agent version retention runs without lifecycle policies, so
  every configuration change accumulates images in the
  container registry and storage costs grow indefinitely.
- Blue/green and canary deployments run full parallel fleets
  instead of routing a small traffic percentage, doubling
  compute cost during every rollout.
- Frequently invoked agents pay cold start costs on every
  invocation because session lifetimes, persistent filesystem
  caching, and session affinity are not configured.
- Discovery, versioning, and initialization costs are not
  instrumented, so expensive patterns such as scan-heavy
  queries, unused versions, and repeated cold starts grow
  silently as the fleet expands.

###### Best practices

- [AGENTCOST06-BP01 Implement lightweight discovery and registry for cost-effective collaboration](agentcost06-bp01.md "agentcost06-bp01.md")
- [AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management](agentcost06-bp02.md "agentcost06-bp02.md")
- [AGENTCOST06-BP03 Design cost-efficient initialization through warm pools and caching](agentcost06-bp03.md "agentcost06-bp03.md")
