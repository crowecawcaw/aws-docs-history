# Use `ModifyVpcAttribute` with a CLI

The following code examples show how to use `ModifyVpcAttribute`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To modify the enableDnsSupport attribute**

This example modifies the `enableDnsSupport` attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is `true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not. If the command succeeds, no output is returned.

Command:

```
`aws ec2 modify-vpc-attribute --vpc-id `vpc-a01106c2` --enable-dns-support "{\"Value\":false}"`

```

**To modify the enableDnsHostnames attribute**

This example modifies the `enableDnsHostnames` attribute. This attribute indicates whether instances launched in the VPC get DNS hostnames. If this attribute is `true`, instances in the VPC get DNS hostnames; otherwise, they do not. If the command succeeds, no output is returned.

Command:

```
`aws ec2 modify-vpc-attribute --vpc-id `vpc-a01106c2` --enable-dns-hostnames "{\"Value\":false}"`

```

- For API details, see
  [ModifyVpcAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example enables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $true

```

**Example 2: This example disables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $false

```

**Example 3: This example enables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $true

```

**Example 4: This example disables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $false

```

- For API details, see
  [ModifyVpcAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example enables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $true

```

**Example 2: This example disables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $false

```

**Example 3: This example enables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $true

```

**Example 4: This example disables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $false

```

- For API details, see
  [ModifyVpcAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
