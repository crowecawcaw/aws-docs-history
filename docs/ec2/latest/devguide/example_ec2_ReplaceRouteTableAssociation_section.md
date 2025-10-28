# Use `ReplaceRouteTableAssociation` with a CLI

The following code examples show how to use `ReplaceRouteTableAssociation`.

CLI

**AWS CLI**

**To replace the route table associated with a subnet**

This example associates the specified route table with the subnet for the specified route table association.

Command:

```
`aws ec2 replace-route-table-association --association-id `rtbassoc-781d0d1a` --route-table-id `rtb-22574640``

```

Output:

```
{
    "NewAssociationId": "rtbassoc-3a1f0f58"
}
```

- For API details, see
  [ReplaceRouteTableAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route-table-association.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route-table-association.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example associates the specified route table with the subnet for the specified route table association.**

```
Set-EC2RouteTableAssociation -RouteTableId rtb-1a2b3c4d -AssociationId rtbassoc-12345678

```

**Output:**

```
rtbassoc-87654321
```

- For API details, see
  [ReplaceRouteTableAssociation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example associates the specified route table with the subnet for the specified route table association.**

```
Set-EC2RouteTableAssociation -RouteTableId rtb-1a2b3c4d -AssociationId rtbassoc-12345678

```

**Output:**

```
rtbassoc-87654321
```

- For API details, see
  [ReplaceRouteTableAssociation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
