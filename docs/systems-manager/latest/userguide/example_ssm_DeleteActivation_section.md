AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DeleteActivation` with a CLI

The following code examples show how to use `DeleteActivation`.

CLI

**AWS CLI**

**To delete a managed instance activation**

The following `delete-activation` example deletes a managed instance activation.

```
`aws ssm delete-activation \
 --activation-id `"aa673477-d926-42c1-8757-1358cEXAMPLE"``

```

This command produces no output.

For more information, see [Setting Up AWS Systems Manager for Hybrid Environments](systems-manager-managedinstances.md "systems-manager-managedinstances.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeleteActivation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes an activation. There is no output if the command succeeds.**

```
Remove-SSMActivation -ActivationId "08e51e79-1e36-446c-8e63-9458569c1363"

```

- For API details, see
  [DeleteActivation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes an activation. There is no output if the command succeeds.**

```
Remove-SSMActivation -ActivationId "08e51e79-1e36-446c-8e63-9458569c1363"

```

- For API details, see
  [DeleteActivation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
