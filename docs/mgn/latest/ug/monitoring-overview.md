NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Monitoring Application Migration

Service

Monitoring is an important part of maintaining the reliability, availability, and
performance of Application Migration Service and your other AWS
solutions. AWS provides the following monitoring tools to watch Application
Migration Service, report when something is wrong, and take automatic actions
when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a threshold
  that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your
  Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Events_ delivers a near real-time stream of system events that
  describe changes in AWS resources. CloudWatch Events allows automated event-driven computing, as you
  can write rules that watch for certain events and trigger automated actions in other AWS
  services when these events happen. For more information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").
- _Amazon CloudWatch Logs_ allows you to monitor, store, and access your log files
  from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log
  files and notify you when certain thresholds are met. You can also archive your log data in
  highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
