# View states for Amazon EC2 High Availability for SQL Server

You can view the Amazon EC2 High Availability for SQL Server (SQL HA) current and historical states. Use one of the following
methods:

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances**.
3. Select the instances in the High Availability deployment for which to view the SQL HA
   states, then choose the **SQL High Availability** tab.

AWS CLI
To view the current SQL HA states for Amazon EC2 instances, use the [describe-instance-sql-ha-states](../../../cli/latest/reference/ec2/describe-instance-sql-ha-states.md "../../../cli/latest/reference/ec2/describe-instance-sql-ha-states.md")
command. This command returns only the instances that are currently enabled for SQL HA
standby detection. If any instance ID that you specify is not currently enabled, the entire
request fails and no states are returned.

```
aws ec2 describe-instance-sql-ha-states \
--instance-ids `i-1234567890abcdef0` `i-0fedcba0987654321`
```

To view the historical SQL HA states for instances, use the [describe-instance-sql-ha-history-states](../../../cli/latest/reference/ec2/describe-instance-sql-ha-history-states.md "../../../cli/latest/reference/ec2/describe-instance-sql-ha-history-states.md") command. This command returns your SQL HA instance
state transitions in descending time order. Specify `--start-time` and
`--end-time` in UTC, using the ISO 8601 format
`YYYY-MM-DDThh:mm:ssZ`.

```
aws ec2 describe-instance-sql-ha-history-states \
--instance-ids `i-1234567890abcdef0` `i-0fedcba0987654321` \
--start-time `2026-08-01T00:00:00Z` \
--end-time `2026-08-24T00:00:00Z`
```

You can run these commands from [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"), which comes with the [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md")
pre-installed.

PowerShell
To view the current SQL HA states for Amazon EC2 instances, use the [Get-EC2InstanceSqlHaState](../../../powershell/latest/reference/items/Get-EC2InstanceSqlHaState.md "../../../powershell/latest/reference/items/Get-EC2InstanceSqlHaState.md")
cmdlet. This cmdlet returns only the instances that are currently enabled for SQL HA
standby detection. If any instance ID that you specify is not currently enabled, the entire
request fails and no states are returned.

```
Get-EC2InstanceSqlHaState `
-InstanceId '`i-1234567890abcdef0`','`i-0fedcba0987654321`'
```

To view the historical SQL HA states for instances, use the [Get-EC2InstanceSqlHaHistoryState](../../../powershell/latest/reference/items/Get-EC2InstanceSqlHaHistoryState.md "../../../powershell/latest/reference/items/Get-EC2InstanceSqlHaHistoryState.md") cmdlet. This cmdlet returns your SQL HA instance
state transitions in descending time order. Specify `-StartTime` and
`-EndTime` in UTC, using the ISO 8601 format
`YYYY-MM-DDThh:mm:ssZ`.

```
Get-EC2InstanceSqlHaHistoryState `
-InstanceId '`i-1234567890abcdef0`','`i-0fedcba0987654321`' `
-StartTime '`2026-08-01T00:00:00Z`' `
-EndTime '`2026-08-24T00:00:00Z`'
```

You can run these cmdlets from [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"), which comes with [AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-welcome.md "../../../powershell/latest/userguide/pstools-welcome.md") pre-installed. Run `pwsh` to start PowerShell.
