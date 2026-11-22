

# `AWSSupportRemediator-EnableElbDeletionProtection`

**Description**

Enables deletion protection for an Elastic Load Balancing (ELB) Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Elastic Load Balancing Deletion Protection Not Enabled for Load Balancers](https://docs.aws.amazon.com/awssupport/latest/user/operational-excellence-checks.html#elb-deletion-protection-enabled).

If the load balancer does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

This automation modifies the load balancer attributes directly through the ELB API.

After this automation completes, `DeleteLoadBalancer` calls fail until you disable deletion protection. This restriction also applies to CloudFormation stack deletions when the load balancer is part of a stack.

To delete the load balancer or its CloudFormation stack, first disable deletion protection by calling `ModifyLoadBalancerAttributes` with `deletion_protection.enabled` set to `false`.

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
+ LoadBalancerArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the load balancer.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

1. **validateELB** - Validates that the load balancer exists and checks whether deletion protection is already enabled.

1. **branchOnChangeRequired** - Branches on whether deletion protection requires an update.

1. **updateELB** - Enables deletion protection on the load balancer.

**Outputs**
+ validateELB.ChangeRequired: Whether deletion protection requires an update.
+ validateELB.ValidationMessage: A message describing the validation result.