

# Disable Amazon EC2 High Availability for SQL Server
<a name="sql-high-availability-disable"></a>

You can disable Amazon EC2 High Availability for SQL Server (SQL HA). Note only instances enabled by SQL HA can receive the SQL Server license savings. Use one of the following methods to disable SQL HA for your instances:

------
#### [ Console ]

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation panel, choose **Instances**.

1. Select the instances in the High Availability deployment to enable SQL HA standby detection monitoring, choose **Actions**, **Instance settings**, **Modify SQL High Availability settings**.

1. In the **Review prerequisites** step, choose **Next**. The prerequisites only apply for enabling the monitoring, and it is not necessary to review them for disabling SQL HA standby detection monitoring.

1. In the **Manage SQL High Availability license savings** step, for each instance to disable, for **SQL High Availability license savings**, select **None**.

1. Choose **Next**.

1. In the **Review and apply changes** step, review the configuration and then choose **Apply changes**.

------
#### [ AWS CLI ]

Use the [ disable-instance-sql-ha-standby-detections](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-instance-sql-ha-standby-detections.html) command. For `instance-ids`, specify the IDs of the instances to disable.

```
aws ec2 disable-instance-sql-ha-standby-detections \
--instance-ids {{i-1234567890abcdef0}} {{i-0fedcba0987654321}}
```

You can run these commands from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) pre-installed.

------
#### [ PowerShell ]

Use the [ Disable-EC2InstanceSqlHaStandbyDetection](https://docs.aws.amazon.com/powershell/latest/reference/items/Disable-EC2InstanceSqlHaStandbyDetection.html) cmdlet. For `-InstanceId`, specify the IDs of the instances to disable.

```
Disable-EC2InstanceSqlHaStandbyDetection `
-InstanceId '{{i-1234567890abcdef0}}','{{i-0fedcba0987654321}}'
```

You can run these cmdlets from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) pre-installed. Run `pwsh` to start PowerShell.

------