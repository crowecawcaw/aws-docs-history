Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Monitoring Lookout for Metrics

Monitoring is an important part of ensuring the reliability, availability, and performance of Amazon Lookout for Metrics and your
other AWS solutions. AWS provides the following monitoring tools to watch Lookout for Metrics, report when something is wrong, and
take automatic actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real
  time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take
  actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU
  usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more
  information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS
  account and optionally delivers the log files to an Amazon S3 bucket that you specify. You can identify which users
  and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred.
  For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Viewing Amazon Lookout for Metrics API activity in CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md")
- [Monitoring Lookout for Metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
