

# `AWSSupportRemediator-ChangeInstanceType`

**Description**

Resizes an Amazon Elastic Compute Cloud (Amazon EC2) instance by changing its instance type.

This automation remediates findings identified by AWS Well-Architected Agent.

If the Amazon EC2 instance does not exist or is in `terminated` state, the automation completes successfully without making changes. The automation also completes without changes if the instance already runs the requested instance type.

The automation fails without making changes in any of the following cases:
+ The instance belongs to an Amazon EC2 Auto Scaling group.
+ The instance has stop protection on.
+ The instance has encrypted Amazon Elastic Block Store (Amazon EBS) volumes whose AWS Key Management Service (AWS KMS) key is not in `Enabled` state.
+ The requested instance type has a different hypervisor than the current instance type.
+ The requested instance type requires Elastic Network Adapter (ENA) but the current Xen-family instance type does not support ENA.
+ The requested instance type is not a valid Amazon EC2 instance type.

This automation does not verify that the guest operating system has the required drivers for the new instance type. Resizing a Windows instance with an outdated or missing ENA driver to a newer instance type can cause complete network loss after the resize. Resizing a Linux instance to a Nitro-based instance type without the ENA and NVMe kernel drivers can leave the instance unreachable or unable to boot. Before resizing, confirm that the instance has a current ENA driver. For Windows, AWS recommends the latest ENA driver; see [Track ENA Windows driver version releases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-driver-releases-windows.html). For Linux, confirm the ENA and NVMe kernel modules are present and built into the initramfs. Without these modules, the instance cannot reach the network or boot from its root volume. For Windows instances, you can upgrade the driver with the `AWSSupport-UpgradeWindowsAWSDrivers` runbook before running this automation.

The automation stops the instance and modifies the `InstanceType` attribute. It enables Amazon EBS optimization and ENA on the new instance type when appropriate. After starting the instance, the automation returns it to its initial state. When `CreateAMIBeforeResize` is `true` (the default), the automation creates an Amazon Machine Image (AMI) and the associated Amazon EBS snapshots. The automation creates the AMI from the instance in its stopped state without rebooting it (`NoReboot=true`), so the AMI captures a consistent snapshot of the file system. The AMI and snapshots remain in the customer account. You are responsible for removing them when you no longer need them.

Because this automation stops and starts the instance, you should be aware of the following side effects:
+ Applications running on the instance are unavailable while the instance is stopped.
+ Stopping and starting the instance releases its public IPv4 address (unless an Elastic IP address is associated) and assigns a new one.
+ Stopping the instance permanently deletes data on instance store (ephemeral) volumes.

To roll back the instance type change, launch a new instance from the AMI that this automation creates, or modify the instance type back to the original type that `validateInstance.InitialInstanceType` stores.

The AMI and Amazon EBS snapshots that this automation creates incur Amazon EBS snapshot storage charges. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).

This automation does not implement an internal concurrency guard. You are responsible for ensuring that the runbook does not run concurrently against the same Amazon EC2 instance. Concurrent `StopInstances`, `ModifyInstanceAttribute`, and `StartInstances` calls can leave the instance in an unexpected state.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ InstanceId

  Type: `AWS::EC2::Instance::Id`

  Description: (Required) The ID of the Amazon EC2 instance.
+ InstanceType

  Type: String

  Description: (Required) The target Amazon EC2 instance type.
+ CreateAMIBeforeResize

  Type: Boolean

  Description: (Optional) Whether to create an AMI as a backup before resizing the instance.

  Default: True

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `autoscaling:DescribeAutoScalingInstances`
+ `ec2:CreateImage`
+ `ec2:DescribeImages`
+ `ec2:DescribeInstanceAttribute`
+ `ec2:DescribeInstanceStatus`
+ `ec2:DescribeInstanceTypes`
+ `ec2:DescribeInstances`
+ `ec2:DescribeVolumes`
+ `ec2:ModifyInstanceAttribute`
+ `ec2:StartInstances`
+ `ec2:StopInstances`
+ `kms:CreateGrant`
+ `kms:Decrypt`
+ `kms:DescribeKey`

**Document Steps**

1. **validateInstance** - Validates the Amazon EC2 instance and the requested instance type. Confirms the instance exists, does not belong to an Amazon EC2 Auto Scaling group, and does not have stop protection on. Confirms that any encrypted Amazon EBS volumes use an AWS KMS key in `Enabled` state. Confirms the requested instance type is valid and shares the same hypervisor family as the current type. Determines whether to enable Amazon EBS optimization and ENA on the new instance type. Verifies the automation can perform each mutating action via DryRun probes before any change runs.

1. **branchOnChangeRequired** - Branches on whether the automation needs to change the instance type. Ends the automation successfully when the instance already runs the requested type.

1. **branchOnInstanceState** - Branches on whether the Amazon EC2 instance is in `running` state, to determine whether to stop the instance before modifying the instance type.

1. **stopInstance** - Stops the Amazon EC2 instance so the automation can modify the instance type.

1. **branchOnCreateAMIBeforeResize** - Branches on whether `CreateAMIBeforeResize` is `true`, to determine whether to create an AMI backup before modifying the instance type.

1. **createAmi** - Creates an AMI from the Amazon EC2 instance as a backup before the instance type change. The AMI and its Amazon EBS snapshots remain in the customer account.

1. **changeInstanceType** - Modifies the Amazon EC2 instance to the requested instance type. Enables Amazon EBS optimization and ENA support on the new instance type when appropriate.

1. **startInstance** - Starts the Amazon EC2 instance so that the new instance type takes effect.

1. **ensureInstanceInitialState** - Returns the Amazon EC2 instance to the initial state (for example, `stopped`) that the automation captured at the start.

1. **describeInstanceFinalInfo** - Retrieves the final Amazon EC2 instance type and state after all modifications.

**Outputs**
+ `validateInstance.InstanceInitialState`: The Amazon EC2 instance state before the automation runs.
+ `validateInstance.InitialInstanceType`: The instance type before the automation runs.
+ `validateInstance.InitialInstanceEnaSupport`: Whether the instance has ENA enabled before the automation runs.
+ `validateInstance.InitialInstanceEbsOptimized`: Whether the instance has Amazon EBS optimization enabled before the automation runs.
+ `validateInstance.ChangeRequired`: Whether the automation needs to change the instance type. `false` when the instance does not exist, is in `terminated` state, or already runs the requested type.
+ `validateInstance.ValidationMessage`: A message describing the result of the validation step.
+ `describeInstanceFinalInfo.FinalInstanceType`: The Amazon EC2 instance type after the automation runs.
+ `describeInstanceFinalInfo.InstanceFinalState`: The Amazon EC2 instance state after the automation runs.
+ `createAmi.ImageId`: The ID of the AMI that the runbook creates before the instance type change, when `CreateAMIBeforeResize` is `true`.