

# AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl
<a name="agentsus03-bp04"></a>

 Every agent that stays deployed past its usefulness consumes infrastructure, expands the attack surface, and adds operational overhead that never shows up as an explicit line item. Active portfolio management helps prevent the silent accumulation of cost and complexity that comes with scaled adoption. 

 **Desired outcome:** 
+  Every deployed agent has a documented owner, a clear business purpose, and measurable usage. 
+  Agents that no longer deliver value move through a structured decommissioning lifecycle and are retired. 
+  Teams search the agent registry for existing capabilities before initiating new agent development. 
+  Portfolio health, total agent count, percentage with active usage, percentage with current documentation, is visible at the organizational level. 

 **Common anti-patterns:** 
+  Deploying agents without ownership assignment or usage tracking, so no one can tell which agents still deliver value. 
+  Allowing abandoned agents to persist indefinitely because no decommissioning process exists, accumulating infrastructure cost and expanding the attack surface. 
+  Building new agents for capabilities that already exist in deployed agents elsewhere in the organization, creating redundant implementations. 
+  Relying on informal knowledge of which agents are still useful instead of automated usage tracking, so the decommissioning decision depends on whoever happens to remember which agents are deployed. 

 **Benefits of establishing this best practice:** 
+  Portfolio-level decisions about resource consumption are tied to actual business value delivered, rather than historical deployment patterns. 
+  Decommissioning reclaims infrastructure resources and reduces the operational surface area. 
+  Discoverability of existing capabilities reduces redundant implementations and reinforces reusable architecture patterns. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the authoritative catalog of deployed agents, with each entry capturing business purpose, designated owner, deployment date, dependencies, and usage metrics. Semantic capability search lets teams discover existing agents before building new ones, which is the preventive side of avoiding agent sprawl. Pair the registry with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics tracking invocation frequency and last-invocation timestamp for each agent. Inactive agents then surface automatically for owner review instead of being discovered during audits. 

 Decommissioning becomes routine when it has a defined lifecycle. Active, under review, deprecated, and decommissioned stages give owners clear transitions and give the organization consistent visibility into which agents are on the path to retirement. When an agent is flagged for low usage, the owner's first question is whether it serves a seasonal or infrequent-but-critical purpose. Tax-season agents, quarterly reporting agents, and disaster-recovery agents appear idle most of the time but are essential when they are invoked. A structured review makes that distinction before deprecation happens. 

 During quarterly portfolio rationalization, teams evaluate the full agent inventory against current business priorities, identify overlapping capabilities, and merge redundant implementations into shared patterns (following [AGENTSUS01-BP02 Implement reusable workflow patterns](agentsus01-bp02.html)). They retire agents whose business context has changed. Portfolio health metrics tracked through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), total agent count, percentage with active usage, and percentage with current documentation, make sustainability outcomes visible at the organizational level. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Register every deployed agent with ownership metadata:** Record each agent in [Amazon Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with the following: 
   +  Business purpose 
   +  Designated owner 
   +  Deployment date 
   +  Dependencies 

1.  **Track invocation metrics and flag inactive agents:** Instrument agents with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics capturing invocation frequency and last-invocation timestamp, and flag agents that cross a defined inactivity threshold for owner review. 

1.  **Define a decommissioning lifecycle:** Establish the following stages with transition criteria and owner responsibilities at each: 
   +  Active 
   +  Under review 
   +  Deprecated 
   +  Decommissioned 

1.  **Require registry search before new agent development:** Add a pre-development check to the intake process so teams discover and evaluate existing capabilities before initiating new work. 

1.  **Run quarterly portfolio reviews:** Evaluate the full agent inventory against current business priorities, consolidate overlapping capabilities into shared patterns, and retire agents whose business context has changed. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSUS01-BP02 Implement reusable workflow patterns](agentsus01-bp02.html) 
+  [AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems](agentsus03-bp03.html) 
+  [AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads](agentsus02-bp04.html) 
+  [SUS03-BP02 Remove or refactor workload components with low or no use](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) 
+  [The future of managing agents at scale: AWS Agent Registry now in preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 

 **Related videos:** 
+  [AgentCore Registry: Discover, Govern, and Reuse AI Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 