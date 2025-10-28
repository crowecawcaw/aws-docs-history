# Use `ReplaceNetworkAclAssociation` with a CLI

The following code examples show how to use `ReplaceNetworkAclAssociation`.

CLI

**AWS CLI**

**To replace the network ACL associated with a subnet**

This example associates the specified network ACL with the subnet for the specified network ACL association.

Command:

```
`aws ec2 replace-network-acl-association --association-id `aclassoc-e5b95c8c` --network-acl-id `acl-5fb85d36``

```

Output:

```
{
    "NewAssociationId": "aclassoc-3999875b"
}
```

- For API details, see
  [ReplaceNetworkAclAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-association.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-association.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example associates the specified network ACL with the subnet for the specified network ACL association.**

```
Set-EC2NetworkAclAssociation -NetworkAclId acl-12345678 -AssociationId aclassoc-1a2b3c4d

```

**Output:**

```
aclassoc-87654321
```

- For API details, see
  [ReplaceNetworkAclAssociation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example associates the specified network ACL with the subnet for the specified network ACL association.**

```
Set-EC2NetworkAclAssociation -NetworkAclId acl-12345678 -AssociationId aclassoc-1a2b3c4d

```

**Output:**

```
aclassoc-87654321
```

- For API details, see
  [ReplaceNetworkAclAssociation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
