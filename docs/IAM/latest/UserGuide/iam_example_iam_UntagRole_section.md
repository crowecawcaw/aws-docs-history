

# Use `UntagRole` with a CLI
<a name="iam_example_iam_UntagRole_section"></a>

The following code examples show how to use `UntagRole`.

------
#### [ CLI ]

**AWS CLI**  
**To remove a tag from a role**  
The following `untag-role` command removes any tag with the key name 'Department' from the specified role.  

```
aws iam untag-role \
    --role-name {{my-role}} \
    --tag-keys {{Department}}
```
This command produces no output.  
For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *AWS IAM User Guide*.  
+  For API details, see [UntagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**  

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"
```
+  For API details, see [UntagRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**  

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"
```
+  For API details, see [UntagRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.