

# Use `AddUserToGroup` with a CLI
<a name="iam_example_iam_AddUserToGroup_section"></a>

The following code examples show how to use `AddUserToGroup`.

------
#### [ CLI ]

**AWS CLI**  
**To add a user to an IAM group**  
The following `add-user-to-group` command adds an IAM user named `Bob` to the IAM group named `Admins`.  

```
aws iam add-user-to-group \
    --user-name {{Bob}} \
    --group-name {{Admins}}
```
This command produces no output.  
For more information, see [Adding and removing users in an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html) in the *AWS IAM User Guide*.  
+  For API details, see [AddUserToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-user-to-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This command adds the user named `Bob` to the group named `Admins`.**  

```
Add-IAMUserToGroup -UserName "Bob" -GroupName "Admins"
```
+  For API details, see [AddUserToGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This command adds the user named `Bob` to the group named `Admins`.**  

```
Add-IAMUserToGroup -UserName "Bob" -GroupName "Admins"
```
+  For API details, see [AddUserToGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.