

# `AWSSupportRemediator-DisableAutoAssignPublicIpv4Addresses`

**Description**

Disables automatic assignment of public IPv4 addresses for an Amazon Virtual Private Cloud (Amazon VPC) subnet.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon EC2 subnets should not automatically assign public IP addresses](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-15).

If the subnet does not exist or automatic public IPv4 assignment is already disabled, the automation completes successfully without making changes.

Disabling automatic public IPv4 assignment only affects Amazon Elastic Compute Cloud (Amazon EC2) instances launched into the subnet after the change. It does not modify public IPv4 addresses already assigned to existing instances.

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
+ SubnetId

  Type: String

  Description: (Required) The ID of the Amazon VPC subnet for which to disable automatic public IPv4 assignment.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:DescribeSubnets`
+ `ec2:ModifySubnetAttribute`

**Document Steps**

1. **validateSubnet** - Validates that the subnet exists and determines whether automatic public IPv4 assignment is currently enabled.

1. **branchOnChangeRequired** - Branches on whether a change is required to disable automatic public IPv4 assignment.

1. **disableMapPublicIpOnLaunch** - Disables automatic public IPv4 assignment for the subnet by setting `MapPublicIpOnLaunch` to false.

**Outputs**
+ validateSubnet.ChangeRequired: Whether a change is required to disable automatic public IPv4 assignment.
+ validateSubnet.ValidationMessage: A message describing the validation result.