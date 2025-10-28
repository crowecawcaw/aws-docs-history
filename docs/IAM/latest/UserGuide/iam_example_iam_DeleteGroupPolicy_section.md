# Use `DeleteGroupPolicy` with a CLI

The following code examples show how to use `DeleteGroupPolicy`.

CLI

**AWS CLI**

**To delete a policy from an IAM group**

The following `delete-group-policy` command deletes the policy named `ExamplePolicy` from the group named `Admins`.

```
`aws iam delete-group-policy \
 --group-name `Admins` \
 --policy-name `ExamplePolicy``

```

This command produces no output.

To see the policies attached to a group, use the `list-group-policies` command.

For more information, see [Managing IAM policies](access_policies_manage.md "access_policies_manage.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the inline policy named `TesterPolicy` from the IAM group `Testers`. The users in that group immediately lose the permissions defined in that policy.**

```
Remove-IAMGroupPolicy -GroupName Testers -PolicyName TestPolicy

```

- For API details, see
  [DeleteGroupPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the inline policy named `TesterPolicy` from the IAM group `Testers`. The users in that group immediately lose the permissions defined in that policy.**

```
Remove-IAMGroupPolicy -GroupName Testers -PolicyName TestPolicy

```

- For API details, see
  [DeleteGroupPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
