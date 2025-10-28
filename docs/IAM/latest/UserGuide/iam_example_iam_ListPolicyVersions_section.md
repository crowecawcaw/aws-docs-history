# Use `ListPolicyVersions` with a CLI

The following code examples show how to use `ListPolicyVersions`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code examples:

- [Manage policies](iam_example_iam_Scenario_PolicyManagement_section.md "iam_example_iam_Scenario_PolicyManagement_section.md")
- [Roll back a policy version](iam_example_iam_Scenario_RollbackPolicyVersion_section.md "iam_example_iam_Scenario_RollbackPolicyVersion_section.md")

CLI

**AWS CLI**

**To list information about the versions of the specified managed policy**

This example returns the list of available versions of the policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.

```
`aws iam list-policy-versions \
 --policy-arn `arn:aws:iam::123456789012:policy/MySamplePolicy``

```

Output:

```
{
    "IsTruncated": false,
    "Versions": [
        {
        "VersionId": "v2",
        "IsDefaultVersion": true,
        "CreateDate": "2015-06-02T23:19:44Z"
        },
        {
        "VersionId": "v1",
        "IsDefaultVersion": false,
        "CreateDate": "2015-06-02T22:30:47Z"
        }
    ]
}
```

For more information, see [Policies and permissions in IAM](access_policies.md "access_policies.md") in the _AWS IAM User Guide_.

- For API details, see
  [ListPolicyVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns the list of available versions of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyManagedPolicy`. To get the policy document for a specific version, use the `Get-IAMPolicyVersion` command and specify the `VersionId` of the one you want.**

```
Get-IAMPolicyVersionList -PolicyArn arn:aws:iam::123456789012:policy/MyManagedPolicy

```

**Output:**

```
CreateDate                   Document                 IsDefaultVersion                  VersionId
----------                   --------                 ----------------                  ---------
2/12/2015 9:39:53 AM                                  True                              v2
2/12/2015 9:39:09 AM                                  False                             v1
```

- For API details, see
  [ListPolicyVersions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns the list of available versions of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyManagedPolicy`. To get the policy document for a specific version, use the `Get-IAMPolicyVersion` command and specify the `VersionId` of the one you want.**

```
Get-IAMPolicyVersionList -PolicyArn arn:aws:iam::123456789012:policy/MyManagedPolicy

```

**Output:**

```
CreateDate                   Document                 IsDefaultVersion                  VersionId
----------                   --------                 ----------------                  ---------
2/12/2015 9:39:53 AM                                  True                              v2
2/12/2015 9:39:09 AM                                  False                             v1
```

- For API details, see
  [ListPolicyVersions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
