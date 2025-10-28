# Monitoring AWS B2B Data Interchange

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS B2B Data Interchange and your other AWS solutions. AWS provides the following
monitoring tools to watch AWS B2B Data Interchange, report when something is wrong, and take automatic
actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications
  you run on AWS in real time. You can collect and track metrics, create customized
  dashboards, and set alarms that notify you or take actions when a specified metric
  reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage
  or other metrics of your Amazon EC2 instances and automatically launch new instances when
  needed. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log
  files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information
  in the log files and notify you when certain thresholds are met. You can also
  archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _Amazon EventBridge_ can be used to automate your AWS services and
  respond automatically to system events, such as application availability issues or
  resource changes. Events from AWS services are delivered to EventBridge in near real
  time. You can write simple rules to indicate which events are of interest to you and
  which automated actions to take when an event matches a rule. For more information,
  see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you
  specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Monitoring AWS B2B Data Interchange events in Amazon EventBridge

You can monitor AWS B2B Data Interchange events in EventBridge, which delivers a stream of real-time
data from your own applications, software-as-a-service (SaaS) applications, and AWS
services. EventBridge routes that data to targets such as AWS Lambda and Amazon Simple Notification Service. These events
are the same as those that appear in Amazon CloudWatch Events, which delivers a near real-time stream
of system events that describe changes in AWS resources.
