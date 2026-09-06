

# Creating CloudWatch alarms to monitor Amazon RDS
<a name="creating_alarms"></a>

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period that you specify. The alarm can also perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic or Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke actions simply because they are in a particular state. The state must have changed and have been maintained for a specified number of time periods.

You can use the **DB\_PERF\_INSIGHTS** metric math function in the CloudWatch console to query Amazon RDS for detailed per-query and database counter metrics, which are exposed through the Performance Insights API. The **DB\_PERF\_INSIGHTS** function also includes the DBLoad metric at sub-minute intervals. You can set CloudWatch alarms on these metrics.

For more details on how to create an alarm, see [ Create an alarm on Performance Insights counter metrics from an AWS database](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.html).

**To set an alarm using the AWS CLI**
+ Call [`put-metric-alarm`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html). For more information, see *[AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)*.

**To set an alarm using the CloudWatch API**
+ Call [`PutMetricAlarm`](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html). For more information, see *[Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/)* 

For more information about setting up Amazon SNS topics and creating alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).