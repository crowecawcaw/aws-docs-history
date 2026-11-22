

# `AWSSupportRemediator-ResizeInstanceByComputeOptimizerRecommendation`

**Description**

Changes the instance type of an Amazon Elastic Compute Cloud (Amazon EC2) instance based on AWS Compute Optimizer recommendations.

The runbook selects the option with the largest monetary savings while maintaining the same platform parameters (architecture, hypervisor, network interface, virtualization type, and so on).

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Compute Optimizer [Amazon EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html).

The runbook calls the AWSSupportRemediator-ChangeInstanceType runbook to perform the instance type change. During the resize operation, the child runbook stops and starts the instance. After the automation completes, it returns the instance to its initial state (running or stopped). If `CreateAMIBeforeResize` is `true`, the child runbook creates an AMI before the change. The AMI remains in the account after the runbook completes; delete the AMI and its backing snapshots when they are no longer needed. For details about driver compatibility requirements, side effects of stopping and starting an instance, and additional prerequisites, see the AWSSupportRemediator-ChangeInstanceType runbook documentation.

The automation completes successfully without making changes in any of the following cases:
+ The Amazon EC2 instance does not exist.
+ The instance is in a terminated or shutting-down state.
+ The instance belongs to an Amazon EC2 Auto Scaling group.
+ The instance is already marked as optimized.

The automation also skips changes if a resize occurred within `MinimumDaysSinceLastChange` days or no Compute Optimizer recommendations exist without platform differences. The automation fails if the instance is running and has stop protection enabled, or if Compute Optimizer is not enrolled for the account.

The automation calls Compute Optimizer and AWS CloudTrail to evaluate recommendations and recent instance type changes. It does not move data across Regions or accounts and does not modify network access controls.

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
+ CreateAMIBeforeResize

  Type: Boolean

  Description: (Optional) Whether to create an Amazon Machine Image (AMI) as a backup before resizing the instance.

  Default: True
+ MinimumDaysSinceLastChange

  Type: String

  Description: (Optional) The minimum number of days since the last instance type change. If the instance type was modified within the specified time, the automation skips optimization. Use `0` to skip this validation.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `autoscaling:DescribeAutoScalingInstances`
+ `cloudtrail:LookupEvents`
+ `compute-optimizer:GetEC2InstanceRecommendations`
+ `compute-optimizer:GetEnrollmentStatus`
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
+ `iam:PassRole`
+ `kms:CreateGrant`
+ `kms:Decrypt`
+ `kms:DescribeKey`
+ `ssm:GetAutomationExecution`
+ `ssm:StartAutomationExecution`

**Document Steps**

1. **validateInput** - Validates the Amazon EC2 instance and retrieves the recommended instance type from Compute Optimizer. The step confirms that the instance exists, is not in a terminated or shutting-down state, and is not a member of an Amazon EC2 Auto Scaling group. It also verifies that stop protection is not enabled while running, the instance has not been resized within `MinimumDaysSinceLastChange` days, and at least one Compute Optimizer recommendation exists without platform differences.

1. **branchOnChangeRequired** - Branches on whether a change is required. If `ChangeRequired` is `false`, the automation ends successfully without making changes. Otherwise, execution continues to the next step.

1. **waitForInstanceRunningOrStopped** - Waits for the Amazon EC2 instance to reach a stable state (`running` or `stopped`) before proceeding with the instance type change.

1. **executeChangeInstanceType** - Runs the AWSSupportRemediator-ChangeInstanceType runbook to resize the Amazon EC2 instance to `validateInput.RecommendedInstanceType`. The child runbook stops the instance if it is running, changes the instance type, and returns the instance to its initial state. If `CreateAMIBeforeResize` is `true`, the child runbook creates an AMI before the change.

1. **printChangeInstanceTypeOutput** - Retrieves the execution details of the child AWSSupportRemediator-ChangeInstanceType runbook and surfaces its outputs, failure message, and status as outputs of this runbook.

**Outputs**
+ validateInput.InstanceId: The ID of the Amazon EC2 instance.
+ validateInput.InitialInstanceType: The instance type before the automation execution.
+ validateInput.RecommendedInstanceType: The recommended instance type from Compute Optimizer.
+ validateInput.ChangeRequired: Whether a change is required based on Compute Optimizer recommendations.
+ validateInput.EstimatedMonthlySavings: The estimated monthly savings from the optimization.
+ validateInput.SavingsCurrency: The currency for the estimated savings (USD or CNY).
+ validateInput.ValidationMessage: The message explaining the validation result.
+ validateInput.EvaluationFinding: The Compute Optimizer finding, such as underprovisioned, overprovisioned, or optimized.
+ printChangeInstanceTypeOutput.Summary: The summary of the instance type change execution.
+ printChangeInstanceTypeOutput.FailureMessage: The failure message if the instance type change failed.
+ printChangeInstanceTypeOutput.AutomationExecutionStatus: The status of the instance type change automation.