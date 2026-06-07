# Monitoring RTB Fabric

Monitoring is an important part of maintaining the reliability, availability, and performance of
RTB Fabric and your other AWS solutions. AWS provides the following monitoring tools to
watch RTB Fabric, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _RTB Fabric vended logs_ deliver application logs through an AWS-managed pipeline to
  Amazon S3, Amazon CloudWatch Logs, or Amazon Data Firehose. Use these logs to analyze how the service processes requests on your
  links. For more information, see [Logging RTB Fabric link activity using vended logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").
- _Amazon CloudWatch Logs_ lets you monitor, store, and access log files. As one RTB Fabric vended-log
  destination, CloudWatch Logs supports live querying with CloudWatch Logs Insights and CloudWatch alarms. You can also archive your log data in
  highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
