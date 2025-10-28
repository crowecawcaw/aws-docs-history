# Logging and monitoring in MediaPackage

Monitoring is an important part of maintaining the reliability, availability, and performance
of MediaPackage and your other AWS solutions. AWS provides the following monitoring tools to watch
MediaPackage, report when something is wrong, and take automatic actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications that you
  run on AWS in real-time. You can collect and track metrics, create customized dashboards, and
  set alarms that notify you or take actions when a specified metric reaches a threshold that you
  specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances
  and automatically launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of
  your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls were
  made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring AWS Elemental MediaPackage with EventBridge
  events](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md")
- [Logging AWS Elemental MediaPackage API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Access logging](access-logging.md "access-logging.md")
- [Monitoring manifest update time in
  AWS Elemental MediaPackage](monitoring-manifest-last-updated.md "monitoring-manifest-last-updated.md")
- [MediaPackage response headers](response-headers.md "response-headers.md")
