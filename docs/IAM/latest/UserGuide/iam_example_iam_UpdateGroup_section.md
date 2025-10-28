# Use `UpdateGroup` with a CLI

The following code examples show how to use `UpdateGroup`.

CLI

**AWS CLI**

**To rename an IAM group**

The following `update-group` command changes the name of the IAM group `Test` to `Test-1`.

```
`aws iam update-group \
 --group-name `Test` \
 --new-group-name `Test-1``

```

This command produces no output.

For more information, see [Renaming an IAM user group](id_groups_manage_rename.md "id_groups_manage_rename.md") in the _AWS IAM User Guide_.

- For API details, see
  [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example renames the IAM group `Testers` to `AppTesters`.**

```
Update-IAMGroup -GroupName Testers -NewGroupName AppTesters

```

**Example 2: This example changes the path of the IAM group `AppTesters` to `/Org1/Org2/`. This changes the ARN for the group to `arn:aws:iam::123456789012:group/Org1/Org2/AppTesters`.**

```
Update-IAMGroup -GroupName AppTesters -NewPath /Org1/Org2/

```

- For API details, see
  [UpdateGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example renames the IAM group `Testers` to `AppTesters`.**

```
Update-IAMGroup -GroupName Testers -NewGroupName AppTesters

```

**Example 2: This example changes the path of the IAM group `AppTesters` to `/Org1/Org2/`. This changes the ARN for the group to `arn:aws:iam::123456789012:group/Org1/Org2/AppTesters`.**

```
Update-IAMGroup -GroupName AppTesters -NewPath /Org1/Org2/

```

- For API details, see
  [UpdateGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
