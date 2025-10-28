# Use `CreateNetworkAclEntry` with a CLI

The following code examples show how to use `CreateNetworkAclEntry`.

CLI

**AWS CLI**

**To create a network ACL entry**

This example creates an entry for the specified network ACL. The rule allows ingress traffic from any IPv4 address (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet. If the command succeeds, no output is returned.

Command:

```
`aws ec2 create-network-acl-entry --network-acl-id `acl-5fb85d36` --ingress --rule-number `100` --protocol `udp` --port-range `From=53,To=53` --cidr-block `0.0.0.0/0` --rule-action `allow``

```

This example creates a rule for the specified network ACL that allows ingress traffic from any IPv6 address (::/0) on TCP port 80 (HTTP).

Command:

```
`aws ec2 create-network-acl-entry --network-acl-id `acl-5fb85d36` --ingress --rule-number `120` --protocol `tcp` --port-range `From=80,To=80` --ipv6-cidr-block `::/0` --rule-action `allow``

```

- For API details, see
  [CreateNetworkAclEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates an entry for the specified network ACL. The rule allows inbound traffic from anywhere (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet.**

```
New-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 0.0.0.0/0 -RuleAction allow

```

- For API details, see
  [CreateNetworkAclEntry](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates an entry for the specified network ACL. The rule allows inbound traffic from anywhere (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet.**

```
New-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 0.0.0.0/0 -RuleAction allow

```

- For API details, see
  [CreateNetworkAclEntry](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
