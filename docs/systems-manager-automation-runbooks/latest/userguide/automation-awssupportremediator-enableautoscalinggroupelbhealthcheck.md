

# `AWSSupportRemediator-EnableAutoScalingGroupElbHealthCheck`

**Description**

Enables Elastic Load Balancing (ELB) health checks for an Amazon EC2 Auto Scaling group by calling the Amazon EC2 Auto Scaling `UpdateAutoScalingGroup` API.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Auto Scaling groups associated with a load balancer should use ELB health checks](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-1).

If the Amazon EC2 Auto Scaling group does not exist, has no attached load balancer, or already includes `ELB` in its health check types, the automation completes successfully without making changes.

The Amazon EC2 Auto Scaling `HealthCheckType` field is a comma-separated list of one or more health check types: `EC2`, `EBS`, `ELB`, and `VPC_LATTICE`. Because `EC2` is the default and cannot be disabled, it does not appear in the value alongside other types.

This automation is additive. If the group already has other health check types configured (for example, `EBS`), the automation appends `ELB` to those existing types (resulting in `EBS,ELB`). It does not replace or remove other health check types.

Turning on `ELB` health checks can cause Amazon EC2 Auto Scaling to replace an instance if any attached load balancer reports it as unhealthy.

To revert the change after the automation runs, update the Amazon EC2 Auto Scaling group's `HealthCheckType` to the value in the `validateInput.PreviousHealthCheckType` output. For example, `EC2` or `EBS`. The `PreviousHealthCheckType` output reflects the group's health check type at the moment this automation observes it. If multiple executions target the same group, only the first execution's output captures the original value.

Instance replacement might incur additional costs from new instance launches and data transfer. For more information about pricing, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

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
+ AutoScalingGroupARN

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon EC2 Auto Scaling group to update.
+ HealthCheckGracePeriod

  Type: Integer

  Description: (Optional) The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an Amazon EC2 instance that has come into service. Valid range is 60 to 86400.

  Default: 300

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `autoscaling:DescribeAutoScalingGroups`
+ `autoscaling:UpdateAutoScalingGroup`

**Document Steps**

1. **validateInput** - Validates that the Amazon EC2 Auto Scaling group exists, has an attached load balancer, and does not already include `ELB` in its health check types.

1. **branchOnChangeRequired** - Branches on whether an update to the Amazon EC2 Auto Scaling group is required.

1. **enableAutoScalingGroupElbHealthCheck** - Updates the Amazon EC2 Auto Scaling group's health check types using `validateInput.NewHealthCheckType` and applies the grace period from the `HealthCheckGracePeriod` parameter.

**Outputs**
+ validateInput.ChangeRequired: Whether an update to the Amazon EC2 Auto Scaling group is required.
+ validateInput.ValidationMessage: A message describing the validation result.
+ validateInput.PreviousHealthCheckType: The comma-separated health check types that the automation observes on the Amazon EC2 Auto Scaling group before making any change. Use this value to revert the change if needed. Returns an empty string when the group does not exist or has no attached load balancer.
+ validateInput.NewHealthCheckType: The comma-separated health check types that the automation passes to `UpdateAutoScalingGroup`. This value adds `ELB` to the existing health check types. Returns an empty string when no change is required.