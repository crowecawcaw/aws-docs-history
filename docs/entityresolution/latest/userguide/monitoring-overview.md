# Monitoring AWS Entity Resolution

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Entity Resolution and your other AWS solutions. AWS provides the following
monitoring tools to watch AWS Entity Resolution, report when something is wrong, and take automatic actions
when appropriate:

- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP discuss from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon CloudWatch Logs_ enables you to check, store, and access your logs from
  Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can check information in the log files and
  tell you when certain thresholds are met. You can also archive your log data in highly
  durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

###### Topics

- [Logging AWS Entity Resolution API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Monitoring and logging workflows using Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md")
