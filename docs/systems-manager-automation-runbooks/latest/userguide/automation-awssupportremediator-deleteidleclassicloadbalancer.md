

# `AWSSupportRemediator-DeleteIdleClassicLoadBalancer`

**Description**

Deletes an idle Elastic Load Balancing (ELB) Classic Load Balancer and its associated Amazon CloudWatch alarms.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Idle Load Balancers](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#idle-load-balancers).

If the Classic Load Balancer does not exist, the automation completes successfully without making changes.

The automation considers a Classic Load Balancer idle when it has no registered instances and has had zero successful connections within the specified idle period (default: 7 days). The automation fails if the load balancer has registered instances or has had successful connections within the specified idle period.

The automation deletes the Classic Load Balancer and any CloudWatch metric alarms associated with the load balancer. The automation also deletes CloudWatch composite alarms that reference only the load balancer metric alarms. The automation does not delete metric alarms referenced by composite alarms that also contain non-load-balancer metrics. The automation saves the load balancer description, attributes, and policy descriptions as step outputs before deletion.

**Irreversible action**  
Deleting a Classic Load Balancer is irreversible.

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
+ LoadBalancerName

  Type: String

  Description: (Required) The name of the Classic Load Balancer.
+ IdleLoadBalancerDays

  Type: Integer

  Description: (Optional) The number of days in which the Classic Load Balancer has had zero successful connections before considering it idle. If set to 0, the load balancer is considered idle regardless of connection history.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudwatch:DeleteAlarms`
+ `cloudwatch:DescribeAlarms`
+ `cloudwatch:GetMetricData`
+ `elasticloadbalancing:DeleteLoadBalancer`
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:DescribeLoadBalancerPolicies`
+ `elasticloadbalancing:DescribeLoadBalancers`

**Document Steps**

1. **validateLoadBalancerIdle** - Validates that the Classic Load Balancer exists, has no registered instances, and has had no successful connections within the specified idle period. Returns the list of associated CloudWatch alarms to delete.

1. **branchOnChangeRequired** - Branches on whether the Classic Load Balancer is idle and requires deletion.

1. **describeLoadBalancerAttributes** - Retrieves the Classic Load Balancer attributes before deletion.

1. **describePolicyDescriptions** - Retrieves the Classic Load Balancer policy descriptions before deletion.

1. **deleteClassicLoadBalancer** - Deletes the Classic Load Balancer.

1. **branchOnDeleteCompositeAlarms** - Branches on whether composite alarms need to be deleted.

1. **deleteCompositeAlarms** - Deletes each composite alarm associated with the Classic Load Balancer.

1. **branchOnDeleteAlarms** - Branches on whether metric alarms need to be deleted.

1. **deleteMetricAlarms** - Deletes the metric alarms associated with the Classic Load Balancer.

**Outputs**
+ validateLoadBalancerIdle.ChangeRequired: Whether the Classic Load Balancer is idle and requires deletion.
+ validateLoadBalancerIdle.ValidationMessage: A message describing the validation result.
+ validateLoadBalancerIdle.MetricAlarmsToDelete: The list of metric alarm names to delete.
+ validateLoadBalancerIdle.CompositeAlarmsListToDelete: The list of composite alarm names to delete.
+ deleteCompositeAlarms.DeletedCompositeAlarms: The list of composite alarms that the automation deleted.
+ deleteCompositeAlarms.NotDeletedCompositeAlarms: The list of composite alarms that the automation did not delete.
+ validateLoadBalancerIdle.CurrentLoadBalancerDescriptions: The load balancer descriptions before deletion.
+ describeLoadBalancerAttributes.CurrentLoadBalancerAttributes: The load balancer attributes before deletion.
+ describePolicyDescriptions.CurrentPolicyDescriptions: The load balancer policy descriptions before deletion.