# Creating CloudWatch alarms to monitor Amazon Keyspaces

You can create an Amazon CloudWatch alarm for Amazon Keyspaces that sends an Amazon Simple Notification Service (Amazon SNS) message when
the alarm changes state. An alarm watches a single metric over a time period that you
specify. It performs one or more actions based on the value of the metric relative to a
given threshold over a number of time periods. The action is a notification sent to an Amazon SNS
topic or an Application Auto Scaling policy.

When you use Amazon Keyspaces in provisioned mode with Application Auto Scaling, the service creates two pairs of
CloudWatch alarms on your behalf. Each pair represents your upper and lower boundaries for
provisioned and consumed throughput settings. These CloudWatch alarms are triggered when the table's
actual utilization deviates from your target utilization for a sustained period of time. To
learn more about CloudWatch alarms created by Application Auto Scaling, see [How Amazon Keyspaces automatic scaling works](autoscaling.md#autoscaling.HowItWorks "autoscaling.md#autoscaling.HowItWorks").

Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke
actions simply because they are in a particular state. The state must have changed and been
maintained for a specified number of periods.

For more information about creating CloudWatch alarms, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
_Amazon CloudWatch User Guide_.
