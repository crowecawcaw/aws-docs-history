# Monitoring FSx for Windows File Server file systems

Monitoring is an important part of maintaining the reliability, availability, and
performance of FSx for Windows File Server and your AWS solutions. You should collect monitoring data from all
parts of your AWS solution so that you can more easily debug a failure if one
occurs. However, before you start monitoring FSx for Windows File Server, you should create a monitoring plan
that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  For more information about logging and monitoring in FSx for Windows File Server, see the following topics.

###### Topics

- [Automated and manual monitoring](#monitoring_automated_manual "#monitoring_automated_manual")
- [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging Amazon FSx for Windows File Server API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")

## Automated and manual monitoring

AWS provides various tools that you can use to monitor FSx for Windows File Server. You can configure
some of these tools to do the monitoring for you, whereas some of the tools require manual
intervention. We recommend that you automate monitoring tasks as much as possible.

### Automated monitoring tools

You can use the following automated monitoring tools to watch FSx for Windows File Server and report
when something is wrong:

- **Amazon CloudWatch Alarms** – Watch a single metric over a time period
  that you specify, and perform one or more actions based on the value of the metric relative
  to a given threshold over a number of time periods. The action is a notification sent to an
  Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms do not invoke actions simply because
  they are in a particular state; the state must have changed and been maintained for a specified
  number of periods. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Amazon CloudWatch Logs** – Monitor, store, and access your log files from AWS CloudTrail
  or other sources. For more information, see [What Is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
  in the _Amazon CloudWatch Logs User Guide_.
- **AWS CloudTrail Log Monitoring** – Share log files
  between accounts, monitor CloudTrail log files in real time by sending them to
  CloudWatch Logs, write log processing applications in Java, and validate that your log
  files have not changed after delivery by CloudTrail. For more information, see
  [Working with
  CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.

### Manual monitoring tools

Another important part of monitoring FSx for Windows File Server involves manually monitoring those
items that the Amazon CloudWatch alarms don't cover. The FSx for Windows File Server, CloudWatch, and other AWS console
dashboards provide an at-a-glance view of the state of your AWS environment.

Amazon FSx **Monitoring & performance** dashboard shows:

- Current warnings and CloudWatch alarms
- A summary of file system activity
- File system storage capacity and utilization
- File server and storage volume performance
- CloudWatch alarms

Amazon CloudWatch Dashboard shows:

- Current alarms and status
- Graphs of alarms and resources
- Service health status

In addition, you can use CloudWatch to do the following:

- Create [customized
  dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to monitor the services you use.
- Graph metric data to troubleshoot issues and discover trends.
- Search and browse all your AWS resource metrics.
- Create and edit alarms to be notified of problems.

For more information about the Amazon FSx **Monitoring & performance** dashboard,
see [Using file system metrics](monitoring-cloudwatch.md#how_to_use_metrics "monitoring-cloudwatch.md#how_to_use_metrics").
