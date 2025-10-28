# Monitoring Amazon Keyspaces (for Apache Cassandra)

Monitoring is an important part of maintaining the reliability, availability, and performance of
Amazon Keyspaces and your other AWS solutions. AWS provides the following monitoring tools to
watch Amazon Keyspaces, report when something is wrong, and take automatic actions when
appropriate:

- _Amazon Keyspaces_ offers a preconfigured dashboard in the AWS Management Console showing
  the latency and errors aggregated across all tables in the account.
- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics with customized dashboards. For example, you can create a baseline
  for normal Amazon Keyspaces performance in your environment by measuring performance at various
  times and under different load conditions. As you monitor Amazon Keyspaces, store historical monitoring
  data so that you can compare it with current performance data, identify normal performance
  patterns and performance anomalies, and devise methods to address issues. To establish a baseline, you should,
  at a minimum, monitor for system errors. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch alarms_ monitor a single metric over a time period
  that you specify, and perform one or more actions based on the value of the metric
  relative to a given threshold over a number of time periods. For example if you use Amazon Keyspaces in
  provisioned mode with application auto scaling, the action is a notification sent by the Amazon Simple Notification Service (Amazon SNS)
  to evaluate an Application Auto Scaling policy.

CloudWatch alarms do not invoke actions simply because they are in a particular state. The
state must have changed and been maintained for a specified number of periods. For more
information, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log files from Amazon Keyspaces tables,
  CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are
  met. You can also archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
  _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your
  own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that
  data to targets such as Lambda. This enables you to monitor events that happen in services, and build
  event-driven architectures. For more information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### Topics

- [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging Amazon Keyspaces API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
