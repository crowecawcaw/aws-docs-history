

# Monitor performance
<a name="performance-monitoring"></a>

This section describes tools for monitoring an application's performance.

## Monitor performance using CloudWatch metrics
<a name="performance-monitoring-metrics"></a>

You monitor your application's resource usage, throughput, checkpointing, and downtime using CloudWatch metrics. For information about using CloudWatch metrics with your Managed Service for Apache Flink application, see [Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md).

## Monitor performance using CloudWatch logs and alarms
<a name="performance-monitoring-logs"></a>

You monitor error conditions that could potentially cause performance issues using CloudWatch Logs. 

Error conditions appear in log entries as Apache Flink job status changes from the `RUNNING` status to the `FAILED` status. 

You use CloudWatch alarms to create notifications for performance issues, such as resource use or checkpoint metrics above a safe threshold, or unexpected application status changes.

For information about creating CloudWatch alarms for a Managed Service for Apache Flink application, see [Use CloudWatch Alarms with Amazon Managed Service for Apache Flink](monitoring-metrics-alarms.md).