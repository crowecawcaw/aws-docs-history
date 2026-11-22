

# Create and manage AWS Cloud WAN Flow Logs using APIs or the CLI

You can perform the tasks described on this page using the command line.

The following limitations apply when using the [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) command:
+ `--resource-ids` has a maximum constraint of 25 `CoreNetwork`, `CoreNetworkEdge`, or `CoreNetworkAttachment` resource types. For `CoreNetworkEdge`, specify each resource ID in the format `{{core-network-id}}/{{region}}` (for example, `core-network-0123456789abcdef0/us-east-1`).
+ `--traffic-type` is not supported for Cloud WAN resource types. An error is returned if you provide this for core network resource types.
+ `--max-aggregation-interval` has a default value of `60`, and is the only accepted value for core network resource types. An error is returned if you try to pass any other value. This limit applies only to core network resource types. 
+ `--resource-type` supports the resource types `CoreNetwork`, `CoreNetworkEdge`, and `CoreNetworkAttachment`.
+ `--log-format` includes all log fields for core network resource types if you do not set which fields you want to include. This applies only to core network resource types.

**Create a flow log**
+ [create-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-flow-logs.html) (AWS CLI)
+ [New-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

**Describe your flow logs**
+ [describe-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-flow-logs.html) (AWS CLI)
+ [Get-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2FlowLog.html) (AWS Tools for Windows PowerShell)

**View your flow log records (log events)**
+ [get-log-events](https://docs.aws.amazon.com/cli/latest/reference/logs/get-log-events.html) (AWS CLI)
+ [Get-CWLLogEvent](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-CWLLogEvent.html) (AWS Tools for Windows PowerShell)

**Delete a flow log**
+ [delete-flow-logs](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-flow-logs.html) (AWS CLI)
+ [Remove-EC2FlowLog](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2FlowLog.html) (AWS Tools for Windows PowerShell)