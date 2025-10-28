# Use `DetachGroupPolicy` with a CLI

The following code examples show how to use `DetachGroupPolicy`.

CLI

**AWS CLI**

**To detach a policy from a group**

This example removes the managed policy with the ARN `arn:aws:iam::123456789012:policy/TesterAccessPolicy` from the group called `Testers`.

```
`aws iam detach-group-policy \
 --group-name `Testers` \
 --policy-arn `arn:aws:iam::123456789012:policy/TesterAccessPolicy``

```

This command produces no output.

For more information, see [Managing IAM user groups](id_groups_manage.md "id_groups_manage.md") in the _AWS IAM User Guide_.

- For API details, see
  [DetachGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example detaches the managed group policy whose ARN is `arn:aws:iam::123456789012:policy/TesterAccessPolicy` from the group named `Testers`.**

```
Unregister-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterAccessPolicy

```

**Example 2: This example finds all the managed policies that are attached to the group named `Testers` and detaches them from the group.**

```
Get-IAMAttachedGroupPolicies -GroupName Testers | Unregister-IAMGroupPolicy -Groupname Testers

```

- For API details, see
  [DetachGroupPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example detaches the managed group policy whose ARN is `arn:aws:iam::123456789012:policy/TesterAccessPolicy` from the group named `Testers`.**

```
Unregister-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterAccessPolicy

```

**Example 2: This example finds all the managed policies that are attached to the group named `Testers` and detaches them from the group.**

```
Get-IAMAttachedGroupPolicies -GroupName Testers | Unregister-IAMGroupPolicy -Groupname Testers

```

- For API details, see
  [DetachGroupPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
