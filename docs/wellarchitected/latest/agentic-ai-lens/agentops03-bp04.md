

# AGENTOPS03-BP04 Implement organizational agent portfolio management and governance at scale
<a name="agentops03-bp04"></a>

 A handful of agents built by one team is a project. Dozens of agents built by multiple teams is a portfolio, and portfolios need different operational mechanisms. Without cross-organizational visibility, teams build redundant agents, break each other's integrations, and lose track of which agents still earn their keep. 

 **Desired outcome:** 
+  A centralized catalog gives the organization a current view of every agent, owner, capabilities, dependencies, lifecycle state, cost profile, and business value. 
+  Teams discover existing agents before building new ones, so effort goes to capability gaps rather than duplicates. 
+  Cross-team dependencies are tracked and managed through coordinated deprecation processes. 
+  Quarterly portfolio reviews reveal underutilized agents for consolidation or retirement, keeping the portfolio aligned with business priorities. 

 **Common anti-patterns:** 
+  Allowing teams to build agents independently without checking for existing capabilities, creating redundant agents that duplicate development cost, infrastructure cost, and operational burden. 
+  Maintaining agent registries only within individual teams, so no one has the cross-organizational view needed to identify redundancy or assess overall system health. 
+  Deprecating or modifying agents without notifying dependent teams, causing cascading failures when orchestrators or delegating agents invoke agents that have changed. 
+  Treating agent creation as a no-justification-required activity, so the portfolio grows faster than the organization's ability to operate, monitor, and maintain it. 
+  Failing to measure business value relative to operational cost, reducing the risk of data-driven decisions about which agents warrant continued investment. 

 **Benefits of establishing this best practice:** 
+  Portfolio governance scales operational practices from individual agents to enterprise environments, so governance overhead grows sub-linearly with agent count. 
+  A centralized catalog with ownership, dependency tracking, and lifecycle state provides the auditable record needed for compliance and organizational accountability. 
+  Capability search before build reduces redundant development, freeing engineering effort for capability gaps. 
+  Quarterly reviews help prevent sprawl by revealing candidates for consolidation and retirement before the portfolio becomes unmanageable. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Portfolio governance extends the team-level registry into an organizational catalog that spans team boundaries (for more detail, see [AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance](agentops03-bp01.html)). The fields added at this layer are the ones that support cross-team decisions: 
+  Owning team 
+  Business domain 
+  Upstream dependencies (agents or systems that invoke this agent) 
+  Downstream dependencies (agents, tools, or services this agent invokes) 
+  Cost-per-month (derived from CloudWatch and Cost Explorer) 
+  Business value indicators (task completion volume, business outcome metrics). 

 [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the centralized catalog with built-in approval workflows, flexible metadata, and hybrid search (semantic and keyword) so cross-organizational queries run efficiently. Enrich registry records with dependency metadata, cost attribution, and business value indicators so the catalog supports portfolio-level decisions beyond simple discovery. 

 The pre-creation review gate helps prevent duplicate builds. Teams searching for specific agents by purpose will not find one through keyword matching against agent names. [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides built-in hybrid search that combines semantic understanding with keyword matching, so natural-language capability queries reveal existing agents with overlapping capabilities. When overlap exists, the requesting team documents why the existing agent is insufficient before proceeding. 

 This applies to code-based agents (Strands Agents, LangGraph) and no-code agents built through [Amazon Quick Suite](https://aws.amazon.com/quicksuite/) alike. A lightweight CI/CD gate that checks the registry and flags potential duplicates is enough for most organizations, while heavy approval processes encourage bypass. 

 Implement cross-team dependency tracking as a managed practice. Agents declare their upstream and downstream dependencies at registration and update declarations when dependencies change. [Amazon EventBridge](https://aws.amazon.com/eventbridge/) publishes events when agents are deprecated, modified, or decommissioned so downstream teams receive advance notice. Agents exposed through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) benefit from Gateway's tool registration metadata, which automatically tracks which agents consume which tools and reduces manual declaration burden. A dependency graph in [Amazon Neptune](https://aws.amazon.com/neptune/) enables impact analysis for determining how a change to one agent will affect others. 

 Quarterly portfolio reviews help prevent gradual drift. The review assesses four dimensions: 

1.  Utilization (which agents are actively used and which are idle) 

1.  Cost efficiency (which agents deliver business value proportional to cost) 

1.  Redundancy (which agents overlap with others) 

1.  Health (which agents show elevated error rates, degraded performance, or stale configurations) 

 The catalog is the primary data source, enriched with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics, [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) attribution, and the dependency graph. Reviews produce concrete recommendations. These include agents to consolidate, deprecate, or invest in, and cross-team dependency risks to address. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Extend the agent registry into an organizational catalog:** Use [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) to catalog agents with metadata for owning team, business domain, upstream and downstream dependencies, cost-per-month, and business value indicators. 

1.  **Enable semantic capability search:** Use Agent Registry's built-in hybrid search so natural-language queries reveal overlapping capabilities before new development begins. 

1.  **Gate new agent creation on registry search:** Add a pre-creation CI/CD check that requires justification when overlapping agents exist. 

1.  **Track cross-team dependencies:** Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to notify downstream teams when upstream agents are deprecated, modified, or decommissioned. 

1.  **Build a dependency graph:** Use [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) to answer impact-analysis questions before agent modifications. 

1.  **Run quarterly portfolio reviews:** Assess utilization, cost efficiency, redundancy, and health, producing specific recommendations for consolidation, deprecation, and investment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance](agentops03-bp01.html) 
+  [AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)](agentops03-bp02.html) 
+  [AGENTOPS04-BP01 Implement tool registry and catalog management](agentops04-bp01.html) 
+  [AGENTOPS05-BP04 Define and track KPIs for agent workflows](agentops05-bp04.html) 
+  [AGENTCOST06-BP01 Implement lightweight discovery and registry for cost-effective collaboration](agentcost06-bp01.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Preparing the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html) 
+  [AI agents in enterprises: Best practices with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Agents in the enterprise: Best practices with AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY) 
+  [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk) 
+  [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q) 

 **Related services:** 
+  [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Neptune](https://aws.amazon.com/neptune/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 