# Logging and monitoring in AWS Network Firewall

Logging and monitoring helps you maintain the reliability, availability, and performance
of AWS Network Firewall. You can monitor how the service is being used and you can monitor
network traffic and traffic filtering in your Network Firewall firewalls.

AWS provides a number of tools that you can use to monitor Network Firewall. You can
configure some of these tools to do the monitoring for you, while other tools require manual
intervention. We recommend that you automate monitoring tasks as much as possible.

###### Automated monitoring tools that work with Network Firewall

You can use the following automated monitoring tools with Network Firewall:

- _Amazon CloudWatch_ provides metrics for the AWS resources and the
  applications that you run on AWS. Monitoring and alarms are real time. You can
  collect and track metrics, create customized dashboards, and set alarms that notify
  you or take actions when a specified metric reaches a threshold that you specify.
  For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2
  instances and automatically launch new instances when needed. For more information,
  see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").
- _Amazon CloudWatch Logs_ provides logging for sources such as Amazon EC2
  instances and CloudTrail. CloudWatch Logs can monitor information in the log files and notify you
  when certain thresholds are met. You can also archive your log data in highly
  durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").
- _AWS CloudTrail_ captures API calls and related events made by or on
  behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you
  specify. You can identify which users and accounts called AWS, the source IP
  address from which the calls were made, and when the calls occurred. For more
  information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- _AWS Config_ lets you view the configuration of your AWS
  resources in your AWS account. The available information includes how the
  resources are related to one another and how they were configured in the past, so
  that you can see how the configurations and relationships change over time. For more
  information, see the [AWS Config Developer
  Guide](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md").

###### Monitoring and reporting options native to AWS Network Firewall

In addition to automated monitoring tools, you can access the following
monitoring and reporting capabilities to analyze your network traffic directly
from the Network Firewall console:

- Firewall request graph of packets monitored
- Firewall monitoring dashboard for flow and alert logs
- Traffic analysis mode and report generation

###### Note

Firewall monitoring and traffic analysis mode each have specific prerequisites and configuration.
For information, see [Monitoring and reporting in Network Firewall](nwfw-monitoring-reporting.md "nwfw-monitoring-reporting.md").

Review the topics in this guide to learn more about the different logging, monitoring, and reporting capabilities you can use with Network Firewall.

###### Topics

- [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md")
- [Logging calls to the AWS Network Firewall API with
  AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring and reporting in Network Firewall](nwfw-monitoring-reporting.md "nwfw-monitoring-reporting.md")
