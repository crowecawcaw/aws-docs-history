# `AWS-EnableDynamoDbAutoscaling`

**Description**

The `AWS-EnableDynamoDbAutoscaling` runbook enables Application Auto Scaling for the provisioned capacity Amazon DynamoDB table you specify. Application Auto Scaling dynamically adjusts provisioned throughput capacity in response to traffic patterns. For more information, see
[Managing throughput capacity automatically with DynamoDB auto scaling](../../../amazondynamodb/latest/developerguide/AutoScaling.md "../../../amazondynamodb/latest/developerguide/AutoScaling.md") in the _Amazon DynamoDB Developer Guide_.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- TableName

Type: String

Description: (Required) The name of the DynamoDB table you want to enable Application Auto Scaling on.

- MinReadCapacity

Type: Integer

Description: (Required) The minimum number of provisioned throughput read capacity units for the DynamoDB table.

- MaxReadCapacity

Type: Integer

Description: (Required) The maximum number of provisioned throughput read capacity units for the DynamoDB table.

- TargetReadCapacityUtilization

Type: Integer

Description: (Required) The desired target read capacity utilization. Target utilization is the percentage of consumed provisioned throughput at a point in time. You can set the auto scaling target utilization values between 20 and 90 percent.

- ReadScaleOutCooldown

Type: Integer

Description: (Required) The amount of time in seconds to wait for a previous read capacity scale-out activity to take effect.

- ReadScaleInCooldown

Type: Integer

Description: (Required) The amount of time in seconds after a read capacity scale-in activity completes before another scale-in activity can start.

- MinWriteCapacity

Type: Integer

Description: (Required) The minimum number of provisioned throughput write units for the DynamoDB table.

- MaxWriteCapacity

Type: Integer

Description: (Required) The maximum number of provisioned throughput write units for the DynamoDB table.

- TargetWriteCapacityUtilization

Type: Integer

Description: (Required) The desired target write capacity utilization. Target utilization is the percentage of consumed provisioned throughput at a point in time. You can set the auto scaling target utilization values between 20 and 90 percent.

- WriteScaleOutCooldown

Type: Integer

Description: (Required) The amount of time in seconds to wait for a previous write capacity scale-out activity to take effect.

- WriteScaleInCooldown

Type: Integer

Description: (Required) The amount of time in seconds after a write capacity scale-in activity completes before another scale-in activity can start.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `application-autoscaling:DescribeScalableTargets`
- `application-autoscaling:DescribeScalingPolicies`
- `application-autoscaling:PutScalingPolicy`
- `application-autoscaling:RegisterScalableTarget`

- RegisterAppAutoscalingTargetWrite (`aws:executeAwsApi`) - Configures Application Auto Scaling on the DynamoDB table you specify.
- RegisterAppAutoscalingTargetWriteDelay (`aws:sleep`) - Sleeps to avoid API throttling.
- PutScalingPolicyWrite (`aws:executeAwsApi`) - Configures the target write capacity utilization for the DynamoDB table.
- PutScalingPolicyWriteDelay (`aws:sleep`) - Sleeps to avoid API throttling.
- RegisterAppAutoscalingTargetRead (`aws:executeAwsApi`) - Configures minimum and maximum read capacity units for the DynamoDB table.
- RegisterAppAutoscalingTargetReadDelay (`aws:sleep`) - Sleeps to avoid API throttling.
- PutScalingPolicyRead (`aws:executeAwsApi`) - Configures the target read capacity utilization for the DynamoDB table.
- VerifyDynamoDbAutoscalingEnabled (`aws:executeScript`) - Verifies Application Auto Scaling is enabled for the DynamoDB table according to the values you specify.

**Outputs**

- RegisterAppAutoscalingTargetWrite.Response
- PutScalingPolicyWrite.Response
- RegisterAppAutoscalingTargetRead.Response
- PutScalingPolicyRead.Response
- VerifyDynamoDbAutoscalingEnabled.DynamoDbAutoscalingEnabledResponse
