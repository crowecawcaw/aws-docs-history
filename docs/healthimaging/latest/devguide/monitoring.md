# Monitoring AWS HealthImaging

Monitoring and logging are important parts of maintaining the security, reliability,
availability, and performance of AWS HealthImaging. AWS provides the following logging and monitoring
tools to watch HealthImaging, report when something is wrong, and take automatic actions when
appropriate:

- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _Amazon CloudWatch_ monitors your AWS resources and the applications you run
  on AWS in real time. You can collect and track metrics, create customized dashboards, and
  set alarms that notify you or take actions when a specified metric reaches a threshold that
  you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2
  instances and automatically launch new instances when needed. For more information, see the
  [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon EventBridge_ is a serverless event bus service that makes it easy to
  connect your applications with data from a variety of sources. EventBridge delivers a stream of
  real-time data from your own applications, Software-as-a-Service (SaaS) applications, and
  AWS services and routes that data to targets such as Lambda. This enables you to monitor
  events that happen in services, and build event-driven architectures. For more information,
  see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### Topics

- [Using AWS CloudTrail with HealthImaging](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Using Amazon CloudWatch with HealthImaging](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Using Amazon EventBridge with HealthImaging](event-notifications.md "event-notifications.md")
