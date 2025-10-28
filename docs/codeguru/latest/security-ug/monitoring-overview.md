On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Monitoring Amazon CodeGuru Security

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon CodeGuru Security and your other AWS solutions. AWS provides the following monitoring
tools to watch CodeGuru Security, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon EventBridge_ can be used to automate your AWS services and respond
  automatically to system events, such as application availability issues or resource changes.
  Events from AWS services are delivered to EventBridge in near real time. You can write simple
  rules to indicate which events are of interest to you and which automated actions to take
  when an event matches a rule. For more information, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
