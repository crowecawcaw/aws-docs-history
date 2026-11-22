

# Create alarms with Performance Monitor

When you create a monitor, you can turn on a recommended CloudWatch alarm for High impact to get notified when network degradation occurs. You can also set a custom alarm threshold for High impact.

To alarm on specific paths, configure additional alarms in CloudWatch after you create the monitor. For example, you can alarm when `ImpactScore` for a critical path exceeds a threshold that you define.

**To create an alarm for a network path**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose **Select metric**, and then choose `AWS/NetworkFlowMonitor`.

1. Choose **LocalLocation, MonitorId, RemoteLocation**.

1. Select the metric that you want to alarm on, for example, `ImpactScore`.

1. Configure the threshold, for example, greater than or equal to 65 for Medium impact, or greater than or equal to 95 for High impact.

1. Configure the notification action, for example, to send a notification to an Amazon SNS topic.

1. Choose **Create alarm**.

## Create an alarm for any path in a monitor
<a name="CloudWatch-PerformanceMonitor-alarm-any-path"></a>

To get notified when any network path in a monitor reaches an impact level, create an alarm on a CloudWatch Metrics Insights query. The following query returns the highest `ImpactScore` across all paths in a monitor:

```sql
SELECT MAX(ImpactScore)
FROM SCHEMA("AWS/NetworkFlowMonitor", LocalLocation, MonitorId, RemoteLocation)
WHERE MonitorId = '{{monitor-id}}'
```

Set the alarm threshold to greater than or equal to 95 to alarm when any path reaches High impact. For more information, see [Creating a Metrics Insights CloudWatch alarm](cloudwatch-metrics-insights-alarm-create.md).

Standard CloudWatch alarm charges apply. For more information about options when you create a CloudWatch alarm, see [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md).