# dynamodb-autoscaling-enabled

Checks if Amazon DynamoDB tables or global secondary indexes can process read/write capacity using on-demand mode or provisioned mode with auto scaling enabled. The rule is NON_COMPLIANT if either mode is used without auto scaling enabled

**Identifier:** DYNAMODB_AUTOSCALING_ENABLED

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

minProvisionedReadCapacity (Optional)
Type: int

The minimum number of units that should be provisioned with read capacity in the Auto Scaling group.

maxProvisionedReadCapacity (Optional)
Type: int

The maximum number of units that should be provisioned with read capacity in the Auto Scaling group.

targetReadUtilization (Optional)
Type: double

The target utilization percentage for read capacity. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity.

minProvisionedWriteCapacity (Optional)
Type: int

The minimum number of units that should be provisioned with write capacity in the Auto Scaling group.

maxProvisionedWriteCapacity (Optional)
Type: int

The maximum number of units that should be provisioned with write capacity in the Auto Scaling group.

targetWriteUtilization (Optional)
Type: double

The target utilization percentage for write capacity. Target utilization is expressed in terms of the ratio of consumed capacity to provisioned capacity.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
