

# Use `GetLoginProfile` with a CLI
<a name="iam_example_iam_GetLoginProfile_section"></a>

The following code examples show how to use `GetLoginProfile`.

------
#### [ CLI ]

**AWS CLI**  
**To get password information for an IAM user**  
The following `get-login-profile` command gets information about the password for the IAM user named `Bob`.  

```
aws iam get-login-profile \
    --user-name {{Bob}}
```
Output:  

```
{
    "LoginProfile": {
        "UserName": "Bob",
        "CreateDate": "2012-09-21T23:03:39Z"
    }
}
```
The `get-login-profile` command can be used to verify that an IAM user has a password. The command returns a `NoSuchEntity` error if no password is defined for the user.  
You cannot view a password using this command. If the password is lost, you can reset the password (`update-login-profile`) for the user. Alternatively, you can delete the login profile (`delete-login-profile`) for the user and then create a new one (`create-login-profile`).  
For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html) in the *AWS IAM User Guide*.  
+  For API details, see [GetLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns the password creation date and whether a password reset is required for the IAM user `David`.**  

```
Get-IAMLoginProfile -UserName David
```
**Output:**  

```
CreateDate                   PasswordResetRequired                 UserName
----------                   ---------------------                 --------
12/10/2014 3:39:44 PM        False                                 David
```
+  For API details, see [GetLoginProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns the password creation date and whether a password reset is required for the IAM user `David`.**  

```
Get-IAMLoginProfile -UserName David
```
**Output:**  

```
CreateDate                   PasswordResetRequired                 UserName
----------                   ---------------------                 --------
12/10/2014 3:39:44 PM        False                                 David
```
+  For API details, see [GetLoginProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.