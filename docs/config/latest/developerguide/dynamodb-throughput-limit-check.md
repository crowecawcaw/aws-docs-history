# dynamodb-throughput-limit-check

Checks if provisioned DynamoDB throughput is approaching the maximum limit for your account. By default, the rule checks if provisioned throughput exceeds a threshold of 80 percent of your account limits.

**Identifier:** DYNAMODB_THROUGHPUT_LIMIT_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

accountRCUThresholdPercentage (Optional)
Type: int
Default: 80

Percentage of provisioned read capacity units for your account. When this value is reached, the rule is marked as noncompliant.

accountWCUThresholdPercentage (Optional)
Type: int
Default: 80

Percentage of provisioned write capacity units for your account. When this value is reached, the rule is marked as noncompliant.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
