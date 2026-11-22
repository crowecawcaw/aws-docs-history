

# `AWSSupportRemediator-StopEc2Instance`

**Description**

Stops an Amazon Elastic Compute Cloud (Amazon EC2) instance after performing validation checks.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Low Utilization Amazon EC2 Instances](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#low-utilization-amazon-ec2-instances) and AWS Compute Optimizer [Idle Amazon EC2 instance](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).

If the instance does not exist, is already stopped, or is in a non-running state, the automation completes successfully without making changes.

The automation fails in the following cases:
+ The instance belongs to an Amazon EC2 Auto Scaling group.
+ The instance uses instance store volumes without `ForceStopWithInstanceStore` set to `true`.
+ The instance has Amazon Elastic Block Store (Amazon EBS) volumes encrypted with an AWS Key Management Service (AWS KMS) key that is pending deletion or does not exist.

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
+ ForceStopWithInstanceStore

  Type: Boolean

  Description: (Optional) Whether to force stop instances that use instance store volumes. Data on instance store volumes is lost when the instance is stopped.

  Default: False

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeInstanceStatus`
+ `ec2:DescribeInstances`
+ `ec2:DescribeVolumes`
+ `ec2:StopInstances`
+ `kms:DescribeKey`

**Document Steps**

1. **validateInstance** - Validates that the Amazon EC2 instance exists and is in a running state. Checks that the instance does not belong to an Amazon EC2 Auto Scaling group. Verifies that `ForceStopWithInstanceStore` is set to true if instance store volumes are present. Validates AWS KMS keys for encrypted Amazon EBS volumes.

1. **branchOnChangeRequired** - Branches on whether the instance needs to be stopped.

1. **changeInstanceState** - Stops the Amazon EC2 instance.

**Outputs**
+ validateInstance.InstanceInitialState: The state of the instance before the automation runs.
+ validateInstance.ChangeRequired: Whether the instance needs to be stopped.
+ validateInstance.ValidationMessage: A message describing the validation result.