End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Monitoring and tagging in AWS Elemental MediaStore

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS Elemental MediaStore and your other AWS solutions. AWS provides the
following monitoring tools to watch MediaStore, report when something is wrong, and take
automatic actions when appropriate:

- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you
  specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon CloudWatch_ monitors your AWS resources and the applications
  that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you or take actions when a
  specified metric reaches a threshold that you specify. For example, you can have
  CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically
  launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Events_ delivers a stream of system events that describe
  changes in AWS resources. Typically, AWS services deliver event notifications to
  CloudWatch Events in seconds but can sometimes take a minute or longer. CloudWatch Events enables automated
  event-driven computing, as you can write rules that watch for certain events and
  trigger automated actions in other AWS services when these events happen. For more
  information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").
- _Amazon CloudWatch Logs_ enables you to monitor, store, and access your log
  files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information
  in the log files and notify you when certain thresholds are met. You can also
  archive your log data in highly durable storage. For more information, see the
  [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
  You can also assign metadata to your MediaStore containers in the form of tags. Each
  tag is a label that consists of a key and value that you define. Tags can make it easier to
  manage, search for, and filter resources. You can use tags to organize your AWS resources
  in the AWS Management Console, create usage and billing reports across all of your AWS
  resources, and filter resources during infrastructure automation activities.

###### Topics

- [Logging AWS Elemental MediaStore API calls with
  AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Monitoring AWS Elemental MediaStore with
  Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Tagging AWS Elemental MediaStore resources](tagging.md "tagging.md")
