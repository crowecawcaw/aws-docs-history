

# User passwords in AWS
<a name="id_credentials_passwords"></a>

You can manage passwords for IAM users in your account. IAM users need passwords in order to access the AWS Management Console. Users do not need passwords to access AWS resources programmatically by using the AWS CLI, Tools for Windows PowerShell, the AWS SDKs or APIs. For those environments, you have the option of assigning IAM users [access keys](id_credentials_access-keys.md). However, there are other more secure alternatives to access keys that we recommend you consider first. For more information, see [AWS security credentials](security-creds.md).

**Note**  
If one of your IAM users loses or forgets their password, you *cannot* retrieve it from IAM. Depending on your settings, either the user or the administrator must create a new password.

**Topics**
+ [Set an account password policy for IAM users](id_credentials_passwords_account-policy.md)
+ [Manage passwords for IAM users](id_credentials_passwords_admin-change-user.md)
+ [Permit IAM users to change their own passwords](id_credentials_passwords_enable-user-change.md)
+ [How an IAM user changes their own password](id_credentials_passwords_user-change-own.md)