

# `AWSSupportRemediator-ResizeInstanceByOneLevel`

**Description**

Downsizes or upsizes an Amazon Elastic Compute Cloud (Amazon EC2) instance by one level within the same instance type family.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor checks [Low utilization Amazon EC2 instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#low-utilization-amazon-ec2-instances) and [High CPU Utilization Amazon EC2 Instances](https://docs.aws.amazon.com/awssupport/latest/user/performance-checks.html#high-utilization-amazon-ec2-instances).

If the instance does not exist, is in terminated or shutting-down state, or the instance type changed within the specified number of days, the automation completes successfully without making changes. If the instance is in stopped state and `ResizeIfStopped` is set to false, the automation also completes successfully without making changes.

If the instance is in running state, the automation stops and restarts it during the resize operation. If `CreateAMIBeforeResize` is set to true, the automation creates an Amazon Machine Image (AMI) as a backup before changing the instance type.

The AMI and its associated Amazon Elastic Block Store (Amazon EBS) snapshot remain in the account after the automation completes and incur ongoing storage costs until you delete them. For more information about pricing, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/). If the automation fails after creating the AMI, you must remove the AMI and snapshot manually.

The automation fails without making changes in the following cases:
+ The instance is part of an Amazon EC2 Auto Scaling group or has stop protection enabled.
+ The instance has an Amazon EBS volume encrypted with an AWS KMS key that is not in enabled state.
+ The instance is already the smallest or largest instance type in its family.

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
+ Direction

  Type: String

  Description: (Required) The direction to resize the instance. Use `down` to downsize or `up` to upsize by one level within the same instance type family.
+ InstanceId

  Type: `AWS::EC2::Instance::Id`

  Description: (Required) The ID of the Amazon EC2 instance.
+ CreateAMIBeforeResize

  Type: Boolean

  Description: (Optional) Whether to create an AMI as a backup before resizing the instance.

  Default: True
+ MinimumDaysSinceLastChange

  Type: String

  Description: (Optional) The minimum number of days since the last instance type change. If the instance type changed within the specified number of days, the automation completes successfully without making changes. Use `0` to skip this validation.

  Default: 7
+ ResizeIfStopped

  Type: Boolean

  Description: (Optional) Whether to proceed with the resize if the instance is in stopped state.

  Default: False

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudtrail:LookupEvents`
+ `ec2:CreateImage`
+ `ec2:CreateTags`
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

1. **validateInput** - Validates the Amazon EC2 instance and calculates the new instance type one level up or down within the same family.

1. **branchOnChangeRequired** - Branches on whether the instance type change is required.

1. **waitForInstanceRunningOrStopped** - Waits for the instance to reach running or stopped state before proceeding.

1. **branchOnInstanceStatus** - Branches on whether the instance needs to be stopped before resizing.

1. **stopInstance** - Stops the instance before changing the instance type.

1. **branchOnAmiCreationRequired** - Branches on whether an AMI backup is required before resizing.

1. **createAmi** - Creates an AMI as a backup before changing the instance type.

1. **waitForAmiToBeAvailable** - Waits for the AMI to reach available state before proceeding.

1. **changeInstanceType** - Changes the instance type to the calculated target instance type.

1. **branchOnInitialInstanceStatus** - Branches on whether the instance needs to be restarted after resizing.

1. **startInstance** - Starts the instance after changing the instance type.

**Outputs**
+ validateInput.InitialInstanceState: The state of the instance before the automation runs.
+ validateInput.InitialInstanceType: The instance type before the automation runs.
+ validateInput.NewInstanceType: The target instance type after the automation runs.
+ validateInput.ChangeRequired: Whether the instance type change is required.
+ validateInput.ValidationMessage: A message describing the validation result.
+ createAmi.AmiId: The ID of the AMI created as a backup before the instance type is changed.