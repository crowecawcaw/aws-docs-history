# Monitoring and tagging in AWS Elemental MediaConnect

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Elemental MediaConnect and your other AWS solutions. AWS provides the
following monitoring tools to watch MediaConnect, report when something is wrong, and take
automatic actions when appropriate:

- _MediaConnect flow source monitoring_ displays detailed
  information about a source stream and its program media. You can view status
  messages about the stream as well as details about the program video, audio, and
  other data. For more information, see the [Monitoring using source metadata](monitor-with-source-stream-monitoring.md "monitor-with-source-stream-monitoring.md") section of this
  guide.
- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you
  specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon EventBridge_ delivers a near real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing, as you can write rules that watch for certain events and trigger
  automated actions in other AWS services when these events happen. For more
  information, see the [Amazon EventBridge User
  Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").
- _Amazon CloudWatch_ monitors your AWS resources and the applications
  that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For example, you can have
  CloudWatch track the number of dropped and unrecovered packets on your AWS Elemental MediaConnect
  flows and automatically notify you when those values exceed a certain number. For
  more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
