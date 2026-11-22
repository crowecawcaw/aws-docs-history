

# `AWSSupportRemediator-TerminateEc2Instance`

**Description**

Terminates an Amazon Elastic Compute Cloud (Amazon EC2) instance that is underutilized based on the AWS Trusted Advisor Low Utilization Amazon EC2 Instances check criteria.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Low Utilization Amazon EC2 Instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#low-utilization-amazon-ec2-instances).

The automation completes successfully without making changes in several cases. These include when the instance does not exist, is already terminated, or is in a stopped state (already cost-remediated). The same applies when the instance is in a transient state (`pending`, `stopping`) or has fewer than 14 days of Amazon CloudWatch metric history. The automation also takes no action when the instance does not meet the Trusted Advisor low-utilization criteria on enough days in the evaluation window.

The automation fails if the Amazon EC2 instance has termination protection enabled or is part of an Amazon EC2 Auto Scaling group. The automation also fails if it cannot retrieve Amazon CloudWatch metric data. Disable termination protection, detach the instance from the Auto Scaling group, or make sure that CloudWatch metrics are available before running this runbook.

Before termination, the automation re-verifies the Trusted Advisor alert criteria from Amazon CloudWatch metrics. The automation terminates the instance only when two thresholds hold: daily average CPU at or below 10 percent, and daily network I/O at or below 5 MB. The instance must meet both thresholds on at least 4 of the previous 14 days.

**Data loss risk**  
Terminating the instance is irreversible. It deletes any attached Amazon Elastic Block Store (Amazon EBS) volumes that have `DeleteOnTermination` set to `true`. The automation also releases the instance private IP addresses, disassociates any Elastic IP addresses from the instance, and deletes elastic network interfaces created with the instance. Elastic IP allocations remain in the account.

Terminating a running instance causes an availability interruption for any workload on the instance. Make sure the Trusted Advisor finding for the instance reflects the current workload before running this automation in auto-remediation mode.

If `CreateAMIBeforeTermination` is set to `true`, the automation creates an AMI and associated snapshots before termination. After a successful termination, the AMI and snapshots remain in your account and might incur ongoing storage costs. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/). Use the AMI to relaunch the instance if needed.

The automation does not restore original settings, such as the private IP address, Elastic IP association, or elastic network interfaces. If the automation fails after creating the AMI, it deregisters the AMI and deletes the associated snapshots.

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

  Description: (Required) The ID of the Amazon EC2 instance to terminate.
+ CreateAMIBeforeTermination

  Type: Boolean

  Description: (Optional) Whether to create an AMI as a backup before terminating the Amazon EC2 instance.

  Default: True

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `autoscaling:DescribeAutoScalingInstances`
+ `cloudwatch:GetMetricStatistics`
+ `ec2:CreateImage`
+ `ec2:CreateTags`
+ `ec2:DeleteSnapshot`
+ `ec2:DeregisterImage`
+ `ec2:DescribeImages`
+ `ec2:DescribeInstanceAttribute`
+ `ec2:DescribeInstanceStatus`
+ `ec2:DescribeInstances`
+ `ec2:TerminateInstances`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:GetAutomationExecution`

**Document Steps**

1. **checkConcurrency** - Checks for concurrent runs of this runbook targeting the same Amazon EC2 instance.

1. **validateInstance** - Validates the Amazon EC2 instance state, termination protection, Auto Scaling group membership, and Trusted Advisor low-utilization criteria, and determines whether termination is required.

1. **branchOnChangeRequired** - Branches on whether termination is required for the instance.

1. **branchOnCreateAMIBeforeTermination** - Branches on whether to create an AMI before terminating the instance.

1. **createAmi** - Creates an AMI from the instance as a backup before termination.

1. **waitForAmiToBeAvailable** - Waits for the AMI to reach the available state before proceeding with termination.

1. **terminateInstance** - Terminates the Amazon EC2 instance.

1. **branchOnCleanupAmi** - Branches on whether AMI cleanup is needed after a failure.

1. **cleanupAmiOnFailure** - Deregisters the AMI and deletes the associated snapshots created during a failed run.

**Outputs**
+ createAmi.AmiId: The ID of the AMI created as backup before termination, if `CreateAMIBeforeTermination` is set to `true`.
+ validateInstance.ChangeRequired: Whether termination is required for the instance.
+ validateInstance.ValidationMessage: The reason when no change is required.