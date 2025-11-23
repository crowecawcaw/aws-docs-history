# Creating a CloudWatch alarm

You can create a CloudWatch alarm that sends an Amazon Simple Notification Service (Amazon SNS) message when the alarm
changes state. An alarm watches a single metric over a time period that you specify. It
performs one or more actions based on the value of the metric relative to a given threshold
over a number of time periods. The action is a notification sent to an Amazon SNS topic or an
Amazon EC2 Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke actions
simply because they are in a particular state. The state must have changed and have been
maintained for a specified number of time periods.

To create an alarm based on an Amazon Q Business or Q Apps metric, see [Create a CloudWatch Alarm Based on a CloudWatch
Metric](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md").

###### To set an alarm (console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and choose
   **Create Alarm**. This opens the **Create Alarm
   Wizard**.
3. Choose **Select metric**.
4. In the **All metrics** tab, choose an AWS/QBusiness or
   AWS/QApps metric for your application, index, and data source. Also set the time as
   set number of hours, days, weeks, or custom.
5. Choose your statistic. For example, **Average**. Also choose your
   alarm trigger time period as a set number of minutes, hours, per day, or custom.
6. Choose your threshold to trigger the alarm, whether to use a static value or a band
   and the condition to meet for the threshold.
7. Choose the alarm state for the trigger, whether the metric must fall outside your
   set threshold, or another state. Select who/which email to send the alarm notification
   to.
8. Choose **Next**. Add a name and optional description for your
   alarm. Choose **Next**.
9. Choose **Create Alarm**.
