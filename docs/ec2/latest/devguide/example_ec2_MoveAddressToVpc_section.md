# Use `MoveAddressToVpc` with a CLI

The following code examples show how to use `MoveAddressToVpc`.

CLI

**AWS CLI**

**To move an address to EC2-VPC**

This example moves Elastic IP address 54.123.4.56 to the EC2-VPC platform.

Command:

```
`aws ec2 move-address-to-vpc --public-ip `54.123.4.56``

```

Output:

```
{
  "Status": "MoveInProgress"
}
```

- For API details, see
  [MoveAddressToVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-address-to-vpc.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-address-to-vpc.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example moves an EC2 instance with a public IP address of 12.345.67.89 to the EC2-VPC platform in the US East (Northern Virginia) region.**

```
Move-EC2AddressToVpc -PublicIp 12.345.67.89 -Region us-east-1

```

**Example 2: This example pipes the results of a Get-EC2Instance command to the Move-EC2AddressToVpc cmdlet. The Get-EC2Instance command gets an instance that is specified by instance ID, then returns the public IP address property of the instance.**

```
(Get-EC2Instance -Instance i-12345678).Instances.PublicIpAddress | Move-EC2AddressToVpc

```

- For API details, see
  [MoveAddressToVpc](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example moves an EC2 instance with a public IP address of 12.345.67.89 to the EC2-VPC platform in the US East (Northern Virginia) region.**

```
Move-EC2AddressToVpc -PublicIp 12.345.67.89 -Region us-east-1

```

**Example 2: This example pipes the results of a Get-EC2Instance command to the Move-EC2AddressToVpc cmdlet. The Get-EC2Instance command gets an instance that is specified by instance ID, then returns the public IP address property of the instance.**

```
(Get-EC2Instance -Instance i-12345678).Instances.PublicIpAddress | Move-EC2AddressToVpc

```

- For API details, see
  [MoveAddressToVpc](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
