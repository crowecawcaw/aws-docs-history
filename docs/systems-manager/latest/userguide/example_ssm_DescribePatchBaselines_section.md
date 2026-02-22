• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `DescribePatchBaselines` with a CLI

The following code examples show how to use `DescribePatchBaselines`.

CLI

**AWS CLI**

**Example 1: To list all patch baselines**

The following `describe-patch-baselines` example retrieves details for all patch baselines in your account in the current Region.

```
`aws ssm describe-patch-baselines`

```

Output:

```
{
    "BaselineIdentities": [
        {
            "BaselineName": "AWS-SuseDefaultPatchBaseline",
            "DefaultBaseline": true,
            "BaselineDescription": "Default Patch Baseline for Suse Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0123fdb36e334a3b2",
            "OperatingSystem": "SUSE"
        },
        {
            "BaselineName": "AWS-DefaultPatchBaseline",
            "DefaultBaseline": false,
            "BaselineDescription": "Default Patch Baseline Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-020d361a05defe4ed",
            "OperatingSystem": "WINDOWS"
        },
        ...
        {
            "BaselineName": "MyWindowsPatchBaseline",
            "DefaultBaseline": true,
            "BaselineDescription": "My patch baseline for EC2 instances for Windows Server",
            "BaselineId": "pb-0ad00e0dd7EXAMPLE",
            "OperatingSystem": "WINDOWS"
        }
    ]
}
```

**Example 2: To list all patch baselines provided by AWS**

The following `describe-patch-baselines` example lists all patch baselines provided by AWS.

```
`aws ssm describe-patch-baselines \
 --filters `"Key=OWNER,Values=[AWS]"``

```

**Example 3: To list all patch baselines that you own**

The following `describe-patch-baselines` example lists all custom patch baselines created in your account in the current Region.

```
`aws ssm describe-patch-baselines \
 --filters `"Key=OWNER,Values=[Self]"``

```

For more information, see [About Predefined and Custom Patch Baselines](sysman-patch-baselines.md "sysman-patch-baselines.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribePatchBaselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-baselines.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-baselines.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists all patch baselines.**

```
Get-SSMPatchBaseline

```

**Output:**

```
BaselineDescription                                             BaselineId                                                            BaselineName
-------------------                                             ----------                                                            ------------
Default Patch Baseline Provided by AWS.                         arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultP...
Baseline containing all updates approved for production systems pb-045f10b4f382baeda                                                  Production-B...
Baseline containing all updates approved for production systems pb-0a2f1059b670ebd31                                                  Production-B...
```

**Example 2: This example lists all patch baselines provided by AWS. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("AWS")}

```

**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```

**Example 3: This example lists all patch baselines with you as the owner. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("Self")}

```

**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```

**Example 4: With PowerShell version 2, you must use New-Object to create each tag.**

```
$filter1 = New-Object Amazon.SimpleSystemsManagement.Model.PatchOrchestratorFilter
$filter1.Key = "OWNER"
$filter1.Values = "AWS"

Get-SSMPatchBaseline -Filter $filter1

```

**Output:**

```
BaselineDescription                     BaselineId                                                            BaselineName             DefaultBaselin
                                                                                                                                       e
-------------------                     ----------                                                            ------------             --------------
Default Patch Baseline Provided by AWS. arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultPatchBaseline True
```

- For API details, see
  [DescribePatchBaselines](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists all patch baselines.**

```
Get-SSMPatchBaseline

```

**Output:**

```
BaselineDescription                                             BaselineId                                                            BaselineName
-------------------                                             ----------                                                            ------------
Default Patch Baseline Provided by AWS.                         arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultP...
Baseline containing all updates approved for production systems pb-045f10b4f382baeda                                                  Production-B...
Baseline containing all updates approved for production systems pb-0a2f1059b670ebd31                                                  Production-B...
```

**Example 2: This example lists all patch baselines provided by AWS. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("AWS")}

```

**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```

**Example 3: This example lists all patch baselines with you as the owner. The syntax used by this example requires PowerShell version 3 or later.**

```
$filter1 = @{Key="OWNER";Values=@("Self")}

```

**Output:**

```
Get-SSMPatchBaseline -Filter $filter1
```

**Example 4: With PowerShell version 2, you must use New-Object to create each tag.**

```
$filter1 = New-Object Amazon.SimpleSystemsManagement.Model.PatchOrchestratorFilter
$filter1.Key = "OWNER"
$filter1.Values = "AWS"

Get-SSMPatchBaseline -Filter $filter1

```

**Output:**

```
BaselineDescription                     BaselineId                                                            BaselineName             DefaultBaselin
                                                                                                                                       e
-------------------                     ----------                                                            ------------             --------------
Default Patch Baseline Provided by AWS. arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966 AWS-DefaultPatchBaseline True
```

- For API details, see
  [DescribePatchBaselines](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
