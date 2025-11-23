# Creating CloudWatch alarms to monitor Amazon File Cache

You can create an Amazon CloudWatch Logs alarm that sends an Amazon SNS message when the alarm's
state changes. An alarm watches a single metric over a time period that you specify, and
performs one or more actions based on the value of the metric relative to a given threshold
over a number of time periods. The action is a notification sent to an Amazon SNS topic or Amazon EC2 Auto Scaling
policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke
actions because they are in a particular state; the state must have changed and been
maintained for a specified number of periods.

The following procedures outline how to create alarms for an Amazon File Cache resource.

###### To set alarms using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm**. Doing this launches the Create
   Alarm Wizard.
3. Choose **FSx Metrics** and scroll through the Amazon File Cache
   metrics to locate the metric that you want to place an alarm on. To display only the
   Amazon File Cache metrics in this dialog box, search the cache ID of your cache. Choose the
   metric to create an alarm on, and choose **Next**.
4. In the **Conditions** section, choose the conditions that you want for the
   alarm, then choose **Next**.

###### Note

Metrics may not be published during system
maintenance. To prevent unnecessary and misleading alarm condition changes and
to configure your alarms so that they are resilient to missing data points,
see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") in the
_Amazon CloudWatch User Guide_. 5. If you want CloudWatch to send you an email when the alarm state is reached, for
**Whenever this alarm**, choose **State is ALARM**.
For **Send notification to**, choose an existing SNS topic. If you choose
**Create topic**, you can set the name and email addresses for a new
email subscription list. This list is saved and appears in this box for future
alarms.

###### Note

If you use **Create topic** to create a new Amazon SNS topic, verify
the email addresses before sending them notifications. Emails are only sent when the
alarm enters an alarm state. If this alarm state change happens before the email
addresses are verified, they don't receive a notification. 6. Preview the alarm you're about to create in the **Alarm
Preview** area. If it appears as expected, choose **Create
Alarm**.

###### To set an alarm using the AWS CLI

- Call `put-metric-alarm`. For more information, see
  _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_.

###### To set an alarm using the CloudWatch API

- Call `PutMetricAlarm`. For more information, see
  _[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md")_.
