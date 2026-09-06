

# Use `TagUser` with a CLI
<a name="iam_example_iam_TagUser_section"></a>

The following code examples show how to use `TagUser`.

------
#### [ CLI ]

**AWS CLI**  
**To add a tag to a user**  
The following `tag-user` command adds a tag with the associated Department to the specified user.  

```
aws iam tag-user \
    --user-name {{alice}} \
    --tags '{{{"Key": "Department", "Value": "Accounting"}}}'
```
This command produces no output.  
For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *AWS IAM User Guide*.  
+  For API details, see [TagUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example adds tag to User in Identity Management Service**  

```
Add-IAMUserTag -UserName joe -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example adds tag to User in Identity Management Service**  

```
Add-IAMUserTag -UserName joe -Tag @{ Key = 'abac'; Value = 'testing'}
```
+  For API details, see [TagUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.