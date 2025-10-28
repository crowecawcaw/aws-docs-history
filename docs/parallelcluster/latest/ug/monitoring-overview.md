# Monitoring AWS ParallelCluster and logs

Monitoring is an important part of maintaining the reliability, availability, and performance of
AWS ParallelCluster and your other AWS solutions. AWS provides the following monitoring tools to
watch AWS ParallelCluster, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage
  or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files from Amazon EC2 instances,
  CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are
  met. You can also archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your
  own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that
  data to targets such as Lambda. This enables you to monitor events that happen in services, and build
  event-driven architectures. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### Topics

- [Integration with Amazon CloudWatch Logs](cloudwatch-logs-v3.md "cloudwatch-logs-v3.md")
- [Amazon CloudWatch dashboard](cloudwatch-dashboard-v3.md "cloudwatch-dashboard-v3.md")
- [Amazon CloudWatch alarms for cluster metrics](cloudwatch-alarms-v3.md "cloudwatch-alarms-v3.md")
- [AWS ParallelCluster configured log rotation](log-rotation-v3.md "log-rotation-v3.md")
- [pcluster CLI logs](troubleshooting-v3-pc-cli-logs.md "troubleshooting-v3-pc-cli-logs.md")
- [Amazon EC2 console output logs](console-logs-v3.md "console-logs-v3.md")
- [Retrieve PCUI and AWS ParallelCluster runtime logs](troubleshooting-v3-get-runtime-logs.md "troubleshooting-v3-get-runtime-logs.md")
- [Retrieving and preserving logs](troubleshooting-v3-get-logs.md "troubleshooting-v3-get-logs.md")
