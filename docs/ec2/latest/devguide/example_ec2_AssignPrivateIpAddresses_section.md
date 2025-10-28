# Use `AssignPrivateIpAddresses` with a CLI

The following code examples show how to use `AssignPrivateIpAddresses`.

CLI

**AWS CLI**

**To assign a specific secondary private IP address a network interface**

This example assigns the specified secondary private IP address to the specified network interface. If the command succeeds, no output is returned.

Command:

```
`aws ec2 assign-private-ip-addresses --network-interface-id `eni-e5aa89a3` --private-ip-addresses `10.0.0.82``

```

**To assign secondary private IP addresses that Amazon EC2 selects to a network interface**

This example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses in the CIDR block range of the subnet the network interface is associated with. If the command succeeds, no output is returned.

Command:

```
`aws ec2 assign-private-ip-addresses --network-interface-id `eni-e5aa89a3` --secondary-private-ip-address-count `2``

```

- For API details, see
  [AssignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-ip-addresses.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-ip-addresses.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example assigns the specified secondary private IP address to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82

```

**Example 2: This example creates two secondary private IP addresses and assigns them to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -SecondaryPrivateIpAddressCount 2

```

- For API details, see
  [AssignPrivateIpAddresses](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example assigns the specified secondary private IP address to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82

```

**Example 2: This example creates two secondary private IP addresses and assigns them to the specified network interface.**

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -SecondaryPrivateIpAddressCount 2

```

- For API details, see
  [AssignPrivateIpAddresses](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
