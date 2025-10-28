# Create and manage AWS Transit Gateway Flow Logs using APIs or the CLI

You can perform the tasks described on this page using the command line.

The following limitations apply when using the [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md") command:

- `--resource-ids` has a maximum constraint of 25
  `TransitGateway` or `TransitGatewayAttachment`
  resource types.
- `--traffic-type` is not a required field by default. An error
  is returned if you provide this for transit gateway resource types. This limit applies
  only to transit gateway resource types.
- `--max-aggregation-interval` has a default value of
  `60`, and is the only accepted value for transit gateway resource
  types. An error is returned if you try to pass any other value. This limit
  applies only to transit gateway resource types.
- `--resource-type` supports two new resource types,
  `TransitGateway` and
  `TransitGatewayAttachment`.
- `--log-format` includes all log fields for transit gateway resource types
  if you do not set which fields you want to include. This applies only to
  transit gateway resource types.

###### Create a flow log

- [create-flow-logs](../../../cli/latest/reference/ec2/create-flow-logs.md "../../../cli/latest/reference/ec2/create-flow-logs.md") (AWS CLI)
- [New-EC2FlowLog](../../../powershell/latest/reference/items/New-EC2FlowLog.md "../../../powershell/latest/reference/items/New-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)

###### Describe your flow logs

- [describe-flow-logs](../../../cli/latest/reference/ec2/describe-flow-logs.md "../../../cli/latest/reference/ec2/describe-flow-logs.md") (AWS CLI)
- [Get-EC2FlowLog](../../../powershell/latest/reference/items/Get-EC2FlowLog.md "../../../powershell/latest/reference/items/Get-EC2FlowLog.md")
  (AWS Tools for Windows PowerShell)

###### View your flow log records (log events)

- [get-log-events](../../../cli/latest/reference/logs/get-log-events.md "../../../cli/latest/reference/logs/get-log-events.md")
  (AWS CLI)
- [Get-CWLLogEvent](../../../powershell/latest/reference/items/Get-CWLLogEvent.md "../../../powershell/latest/reference/items/Get-CWLLogEvent.md") (AWS Tools for Windows PowerShell)

###### Delete a flow log

- [delete-flow-logs](../../../cli/latest/reference/ec2/delete-flow-logs.md "../../../cli/latest/reference/ec2/delete-flow-logs.md") (AWS CLI)
- [Remove-EC2FlowLog](../../../powershell/latest/reference/items/Remove-EC2FlowLog.md "../../../powershell/latest/reference/items/Remove-EC2FlowLog.md") (AWS Tools for Windows PowerShell)
