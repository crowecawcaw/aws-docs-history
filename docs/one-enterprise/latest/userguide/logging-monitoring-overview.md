# Monitoring Amazon One Enterprise

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon One Enterprise and your other AWS solutions. AWS provides the following
monitoring tools to watch Amazon One Enterprise, report when something is wrong, and take automatic actions
when appropriate:

- _Amazon EventBridge_ can be used to automate your AWS services and respond
  automatically to system events, such as application availability issues or resource changes.
  Events from AWS services are delivered to EventBridge in near real time. You can write simple
  rules to indicate which events are of interest to you and which automated actions to take
  when an event matches a rule. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
