

# SEC01-BP02 Identify and validate control objectives

 Control objectives translate compliance obligations and identified risks into outcomes your controls must achieve. Validate the controls at a point in time and over a period to produce evidence you can act on and report. 

 **Desired outcome:** 
+  Your control objectives are defined and traceable to specific compliance requirements and risks. 
+  Your controls are implemented and enforced through policy and automation rather than manual effort. 
+  You continually evaluate control effectiveness and can identify where a control is failing. 
+  You can produce evidence of effectiveness, both point-in-time and over a period, for auditors on demand. 

 **Common anti-patterns:** 
+  Regulatory requirements, customer expectations, and industry standards are not clearly understood for the business. 
+  The chosen cybersecurity frameworks and control objectives do not align with business requirements. 
+  Controls are implemented but cannot be measured against the objectives they are meant to satisfy. 
+  Teams report control effectiveness manually, so evidence is stale, inconsistent, and slow to produce. 

 **Benefits of establishing this best practice:** 
+  Controls apply consistently, because they trace to defined objectives rather than individual judgment. 
+  Audit preparation shrinks, because evidence of effectiveness is collected automatically. 
+  Risk decisions improve, because gaps between objectives and implemented controls become visible. 
+  Compliance reporting becomes repeatable across multiple frameworks that share common controls. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A *control objective* is the outcome a control must achieve, such as "only authorized principals can read customer records." A *control* is the mechanism that delivers that outcome. Start from objectives derived from your compliance requirements and your threat model, then select controls that satisfy those requirements. 

 Established cybersecurity frameworks provide a vetted starting set of objectives. The framework that fits depends on your regulatory obligations, customer expectations, and industry. Common choices include [AICPA SOC](https://aws.amazon.com/compliance/soc-faqs/), [HITRUST](https://aws.amazon.com/compliance/hitrust/), [PCI DSS](https://aws.amazon.com/compliance/pci-faqs/), [ISO 27001](https://aws.amazon.com/compliance/iso-27001-faqs/), and the [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework). Many of these frameworks share underlying controls, so a single implementation often satisfies several objectives. You and AWS share responsibility for meeting each objective under the shared responsibility model. [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides the audit reports and responsibility guidance that show which parts AWS covers and which remain yours. 

 Controls fall into two types that work together. *Preventative* controls stop a non-compliant action before it happens. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) cap the maximum permissions for users and roles in your organization, while [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) do the same for resources. 

 *Detective* controls identify non-compliant states after they occur, such as rules in [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) that report on drift. Review detective findings first, and then automate remediation once you trust a rule's behavior. 

 Most objectives need both kinds of controls. Detective controls alone leave a window in which misconfigurations are live, and preventative controls alone can block legitimate work. 

 To validate your controls, deploy managed control sets that align to your frameworks. Start with [AWS Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html), particularly the Foundational Security Best Practices standard and the CIS AWS Foundations Benchmark. Complement gaps with [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html). If you need external help, [Global Security and Compliance Acceleration Partner bundles](https://aws.amazon.com/partners/programs/gsca/bundles/) provide advisors, evidence-collection systems, and auditors. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select frameworks and align objectives:** Evaluate common cybersecurity frameworks against your regulatory, business, and industry requirements, then map your control objectives to the frameworks you select. 

1.  **Establish shared responsibility for each objective:** Use [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) to obtain the documentation and reports for your frameworks, and determine which parts of each objective AWS covers and which parts are yours. 

1.  **Enforce with preventative controls:** Apply [SCPs, resource policies, and role trust policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#orgs-policy-types) to prevent non-compliant resource configurations and actions before they take effect. 

1.  **Detect with managed control sets:** Deploy [Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-view-manage.html) and [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) that align to your objectives. Review their findings before you automate any remediation, so you understand each rule's behavior first. 

1.  **Automate control metrics:** Use tools such as [Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) to provide metrics on your security and control objectives. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 
+  [SEC04-BP01 Configure service and application logging](sec04-bp01.md) 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [FND05-BP01 Shift compliance checks left with proactive controls](fnd05-bp01.md) 

 **Related documents:** 
+  [Downloading reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html) 
+  [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) 

 **Related tools:** 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 