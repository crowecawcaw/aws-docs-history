# Monitoring and metrics for Amazon EventBridge Scheduler

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon EventBridge Scheduler and your other AWS solutions. AWS provides the following monitoring
tools to watch EventBridge Scheduler, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a threshold
  that you specify. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitoring Amazon EventBridge Scheduler with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging Amazon EventBridge Scheduler API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
