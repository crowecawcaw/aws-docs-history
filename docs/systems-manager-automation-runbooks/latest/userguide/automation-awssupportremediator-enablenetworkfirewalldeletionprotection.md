

# `AWSSupportRemediator-EnableNetworkFirewallDeletionProtection`

**Description**

Enables deletion protection for an AWS Network Firewall firewall.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Network Firewall firewalls should have deletion protection enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-9).

If the firewall does not exist or deletion protection is already enabled, the automation completes successfully without making changes.

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
+ NetworkFirewallArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the firewall.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `network-firewall:DescribeFirewall`
+ `network-firewall:UpdateFirewallDeleteProtection`

**Document Steps**

1. **validate** - Validates whether the firewall exists and whether deletion protection is already enabled.

1. **branchOnChangeRequired** - Branches on whether deletion protection must be enabled on the firewall.

1. **enableDeleteProtection** - Enables deletion protection on the firewall by calling the `UpdateFirewallDeleteProtection` API.

**Outputs**
+ validate.ChangeRequired: Whether deletion protection must be enabled on the firewall.
+ validate.CurrentProtectionState: The current deletion protection state of the firewall before the automation runs.
+ validate.ValidationMessage: A message describing the validation result.