# Use `DetachInternetGateway` with a CLI

The following code examples show how to use `DetachInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To detach an internet gateway from your VPC**

The following `detach-internet-gateway` example detaches the specified internet gateway from the specific VPC.

```
`aws ec2 detach-internet-gateway \
 --internet-gateway-id `igw-0d0fb496b3EXAMPLE` \
 --vpc-id `vpc-0a60eb65b4EXAMPLE``

```

This command produces no output.

For more information, see [Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon VPC User Guide_.

- For API details, see
  [DetachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example detaches the specified Internet gateway from the specified VPC.**

```
Dismount-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678

```

- For API details, see
  [DetachInternetGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example detaches the specified Internet gateway from the specified VPC.**

```
Dismount-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d -VpcId vpc-12345678

```

- For API details, see
  [DetachInternetGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
