# Use `UpdateAccountPasswordPolicy` with a CLI

The following code examples show how to use `UpdateAccountPasswordPolicy`.

CLI

**AWS CLI**

**To set or change the current account password policy**

The following `update-account-password-policy` command sets the password policy to require a minimum length of eight
characters and to require one or more numbers in the password.

```
`aws iam update-account-password-policy \
 --minimum-password-length `8` \
 --require-numbers`

```

This command produces no output.

Changes to an account's password policy affect any new passwords that are created for IAM users in the account. Password
policy changes do not affect existing passwords.

For more information, see [Setting an account password policy for IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md") in the _AWS IAM User Guide_.

- For API details, see
  [UpdateAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-account-password-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-account-password-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates the password policy for the account with the specified settings. Note that any parameters that are not included in the command are not left unmodified. Instead, they are reset to default values.**

```
Update-IAMAccountPasswordPolicy -AllowUsersToChangePasswords $true -HardExpiry $false -MaxPasswordAge 90 -MinimumPasswordLength 8 -PasswordReusePrevention 20 -RequireLowercaseCharacters $true -RequireNumbers $true -RequireSymbols $true -RequireUppercaseCharacters $true

```

- For API details, see
  [UpdateAccountPasswordPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates the password policy for the account with the specified settings. Note that any parameters that are not included in the command are not left unmodified. Instead, they are reset to default values.**

```
Update-IAMAccountPasswordPolicy -AllowUsersToChangePasswords $true -HardExpiry $false -MaxPasswordAge 90 -MinimumPasswordLength 8 -PasswordReusePrevention 20 -RequireLowercaseCharacters $true -RequireNumbers $true -RequireSymbols $true -RequireUppercaseCharacters $true

```

- For API details, see
  [UpdateAccountPasswordPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
