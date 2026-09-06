

# AGENTOPS07-BP04 Implement break-glass operational runbooks
<a name="agentops07-bp04"></a>

 Write and test emergency runbooks before they are needed. Rehearsed manual fallback procedures, accessible escalation paths, and current contact information turn a complete agent failure into a brief manual period rather than a prolonged outage. 

 **Desired outcome:** 
+  When agents fail completely or behave unexpectedly, human operators execute well-documented manual procedures that maintain business continuity. 
+  Break-glass runbooks are tested regularly, and operators are trained and confident in the manual procedures. 
+  Escalation paths and contact information stay current. 
+  Emergency response times meet defined objectives because procedures are documented, accessible, and practiced. 

 **Common anti-patterns:** 
+  Assuming agent systems will always be available and not documenting manual fallback procedures, leaving operators without guidance when agents fail during critical business operations. 
+  Creating break-glass runbooks once and never testing or updating them, resulting in procedures that reference outdated systems, incorrect contacts, or steps that no longer work. 
+  Storing emergency procedures in locations inaccessible during the outage scenarios they are designed to address (for example, in systems that depend on the failing agent infrastructure). 
+  Designing manual fallback processes that require specialized knowledge held by only one or two team members, creating single points of failure in emergency response. 
+  Failing to define clear triggers for when break-glass procedures should be activated, causing delays as operators debate whether the situation warrants manual intervention. 

 **Benefits of establishing this best practice:** 
+  Documented break-glass procedures support consistent emergency responses regardless of who is on call. 
+  Break-glass runbooks formalize the transition from automated agent operations to human-driven processes, keeping business continuity intact when agent systems can't function. 
+  Regular drills keep procedures current and operators ready, so response quality doesn't depend on which person happens to be on call. 
+  Clear activation triggers remove hesitation that delays response. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Inventory your system by identifying every critical business process that depends on agent systems and assess the impact of agent unavailability for each. The output is a ranked list of processes that need break-glass coverage, from brief inconveniences to service-stopping issues. Processes at the top of the list get runbooks first. 

 Each runbook should cover trigger conditions, step-by-step manual execution instructions, required access credentials, escalation contacts with primary and backup personnel, expected completion times, and criteria for returning to automated operations. The most common failure mode, and the most dangerous, is runbooks stored in systems that depend on the very infrastructure they are designed to work around. An emergency runbook stored in a wiki that depends on the same agent infrastructure is a runbook you can't read during the outage. Store runbooks in a highly available, agent-independent location, with offline copies accessible to on-call operators. 

 Single-person knowledge is the other common single point of failure. Designing manual procedures that only one or two people can execute produces a plan that collapses when those people are unavailable. Broaden the knowledge base through tabletop exercises, documentation that doesn't assume expertise, and regular cross-training. 

 Activation triggers remove hesitation from response. Clear conditions, for example, "agent error rate exceeds 50% for 15 minutes" or "complete agent infrastructure unavailability for 5 minutes", tell operators when to switch to manual procedures without waiting for judgment calls under pressure. Automated alerts that explicitly name the trigger conditions they have met make the decision obvious. 

 Testing keeps runbooks alive. Tabletop exercises quarterly, operators walking through runbook steps without executing them, catch outdated references and missing steps. Full drills semi-annually, operators actually executing manual procedures in a non-production environment, catch everything tabletop exercises miss. Drill results become input for runbook revisions, not just training feedback. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory critical business processes:** Assess the impact of agent unavailability for each to produce a ranked list. 

1.  **Document manual fallback procedures:** Cover each critical process assuming no agent system availability, with step-by-step instructions. 

1.  **Establish escalation paths:** Include primary and backup contacts, with a process for keeping contact information current. 

1.  **Store runbooks independently:** Use a highly available, agent-independent location with offline copies accessible to on-call operators. 

1.  **Define clear activation triggers:** Configure automated alerts that notify operators when trigger conditions are met. 

1.  **Conduct exercises on a cadence:** Run tabletop exercises quarterly and full drills semi-annually, and update procedures based on findings. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS07-BP01 Implement automated response and recovery mechanisms](agentops07-bp01.xml) 
+  [AGENTOPS07-BP02 Establish operational knowledge management systems](agentops07-bp02.xml) 
+  [AGENTOPS07-BP03 Augment change management to accommodate technical improvements and business requirements](agentops07-bp03.xml) 
+  [AGENTOPS04-BP03 Develop fallback behavior and error handling for tool invocations](../agentops04/agentops04-bp03.xml) 
+  [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Build resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents) 
+  [Agentic AI in the Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) 
+  [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 