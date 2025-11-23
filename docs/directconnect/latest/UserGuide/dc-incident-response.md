# Logging and monitoring in AWS Direct Connect

You can use the following automated monitoring tools to watch
Direct Connect and report when something is wrong:

- **Amazon CloudWatch Alarms** – Watch a single metric over a
  time period that you specify. Perform one or more actions based on the value
  of the metric relative to a given threshold over a number of time periods.
  The action is a notification sent to an Amazon SNS topic. CloudWatch alarms do not
  invoke actions simply because they are in a particular state; the state must
  have changed and been maintained for a specified number of periods. For more
  information, see [Monitor with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **AWS CloudTrail Log Monitoring** – Share log files between accounts and
  monitor CloudTrail log files in real time by sending them to CloudWatch Logs. You can also
  write log processing applications in Java and validate that your log files
  have not changed after delivery by CloudTrail. For more information, see [Log Direct Connect API calls using AWS CloudTrail](logging_dc_api_calls.md "logging_dc_api_calls.md")
  and [Working
  with CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the
  _AWS CloudTrail User Guide_.
  For more information, see [Monitor Direct Connect resources](monitoring-overview.md "monitoring-overview.md").
