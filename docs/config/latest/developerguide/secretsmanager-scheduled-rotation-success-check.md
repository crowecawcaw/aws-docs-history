# secretsmanager-scheduled-rotation-success-check

Checks if AWS Secrets Manager secrets rotated successfully according to the rotation schedule. Secrets Manager calculates the date the rotation should happen. The rule is NON_COMPLIANT if the date passes and the secret isn't rotated.

###### Note

**Recording delays**

Evaluation results for this rule can be delayed for up to 2 days from a missed rotation date.
For more immediate monitoring, see [Monitor
AWS Secrets Manager with Amazon CloudWatch](../../../secretsmanager/latest/userguide/monitoring-cloudwatch.md "../../../secretsmanager/latest/userguide/monitoring-cloudwatch.md") in the _Secrets Manager User Guide_.

**Secrets without rotation**

The rule returns `NOT_APPLICABLE` for secrets that aren't configured for rotation.

**Identifier:** SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
