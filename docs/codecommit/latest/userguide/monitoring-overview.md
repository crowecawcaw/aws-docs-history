# Monitoring AWS CodeCommit

Monitoring is an important part of maintaining the reliability, availability, and performance of
CodeCommit and your other AWS solutions. AWS provides the following monitoring tools to
watch CodeCommit, report when something is wrong, and take automatic actions when
appropriate:

- Amazon EventBridge can be used to automate your AWS services and respond automatically to system
  events, such as application availability issues or resource changes. Events from AWS
  services are delivered to EventBridge in near real time. You can write simple rules to indicate
  which events are of interest to you and which automated actions to take when an event
  matches a rule. For more information, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") and [Monitoring CodeCommit events in Amazon EventBridge and Amazon CloudWatch Events](monitoring-events.md "monitoring-events.md").
- Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS
  resources. CloudWatch Events enables automated event-driven computing, as you can write rules that watch for certain events and
  trigger automated actions in other AWS services when these events happen. For more information, see the
  [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md") and [Monitoring CodeCommit events in Amazon EventBridge and Amazon CloudWatch Events](monitoring-events.md "monitoring-events.md").
- Amazon CloudWatch Logs can be used to monitor, store, and access your log files from CloudTrail and other
  sources. CloudWatch Logs can monitor information in the log files and notify you when certain
  thresholds are met. You can also archive your log data in highly durable storage. For more
  information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- AWS CloudTrail captures API calls and related events made by or on behalf of your Amazon Web Services account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") and [Logging AWS CodeCommit API calls with AWS CloudTrail](integ-cloudtrail.md "integ-cloudtrail.md").
