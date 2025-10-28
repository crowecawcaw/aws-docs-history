**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Logging and monitoring in Amazon Chime

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Chime and your other AWS solutions. AWS provides the following tools to
monitor Amazon Chime, report issues, and take automatic actions when appropriate:

- _Amazon CloudWatch_ monitors in real time your AWS resources and the
  applications that you run on AWS. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For example, you can have
  CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically
  launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ delivers a near real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing. This lets you write rules that watch for certain events, and trigger
  automated actions in other AWS services when these events happen. For more
  information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _Amazon CloudWatch Logs_ lets you monitor, store, and access your log files
  from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the
  log files and notify you when certain thresholds are met. You can also archive your
  log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account. It then delivers the log files to an Amazon S3 bucket that
  you specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Monitoring Amazon Chime with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Automating Amazon Chime with
  EventBridge](automating-chime-with-cloudwatch-events.md "automating-chime-with-cloudwatch-events.md")
- [Logging Amazon Chime API calls with
  AWS CloudTrail](cloudtrail.md "cloudtrail.md")
