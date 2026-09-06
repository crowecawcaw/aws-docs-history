

# Setting up alarms on error logs
<a name="logging-setting-up-alarms"></a>

We recommend setting up a monitoring system on your `ERROR` logs to alert you of consistent failures. You can use Amazon CloudWatch metric filters and alarms to detect error patterns automatically.

**To create an alarm on error logs**

1. Create a metric filter on the `/aws/iotmanagedintegrations/EventLog` log group that matches error-level log entries.

1. Create a CloudWatch alarm on the metric filter that triggers when the error count exceeds your threshold.

1. Configure an Amazon Simple Notification Service topic as the alarm action to receive notifications.

For detailed instructions, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.