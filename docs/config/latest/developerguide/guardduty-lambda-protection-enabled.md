# guardduty-lambda-protection-enabled

Checks if Lambda Protection is enabled for an Amazon GuardDuty detector in your account. The rule is NON_COMPLIANT if the Lambda Protection feature in Amazon GuardDuty is not enabled for your account.

**Identifier:** GUARDDUTY_LAMBDA_PROTECTION_ENABLED

**Resource Types:** AWS::GuardDuty::Detector

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
