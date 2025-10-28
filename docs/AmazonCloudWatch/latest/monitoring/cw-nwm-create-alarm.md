# Probe alarms

You can create Amazon CloudWatch alarms based on Network Synthetic Monitor metrics, just as you can for other
Amazon CloudWatch metrics. Any alarm that you create will appear in the probe's
**Status** column of the **Monitor details** section of the
Network Synthetic Monitor dashboard when the alarm is triggered. The status will either be
**OK** or **In Alarm**. If no status displays for a probe,
then no alarm was created for that probe.

For example, you can create an alarm based on the Network Synthetic Monitor metric
`PacketLoss`, and configure it to send a notification when the metric is higher than
a value that you choose. You configure alarms for Network Synthetic Monitor metrics following the same
guidelines as for other CloudWatch metrics.

The following metrics are available under `AWS/NetworkMonitor` when creating a
CloudWatch alarm for Network Synthetic Monitor.

- **HealthIndicator**
- **PacketLoss**
- **RTT (Round-trip time)**
  For the steps to create a Network Synthetic Monitor alarm in CloudWatch, see [Create a CloudWatch alarm based on a static threshold](ConsoleAlarms.md "ConsoleAlarms.md").
