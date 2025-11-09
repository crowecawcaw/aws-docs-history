# lambda-dlq-check

Checks if a Lambda function is configured with a dead-letter queue. The rule is NON_COMPLIANT if the Lambda function is not configured with a dead-letter queue.

**Identifier:** LAMBDA_DLQ_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

dlqArns (Optional)
Type: String

Comma-separated list of Amazon SQS and Amazon SNS ARNs that must be configured as the Lambda function dead-letter queue target.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
