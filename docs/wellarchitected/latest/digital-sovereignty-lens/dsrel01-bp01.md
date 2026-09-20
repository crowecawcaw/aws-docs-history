

# DSREL01-BP01 Establish a sovereignty-aware risk management framework
<a name="dsrel01-bp01"></a>

 Establish a risk management framework that identifies, prioritizes, and mitigates business continuity risks specific to sovereign workloads. Beyond standard technical and operational risks, sovereign workloads face risks from large-scale disruptions caused by natural disasters, regional instabilities, and shifts in international trade policies that require dedicated assessment and mitigation. 

 **Desired outcome:** 
+  A prioritized risk register documents sovereignty-specific business continuity risks alongside standard technical and operational risks. 
+  Mitigation strategies address data residency constraints, cross-border recovery implications, and regulatory obligations. 
+  Risk assessments are continuous and evolve with the regulatory environment. 

 **Common anti-patterns:** 
+  Limiting risk assessment to technical and operational risks without considering sovereignty-specific categories. 
+  Treating risk documentation as one-time deliverables instead of living artifacts that evolve over time. 
+  Conducting risk assessments without cross-functional input from legal, compliance, and regional teams, missing jurisdiction-specific dependencies. 
+  Developing mitigation plans that don't account for data residency constraints, for example, a failover plan that moves data to an AWS Region in a different jurisdiction. 

 **Benefits of establishing this best practice:** 
+  Proactive identification of sovereignty-specific risks reduces exposure to compliance violations during disruptions. 
+  Continuous risk tracking enables rapid response to regulatory changes and evolving international trade conditions. 
+  Systematic documentation demonstrates due diligence to auditors and regulators, supporting adherence to frameworks such as the EU Digital Operational Resilience Act (EU DORA), General Data Protection Regulation (GDPR), and industry-specific regulations. 
+  Data-driven prioritization focuses investments on highest-impact risks, including those unique to sovereign workloads. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Sovereignty-specific risks, such as disruptive regulatory changes, cross-border data movement constraints, and jurisdictional concentration, often fall between traditional IT and compliance risk disciplines. Addressing them requires a cross-functional team that brings together IT, security, compliance, legal, and business perspectives into a unified risk assessment framework. This breadth of input enables organizations to evaluate sovereignty risks as a whole, surfacing interdependencies that only become visible when multiple disciplines examine the same scenario. 

 Many sovereign nations are strengthening regulatory requirements related to cyber-resiliency to protect critical national infrastructure. Regulations such as [EU DORA](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) require financial entities to maintain a sound, thorough, well-documented information and communications technology (ICT) risk management framework as part of their overall ICT risk management system. Your risk management framework needs to account for these and similar regulatory requirements applicable to your jurisdiction. 

 **Balancing residency and resilience:** Sovereignty constraints and resilience can pull in opposite directions. Strict data residency mandates that restrict failover to a single jurisdiction can potentially create concentration risks that could affect availability. Conversely, unrestricted cross-jurisdictional recovery can conflict with data residency and regulatory requirements. Assess both risks and identify where multi-Region deployments within the same sovereign jurisdiction, pre-authorized temporary waivers, or contingency arrangements in approved jurisdictions are acceptable. Similar logic applies to supply chains. Concentration in one country or geography could increase exposure to disruption in that jurisdiction. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify sovereignty-specific risks:** Conduct a business impact analysis (BIA) that includes the following risk categories beyond standard technical and operational risks: 
   +  **International trade and regulatory risks:** Changes in international trade policies, regulatory requirements, or emerging sovereignty legislation might affect access to certain cloud services, technology components, or specific AWS Regions. Establish a process to track regulatory developments in your operating jurisdictions and assess their potential impact. 
   +  **Concentration risks:** Reliance on infrastructure and services within a single jurisdiction might create resilience challenges if that jurisdiction is affected by regional disruptions such as natural disasters or infrastructure disruptions. 
   +  **Data residency risks in disaster recovery (DR):** Failover to an AWS Region in a different jurisdiction might create compliance issues. Identify which workloads have data residency constraints that might limit DR site selection, and factor these into your recovery planning. 
   +  **Supply chain and operational risks:** Changes to licensing terms, pricing models, or service availability might affect operational continuity. Key personnel or operational support teams might become unavailable. Verify that the workforce required to activate and execute disaster recovery procedures is appropriately distributed, cross-trained, and documented. 

    This list of risks isn't exhaustive. It varies by jurisdiction, workload characteristics, and industry. 

1.  **Prioritize risks with a sovereignty dimension:** Score each risk by likelihood and impact. Add a sovereignty impact dimension to your scoring: 
   +  Does this risk affect data residency compliance or could it trigger cross-border data movement? 
   +  Does it expose the organization to regulatory consequences in specific jurisdictions? 
   +  Could it affect the organization's ability to operate in a specific jurisdiction? 
   +  Could this lead to invalidation of existing software or service contracts? 

1.  **Build mitigation strategies using AWS services:** For each risk, document preventive controls, detective controls, remediation measures, an accountable owner, and a timeline. Use the following AWS services to support this process: 
   +  [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) to define resilience goals, assess your resilience posture, and implement recommendations. 
   +  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) to continuously assess your resources against security standards that include controls mapped to high availability and data protection domains. 
   +  [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) to map service dependencies and trace requests through distributed applications. 
   +  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html) to set preventive, proactive, and detective controls that map to compliance frameworks. 

1.  **Maintain the risk register as a living artifact:** Integrate risk review into your regular operational cadence: 
   +  Schedule regular reviews. 
   +  Update the risk register after incidents, regulatory changes, and architecture modifications. 
   +  Track metrics: open risks, overdue mitigations, and risk trend over time. 
   +  Integrate with change management to assess new risks when deploying changes. 

 The following is an example of how a sovereignty-aware risk register for an EU-based workload might be structured. Likelihood and impact are scored from 1 to 10. 


|  Risk ID  |  Description  |  Category  |  Sovereignty Consideration  |  Likelihood  |  Impact  |  Priority  |  Mitigation Strategy  |  Owner  |  Status  |  Review Date  | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
|  R-001  |  Primary AWS Region becomes inaccessible  |  Technical  |  A DR site can be activated, but the site must be within the EU  |  2  |  10  |  20  |  Build and validate Multi-Region DR site within EU  |  Ops Lead  |  Active  |  Monthly  | 
|  R-002  |  New data residency regulation or a new data localization mandate  |  Regulatory  |  May require changes to technical architecture and operational support contracts  |  2  |  5  |  10  |  Track regulatory pipeline and plan ahead  |  Compliance  |  Active  |  Quarterly  | 
|  R-003  |  Outage affecting more than one EU member state  |  Technical  |  A DR site within the EU can't be activated  |  1  |  10  |  10  |  Activate DR in an approved jurisdiction outside the EU  |  CTO  |  Planned  |  Half-yearly  | 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html) 
+  [OPS01-BP05 Evaluate threat landscape](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_threat_landscape.html) 
+  [OPS01-BP06 Evaluate tradeoffs while managing benefits and risks](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_tradeoffs.html) 
+  [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html) 

 **Related documents:** 
+  [Risk Management](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/risk-management.html) 
+  [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [AWS designated as a critical third-party provider under EU's DORA regulation](https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 
+  [AWS re:Invent 2023: Backup and Disaster Recovery Strategies for Increased Resilience (ARC208)](https://aws.amazon.com/awstv/watch/173a403d06b/) 

 **Related services:** 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS X-Ray](https://aws.amazon.com/xray/) 