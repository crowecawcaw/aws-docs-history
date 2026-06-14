# Resource right-sizing

Agents that right-size their dependencies (memory, caching,
compute, and networking) deliver automation value without placing
unsustainable load on the systems they depend on. Increased agent
traffic increases the load on these dependencies. Sustainable
frameworks help dependent systems scale proportionally to the
benefit achieved through agentic automation.

| AGENTSUS02: How do I establish sustainable frameworks for<br>agent dependencies? |
| -------------------------------------------------------------------------------- |
|                                                                                  |

## Capability intent

- Memory and context infrastructure scales with actual
  contextual needs rather than worst-case estimates, with
  tiered storage and shared persistent context separating hot
  and cold access paths.
- Caching is applied at every integration point, and shared
  caches amortize work across the agent fleet rather than
  being rediscovered by each agent in isolation.
- Compute, networking, and storage scale dynamically with
  bursty agent workloads, contracting during quiet periods and
  expanding during peaks without manual intervention.
- Regional and connectivity choices are deliberate, so traffic
  stays close to the services agents depend on and private
  paths are used where security or latency justifies them.
- Environmental impact is measured alongside operational
  metrics, and deferrable workloads are scheduled and placed
  with carbon-awareness to reduce footprint without affecting
  user-facing performance.

## Maturity levels

These levels summarize what each stage of maturity looks like
for resource right-sizing as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent memory, caching, and infrastructure run without<br>deliberate right-sizing. Memory grows unboundedly,<br>caches are isolated to each agent if they exist at all,<br>and compute is statically provisioned for peak demand.<br>Environmental impact isn't measured, and Region<br>placement is treated as an afterthought.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2     | Emerging  | Teams have adopted<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") with basic retention<br>policies and have enabled<br>[Amazon<br>Bedrock prompt caching](../../../bedrock/latest/userguide/prompt-caching.md "../../../bedrock/latest/userguide/prompt-caching.md") for stable system prompts.<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") is used for some<br>agents, and<br>[AWS Sustainability](../../../sustainability/latest/userguide/what-is-sustainability.md "../../../sustainability/latest/userguide/what-is-sustainability.md") has been turned on for reporting<br>but has not informed design decisions.                                                                                                                                                                             |
| 3     | Defined   | Tiered memory with shared persistent context through<br>[AgentCore<br>Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") namespaces is the default for multi-agent<br>systems. Shared caches exposed through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") amortize work across<br>the fleet. Token caching in<br>[Amazon<br>Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md") reduces repeated<br>credential validation.<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") tracks memory<br>access patterns, cache hit rates, and efficiency<br>metrics, and a 30-day environmental baseline has been<br>established. |
| 4     | Proactive | Infrastructure scaling, Regional placement, and private<br>connectivity through<br>[VPC<br>interface endpoints](../../../bedrock-agentcore/latest/devguide/vpc-interface-endpoints.md "../../../bedrock-agentcore/latest/devguide/vpc-interface-endpoints.md") are driven by observed<br>patterns. Context compression, semantic retrieval<br>through<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md"), and streaming responses<br>are standard. Deferrable workloads run off-peak, and<br>[Amazon<br>Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") routes batch<br>workloads to Regions with favorable energy profiles<br>where latency allows. Sustainability dashboards<br>combining operational and carbon metrics are reviewed on<br>a regular cadence.                                            |
| 5     | Optimized | Memory tiers, cache policies, and infrastructure<br>provisioning are continuously recalibrated from<br>telemetry rather than through periodic review.<br>Environmental footprint is a first-class design input<br>for every new agent workload, and efficiency<br>improvements compound week over week as coverage<br>expands. The organization contributes reasoning-cost and<br>sustainability patterns back to its communities of<br>practice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Common issues to watch for

- Teams build flat memory architectures without tiered
  storage, so frequently accessed context competes with
  archival data for the same tier and retrieval costs grow
  with every new session.
- Organizations treat each agent instance as an isolated
  system with its own cache, missing the fleet-wide
  amortization that turns one cache hit into savings for every
  agent that asks the same question.
- Infrastructure stays statically provisioned for worst-case
  demand, so utilization sits low during normal operations and
  dynamic contraction never happens.
- Regional placement ignores where the frequently accessed
  services live, so agent traffic crosses Regions
  unnecessarily and adds both latency and data transfer to
  every invocation.
- Sustainability claims are made without baselines or trend
  tracking, so optimization work can't be validated and
  deferrable workloads still run during peak hours alongside
  user-facing traffic.

###### Best practices

- [AGENTSUS02-BP01 Optimize context management and memory utilization](agentsus02-bp01.md "agentsus02-bp01.md")
- [AGENTSUS02-BP02 Establish efficient agent caching strategies](agentsus02-bp02.md "agentsus02-bp02.md")
- [AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies](agentsus02-bp03.md "agentsus02-bp03.md")
- [AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads](agentsus02-bp04.md "agentsus02-bp04.md")
