

# Use `UpdateLoginProfile` with a CLI
<a name="iam_example_iam_UpdateLoginProfile_section"></a>

The following code examples show how to use `UpdateLoginProfile`.

------
#### [ CLI ]

**AWS CLI**  
**To update the password for an IAM user**  
The following `update-login-profile` command creates a new password for the IAM user named `Bob`.  

```
aws iam update-login-profile \
    --user-name {{Bob}} \
    --password {{<password>}}
```
This command produces no output.  
To set a password policy for the account, use the `update-account-password-policy` command. If the new password violates the account password policy, the command returns a `PasswordPolicyViolation` error.  
If the account password policy allows them to, IAM users can change their own passwords using the `change-password` command.  
Store the password in a secure place. If the password is lost, it cannot be recovered, and you must create a new one using the `create-login-profile` command.  
For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html) in the *AWS IAM User Guide*.  
+  For API details, see [UpdateLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example sets a new temporary password for the IAM user `Bob`, and requires the user to change the password the next time the user signs in.**  

```
Update-IAMLoginProfile -UserName Bob -Password "P@ssw0rd1234" -PasswordResetRequired $true
```
+  For API details, see [UpdateLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example sets a new temporary password for the IAM user `Bob`, and requires the user to change the password the next time the user signs in.**  

```
Update-IAMLoginProfile -UserName Bob -Password "P@ssw0rd1234" -PasswordResetRequired $true
```
+  For API details, see [UpdateLoginProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.