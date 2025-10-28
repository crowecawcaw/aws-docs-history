# Use `UpdateLoginProfile` with a CLI

The following code examples show how to use `UpdateLoginProfile`.

CLI

**AWS CLI**

**To update the password for an IAM user**

The following `update-login-profile` command creates a new password for the IAM user named `Bob`.

```
`aws iam update-login-profile \
 --user-name `Bob` \
 --password `<password>``

```

This command produces no output.

To set a password policy for the account, use the `update-account-password-policy` command. If the new password
violates the account password policy, the command returns a `PasswordPolicyViolation` error.

If the account password policy allows them to, IAM users can change their own passwords using the `change-password` command.

Store the password in a secure place. If the password is lost, it cannot be recovered, and you must create a new one using the `create-login-profile` command.

For more information, see [Managing passwords for IAM users](id_credentials_passwords_admin-change-user.md "id_credentials_passwords_admin-change-user.md") in the _AWS IAM User Guide_.

- For API details, see
  [UpdateLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example sets a new temporary password for the IAM user `Bob`, and requires the user to change the password the next time the user signs in.**

```
Update-IAMLoginProfile -UserName Bob -Password "P@ssw0rd1234" -PasswordResetRequired $true

```

- For API details, see
  [UpdateLoginProfile](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example sets a new temporary password for the IAM user `Bob`, and requires the user to change the password the next time the user signs in.**

```
Update-IAMLoginProfile -UserName Bob -Password "P@ssw0rd1234" -PasswordResetRequired $true

```

- For API details, see
  [UpdateLoginProfile](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
