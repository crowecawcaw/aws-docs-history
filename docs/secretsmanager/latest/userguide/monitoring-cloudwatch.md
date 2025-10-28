# Monitor AWS Secrets Manager with Amazon CloudWatch

Using Amazon CloudWatch, you can monitor AWS services and create alarms to let you know when metrics change. CloudWatch keeps these statistics for 15 months, so you can access
historical information and gain a better perspective on how your web application or service is
performing. For AWS Secrets Manager, you can monitor the number of secrets in your account, including secrets marked for deletion, and API calls to Secrets Manager, including calls made through the console. For information about how to monitor metrics, see [Use CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _CloudWatch User Guide_.

###### To find Secrets Manager metrics

1. On the CloudWatch console, under **Metrics**, choose **All metrics**.
2. In the **Metrics** search, box, enter `secret`.
3. Do the following:
   - To monitor the number of secrets in your account, choose **AWS/SecretsManager**, and then select **SecretCount**. This metric is published hourly.
   - To monitor API calls to Secrets Manager, including calls made through the console, choose **Usage > By AWS Resource**, and then select the API calls to monitor. For a list of Secrets Manager APIs, see [Secrets Manager operations](../apireference/API_Operations.md "../apireference/API_Operations.md").

4. Do the following:
   - To create a graph of the metric, see [Graphing metrics](../../../AmazonCloudWatch/latest/monitoring/graph_metrics.md "../../../AmazonCloudWatch/latest/monitoring/graph_metrics.md") in the _Amazon CloudWatch User Guide_.
   - To detect anomalies, see [Using CloudWatch anomaly detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") in the _Amazon CloudWatch User Guide_.
   - To get statistics for a metric, see [Get statistics for a metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md") in the _Amazon CloudWatch User Guide_.

## CloudWatch alarms

You can create a CloudWatch alarm that sends an Amazon SNS message when the value of a metric changes and causes the alarm to change state. You can set an alarm on the Secrets Manager metric `ResourceCount`, which is the number of secrets in your account. You can also set alarms on An alarm watches a metric over a time period you specify, and performs actions based on the value of the metric relative to a given threshold over a number of time periods. Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods.

For more information, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") and [Create a CloudWatch alarm based on anomaly detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md") in the _CloudWatch User Guide_.

You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
