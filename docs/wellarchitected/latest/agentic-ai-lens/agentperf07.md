# Multi-tenancy and resource optimization

A well-designed multitenant agent service lets organizations serve
many teams and customers from shared infrastructure while
delivering consistent, predictable performance to each.
Multitenant agent deployments must isolate one tenant's workload
so it can't degrade the performance experienced by other tenants,
and at the same time optimize overall resource utilization to
control costs. This requires designing deployment models that
provide appropriate isolation boundaries, implementing throttling
and quota mechanisms that enforce fair resource allocation, and
right-sizing serverless compute configurations for the bursty
nature of agent workloads.

| AGENTPERF07: How do you manage multitenant performance<br>isolation and optimize resource utilization? |
| ------------------------------------------------------------------------------------------------------ |
|                                                                                                        |

## Capability intent

- Tenant deployments are organized into tiers with explicit
  performance, isolation, and cost profiles, rather than a
  single shape applied uniformly to every tenant.
- Pooled tiers share managed infrastructure that provides
  session-level isolation, and premium or enterprise tiers add
  dedicated resources where stronger isolation is required.
- Throttling is enforced at every shared resource layer (API,
  inference, memory, tools), so tenants can't bypass edge
  limits through long-running downstream operations.
- Adaptive throttling lets tenants use slack capacity during
  low-load periods and snaps back to baseline during
  contention, while honoring tier priority.
- Tenant context propagates through the full stack, and
  per-tenant dashboards track latency, error rates, throttle
  state, and resource consumption against the tier's SLA.
- Isolation is validated through regular noisy-neighbor
  testing, so the deployment model's performance claims are
  measured rather than assumed.

## Maturity levels

These levels summarize what each stage of maturity looks like
for multi-tenancy and resource optimization as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Initial   | Tenants are served from a single shared deployment with<br>no isolation mechanisms or from duplicated siloed<br>infrastructure with no tier policy. Throttling, if it<br>exists, is at the API edge only and uses static limits.<br>There is no per-tenant telemetry, so noisy-neighbor<br>effects and SLA violations are discovered after<br>customers report them. Tenant onboarding requires manual<br>infrastructure provisioning for every new customer.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2     | Emerging  | A small number of tiers (standard and premium,<br>optionally enterprise) is documented with performance<br>SLAs, isolation requirements, and pricing. The standard<br>tier runs on pooled infrastructure such as<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") with session-level<br>isolation.<br>[Amazon API Gateway usage plans](../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md "../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md") enforce per-tenant rate<br>limits at the edge. Data is isolated per tier using<br>[Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") partition keys for pooled tiers. |
| 3     | Defined   | Throttling is enforced at every shared layer, not only<br>at the edge. Tenant-aware queuing limits per-tenant<br>concurrency on<br>[Amazon<br>Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") invocations, and memory and tool layers<br>enforce their own per-tenant limits. Premium tenants use<br>dedicated resources such as<br>[Amazon<br>Bedrock provisioned throughput](../../../bedrock/latest/userguide/prov-throughput.md "../../../bedrock/latest/userguide/prov-throughput.md"). Tenant context<br>propagates through the runtime, memory, and tool layers.<br>Per-tenant dashboards in<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") track consumption and SLA compliance.                        |
| 4     | Proactive | Adaptive throttling loosens limits during low-load<br>periods and tightens during contention, honoring tier<br>priority so premium tenants retain capacity. Onboarding<br>for standard-tier tenants is configuration-driven<br>through<br>[AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") or<br>[AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") templates rather than a bespoke<br>infrastructure build. Alarms fire on per-tenant limit<br>proximity and SLA violations, and noisy-neighbor testing<br>runs on a regular cadence to validate isolation claims<br>against real load.                                                                                                                                                                                              |
| 5     | Optimized | Tier definitions, throttling policies, and deployment<br>models are continuously refined against operational<br>data. Onboarding is fully self-service for standard and<br>premium tiers with guardrails that help prevent<br>tier-inappropriate configurations. Cost and performance<br>per tenant are reported to tenant-facing dashboards, and<br>isolation effectiveness is validated through automated<br>chaos and noisy-neighbor scenarios. The organization<br>publishes reusable multitenant reference patterns<br>internally and contributes benchmarks across teams.                                                                                                                                                                                                                                                                                                                  |

## Common issues to watch for

- Teams deploy fully isolated infrastructure for every tenant
  regardless of need, wasting capacity on tenants whose
  requirements would be met by pooled resources.
- Teams use a single pooled deployment without per-layer
  isolation, letting high-volume tenants consume
  disproportionate capacity and degrade performance for
  everyone else.
- Throttling is enforced only at the API edge, so tenants
  bypass edge limits through long-running inference, memory,
  or tool operations that saturate downstream shared
  resources.
- Throttling uses static limits that neither use available
  slack during low-load periods nor protect isolation during
  high-load periods, and premium tenants are throttled
  identically to standard tenants.
- Tenant onboarding requires infrastructure provisioning on
  every new customer, so onboarding time and operational
  overhead grow linearly with tenant count.
- Isolation is assumed rather than tested, so subtle changes
  (a new tool, a heavier prompt, a shift in traffic mix) erode
  the isolation boundary silently and surface only during a
  real incident.

###### Best practices

- [AGENTPERF07-BP01 Design efficient multitenant agent deployment models](agentperf07-bp01.md "agentperf07-bp01.md")
- [AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling](agentperf07-bp02.md "agentperf07-bp02.md")
