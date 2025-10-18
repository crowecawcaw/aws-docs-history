# Alarming on logs

The steps in the following sections explain how to create CloudWatch alarms on logs.


## Create a CloudWatch alarm based on a log
 group-metric filter


 The procedure in this section describes how to create an alarm based on a log
 group-metric filter. With metric filters, you can look for terms and patterns in log data as
 the data is sent to CloudWatch. For more information, see [Create metrics from log events
 using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html") in the *Amazon CloudWatch Logs User Guide*. Before you create
 an alarm based on a log group-metric filter, you must complete the following actions: 



* Create a log group. For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group") in the *Amazon CloudWatch Logs User
 Guide*.
* Create a metric filter. For more information, see [Create a metric
 filter for a log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html") in the *Amazon CloudWatch Logs User Guide*.

######  To create an alarm based on a log group-metric filter

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. From the navigation pane, choose **Logs**, and then choose
 **Log groups**.
3. Choose the log group that includes your metric filter.
4. Choose **Metric filters**.
5. In the metric filters tab, select the box for the metric filter that you want to
 base your alarm on.
6. Choose **Create alarm**.
7. (Optional) Under **Metric**, edit **Metric
 name**, **Statistic**, and **Period**.
8. Under **Conditions**, specify the following: 


	1. For **Threshold type**, choose **Static** or
	 **Outlier detection**.
	2. For **Whenever `your-metric-name` is . .
	 .**, choose **Greater**,
	 **Greater/Equal**, **Lower/Equal** , or
	 **Lower**.
	3. For **than . . .**, specify a number for your threshold value.
9. Choose **Additional configuration**. 


	1. For **Data points to alarm**, specify how many data points
	 trigger your alarm to go into the `ALARM` state. If you specify matching
	 values, your alarm goes into the `ALARM` state if that many consecutive
	 periods are breaching. To create an M-out-of-N alarm, specify a number for the first
	 value that's lower than the number you specify for the second value. For more
	 information, see [Using Amazon CloudWatch alarms](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").
	2. For **Missing data treatment**, select an option to specify
	 how to treat missing data when your alarm is evaluated.
10. Choose **Next**.
11. For **Notification**, specify an Amazon SNS topic to notify when your
 alarm is in the `ALARM`, `OK`, or `INSUFFICIENT_DATA`
 state. 


	1. (Optional) To send multiple notifications for the same alarm state or for
	 different alarm states, choose **Add notification**.
	2. (Optional) To not send notifications, choose **Remove**.
12. To have the alarm perform Auto Scaling, EC2, Lambda, or Systems Manager actions, choose the
 appropriate button and choose the alarm state and action to perform. If you choose a
 Lambda function as an alarm action, you specify the function name or ARN, and you can
 optionally choose a specific version of the function.


Alarms can perform Systems Manager actions only when they go into ALARM state. For more
 information about Systems Manager actions, see see  [Configuring CloudWatch to create OpsItems from alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html") and [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html").


###### Note

To create an alarm that performs an SSM Incident Manager action, you must have
 certain permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident
 Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html").
13. Choose **Next**.
14. For **Name and description**, enter a name and description for
 your alarm. The name must contain only UTF-8 characters, and can't contain ASCII control
 characters. The description can include markdown formatting, which is displayed only in
 the alarm **Details** tab in the CloudWatch console. The markdown can be
 useful to add links to runbooks or other internal resources.
15. For **Preview and create**, check that your configuration is
 correct, and choose **Create alarm**.
