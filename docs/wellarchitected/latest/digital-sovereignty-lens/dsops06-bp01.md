

# DSOPS06-BP01 Track regulatory changes across jurisdictions
<a name="dsops06-bp01"></a>

 Regulations change at different times across jurisdictions, and a change in one can diverge from requirements in another. Without a structured approach to tracking these changes, organizations risk falling out of compliance or discovering divergences too late to address them cost-effectively. 

 **Desired outcome:** 
+  You detect regulatory changes early and assess their impact on your compliance baseline. 
+  You update controls, conformance packs, and remediation runbooks before compliance deadlines. 
+  Your tracking approach covers all jurisdictions where you operate and identifies cross-jurisdictional divergences. 

 **Common anti-patterns:** 
+  Monitoring only global standards while ignoring region-specific regulations that affect workload deployment. 
+  Discovering regulatory changes after compliance deadlines have passed or during audit. 
+  Addressing compliance reactively without a structured process for detecting and assessing impending changes. 

 **Benefits of establishing this best practice:** 
+  Reduced risk through early identification of regulatory changes that affect deployed workloads. 
+  Lower costs by avoiding last-minute remediation when requirements change. 
+  Faster expansion into new jurisdictions because the compliance baseline is maintained and auditable. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A structured regulatory intelligence function helps organizations detect changes early, assess cross-jurisdictional dependencies, and implement updates before compliance deadlines. The function works most effectively when it combines internal expertise and external sources (local legal counsel, regional compliance specialists, industry working groups, and regulatory consultation exercises). These external sources, not an AWS service, identify impending regulatory change. 

 Regulatory tracking feeds into a multi-stage pipeline that converts detected changes into implemented controls. Detection identifies that a change is impending. Assessment determines which controls, workloads, and jurisdictions are affected. Update applies the changes to the compliance baseline, conformance packs, and remediation runbooks. Validation confirms that updated controls are effective and that no new gaps were introduced during the transition. 

 When a change in one jurisdiction affects another, the assessment stage benefits from centralized coordination. A change identified in one jurisdiction must be evaluated for divergences or conflicts with requirements in other jurisdictions. Codifying jurisdiction-specific requirements in [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) makes these divergences visible through automated evaluation rather than manual comparison. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a regulatory intelligence capability:** Define a structured process for monitoring regulatory changes across jurisdictions where you operate. The process covers detection of impending changes, assessment of impact on existing workloads and controls, and coordination of updates across affected jurisdictions. 

1.  **Augment tracking with third-party tooling:** Complement your regulatory intelligence process with dedicated tooling. Explore [governance, risk, and compliance (GRC) solutions](https://aws.amazon.com/marketplace/solutions/security/governance-risk-compliance/) in AWS Marketplace that track regulatory changes and map them to controls, so detection and impact assessment are not entirely manual. 

1.  **Update controls and coordinate across jurisdictions:** When a regulatory change is identified, update the compliance baseline, conformance packs, and remediation runbooks to reflect new requirements. Coordinate updates across affected jurisdictions so that changes in one don't create unintended divergences in another. 

1.  **Establish regular review cycles:** Conduct regular reviews of compliance configurations to verify they remain aligned with current regulations. Track metrics such as time from regulatory change announcement to implementation completion, and percentage of resources in compliance across jurisdictions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS01-BP03 Implement compliance training and awareness](dsops01-bp03.html) 
+  [DSOPS02-BP01 Baseline your compliance requirements](dsops02-bp01.html) 
+  [OPS01-BP03 Evaluate governance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 

 **Related documents:** 
+  [Amazon Web Services: Risk and Compliance](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html) 
+  [Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 
+  [AWS Compliance Center](https://aws.amazon.com/financial-services/security-compliance/compliance-center/) 
+  [AWS services in scope by compliance programs](https://aws.amazon.com/compliance/services-in-scope/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 
+  [AWS re:Inforce 2024 - Automation in action: Strategies for risk mitigation (GRC301)](https://www.youtube.com/watch?v=gbo-Z01NTc8) 

 **Related services:** 
+  [AWS Config](https://aws.amazon.com/config/) 