• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `DescribeEffectivePatchesForPatchBaseline` with a CLI

The following code examples show how to use `DescribeEffectivePatchesForPatchBaseline`.

CLI

**AWS CLI**

**Example 1: To get all patches defined by a custom patch baseline**

The following `describe-effective-patches-for-patch-baseline` example returns the patches defined by a custom patch baseline in the current AWS account. Note that for a custom baseline, only the ID is required for `--baseline-id`.

```
`aws ssm describe-effective-patches-for-patch-baseline \
 --baseline-id `"pb-08b654cf9b9681f04"``

```

Output:

```
{
    "EffectivePatches": [
        {
            "Patch": {
                "Id": "fe6bd8c2-3752-4c8b-ab3e-1a7ed08767ba",
                "ReleaseDate": 1544047205.0,
                "Title": "2018-11 Update for Windows Server 2019 for x64-based Systems (KB4470788)",
                "Description": "Install this update to resolve issues in Windows. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article for more information. After you install this item, you may have to restart your computer.",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/4470788",
                "Vendor": "Microsoft",
                "ProductFamily": "Windows",
                "Product": "WindowsServer2019",
                "Classification": "SecurityUpdates",
                "MsrcSeverity": "Critical",
                "KbNumber": "KB4470788",
                "MsrcNumber": "",
                "Language": "All"
            },
            "PatchStatus": {
                "DeploymentStatus": "APPROVED",
                "ComplianceLevel": "CRITICAL",
                "ApprovalDate": 1544047205.0
            }
        },
        {
            "Patch": {
                "Id": "915a6b1a-f556-4d83-8f50-b2e75a9a7e58",
                "ReleaseDate": 1549994400.0,
                "Title": "2019-02 Cumulative Update for .NET Framework 3.5 and 4.7.2 for Windows Server 2019 for x64 (KB4483452)",
                "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/4483452",
                "Vendor": "Microsoft",
                "ProductFamily": "Windows",
                "Product": "WindowsServer2019",
                "Classification": "SecurityUpdates",
                "MsrcSeverity": "Important",
                "KbNumber": "KB4483452",
                "MsrcNumber": "",
                "Language": "All"
            },
            "PatchStatus": {
                "DeploymentStatus": "APPROVED",
                "ComplianceLevel": "CRITICAL",
                "ApprovalDate": 1549994400.0
            }
        },
        ...
    ],
    "NextToken": "--token string truncated--"
}
```

**Example 2: To get all patches defined by an AWS managed patch baseline**

The following `describe-effective-patches-for-patch-baseline` example returns the patches defined by an AWS managed patch baseline. Note that for an AWS managed baseline, the complete baseline ARN is required for `--baseline-id`

```
`aws ssm describe-effective-patches-for-patch-baseline \
 --baseline-id `"arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-020d361a05defe4ed"``

```

See example 1 for sample output.

For more information, see [How Security Patches Are Selected](patch-manager-how-it-works-selection.md "patch-manager-how-it-works-selection.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeEffectivePatchesForPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-patches-for-patch-baseline.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-patches-for-patch-baseline.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all patch baselines, with a maximum result list of 1.**

```
Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1

```

**Output:**

```
Patch                                      PatchStatus
-----                                      -----------
Amazon.SimpleSystemsManagement.Model.Patch Amazon.SimpleSystemsManagement.Model.PatchStatus
```

**Example 2: This example displays the patch status for all patch baselines, with a maximum result list of 1.**

```
(Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1).PatchStatus

```

**Output:**

```
ApprovalDate          DeploymentStatus
------------          ----------------
12/21/2010 6:00:00 PM APPROVED
```

- For API details, see
  [DescribeEffectivePatchesForPatchBaseline](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all patch baselines, with a maximum result list of 1.**

```
Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1

```

**Output:**

```
Patch                                      PatchStatus
-----                                      -----------
Amazon.SimpleSystemsManagement.Model.Patch Amazon.SimpleSystemsManagement.Model.PatchStatus
```

**Example 2: This example displays the patch status for all patch baselines, with a maximum result list of 1.**

```
(Get-SSMEffectivePatchesForPatchBaseline -BaselineId "pb-0a2f1059b670ebd31" -MaxResult 1).PatchStatus

```

**Output:**

```
ApprovalDate          DeploymentStatus
------------          ----------------
12/21/2010 6:00:00 PM APPROVED
```

- For API details, see
  [DescribeEffectivePatchesForPatchBaseline](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
