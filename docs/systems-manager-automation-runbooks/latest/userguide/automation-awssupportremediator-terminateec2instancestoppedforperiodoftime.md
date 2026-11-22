

# `AWSSupportRemediator-TerminateEc2InstanceStoppedForPeriodOfTime`

**Description**

Terminates an Amazon Elastic Compute Cloud (Amazon EC2) instance that has been stopped for a specified number of days.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon EC2 Instances Stopped](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#ec2-instance-stopped-for-thirty-days) or AWS Security Hub CSPM control [Stopped EC2 instances should be removed after a specified time period](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-4).

If the Amazon EC2 instance does not exist, is already terminated, is not in stopped state, or has not been stopped for the specified period, the automation completes successfully without making changes.

The automation fails if the Amazon EC2 instance has termination protection enabled. Disable termination protection before running this runbook.

If `CreateAMIBeforeTermination` is set to `true`, the automation creates an AMI and associated snapshots in the customer account before termination. On successful termination, the AMI and snapshots are retained in the customer account and might incur ongoing storage costs. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/). If the automation fails after creating the AMI, the automation deregisters the AMI and deletes the associated snapshots.

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
+ AllowedDays

  Type: String

  Description: (Conditional) The number of days the Amazon EC2 instance is in a stopped state before termination. Valid range is 0-365. If set to 0, the automation terminates any stopped Amazon EC2 instance immediately. Required if `CheckId` is not specified. Cannot be used with `CheckId`.
+ CheckId

  Type: String

  Description: (Conditional) The Security Hub CSPM control ID used to retrieve the number of allowed days in stopped state. Currently only `Hs4Ma3G120` is supported. Required if `AllowedDays` is not specified. Cannot be used with `AllowedDays`.
+ CreateAMIBeforeTermination

  Type: Boolean

  Description: (Optional) Whether to create an AMI as a backup before terminating the Amazon EC2 instance.

  Default: True

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `config:GetResourceConfigHistory`
+ `ec2:CreateImage`
+ `ec2:CreateTags`
+ `ec2:DeleteSnapshot`
+ `ec2:DeregisterImage`
+ `ec2:DescribeImages`
+ `ec2:DescribeInstanceAttribute`
+ `ec2:DescribeInstanceStatus`
+ `ec2:DescribeInstances`
+ `ec2:TerminateInstances`
+ `securityhub:BatchGetSecurityControls`
+ `securityhub:DescribeStandardsControls`
+ `ssm:DescribeAutomationExecutions`
+ `ssm:GetAutomationExecution`

**Document Steps**

1. **checkConcurrency** - Checks for concurrent runs of this runbook targeting the same Amazon EC2 instance.

1. **validateInstance** - Validates the Amazon EC2 instance state and determines whether termination is required.

1. **branchOnChangeRequired** - Branches on whether termination is required for the instance.

1. **branchOnCreateAMIBeforeTermination** - Branches on whether an AMI should be created before terminating the instance.

1. **createAmi** - Creates an AMI from the instance as a backup before termination.

1. **waitForAmiToBeAvailable** - Waits for the AMI to reach the available state before proceeding with termination.

1. **terminateInstance** - Terminates the Amazon EC2 instance.

1. **branchOnCleanupAmi** - Branches on whether AMI cleanup is needed after a failure.

1. **cleanupAmiOnFailure** - Deregisters the AMI and deletes the associated snapshots created during a failed run.

**Outputs**
+ createAmi.AmiId: The ID of the AMI created as backup before termination, if `CreateAMIBeforeTermination` is set to `true`.
+ validateInstance.ChangeRequired: Whether termination is required for the instance.
+ validateInstance.ValidationMessage: The reason when no change is required.