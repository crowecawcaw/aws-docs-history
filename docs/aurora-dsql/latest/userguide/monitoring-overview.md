# Monitoring and logging for Aurora DSQL

Monitoring and logging is an important part of maintaining the reliability, availability, and
performance of your Amazon Aurora DSQL resources. You should monitor and collect logging data from all parts of your
Aurora DSQL resources so you can easily debug a multi-point failure.

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage
  or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of
  your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls were
  made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
