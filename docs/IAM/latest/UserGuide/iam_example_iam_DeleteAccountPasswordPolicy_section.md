# Use `DeleteAccountPasswordPolicy` with a CLI

The following code examples show how to use `DeleteAccountPasswordPolicy`.

CLI

**AWS CLI**

**To delete the current account password policy**

The following `delete-account-password-policy` command removes the password policy for the current account.

```
`aws iam delete-account-password-policy`

```

This command produces no output.

For more information, see [Setting an account password policy for IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-password-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-password-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**

```
Remove-IAMAccountPasswordPolicy

```

- For API details, see
  [DeleteAccountPasswordPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**

```
Remove-IAMAccountPasswordPolicy

```

- For API details, see
  [DeleteAccountPasswordPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
