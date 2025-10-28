For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Monitoring tools

AWS provides various tools that you can use to monitor Timestream for LiveAnalytics. You can configure some of
these tools to do the monitoring for you, while some of the tools require manual intervention.
We recommend that you automate monitoring tasks as much as possible.

###### Topics

- [Automated monitoring tools](#monitoring-automated_tools "#monitoring-automated_tools")
- [Manual monitoring tools](#monitoring-manual-tools "#monitoring-manual-tools")

## Automated monitoring tools

You can use the following automated monitoring tools to watch Timestream for LiveAnalytics and report when
something is wrong:

- **Amazon CloudWatch Alarms** – Watch a single metric over a time
  period that you specify, and perform one or more actions based on the value of the
  metric relative to a given threshold over a number of time periods. The action is a
  notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms do not
  invoke actions simply because they are in a particular state; the state must have
  changed and been maintained for a specified number of periods. For more information, see
  [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Manual monitoring tools

Another important part of monitoring Timestream for LiveAnalytics involves manually monitoring those items that
the CloudWatch alarms don't cover. The Timestream for LiveAnalytics, CloudWatch, Trusted Advisor, and other AWS Management Console dashboards provide
an at-a-glance view of the state of your AWS environment.

- The CloudWatch home page shows the following:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized
       dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to monitor the services you care about
      + Graph metric data to troubleshoot issues and discover trends
      + Search and browse all your AWS resource metrics
      + Create and edit alarms to be notified of problems
