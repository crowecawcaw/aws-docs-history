# Use `AttachNetworkInterface` with a CLI

The following code examples show how to use `AttachNetworkInterface`.

CLI

**AWS CLI**

**Example 1: To attach a network interface to an instance**

The following `attach-network-interface` example attaches the specified network interface to the specified instance.

```
`aws ec2 attach-network-interface \
 --network-interface-id `eni-0dc56a8d4640ad10a` \
 --instance-id `i-1234567890abcdef0` \
 --device-index `1``

```

Output:

```
{
    "AttachmentId": "eni-attach-01a8fc87363f07cf9"
}
```

For more information, see [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide_.

**Example 2: To attach a network interface to an instance with multiple network cards**

The following `attach-network-interface` example attaches the specified network interface to the specified instance and network card.

```
`aws ec2 attach-network-interface \
 --network-interface-id `eni-07483b1897541ad83` \
 --instance-id `i-01234567890abcdef` \
 --network-card-index `1` \
 --device-index `1``

```

Output:

```
{
    "AttachmentId": "eni-attach-0fbd7ee87a88cd06c"
}
```

For more information, see [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [AttachNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-network-interface.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-network-interface.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attaches the specified network interface to the specified instance.**

```
Add-EC2NetworkInterface -NetworkInterfaceId eni-12345678 -InstanceId i-1a2b3c4d -DeviceIndex 1

```

**Output:**

```
eni-attach-1a2b3c4d
```

- For API details, see
  [AttachNetworkInterface](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attaches the specified network interface to the specified instance.**

```
Add-EC2NetworkInterface -NetworkInterfaceId eni-12345678 -InstanceId i-1a2b3c4d -DeviceIndex 1

```

**Output:**

```
eni-attach-1a2b3c4d
```

- For API details, see
  [AttachNetworkInterface](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
