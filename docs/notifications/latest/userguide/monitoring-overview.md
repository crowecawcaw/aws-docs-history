# Monitoring AWS User Notifications

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS User Notifications and your other AWS solutions. AWS provides the following monitoring
tools to watch User Notifications, report problems, and take automatic actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications that
  you run on AWS in real time. You can collect and track metrics, and create customized
  dashboards. You can also set alarms that notify you or act automatically when a specified
  metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage
  or other metrics of your Amazon EC2 instances. When demand on your instances reaches a set
  threshold, CloudWatch can automatically launch new instances as needed. For more information, see
  the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account. It then delivers these log files to an Amazon S3 bucket that you specify.
  You can identify which users and accounts called AWS, the source IP address that the calls
  were made from, and when the calls occurred. For more information, see the
  [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
