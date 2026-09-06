

# Use `ListUserTags` with a CLI
<a name="iam_example_iam_ListUserTags_section"></a>

The following code examples show how to use `ListUserTags`.

------
#### [ CLI ]

**AWS CLI**  
**To list the tags attached to a user**  
The following `list-user-tags` command retrieves the list of tags associated with the specified IAM user.  

```
aws iam list-user-tags \
    --user-name {{alice}}
```
Output:  

```
{
    "Tags": [
        {
            "Key": "Department",
            "Value": "Accounting"
        },
        {
            "Key": "DeptID",
            "Value": "12345"
        }
    ],
    "IsTruncated": false
}
```
For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *AWS IAM User Guide*.  
+  For API details, see [ListUserTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-tags.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example fetches the tag associated with the user.**  

```
Get-IAMUserTagList -UserName joe
```
+  For API details, see [ListUserTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example fetches the tag associated with the user.**  

```
Get-IAMUserTagList -UserName joe
```
+  For API details, see [ListUserTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.