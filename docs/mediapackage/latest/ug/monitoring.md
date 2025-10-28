# Logging and monitoring in AWS Elemental MediaPackage

Monitoring is an important part of maintaining the reliability, availability, and performance
of AWS Elemental MediaPackage and your other AWS solutions. AWS provides the following monitoring tools to
watch MediaPackage, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications that you
  run on AWS in real-time. You can collect and track metrics, create customized dashboards, and
  set alarms that notify you or take actions when a specified metric reaches a threshold that you
  specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances
  and automatically launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Events_ delivers a near real-time stream of system events that
  describe changes in AWS resources. CloudWatch Events enables automated event-driven computing, as you can
  write rules that watch for certain events and trigger automated actions in other AWS services
  when these events happen. For more information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of
  your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls were
  made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _AWS Elemental MediaPackage access logs_
  provide detailed records about requests that are made to a channel. Access logs are
  useful for many applications. For example, access log information can be useful in security and
  access audits. For more information, see [Access logging](access-logging.md "access-logging.md").
- _MediaPackage manifest update headers_ indicate when the service last updated the manifest and segment
  sequence in workflows that don't use dynamic ad insertion. MediaPackage includes these custom headers in playback responses. These headers are helpful when troubleshooting issues related to stale manifests. For more information, see [Monitoring manifest update time](monitoring-manifest-last-updated.md "monitoring-manifest-last-updated.md").

###### Topics

- [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch
  metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring AWS Elemental MediaPackage with CloudWatch Events](monitoring-cloudwatch-events.md "monitoring-cloudwatch-events.md")
- [Logging AWS Elemental MediaPackage API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Access logging](access-logging.md "access-logging.md")
- [Monitoring manifest update time](monitoring-manifest-last-updated.md "monitoring-manifest-last-updated.md")
- [Monitoring AWS media services with
  workflow monitor](monitor-with-workflow-monitor.md "monitor-with-workflow-monitor.md")
