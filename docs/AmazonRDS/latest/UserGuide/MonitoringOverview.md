# Monitoring tools for Amazon RDS

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon RDS and your other AWS solutions.
AWS provides various monitoring tools to watch Amazon RDS, report when something is wrong, and take automatic actions when
appropriate.

###### Topics

- [Automated monitoring tools](#MonitoringOverview.tools.automated "#MonitoringOverview.tools.automated")
- [Manual monitoring tools](#monitoring_manual_tools "#monitoring_manual_tools")

## Automated monitoring tools

We recommend that you automate monitoring tasks as much as possible.

###### Topics

- [Amazon RDS instance status and recommendations](#MonitoringOverview.tools.automated.rds "#MonitoringOverview.tools.automated.rds")
- [Amazon CloudWatch metrics for Amazon RDS](#MonitoringOverview.tools.automated.integrated "#MonitoringOverview.tools.automated.integrated")
- [Amazon RDS Performance Insights and operating-system monitoring](#MonitoringOverview.tools.automated.metrics.rds "#MonitoringOverview.tools.automated.metrics.rds")
- [Integrated services](#MonitoringOverview.tools.automated.integrated.events-logs-streams "#MonitoringOverview.tools.automated.integrated.events-logs-streams")

### Amazon RDS instance status and recommendations

You can use the following automated tools to watch
Amazon RDS and report when something is wrong:

- **Amazon RDS
  instance
  status** — View details about the current status of your instance by using
  the Amazon RDS console, the AWS CLI, or the RDS API.
- **Amazon RDS recommendations** — Respond to automated
  recommendations for database resources, such as DB instances, read replicas, and DB parameter groups. For more information, see [Recommendations from Amazon RDS](monitoring-recommendations.md "monitoring-recommendations.md").

### Amazon CloudWatch metrics for Amazon RDS

Amazon RDS integrates with
Amazon CloudWatch for additional monitoring capabilities.

- **Amazon CloudWatch** – This service monitors your AWS resources
  and the applications you run on AWS in real time. You can use the following Amazon CloudWatch features
  with Amazon RDS:
  - **Amazon CloudWatch metrics** – Amazon RDS
    automatically sends metrics to CloudWatch every minute for each active database. You don't get
    additional charges for Amazon RDS metrics in CloudWatch.

  For more
  information, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
  - **Amazon CloudWatch alarms** – You can watch a single
    Amazon RDS metric over a specific time period. You can then perform one or
    more actions based on the value of the metric relative to a threshold that you set.
    For more information, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

### Amazon RDS Performance Insights and operating-system monitoring

You can use the following automated tools to monitor Amazon RDS performance:

- **Amazon RDS Performance Insights** – Assess the load on your
  database, and determine when and where to take action. For more information, see [Monitoring DB load with Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md").
- **Amazon RDS Enhanced Monitoring** – Look at metrics in real time
  for the operating system. For more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").

### Integrated services

The following AWS services are integrated with Amazon RDS:

- _Amazon EventBridge_ is a serverless event bus service that makes it easy to connect your
  applications with data from a variety of sources. For more information, see [Monitoring Amazon RDS events](working-with-events.md "working-with-events.md").
- _Amazon CloudWatch Logs_ lets you monitor, store, and access your log files from Amazon RDS instances,
  CloudTrail, and other sources. For more information, see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf of your
  AWS account and delivers the log files to an Amazon S3 bucket that you specify. For more information,
  see [Monitoring Amazon RDS API calls in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- _Database Activity Streams_ is an Amazon RDS
  feature that provides a near-real-time
  stream of the activity in your Oracle DB instance. For more
  information, see [Monitoring Amazon RDS with Database Activity Streams](DBActivityStreams.md "DBActivityStreams.md").

## Manual monitoring tools

You need to manually monitor those items that the CloudWatch alarms don't cover. The Amazon RDS, CloudWatch, AWS Trusted Advisor
and other AWS console dashboards provide an at-a-glance view of the state of your AWS environment. We
recommend that you also check the log files on your DB instance.

- From the Amazon RDS console, you can monitor the following items for your resources:
  - The number of connections to a DB instance
  - The amount of read and write operations to a DB instance
  - The amount of storage that a DB instance is currently using
  - The amount of memory and CPU being used for a DB instance
  - The amount of network traffic to and from a DB instance

- From the Trusted Advisor dashboard, you can review the following cost optimization, security, fault
  tolerance, and performance improvement checks:

      + Amazon RDS Idle DB Instances
      + Amazon RDS Security Group Access Risk
      + Amazon RDS Backups
      + Amazon RDS Multi-AZ

  For more information on these checks, see [Trusted Advisor best practices (checks)](https://aws.amazon.com/premiumsupport/trustedadvisor/best-practices/ "https://aws.amazon.com/premiumsupport/trustedadvisor/best-practices/").

- CloudWatch home page shows:

      + Current alarms and status
      + Graphs of alarms and resources
      + Service health status

  In addition, you can use CloudWatch to do the following:

      + Create [customized dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to
       monitor the services that you care about.
      + Graph metric data to troubleshoot issues and discover trends.
      + Search and browse all your AWS resource metrics.
      + Create and edit alarms to be notified of problems.
