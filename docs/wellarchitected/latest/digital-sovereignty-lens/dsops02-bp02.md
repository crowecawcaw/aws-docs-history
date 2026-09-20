

# DSOPS02-BP02 Establish an automated path to compliance
<a name="dsops02-bp02"></a>

 Automation reduces the risk of human error, speeds up the compliance process, and enables continuous monitoring across jurisdictions. When compliance requirements are codified and integrated into your development pipelines, every change is validated before deployment rather than discovered during audits. 

 **Desired outcome:** 
+  Compliance is built into every change through automated validation, detection, and remediation, enabling faster deployments and audit-ready documentation across jurisdictions. 

 **Common anti-patterns:** 
+  Relying on periodic manual audits and spreadsheet-based tracking instead of continuous automated monitoring. 
+  Performing compliance validation only during audit periods rather than continuously. 
+  Failing to use a centralized tool for compliance reporting, resulting in blind spots across jurisdictions. 
+  Generating compliance alerts without automated remediation or clear escalation procedures. 

 **Benefits of establishing this best practice:** 
+  Reduced human error in compliance monitoring, detection, analysis, and remediation. 
+  Real-time regulatory posture with automated evidence collection and reporting, enabling audit-ready responses across jurisdictions. 
+  Consistent enforcement across accounts and jurisdictions, because shared controls are automated once and applied everywhere rather than re-implemented by each team. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Validating compliance early checks every change against compliance policies before deployment, catching violations at provisioning time rather than during an audit. This approach transforms compliance from a periodic assessment activity into a continuous and automated set of checks applied consistently across workloads. 

 Policy as code (PaC) is the foundation for validating compliance early. When compliance requirements are expressed as machine-readable rules rather than natural-language documents, they become testable, version-controlled, and executable. Rules can be unit tested locally, integrated into Continuous Integration/Continuous Delivery (CI/CD) pipelines, and applied consistently across accounts and jurisdictions without manual interpretation. This codification also creates an auditable history of policy changes, making it possible to demonstrate exactly which rules were in effect at any point in time. 

 The compliance catalog developed in the preceding best practice defines *what* must be enforced. This best practice defines *how* enforcement is automated. Organizational controls from the catalog translate into preventive guardrails applied centrally (for example, Region deny policies through [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html)), while jurisdiction-specific and workload-specific controls translate into pipeline validation rules and detective controls scoped to the appropriate accounts. This layered automation mirrors the tiered structure of the catalog itself, ensuring that automation coverage matches policy coverage without requiring each team to re-implement shared controls. 

 Consider using a structured approach such as the [three lines of defense model](https://internalauditor.theiia.org/en/video/2020/august/the-iias-new-three-lines-model-part-1-the-basics/) developed by the Institute of Internal Auditors (IIA) to drive your compliance automation consistently across jurisdictions. In this model, first-line controls in CI/CD pipelines validate policies before provisioning (including jurisdiction-specific rules such as encryption key configurations or Region restrictions), second-line detects resources falling out of compliance with established baselines, and third-line collects evidence to build reports scoped by workload or jurisdiction so that auditors can assess each scope independently. 

### Implementation steps
<a name="implementation-steps"></a>

 **Note:** The following steps are organized along the three lines of defense model. This is a customizable reference. Adapt the sequencing and prioritization to fit your organization's requirements, risk appetite, and operational maturity. 

1.  **First line: embed compliance validation into CI/CD pipelines:** 
   +  Codify your compliance requirements as policy as code. Use [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) to write rules that validate infrastructure templates against compliance policies before deployment. Use cfn-guard validate and cfn-guard test to unit test your rules locally and in your CI/CD pipeline. 
   +  Enable [proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) in AWS Control Tower. Proactive controls are implemented as CloudFormation hooks and check resources for compliance before they are provisioned. 
   +  Provide pre-approved, compliance-aligned infrastructure templates so that developers can provision standardized resources. Consider using [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) to manage standardized CloudFormation or Terraform Cloud products. Include jurisdiction-specific template variants where requirements differ (for example, templates that enforce specific encryption key configurations or Region restrictions). 
   +  Regularly test compliance as code policies through controlled deviations in sandbox or development environments. Verify that deviations are detected and that automated remediation actions work as expected. 

1.  **Second line: detect compliance drift continuously:** 
   +  Enable [detective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/detective-controls.html) in AWS Control Tower to detect noncompliant resources after deployment. AWS Control Tower integrates with AWS Security Hub CSPM and AWS Config to help you monitor your AWS environment. You can enable controls by organizational units (OUs) and AWS accounts spread across jurisdictions. 
   +  When you enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) as part of your AWS Control Tower deployment (achieved through integration with AWS Organizations), you get a unified view from which to continuously identify compliance drifts and prioritize remediations based on severity scores. Enable [consolidated controls view](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-changes-consolidation.html) to reduce findings noise. 
   +  Log API activity with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) across accounts and store logs in a central S3 bucket. Enable encryption and log integrity validation. Consider enforcing [write once read many (WORM)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) storage to protect the chain of evidence. 

