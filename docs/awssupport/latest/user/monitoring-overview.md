# Monitoring and logging for AWS Support

Monitoring is an important part of maintaining the reliability, availability, and
performance of Support and your other AWS solutions. AWS provides the following monitoring
tools to watch Support, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon EventBridge_ delivers a near real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing, as you can write rules that watch for certain events and trigger
  automated actions in other AWS services when these events happen. For more
  information, see the [Amazon EventBridge User
  Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").
- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you
  specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Integrating AWS Support into event-driven applications using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md")
- [Logging AWS Support API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Logging AWS Support App in Slack API calls using
  AWS CloudTrail](logging-using-cloudtrail-support-app.md "logging-using-cloudtrail-support-app.md")
