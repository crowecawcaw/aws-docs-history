# Logging and monitoring in AWS Identity and Access Management

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Identity and Access Management (IAM), AWS Security Token Service (AWS STS) and your other AWS solutions. AWS provides several tools for
monitoring your AWS resources and responding to potential incidents:

- _AWS CloudTrail_ captures all API calls for IAM and AWS STS as events,
  including calls from the console and API calls. To learn more about using CloudTrail with IAM
  and AWS STS, see [Logging IAM and AWS STS API calls
  with AWS CloudTrail](cloudtrail-integration.md "cloudtrail-integration.md"). For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _AWS Identity and Access Management and Access Analyzer_ helps you identify the resources in your
  organization and accounts, such as Amazon S3 buckets or IAM roles, that are shared with an
  external entity. This helps you identify unintended access to your resources and data, which
  is a security risk. To learn more, see [What is IAM Access Analyzer?](what-is-access-analyzer.md "what-is-access-analyzer.md")
- _Amazon CloudWatch_ monitors your AWS resources and the applications that
  you run on AWS in real time. You can collect and track metrics, create customized
  dashboards, and set alarms that notify you or take actions when a specified metric reaches a
  threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics
  of your Amazon EC2 instances and automatically launch new instances when needed. For more
  information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ helps you monitor, store, and access your log files from
  Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and
  notify you when certain thresholds are met. You can also archive your log data in highly
  durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
  For additional resources and security best practices for IAM, see [Security best practices and use cases in
  AWS Identity and Access Management](best-practices-use-cases.md "best-practices-use-cases.md").

###### Topics

- [Logging IAM and AWS STS API calls
  with AWS CloudTrail](cloudtrail-integration.md "cloudtrail-integration.md")
- [Track privileged tasks in
  AWS CloudTrail](cloudtrail-track-privileged-tasks.md "cloudtrail-track-privileged-tasks.md")
