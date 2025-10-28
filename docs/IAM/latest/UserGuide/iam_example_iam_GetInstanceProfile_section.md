# Use `GetInstanceProfile` with a CLI

The following code examples show how to use `GetInstanceProfile`.

CLI

**AWS CLI**

**To get information about an instance profile**

The following `get-instance-profile` command gets information about the instance profile named `ExampleInstanceProfile`.

```
`aws iam get-instance-profile \
 --instance-profile-name `ExampleInstanceProfile``

```

Output:

```
{
    "InstanceProfile": {
        "InstanceProfileId": "AID2MAB8DPLSRHEXAMPLE",
        "Roles": [
            {
                "AssumeRolePolicyDocument": "<URL-encoded-JSON>",
                "RoleId": "AIDGPMS9RO4H3FEXAMPLE",
                "CreateDate": "2013-01-09T06:33:26Z",
                "RoleName": "Test-Role",
                "Path": "/",
                "Arn": "arn:aws:iam::336924118301:role/Test-Role"
            }
        ],
        "CreateDate": "2013-06-12T23:52:02Z",
        "InstanceProfileName": "ExampleInstanceProfile",
        "Path": "/",
        "Arn": "arn:aws:iam::336924118301:instance-profile/ExampleInstanceProfile"
    }
}
```

For more information, see [Using instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-instance-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-instance-profile.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns details of the instance profile named `ec2instancerole` that is defined in the current AWS account.**

```
Get-IAMInstanceProfile -InstanceProfileName ec2instancerole

```

**Output:**

```
Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
CreateDate          : 2/17/2015 2:49:04 PM
InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
InstanceProfileName : ec2instancerole
Path                : /
Roles               : {ec2instancerole}
```

- For API details, see
  [GetInstanceProfile](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns details of the instance profile named `ec2instancerole` that is defined in the current AWS account.**

```
Get-IAMInstanceProfile -InstanceProfileName ec2instancerole

```

**Output:**

```
Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
CreateDate          : 2/17/2015 2:49:04 PM
InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
InstanceProfileName : ec2instancerole
Path                : /
Roles               : {ec2instancerole}
```

- For API details, see
  [GetInstanceProfile](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
