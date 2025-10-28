# User passwords in AWS

You can manage passwords for IAM users in your account. IAM users need passwords in
order to access the AWS Management Console. Users do not need passwords to access AWS resources
programmatically by using the AWS CLI, Tools for Windows PowerShell, the AWS SDKs or APIs. For those environments, you
have the option of assigning IAM users [access
keys](id_credentials_access-keys.md "id_credentials_access-keys.md"). However, there are other more secure alternatives to access keys that we
recommend you consider first. For more information, see [AWS security credentials](security-creds.md "security-creds.md").

###### Note

If one of your IAM users
lose or forget their password, you _cannot_ retrieve them from IAM. Depending on your settings, either the user or the administrator must create a
new password.

###### Contents

- [Set an account password policy for
  IAM users](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md")
- [Manage passwords for
  IAM users](id_credentials_passwords_admin-change-user.md "id_credentials_passwords_admin-change-user.md")
- [Permit IAM users to change
  their own passwords](id_credentials_passwords_enable-user-change.md "id_credentials_passwords_enable-user-change.md")
- [How an IAM user changes their own
  password](id_credentials_passwords_user-change-own.md "id_credentials_passwords_user-change-own.md")
