# Use `PutGroupPolicy` with a CLI

The following code examples show how to use `PutGroupPolicy`.

CLI

**AWS CLI**

**To add a policy to a group**

The following `put-group-policy` command adds a policy to the IAM group named `Admins`.

```
`aws iam put-group-policy \
 --group-name `Admins` \
 --policy-document `file://AdminPolicy.json` \
 --policy-name `AdminRoot``

```

This command produces no output.

The policy is defined as a JSON document in the _AdminPolicy.json_ file. (The file name and extension do not have
significance.)

For more information, see [Managing IAM policies](access_policies_manage.md "access_policies_manage.md") in the _AWS IAM User Guide_.

- For API details, see
  [PutGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates an inline policy named `AppTesterPolicy` and embeds it in the IAM group `AppTesters`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes the file `apptesterpolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMGroupPolicy -GroupName AppTesters -PolicyName AppTesterPolicy -PolicyDocument (Get-Content -Raw apptesterpolicy.json)

```

- For API details, see
  [PutGroupPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates an inline policy named `AppTesterPolicy` and embeds it in the IAM group `AppTesters`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes the file `apptesterpolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMGroupPolicy -GroupName AppTesters -PolicyName AppTesterPolicy -PolicyDocument (Get-Content -Raw apptesterpolicy.json)

```

- For API details, see
  [PutGroupPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
