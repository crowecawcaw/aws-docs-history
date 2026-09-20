

# DSOPS06-BP02 Manage regulatory changes
<a name="dsops06-bp02"></a>

 Regulatory changes directly impact cloud operations, security controls, and compliance status. A regulatory change in one jurisdiction might require updates to the common baseline that affect other jurisdictions. A structured change management process helps you assess impact, implement updates, and verify compliance across jurisdictions. 

 **Desired outcome:** 
+  Your organization has a systematic process that evaluates regulatory changes, assesses their impact across jurisdictions, and implements control updates while maintaining adherence. 
+  Changes are traced from the regulatory requirement through to the technical control, with documented evidence for auditors. 

 **Common anti-patterns:** 
+  Technical or operational changes are not traced back to regulatory changes. 
+  Implementing regulatory changes without an effective change management process. 
+  Lacking integration between compliance processes and cloud operations. 
+  A regulatory change in one jurisdiction is implemented without assessing its impact on the common baseline or on other jurisdictions. 

 **Benefits of establishing this best practice:** 
+  Reduced risk through early identification of regulatory requirements. 
+  Lower costs by avoiding emergency remediation efforts. 
+  Improved audit readiness with documented evidence tracing changes to regulatory requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 With a regulatory change detected and triaged, the next challenge is determining its scope and implementing the required updates. Impact assessment is the critical decision point, determining whether a change affects the common baseline (affecting all jurisdictions), a jurisdiction-specific extension (affecting one Region), or specific workloads only, and whether it conflicts with obligations in other jurisdictions. Figure 1 illustrates an example change management process: 

![Flowchart of the regulatory change process: detection and triage, then impact assessment classifying the change as common-baseline, jurisdiction-specific, or workload-only and checking for cross-jurisdictional conflicts, then control updates, then post-implementation verification](https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/images/regulatory-change-flow.png)


 Consider addressing the following questions during impact assessment: 

**Note**  
 The questions listed are not exhaustive. Consult your legal, compliance, and regional teams to adapt them to your organization's specific regulatory context and jurisdictional requirements. 
+  Which jurisdictions are affected, and does the change apply to the common baseline or only to jurisdiction-specific extensions? 
+  Does the change conflict with or diverge from requirements in other jurisdictions, and how will you resolve the conflict? 
+  What is the compliance deadline in each affected jurisdiction, and do the deadlines differ? 
+  Which workloads are in scope, based on their data classification, residency, and the jurisdictions they operate in? 
+  Does the change mandate specific sovereignty controls, such as operator access by nationality, encryption key location, or data residency boundaries? 
+  Which compliance controls, jurisdiction-specific conformance packs, or remediation runbooks need to be developed, modified, or replaced? 
+  Do affected workloads depend on vendors that constrain how the change can be applied in a given jurisdiction? 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Conduct impact analysis:** Assess the scope and implications of the regulatory change using the questions framework (not exhaustive) in the guidance above. Use AWS resource tagging to identify which resources are affected by the change. Determine whether the change affects the common baseline, a jurisdiction-specific extension, or specific workloads, and whether it conflicts with requirements in other jurisdictions. 

1.  **Update the compliance baseline and controls:** Update the compliance baseline, conformance packs, and remediation runbooks to reflect new requirements. Where the change mandates specific technical or operational measures (for example, operator access restrictions by nationality), evaluate the available implementation options. Use resource tags to scope the impact and automate compliance checks for affected resources. 

1.  **Update training content:** Update compliance training to cover the new or modified requirements so that affected teams understand what has changed, how it affects their jurisdiction, and what actions they are accountable for. 

1.  **Verify compliance after implementation:** After implementing changes, verify that updated controls pass validation and that affected resources return to compliance. Document the change, the controls updated, and the verification results as audit evidence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS06-BP01 Track regulatory changes across jurisdictions](dsops06-bp01.html) 
+  [DSOPS02-BP01 Baseline your compliance requirements](dsops02-bp01.html) 
+  [DSOPS05-BP02 Automate compliance remediation](dsops05-bp02.html) 
+  [OPS01-BP03 Evaluate governance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 

 **Related documents:** 
+  [Amazon Web Services: Risk and Compliance](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 

 **Related services:** 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 