# `AWSPremiumSupport-ResizeNitroInstance`

**Description**

The `AWSPremiumSupport-ResizeNitroInstance` runbook provides an automated solution for resizing Amazon Elastic Compute Cloud (Amazon EC2) instances built on the Nitro System.

To reduce the potential risk of data loss and downtime, the runbook verifies the following:

- Instance stop behavior.
- If the instance is part of an Amazon EC2 Auto Scaling group, and in `standby` mode.
- Instance state and tenancy.
- The instance type you want to change to supports the number of network interfaces currently attached to your instance.
- The processor architecture and virtualization type for both the current and target instance type are the same.
- If the instance is running, that it's passing all status checks.
- The instance type you want to change to is available in the same Availability Zone.
  If the Amazon EC2 does not pass status checks after changing the instance type, the runbook automatically rolls back to the previous instance type.

By default, this runbook will not change the instance type if it is running and instance store volumes are attached. The runbook will also not change the instance type if the instance is part of an AWS CloudFormation stack. If you want to change either of these behaviors, specify `yes` for the `AllowInstanceStoreInstances` and `AllowCloudFormationInstances` parameters.

The runbook provides two different ways to specify the instance type you want to change to:

- For simple automations targeting a single instance, specify the instance type you want to change to using the `TargetInstanceTypeFromParameter` parameter.
- For running automations at scale to change the instance type of several instances, specify the instance type using the `TargetInstanceTypeFromTagValue` parameter. For information about running automations at scale, see [Run automations at scale](../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md "../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md").
  If you don't specify a value for either parameter, the automation fails.

###### Important

