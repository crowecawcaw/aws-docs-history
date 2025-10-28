# Monitoring AWS Glue

Monitoring is an important part of maintaining the reliability, availability,
and performance of AWS Glue and your other AWS solutions. AWS provides monitoring tools that
you can use to watch AWS Glue, report when something is wrong, and take action automatically when
appropriate:

You can use the following automated monitoring tools to watch
AWS Glue and report when something is wrong:

- **Amazon CloudWatch Events** delivers a near real-time stream of system
  events that describe changes in AWS resources. CloudWatch Events enables automated event-driven
  computing. You can write rules that watch for certain events and trigger automated actions
  in other AWS services when these events occur. For more information, see the
  [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").
- **Amazon CloudWatch Logs** enables you to monitor, store, and access
  your log files from Amazon EC2 instances, AWS CloudTrail, and other sources. CloudWatch Logs can monitor
  information in the log files and notify you when certain thresholds are met. You can also
  archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- **AWS CloudTrail** captures API calls and related events made
  by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that
  you specify. You can identify which users and accounts call AWS, the source IP address
  from which the calls are made, and when the calls occur. For more information, see the
  [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
  Additionally, you have access to the following insights in the AWS Glue console to help you debug and profile
  jobs:

- Spark jobs – you can see a visualization of selected CloudWatch metrics series, and newer jobs have access to the
  Spark UI. For more information, see [Monitoring AWS Glue Spark jobs](monitor-spark.md "monitor-spark.md").
- Ray jobs – you can see a visualization of selected CloudWatch metrics series. For more information, see [Monitoring Ray jobs with metrics](author-job-ray-monitor.md "author-job-ray-monitor.md").

###### Topics

- [AWS tags in AWS Glue](monitor-tags.md "monitor-tags.md")
- [Automating AWS Glue with EventBridge](automating-awsglue-with-cloudwatch-events.md "automating-awsglue-with-cloudwatch-events.md")
- [Monitoring AWS Glue resources](monitor-resource-metrics.md "monitor-resource-metrics.md")
- [Logging AWS Glue API calls with AWS CloudTrail](monitor-cloudtrail.md "monitor-cloudtrail.md")
