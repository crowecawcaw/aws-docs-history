End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Logging and monitoring in SimSpace Weaver

Monitoring is an important part of maintaining the reliability, availability, and performance of
SimSpace Weaver and your other AWS solutions. AWS provides the following monitoring tools to
watch SimSpace Weaver, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log data from your SimSpace Weaver workers,
  CloudTrail, and other sources. CloudWatch Logs can monitor information in the log data and notify you when certain thresholds are
  met. You can also archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [SimSpace Weaver logs in Amazon CloudWatch Logs](cloudwatch-logs.md "cloudwatch-logs.md")
- [Monitoring SimSpace Weaver with Amazon CloudWatch](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md")
- [Logging AWS SimSpace Weaver API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
