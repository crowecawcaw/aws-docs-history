# Monitoring Amazon FSx for Lustre file systems

Monitoring is an important part of maintaining the reliability, availability, and
performance of your FSx for Lustre file system and your other AWS solutions. Collecting monitoring data from all
parts of your AWS solution allows you to more easily debug a multi-point failure if one
occurs. You can monitor your FSx for Lustre file system, report when
something is wrong, and take action automatically when appropriate using the following tools:

- **Amazon CloudWatch** – Monitors your AWS resources and the
  applications that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you when a specified metric reaches a
  threshold that you specify. For example, you can have CloudWatch track storage capacity or other
  metrics for your Amazon FSx for Lustre instances and automatically launch new instances when needed.
- **Lustre logging** – Monitors the enabled logging events for
  your file system. Lustre logging writes these events to Amazon CloudWatch Logs.
- **AWS CloudTrail** – Captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred.
  The following sections provide information on how to use the tools with your FSx for Lustre file systems.

###### Topics

- [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging with Amazon CloudWatch Logs](cw-event-logging.md "cw-event-logging.md")
- [Logging FSx for Lustre API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
