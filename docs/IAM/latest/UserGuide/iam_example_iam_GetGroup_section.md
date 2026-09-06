

# Use `GetGroup` with a CLI
<a name="iam_example_iam_GetGroup_section"></a>

The following code examples show how to use `GetGroup`.

------
#### [ CLI ]

**AWS CLI**  
**To get an IAM group**  
This example returns details about the IAM group `Admins`.  

```
aws iam get-group \
    --group-name {{Admins}}
```
Output:  

```
{
    "Group": {
        "Path": "/",
        "CreateDate": "2015-06-16T19:41:48Z",
        "GroupId": "AIDGPMS9RO4H3FEXAMPLE",
        "Arn": "arn:aws:iam::123456789012:group/Admins",
        "GroupName": "Admins"
    },
    "Users": []
}
```
For more information, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *AWS IAM User Guide*.  
+  For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns details about the IAM group `Testers`, including a collection of all the IAM users that belong to the group. **  

```
$results = Get-IAMGroup -GroupName "Testers"
$results
```
**Output:**  

```
Group                                     IsTruncated           Marker                Users
-----                                     -----------           ------                -----
Amazon.IdentityManagement.Model.Group     False                                       {Theresa, David}
```

```
$results.Group
```
**Output:**  

```
Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : 3RHNZZGQJ7QHMAEXAMPLE1
GroupName  : Testers
Path       : /
```

```
$results.Users
```
**Output:**  

```
Arn              : arn:aws:iam::123456789012:user/Theresa
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 1/1/0001 12:00:00 AM
Path             : /
UserId           : 4OSVDDJJTF4XEEXAMPLE2
UserName         : Theresa

Arn              : arn:aws:iam::123456789012:user/David
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 3/19/2015 8:44:04 AM
Path             : /
UserId           : Y4FKWQCXTA52QEXAMPLE3
UserName         : David
```
+  For API details, see [GetGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns details about the IAM group `Testers`, including a collection of all the IAM users that belong to the group. **  

```
$results = Get-IAMGroup -GroupName "Testers"
$results
```
**Output:**  

```
Group                                     IsTruncated           Marker                Users
-----                                     -----------           ------                -----
Amazon.IdentityManagement.Model.Group     False                                       {Theresa, David}
```

```
$results.Group
```
**Output:**  

```
Arn        : arn:aws:iam::123456789012:group/Testers
CreateDate : 12/10/2014 3:39:11 PM
GroupId    : 3RHNZZGQJ7QHMAEXAMPLE1
GroupName  : Testers
Path       : /
```

```
$results.Users
```
**Output:**  

```
Arn              : arn:aws:iam::123456789012:user/Theresa
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 1/1/0001 12:00:00 AM
Path             : /
UserId           : 4OSVDDJJTF4XEEXAMPLE2
UserName         : Theresa

Arn              : arn:aws:iam::123456789012:user/David
CreateDate       : 12/10/2014 3:39:27 PM
PasswordLastUsed : 3/19/2015 8:44:04 AM
Path             : /
UserId           : Y4FKWQCXTA52QEXAMPLE3
UserName         : David
```
+  For API details, see [GetGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.