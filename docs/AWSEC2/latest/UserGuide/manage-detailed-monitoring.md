

# Manage detailed monitoring for your EC2 instances

Amazon CloudWatch provides two categories of monitoring: *basic monitoring* and *detailed monitoring*. By default, your instance is configured for basic monitoring. You can enable detailed monitoring to receive the default instance metrics in 1-minute periods. You can also associate metric categories with an instance to publish additional metrics. You can manage detailed monitoring and metric categories at launch or when the instance is running or stopped.

Enabling detailed monitoring on an instance does not affect the monitoring of its attached EBS volumes. For more information, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/using_cloudwatch_ebs.html).

The following table shows the differences between basic monitoring and detailed monitoring for your instances.


| Monitoring type | Description | Charges | 
| --- | --- | --- | 
| Basic monitoring | Status check metrics are available in 1-minute periods. All other default metrics are available in 5-minute periods. | No charge. | 
| Detailed monitoring | Default instance metrics are available in 1-minute periods.<br />Metric categories can add selected graphics processing unit (GPU) metrics in 1-minute periods and CPU utilization in 10-second periods. | For CloudWatch Metrics, CloudWatch charges for each metric. For OpenTelemetry metrics, CloudWatch charges by the volume of data ingested. Standard CloudWatch pricing applies. For more information about pricing, see Paid tier in [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Paid_tier). | 

