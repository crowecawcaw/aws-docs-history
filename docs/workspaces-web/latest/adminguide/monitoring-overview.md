# Monitoring Amazon WorkSpaces Secure Browser

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon WorkSpaces Secure Browser and your other AWS solutions. AWS provides the following
monitoring tools to watch your WorkSpaces Secure Browser portals and their resources, report when something is
wrong, and take automatic actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a specified
  threshold. For example, you can have CloudWatch track CPU usage or other metrics for your Amazon EC2
  instances and automatically launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ lets you monitor, store, and access your log files from
  Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and
  notify you when certain thresholds are met. You can also archive your log data in highly
  durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging WorkSpaces Secure Browser API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [User activity logging in Amazon WorkSpaces Secure Browser](monitoring-logging.md "monitoring-logging.md")
