# Use `TagRole` with a CLI

The following code examples show how to use `TagRole`.

CLI

**AWS CLI**

**To add a tag to a role**

The following `tag-role` command adds a tag with a Department name to the specified role.

```
`aws iam tag-role --role-name `my-role` \
 --tags '`{"Key": "Department", "Value": "Accounting"}`'`

```

This command produces no output.

For more information, see [Tagging IAM resources](id_tags.md "id_tags.md") in the _AWS IAM User Guide_.

- For API details, see
  [TagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example adds tag to Role in Identity Management Service**

```
Add-IAMRoleTag -RoleName AdminRoleacess -Tag @{ Key = 'abac'; Value = 'testing'}

```

- For API details, see
  [TagRole](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example adds tag to Role in Identity Management Service**

```
Add-IAMRoleTag -RoleName AdminRoleacess -Tag @{ Key = 'abac'; Value = 'testing'}

```

- For API details, see
  [TagRole](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