**Topics**
+ [Required permissions](#iam-detailed-monitoring)
+ [Use metric categories for additional metrics](#detailed-monitoring-metric-categories)
+ [Enable detailed monitoring at launch](#enable-detailed-monitoring)
+ [Manage detailed monitoring](#disable-detailed-monitoring)

## Required permissions
<a name="iam-detailed-monitoring"></a>

To enable detailed monitoring or associate metric categories with an existing instance, you must have permission to use the [MonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html) API action. To turn off detailed monitoring or remove metric category associations, you must have permission to use the [UnmonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html) API action.

To associate metric categories when you launch an instance, your IAM policy must allow `ec2:RunInstances` for the metric category resources.

To manage metric category resources, you need permission to use the `CreateMetricCategory`, `DescribeMetricCategories`, `ModifyMetricCategory`, and `DeleteMetricCategory` API actions. If you add tags when you create a category, you also need permission to use the `CreateTags` API action.

## Use metric categories for additional metrics
<a name="detailed-monitoring-metric-categories"></a>

A metric category is a Regional Amazon EC2 resource that contains a reusable set of additional metric names. Each category has an ID that starts with `mc-` and can contain up to 20 metrics. You can have up to 100 active metric categories in each Region, and deleted categories do not count toward this quota. Associate up to 10 category IDs with an instance that has detailed monitoring enabled.

Each metric name selects a publication format and period. The CloudWatch Metrics and OpenTelemetry names for the same measurement are separate selections. If you include both names, Amazon EC2 publishes both formats and charges apply to both. You can query the OpenTelemetry metrics using Prometheus Query Language (PromQL).

The following metrics are available for metric categories. For each metric's description, unit, and supported instance types, see [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics) and [Accelerator metrics](viewing_metrics_with_cloudwatch.md#accelerator-metrics).


| Metric | Metric type | Period | 
| --- | --- | --- | 
| instance.cpu.utilization | OpenTelemetry | 10 seconds | 
| instance.gpu.utilization | OpenTelemetry | 1 minute | 
| instance.gpu.sm\_utilization | OpenTelemetry | 1 minute | 
| instance.gpu.memory\_utilization | OpenTelemetry | 1 minute | 
| instance.gpu.context\_accumulated\_time | OpenTelemetry | 1 minute | 
| instance.gpu.temperature\_percent\_of\_limit | OpenTelemetry | 1 minute | 
| instance.gpu.memory\_temperature\_percent\_of\_limit | OpenTelemetry | 1 minute | 
| instance.gpu.pcie\_utilization | OpenTelemetry | 1 minute | 
| instance.gpu.nvlink\_utilization | OpenTelemetry | 1 minute | 
| CPUUtilization10Sec | CloudWatch | 10 seconds | 
| GPUUtilization | CloudWatch | 1 minute | 
| GPUStreamingMultiprocessorUtilization | CloudWatch | 1 minute | 
| GPUMemoryUtilization | CloudWatch | 1 minute | 
| GPUContextAccumulatedTime | CloudWatch | 1 minute | 
| GPUTemperaturePercentOfLimit | CloudWatch | 1 minute | 
| GPUMemoryTemperaturePercentOfLimit | CloudWatch | 1 minute | 
| GPUPCIeUtilization | CloudWatch | 1 minute | 
| GPUNVLinkUtilization | CloudWatch | 1 minute | 

The GPU metrics are available only for supported accelerated computing instance types. If an instance does not support a selected metric, Amazon EC2 does not publish that metric for the instance.

### Create a metric category
<a name="create-detailed-monitoring-metric-category"></a>

------
#### [ AWS CLI ]

The following AWS CLI example creates a category for CPU utilization measured every 10 seconds:

```bash
aws ec2 create-metric-category \
    --metrics CPUUtilization10Sec \
    --tag-specifications 'ResourceType=metric-category,Tags=[{Key=Name,Value=cpu-10-second}]'
```

The response includes the metric category ID. Use this ID when you associate the category with an instance.

------

### Metric category management
<a name="manage-detailed-monitoring-metric-categories"></a>

Use the following commands to manage your metric categories.
+ To list all metric categories, use `describe-metric-categories` with no parameters:

  ```bash
  aws ec2 describe-metric-categories
  ```
+ To replace the complete metric set in a category, use `modify-metric-category`:

  ```bash
  aws ec2 modify-metric-category \
      --metric-category-id {{mc-0123456789abcdef0}} \
      --metrics GPUUtilization GPUMemoryUtilization GPUNVLinkUtilization
  ```
+ To delete a category, use `delete-metric-category`:

  ```bash
  aws ec2 delete-metric-category \
      --metric-category-id {{mc-0123456789abcdef0}}
  ```

To update your running or stopped instances after `modify-metric-category`, call `monitor-instances` with the category ID.

Amazon EC2 also updates every associated instance asynchronously after you modify or delete a metric category. For more information, see [Eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html).

## Enable detailed monitoring at launch
<a name="enable-detailed-monitoring"></a>

Use the following procedures to enable detailed monitoring at launch. By default, your instance uses basic monitoring.

------
#### [ Console ]

**To enable detailed monitoring when launching an instance**  
When launching an instance using the Amazon EC2 console, under **Advanced details**, select **Detailed CloudWatch monitoring**.

------
#### [ AWS CLI ]

**To enable detailed monitoring when launching an instance**  
Use the `run-instances` command with the `--monitoring` option. The following AWS CLI option enables detailed monitoring and associates a metric category:

```bash
--monitoring '{"Enabled":true,"MetricCategoryIds":["mc-0123456789abcdef0"]}'
```

For more information about the `run-instances` command, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html).

------
#### [ PowerShell ]

**To enable detailed monitoring when launching an instance**  
Use the `New-EC2Instance` cmdlet with the `-Monitoring` parameter.

```powershell
-Monitoring $true
```

For cmdlet details, see the [Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html).

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

1. On the **Manage detailed monitoring** page, enable or disable detailed monitoring.

1. Choose **Done**.

------
#### [ AWS CLI ]

**To enable detailed monitoring**  
Use the following AWS CLI command:

```bash
aws ec2 monitor-instances --instance-ids {{i-1234567890abcdef0}}
```

For more information about the `monitor-instances` command, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/monitor-instances.html).

**To associate a metric category**  
Use `monitor-instances` with `--metric-category-ids`:

```bash
aws ec2 monitor-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --metric-category-ids {{mc-0123456789abcdef0}}
```

This command enables detailed monitoring if needed and adds the categories that you specify. It keeps existing associations.

**To remove a metric category association**  
Use `unmonitor-instances` with `--metric-category-ids`:

```bash
aws ec2 unmonitor-instances \
    --instance-ids {{i-1234567890abcdef0}} \
    --metric-category-ids {{mc-0123456789abcdef0}}
```

Detailed monitoring remains enabled.

**To disable detailed monitoring**  
Use the following AWS CLI command without metric category IDs:

```bash
aws ec2 unmonitor-instances --instance-ids {{i-1234567890abcdef0}}
```

This command removes all metric category associations. For more information about the `unmonitor-instances` command, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/unmonitor-instances.html).

------
#### [ PowerShell ]

**To enable detailed monitoring**  
Use the [Start-EC2InstanceMonitoring](https://docs.aws.amazon.com/powershell/latest/reference/items/Start-EC2InstanceMonitoring.html) cmdlet.

```powershell
Start-EC2InstanceMonitoring -InstanceId {{i-1234567890abcdef0}}
```

**To disable detailed monitoring**  
Use the [Stop-EC2InstanceMonitoring](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2InstanceMonitoring.html) cmdlet.

```powershell
Stop-EC2InstanceMonitoring -InstanceId {{i-1234567890abcdef0}}
```

------