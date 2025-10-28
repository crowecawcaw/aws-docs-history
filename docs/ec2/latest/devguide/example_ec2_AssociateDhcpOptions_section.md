# Use `AssociateDhcpOptions` with a CLI

The following code examples show how to use `AssociateDhcpOptions`.

CLI

**AWS CLI**

**To associate a DHCP options set with your VPC**

This example associates the specified DHCP options set with the specified VPC. If the command succeeds, no output is returned.

Command:

```
`aws ec2 associate-dhcp-options --dhcp-options-id `dopt-d9070ebb` --vpc-id `vpc-a01106c2``

```

**To associate the default DHCP options set with your VPC**

This example associates the default DHCP options set with the specified VPC. If the command succeeds, no output is returned.

Command:

```
`aws ec2 associate-dhcp-options --dhcp-options-id `default` --vpc-id `vpc-a01106c2``

```

- For API details, see
  [AssociateDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example associates the specified DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678

```

**Example 2: This example associates the default DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678

```

- For API details, see
  [AssociateDhcpOptions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example associates the specified DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId dopt-1a2b3c4d -VpcId vpc-12345678

```

**Example 2: This example associates the default DHCP options set with the specified VPC.**

```
Register-EC2DhcpOption -DhcpOptionsId default -VpcId vpc-12345678

```

- For API details, see
  [AssociateDhcpOptions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
