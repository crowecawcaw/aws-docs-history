# Creating CloudWatch alarms

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An
alarm watches a single metric over a time period you specify, and performs one or more
actions based on the value of the metric relative to a given threshold over a number of time
periods. The action is a notification sent to an Amazon SNS topic or Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke
actions simply because they are in a particular state; the state must have changed and been
maintained for a specified number of periods. You can create an alarm from the Amazon FSx console
or the CloudWatch console.

The following procedures describe how to create alarms for Amazon FSx using the console,
AWS CLI, and API.

###### To set a CloudWatch alarm (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the navigation pane, choose **File systems**, and then choose
   the file system you want to create the alarm for.
3. Choose the **Actions** menu, and choose **View
   details**.
4. On the **Summary** page, choose **Monitoring and performance**.
5. Choose **CloudWatch alarms**.
6. Choose **Create CloudWatch alarm**. You are redirected to the CloudWatch
   console.
7. Choose **Select metrics**, and choose **Next**.
8. In the **Metrics** section, choose **FSX**.
9. Choose **File System Metrics**, choose the metric you want to set the alarm
   for, and then choose **Select metric**.
10. In the **Conditions** section, choose the conditions you want for the alarm,
    and choose **Next**.

###### Note

Metrics may not be published during file system maintenance for Single-AZ file systems,
or during failover and failback to or from the primary or secondary servers for
Multi-AZ file systems. To prevent unnecessary and misleading alarm condition changes and
to configure your alarms so that they are resilient to missing data points,
see [Configuring how CloudWatch alarms treat missing data](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data") in the
_Amazon CloudWatch User Guide_. 11. If you want CloudWatch to send you an email or SNS notification when the alarm state
triggers the action, choose an alarm state for **Whenever this alarm state
is**.

For **select an SNS topic**, choose an existing SNS topic. If you
select **Create topic**, you can set the name and email addresses for a
new email subscription list. This list is saved and appears in the field for future
alarms. Choose **Next**.

###### Note

If you use **Create topic** to create a new Amazon SNS topic, the
email addresses must be verified before they receive notifications. Emails are only
sent when the alarm enters an alarm state. If this alarm state change happens before
the email addresses are verified, they do not receive a notification. 12. Fill in the **Name**, **Description**, and
**Whenever** values for the metric, and choose
**Next**. 13. On the **Preview and create** page, review the alarm you're about to create,
and then choose **Create Alarm**.

###### To set alarms using the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm** to start the **Create Alarm
   Wizard**.
3. Choose **FSx Metrics**, and scroll through the Amazon FSx metrics to
   locate the metric you want to place an alarm on. To display just the Amazon FSx metrics in
   this dialog box, search on the file system ID of your file system. Select the metric to
   create an alarm on, and choose **Next**.
4. Fill in the **Name**, **Description**, and
   **Whenever** values for the metric.
5. If you want CloudWatch to send you an email when the alarm state is reached, for
   **Whenever this alarm**, choose **State is ALARM**.
   For **Send notification to**, choose an existing SNS topic. If you
   select **Create topic**, you can set the name and email addresses for a
   new email subscription list. This list is saved and appears in the field for future
   alarms.

###### Note

If you use **Create topic** to create a new Amazon SNS topic, the
email addresses must be verified before they receive notifications. Emails are only
sent when the alarm enters an alarm state. If this alarm state change happens before
the email addresses are verified, they do not receive a notification. 6. At this point, the **Alarm Preview** area gives you a chance to
preview the alarm you're about to create. Choose **Create Alarm**.

###### To set a CloudWatch alarm (CLI)

- Call `put-metric-alarm`. For more information, see
  _[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")_.

###### To set an alarm (API)

- Call `PutMetricAlarm`. For more information, see
  _[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md")_.
