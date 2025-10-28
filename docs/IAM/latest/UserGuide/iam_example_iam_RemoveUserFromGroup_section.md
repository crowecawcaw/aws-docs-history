# Use `RemoveUserFromGroup` with a CLI

The following code examples show how to use `RemoveUserFromGroup`.

CLI

**AWS CLI**

**To remove a user from an IAM group**

The following `remove-user-from-group` command removes the user named `Bob` from the IAM group named `Admins`.

```
`aws iam remove-user-from-group \
 --user-name `Bob` \
 --group-name `Admins``

```

This command produces no output.

For more information, see [Adding and removing users in an IAM user group](id_groups_manage_add-remove-users.md "id_groups_manage_add-remove-users.md") in the _AWS IAM User Guide_.

- For API details, see
  [RemoveUserFromGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-user-from-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-user-from-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the IAM user `Bob` from the group `Testers`.**

```
Remove-IAMUserFromGroup -GroupName Testers -UserName Bob

```

**Example 2: This example finds any groups of which IAM user `Theresa` is a member, and then removes `Theresa` from those groups.**

```
$groups = Get-IAMGroupForUser -UserName Theresa
foreach ($group in $groups) { Remove-IAMUserFromGroup -GroupName $group.GroupName -UserName Theresa -Force }

```

**Example 3: This example shows an alternate way of removing the IAM user `Bob` from the `Testers` group.**

```
Get-IAMGroupForUser -UserName Bob | Remove-IAMUserFromGroup -UserName Bob -GroupName Testers -Force

```

- For API details, see
  [RemoveUserFromGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the IAM user `Bob` from the group `Testers`.**

```
Remove-IAMUserFromGroup -GroupName Testers -UserName Bob

```

**Example 2: This example finds any groups of which IAM user `Theresa` is a member, and then removes `Theresa` from those groups.**

```
$groups = Get-IAMGroupForUser -UserName Theresa
foreach ($group in $groups) { Remove-IAMUserFromGroup -GroupName $group.GroupName -UserName Theresa -Force }

```

**Example 3: This example shows an alternate way of removing the IAM user `Bob` from the `Testers` group.**

```
Get-IAMGroupForUser -UserName Bob | Remove-IAMUserFromGroup -UserName Bob -GroupName Testers -Force

```

- For API details, see
  [RemoveUserFromGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
