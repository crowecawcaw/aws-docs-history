# Use `DeregisterManagedInstance` with a CLI

The following code examples show how to use `DeregisterManagedInstance`.

CLI

**AWS CLI**

**To deregister a managed instance**

The following `deregister-managed-instance` example deregisters the specified managed instance.

```
`aws ssm deregister-managed-instance \
 --instance-id '`mi-08ab247cdfEXAMPLE`'`

```

This command produces no output.

For more information, see [Deregistering managed nodes in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeregisterManagedInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-managed-instance.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-managed-instance.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"

```

- For API details, see
  [DeregisterManagedInstance](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deregisters a managed instance. There is no output if the command succeeds.**

```
Unregister-SSMManagedInstance -InstanceId "mi-08ab247cdf1046573"

```

- For API details, see
  [DeregisterManagedInstance](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
