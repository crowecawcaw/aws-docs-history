# cloudformation-termination-protection-check

Checks if an AWS CloudFormation stack has termination protection enabled. This rule is NON_COMPLIANT if termination protection is not enabled on a CloudFormation stack.

**Identifier:** CLOUDFORMATION_TERMINATION_PROTECTION_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
