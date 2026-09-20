

# DSREL04-BP01 Plan for disruptions beyond technical failures
<a name="dsrel04-bp01"></a>

 Organizations operating across multiple jurisdictions should consider a broader set of resilience factors beyond technical failures. Changes in international trade policies, regulatory requirements, licensing terms, regional service availability, or natural disasters can affect access to infrastructure, services, or specialist skills. In some cases, these events might affect multiple jurisdictions simultaneously, limiting the availability of nearby recovery sites. Standard disaster recovery planning might not fully address these scenarios, as the disruption isn't a system failure, but a change in the conditions under which the system is permitted or able to operate. 

 **Desired outcome:** 
+  Organizations maintain predefined response plans to address disruptions beyond technical failures. 
+  Each plan identifies trigger conditions, decision criteria, and operational steps to maintain business continuity while maintaining compliance with jurisdictional requirements. 
+  Plans are tested, updated as conditions evolve, and integrated with the sovereignty-aware risk register. 

 **Common anti-patterns:** 
+  Treating non-technical disruption risks as unlikely edge cases that don't warrant dedicated planning, leaving organizations reactive when conditions change. 
+  Depending on a vendor-specific stack without evaluating the impact of export controls, trade restrictions, or licensing changes on continued operations. 
+  Developing response plans in isolation within IT teams, without input from legal, compliance, procurement, and regional business stakeholders who understand jurisdictional implications. 

 **Benefits of establishing this best practice:** 
+  Predefined response plans reduce decision-making time during non-technical disruptions, when delays can result in compliance gaps or operational disruptions. 
+  Systematic evaluation of vendor and technology dependencies identifies concentration risks before they become urgent, supporting informed procurement and architecture decisions. 
+  Documented scenario planning demonstrates due diligence to regulators and auditors, supporting adherence to frameworks such as the [EU Digital Operational Resilience Act](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) (EU DORA) that require information and communication technology (ICT) third-party risk management. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 This best practice is the decision layer above technical disaster recovery. It determines when to invoke capabilities covered elsewhere in this lens, recovery-site selection ([DSREL01-BP02](dsrel01-bp02.html)), workload portability ([DSREL03-BP01](dsrel03-bp01.html)), and risk identification ([DSREL01-BP01](dsrel01-bp01.html)), in response to a change in the conditions under which your workload is permitted or able to operate. 

 Non-technical disruptions usually give you lead time that technical failures don't. A regulatory, trade, or licensing change is often visible before it takes effect, so the response is to monitor regulatory and commercial signals and pre-assign who acts on them, rather than to detect and alarm. Because the response is frequently a legal, contractual, or procurement action, assign decision authority to those functions, not only to operations. 

 Account for correlated impact. A regional geopolitical or regulatory event can affect nearby Regions that technical disaster recovery treats as independent, so confirm your recovery options remain valid for each scenario. Prioritize scenarios by likelihood, impact, and jurisdictions affected, reuse your existing recovery and portability capabilities as the response, and keep the plans in your sovereignty-aware risk register. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify and categorize disruption scenarios:** For each sovereignty-specific risk identified in [DSREL01-BP01](dsrel01-bp01.html), determine whether it requires a dedicated response plan. Common scenario categories that warrant response plans include: 
   +  International trade restrictions affecting access to cloud services, software licenses, or technical support. 
   +  Regulatory change requiring architectural or operational changes (data residency mandates, mandatory use of domestic technology, or new certification requirements). 
   +  Pricing changes and licensing disputes affecting continued operation of vendor-specific components. 
   +  Regional disruptions and natural disasters that affect multiple jurisdictions simultaneously, limiting the availability of nearby recovery options. 

    Document each scenario in your sovereignty-aware risk register with likelihood, impact, and the jurisdictions affected. 

1.  **Develop response plans for priority scenarios:** For each high-priority scenario, create a response plan that includes: 
   +  **Trigger conditions:** Observable signals that indicate the scenario is materializing (for example, draft legislation reaching committee stage, vendor communications about licensing changes). 
   +  **Decision authority and criteria:** Who is authorized to activate the plan, what information they need, and what thresholds apply. Include escalation paths to executive leadership. 
   +  **Operational steps:** Sequenced actions to maintain business continuity. These might include activating a recovery site in an alternative jurisdiction (see [DSREL01-BP02](dsrel01-bp02.html)), migrating workloads using pre-tested portability procedures (see [DSREL03-BP01](dsrel03-bp01.html)), or switching to alternative services and components. 
   +  **Communication plan:** How to notify internal stakeholders, regulators, customers, and vendors. Include regulatory notification timelines where applicable. 
   +  **Rollback criteria:** Conditions under which the response can be reversed and normal operations resumed. 

1.  **Test and update response plans:** Conduct tabletop exercises for priority scenarios at least annually. Include participants with the authority and context to assess cross-functional effects. Document findings, update plans based on lessons learned, and feed results back into the risk register. When conditions change materially, review affected plans outside the regular cycle. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSREL01-BP01 Establish a sovereignty-aware risk management framework](dsrel01-bp01.html) 
+  [DSREL01-BP02 Select and operationalize sovereignty-compliant recovery sites](dsrel01-bp02.html) 
+  [DSREL03-BP01 Design workloads for greater interoperability and portability](dsrel03-bp01.html) 
+  [OPS01-BP05 Evaluate threat landscape](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_threat_landscape.html) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) 

 **Related documents:** 
+  [Controls that enhance data residency protection](https://docs.aws.amazon.com/controltower/latest/controlreference/data-residency-controls.html) 
+  [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [EU Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) 
+  [AWS designated as a critical third-party provider under EU's DORA regulation](https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 
+  [AWS re:Inforce 2024 - Automation in action: Strategies for risk mitigation (GRC301)](https://www.youtube.com/watch?v=gbo-Z01NTc8) 
+  [AWS re:Invent 2025 - Digital sovereignty and data residency with AWS Hybrid and Edge services (HMC310)](https://www.youtube.com/watch?v=CxkRvW42Hgc) 