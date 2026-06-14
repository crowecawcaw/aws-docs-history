# AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling

Trust in a shared agent service is built through consistent,
predictable performance for every tenant, even during demand spikes.
In pooled multitenant deployments, effective isolation requires
throttling at multiple layers (API, inference, memory, and tools),
monitoring per-tenant resource consumption, and adaptive fairness
mechanisms that distribute shared resources equitably based on
current load.

**Desired outcome:**

- You have per-tenant throttling enforced at every shared resource
  layer.
- You have tenant resource consumption monitored in real time with
  alerts for tenants approaching their limits.
- You have graceful throttling that provides clear feedback to
  throttled tenants.
- You have performance isolation validated through regular load
  testing that simulates noisy neighbor scenarios.

**Common anti-patterns:**

- Applying throttling only at the API gateway layer without
  enforcing limits at downstream shared resources, letting tenants
  bypass API-level limits through long-running operations.
- Using static throttling limits that don't adapt to current
  system load, wasting available capacity during low-load periods
  or failing to protect isolation during high-load periods.
- Throttling all tenants equally regardless of their service tier,
  failing to honor premium SLAs.

**Benefits of establishing this best
practice:**

- Multi-layer throttling distributes shared resources fairly
  across tenants.
- Real-time per-tenant consumption metrics support proactive
  management.
- Per-tenant performance monitoring validates SLA compliance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Multi-layer throttling enforces tenant limits at every shared
resource. At the API layer,
[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") usage plans with per-tenant API keys enforce
request rate and burst limits. At the inference layer,
tenant-aware request queuing caps concurrent
[Amazon
Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") inference calls per tenant. At the memory and tool
layers, per-tenant rate limiting applies to shared endpoints. For
agents deployed on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md"), the runtime's session isolation
provides natural per-session resource boundaries.

Adaptive throttling adjusts limits based on current system load:
during low-load periods, tenants can burst above their baseline
limits to use available capacity, and during high-load periods,
strict limits protect isolation. Per-tenant
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") dashboards and metrics track request volume,
inference consumption, latency percentiles, throttle rates, and
error rates. Alarms fire when a tenant approaches their limits or
when per-tenant latency exceeds SLA thresholds. Regular noisy
neighbor testing, simulating high-load scenarios for individual
tenants, validates that other tenants' performance stays within
SLA bounds.

### Implementation steps

1. **Define per-tenant throttling limits
   for each resource layer:** Set per-tenant limits
   for API requests per second, concurrent inference calls,
   memory storage quota, and tool invocations per minute.
2. **Implement API Gateway usage plans
   with per-tenant API keys and rate/burst limits:**
   Use
   [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") usage plans with per-tenant API keys to
   enforce rate and burst limits at ingress.
3. **Deploy tenant-aware inference
   queuing with per-tenant concurrency limits:** Queue
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") inference calls per tenant so no single
   tenant can consume all inference capacity.
4. **Configure adaptive throttling that
   adjusts limits based on current system load:**
   Allow bursts during low-load periods and enforce strict
   limits during high-load periods to protect isolation.
5. **Create per-tenant CloudWatch
   dashboards and configure SLA-based alarms:**
   Publish per-tenant metrics in
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and alarm on consumption approaching
   limits or latency exceeding SLA thresholds.
6. **Establish regular noisy neighbor
   load testing to validate isolation effectiveness:**
   Schedule noisy neighbor load tests that simulate high-load
   scenarios for individual tenants and verify others stay
   within SLA.

## Resources

**Related best practices:**

- [AGENTPERF07-BP01 Design
  efficient multi-tenant agent deployment models](agentperf07-bp01.md "agentperf07-bp01.md")
- [AGENTPERF04-BP02
  Implement efficient protocol-based agent communications](agentperf04-bp02.md "agentperf04-bp02.md")
- [AGENTSUS01-BP04
  Scale cognitive processing pathways appropriately](agentsus01-bp04.md "agentsus01-bp04.md")

**Related documents:**

- [Building
  multi-tenant architectures for agentic AI on AWS](../../../prescriptive-guidance/latest/agentic-ai-multitenant/introduction.md "../../../prescriptive-guidance/latest/agentic-ai-multitenant/introduction.md")
- [Enforcing
  tenant isolation, Multi-tenant agentic AI](../../../prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.md "../../../prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.md")

**Related videos:**

- [Building
  multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8 "https://www.youtube.com/watch?v=uwXrtyXXuy8")

**Related services:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
