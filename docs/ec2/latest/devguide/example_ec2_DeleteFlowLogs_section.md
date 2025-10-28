# Use `DeleteFlowLogs` with a CLI

The following code examples show how to use `DeleteFlowLogs`.

CLI

**AWS CLI**

**To delete a flow log**

The following `delete-flow-logs` example deletes the specified flow log.

```
`aws ec2 delete-flow-logs --flow-log-id `fl-11223344556677889``

```

Output:

```
{
    "Unsuccessful": []
}
```

- For API details, see
  [DeleteFlowLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the given FlowLogId fl-01a2b3456a789c01**

```
Remove-EC2FlowLog -FlowLogId fl-01a2b3456a789c01

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2FlowLog (DeleteFlowLogs)" on target "fl-01a2b3456a789c01".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```

- For API details, see
  [DeleteFlowLogs](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the given FlowLogId fl-01a2b3456a789c01**

```
Remove-EC2FlowLog -FlowLogId fl-01a2b3456a789c01

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2FlowLog (DeleteFlowLogs)" on target "fl-01a2b3456a789c01".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```

- For API details, see
  [DeleteFlowLogs](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
