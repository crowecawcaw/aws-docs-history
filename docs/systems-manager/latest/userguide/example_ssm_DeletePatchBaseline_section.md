AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DeletePatchBaseline` with a CLI

The following code examples show how to use `DeletePatchBaseline`.

CLI

**AWS CLI**

**To delete a patch baseline**

The following `delete-patch-baseline` example deletes the specified patch baseline.

```
`aws ssm delete-patch-baseline \
 --baseline-id `"pb-045f10b4f382baeda"``

```

Output:

```
{
    "BaselineId": "pb-045f10b4f382baeda"
}
```

For more information, see [Update or Delete a Patch Baseline (Console)](patch-baseline-update-or-delete.md "patch-baseline-update-or-delete.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeletePatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes a patch baseline.**

```
Remove-SSMPatchBaseline -BaselineId "pb-045f10b4f382baeda"

```

**Output:**

```
pb-045f10b4f382baeda
```

- For API details, see
  [DeletePatchBaseline](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes a patch baseline.**

```
Remove-SSMPatchBaseline -BaselineId "pb-045f10b4f382baeda"

```

**Output:**

```
pb-045f10b4f382baeda
```

- For API details, see
  [DeletePatchBaseline](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
