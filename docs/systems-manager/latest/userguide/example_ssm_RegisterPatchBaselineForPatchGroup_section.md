• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `RegisterPatchBaselineForPatchGroup` with a CLI

The following code examples show how to use `RegisterPatchBaselineForPatchGroup`.

CLI

**AWS CLI**

**To register a patch baseline for a patch group**

The following `register-patch-baseline-for-patch-group` example registers a patch baseline for a patch group.

```
`aws ssm register-patch-baseline-for-patch-group \
 --baseline-id `"pb-045f10b4f382baeda"` \
 --patch-group `"Production"``

```

Output:

```
{
    "BaselineId": "pb-045f10b4f382baeda",
    "PatchGroup": "Production"
}
```

For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>\_\_ and [Add a Patch Group to a Patch Baseline](sysman-patch-group-patchbaseline.md "sysman-patch-group-patchbaseline.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [RegisterPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example registers a patch baseline for a patch group.**

```
Register-SSMPatchBaselineForPatchGroup -BaselineId "pb-03da896ca3b68b639" -PatchGroup "Production"

```

**Output:**

```
BaselineId           PatchGroup
----------           ----------
pb-03da896ca3b68b639 Production
```

- For API details, see
  [RegisterPatchBaselineForPatchGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example registers a patch baseline for a patch group.**

```
Register-SSMPatchBaselineForPatchGroup -BaselineId "pb-03da896ca3b68b639" -PatchGroup "Production"

```

**Output:**

```
BaselineId           PatchGroup
----------           ----------
pb-03da896ca3b68b639 Production
```

- For API details, see
  [RegisterPatchBaselineForPatchGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
