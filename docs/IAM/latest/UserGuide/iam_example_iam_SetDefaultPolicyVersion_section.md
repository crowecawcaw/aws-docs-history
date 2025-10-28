# Use `SetDefaultPolicyVersion` with a CLI

The following code examples show how to use `SetDefaultPolicyVersion`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Manage policies](iam_example_iam_Scenario_PolicyManagement_section.md "iam_example_iam_Scenario_PolicyManagement_section.md")
- [Roll back a policy version](iam_example_iam_Scenario_RollbackPolicyVersion_section.md "iam_example_iam_Scenario_RollbackPolicyVersion_section.md")

CLI

**AWS CLI**

**To set the specified version of the specified policy as the policy's default version.**

This example sets the `v2` version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyPolicy` as the default active version.

```
`aws iam set-default-policy-version \
 --policy-arn `arn:aws:iam::123456789012:policy/MyPolicy` \
 --version-id `v2``

```

For more information, see [Policies and permissions in IAM](access_policies.md "access_policies.md") in the _AWS IAM User Guide_.

- For API details, see
  [SetDefaultPolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/set-default-policy-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/set-default-policy-version.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example sets the `v2` version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyPolicy` as the default active version.**

```
Set-IAMDefaultPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MyPolicy -VersionId v2

```

- For API details, see
  [SetDefaultPolicyVersion](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example sets the `v2` version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyPolicy` as the default active version.**

```
Set-IAMDefaultPolicyVersion -PolicyArn arn:aws:iam::123456789012:policy/MyPolicy -VersionId v2

```

- For API details, see
  [SetDefaultPolicyVersion](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
