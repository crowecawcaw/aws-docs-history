

# Use `UpdateRoleDescription` with a CLI
<a name="iam_example_iam_UpdateRoleDescription_section"></a>

The following code examples show how to use `UpdateRoleDescription`.

------
#### [ CLI ]

**AWS CLI**  
**To change an IAM role's description**  
The following `update-role` command changes the description of the IAM role `production-role` to `Main production role`.  

```
aws iam update-role-description \
    --role-name {{production-role}} \
    --description '{{Main production role}}'
```
Output:  

```
{
    "Role": {
        "Path": "/",
        "RoleName": "production-role",
        "RoleId": "AROA1234567890EXAMPLE",
        "Arn": "arn:aws:iam::123456789012:role/production-role",
        "CreateDate": "2017-12-06T17:16:37+00:00",
        "AssumeRolePolicyDocument": {
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::123456789012:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {}
                }
            ]
        },
        "Description": "Main production role"
    }
}
```
For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) in the *AWS IAM User Guide*.  
+  For API details, see [UpdateRoleDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role-description.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the description of an IAM role in your account.**  

```
Update-IAMRoleDescription -RoleName MyRoleName -Description "My testing role"
```
+  For API details, see [UpdateRoleDescription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the description of an IAM role in your account.**  

```
Update-IAMRoleDescription -RoleName MyRoleName -Description "My testing role"
```
+  For API details, see [UpdateRoleDescription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.