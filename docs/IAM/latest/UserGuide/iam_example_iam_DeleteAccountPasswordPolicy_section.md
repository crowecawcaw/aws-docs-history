

# Use `DeleteAccountPasswordPolicy` with a CLI
<a name="iam_example_iam_DeleteAccountPasswordPolicy_section"></a>

The following code examples show how to use `DeleteAccountPasswordPolicy`.

------
#### [ CLI ]

**AWS CLI**  
**To delete the current account password policy**  
The following `delete-account-password-policy` command removes the password policy for the current account.  

```
aws iam delete-account-password-policy
```
This command produces no output.  
For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) in the *AWS IAM User Guide*.  
+  For API details, see [DeleteAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-password-policy.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**  

```
Remove-IAMAccountPasswordPolicy
```
+  For API details, see [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the password policy for the AWS account and resets all values to their original defaults. If a password policy does not currently exist, the following error message appears: The account policy with name PasswordPolicy cannot be found.**  

```
Remove-IAMAccountPasswordPolicy
```
+  For API details, see [DeleteAccountPasswordPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.