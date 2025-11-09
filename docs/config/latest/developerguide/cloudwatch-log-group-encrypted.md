# cloudwatch-log-group-encrypted

Checks if Amazon CloudWatch Log Groups are encrypted with any AWS KMS key or a specified AWS KMS key Id. The rule is NON_COMPLIANT if a CloudWatch Log Group is not encrypted with a KMS key or is encrypted with a KMS key not supplied in the rule parameter.

**Identifier:** CLOUDWATCH_LOG_GROUP_ENCRYPTED

**Resource Types:** AWS::Logs::LogGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS Secret - West Region

**Parameters:**

KmsKeyId (Optional)
Type: String

Amazon Resource Name (ARN) of the ID for the KMS key that is used to encrypt the log group.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
