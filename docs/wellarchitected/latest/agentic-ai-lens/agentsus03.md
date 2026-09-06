

# Agent governance
<a name="agentsus03"></a>

 Organizations that deliberately design how agents interact with users and business processes sustain both automation value and institutional expertise as adoption scales. As agents proliferate, there is a risk that internal expertise will be diluted or lost to fully automated processes. The patterns governing agent interactions must be deliberately designed and maintained, establishing reusable approaches based on real-world organizational needs. 


|  AGENTSUS03: How do I establish durable patterns for agent interactions with users and business processes?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-2"></a>
+  Organizational competencies are deliberately categorized across human-owned, agent-augmented, and fully automated tiers, with clear boundaries enforced by routing and guardrail policies. 
+  Agent development targets processes the organization has already mastered, so automation accelerates proven workflows rather than substituting for process discovery. 
+  Agents ship with declarative specifications, dependency graphs, and policy documentation that remain current as agents evolve, so institutional knowledge is preserved in an accessible form. 
+  A central catalog of deployed agents captures owner, purpose, dependencies, and usage, and teams consult it before building new agents. 
+  The agent portfolio is actively rationalized, with inactive agents flagged for review, decommissioned through a structured lifecycle, and reclaimed infrastructure returned to the shared pool. 

## Maturity levels
<a name="maturity-levels-2"></a>

 These levels summarize what each stage of maturity looks like for agent governance as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agents are built and deployed without competency tiering, ownership assignment, or portfolio oversight. Documentation is thin, decommissioning is one-time, and institutional knowledge is held only by the original developers rather than recorded in any specification.  | 
|  2  |  Emerging  |  Teams have categorized competencies into human-owned, agent-augmented, and fully automated tiers, and [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) are in place for high-stakes escalation. Declarative configuration in [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) captures the baseline agent specification. Basic ownership metadata is recorded for each deployed agent.  | 
|  3  |  Defined  |  Documented workflows feed agent development through [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) RAG sources, and [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) routing separates routine tasks from cases that require human judgment. [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) compares agent outputs against expert baselines, and rotation programs keep subject matter experts practiced in the underlying work. A central agent catalog with ownership and purpose is maintained.  | 
|  4  |  Proactive  |  Runtime documentation generated through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) validates design specifications against actual behavior, and production promotion is gated on current documentation. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metrics flag inactive agents for owner review, and a structured decommissioning lifecycle moves agents through active, under review, deprecated, and decommissioned states. Quarterly portfolio rationalization reviews are a standing cadence.  | 
|  5  |  Optimized  |  Governance is continuous rather than periodic. Portfolio health metrics (total agent count, percentage with active usage, percentage with current documentation) are reviewed at the organizational level. Specification currency, evaluation baselines, and competency tiering adjust based on operational telemetry, and the organization shares its agent governance patterns with its communities of practice.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-2"></a>
+  Teams automate unfamiliar or poorly understood processes where decision criteria and success metrics are not documented, so agent development wastes resources on untested methodologies. 
+  Organizations skip competency tiering, so agents end up handling high-stakes or ambiguous decisions that should be routed to human experts and subject matter expertise quietly atrophies. 
+  Teams treat agent development as code-only artifacts without capturing the expert decision-making patterns and business logic rationale, leaving institutional knowledge locked inside implementations that only the original developers understand. 
+  Agents are deployed without ownership assignment or usage tracking, so there is no basis for evaluating whether an agent is still delivering value or has fallen out of use. 
+  Teams build new agents for capabilities that already exist elsewhere in the organization because no one searches the catalog first, creating redundant implementations and undermining reuse. 

**Topics**
+ [Capability intent](#capability-intent-2)
+ [Maturity levels](#maturity-levels-2)
+ [Common issues to watch for](#common-issues-to-watch-for-2)
+ [AGENTSUS03-BP01 Maintain organizational skills and competencies](agentsus03-bp01.md)
+ [AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies](agentsus03-bp02.md)
+ [AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems](agentsus03-bp03.md)
+ [AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl](agentsus03-bp04.md)