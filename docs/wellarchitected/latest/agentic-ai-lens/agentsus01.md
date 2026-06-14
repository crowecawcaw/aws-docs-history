# Resource reusability

Organizations that invest in reusable agent infrastructure
accelerate every subsequent project while reducing cumulative
resource consumption. As agents are used more, the opportunity to
optimize, share, and recycle agent resources increases. Shared
resources pose a less significant burden on the overall
architecture, creating a more sustainable workflow.

| AGENTSUS01: How do you build sustainable and repeatable<br>frameworks for managing compute, memory, and other<br>shareable agent resources? |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                             |

## Capability intent

- Each agent encapsulates a single, well-defined capability
  with explicit resource boundaries, and those boundaries
  cascade through delegation to child agents so no subtree
  consumes resources without a defined cap.
- Recurring workflow patterns (retrieval, validation,
  transformation, and decision-making) exist as parameterized,
  discoverable components that teams compose rather than
  rebuild for every new use case.
- Common infrastructure such as connection pools, caches,
  authentication, and foundation model access is consolidated
  into shared services, so capacity grows with aggregate
  demand rather than with the number of agent instances.
- Cognitive pathways are right-sized to task complexity, with
  model selection, retrieval depth, and memory scope each
  matched to actual needs rather than defaulting to the
  largest or broadest option.
- Long-running and frontier workloads run against explicit
  specifications covering success criteria, resource budgets,
  and termination conditions, with checkpoints that make
  compute investment reviewable against business value.

## Maturity levels

These levels summarize what each stage of maturity looks like
for resource reusability as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents are provisioned for worst-case scenarios without<br>explicit resource contracts, and delegated child agents<br>inherit no constraints. Workflows are rebuilt from<br>scratch per use case, with no shared pattern library or<br>inventory of reusable components. Every agent<br>establishes its own connections to external services,<br>duplicating infrastructure across instances. Foundation<br>model calls default to the largest available model, and<br>long-running agents run without specifications or<br>checkpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2     | Emerging  | Teams have started to decompose workflows into<br>specialized agents with basic timeout and memory limits<br>configured per agent. Some recurring workflow patterns<br>have been extracted into templates, though discovery is<br>informal. A handful of shared services (usually a<br>central cache or a common authentication path) are in<br>production.<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") is enabled for<br>most production agents, and manual reviews of resource<br>consumption occur on a regular cadence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3     | Defined   | Specialized agents are the default pattern, deployed on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md") with explicit resource<br>boundaries, and reusable workflow patterns are published<br>through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") as discoverable MCP<br>tools. Shared caches such as<br>[Amazon ElastiCache](../../../AmazonElastiCache/latest/UserGuide/BestPractices.md "../../../AmazonElastiCache/latest/UserGuide/BestPractices.md") are standard, and authentication runs<br>through<br>[Amazon<br>Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md"). Tiered model routing<br>and scoped retrieval against<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") are in place for most<br>workflows, and long-running agents run with documented<br>specifications. |
| 4     | Proactive | Resource budgets are enforced at the orchestration layer<br>through<br>[AWS Step Functions](../../../step-functions/latest/dg/concepts-nested-workflows.md "../../../step-functions/latest/dg/concepts-nested-workflows.md") and AgentCore Policies rather than<br>relying on agent self-restraint. Pattern libraries are<br>maintained, governed, and instrumented so a single<br>optimization propagates to every consuming workflow.<br>[Amazon<br>Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") distributes model<br>traffic, and<br>[Amazon<br>Bedrock Data Automation](../../../bedrock/latest/userguide/bda.md "../../../bedrock/latest/userguide/bda.md") handles document<br>extraction in place of large vision models. Frontier<br>agents run with cascading budgets, checkpoint-based<br>evaluation, and state persistence through<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md").                                                                                     |
| 5     | Optimized | Resource boundaries, routing thresholds, retention<br>policies, and specification templates are continuously<br>recalibrated from<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") data rather than<br>through manual review cycles. Shared services and<br>pattern libraries are the default composition point for<br>new workflows, and new development that doesn't reuse<br>existing components is the exception. Resource<br>utilization efficiency (successful completions per unit<br>of compute) is a first-class metric alongside cost and<br>latency, and the organization contributes reusable<br>patterns and sustainability measurements back to its<br>communities of practice.                                                                                                                                                                                                                                                                                                                                                                                |

## Common issues to watch for

- Teams provision agents for worst-case scenarios and let
  parent agents delegate work to child agents without
  cascading resource budgets, so runaway consumption in one
  subtree is discovered only after the monthly bill.
- Recurring workflow logic is rebuilt for each new use case,
  accumulating duplicated code and testing debt while missing
  the renewable-architecture benefit of optimizing a shared
  pattern once and propagating the improvement everywhere.
- Each agent establishes its own connections, caches, and
  authentication flows rather than consuming shared services,
  so infrastructure costs scale linearly with agent count
  instead of with aggregate demand.
- Every request is routed to the largest foundation model,
  retrieval is unbounded against knowledge bases, and memory
  grows without pruning, so cognitive overhead is
  disproportionate to the value delivered by each interaction.
- Long-running and frontier agents run without specifications,
  resource budgets, or checkpoints, so they explore tangential
  paths and consume extended compute without an accountability
  mechanism that ties outcomes to business value.

###### Best practices

- [AGENTSUS01-BP01 Design specialized agents with explicit resource boundaries](agentsus01-bp01.md "agentsus01-bp01.md")
- [AGENTSUS01-BP02 Implement reusable workflow patterns](agentsus01-bp02.md "agentsus01-bp02.md")
- [AGENTSUS01-BP03 Optimize resource utilization through shared services](agentsus01-bp03.md "agentsus01-bp03.md")
- [AGENTSUS01-BP04 Scale cognitive processing pathways appropriately](agentsus01-bp04.md "agentsus01-bp04.md")
- [AGENTSUS01-BP05 Adopt specification-driven tasks for frontier agents and long-running workflows](agentsus01-bp05.md "agentsus01-bp05.md")
