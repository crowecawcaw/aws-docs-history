

# Use `ListGroupsForUser` with a CLI
<a name="iam_example_iam_ListGroupsForUser_section"></a>

The following code examples show how to use `ListGroupsForUser`.

------
#### [ CLI ]

**AWS CLI**  
**To list the groups that an IAM user belongs to**  
The following `list-groups-for-user` command displays the groups that the IAM user named `Bob` belongs to.  

```
aws iam list-groups-for-user \
    --user-name {{Bob}}
```
Output:  

```
{
    "Groups": [
        {
            "Path": "/",
            "CreateDate": "2013-05-06T01:18:08Z",
            "GroupId": "AKIAIOSFODNN7EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/Admin",
            "GroupName": "Admin"
        },
        {
            "Path": "/",
            "CreateDate": "2013-05-06T01:37:28Z",
            "GroupId": "AKIAI44QH8DHBEXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/s3-Users",
            "GroupName": "s3-Users"
        }
    ]
}
```
For more information, see [Managing IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html) in the *AWS IAM User Guide*.  
+  For API details, see [ListGroupsForUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-groups-for-user.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns the list of IAM groups that the IAM user `David` belongs to.**  

```
Get-IAMGroupForUser -UserName David
```
**Output:**  

```
Arn        : arn:aws:iam::123456789012:group/Administrators
CreateDate : 10/20/2014 10:06:24 AM
GroupId    : 6WCH4TRY3KIHIEXAMPLE1
GroupName  : Administrators
Path       : /
      
Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : RHNZZGQJ7QHMAEXAMPLE2
GroupName  : Testers
Path       : /
      
Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 12/10/2014 3:38:55 PM
GroupId    : ZU2EOWMK6WBZOEXAMPLE3
GroupName  : Developers
Path       : /
```
+  For API details, see [ListGroupsForUser](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns the list of IAM groups that the IAM user `David` belongs to.**  

```
Get-IAMGroupForUser -UserName David
```
**Output:**  

```
Arn        : arn:aws:iam::123456789012:group/Administrators
CreateDate : 10/20/2014 10:06:24 AM
GroupId    : 6WCH4TRY3KIHIEXAMPLE1
GroupName  : Administrators
Path       : /
      
Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : RHNZZGQJ7QHMAEXAMPLE2
GroupName  : Testers
Path       : /
      
Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 12/10/2014 3:38:55 PM
GroupId    : ZU2EOWMK6WBZOEXAMPLE3
GroupName  : Developers
Path       : /
```
+  For API details, see [ListGroupsForUser](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.