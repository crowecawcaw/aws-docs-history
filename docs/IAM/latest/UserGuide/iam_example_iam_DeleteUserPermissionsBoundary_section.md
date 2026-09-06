

# Use `DeleteUserPermissionsBoundary` with a CLI
<a name="iam_example_iam_DeleteUserPermissionsBoundary_section"></a>

The following code examples show how to use `DeleteUserPermissionsBoundary`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a permissions boundary from an IAM user**  
The following `delete-user-permissions-boundary` example deletes the permissions boundary attached to the IAM user named `intern`. To apply a permissions boundary to a user, use the `put-user-permissions-boundary` command.  

```
aws iam delete-user-permissions-boundary \
    --user-name {{intern}}
```
This command produces no output.  
For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *AWS IAM User Guide*.  
+  For API details, see [DeleteUserPermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-permissions-boundary.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example shows how to remove the permission boundary attached to an IAM user.**  

```
Remove-IAMUserPermissionsBoundary -UserName joe
```
+  For API details, see [DeleteUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example shows how to remove the permission boundary attached to an IAM user.**  

```
Remove-IAMUserPermissionsBoundary -UserName joe
```
+  For API details, see [DeleteUserPermissionsBoundary](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.