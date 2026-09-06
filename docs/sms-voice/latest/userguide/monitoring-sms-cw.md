

# Create CloudWatch Alarms for AWS End User Messaging SMS metrics
<a name="monitoring-sms-cw"></a>

With CloudWatch you can create alarms that trigger based on metric thresholds for AWS End User Messaging SMS metrics. For example, you can create an alarm for the `NumberOfTextMessagePartsSent` metric. If more than 1000 text message parts are sent in 1 hour, an email notification can be sent. For more information, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

**To create an alarm that sends an email when 1000 text message parts have been sent in an hour**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Alarms** in the navigation pane, then choose **Create Alarm**.

1. In the **Select Metric** section choose **Browse Metrics** and then choose the `AWS/SMSVoice` namespace.

1. For `AWS/SMSVoice` metrics, choose the metric for which you want to set an alarm, then choose **Next**. For a list of available metrics, see [Monitoring with CloudWatch](monitoring-cloudwatch.md).

1. To set an alarm for the number of text message parts sent:

   1. Choose **Message Delivery Metrics**

   1. Choose the **NumberOfTextMessagePartsSent** metric

1. In the **Specify metric and conditions** section:

   1. Set the statistic to Sum

   1. Set the period to 1 hour

   1. For **Conditions**, choose **Static**

   1. Set "**Whenever NumberOfTextMessagePartsSent is...**" to "**Greater than**"

   1. Enter the threshold value of 1000

1. In the **Configure actions** section:

   1. For **Alarm state trigger**, choose **In alarm**

   1. Choose an existing Amazon SNS topic to notify or create a new one

   1. If creating a new topic, enter email addresses separated by commas
**Note**  
If you create a new Amazon SNS topic, the email addresses must be verified before they receive notifications.

1. In the **Add name and description** section:

   1. Enter a name for your alarm. for example, **High Text Message Volume**

   1. Optionally, add a description

1. Preview the alarm settings in the **Preview and create** section, then choose **Create alarm**.

The alarm is now created and will trigger based on the conditions you specified.

You can create similar alarms for other AWS End User Messaging SMS metrics, such as:
+ `NumberOfMediaMessagePartsSent`
+ `NumberOfTextMessagePartsDelivered`
+ `TextMessagesBlockedByProtect`

Adjust the metric, threshold, and other settings as needed for your specific use case.