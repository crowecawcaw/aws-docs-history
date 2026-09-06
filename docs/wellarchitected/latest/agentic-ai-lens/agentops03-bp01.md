

# AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance
<a name="agentops03-bp01"></a>

 An agent portfolio without lifecycle discipline becomes a graveyard of undocumented services with forgotten owners. Explicit lifecycle stages, named SME ownership, and clean decommissioning keep the portfolio tractable as it grows from a handful of agents to dozens or hundreds. 

 **Desired outcome:** 
+  Every agent has a documented lifecycle state (development, pilot, production, deprecated, and decommissioned) with defined transition criteria. 
+  Onboarding follows a standardized provisioning process that configures required resources, permissions, and monitoring before an agent handles production traffic. 
+  Decommissioning cleanly removes retired agents, no orphaned resources, dangling permissions, or undocumented dependencies left behind. 
+  Each agent has a named SME owner accountable for its behavior, performance, and eventual retirement. 

 **Common anti-patterns:** 
+  Deploying agents to production without a defined lifecycle state or designated owner, so no one is accountable when behavior needs attention. 
+  Operating without decommissioning procedures, leaving retired agents running with active permissions and consuming resources long after they were replaced. 
+  Skipping the pilot stage and pushing agents from development directly to full production, missing the chance to validate behavior under real traffic with enhanced monitoring. 
+  Treating the agent registry as a one-time artifact that nobody updates once the agent is live. 

 **Benefits of establishing this best practice:** 
+  Standardized lifecycle procedures produce consistent provisioning, operation, and retirement, reducing operational complexity as the portfolio grows. 
+  Documented lifecycle states and transition criteria create an auditable record of each agent's history for compliance and governance. 
+  Named owners accelerate incident response. When an agent misbehaves, the team knows who to engage without a search. 
+  Clean decommissioning helps prevent the slow accumulation of abandoned resources that becomes a cost and security problem over time. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Five stages cover the operational arc of almost any agent: 

1.  Development (under active development, not serving production traffic) 

1.  Pilot (limited production use with enhanced monitoring and cost validation) 

1.  Production (full deployment with standard operational procedures) 

1.  Deprecated (scheduled for decommissioning, no new integrations) 

1.  Decommissioned (removed from service, resources cleaned up) 

 Each transition should carry explicit criteria, required approvals, validation gates, and documentation requirements, so stage changes are decisions rather than drift. 

 Pilot validates economic viability and identifies issues before full deployment, reducing the cost of addressing problems. For teams using spec-driven development with tools like Kiro, the spec workflow produces the documentation needed for lifecycle governance as a byproduct. This is a useful side effect worth using rather than rebuilding. 

 An agent registry is a durable artifact that makes this process coherent. It should track agent ID, lifecycle state, owner, dependencies, capabilities, and operational metadata. Without a registry, lifecycle state exists only in people's heads, making it difficult to track and manage consistently across the organization. The registry becomes the input for portfolio reviews, decommissioning dependency analysis, and emergency response. 

 Emergency lifecycle transitions deserve their own processes. Automated emergency termination switch mechanisms allow immediate revocation of an agent's permissions and halting of operations, enabling rapid response to operational issues. The decommissioning runbook does similar work for the planned case. It removes resources, revokes permissions, updates the registry, and notifies dependent systems as automated steps rather than as checklist items. For agents built through no-code platforms like [Amazon Quick Suite](https://aws.amazon.com/quicksuite/), the same lifecycle rules apply. The registry tracks them, portfolio reviews consider them, and decommissioning cleans them up. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Document the five lifecycle stages:** Specify transition criteria, required approver roles, and validation gates for each stage. 

1.  **Build the agent registry:** Track agent ID, lifecycle state, owner, dependencies, capabilities, and operational metadata in a durable store. 

1.  **Automate lifecycle state transitions:** Validate criteria, trigger stage-specific actions, and record transitions with attribution, deployments, permission changes, monitoring setup, and decommissioning steps. 

1.  **Create standardized provisioning templates:** Configure required resources, permissions, and monitoring automatically so new agents enter production with a consistent baseline. 

1.  **Implement emergency termination switch and decommissioning runbooks:** Include dependency analysis before running so decommissioning doesn't break upstream consumers. 

1.  **Establish quarterly portfolio reviews:** Identify agents for deprecation or decommissioning, including those built with no-code platforms like [Amazon Quick](https://aws.amazon.com/quicksuite/). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS01-BP01 Establish well-defined agent roles, responsibilities, and success criteria](agentops01-bp01.html) 
+  [AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)](agentops03-bp02.html) 
+  [AGENTOPS03-BP03 Implement agent-specific scaling policies and capacity planning](agentops03-bp03.html) 
+  [AGENTOPS02-BP02 Implement configuration drift detection and remediation](agentops02-bp02.html) 
+  [AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management](agentcost06-bp02.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Focus area 5: Manage the lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/focus-areas-lifecycle.html) 
+  [Evolving software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html) 
+  [Preparing the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html) 
+  [Kiro Specs](https://kiro.dev/docs/specs/) 
+  [Operationalizing Agentic AI Part 1: A Stakeholder's Guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Agents in the enterprise: Best practices with AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY) 
+  [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q) 
+  [AWS re:Invent 2024 - Bridging from POC to production: Intro to AgentCore (AIM2204)](https://www.youtube.com/watch?v=oDjESsByBmM) 

 **Related workshops:** 
+  [Getting started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 