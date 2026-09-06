

# Resource right-sizing
<a name="agentsus02"></a>

 Agents that right-size their dependencies (memory, caching, compute, and networking) deliver automation value without placing unsustainable load on the systems they depend on. Increased agent traffic increases the load on these dependencies. Sustainable frameworks help dependent systems scale proportionally to the benefit achieved through agentic automation. 


|  AGENTSUS02: How do I establish sustainable frameworks for agent dependencies?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-1"></a>
+  Memory and context infrastructure scales with actual contextual needs rather than worst-case estimates, with tiered storage and shared persistent context separating hot and cold access paths. 
+  Caching is applied at every integration point, and shared caches amortize work across the agent fleet rather than being rediscovered by each agent in isolation. 
+  Compute, networking, and storage scale dynamically with bursty agent workloads, contracting during quiet periods and expanding during peaks without manual intervention. 
+  Regional and connectivity choices are deliberate, so traffic stays close to the services agents depend on and private paths are used where security or latency justifies them. 
+  Environmental impact is measured alongside operational metrics, and deferrable workloads are scheduled and placed with carbon-awareness to reduce footprint without affecting user-facing performance. 

## Maturity levels
<a name="maturity-levels-1"></a>

 These levels summarize what each stage of maturity looks like for resource right-sizing as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agent memory, caching, and infrastructure run without deliberate right-sizing. Memory grows unboundedly, caches are isolated to each agent if they exist at all, and compute is statically provisioned for peak demand. Environmental impact isn't measured, and Region placement is treated as an afterthought.  | 
|  2  |  Emerging  |  Teams have adopted [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) with basic retention policies and have enabled [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for stable system prompts. [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) is used for some agents, and [AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) has been turned on for reporting but has not informed design decisions.  | 
|  3  |  Defined  |  Tiered memory with shared persistent context through [AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) namespaces is the default for multi-agent systems. Shared caches exposed through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) amortize work across the fleet. Token caching in [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) reduces repeated credential validation. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks memory access patterns, cache hit rates, and efficiency metrics, and a 30-day environmental baseline has been established.  | 
|  4  |  Proactive  |  Infrastructure scaling, Regional placement, and private connectivity through [VPC interface endpoints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) are driven by observed patterns. Context compression, semantic retrieval through [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), and streaming responses are standard. Deferrable workloads run off-peak, and [Amazon Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) routes batch workloads to Regions with favorable energy profiles where latency allows. Sustainability dashboards combining operational and carbon metrics are reviewed on a regular cadence.  | 
|  5  |  Optimized  |  Memory tiers, cache policies, and infrastructure provisioning are continuously recalibrated from telemetry rather than through periodic review. Environmental footprint is a first-class design input for every new agent workload, and efficiency improvements compound week over week as coverage expands. The organization contributes reasoning-cost and sustainability patterns back to its communities of practice.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Teams build flat memory architectures without tiered storage, so frequently accessed context competes with archival data for the same tier and retrieval costs grow with every new session. 
+  Organizations treat each agent instance as an isolated system with its own cache, missing the fleet-wide amortization that turns one cache hit into savings for every agent that asks the same question. 
+  Infrastructure stays statically provisioned for worst-case demand, so utilization sits low during normal operations and dynamic contraction never happens. 
+  Regional placement ignores where the frequently accessed services live, so agent traffic crosses Regions unnecessarily and adds both latency and data transfer to every invocation. 
+  Sustainability claims are made without baselines or trend tracking, so optimization work can't be validated and deferrable workloads still run during peak hours alongside user-facing traffic. 

**Topics**
+ [Capability intent](#capability-intent-1)
+ [Maturity levels](#maturity-levels-1)
+ [Common issues to watch for](#common-issues-to-watch-for-1)
+ [AGENTSUS02-BP01 Optimize context management and memory utilization](agentsus02-bp01.md)
+ [AGENTSUS02-BP02 Establish efficient agent caching strategies](agentsus02-bp02.md)
+ [AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies](agentsus02-bp03.md)
+ [AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads](agentsus02-bp04.md)