# Logging and monitoring in AWS Support and AWS Trusted Advisor

Monitoring is an important part of maintaining the reliability, availability, and performance
of AWS Support and AWS Trusted Advisor and your other AWS solutions. AWS provides the following monitoring tools to
watch AWS Support and AWS Trusted Advisor, report when something is wrong, and take actions when appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications that you
  run on AWS in real time. You can collect and track metrics, create customized dashboards, and
  set alarms that notify you or take actions when a specified metric reaches a threshold that you
  specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon Elastic Compute Cloud
  (Amazon EC2) instances and automatically launch new instances when needed. For more information, see
  the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ delivers a near real-time stream of system events
  that describe changes in AWS resources. EventBridge enables automated event-driven
  computing, as you can write rules that watch for certain events and trigger
  automated actions in other AWS services when these events happen. For more
  information, see the [Amazon EventBridge User
  Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of
  your AWS account and delivers the log files to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. You
  can identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
  For more information, see [Monitoring and logging for AWS Support](monitoring-overview.md "monitoring-overview.md") and [Monitoring and logging for AWS Trusted Advisor](cloudwatch-ta.md "cloudwatch-ta.md").
