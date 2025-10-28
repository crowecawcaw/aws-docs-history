# Use `ListGroupPolicies` with a CLI

The following code examples show how to use `ListGroupPolicies`.

CLI

**AWS CLI**

**To list all inline policies that are attached to the specified group**

The following `list-group-policies` command lists the names of inline policies that are attached to the IAM group named
`Admins` in the current account.

```
`aws iam list-group-policies \
 --group-name `Admins``

```

Output:

```
{
    "PolicyNames": [
        "AdminRoot",
        "ExamplePolicy"
    ]
}
```

For more information, see [Managing IAM policies](access_policies_manage.md "access_policies_manage.md") in the _AWS IAM User Guide_.

- For API details, see
  [ListGroupPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns a list of the inline policies that are embedded in the group `Testers`. To get the managed policies that are attached to the group, use the command `Get-IAMAttachedGroupPolicyList`.**

```
Get-IAMGroupPolicyList -GroupName Testers

```

**Output:**

```
Deny-Assume-S3-Role-In-Production
PowerUserAccess-Testers
```

- For API details, see
  [ListGroupPolicies](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns a list of the inline policies that are embedded in the group `Testers`. To get the managed policies that are attached to the group, use the command `Get-IAMAttachedGroupPolicyList`.**

```
Get-IAMGroupPolicyList -GroupName Testers

```

**Output:**

```
Deny-Assume-S3-Role-In-Production
PowerUserAccess-Testers
```

- For API details, see
  [ListGroupPolicies](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
