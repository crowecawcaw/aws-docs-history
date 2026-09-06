

# Multi-tenancy and resource optimization
<a name="agentperf07"></a>

 A well-designed multitenant agent service lets organizations serve many teams and customers from shared infrastructure while delivering consistent, predictable performance to each. Multitenant agent deployments must isolate one tenant's workload so it can't degrade the performance experienced by other tenants, and at the same time optimize overall resource utilization to control costs. This requires designing deployment models that provide appropriate isolation boundaries, implementing throttling and quota mechanisms that enforce fair resource allocation, and right-sizing serverless compute configurations for the bursty nature of agent workloads. 


|  AGENTPERF07: How do you manage multitenant performance isolation and optimize resource utilization?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-6"></a>
+  Tenant deployments are organized into tiers with explicit performance, isolation, and cost profiles, rather than a single shape applied uniformly to every tenant. 
+  Pooled tiers share managed infrastructure that provides session-level isolation, and premium or enterprise tiers add dedicated resources where stronger isolation is required. 
+  Throttling is enforced at every shared resource layer (API, inference, memory, tools), so tenants can't bypass edge limits through long-running downstream operations. 
+  Adaptive throttling lets tenants use slack capacity during low-load periods and snaps back to baseline during contention, while honoring tier priority. 
+  Tenant context propagates through the full stack, and per-tenant dashboards track latency, error rates, throttle state, and resource consumption against the tier's SLA. 
+  Isolation is validated through regular noisy-neighbor testing, so the deployment model's performance claims are measured rather than assumed. 

## Maturity levels
<a name="maturity-levels-6"></a>

 These levels summarize what each stage of maturity looks like for multi-tenancy and resource optimization as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Tenants are served from a single shared deployment with no isolation mechanisms or from duplicated siloed infrastructure with no tier policy. Throttling, if it exists, is at the API edge only and uses static limits. There is no per-tenant telemetry, so noisy-neighbor effects and SLA violations are discovered after customers report them. Tenant onboarding requires manual infrastructure provisioning for every new customer.  | 
|  2  |  Emerging  |  A small number of tiers (standard and premium, optionally enterprise) is documented with performance SLAs, isolation requirements, and pricing. The standard tier runs on pooled infrastructure such as [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with session-level isolation. [Amazon API Gateway usage plans](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) enforce per-tenant rate limits at the edge. Data is isolated per tier using [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) partition keys for pooled tiers.  | 
|  3  |  Defined  |  Throttling is enforced at every shared layer, not only at the edge. Tenant-aware queuing limits per-tenant concurrency on [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) invocations, and memory and tool layers enforce their own per-tenant limits. Premium tenants use dedicated resources such as [Amazon Bedrock provisioned throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html). Tenant context propagates through the runtime, memory, and tool layers. Per-tenant dashboards in [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) track consumption and SLA compliance.  | 
|  4  |  Proactive  |  Adaptive throttling loosens limits during low-load periods and tightens during contention, honoring tier priority so premium tenants retain capacity. Onboarding for standard-tier tenants is configuration-driven through [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) or [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates rather than a bespoke infrastructure build. Alarms fire on per-tenant limit proximity and SLA violations, and noisy-neighbor testing runs on a regular cadence to validate isolation claims against real load.  | 
|  5  |  Optimized  |  Tier definitions, throttling policies, and deployment models are continuously refined against operational data. Onboarding is fully self-service for standard and premium tiers with guardrails that help prevent tier-inappropriate configurations. Cost and performance per tenant are reported to tenant-facing dashboards, and isolation effectiveness is validated through automated chaos and noisy-neighbor scenarios. The organization publishes reusable multitenant reference patterns internally and contributes benchmarks across teams.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-6"></a>
+  Teams deploy fully isolated infrastructure for every tenant regardless of need, wasting capacity on tenants whose requirements would be met by pooled resources. 
+  Teams use a single pooled deployment without per-layer isolation, letting high-volume tenants consume disproportionate capacity and degrade performance for everyone else. 
+  Throttling is enforced only at the API edge, so tenants bypass edge limits through long-running inference, memory, or tool operations that saturate downstream shared resources. 
+  Throttling uses static limits that neither use available slack during low-load periods nor protect isolation during high-load periods, and premium tenants are throttled identically to standard tenants. 
+  Tenant onboarding requires infrastructure provisioning on every new customer, so onboarding time and operational overhead grow linearly with tenant count. 
+  Isolation is assumed rather than tested, so subtle changes (a new tool, a heavier prompt, a shift in traffic mix) erode the isolation boundary silently and surface only during a real incident. 

**Topics**
+ [Capability intent](#capability-intent-6)
+ [Maturity levels](#maturity-levels-6)
+ [Common issues to watch for](#common-issues-to-watch-for-6)
+ [AGENTPERF07-BP01 Design efficient multitenant agent deployment models](agentperf07-bp01.md)
+ [AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling](agentperf07-bp02.md)