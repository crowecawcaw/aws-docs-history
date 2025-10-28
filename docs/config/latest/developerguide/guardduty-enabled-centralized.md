# guardduty-enabled-centralized

Checks if Amazon GuardDuty is enabled in your AWS account and AWS Region. If you provide an AWS account for centralization, the rule evaluates the GuardDuty results in the centralized account. The rule is COMPLIANT when GuardDuty is enabled.

**Identifier:** GUARDDUTY_ENABLED_CENTRALIZED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), AWS Secret - West, Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

CentralMonitoringAccount (Optional)
Type: String

Comma separated list of AWS Accounts (12-digit) where Amazon GuardDuty results are allowed to be centralized.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
