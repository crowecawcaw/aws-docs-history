

# `AWSSupportRemediator-EnableClbConnectionDraining`

**Description**

Enables connection draining for an Elastic Load Balancing (ELB) Classic Load Balancer.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [CLB Connection Draining](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#elb-connection-draining).

If the load balancer does not exist or connection draining is already enabled, the automation completes successfully without making changes.

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
+ ConnectionDrainingTimeout

  Type: Integer

  Description: (Optional) The maximum time, in seconds, to keep the existing connections open before deregistering the instances.

  Default: 300

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

1. **validateLoadBalancer** - Validates that the Classic Load Balancer exists and checks whether connection draining is already enabled.

1. **branchOnChangeRequired** - Branches on whether connection draining needs to be enabled.

1. **updateLoadBalancer** - Enables connection draining for the Classic Load Balancer with the specified timeout.

**Outputs**
+ validateLoadBalancer.ChangeRequired: Whether the load balancer requires connection draining to be enabled.
+ validateLoadBalancer.ValidationMessage: A message describing the validation result.