

# Create a CloudWatch alarm for an instance
<a name="using-cloudwatch-createalarm"></a>

You can create a CloudWatch alarm that monitors CloudWatch metrics for one of your instances. CloudWatch will automatically send you a notification when the metric reaches a threshold you specify. You can create a CloudWatch alarm using the Amazon EC2 console, or using the more advanced options provided by the CloudWatch console.

**To create an alarm using the CloudWatch console**  
For examples, see [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

**To create an alarm using the Amazon EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the instance and choose **Actions**, **Monitor and troubleshoot**, **Manage CloudWatch alarms**.

1. On the **Manage CloudWatch alarms** detail page, under **Add or edit alarm**, select **Create an alarm**.

1. For **Alarm notification**, choose whether to configure Amazon Simple Notification Service (Amazon SNS) notifications. Enter an existing Amazon SNS topic or enter a name to create a new topic.

1. For **Alarm action**, choose whether to specify an action to take when the alarm is triggered. Choose an action from the list.

1. For **Alarm thresholds**, select the metric and criteria for the alarm. For example, to create an alarm that is triggered when CPU utilization reaches 80% for a 5 minute period, do the following:

   1. Keep the default setting for **Group samples by** (**Average**) and **Type of data to sample** (**CPU utilization**).

   1. Choose **>=** for **Alarm when** and enter **0.80** for **Percent**.

   1. Enter **1** for **Consecutive period** and select **5 minutes** for **Period**.

1. (Optional) For **Sample metric data**, choose **Add to dashboard**.

1. Choose **Create**.

You can edit your CloudWatch alarm settings from the Amazon EC2 console or the CloudWatch console. If you want to delete your alarm, you can do so from the CloudWatch console. For more information, see [Edit or delete a CloudWatch alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Manage-CloudWatch-Alarm.html#Edit-CloudWatch-Alarm) in the *Amazon CloudWatch User Guide*.