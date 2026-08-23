# dynamodb-table-deletion-protection-enabled

Checks if an Amazon DynamoDB table have deletion protection set to enabled. The rule is NON\_COMPLIANT if the table have deletion protection set to disabled.

**Identifier:** DYNAMODB\_TABLE\_DELETION\_PROTECTION\_ENABLED

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
