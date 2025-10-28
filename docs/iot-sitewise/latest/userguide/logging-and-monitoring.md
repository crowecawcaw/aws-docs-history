# Log and monitor in AWS IoT SiteWise

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS IoT SiteWise and your other AWS solutions. AWS IoT SiteWise supports the following monitoring
tools to watch the service, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications that
  you run on AWS in real time. Collect and track metrics, create customized
  dashboards, and set alarms that notify you or take actions when a specified metric reaches a
  certain threshold. For example, you can have CloudWatch track CPU usage or other metrics
  of your Amazon EC2 instances and automatically launch new instances when needed. For more
  information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ monitors, stores, and accesses your log files from SiteWise Edge
  gateways, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify
  you when certain thresholds are met. You can also archive your log data in highly durable
  storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account. Then CloudTrail delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitor with Amazon CloudWatch Logs](monitor-cloudwatch-logs.md "monitor-cloudwatch-logs.md")
- [Monitor SiteWise Edge gateway logs](monitor-gateway-logs.md "monitor-gateway-logs.md")
- [Monitor AWS IoT SiteWise with Amazon CloudWatch metrics](monitor-cloudwatch-metrics.md "monitor-cloudwatch-metrics.md")
- [Log AWS IoT SiteWise API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
