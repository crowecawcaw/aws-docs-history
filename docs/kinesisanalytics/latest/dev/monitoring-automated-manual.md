After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Monitoring Tools

AWS provides various tools that you can use to monitor
. You can configure some of these tools to do
the monitoring for you, while some of the tools require manual intervention. We
recommend that you automate monitoring tasks as much as possible.

## Automated Monitoring Tools

You can use the following automated monitoring tools to watch
and report when something is wrong:

- **Amazon CloudWatch Alarms** – Watch a single metric over a time period
  that you specify, and perform one or more actions based on the value of the metric relative
  to a given threshold over a number of time periods. The action is a notification sent to an
  Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms do not invoke actions simply because
  they are in a particular state; the state must have changed and been maintained for a specified
  number of periods. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Amazon CloudWatch Logs** – Monitor, store, and access your log files from AWS CloudTrail
  or other sources. For more information, see [Monitoring Log Files](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md")
  in the _Amazon CloudWatch User Guide_.
- **Amazon CloudWatch Events** – Match events and route them to one
  or more target functions or streams to make changes, capture state
  information, and take corrective action. For more information, see [What is Amazon CloudWatch Events](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchEvents.md") in
  the _Amazon CloudWatch User Guide_.
- **AWS CloudTrail Log Monitoring** – Share log files
  between accounts, monitor CloudTrail log files in real time by sending them to
  CloudWatch Logs, write log processing applications in Java, and validate that your log
  files have not changed after delivery by CloudTrail. For more information, see
  [Working with
  CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.

## Manual Monitoring Tools

Another important part of monitoring
involves manually monitoring those items that the CloudWatch alarms don't cover. The
, CloudWatch, Trusted Advisor, and other AWS Management Console dashboards
provide an at-a-glance view of the state of your AWS environment.

- The CloudWatch home page shows the following:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to monitor the services you
       care about
      + Graph metric data to troubleshoot issues and discover
       trends
      + Search and browse all your metrics
      + Create and edit alarms to be notified of problems

- AWS Trusted Advisor can help you monitor your to improve
  performance, reliability, security, and cost effectiveness. Four Trusted Advisor
  checks are available to all users. More than 50 checks are available to
  users with a Business or Enterprise support plan. For more information, see
  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/ "https://aws.amazon.com/premiumsupport/trustedadvisor/").
