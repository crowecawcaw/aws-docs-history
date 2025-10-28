# Create a CloudWatch alarm for an instance

You can create a CloudWatch alarm that monitors CloudWatch metrics for one of your instances. CloudWatch
will automatically send you a notification when the metric reaches a threshold you specify.
You can create a CloudWatch alarm using the Amazon EC2 console, or using the more advanced options
provided by the CloudWatch console.

###### To create an alarm using the CloudWatch console

For examples, see [Creating Amazon CloudWatch
Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

###### To create an alarm using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Actions**, **Monitor and troubleshoot**, **Manage CloudWatch alarms**.
4. On the **Manage CloudWatch alarms** detail page, under **Add or edit alarm**, select **Create an alarm**.
5. For **Alarm notification**, choose whether to configure Amazon Simple Notification Service (Amazon SNS)
   notifications. Enter an existing Amazon SNS topic or enter a name to create a new topic.
6. For **Alarm action**, choose whether to specify an action to take when the
   alarm is triggered. Choose an action from the list.
7. For **Alarm thresholds**, select the metric and criteria for the alarm. For
   example, to create an alarm that is triggered when CPU utilization reaches 80% for a 5
   minute period, do the following:
   1. Keep the default setting for **Group samples by** (**Average**)
      and **Type of data to sample** (**CPU utilization**).
   2. Choose **>=** for **Alarm when** and
      enter `0.80` for **Percent**.
   3. Enter `1` for **Consecutive period**
      and select **5 minutes** for **Period**.

8. (Optional) For **Sample metric data**, choose **Add to dashboard**.
9. Choose **Create**.
   You can edit your CloudWatch alarm settings from the Amazon EC2 console or the CloudWatch console. If you
   want to delete your alarm, you can do so from the CloudWatch console. For more information, see
   [Edit or delete a
   CloudWatch alarm](../../../AmazonCloudWatch/latest/monitoring/Manage-CloudWatch-Alarm.md#Edit-CloudWatch-Alarm "../../../AmazonCloudWatch/latest/monitoring/Manage-CloudWatch-Alarm.md#Edit-CloudWatch-Alarm") in the _Amazon CloudWatch User Guide_.
