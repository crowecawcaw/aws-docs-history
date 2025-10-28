# Monitoring Amazon FSx for OpenZFS file systems

Monitoring is an important part of maintaining the reliability, availability, and
performance of your FSx for OpenZFS file system and your other AWS solutions. Collecting monitoring data from all
parts of your AWS solution allows you to more easily debug a multi-point failure if one
occurs. You can monitor your FSx for OpenZFS file system, report when
something is wrong, and take action automatically when appropriate using the following tools:

- **Amazon CloudWatch** – Monitors your AWS resources and the
  applications that you run on AWS in real time. You can collect and track metrics, create
  customized dashboards, and set alarms that notify you when a specified metric reaches a
  threshold that you specify. For example, you can have CloudWatch track storage capacity or other
  metrics for your Amazon FSx instances and automatically launch new instances when needed.
- **AWS CloudTrail** – Captures API calls and related events made by or on behalf of your AWS account
  and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called
  AWS, the source IP address from which the calls were made, and when the calls occurred.
  The following sections provide information on how to use both Amazon CloudWatch and AWS CloudTrail with your FSx for OpenZFS file systems.

###### Topics

- [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging FSx for OpenZFS API calls with AWS CloudTrail](logging-using-cloudtrail-win.md "logging-using-cloudtrail-win.md")
