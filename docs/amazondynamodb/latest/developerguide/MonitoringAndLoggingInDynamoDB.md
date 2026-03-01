# Monitoring and logging in DynamoDB

Monitoring is an important part of maintaining the reliability, availability, and
performance of DynamoDB and your AWS solutions. You should collect monitoring data from all parts of your AWS
solutions so you can easily debug a multi-point failure.

###### Topics

- [Monitoring plan](#monitoring-plan "#monitoring-plan")
- [Performance baseline](#performance-baseline "#performance-baseline")
- [Integrated services](#integrated-services "#integrated-services")
- [Automated monitoring tools](#automated-monitoring-tools "#automated-monitoring-tools")
- [Monitoring metrics in DynamoDB with Amazon CloudWatch](Monitoring-metrics-with-Amazon-CloudWatch.md "Monitoring-metrics-with-Amazon-CloudWatch.md")
- [Logging DynamoDB operations by using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Analyzing data access using CloudWatch contributor insights for DynamoDB](contributorinsights.md "contributorinsights.md")

## Monitoring plan

Before you start monitoring DynamoDB, create a monitoring plan that includes
answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?

## Performance baseline

Establish a baseline for normal DynamoDB performance in your environment,
by measuring performance at various times and under different load conditions.
As you monitor DynamoDB, you should consider storing historical monitoring data.
This stored data will give you a baseline from which to compare current performance
data, identify normal performance patterns and performance anomalies, and devise
methods to address issues. To establish a baseline you should, at a minimum, monitor
the following items:

- The number of read or write capacity units consumed over the specified time period,
  so you can track how much of your provisioned throughput is used.
- Requests that exceeded a table's provisioned write or read capacity during the
  specified time period, so you can determine which requests exceed the provisioned
  throughput quotas of a table.
- System errors, so you can determine if any requests resulted in an error.

## Integrated services

DynamoDB automatically monitors your tables on your behalf and reports metrics through
Amazon CloudWatch. Additionally, DynamoDB integrates with the following AWS services to help
you monitor and troubleshoot your DynamoDB resources.

- AWS CloudTrail captures API calls and related events made by or on behalf of your
  AWS account and delivers the log files to an Amazon S3 bucket that you specify. For
  more information, see [Logging DynamoDB operations by using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- Contributor Insights is a diagnostic tool for identifying the most frequently
  accessed and throttled keys in your table or index at a glance. For more information,
  see [Analyzing data access using CloudWatch contributor insights for DynamoDB](contributorinsights.md "contributorinsights.md").

## Automated monitoring tools

AWS provides various tools that you can use to monitor DynamoDB. We recommend
that you automate monitoring tasks as much as possible. You can use the following automated
monitoring tools to watch DynamoDB and report when something is wrong:

- **Amazon CloudWatch alarms** – Watch a single metric over a time
  period that you specify, and perform one or more actions based on the value of the metric
  relative to a given threshold over a number of time periods.

The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto
Scaling policy. Amazon CloudWatch alarms do not invoke actions simply because they are in a particular
state; the state must have changed and been maintained for a specified number of periods.
For more information, see
[Monitoring metrics in DynamoDB with Amazon CloudWatch](Monitoring-metrics-with-Amazon-CloudWatch.md "Monitoring-metrics-with-Amazon-CloudWatch.md").

- **AWS CloudTrail log monitoring** – Share log files between
  accounts, monitor AWS CloudTrail log files in real time by sending them to AWS CloudTrail Logs, write
  log processing applications in Java, and validate that your log files haven't changed
  after delivery by AWS CloudTrail. For more information, see [What is Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the _AWS CloudTrail User
  Guide_.
