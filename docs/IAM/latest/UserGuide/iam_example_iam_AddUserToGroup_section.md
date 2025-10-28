# Use `AddUserToGroup` with a CLI

The following code examples show how to use `AddUserToGroup`.

CLI

**AWS CLI**

**To add a user to an IAM group**

The following `add-user-to-group` command adds an IAM user named `Bob` to the IAM group named `Admins`.

```
`aws iam add-user-to-group \
 --user-name `Bob` \
 --group-name `Admins``

```

This command produces no output.

For more information, see [Adding and removing users in an IAM user group](id_groups_manage_add-remove-users.md "id_groups_manage_add-remove-users.md") in the _AWS IAM User Guide_.

- For API details, see
  [AddUserToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-user-to-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-user-to-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command adds the user named `Bob` to the group named `Admins`.**

```
Add-IAMUserToGroup -UserName "Bob" -GroupName "Admins"

```

- For API details, see
  [AddUserToGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command adds the user named `Bob` to the group named `Admins`.**

```
Add-IAMUserToGroup -UserName "Bob" -GroupName "Admins"

```

- For API details, see
  [AddUserToGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
