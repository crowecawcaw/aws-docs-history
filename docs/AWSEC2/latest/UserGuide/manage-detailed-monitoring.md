

# Manage detailed monitoring for your EC2 instances
<a name="manage-detailed-monitoring"></a>

Amazon CloudWatch provides two categories of monitoring: *basic monitoring* and *detailed monitoring*. By default, your instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the instance is running or stopped.

Enabling detailed monitoring on an instance does not affect the monitoring of its attached EBS volumes. For more information, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/using_cloudwatch_ebs.html).

The following table highlights the differences between basic monitoring and detailed monitoring for your instances.


| Monitoring type | Description | Charges | 
| --- | --- | --- | 
| Basic monitoring | Status check metrics are available in 1-minute periods. All other metrics are available in 5-minute periods. | No charge. | 
| Detailed monitoring | You can get metrics in 1-minute periods, provided you enable detailed monitoring for the instance.<br />After you've enabled detailed monitoring, you can aggregate the data across groups of similar instances. | You are charged per metric that Amazon EC2 sends to CloudWatch. You are not charged for data storage. For more information, see Paid tier on the [Amazon CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/#Paid_tier). | 

**Topics**
+ [Required permissions](#iam-detailed-monitoring)
+ [Enable detailed monitoring at launch](#enable-detailed-monitoring)
+ [Manage detailed monitoring](#disable-detailed-monitoring)

## Required permissions
<a name="iam-detailed-monitoring"></a>

To enable detailed monitoring for an instance, your user must have permission to use the [MonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html) API action. To turn off detailed monitoring for an instance, your user must have permission to use the [UnmonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html) API action. 

## Enable detailed monitoring at launch
<a name="enable-detailed-monitoring"></a>

Use the following procedures to enable detailed monitoring at launch. By default, your instance uses basic monitoring.

------
#### [ Console ]

**To enable detailed monitoring when launching an instance**  
When launching an instance using the Amazon EC2 console, under **Advanced details**, select the **Detailed CloudWatch monitoring** checkbox.

------
#### [ AWS CLI ]

**To enable detailed monitoring when launching an instance**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--monitoring` option.

```
--monitoring Enabled=true
```

------
#### [ PowerShell ]

**To enable detailed monitoring when launching an instance**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-Monitoring` parameter.

```
-Monitoring $true
```

------

## Manage detailed monitoring
<a name="disable-detailed-monitoring"></a>

Use the following procedures to manage detailed monitoring for a running or stopped instance.

------
#### [ Console ]

**To manage detailed monitoring**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance.

1. Choose **Actions**, **Monitor and troubleshoot**, **Manage detailed monitoring**.

1. On the **Detailed monitoring** page, for **Detailed monitoring**, do one of the following:
   + Detailed monitoring – Select **Enable**.
   + Basic monitoring – Clear **Enable**.

1. Choose **Confirm**.

------
#### [ AWS CLI ]

**To enable detailed monitoring**  
Use the following [monitor-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/monitor-instances.html) command.

```
aws ec2 monitor-instances --instance-ids {{i-1234567890abcdef0}}
```

**To disable detailed monitoring**  
Use the [unmonitor-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/unmonitor-instances.html) command.

```
aws ec2 unmonitor-instances --instance-ids {{i-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To enable detailed monitoring**  
Use the [Start-EC2InstanceMonitoring](https://docs.aws.amazon.com/powershell/latest/reference/items/Start-EC2InstanceMonitoring.html) cmdlet.

```
Start-EC2InstanceMonitoring -InstanceId {{i-1234567890abcdef0}}
```

**To disable detailed monitoring**  
Use the [Stop-EC2InstanceMonitoring](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2InstanceMonitoring.html) cmdlet.

```
Stop-EC2InstanceMonitoring -InstanceId {{i-1234567890abcdef0}}
```

------