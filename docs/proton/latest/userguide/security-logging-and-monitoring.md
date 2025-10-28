End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Logging and monitoring in AWS Proton

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Proton and your other AWS solutions.
AWS provides the following monitoring tools to watch your instances running in AWS Proton, report when something is wrong, and take automatic
actions when appropriate.

At this time, AWS Proton itself is not integrated with Amazon CloudWatch Logs or AWS Trusted Advisor. Administrators can configure and use CloudWatch to monitor
other AWS services as defined in their service and environment templates. AWS Proton is integrated with AWS CloudTrail.

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real time. You can collect and
  track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a
  threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically
  launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other
  sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are met. You can also archive your log
  data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account and delivers the log
  files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the
  calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your applications with data from a
  variety of sources. EventBridge delivers a stream of real-time data from your own applications, Software-as-a-Service (SaaS) applications,
  and AWS services and routes that data to targets such as Lambda. This enables you to monitor events that happen in services, and
  build event-driven architectures. For more information, see [Automate AWS Proton with EventBridge](event-bridge.md "event-bridge.md") and the [EventBridge User Guide](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md").
