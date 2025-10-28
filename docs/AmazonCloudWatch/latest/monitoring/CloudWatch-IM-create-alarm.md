# Create alarms with Internet Monitor

You can create Amazon CloudWatch alarms based on Internet Monitor metrics, just as you can for other Amazon CloudWatch metrics.

For example, you can create an alarm based on the Internet Monitor metric `PerformanceScore`, and configure it to send a notification when the metric is
lower than a value that you choose. You configure alarms for Internet Monitor metrics following the same guidelines as for other CloudWatch metrics.

Following are the example Internet Monitor metrics that you might choose to create an alarm for:

- **PerformanceScore**
- **AvailabilityScore**
- **RoundtripTime**
  To see all the metrics available for
  Internet Monitor, see [View Internet Monitor metrics or set alarms in CloudWatch Metrics](CloudWatch-IM-view-cw-tools-metrics-dashboard.md "CloudWatch-IM-view-cw-tools-metrics-dashboard.md").

The following procedure provides an example of setting an alarm on **PerformanceScore** by
navigating to the metric in the CloudWatch dashboard. Then, you follow the standard CloudWatch steps to create an alarm based
on a threshold that you choose, and set up a notification or choose other options.

###### To create an alarm for **PerformanceScore** in CloudWatch Metrics

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, and then choose **All metrics**.
3. Filter for Internet Monitor by choosing `AWS/InternetMonitor`.
4. Choose **MeasurementSource, MonitorName**.
5. In the list, select **PerformanceScore**.
6. On the **GraphedMetrics** tab, under **Actions**, choose the bell icon to
   create an alarm based on a static threshold.
   Now, follow the standard CloudWatch steps to choose options for the alarm. For example, you can choose to be
   notified by an Amazon SNS message if **PerformanceScore** is below a specific threshold number. Alternatively,
   or in addition, you can add the alarm to a dashboard.

Keep in mind the following:

- Internet Monitor metrics are typically calculated and published within 20 minutes.
- When you create an alarm based on Internet Monitor metrics, make sure that you take into account
  the short delay before publication when you set an alarm’s lookback period. We recommend that you configure
  **Evaluation Periods** with lookback period that is a minimum of 25 minutes.
  To learn more about using CloudWatch alarms with Internet Monitor, see the following blog post:
  [Using Internet Monitor for enhanced internet observability](https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-cloudwatch-internet-monitor-for-enhanced-internet-observability "https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-cloudwatch-internet-monitor-for-enhanced-internet-observability").

For more information about options when you create a CloudWatch alarm, see [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md "ConsoleAlarms.md").
