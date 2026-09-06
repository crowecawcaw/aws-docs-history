

# Use `PutRolePermissionsBoundary` with a CLI
<a name="iam_example_iam_PutRolePermissionsBoundary_section"></a>

The following code examples show how to use `PutRolePermissionsBoundary`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To apply a permissions boundary based on a custom policy to an IAM role**  
The following `put-role-permissions-boundary` example applies the custom policy named `intern-boundary` as the permissions boundary for the specified IAM role.  

```
aws iam put-role-permissions-boundary \
    --permissions-boundary {{arn:aws:iam::123456789012:policy/intern-boundary}} \
    --role-name {{lambda-application-role}}
```
This command produces no output.  
**Example 2: To apply a permissions boundary based on an AWS managed policy to an IAM role**  
The following `put-role-permissions-boundary` example applies the AWS managed `PowerUserAccess` policy as the permissions boundary for the specified IAM role.  

```
aws iam put-role-permissions-boundary \
    --permissions-boundary {{arn:aws:iam::aws:policy/PowerUserAccess}} \
    --role-name {{x-account-admin}}
```
This command produces no output.  
For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) in the *AWS IAM User Guide*.  
+  For API details, see [PutRolePermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-permissions-boundary.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example shows how to set the Permission boundary for a IAM Role. You can set AWS Managed policies or Custom policies as permission boundary.**  

```
Set-IAMRolePermissionsBoundary -RoleName MyRoleName -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example shows how to set the Permission boundary for a IAM Role. You can set AWS Managed policies or Custom policies as permission boundary.**  

```
Set-IAMRolePermissionsBoundary -RoleName MyRoleName -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary
```
+  For API details, see [PutRolePermissionsBoundary](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.