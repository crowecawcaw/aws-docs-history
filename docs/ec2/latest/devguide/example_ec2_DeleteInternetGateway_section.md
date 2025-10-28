# Use `DeleteInternetGateway` with a CLI

The following code examples show how to use `DeleteInternetGateway`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To delete an internet gateway**

The following `delete-internet-gateway` example deletes the specified internet gateway.

```
`aws ec2 delete-internet-gateway \
 --internet-gateway-id `igw-0d0fb496b3EXAMPLE``

```

This command produces no output.

For more information, see [Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the _Amazon VPC User Guide_.

- For API details, see
  [DeleteInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the specified Internet gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2InternetGateway (DeleteInternetGateway)" on Target "igw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteInternetGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the specified Internet gateway. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2InternetGateway -InternetGatewayId igw-1a2b3c4d

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2InternetGateway (DeleteInternetGateway)" on Target "igw-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteInternetGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
