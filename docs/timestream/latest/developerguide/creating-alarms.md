For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating CloudWatch alarms to monitor Timestream for LiveAnalytics

You can create an Amazon CloudWatch alarm for Timestream for LiveAnalytics that sends an Amazon Simple Notification Service (Amazon SNS) message when
the alarm changes state. An alarm watches a single metric over a time period that you
specify. It performs one or more actions based on the value of the metric relative to a
given threshold over a number of time periods. The action is a notification sent to an Amazon SNS
topic or Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke
actions simply because they are in a particular state. The state must have changed and been
maintained for a specified number of periods.

For more information about creating CloudWatch alarms, see [Using Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
_Amazon CloudWatch User Guide_.
