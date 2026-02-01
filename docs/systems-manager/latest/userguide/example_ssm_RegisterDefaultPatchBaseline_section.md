• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `RegisterDefaultPatchBaseline` with a CLI

The following code examples show how to use `RegisterDefaultPatchBaseline`.

CLI

**AWS CLI**

**To set the default patch baseline**

The following `register-default-patch-baseline` example registers the specified custom patch baseline as the default patch baseline for the operating system type that it supports.

```
`aws ssm register-default-patch-baseline \
 --baseline-id `"pb-abc123cf9bEXAMPLE"``

```

Output:

```
{
    "BaselineId":"pb-abc123cf9bEXAMPLE"
}
```

The following `register-default-patch-baseline` example registers the default patch baseline provided by AWS for CentOS as the default patch baseline.

```
`aws ssm register-default-patch-baseline \
 --baseline-id `"arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed"``

```

Output:

```
{
    "BaselineId":"pb-abc123cf9bEXAMPLE"
}
```

For more information, see [About Predefined and Custom Patch Baselines](sysman-patch-baselines.md "sysman-patch-baselines.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [RegisterDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-default-patch-baseline.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-default-patch-baseline.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example registers a patch baseline as the default patch baseline.**

```
Register-SSMDefaultPatchBaseline -BaselineId "pb-03da896ca3b68b639"

```

**Output:**

```
pb-03da896ca3b68b639
```

- For API details, see
  [RegisterDefaultPatchBaseline](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example registers a patch baseline as the default patch baseline.**

```
Register-SSMDefaultPatchBaseline -BaselineId "pb-03da896ca3b68b639"

```

**Output:**

```
pb-03da896ca3b68b639
```

- For API details, see
  [RegisterDefaultPatchBaseline](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
