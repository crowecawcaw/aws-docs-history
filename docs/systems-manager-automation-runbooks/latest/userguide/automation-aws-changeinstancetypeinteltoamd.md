# `AWSPremiumSupport-ChangeInstanceTypeIntelToAMD`

**Description**

The`AWSPremiumSupport-ChangeInstanceTypeIntelToAMD` runbook automates migrations from Intel powered Amazon Elastic Compute Cloud (Amazon EC2) instances to the equivalent AMD powered instance types. This runbook supports general purpose (M), burstable general purpose (T), compute optimized (C), and memory optimized (R) instances built on the Nitro system. This runbook can be used on instances that aren't managed by Systems Manager.

To reduce the potential risk of data loss and downtime, the runbook checks the instance's stop behavior, whether the instance is in an Amazon EC2 Auto Scaling group, the health of the instance, and that the equivalent AMD powered instance type is available in the same Availability Zone. By default, this runbook will not change the instance type if instance store volumes are attached, or if the instance is part of an AWS CloudFormation stack. If you want to change this behavior, specify `yes` for either of the `AllowInstanceStoreInstances` and `AllowCloudFormationInstances` parameters.

###### Important

Access to `AWSPremiumSupport-*` runbooks requires either an Enterprise or Business Support Subscription. For more information, see [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

**Considerations**

- We recommend backing up your instance before using this runbook.
- Changing the instance type requires the runbook to stop your instance. When an instance is stopped, any data stored in the RAM or the instance store volumes is lost, and the automatic public IPv4 address is released. For more information, see [Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md").
- If you don't specify a value for the `TargetInstanceType` parameter, the runbook attempts to identify the equivalent AMD instance in terms of virtual CPUs and memory within the same instance family. The runbook ends if it is not able to identify an equivalent AMD instance type.
- By using the `DryRun` option, you can capture the equivalent AMD instance type, and validate requirements without actually changing the instance type.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ChangeInstanceTypeIntelToAMD "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ChangeInstanceTypeIntelToAMD")

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

- Acknowledge

Type: String

Description: (Required) Enter `yes` to acknowledge that your target instance will be stopped if it's running.

- InstanceId

Type: String

Description: (Required) The ID of Amazon EC2 instance whose type you want to change.

- TargetInstanceType

Type: String

Default: automatic

Description: (Optional) The AMD instance type you want to change your instance to. The default `automatic` value uses the equivalent instance type in terms of virtual CPUs and memory. For example, an m5.large would be changed to m5a.large.

- AllowInstanceStoreInstances

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If you specify `yes`, the runbook runs on instances that have instance store volumes attached.

- AllowCloudFormationInstances

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If set to `yes`, the runbook runs on instances that are part of a AWS CloudFormation stack.

- AllowCrossGeneration

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If set to `yes`, the runbook attempts to find the newest equivalent AMD instance type within the same instance family.

- DryRun

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If set to `yes`, the runbook returns the equivalent AMD instance type and validates migration requirements without making changes to the instance type.

- SleepWait

Type: String

Default: PT3S

Description: (Optional) The time the runbook should wait before starting a new automation. The value you provide for this parameter must match the ISO 8601 standard. For more information about creating ISO 8601 strings, see [Formatting date and time strings for Systems Manager](../../../systems-manager/latest/userguide/systems-manager-datetime-strings.md#systems-manager-datetime-strings-format "../../../systems-manager/latest/userguide/systems-manager-datetime-strings.md#systems-manager-datetime-strings-format").
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeAutomationExecutions`
- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `ec2:GetInstanceTypesFromInstanceRequirements`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeInstanceTypeOfferings`
- `ec2:DescribeInstanceTypes`
- `ec2:DescribeTags`
- `ec2:ModifyInstanceAttribute`
- `ec2:StartInstances`
- `ec2:StopInstances`

**Document Steps**

1. `aws:assertAwsResourceProperty`: Confirms the status of the target Amazon EC2 instance is `running`, `pending`, `stopped`, or `stopping`. Otherwise, the automation ends.
2. `aws:executeAwsApi`: Gathers properties from the target Amazon EC2 instance.
3. `aws:branch`: Branches the automation based on the state of the Amazon EC2 instance.
   1. If `stopped` or `stopping`, the automation runs `aws:waitForAwsResourceProperty` until the Amazon EC2 instance is fully stopped.
   2. If `running` or `pending`, the automation runs `aws:waitForAwsResourceProperty` until the Amazon EC2 instance passes status checks.

4. `aws:assertAwsResourceProperty`: Confirms the Amazon EC2 instance is not part of an Auto Scaling group by checking if the `aws:autoscaling:groupName` tag is applied.
5. `aws:executeAwsApi`: Gathers the current instance type properties to find the equivalent AMD instance type.
6. `aws:assertAwsResourceProperty`: Confirms a AWS Marketplace product code is not associated with the Amazon EC2 instance. Some products are not available on all instance types.
7. `aws:branch`: Branches the automation depending on whether you want the automation to check if the Amazon EC2 instance is part of a AWS CloudFormation stack
   1. If the `aws:cloudformation:stack-name` tag is applied to the instance, the automation runs `aws:assertAwsResourceProperty` to confirm the instance is not part of a AWS CloudFormation stack.

8. `aws:branch`: Branches the automation based on whether the instance root volume type is Amazon Elastic Block Store (Amazon EBS).
9. `aws:assertAwsResourceProperty`: Confirms the instance shutdown behavior is `stop` and not `terminate`.
10. `aws:executeScript`: Confirms there is only one automation of this runbook targeting the current instance. If another automation is already in progress targeting the same instance, it returns an error and ends.
11. `aws:executeAwsApi`: Returns a list of the AMD instance types with same amount of memory and vCPUs.
12. `aws:executeScript`: Checks if the current instance type is supported and returns its equivalent AMD instance type. If there is no equivalent, the automation ends.
13. `aws:executeScript`: Confirms the AMD instance type is available in the same Availability Zone, and verifies the provided IAM permissions.
14. `aws:branch`: Branches the automation based on whether the `DryRun` parameter value is `yes`.
15. `aws:branch`: Checks if the original and the target instance type are the same. If they're the same, the automation ends.
16. `aws:executeAwsApi`: Gets the current instance state.
17. `aws:changeInstanceState`: Stops the Amazon EC2 instance.
18. `aws:changeInstanceState`: Forces the instance to stop if it's stuck in stopping state.
19. `aws:executeAwsApi`: Changes the instance type to the target AMD instance type.
20. `aws:sleep`: Waits 3 seconds after changing the instance type for eventual consistency.
21. `aws:branch`: Branches the automation based on the previous instance state. If it was `running`, the instance is started.
    1. `aws:changeInstanceState`: Starts the Amazon EC2 instance if it was running before changing the instance type.
    2. `aws:waitForAwsResourceProperty`: Waits for the Amazon EC2 instance to pass status checks. If the instance doesn't pass status checks, the instance is changed back to its original instance type.
       1. `aws:changeInstanceState`: Stops the Amazon EC2 instance before changing it to its original instance type.
       2. `aws:changeInstanceState`: Forces the Amazon EC2 instance to stop before changing it to its original instance type in case it gets stuck in a stopping state.
       3. `aws:executeAwsApi`: Changes Amazon EC2 instance to its original type.
       4. `aws:sleep`: Waits 3 seconds after changing instance type for eventual consistency.
       5. `aws:changeInstanceState`: Starts the Amazon EC2 instance if it was running before changing the instance type.
       6. `aws:waitForAwsResourceProperty`: Waits for the Amazon EC2 instance to pass status checks.

22. `aws:sleep`: Waits before ending the runbook.
