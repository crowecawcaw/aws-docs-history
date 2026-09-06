

# View status checks for Amazon EC2 instances
<a name="viewing_status"></a>

If your instance has a failed status check, you typically must address the problem yourself (for example, by rebooting the instance or by making instance configuration changes). To troubleshoot system or instance status check failures yourself, see [Troubleshoot Amazon EC2 Linux instances with failed status checks](TroubleshootingInstances.md).

------
#### [ Console ]

**To view status checks**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. On the **Instances** page, the **Status check** column lists the operational status of each instance.

1. To view the status of a specific instance, select the instance, and then choose the **Status and alarms** tab.

1. To review the CloudWatch metrics for status checks, on the **Status and alarms** tab, expand **Metrics** to see the graphs for the following metrics:
   + **Status check failed for system**
   + **Status check failed for instance**
   + **Status check failed for attached EBS**
   + **Status check failed for application**

   For more information, see [Status check metrics](viewing_metrics_with_cloudwatch.md#status-check-metrics).

------
#### [ AWS CLI ]

**To view status checks**  
Use the [describe-instance-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html) command.

**Example**: Get the status of all running instances

```
aws ec2 describe-instance-status
```

**Example**: Get the status of all instances

```
aws ec2 describe-instance-status --include-all-instances
```

**Example**: Get the status of a single running instance

```
aws ec2 describe-instance-status --instance-ids {{i-1234567890abcdef0}}
```

**Example**: Get all instances with a status of `impaired`

```
aws ec2 describe-instance-status \
--filters Name=instance-status.status,Values=impaired
```

------
#### [ PowerShell ]

**To view status checks**  
Use the [Get-EC2InstanceStatus](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceStatus.html) command.

**Example**: Get the status of all running instances

```
Get-EC2InstanceStatus
```

**Example**: Get the status of all instances

```
Get-EC2InstanceStatus -IncludeAllInstance $true
```

**Example**: Get the status of a single running instance

```
Get-EC2InstanceStatus -InstanceId {{i-1234567890abcdef0}}
```

**Example**: Get all instances with a status of `impaired`

```
Get-EC2InstanceStatus \
-Filter @{Name="instance-status.status"; Values="impaired"}
```

------