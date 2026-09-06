

# Use `TagRole` with a CLI
<a name="iam_example_iam_TagRole_section"></a>

The following code examples show how to use `TagRole`.

------
#### [ CLI ]

**AWS CLI**  
**To add a tag to a role**  
The following `tag-role` command adds a tag with a Department name to the specified role.  

```
aws iam tag-role --role-name {{my-role}} \
    --tags '{{{"Key": "Department", "Value": "Accounting"}}}'
```
This command produces no output.  
For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *AWS IAM User Guide*.  
+  For API details, see [TagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example adds tag to Role in Identity Management Service**  

```
Add-IAMRoleTag -RoleName AdminRoleacess -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example adds tag to Role in Identity Management Service**  

```
Add-IAMRoleTag -RoleName AdminRoleacess -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.