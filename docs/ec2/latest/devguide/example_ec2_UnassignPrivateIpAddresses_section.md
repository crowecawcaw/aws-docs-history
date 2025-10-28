# Use `UnassignPrivateIpAddresses` with a CLI

The following code examples show how to use `UnassignPrivateIpAddresses`.

CLI

**AWS CLI**

**To unassign a secondary private IP address from a network interface**

This example unassigns the specified private IP address from the specified network interface. If the command succeeds, no output is returned.

Command:

```
`aws ec2 unassign-private-ip-addresses --network-interface-id `eni-e5aa89a3` --private-ip-addresses `10.0.0.82``

```

- For API details, see
  [UnassignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-ip-addresses.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-ip-addresses.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example unassigns the specified private IP address from the specified network interface.**

```
Unregister-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82

```

- For API details, see
  [UnassignPrivateIpAddresses](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example unassigns the specified private IP address from the specified network interface.**

```
Unregister-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82

```

- For API details, see
  [UnassignPrivateIpAddresses](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
