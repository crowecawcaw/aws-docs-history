AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `UpdateManagedInstanceRole` with a CLI

The following code examples show how to use `UpdateManagedInstanceRole`.

CLI

**AWS CLI**

**To update the IAM role of a managed instance**

The following `update-managed-instance-role` example updates the IAM instance profile of a managed instance.

```
`aws ssm update-managed-instance-role \
 --instance-id `"mi-08ab247cdfEXAMPLE"` \
 --iam-role `"ExampleRole"``

```

This command produces no output.

For more information, see [Step 4: Create an IAM Instance Profile for Systems Manager](setup-instance-profile.md "setup-instance-profile.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [UpdateManagedInstanceRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"

```

- For API details, see
  [UpdateManagedInstanceRole](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"

```

- For API details, see
  [UpdateManagedInstanceRole](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
