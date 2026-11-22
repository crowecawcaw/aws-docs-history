

# `AWSSupportRemediator-DropInvalidHeadersForAlb`

**Description**

Enables the `routing.http.drop_invalid_header_fields.enabled` attribute on an Elastic Load Balancing (ELB) Application Load Balancer.

When enabled, the load balancer drops HTTP headers with invalid characters before forwarding requests to targets, which mitigates HTTP header smuggling and related attacks.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Application Load Balancer should be configured to drop invalid http headers](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-4).

If the Application Load Balancer does not exist or drop invalid headers is already enabled, the automation completes successfully without making changes.

Enabling this attribute might affect legacy or non-compliant applications that rely on headers containing invalid characters. The load balancer removes those headers instead of forwarding them to targets.

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

  Description: (Required) The Amazon Resource Name (ARN) of the Application Load Balancer.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `elasticloadbalancing:DescribeLoadBalancerAttributes`
+ `elasticloadbalancing:ModifyLoadBalancerAttributes`

**Document Steps**

1. **validateLoadBalancer** - Validates whether the `routing.http.drop_invalid_header_fields.enabled` attribute is already set to `true` on the Application Load Balancer.

1. **branchOnValidationResult** - Branches on whether a configuration change is required. Continues to `enableDropInvalidHeaders` when a change is required; otherwise ends the runbook.

1. **enableDropInvalidHeaders** - Sets the `routing.http.drop_invalid_header_fields.enabled` attribute to `true` on the Application Load Balancer.

**Outputs**
+ validateLoadBalancer.ChangeRequired: Whether a configuration change is required.
+ validateLoadBalancer.ValidationMessage: A message describing the validation result.