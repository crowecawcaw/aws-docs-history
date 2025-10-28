# Use `AttachInternetGateway` with a CLI

The following code examples show how to use `AttachInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To attach an internet gateway to your VPC**

The following `attach-internet-gateway` example attaches the specified internet gateway to the specific VPC.

```
`aws ec2 attach-internet-gateway \
 --internet-gateway-id `igw-0d0fb496b3EXAMPLE` \
 --vpc-id `vpc-0a60eb65b4EXAMPLE``

```

This command produces no output.

For more information, see [Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon VPC User Guide_.

- For API details, see
  [AttachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attaches the specified Internet gateway to the specified VPC.**

```
Add-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678

```

**Example 2: This example creates a VPC and an Internet gateway, and then attaches the Internet gateway to the VPC.**

```
$vpc = New-EC2Vpc -CidrBlock 10.0.0.0/16
New-EC2InternetGateway | Add-EC2InternetGateway -VpcId $vpc.VpcId

```

- For API details, see
  [AttachInternetGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attaches the specified Internet gateway to the specified VPC.**

```
Add-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678

```

**Example 2: This example creates a VPC and an Internet gateway, and then attaches the Internet gateway to the VPC.**

```
$vpc = New-EC2Vpc -CidrBlock 10.0.0.0/16
New-EC2InternetGateway | Add-EC2InternetGateway -VpcId $vpc.VpcId

```

- For API details, see
  [AttachInternetGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
