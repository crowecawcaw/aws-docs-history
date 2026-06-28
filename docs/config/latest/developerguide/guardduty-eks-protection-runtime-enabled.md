# guardduty-eks-protection-runtime-enabled

Checks if Amazon EKS Runtime Monitoring with automated agent management is enabled for GuardDuty detector in your account. The rule is NON\_COMPLIANT if EKS Runtime Monitoring with automated agent management in GuardDuty is not enabled for your account.

**Identifier:** GUARDDUTY\_EKS\_PROTECTION\_RUNTIME\_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
