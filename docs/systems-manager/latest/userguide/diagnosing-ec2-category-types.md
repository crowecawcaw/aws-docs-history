# Categories of diagnosable unmanaged EC2 instance issues

This topic lists the major categories of EC2 management issues, and the specific
issues in each category, that Systems Manager can help you diagnose and remediate. Note that
for some of the issues, Systems Manager can identify the issue, but not provide automatic
remediation. In those cases, the Systems Manager console directs you to information to help
you manually resolve an issue.

The diagnosis process examines each group of EC2 instances at once according to
the virtual private cloud (VPC) they belong to.

###### Issue types

- [Problem category: Security group configuration and HTTPS communications](#unmanaged-ec2-issue-security-groups "#unmanaged-ec2-issue-security-groups")
- [Problem category: DNS or DNS host name configuration](#unmanaged-ec2-issue-dns-configuration "#unmanaged-ec2-issue-dns-configuration")
- [Problem category: VPC endpoint configuration](#unmanaged-ec2-issue-vpc-endpoint-configuration "#unmanaged-ec2-issue-vpc-endpoint-configuration")
- [Problem category: Network ACL configuration](#unmanaged-ec2-issue-nacl-configuration "#unmanaged-ec2-issue-nacl-configuration")
- [Problem category: IAM roles and permissions](#unmanaged-ec2-issue-iam-roles-and-permissions "#unmanaged-ec2-issue-iam-roles-and-permissions")
- [Problem category: SSM Agent version](#unmanaged-ec2-issue-ssm-agent-version "#unmanaged-ec2-issue-ssm-agent-version")
- [Problem category: Instance status check](#unmanaged-ec2-issue-instance-status-check "#unmanaged-ec2-issue-instance-status-check")
- [Problem category: Operating system configuration](#unmanaged-ec2-issue-operating-system-configuration "#unmanaged-ec2-issue-operating-system-configuration")
- [Problem category: Systems Manager service configuration (Default Host Management Configuration)](#unmanaged-ec2-issue-systems-manager-service-configuration "#unmanaged-ec2-issue-systems-manager-service-configuration")
- [Problem category: Hybrid activation issues](#unmanaged-ec2-issue-hybrid-activation-issues "#unmanaged-ec2-issue-hybrid-activation-issues")

## Problem category: Security group configuration and HTTPS communications

A diagnosis operation might find that SSM Agent can't communicate with
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

For more information, see [Verify ingress rules on endpoint security groups](troubleshooting-ssm-agent.md#agent-ts-ingress-egress-rules "troubleshooting-ssm-agent.md#agent-ts-ingress-egress-rules") in the topic [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").

## Problem category: DNS or DNS host name configuration

A diagnosis operation might find that Doman Name System (DNS) or DNS host
names aren't properly configured for the VPC. In those cases, you can choose to
execute an Automation runbook that attempts to enable the
`enableDnsSupport` and `enableDnsHostnames` attributes
of the affected VPC.

###### Supported issue types

- DNS support is disabled in a VPC.
- A DNS hostname is disabled in a VPC.

For more information, see [Verify your VPC DNS-related attributes](troubleshooting-ssm-agent.md#agent-ts-dns-attributes "troubleshooting-ssm-agent.md#agent-ts-dns-attributes") in the topic [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").

## Problem category: VPC endpoint configuration

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

## Problem category: Network ACL configuration

A diagnosis operation might find that network access control lists (NACLs) aren't properly configured for the VPC, blocking necessary traffic for Systems Manager communication. NACLs are stateless, so both outbound and inbound rules must permit Systems Manager traffic.

Systems Manager can identify NACL configuration issues and provide guidance for manual remediation.

###### Supported issue types

- **Instance subnet NACL**: Outbound traffic is not allowed on port 443 to Systems Manager endpoints
- **Instance subnet NACL**: Inbound traffic is not allowed on ephemeral ports (1024-65535) for Systems Manager responses

###### Diagnosable issue types

Systems Manager can diagnose the following NACL configuration issues, but manual remediation is required:

- An instance's subnet NACL blocks outbound HTTPS (port 443) traffic to Systems Manager endpoints
- An instance's subnet NACL blocks inbound ephemeral port traffic (1024-65535) required for Systems Manager responses

For more information, see [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md"), and [Custom network ACLs for your VPC](../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports "../../../vpc/latest/userguide/custom-network-acl.md#nacl-ephemeral-ports").

## Problem category: IAM roles and permissions

A diagnosis operation might find that IAM roles or permissions aren’t properly configured for the EC2 instance to communicate with Systems Manager. In those cases, Systems Manager identifies the missing permissions and provides guidance for remediation.

###### Supported issue types

- **No instance profile attached**: The EC2 instance does not have an IAM instance profile associated with it
- **Missing SSM managed policy**: The IAM role attached to the instance profile does not include the AmazonSSMManagedInstanceCore managed policy or equivalent permissions
- **Insufficient SSM permissions**: The IAM role does not allow the minimum required actions for Systems Manager communication (ssm:UpdateInstanceInformation, ssmmessages:CreateControlChannel, ssmmessages:CreateDataChannel, ec2messages:GetMessages)

For more information, see [Configure instance permissions for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md") in the Amazon Web Services Systems Manager User Guide.

## Problem category: SSM Agent version

A diagnosis operation might find that the SSM Agent installed on the EC2 instance is outdated and no longer compatible with Systems Manager service requirements. In those cases, Systems Manager identifies the outdated agent version and provides remediation guidance.

###### Supported issue types

- **Outdated SSM Agent version**: The instance is running an SSM Agent version that is older than the minimum supported version required for Systems Manager connectivity
- **Agent version incompatible with current features**: The installed agent version does not support required communication protocols used by the Systems Manager service

For more information, see [Checking the SSM Agent version number](ssm-agent-get-version.md "ssm-agent-get-version.md"), and [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md") in the Amazon Web Services Systems Manager User Guide.

## Problem category: Instance status check

A diagnosis operation might find that the EC2 instance is failing system or instance status checks, which prevents the SSM Agent from establishing communication with the Systems Manager service. In those cases, Systems Manager identifies the status check failure and provides guidance for resolution.

###### Supported issue types

- **System status check failure**: The underlying host infrastructure supporting the instance has reported a problem, preventing Systems Manager connectivity
- **Instance status check failure**: The instance’s operating system or network configuration is not responding correctly, blocking SSM Agent communication

For more information, see [Status checks for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md "../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md") in the Amazon Web Services Systems Manager User Guide.

## Problem category: Operating system configuration

A diagnosis operation might find that OS-level issues are preventing the SSM Agent from running or communicating with the Systems Manager service. In those cases, Systems Manager analyzes the instance console output to identify boot errors, service failures, or other operating system problems.

###### Supported issue types

- **SSM Agent service not running**: The SSM Agent service has stopped or crashed due to OS-level issues such as resource exhaustion or service conflicts
- **Boot errors detected**: The instance console output indicates kernel panics, filesystem corruption, or other critical boot failures preventing normal operation
- **OS-level network blocking**: A host-based firewall (such as iptables or Windows Firewall) is blocking outbound HTTPS traffic required for Systems Manager communication
- **Disk space exhaustion**: The root volume or system partition has insufficient free space, preventing the SSM Agent from operating correctly

###### Note

Systems Manager diagnoses OS-level issues by analyzing instance console output. Automatic remediation is not available for these issues because they require direct access to the instance operating system. Systems Manager provides guidance for manual resolution.

For more information, see [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md") in the Amazon Web Services Systems Manager User Guide.

## Problem category: Systems Manager service configuration (Default Host Management Configuration)

A diagnosis operation might find that Default Host Management Configuration (DHMC) is not properly configured in the account and Region. DHMC allows Systems Manager to manage EC2 instances automatically without requiring an instance profile on each instance. If DHMC is not enabled or its associated role lacks required permissions, instances without an instance profile cannot be managed.

###### Supported issue types

- **DHMC not enabled**: Default Host Management Configuration is not turned on in the account and Region. Instances without an instance profile cannot be managed by Systems Manager
- **DHMC role missing required policies**: The IAM role configured for DHMC does not include the AmazonSSMManagedInstanceCore managed policy or equivalent permissions required for Systems Manager connectivity
- **DHMC role trust policy misconfigured**: The IAM role configured for DHMC does not have the correct trust relationship allowing the Systems Manager service to assume it

For more information, see [Default Host Management Configuration](fleet-manager-default-host-management-configuration.md "fleet-manager-default-host-management-configuration.md") in the Amazon Web Services Systems Manager User Guide.

## Problem category: Hybrid activation issues

A diagnosis operation might find that hybrid-activated nodes (instances outside of Amazon Web Services, such as on-premises servers or VMs in other cloud environments) are experiencing registration or connectivity issues with Systems Manager. In those cases, Systems Manager identifies activation and registration problems specific to hybrid environments.

###### Supported issue types

- **Activation expired**: The hybrid activation used to register the managed node has expired. A new activation must be created to register additional nodes
- **Activation registration limit reached**: The maximum number of registrations allowed by the activation has been reached. A new activation with a higher registration limit must be created, or existing registrations must be deregistered
- **Agent registration conflict**: A conflicting registration exists for the node, typically caused by cloning a VM that was previously registered with Systems Manager without deregistering first
- **Connectivity to Systems Manager endpoints**: The hybrid node cannot reach the required Systems Manager service endpoints from its network location

For more information, see [Create a hybrid activation to register nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md"), and [Troubleshooting managed node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md") in the Amazon Web Services Systems Manager User Guide.
