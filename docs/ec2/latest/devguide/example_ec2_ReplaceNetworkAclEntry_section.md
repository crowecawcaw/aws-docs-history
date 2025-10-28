# Use `ReplaceNetworkAclEntry` with a CLI

The following code examples show how to use `ReplaceNetworkAclEntry`.

CLI

**AWS CLI**

**To replace a network ACL entry**

This example replaces an entry for the specified network ACL. The new rule 100 allows ingress traffic from 203.0.113.12/24 on UDP port 53 (DNS) into any associated subnet.

Command:

```
`aws ec2 replace-network-acl-entry --network-acl-id `acl-5fb85d36` --ingress --rule-number `100` --protocol `udp` --port-range `From=53,To=53` --cidr-block `203.0.113.12/24` --rule-action `allow``

```

- For API details, see
  [ReplaceNetworkAclEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-entry.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-entry.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example replaces the specified entry for the specified network ACL. The new rule allows inbound traffic from the specified address to any associated subnet.**

```
Set-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 203.0.113.12/24 -RuleAction allow

```

- For API details, see
  [ReplaceNetworkAclEntry](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example replaces the specified entry for the specified network ACL. The new rule allows inbound traffic from the specified address to any associated subnet.**

```
Set-EC2NetworkAclEntry -NetworkAclId acl-12345678 -Egress $false -RuleNumber 100 -Protocol 17 -PortRange_From 53 -PortRange_To 53 -CidrBlock 203.0.113.12/24 -RuleAction allow

```

- For API details, see
  [ReplaceNetworkAclEntry](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
