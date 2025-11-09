# secretsmanager-secret-unused

Checks if AWS Secrets Manager secrets have been accessed within a specified number of days. The rule is NON_COMPLIANT if a secret has not been accessed in 'unusedForDays' number of days. The default value is 90 days.

**Context**: It is recommended to routinely delete unused secrets.
Unused secrets can be misused by former users who no longer need access to these secrets. Additionally, as more users gain access to a secret,
it becomes increasingly possible that someone has misused a secret or has granted access to an unauthorized entity.
Deleting unused secrets helps revoke secret access from users who no longer need it, and can reduce your cost of using AWS Secrets Manager.

**Identifier:** SECRETSMANAGER_SECRET_UNUSED

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

unusedForDays (Optional)
Type: int

The number of days in which a secret can remain unused. The default value is 90 days.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
