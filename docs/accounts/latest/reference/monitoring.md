# Monitor your AWS account

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Account Management and your other AWS solutions. AWS provides the following
monitoring tools to watch Account Management, report when something is wrong, and take automatic actions
when appropriate:

- _AWS CloudTrail_ captures (logs) API calls and related events made by
  or on behalf of your AWS account and writes the log files to an Amazon Simple Storage Service (Amazon S3)
  bucket that you specify. This lets you identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls
  occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon EventBridge_ adds additional automation to your AWS services by
  responding automatically to system events, such as application availability issues
  or resource changes. Events from AWS services are delivered to EventBridge in near real
  time. You can write simple rules to indicate which events are of interest to you and
  which automated actions to take when an event matches a rule. For more information,
  see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
