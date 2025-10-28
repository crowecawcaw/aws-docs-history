# Create alarms with Network Flow Monitor

You can create Amazon CloudWatch alarms based on Network Flow Monitor metrics, just as you can for other CloudWatch metrics.

For example, you can create an alarm based on the Network Flow Monitor metric `Retransmissions`, and
configure it to send a notification when the metric is higher than a value that you choose. You configure
alarms for Network Flow Monitor metrics following the same guidelines as for other CloudWatch metrics.

Following are example Network Flow Monitor metrics that you might choose to create an alarm for:

- **Retransmissions**
- **Timeouts**
- **RoundTripTime**
  To see all the metrics available for Network Flow Monitor see [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md "ConsoleAlarms.md").

The following procedure provides an example of setting an alarm on **Retransmissions** by
navigating to the metric in the CloudWatch dashboard. Then, you follow the standard CloudWatch steps to create an alarm based
on a threshold that you choose, and set up a notification or choose other options.

###### To create an alarm for **Retransmissions** in CloudWatch Metrics

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, and then choose **All metrics**.
3. Filter for Network Flow Monitor by choosing `AWS/NetworkFlowMonitor`.
4. Choose **MeasurementSource, MonitorName**.
5. In the list, select **Retransmissions**.
6. On the **GraphedMetrics** tab, under **Actions**, choose the bell icon to
   create an alarm based on a static threshold.
   Now, follow the standard CloudWatch steps to choose options for the alarm. For example, you can choose to be
   notified by an Amazon SNS message if **Retransmissions** is below a specific threshold number. Alternatively,
   or in addition, you can add the alarm to a dashboard.

Keep in mind the following:

- Network Flow Monitor metrics are typically aggregated and sent to the Network Flow Monitor backend every 30 seconds,
  with a 5 second potential jitter (in other words, 25 to 35 seconds).
- When you create an alarm based on Network Flow Monitor metrics, make sure that you take into account
  the short delay before publication when you set an alarm’s lookback period. We recommend that you configure
  **Evaluation Periods** with lookback period that is a minimum of 25 minutes.
  For more information about options when you create a CloudWatch alarm, see
  [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md "ConsoleAlarms.md").
