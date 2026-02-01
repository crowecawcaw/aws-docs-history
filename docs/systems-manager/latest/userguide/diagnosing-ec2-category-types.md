• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Categories of diagnosable unmanaged

EC2 instance issues

This topic lists the major categories of EC2 management issues, and the specific
issues in each category, that Systems Manager can help you diagnose and remediate. Note that
for some of the issues, Systems Manager can identify the issue, but not provide automatic
remediation. In those cases, the Systems Manager console directs you to information to help
you manually resolve an issue.

The diagnosis process examines each group of EC2 instances at once according to
the virtual private cloud (VPC) they belong to.

###### Issue types

- [Problem category: Security
  group configuration and HTTPS communications](#unmanaged-ec2-issue-security-groups "#unmanaged-ec2-issue-security-groups")
- [Problem category: DNS or
  DNS host name configuration](#unmanaged-ec2-issue-dns-configuration "#unmanaged-ec2-issue-dns-configuration")
- [Problem
  category: VPC endpoint configuration](#unmanaged-ec2-issue-vpc-endpoint-configuration "#unmanaged-ec2-issue-vpc-endpoint-configuration")

## Problem category: Security

group configuration and HTTPS communications

A diagnosis operation might find that SSM Agent isn't able to communicate with
the Systems Manager service over HTTPS. In those cases, you can choose to execute an
Automation runbook that attempts to update security groups that are attached to
the instances.

###### Note

Occasionally, Systems Manager might not be able to automatically remediate these
issues, but you can manually edit the affected security groups.

###### Supported issue types

- **Instance security group**: Outbound
  traffic is not allowed on port 443
- **`ssm` VPC endpoint’s security
  group**: Inbound traffic is not allowed on port 443
- **`ssmmessages` VPC endpoint's security
  group**: Inbound traffic not allowed on port 443
- **`ec2messages` VPC endpoint's security
  group**: Inbound traffic not allowed on port 443

For more information, see [Verify ingress rules on endpoint
security groups](troubleshooting-ssm-agent.md#agent-ts-ingress-egress-rules "troubleshooting-ssm-agent.md#agent-ts-ingress-egress-rules") in the topic [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").

## Problem category: DNS or

DNS host name configuration

A diagnosis operation might find that Doman Name System (DNS) or DNS host
names aren't properly configured for the VPC. In those cases, you can choose to
execute an Automation runbook that attempts to enable the
`enableDnsSupport` and `enableDnsHostnames` attributes
of the affected VPC.

###### Supported issue types

- DNS support is disabled in a VPC.
- A DNS hostname is disabled in a VPC.

For more information, see [Verify your VPC DNS-related
attributes](troubleshooting-ssm-agent.md#agent-ts-dns-attributes "troubleshooting-ssm-agent.md#agent-ts-dns-attributes") in the topic [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").

## Problem

category: VPC endpoint configuration

A diagnosis operation might find that VPC endpoints aren't properly configured
for the VPC.

If VPC endpoints required by SSM Agent don't exist, Systems Manager attempts to execute
an Automation runbook to create the VPC endpoints and associates them with one
subnet in each relevant regional availability zone (AZ). If VPC the required
endpoints exist but aren't associated with a subnet in which the issue is found,
the runbook associates the VPC endpoints to the affected subnet.

###### Note

Systems Manager doesn't support remediating all misconfigured VPC endpoint issues.
In those cases, Systems Manager directs you to manual remedy instructions instead of
running an Automation runbook.

###### Supported issue types

- No `ssm.`region`.amazonaws.com`
  endpoint for PrivateLink was found.
- No
  `ssmmessages.`region`.amazonaws.com`
  endpoint for PrivateLink was found.
- No
  `ec2messages.`region`.amazonaws.com`
  endpoint for PrivateLink was found.

###### Diagnosable issue types

Systems Manager can diagnose the following issue types, but currently no runbook is
available for remediating their issues. You can edit your configuration
manually for these issues.

- An instance's subnet is not attached to an
  `ssm.`region`.amazonaws.com`
  endpoint.
- An instance's subnet is not attached to an
  `ssmmessages.`region`.amazonaws.com`
  endpoint.
- An instance's subnet not attached to an
  `ec2messages.`region`.amazonaws.com`
  endpoint.

For more information, see [Verify your VPC configuration](troubleshooting-ssm-agent.md#agent-ts-vpc-configuration "troubleshooting-ssm-agent.md#agent-ts-vpc-configuration") in the topic [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").
