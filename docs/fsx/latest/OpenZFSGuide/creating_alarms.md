# Creating CloudWatch alarms to monitor metrics

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An
alarm watches a single metric over a time period that you specify and performs one or more
actions based on the value of the metric relative to a given threshold over a specified period
of time. The action is a notification that's sent to an Amazon SNS topic or Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke
actions because they are in a particular state. The state must change and remain changed for a
specified period of time. You can create an alarm on the Amazon FSx console or the CloudWatch
console.

The following procedures describe how to create alarms for Amazon FSx using the console,
AWS CLI, and API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the navigation pane, choose **File systems**, and then
   choose the file system that you want to create the alarm for.
3. Choose **Actions > View details**.
4. On the **Summary** page, choose **Monitoring and performance**.
5. Choose **Create CloudWatch alarm**. You are redirected to the CloudWatch
   console.
6. Choose **Select metrics**, and choose **Next**.
7. In the **Metrics** section, choose **FSX**.
8. Choose **File System Metrics**, choose the metric that you want to set the
   alarm for, and then choose **Select metric**.
9. In the **Conditions** section, choose the conditions for the alarm, and
   choose **Next**.

###### Note

Metrics might not be published during file system maintenance. To prevent unnecessary and
misleading alarm condition changes and to configure your alarms so that they are
resilient to missing data points, see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") in the
_Amazon CloudWatch User Guide_. 10. If you want CloudWatch to send you an email or SNS notification when the alarm state
triggers the action, choose
**Whenever
this alarm state is**.

For **Select an SNS topic**, choose an existing SNS topic. If
you select **Create topic**, you can set the name and email addresses
for a new email subscription list. This list is saved and appears in the field for
future alarms. Choose **Next**.

###### Warning

If you use **Create topic** to create a new Amazon SNS topic, the
email addresses must be verified before they receive notifications. Emails are only
sent when the alarm enters an alarm state. If this alarm state change happens before
the email addresses are verified, they do not receive a notification. 11. Fill in the **Name**, **Description**, and
**Whenever** values for the metric, and choose
**Next**. 12. On the **Preview and create** page, review the alarm and choose
**Create Alarm**.

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm** to start the **Create Alarm
   Wizard**.
3. Choose **FSx Metrics** to locate a metric. To narrow the
   results, you can search for your file system ID. Select the metric that you want to
   create an alarm for and choose **Next**.
4. Enter a **Name** and a **Description**, and
   choose a
   **Whenever**
   value for the metric.
5. If you want CloudWatch to send you an email when the alarm state is reached, choose
   **State is ALARM** for **Whenever this alarm**.
   For **Send notification to**, choose an existing SNS topic. If you
   select **Create topic**, you can set up the names and email addresses
   for a new email subscription list. This list is saved and appears in the field for
   future alarms.

###### Warning

If you use **Create topic** to create a new Amazon SNS topic, the
email addresses must be verified before they receive notifications. Emails are only
sent when the alarm enters an alarm state. If this alarm state change happens before
the email addresses are verified, they do not receive a notification. 6. View the **Alarm Preview** and then choose **Create
Alarm** or go back to make changes.

- Call `put-metric-alarm`. For more information, see
  _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_.
- Call `PutMetricAlarm`. For more information, see
  _[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md")_.
