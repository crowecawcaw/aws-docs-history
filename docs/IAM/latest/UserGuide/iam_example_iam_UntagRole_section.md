# Use `UntagRole` with a CLI

The following code examples show how to use `UntagRole`.

CLI

**AWS CLI**

**To remove a tag from a role**

The following `untag-role` command removes any tag with the key name 'Department' from the specified role.

```
`aws iam untag-role \
 --role-name `my-role` \
 --tag-keys `Department``

```

This command produces no output.

For more information, see [Tagging IAM resources](id_tags.md "id_tags.md") in the _AWS IAM User Guide_.

- For API details, see
  [UntagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"

```

- For API details, see
  [UntagRole](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"

```

- For API details, see
  [UntagRole](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
