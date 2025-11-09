# secretsmanager-secret-periodic-rotation

Checks if AWS Secrets Manager secrets have been rotated in the past specified number of days. The rule is NON_COMPLIANT if a secret has not been rotated for more than maxDaysSinceRotation number of days. The default value is 90 days.

**Identifier:** SECRETSMANAGER_SECRET_PERIODIC_ROTATION

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

maxDaysSinceRotation (Optional)
Type: int

Maximum number of days in which a secret can remain unchanged. The default value is 90 days.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
