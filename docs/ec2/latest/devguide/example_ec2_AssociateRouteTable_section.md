# Use `AssociateRouteTable` with a CLI

The following code examples show how to use `AssociateRouteTable`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Create a VPC with private subnets and NAT gateways](example_vpc_GettingStartedPrivate_section.md "example_vpc_GettingStartedPrivate_section.md")
- [Get started with Amazon VPC](example_vpc_GettingStartedCLI_section.md "example_vpc_GettingStartedCLI_section.md")

CLI

**AWS CLI**

**To associate a route table with a subnet**

This example associates the specified route table with the specified subnet.

Command:

```
`aws ec2 associate-route-table --route-table-id `rtb-22574640` --subnet-id `subnet-9d4a7b6c``

```

Output:

```
{
    "AssociationId": "rtbassoc-781d0d1a"
}
```

- For API details, see
  [AssociateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-route-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-route-table.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example associates the specified route table with the specified subnet.**

```
Register-EC2RouteTable -RouteTableId rtb-1a2b3c4d -SubnetId subnet-1a2b3c4d

```

**Output:**

```
rtbassoc-12345678
```

- For API details, see
  [AssociateRouteTable](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example associates the specified route table with the specified subnet.**

```
Register-EC2RouteTable -RouteTableId rtb-1a2b3c4d -SubnetId subnet-1a2b3c4d

```

**Output:**

```
rtbassoc-12345678
```

- For API details, see
  [AssociateRouteTable](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
