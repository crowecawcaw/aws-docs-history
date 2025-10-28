End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Monitoring Tools

AWS provides various tools that you can use to monitor
Elastic Transcoder. You can configure some of these tools to do
the monitoring for you, while some of the tools require manual intervention. We
recommend that you automate monitoring tasks as much as possible.

## Automated Monitoring Tools

You can use the following automated monitoring tools to watch
Elastic Transcoder and report when something is wrong:

- **Amazon CloudWatch Alarms** – Watch a single metric over a time period
  that you specify, and perform one or more actions based on the value of the metric relative
  to a given threshold over a number of time periods. The action is a notification sent to an
  Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms do not invoke actions simply because
  they are in a particular state; the state must have changed and been maintained for a specified
  number of periods. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Amazon CloudWatch Logs** – Monitor, store, and access your log files from AWS CloudTrail
  or other sources. For more information, see [Monitoring Log Files](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md")
  in the _Amazon CloudWatch User Guide_.
- **AWS CloudTrail Log Monitoring** – Share log files
  between accounts, monitor CloudTrail log files in real time by sending them to
  CloudWatch Logs, write log processing applications in Java, and validate that your log
  files have not changed after delivery by CloudTrail. For more information, see
  [Working with
  CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.

## Manual Monitoring Tools

Another important part of monitoring Elastic Transcoder
involves manually monitoring those items that the CloudWatch alarms don't cover. The
Elastic Transcoder, CloudWatch, and other AWS console dashboards
provide an at-a-glance view of the state of your AWS environment. We recommend that
you also check your CloudTrail log files.

- Elastic Transcoder dashboard shows:
  - Pipelines and their status

- CloudWatch home page shows:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to monitor the services you
       care about
      + Graph metric data to troubleshoot issues and discover
       trends
      + Search and browse all your AWS resource metrics
      + Create and edit alarms to be notified of problems
