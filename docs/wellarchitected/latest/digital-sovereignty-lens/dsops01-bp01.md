

# DSOPS01-BP01 Organize compliance for multi-jurisdictional operations
<a name="dsops01-bp01"></a>

 When you have workloads deployed across jurisdictions, your compliance function also needs to scale up to meet a wide range of regulatory requirements consistently across geographic locations. Without a layered approach that separates common controls from jurisdiction-specific ones, teams end up duplicating effort, missing local mandates, or discovering regulatory divergences too late to address them cost-effectively. 

 **Desired outcome:** 
+  Your organization maintains a consistent compliance posture across jurisdictions while adapting to local regulatory requirements. 
+  A common baseline applies organization-wide, with jurisdiction-specific extensions that address local regulatory requirements. 
+  Regional teams independently address local regulations using shared control libraries and reusable conformance packs, making expansion into new jurisdictions faster. 
+  Compliance status is visible across jurisdictions, so stakeholders can compare posture and identify gaps by Region. 

 **Common anti-patterns:** 
+  The same compliance controls are applied globally without accounting for jurisdiction-specific requirements such as data residency mandates, breach notification processes, or operator access restrictions. 
+  Compliance knowledge and skills are concentrated at a single location. Regional teams lack the expertise or authority to address local regulatory requirements. 
+  Each team builds its own compliance tooling and processes from scratch, resulting in duplicative initiatives, inconsistent controls, and gaps that are difficult to detect. 
+  There is no process to identify or resolve divergences between overlapping regulatory requirements across workloads. 

 **Benefits of establishing this best practice:** 
+  Faster expansion into new jurisdictions by reusing a common compliance baseline and composing jurisdiction-specific controls on top. 
+  Reduced duplication of effort across teams through shared control libraries, conformance packs, and centralized tooling. 
+  Improved audit readiness across Regions through consistent documentation, centralized dashboards, and automated evidence collection. 
+  Better visibility into compliance posture across jurisdictions, enabling data-driven decisions about where to invest in controls and remediation. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 With a layered compliance model, organizations maintain consistency across jurisdictions while adapting to local regulatory requirements. Regulatory frameworks differ by jurisdiction in areas such as data residency, operator access restrictions, breach notification timelines, and data subject rights. The layered approach establishes a common organizational baseline covering controls that apply everywhere (encryption at rest and in transit, access logging, and least privilege), then composes jurisdiction-specific extensions on top. This separation helps teams reason about compliance at the right level of abstraction. Shared controls are governed centrally, while local requirements are owned by those with the regulatory expertise to interpret them correctly. 

 [AWS Organizations](https://aws.amazon.com/organizations/) provides the account structure to enforce boundaries between jurisdictions, while [AWS Control Tower](https://aws.amazon.com/controltower/) enables centralized deployment of baseline controls across accounts and Regions, including controls in the [digital sovereignty group](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html). Regional teams compose jurisdiction-specific controls as additional guardrails scoped to their accounts. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) aggregates compliance findings across jurisdictions into a single view, so you can compare posture by Region and identify gaps. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define compliance accountability:** Determine who is accountable for compliance across jurisdictions, covering baseline definition, jurisdiction-specific control implementation, monitoring, remediation, reporting, and auditing. Establish accountability for data residency decisions: Region selection, cross-border data transfers, and operator location constraints. Record the rationale for each decision so it is traceable during audits. 

1.  **Document the compliance lifecycle and standard operating procedures:** Outline the compliance lifecycle spanning discovery, baselining, development, operationalization, monitoring, remediation, and evolution. Create regionalized standard operating procedures for data subject requests, breach reporting, and non-compliance incidents. Align compliance policies with business objectives, incorporating framework-specific requirements (for example, Health Insurance Portability and Accountability Act (HIPAA) for healthcare workloads). 

1.  **Build the common baseline and jurisdiction-specific extensions:** Define the common organizational baseline and deploy it across all accounts using [AWS Control Tower](https://aws.amazon.com/controltower/), including controls in the [digital sovereignty group](https://docs.aws.amazon.com/controltower/latest/controlreference/digital-sovereignty-controls.html). For each jurisdiction, identify additional or divergent requirements and document resolution. Package jurisdiction-specific detective controls as [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) scoped to regional accounts, so the baseline stays centrally governed while local extensions remain independently owned. 

1.  **Establish cross-jurisdictional visibility and scaling metrics:** Configure [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) to aggregate compliance findings across jurisdictions, verifying that cross-Region aggregation doesn't violate data residency restrictions. Define a regulatory change management process that assesses the impact of changes on both the common baseline and jurisdiction-specific extensions. Track time-to-compliance for new jurisdictions and control reusability across regional teams as indicators of how effectively the layered model supports expansion. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP02 Enable distributed compliance execution](dsops01-bp02.html) 
+  [DSOPS02-BP01 Baseline your compliance requirements](dsops02-bp01.html) 
+  [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.html) 
+  [DSOPS06-BP01 Track regulatory changes across jurisdictions](dsops06-bp01.html) 
+  [DSSEC09-BP01 Integrate compliance requirements into incident response](dssec09-bp01.html) 
+  [OPS01-BP03 Evaluate governance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 
+  [[AG.ACG.1] Adopt a risk-based compliance framework](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.1-adopt-a-risk-based-compliance-framework.html) 
+  [[AG.ACG.2] Implement controlled procedures for introducing new services and features](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.2-implement-controlled-procedures-for-introducing-new-services-and-features.html) 
+  [[AG.ACG.3] Automate deployment of detective controls](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.3-automate-deployment-of-detective-controls.html) 
+  [[AG.ACG.4] Strengthen security posture with ubiquitous preventive guardrails](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.4-strengthen-security-posture-with-ubiquitous-preventive-guardrails.html) 
+  [[AG.ACG.6] Implement auto-remediation for noncompliant findings](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.6-implement-auto-remediation-for-non-compliant-findings.html) 

 **Related documents:** 
+  [Scaling a governance, risk, and compliance program for the cloud, emerging technologies, and innovation](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/) 
+  [Evolving GRC to Maximize Your Business Benefits from the Cloud](https://aws.amazon.com/blogs/enterprise-strategy/evolving-grc-to-maximize-your-business-benefits-from-the-cloud/) 
+  [Optimizing cloud governance on AWS: Integrating the NIST Cybersecurity Framework, AWS Cloud Adoption Framework, and AWS Well-Architected](https://aws.amazon.com/blogs/security/optimizing-cloud-governance-on-aws-integrating-the-nist-cybersecurity-framework-aws-cloud-adoption-framework-and-aws-well-architected/) 
+  [Decision Guide: Choosing AWS security, identity, and governance services](https://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html) 
+  [Building Security from the Ground up with Secure by Design](https://d1.awsstatic.com/partner-network/AWS-SANS-Secure-by-Design-Whitepaper-2024.pdf) 
+  [Exploring the new AWS European Sovereign Cloud: Sovereign Reference Framework](https://aws.amazon.com/blogs/security/exploring-the-new-aws-european-sovereign-cloud-sovereign-reference-framework/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 

 **Related examples:** 
+  [Security Hub CSPM Compliance Analyzer](https://github.com/awslabs/security-hub-compliance-analyzer) 
+  [AWS Well-Architected Labs - Security](https://wellarchitectedlabs.com/security/) 
+  [AWS Config Conformance Pack Samples](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html) 

 **Related services:** 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 