Access to `AWSPremiumSupport-*` runbooks requires either an Enterprise or Business Support Subscription. For more information, see [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

**Considerations**

- We recommend backing up your instance before using this runbook.
- For information about compatibility for changing instance types, see [Compatibility for changing the instance type](../../../AWSEC2/latest/UserGuide/resize-limitations.md "../../../AWSEC2/latest/UserGuide/resize-limitations.md").
- If the automation fails and rolls back to the original instance type, see [Troubleshoot changing the instance type](../../../AWSEC2/latest/UserGuide/troubleshoot-change-instance-type.md "../../../AWSEC2/latest/UserGuide/troubleshoot-change-instance-type.md").
- Changing the instance type requires the runbook to stop your instance. When an instance is stopped, any data stored in memory or on instance store volumes is lost. Also, any automatically assigned public IPv4 addresses are released. For more information about what happens when you stop an instance, see [Stop and start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md").
- By using the `SkipInstancesWithTagKey` parameter, you can skip instances that have a specific Amazon EC2 tag key applied.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ResizeNitroInstance "https://console.aws.amazon.com/systems-manager/automation/execute/AWSPremiumSupport-ResizeNitroInstance")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- Acknowledge

Type: String

Description: (Required) Enter `yes` to acknowledge that your instance will be stopped if it's currently running.

- AllowInstanceStoreInstances

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If you specify `yes`, you allow the runbook to run on instances that have instance store volumes attached.

- AllowCloudFormationInstances

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If you specify `yes`, the runbook runs on instances that are part of an CloudFormation stack.

- DryRun

Type: String

Valid values: no | yes

Default: no

Description: (Optional) If you specify `yes`, the runbook validates resizing requirements without making changes to the instance type.

- InstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 instance whose type you want to change.

- SkipInstancesWithTagKey

Type: String

Description: (Optional) The automation skips a target instance if the tag key you specify is applied to the instance.

- SleepTime

Type: String

Default: 3

Description: (Optional) The number of seconds this runbook should sleep after completion.

- TagInstance

Type: String

Description: (Optional) Tag the instances with the key and value of your choice using the following format: `Key=ChangingType,Value=True`. This option allows you to track instances that have been targeted by this runbook. Tag keys and values are case sensitive.

- TargetInstanceTypeFromParameter

Type: String

Description: (Optional) The instance type you want to change your instance to. Leave this parameter empty if you want to use the value of the tag key provided in the `TargetInstanceTypeFromTagValue` parameter.

- TargetInstanceTypeFromTagValue

Type: String

Description: (Optional) The tag key applied to your target instances whose value contains the instance type you want to change to. If you specify a value for the `TargetInstanceTypeFromParameter` parameter, it overrides any value you specify for this parameter.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `autoscaling:DescribeAutoScalingInstances`
- `cloudformation:DescribeStackResources`
- `ssm:GetAutomationExecution`
- `ssm:DescribeAutomationExecutions`
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

1. `aws:assertAwsResourceProperty`: Ensures the Amazon EC2 instance is not tagged with the resource tag key specified in the `SkipInstancesWithTagKey` parameter. If the tag key is found applied to the instance, the step fails and the automation ends.
2. `aws:assertAwsResourceProperty`: Confirms the status of the target Amazon EC2 instance is `running`, `pending`, `stopped`, or `stopping`. Otherwise, the automation ends.
3. `aws:executeAwsApi`: Gathers properties from the Amazon EC2 instance.
4. `aws:executeAwsApi`: Gathers details about the current Amazon EC2 instance type.
5. `aws:branch`: Checks if the current instance type and the instance type specified in the `TargetInstanceTypeFromParameter` parameter are the same. If they are, the automation ends.
6. `aws:assertAwsResourceProperty`: Ensures the instance is running on the Nitro System.
7. `aws:branch`: Ensures the Amazon EC2 instance root volume type is an Amazon Elastic Block Store (Amazon EBS) volume.
8. `aws:assertAwsResourceProperty`: Confirms the instance shutdown behavior is `stop` and not `terminate`.
9. `aws:branch`: Ensures the Amazon EC2 instance is not a Spot instance.
10. `aws:branch`: Ensures the Amazon EC2 instance tenancy is default and not dedicated host, or dedicated instance.
11. `aws:executeScript`: Confirms there is only one automation of this runbook targeting the current instance ID. If another automation is already in progress targeting the same instance, the automation returns an error and ends.
12. `aws:branch`: Branches the automation based on the state of the Amazon EC2 instance.
    1. If `stopped` or `stopping`, the automation runs `aws:waitForAwsResourceProperty` until the Amazon EC2 instance is fully stopped.
    2. If `running` or `pending`, the automation runs `aws:waitForAwsResourceProperty` until the Amazon EC2 instance passes status checks.

13. `aws:assertAwsResourceProperty`: Confirms that the Amazon EC2 instance is not part of an Auto Scaling group by calling the `DescribeAutoScalingInstances` API operation. If the instance is part of an Auto Scaling group, ensures the Amazon EC2 instance is in `standby` mode.
14. `aws:branch`: Branches the automation depending on whether you want the automation to check if the Amazon EC2 instance is part of an CloudFormation stack:
    1. `aws:executeScript` Ensures the Amazon EC2 instance is not part of an CloudFormation stack by calling the `DescribeStackResources` API operation.

15. `aws:executeAwsApi`: Returns a list of instance types with the same processor architecture type, virtulization type, and that supports the number of network interfaces currently attached to the target instance.
16. `aws:executeAwsApi`: Gets the target instance type value from the tag key specified in the `TargetInstanceTypeFromTagValue` parameter.
17. `aws:executeScript`: Confirms that the current and target instances types are compatible. Ensures that the target instance type is available in the same subnet. Verifies the principal who started the runbook has permissions to change the instance type, and stop and start the instance if it was running.
18. `aws:branch`: Branches the automation based on whether the `DryRun` parameter value is set to `yes`. If `yes`, the automation ends.
19. `aws:branch`: Checks if the original and the target instance type are the same. If they're the same, the automation ends.
20. `aws:executeAwsApi`: Gets the current instance state.
21. `aws:changeInstanceState`: Stops the Amazon EC2 instance.
22. `aws:changeInstanceState`: Forces the instance to stop if it's stuck in the `stopping` state.
23. `aws:executeAwsApi`: Changes the instance type to the target instance type.
24. `aws:sleep`: Waits 3 seconds after changing the instance type for eventual consistency.
25. `aws:branch`: Branches the automation based on the previous instance state. If it was `running`, the instance is started.
    1. `aws:changeInstanceState`: Starts the Amazon EC2 instance if it was running before changing the instance type.
    2. `aws:waitForAwsResourceProperty`: Waits for the Amazon EC2 instance to pass status checks. If the instance doesn't pass status checks, the instance is changed back to its original instance type.
       1. `aws:changeInstanceState`: Stops the Amazon EC2 instance before changing it to its original instance type.
       2. `aws:changeInstanceState`: Forces the Amazon EC2 instance to stop before changing it to its original instance type in case it gets stuck in a stopping state.
       3. `aws:executeAwsApi`: Changes the Amazon EC2 instance to its original type.
       4. `aws:sleep`: Waits 3 seconds after changing the instance type for eventual consistency.
       5. `aws:changeInstanceState`: Starts the Amazon EC2 instance if it was running before changing the instance type.
       6. `aws:waitForAwsResourceProperty`: Waits for the Amazon EC2 instance to pass status checks.

26. `aws:sleep`: Waits before ending the runbook.
