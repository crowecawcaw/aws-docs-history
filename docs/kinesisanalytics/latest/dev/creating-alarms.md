After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Creating CloudWatch Alarms to Monitor

You can create an Amazon CloudWatch alarm that sends an Amazon SNS message when the alarm
changes state. An alarm watches a single metric over a time period you specify. It
performs one or more actions based on the value of the metric relative to a given
threshold over a number of time periods. The action is a notification sent to an
Amazon SNS topic or Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. For a CloudWatch alarm to invoke
an action, the state must have changed and been maintained for a specified amount of
time.

You can set alarms using the AWS Management Console, CloudWatch AWS CLI, or CloudWatch API, as described
following.

###### To set an alarm using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm**. The **Create Alarm
   Wizard** starts.
3. Choose **Kinesis Analytics Metrics**. Then scroll through
   the metrics to locate the metric you want to place an alarm on.

To display just metrics, search for the file system ID of your
file system. Choose the metric to create an alarm for, and then choose
**Next**. 4. Enter values for **Name**,
**Description**, and **Whenever** for
the metric. 5. If you want CloudWatch to send you an email when the alarm state is reached, in the
**Whenever this alarm:** field, choose **State is
ALARM**. In the **Send notification to:** field, choose an
existing SNS topic. If you select **Create topic**, you can set the name
and email addresses for a new email subscription list. This list is saved and appears in
the field for future alarms.

###### Note

If you use **Create topic** to create a new Amazon SNS topic, the
email addresses must be verified before they receive notifications. Emails are only
sent when the alarm enters an alarm state. If this alarm state change happens before
the email addresses are verified, they do not receive a notification. 6. In the **Alarm Preview** section, preview the alarm
you’re about to create. 7. Choose
**Create Alarm** to create the alarm.

###### To set an alarm using the CloudWatch CLI

- Call `mon-put-metric-alarm`. For more information, see the
  [Amazon CloudWatch CLI Reference](../../../AmazonCloudWatch/latest/cli.md "../../../AmazonCloudWatch/latest/cli.md").

###### To set an alarm using the CloudWatch API

- Call `PutMetricAlarm`. For more information, see the
  [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
