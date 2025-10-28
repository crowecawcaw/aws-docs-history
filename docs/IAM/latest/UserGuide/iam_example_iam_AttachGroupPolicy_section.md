# Use `AttachGroupPolicy` with a CLI

The following code examples show how to use `AttachGroupPolicy`.

CLI

**AWS CLI**

**To attach a managed policy to an IAM group**

The following `attach-group-policy` command attaches the AWS managed policy named `ReadOnlyAccess` to the IAM group named `Finance`.

```
`aws iam attach-group-policy \
 --policy-arn `arn:aws:iam::aws:policy/ReadOnlyAccess` \
 --group-name `Finance``

```

This command produces no output.

For more information, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md") in the _AWS IAM User Guide_.

- For API details, see
  [AttachGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attaches the customer managed policy named `TesterPolicy` to the IAM group `Testers`. The users in that group are immediately affected by the permissions defined in the default version of that policy.**

```
Register-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterPolicy

```

**Example 2: This example attaches the AWS managed policy named `AdministratorAccess` to the IAM group `Admins`. The users in that group are immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMGroupPolicy -GroupName Admins -PolicyArn arn:aws:iam::aws:policy/AdministratorAccess

```

- For API details, see
  [AttachGroupPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attaches the customer managed policy named `TesterPolicy` to the IAM group `Testers`. The users in that group are immediately affected by the permissions defined in the default version of that policy.**

```
Register-IAMGroupPolicy -GroupName Testers -PolicyArn arn:aws:iam::123456789012:policy/TesterPolicy

```

**Example 2: This example attaches the AWS managed policy named `AdministratorAccess` to the IAM group `Admins`. The users in that group are immediately affected by the permissions defined in the latest version of that policy.**

```
Register-IAMGroupPolicy -GroupName Admins -PolicyArn arn:aws:iam::aws:policy/AdministratorAccess

```

- For API details, see
  [AttachGroupPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
