# Monitoring Amazon Q Business and Q Apps

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Q Business and your other AWS solutions. AWS provides the
following monitoring tools to monitor Amazon Q Business, report when something is wrong,
and take automatic actions when appropriate:

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
- You can use [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to monitor
  and analyze user conversations and response feedback in Amazon Q Business. CloudWatch Logs can deliver logs to
  multiple locations, such as Amazon CloudWatch, Amazon S3, or Amazon Data Firehose (standard rates apply). We recommend
  that you set up conversation and feedback logging with Amazon CloudWatch within five minutes of
  creating your Amazon Q Business Application environment. For more information, see [Monitoring Amazon Q Business user conversations with
  Amazon CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").

###### Topics

- [Logging Amazon Q Business API calls using
  AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [Logging Amazon Q Apps API calls using
  AWS CloudTrail](logging-qapps-using-cloudtrail.md "logging-qapps-using-cloudtrail.md")
- [Monitoring Amazon Q Business and Amazon Q Apps
  with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring Amazon Q Business user conversations with
  Amazon CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md")
- [Viewing Amazon Q Business and Q App metrics in analytics
  dashboards](analytics-dashboard.md "analytics-dashboard.md")
