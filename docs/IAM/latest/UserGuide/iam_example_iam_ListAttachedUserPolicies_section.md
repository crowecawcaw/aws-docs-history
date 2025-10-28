# Use `ListAttachedUserPolicies` with a CLI

The following code examples show how to use `ListAttachedUserPolicies`.

CLI

**AWS CLI**

**To list all managed policies that are attached to the specified user**

This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account.

```
`aws iam list-attached-user-policies \
 --user-name `Bob``

```

Output:

```
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "SecurityAudit",
            "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit"
        }
    ],
    "IsTruncated": false
}
```

For more information, see [Policies and permissions in IAM](access_policies.md "access_policies.md") in the _AWS IAM User Guide_.

- For API details, see
  [ListAttachedUserPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-user-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-user-policies.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account. To see the list of inline policies that are embedded in the IAM user, use the `Get-IAMUserPolicyList` command.**

```
Get-IAMAttachedUserPolicyList -UserName "Bob"

```

**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/TesterPolicy                      TesterPolicy
```

- For API details, see
  [ListAttachedUserPolicies](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command returns the names and ARNs of the managed policies for the IAM user named `Bob` in the AWS account. To see the list of inline policies that are embedded in the IAM user, use the `Get-IAMUserPolicyList` command.**

```
Get-IAMAttachedUserPolicyList -UserName "Bob"

```

**Output:**

```
PolicyArn                                                 PolicyName
---------                                                 ----------
arn:aws:iam::aws:policy/TesterPolicy                      TesterPolicy
```

- For API details, see
  [ListAttachedUserPolicies](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
