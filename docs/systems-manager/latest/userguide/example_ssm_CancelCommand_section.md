AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `CancelCommand` with a CLI

The following code examples show how to use `CancelCommand`.

CLI

**AWS CLI**

**Example 1: To cancel a command for all instances**

The following `cancel-command` example attempts to cancel the specified command that is already running for all instances.

```
`aws ssm cancel-command \
 --command-id `"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"``

```

This command produces no output.

**Example 2: To cancel a command for specific instances**

The following `cancel-command` example attempts to cancel a command for the specified instance only.

```
`aws ssm cancel-command \
 --command-id `"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"`
 --instance-ids `"i-02573cafcfEXAMPLE"``

```

This command produces no output.

For more information, see [Tagging Systems Manager Parameters](sysman-paramstore-su-tag.md "sysman-paramstore-su-tag.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [CancelCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"

```

- For API details, see
  [CancelCommand](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attempts to cancel a command. There is no output if the operation succeeds.**

```
Stop-SSMCommand -CommandId "9ded293e-e792-4440-8e3e-7b8ec5feaa38"

```

- For API details, see
  [CancelCommand](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
