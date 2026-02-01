# DSSEC03-BP01 Validate policy effectiveness through automated

analysis

Manual policy validation is error-prone and does not scale well with
the complexity of modern cloud environments. Automated reasoning
tools mathematically analyze access policies to identify potential
security gaps, overprivileged access, and unintended permissions
before they are exploited.

**Desired outcome:** Access policies
grant only intended permissions, with no overprivileged access or
unintended information exposure.

**Common anti-patterns:**

- Relying solely on manual code reviews to validate complex IAM
  policies and resource-based policies.
- Using generic policy templates without validating them against
  specific organizational requirements.
- Defaulting to providing over-permissive actions in policy
  documents.
- Not validating policies against regulatory compliance
  requirements before implementation.

**Benefits of establishing this best
practice:**

- Can accelerate development cycles by catching policy issues
  early in the development process.
- Supports more confident policy changes through comprehensive
  impact analysis.
- Provides audit-ready documentation demonstrating due diligence
  in access control validation. You can track policy changes over
  time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement automated policy reasoning using
[AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") and run automated policy checks with
[AWS CloudFormation Guard](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md") to validate access policies before
deployment.

Common approaches include pre-deployment policy validation in
CI/CD pipelines, automated policy drift detection, and integration
with infrastructure as code (IaC) workflows.

### Implementation steps

1. **Enable AWS IAM Access Analyzer**: IAM Access Analyzer provides
   comprehensive policy validation through mathematical
   reasoning, enabling you to: identify resources shared with
   external entities outside their zone of trust, identify
   internal access patterns, identify
   [unused
   access](../../../IAM/latest/UserGuide/access_policies_last-accessed.md "../../../IAM/latest/UserGuide/access_policies_last-accessed.md"), validate policies against
   [policy
   grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") and
   [AWS best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"), and validate policies using
   [custom
   policy checks](../../../IAM/latest/UserGuide/access-analyzer-custom-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-custom-policy-checks.md"). The following steps outline how you
   can get started:
   - **Create an analyzer for your
     organization or account:** Enable IAM Access Analyzer in AWS console. If you are using AWS Organizations you can create a delegated administrator
     role in a member account. The delegated admin can then
     create and manage analyzers across other member
     accounts.
   - **Select supported resource
     types:** Select AWS resources to monitor.
     Resource types for external
     [access
     detection are listed here](../../../IAM/latest/UserGuide/what-is-access-analyzer.md#what-is-access-analyzer-resource-identification "../../../IAM/latest/UserGuide/what-is-access-analyzer.md#what-is-access-analyzer-resource-identification"). Resource types for
     [internal
     access detection are listed here](../../../IAM/latest/UserGuide/what-is-access-analyzer.md#what-is-access-analyzer-internal-access-analysis "../../../IAM/latest/UserGuide/what-is-access-analyzer.md#what-is-access-analyzer-internal-access-analysis").
   - **Review initial
     findings:** Examine the
     [findings
     dashboard](../../../IAM/latest/UserGuide/access-analyzer-dashboard.md "../../../IAM/latest/UserGuide/access-analyzer-dashboard.md") to identify existing external access
     and internal patterns and prioritize remediation based
     on risk level and business requirements.
   - **Integrate with CI/CD
     pipelines:**
     - Use Access Analyzer APIs to validate policies during
       development and deployment processes.
       - **AWS CLI:**
         [AWS
         accessanalyzer validate-policy](../../../cli/latest/reference/accessanalyzer/validate-policy.md "../../../cli/latest/reference/accessanalyzer/validate-policy.md")
       - **AWS API:**
         [ValidatePolicy](../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md "../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md")

     - You can also use Access Analyzer APIs to:
       - Check whether the specified access isn't allowed
         by a policy
         ([CheckAccessNotGranted](../../../access-analyzer/latest/APIReference/API_CheckAccessNotGranted.md "../../../access-analyzer/latest/APIReference/API_CheckAccessNotGranted.md"))
       - Check whether a resource policy can grant public
         access to the specified resource type
         ([CheckNoPublicAccess](../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md "../../../access-analyzer/latest/APIReference/API_CheckNoPublicAccess.md"))
       - Preview Access Analyzer findings before
         deployment
         ([Create](../../../access-analyzer/latest/APIReference/API_CreateAccessPreview.md "../../../access-analyzer/latest/APIReference/API_CreateAccessPreview.md"),
         [Get](../../../access-analyzer/latest/APIReference/API_GetAccessPreview.md "../../../access-analyzer/latest/APIReference/API_GetAccessPreview.md")
         and
         [List](../../../access-analyzer/latest/APIReference/API_ListAccessPreviewFindings.md "../../../access-analyzer/latest/APIReference/API_ListAccessPreviewFindings.md")
         preview findings).

   - **Implement custom policy
     checks:** Create organization-specific
     validation rules to make sure new policies comply with
     your security standards and regulatory requirements. You
     can find examples of reference policies and learn how to
     set up and run policy checks for new access in the
     [IAM Access Analyzer custom policy checks samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples "https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples")
     repository on GitHub.

2. **Integrate AWS CloudFormation Guard
   into CI/CD pipelines**: AWS CloudFormation Guard rules
   are another method of checking policy adherence. For
   example, you can write guard rules to:
   - Check if a policy grants wildcard access to specific
     services
   - Check if delete actions require multi-factor
     authentication (MFA) to be enabled.
   - Check if a resource-based policy (for example, an S3
     bucket policy) grants public access.
   - Check if a service control policy allows APIs calls
     beyond the allowed Regions.

3. **Validate policies locally
   (optional):** For development and testing purposes,
   you can validate and unit test CloudFormation guard rules
   locally before integrating them into your automated CI/CD
   pipeline.
   - Install CloudFormation Guard
     [on
     your desktop](../../../cfn-guard/latest/ug/setting-up.md "../../../cfn-guard/latest/ug/setting-up.md").
   - Use the cfn-guard validate command to validate your
     CloudFormation templates.

   ```

   cfn-guard validate --rules rules.guard --data template.json

   ```

   - Develop and run unit test cases on your CloudFormation
     Guard rules. While you can validate actual
     CloudFormation templates using the
     cfn-guard validate command, unit
     tests go further. They assist in testing edge-case
     scenarios. Unit tests verify if the Guard rule is
     checking for the right set of property configurations.
     For example the below test case checks if the resource
     AWS::ApiGateway::RestApi has an
     endpoint configuration property of type
     PRIVATE.

   ```

   - name: MyTest4
     input:
       Resources:
         apiGw:
           Type: AWS::ApiGateway::RestApi
           Properties:
             EndpointConfiguration:
               Types: "PRIVATE"
     expectations:
       rules:
         check_rest_api_is_private: PASS

   ```

To summarize, this proactive approach reduces data breaches by
identifying overprivileged access patterns, and validates policy
effectiveness against AWS best practices. IAM Access Analyzer
findings can also be forwarded to AWS Security Hub assisting you
to build audit-ready evidence.

## Resources

**Related best practices:**

- [SEC01-BP06
  Automate testing and validation of security controls in
  pipelines](../security-pillar/sec_securely_operate_automate_security_controls.md "../security-pillar/sec_securely_operate_automate_security_controls.md")

**Related documents:**

- [Using
  AWS Identity and Access Management Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md")
- [AWS IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing/ "https://aws.amazon.com/iam/access-analyzer/pricing/")
- [How
  to prioritize IAM Access Analyzer findings](https://aws.amazon.com/blogs/security/how-to-prioritize-iam-access-analyzer-findings/ "https://aws.amazon.com/blogs/security/how-to-prioritize-iam-access-analyzer-findings/")

**Related examples:**

- The
  [AWS IAM Access Analyzer samples repository](https://github.com/aws-samples/aws-iam-access-analyzer-samples "https://github.com/aws-samples/aws-iam-access-analyzer-samples") on GitHub
  provides examples showing how you can use AWS CLI and APIs to
  programmatically validate and preview policy documents.
- The
  [AWS Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry "https://github.com/aws-cloudformation/aws-guard-rules-registry") is an open-source repository of
  AWS CloudFormation Guard rule files and managed rule sets and
  provides several guard rules you can use straight away.

**Related videos:**

- [AWS re:Inforce 2024 - Refine unused access confidently with IAM Access Analyzer (IAM202-NEW)](https://www.youtube.com/watch?v=nnr0ulOv_X8 "https://www.youtube.com/watch?v=nnr0ulOv_X8")
- [AWS re:Invent 2023 - Use new IAM Access Analyzer features on your
  journey to least privilege (SEC238)](https://www.youtube.com/watch?v=JpemUkU8INA "https://www.youtube.com/watch?v=JpemUkU8INA")
- [AWS re:Invent 2018: The Theory and Math Behind Data Privacy and
  Security Assurance (SEC301)](https://www.youtube.com/watch?v=F3JmBhTQmyY "https://www.youtube.com/watch?v=F3JmBhTQmyY")
- [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure
  governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8 "https://www.youtube.com/watch?v=iXor74El2D8")

**Related services:**

- [AWS IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md")
- [AWS CloudFormation Guard](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md")
- [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