1.  **Third line: automate evidence collection and compliance reporting:** 
   +  AWS Control Tower enables AWS Config on all enrolled accounts, so that it can monitor compliance through detective controls and record resource changes. Use [AWS Config Advanced Query](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) to export resource configuration snapshots and compliance evaluation results for targeted resources or time periods. 
   +  Use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) compliance standard scores as evidence of your security posture against frameworks such as NIST SP 800-53 Rev 5 and PCI DSS v4.0. For long-term evidence retention, enable [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html), which ingests Security Hub CSPM findings into Amazon S3 in Open Cybersecurity Schema Framework (OCSF) format for querying and audit purposes. 
   +  For compliance frameworks requiring controls beyond what Config rules can evaluate (such as organizational policies and operational procedures), consider complementing AWS services with [governance, risk, and compliance (GRC) solutions](https://aws.amazon.com/marketplace/solutions/security/governance-risk-compliance/) available in AWS Marketplace. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS03-BP02 Automate evidence collection and reporting](dsops03-bp02.html) 
+  [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.html) 
+  [DSOPS05-BP02 Automate compliance remediation](dsops05-bp02.html) 
+  [OPS05-BP10 Fully automate integration and deployment](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_auto_integ_deploy.html) 
+  [OPS05-BP02 Test and validate changes](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_test_val_chg.html) 

 **Related documents:** 
+  [Introduction to the Three Lines Model](https://internalauditor.theiia.org/en/video/2020/august/the-iias-new-three-lines-model-part-1-the-basics/) 
+  [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) 
+  [Querying the Current Configuration State of AWS Resources (Config Advanced Query)](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) 
+  [Visualizing AWS Config data using Amazon Athena and Quick](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/) 
+  [Implementing a compliance and reporting strategy for NIST SP 800-53 Rev. 5](https://aws.amazon.com/blogs/security/implementing-a-compliance-and-reporting-strategy-for-nist-sp-800-53-rev-5/) 
+  [Consolidating controls in Security Hub CSPM: The new controls view and consolidated findings](https://aws.amazon.com/blogs/security/consolidating-controls-in-security-hub-the-new-controls-view-and-consolidated-findings/) 

 **Related videos:** 
+  [How to implement compliance at scale with the Three Lines of Defense model: AWS AMER Summit Aug 2021](https://www.youtube.com/watch?v=G5oQwykobNw) 
+  [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8) 
+  [AWS re:Invent 2025 - From Code to Policies: Accelerate Development w/ IAM Policy Autopilot (SEC351)](https://www.youtube.com/watch?v=vgA_sq99Kas) 

 **Related examples:** 
+  [AWS Security Hub CSPM Automated Response and Remediation](https://github.com/aws-solutions/automated-security-response-on-aws) 
+  [AWS Config Conformance Pack Samples](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html) 
+  [AWS CloudFormation Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry) 

 **Related services:** 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Service Catalog](https://aws.amazon.com/servicecatalog/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 