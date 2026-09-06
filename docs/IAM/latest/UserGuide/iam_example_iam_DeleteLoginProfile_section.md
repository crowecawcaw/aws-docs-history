

# Use `DeleteLoginProfile` with a CLI
<a name="iam_example_iam_DeleteLoginProfile_section"></a>

The following code examples show how to use `DeleteLoginProfile`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a password for an IAM user**  
The following `delete-login-profile` command deletes the password for the IAM user named `Bob`.  

```
aws iam delete-login-profile \
    --user-name {{Bob}}
```
This command produces no output.  
For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html) in the *AWS IAM User Guide*.  
+  For API details, see [DeleteLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the login profile from the IAM user named `Bob`. This prevents the user from signing-in to the AWS console. It does not prevent the user from running any AWS CLI, PowerShell, or API calls using AWS access keys that might still be attached to the user account.**  

```
Remove-IAMLoginProfile -UserName Bob
```
+  For API details, see [DeleteLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the login profile from the IAM user named `Bob`. This prevents the user from signing-in to the AWS console. It does not prevent the user from running any AWS CLI, PowerShell, or API calls using AWS access keys that might still be attached to the user account.**  

```
Remove-IAMLoginProfile -UserName Bob
```
+  For API details, see [DeleteLoginProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.