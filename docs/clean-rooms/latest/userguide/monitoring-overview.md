# Monitoring AWS Clean Rooms

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Clean Rooms and your other AWS solutions. AWS provides the following
monitoring tools to watch AWS Clean Rooms, report when something is wrong, and take automatic actions
when appropriate:

- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files
  from Amazon EC2 instances, AWS CloudTrail, and other sources. Amazon CloudWatch Logs can monitor information in the
  log files and notify you when certain thresholds are met. You can also archive your log data
  in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

Clean Rooms ML allows cross-account jobs for certain API actions. The AWS account that
started the job receives the AWS CloudTrail audit log event for the job. For more information, see
[IAM behaviors for AWS Clean Rooms ML](ml-behaviors.md "ml-behaviors.md")

- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon EventBridge_ is a serverless event bus service that makes it easy to
  connect your applications with data from a variety of sources. EventBridge delivers a stream of
  real-time data from your own applications, Software-as-a-Service (SaaS) applications, and
  AWS services and routes that data to targets such as Lambda. This enables you to monitor
  events that happen in services, and build event-driven architectures. For more information,
  see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") and the [Amazon EventBridge
  Events Reference](../../../eventbridge/latest/ref/events-ref-cleanrooms.md "../../../eventbridge/latest/ref/events-ref-cleanrooms.md").
