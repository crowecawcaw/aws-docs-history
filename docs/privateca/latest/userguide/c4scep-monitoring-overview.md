# Monitor Connector for SCEP

Monitoring is an important part of maintaining the reliability, availability, and performance of
Connector for SCEP and your other AWS solutions. AWS provides the following monitoring tools to
watch Connector for SCEP, report when something is wrong, and take automatic actions when
appropriate:

- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS APIs, the source IP address from which the calls were made, and when the calls occurred.

If you monitor CloudTrail data events, the logs contain the list of all recent requests from client devices. Data events come with identifying client device information such as IP address, the type of operation performed, and the error code and detailed message if the operation results in a `failed` status. For more information, see
the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

- _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your
  own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that
  data to targets such as Lambda and CloudWatch Logs. This enables you to monitor events that happen in services, and build
  event-driven architectures. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### Topics

- [Automate Connector for SCEP using EventBridge](c4scep-monitor-eventbridge-events.md "c4scep-monitor-eventbridge-events.md")
- [Log Connector for SCEP API calls using AWS CloudTrail](logging-using-cloudtrail-c4scep.md "logging-using-cloudtrail-c4scep.md")
