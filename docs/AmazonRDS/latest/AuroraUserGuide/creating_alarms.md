# Creating CloudWatch alarms to monitor Amazon Aurora

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period that you specify. The alarm can also perform one or
more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic or Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke actions simply because they are in a particular state. The state must have changed and have been
maintained for a specified number of time periods.

###### Note

For Aurora, use `WRITER` or `READER` role metrics to set up alarms instead of relying on metrics for specific DB instances. Aurora DB instance roles can change roles
over time. You can find these role-based metrics in the CloudWatch console.

Aurora Auto Scaling automatically sets alarms based on `READER` role metrics. For more information about Aurora Auto Scaling, see [Amazon Aurora Auto Scaling with Aurora Replicas](Aurora.Integrating.md "Aurora.Integrating.md").

You can use the **DB_PERF_INSIGHTS**
metric math function in the CloudWatch console to query Amazon RDS for Performance Insights counter metrics. The
**DB_PERF_INSIGHTS** function also includes the DBLoad metric at
sub-minute intervals. You can set CloudWatch alarms on these metrics.

For more details on how to create an alarm, see
[Create an alarm on Performance Insights counter metrics from an AWS database](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.md").

###### To set an alarm using the AWS CLI

- Call [`put-metric-alarm`](../../../cli/latest/reference/cloudwatch/put-metric-alarm.md "../../../cli/latest/reference/cloudwatch/put-metric-alarm.md"). For more information, see _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_.

###### To set an alarm using the CloudWatch API

- Call [`PutMetricAlarm`](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md"). For more information, see _[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md")_
  For more information about setting up Amazon SNS topics and creating alarms, see [Using Amazon CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").
