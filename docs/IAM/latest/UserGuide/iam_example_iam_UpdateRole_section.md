

# Use `UpdateRole` with a CLI
<a name="iam_example_iam_UpdateRole_section"></a>

The following code examples show how to use `UpdateRole`.

------
#### [ CLI ]

**AWS CLI**  
**To change an IAM role's description or session duration**  
The following `update-role` command changes the description of the IAM role `production-role` to `Main production role` and sets the maximum session duration to 12 hours.  

```
aws iam update-role \
    --role-name {{production-role}} \
    --description '{{Main production role}}' \
    --max-session-duration {{43200}}
```
This command produces no output.  
For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html) in the *AWS IAM User Guide*.  
+  For API details, see [UpdateRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the role description and the maximum session duration value(in seconds) for which a role's session can be requested.**  

```
Update-IAMRole -RoleName MyRoleName -Description "My testing role" -MaxSessionDuration 43200
```
+  For API details, see [UpdateRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the role description and the maximum session duration value(in seconds) for which a role's session can be requested.**  

```
Update-IAMRole -RoleName MyRoleName -Description "My testing role" -MaxSessionDuration 43200
```
+  For API details, see [UpdateRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.