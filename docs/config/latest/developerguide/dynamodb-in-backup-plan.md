# dynamodb-in-backup-plan

Checks if an Amazon DynamoDB table is present in AWS Backup plans. The rule is NON_COMPLIANT if DynamoDB tables are not present in any AWS Backup plan.

**Identifier:** DYNAMODB_IN_BACKUP_PLAN

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
