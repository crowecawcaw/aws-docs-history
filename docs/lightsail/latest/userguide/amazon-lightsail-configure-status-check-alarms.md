

# Configure status check alarms for your Lightsail instance
<a name="amazon-lightsail-configure-status-check-alarms"></a>

You can create an alarm that notifies you when a status check fails on your instance, so that you can fix the problem before it affects your applications for long. For more information about status checks, see [View status checks for your Lightsail instance](amazon-lightsail-viewing-instance-status-checks.md).

For details about each alarm setting, such as the threshold, frequency, and duration, see [Create Lightsail instance metric alarms](amazon-lightsail-adding-instance-health-metric-alarms.md).

**Contents**
+ [Choose a status check metric](#status-check-alarm-metrics)
+ [How alarms evaluate status check metrics](#status-check-alarm-periods)
+ [Suggested alarm settings](#suggested-status-check-alarm-settings)
+ [Create a status check alarm](#creating-status-check-alarms)

## Choose a status check metric
<a name="status-check-alarm-metrics"></a>

You can create an alarm on any of the following metrics:
+ **Status check failures** – Notifies you when either status check fails. Choose this metric if you want one alarm that covers both checks.
+ **System status check failures** – Notifies you when the system status check fails, which means there is a problem with the AWS infrastructure that your instance runs on.
+ **Instance status check failures** – Notifies you when the instance status check fails, which means there is a problem inside your instance.

You can create up to two alarms per metric. If you want to know which check failed as soon as you get the notification, create one alarm on **System status check failures** and one on **Instance status check failures**.

## How alarms evaluate status check metrics
<a name="status-check-alarm-periods"></a>

Each status check metric reports 0 when the check passes and 1 when it fails, once every minute. Alarms evaluate these metrics as a total over each 5 minute period. A value of 0 for a period means the check passed for the whole period. A value from 1 to 5 is the number of minutes in that period when the check failed.

Because the value is only above 0 when a check fails, you don't need to review historical data to choose a threshold, as you do for other instance metrics. A threshold of 0 with the **Greater than** rule catches any failure.

## Suggested alarm settings
<a name="suggested-status-check-alarm-settings"></a>

To be notified as soon as a status check fails, use the following settings. These are the default settings in the Lightsail console for status check metrics.
+ **Rule**: Greater than
+ **Threshold**: 0
+ **Frequency**: 1 time
+ **Duration**: 5 minutes

With these settings, the alarm triggers when a check fails at any point in a 5 minute period.

The instance status check can report a failure while your instance reboots. If you get notifications for these short failures and don't want them, set **Frequency** to 2 times and **Duration** to 10 minutes. The alarm then triggers only when a check fails in two 5 minute periods in a row.

## Create a status check alarm
<a name="creating-status-check-alarms"></a>

Complete the following steps to create a status check alarm.

**To open the alarm form for a status check metric**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance for which you want to create an alarm.

1. Choose the **Metrics** tab on the instance management page.

1. Under **Metric graphs**, choose **Status check failures**, **System status check failures**, or **Instance status check failures** in the **Select metric** dropdown.

1. In the **Alarms for** section for the metric, choose **Create alarm**.

**To configure and create the alarm**

1. For **Rule**, choose **Greater than**.

1. For **Threshold**, enter **0**.

1. For **Frequency (times)**, enter **1**, or **2** if you don't want notifications for short failures during a reboot.

1. For **Duration**, choose 5 minutes, or 10 minutes if you entered 2 for **Frequency (times)**.

1. (Optional) Under **Also notify me by**, select **Email** to also get an email when the alarm is triggered. If you have not added an email contact in the AWS Region of your instance, the console prompts you to add one. For more information, see [Metric notifications](amazon-lightsail-notifications.md).

   If you select **Email**, you can also select **Send me a notification when the alarm is no longer triggered** under **Additional notifications**, to know when the check passes again.

1. Choose **Save** to create the alarm.

When a status check alarm triggers, see [Troubleshoot failed status checks on your Lightsail instance](amazon-lightsail-instance-status-checks.md).