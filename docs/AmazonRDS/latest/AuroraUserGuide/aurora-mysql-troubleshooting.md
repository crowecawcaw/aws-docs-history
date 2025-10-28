# Troubleshooting Amazon Aurora MySQL database performance

This topic focuses on some common Aurora MySQL DB performance issues, and how to troubleshoot or collect information to remediate
these issues quickly. We divide database performance into two categories:

- Server performance – The entire database server runs slower.
- Query performance – One or more queries take longer to run.

## AWS monitoring options

We recommend that you use the following AWS monitoring options to help with troubleshooting:

- Amazon CloudWatch – Amazon CloudWatch monitors your AWS resources and the applications you run on AWS in real time. You can
  use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. For more
  information, see [What is
  Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

You can view all of the system metrics and process information for your DB instances on the AWS Management Console. You can
configure your Aurora MySQL DB cluster to publish general, slow, audit, and error log data to a log group in Amazon CloudWatch Logs.
This allows you to view trends, maintain logs if a host is impacted, and create a baseline for "normal" performance to
easily identify anomalies or changes. For more information, see [Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").

- Enhanced Monitoring – To enable additional Amazon CloudWatch metrics for an Aurora MySQL database, turn on Enhanced Monitoring. When you create or
  modify an Aurora DB cluster, select **Enable Enhanced Monitoring**. This allows Aurora to publish performance metrics to
  CloudWatch. Some of the key metrics available include CPU usage, database connections, storage usage, and query latency. These
  can help identify performance bottlenecks.

The amount of information transferred for a DB instance is directly proportional to the defined granularity for Enhanced Monitoring. A
smaller monitoring interval results in more frequent reporting of OS metrics and increases your monitoring cost. To
manage costs, set different granularities for different instances in your AWS accounts. The default granularity at
creation of an instance is 60 seconds. For more information, see [Cost of Enhanced Monitoring](USER_Monitoring.md#USER_Monitoring.OS.cost "USER_Monitoring.md#USER_Monitoring.OS.cost").

- Performance Insights – You can view all of the database call metrics. This includes DB locks, waits, and the number of rows
  processed, all of which you can use for troubleshooting. When you create or modify an Aurora DB cluster, select
  **Turn on Performance Insights**. By default, Performance Insights has a 7-day data retention period, but can be customized to
  analyze longer-term performance trends. For longer than 7-day retention, you need to upgrade to the paid tier. For more
  information, see [Performance Insights pricing](https://aws.amazon.com/rds/performance-insights/pricing/ "https://aws.amazon.com/rds/performance-insights/pricing/"). You can set the
  data retention period for each Aurora DB instance separately. For more information, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

## Most common reasons for Aurora MySQL database performance issues

You can use the following steps to troubleshoot performance issues in your Aurora MySQL database. We list these steps in the
logical order of investigation, but they're not intended to be linear. One discovery could jump across steps, which allow for a
series of investigative paths.

1. [Workload](aurora-mysql-troubleshooting-workload.md "aurora-mysql-troubleshooting-workload.md") – Understand your database workload.
2. [Logging](aurora-mysql-troubleshooting-logging.md "aurora-mysql-troubleshooting-logging.md") – Review all of the database logs.
3. [Database connections](mysql-troubleshooting-dbconn.md "mysql-troubleshooting-dbconn.md") – Make sure that the connections between your
   applications and your database are reliable.
4. [Query performance](aurora-mysql-troubleshooting-query.md "aurora-mysql-troubleshooting-query.md") – Examine your query execution plans to see if they've changed.
   Code changes can cause plans to change.
