# Monitoring AWS Glue DataBrew

Monitoring is an important part of maintaining the reliability, availability, and performance of
AWS Glue DataBrew and your other AWS solutions. AWS provides the following monitoring tools to
watch DataBrew, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage
  or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Events_ enables you to set up automatic notifications for specific
  events in DataBrew. Events from DataBrew are delivered to CloudWatch Events in near-real time. You can
  configure CloudWatch Events to monitor events and invoke targets in response to events that
  indicate changes to your resource shares. Changes to a resource share trigger events for
  both the owner of the resource share and the principals that were granted access to the
  resource share. For more information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files from Amazon EC2 instances,
  CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are
  met. You can also archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of
  your AWS account. It then delivers the log files to an Amazon S3 bucket that you specify. You
  can identify which users and accounts called AWS, the source IP address from which the
  calls were made, and when the calls occurred. For more information, see the
  [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitoring DataBrew with Amazon CloudWatch](monitoring.md "monitoring.md")
- [Automating DataBrew with CloudWatch Events](monitoring.md "monitoring.md")
- [Monitoring DataBrew with CloudWatch Logs](#monitoring.cloudwatch-logs "#monitoring.cloudwatch-logs")
- [Logging DataBrew API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Using AWS User Notifications with AWS Glue Databrew](using-user-notifications.md "using-user-notifications.md")

## Monitoring DataBrew with CloudWatch Logs

You can monitor DataBrew jobs using CloudWatch Logs, which collects detailed information from the DataBrew
job subsystem and makes it available for review. These logs can be helpful if you want to gain
insight into the resources your profile and recipe jobs are using, or for troubleshooting
purposes, For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
