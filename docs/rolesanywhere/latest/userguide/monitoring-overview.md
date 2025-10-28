# AWS services for monitoring IAM Roles Anywhere

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Identity and Access Management Roles Anywhere and your other AWS solutions. AWS provides the following monitoring
tools to watch IAM Roles Anywhere, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a threshold
  that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your
  Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ can be used to automate your AWS services and respond
  automatically to system events, such as application availability issues or resource changes.
  Events from AWS services are delivered to EventBridge in near real time. You can write simple
  rules to indicate which events are of interest to you and which automated actions to take
  when an event matches a rule. For more information, see [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your
  own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that
  data to targets such as Lambda. This enables you to monitor events that happen in services, and build
  event-driven architectures. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
