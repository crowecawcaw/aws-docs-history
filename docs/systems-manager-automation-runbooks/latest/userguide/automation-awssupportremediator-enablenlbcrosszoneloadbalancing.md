

# `AWSSupportRemediator-EnableNlbCrossZoneLoadBalancing`

**Description**

Enables cross-zone load balancing for an Elastic Load Balancing (ELB) Network Load Balancer.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Network Load Balancers Cross Load Balancing](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#network-load-balancers-cross-load-balancing).

If the Network Load Balancer does not exist or already has cross-zone load balancing enabled, the automation completes successfully without making changes.

When enabling cross-zone load balancing for the Network Load Balancer, Amazon Elastic Compute Cloud (Amazon EC2) data transfer charges apply. For more information about pricing, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

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
+ NLBArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Network Load Balancer to enable cross-zone load balancing.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

1. **validateNetworkLoadBalancer** - Validates that the Network Load Balancer exists and whether cross-zone load balancing is already enabled.

1. **branchOnChangeRequired** - Branches on whether modification is needed.

1. **enableNLBCrossZoneLoadBalancing** - Enables cross-zone load balancing for the Network Load Balancer.

**Outputs**
+ validateNetworkLoadBalancer.ChangeRequired: Whether a change is required for the Network Load Balancer.
+ validateNetworkLoadBalancer.ValidationMessage: The validation result message.