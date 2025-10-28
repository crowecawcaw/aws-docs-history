# Use `DeleteNetworkAcl` with a CLI

The following code examples show how to use `DeleteNetworkAcl`.

CLI

**AWS CLI**

**To delete a network ACL**

This example deletes the specified network ACL. If the command succeeds, no output is returned.

Command:

```
`aws ec2 delete-network-acl --network-acl-id `acl-5fb85d36``

```

- For API details, see
  [DeleteNetworkAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the specified network ACL. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkAcl -NetworkAclId acl-12345678

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkAcl (DeleteNetworkAcl)" on Target "acl-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteNetworkAcl](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the specified network ACL. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkAcl -NetworkAclId acl-12345678

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkAcl (DeleteNetworkAcl)" on Target "acl-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteNetworkAcl](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
