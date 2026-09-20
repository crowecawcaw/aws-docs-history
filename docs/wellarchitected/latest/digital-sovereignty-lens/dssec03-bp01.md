

# DSSEC03-BP01 Validate policy effectiveness through automated analysis
<a name="dssec03-bp01"></a>

 Manual policy validation is error-prone and doesn't scale well with the complexity of modern cloud environments. Automated reasoning tools analyze access policies to identify potential security gaps, over-permissive access, and unintended permissions before deployment. 

 **Desired outcome:** 
+  Access policies are checked with automated reasoning before they are deployed, so overly permissive or unintended access, such as a policy that would allow sharing data outside your zone of trust, is identified rather than left to manual review alone. 

 **Common anti-patterns:** 
+  Relying solely on manual code reviews to validate complex IAM policies and resource-based policies. 
+  Using generic policy templates without validating them against specific organizational and jurisdictional requirements. 
+  Defaulting to providing over-permissive actions in policy documents. 
+  Not validating policies against regulatory compliance requirements before implementation. 

 **Benefits of establishing this best practice:** 
+  Can accelerate development cycles by catching policy issues early in the development process. 
+  Supports more confident policy changes through impact analysis. 
+  Automated reasoning gives auditors verifiable evidence that a policy doesn't grant specific unintended access. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Access policies accumulate faster than anyone can review by hand. In a multi-account, multi-jurisdiction estate, a single overly broad statement can permit access across a boundary, and manual review will not reliably catch it. [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) applies automated reasoning to policies. It analyzes the policy itself, translating it into logical statements and using solvers to characterize the access the policy allows. For sovereign workloads, you can then check that a policy doesn't permit specific actions, such as sharing a resource outside your zone of trust, rather than depending on manual reviews. 

 Integrate Access Analyzer in two phases, in order. 

 **Identify and Refine:** Using IAM Access Analyzer from the AWS Management Console, first establish your zone of trust (your organization or an account). Run verifications to **identify** the permissions granted across your resources, and then **refine** your access policies to match your organization's security standards. This step helps you establish a baseline that you can use in the next step. 

 **Validate:** Next, run [custom policy checks](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-custom-policy-checks.html) to compare policy changes against baselines. The sequence matters. A validation gate is only meaningful after you have a clean baseline to compare against, because each new policy can grant back the access you worked to remove. 

 The Identify and Refine phase is a coverage and cost decision, because the three analyzers are priced differently. Analyzing resources shared outside your zone of trust ([external access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-resource-identification)) carries no additional charge, so you can enable it in every Region you use. Analyzing [unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-unused-access-analysis) is a paid feature billed per IAM role or IAM user per month, and it uses a tracking period you set (1 to 365 days). Analyzing [internal access](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-internal-access-analysis) is a paid feature billed per resource, per Region, so reserve it for the business-critical resources holding your most sensitive sovereign data. 

 Two behaviors of the analyzers are worth anticipating. The external access analyzer generates a finding for any resource shared outside your zone of trust, whether you intended the sharing, so expect to review and archive the access you have deliberately approved. Unused access findings depend on the tracking period, so permissions exercised rarely, such as delete or create actions, can appear unused in a short window. Set the tracking period with that in mind before you remove permissions. Where you run policy checks also matters. Custom policy checks can be run through the AWS CLI or the IAM Access Analyzer API, so you can enforce them in a deployment pipeline, where a failing check stops a noncompliant policy before it is attached to an entity. 

 You can integrate IAM Access Analyzer with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), to send findings. Security Hub CSPM can then include those findings in its analysis of your overall sovereignty posture. You can also send an event to [Amazon EventBridge](https://aws.amazon.com/eventbridge/) when a finding is generated, and alert teams to review and remove excessive permissions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable external access analyzer**: The external access analyzer is a free service (but the unused and internal ones are not free). For external access, IAM Access Analyzer analyzes the resource-based policies that are applied to AWS resources in the Region where you enabled the service. For example, for IAM roles, IAM Access Analyzer analyzes [trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#term_trust-policy). Each time a resource-based policy is modified, IAM Access Analyzer analyzes the policy, but it may take up to 30 minutes for the analysis to trigger. For this check, IAM Access Analyzer doesn't examine access logs to determine whether an external entity has actually accessed a resource within your zone of trust. Instead, it generates a finding when a resource-based policy allows access to a resource, regardless of whether the resource was accessed by the external entity. The external access analyzer will generate findings even for those resources that you may have chosen to intentionally share outside your zone of trust. You [can archive](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-archive.html) such findings. 

1.  **Enable unused access analyzer**: Unused access findings are generated for IAM entities (such as roles and users) within the selected account or organization, based on the number of days (known as tracking days) specified when creating the analyzer. For example, if you set the tracking period to 90 days and scope it to your account, the unused access analyzer will flag unused roles, permissions, access keys, and passwords within that account. In addition to reporting findings, the analyzer provides **policy recommendations** when it detects unused permissions, allowing you to refine access and remediate potentially over-permissive policies. Set the tracking days parameter to match your internal or audit cycles. Otherwise, start with a period of six months or a year and adjust over time. You can also exclude certain tagged resources (roles and users) from being evaluated, for example exclude read-only auditor roles that you know will only be used once a year. When removing permissions, be aware that certain permissions (such as Delete or Create) might only be triggered sparingly, and removing them too soon might break your workloads. 

1.  **Enable internal access analyzer (optional)**: Enabling this analyzer has cost implications (billed per resource, per Region, per month, as described in [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/)). Therefore, only enable it for resources holding sovereign data you consider highly sensitive. You can enable this analyzer on a per-resource (or set of resources) basis, and it will begin reporting access findings. 

1.  **Validate policies with custom policy checks**: Create organization-specific validation rules to verify that new policies comply with your security standards and regulatory requirements. You can find examples of reference policies and learn how to set up and run policy checks for new access through the [IAM Access Analyzer custom policy checks samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples) repository on GitHub. To run this policy check, use the AWS CLI and invoke the [check-no-new-access](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/check-no-new-access.html) command. Define a reference policy that sets guardrails around what you consider acceptable, develop a candidate policy that you want to validate, and then specify the policy-type to perform the analysis. 

   ```
   AWS accessanalyzer check-no-new-access --existing-policy-document file://reference-policy.json --new-policy-document file://candidate-policy.json --policy-type IDENTITY_POLICY
   ```

    For example, [this reference policy](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples/blob/main/identity-policies/check-access-to-sensitive-resource/dynamodb-table.md) checks if a candidate policy grants access to any of the listed dynamodb actions on a specific sensitive table. These checks are powered by [Zelkova](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html), AWS's automated reasoning engine, which translates IAM policies into logical statements, so they evaluate what a policy allows with a high degree of assurance rather than relying on pattern matching. 

1.  **Validate resource configurations**: Beyond policy validation, verify that resources themselves are configured to meet sovereignty requirements, for example, that KMS keys are single-Region, S3 buckets don't have cross-Region replication, and resources carry sovereignty tags. For detailed guidance on writing and deploying sovereignty-specific configuration rules using CloudFormation Guard, AWS Config custom rules, and CloudFormation Hooks, see [DSSEC03-BP03 Validate resource configurations for sovereignty compliance](dssec03-bp03.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP06 Automate testing and validation of security controls in pipelines](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_automate_security_controls.html) 
+  [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) 
+  [DSSEC03-BP03 Validate resource configurations for sovereignty compliance](dssec03-bp03.html) 

 **Related documents:** 
+  [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [AWS IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/) 
+  [How to prioritize IAM Access Analyzer findings](https://aws.amazon.com/blogs/security/how-to-prioritize-iam-access-analyzer-findings/) 

 **Related examples:** 
+  The [AWS IAM Access Analyzer samples repository](https://github.com/aws-samples/aws-iam-access-analyzer-samples) on GitHub provides examples showing how you can use AWS CLI and APIs to programmatically validate and preview policy documents. 
+  The [AWS Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry) is an open source repository of CloudFormation Guard rule files and managed rule sets and provides several guard rules you can use straight away. 

 **Related videos:** 
+  [AWS re:Invent 2025 - IAM Access Analyzer Deep Dive: From Configuration to Remediation (SEC340)](https://www.youtube.com/watch?v=IJVe5GxEo44) 
+  [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8) 
+  [AWS re:Inforce 2024 - Refine unused access confidently with IAM Access Analyzer (IAM202-NEW)](https://www.youtube.com/watch?v=nnr0ulOv_X8) 
+  [AWS re:Invent 2023 - Use new IAM Access Analyzer features on your journey to least privilege (SEC238)](https://www.youtube.com/watch?v=JpemUkU8INA) 
+  [AWS re:Invent 2018: The Theory and Math Behind Data Privacy and Security Assurance (SEC301)](https://www.youtube.com/watch?v=F3JmBhTQmyY) 

 **Related services:** 
+  [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 
+  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 