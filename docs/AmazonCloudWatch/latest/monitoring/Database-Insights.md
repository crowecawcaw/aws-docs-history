# CloudWatch Database Insights

###### Note

AWS announced that the end-of-life date for Performance Insights was July 31, 2026, and has migrated
Performance Insights users to Database Insights. Standard mode supports flexible retention of
1–24 months at the same price as Performance Insights. Advanced mode supports flexible retention
of 1–24 months, at no extra cost.

Use CloudWatch Database Insights to monitor and troubleshoot Amazon Aurora MySQL, Amazon Aurora PostgreSQL, Amazon Aurora PostgreSQL Limitless, Amazon Aurora DSQL, Amazon RDS for SQL Server, RDS for MySQL, RDS for PostgreSQL, RDS for Oracle, and RDS for MariaDB databases at scale.

With Database Insights, you can monitor your database fleet with pre-built, opinionated dashboards. To help you analyze the performance of your fleet, the Database Insights dashboards display curated metrics and visualizations, and you
can customize these dashboards.
By presenting metrics in a single dashboard for all databases in your fleet, Database Insights allows you to monitor your databases simultaneously.

For example, you can use Database Insights to find a database that is performing poorly within a fleet of hundreds of database instances. You can then choose that instance and use Database Insights to troubleshoot issues.

For information about engine, AWS Region, and instance class support, see
[Aurora DB engine, Region, and instance class support for Database Insights](../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Engines.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Engines.md")
and [Amazon RDS DB engine, Region, and instance class support for Database Insights](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Engines.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Engines.md").

For information about monitoring Amazon Aurora DSQL, see [Monitoring and logging for Aurora DSQL](../../../aurora-dsql/latest/userguide/monitoring-overview.md "../../../aurora-dsql/latest/userguide/monitoring-overview.md").

Database Insights supports monitoring workloads across multiple accounts and regions.
To learn more about the cross-account cross-region monitoring feauture of Database Insights see
[Set up cross-account cross-region monitoring for CloudWatch Database Insights](Database-Insights-Cross-Account-Cross-Region.md "Database-Insights-Cross-Account-Cross-Region.md")

To get started with Database Insights, see the following topics.

###### Topics

- [Get started with CloudWatch Database Insights](Database-Insights-Get-Started.md "Database-Insights-Get-Started.md")
- [Viewing the Fleet Health Dashboard for CloudWatch Database Insights](Database-Insights-Fleet-Health-Dashboard.md "Database-Insights-Fleet-Health-Dashboard.md")
- [Viewing the Database Instance Dashboard for CloudWatch Database Insights](Database-Insights-Database-Instance-Dashboard.md "Database-Insights-Database-Instance-Dashboard.md")
- [Troubleshooting for CloudWatch Database Insights](Database-Insights-Troubleshooting.md "Database-Insights-Troubleshooting.md")

## Modes for Database Insights

Database Insights modes apply to Amazon Relational Database Service, Amazon Aurora provisioned, Amazon Aurora Serverless, and Amazon Aurora Limitless databases.

Database Insights has an Advanced mode and a Standard mode. Standard mode is the default for Database Insights, and you can turn on the Advanced mode for your database.

The following table shows which features CloudWatch supports for the Advanced mode and Standard mode of Database Insights.

| Feature                                                                                                                                                                                                                                                                                                                                  | Standard mode                               | Advanced mode                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| Analyze the top contributors to DB Load by dimension                                                                                                                                                                                                                                                                                     | Supported                                   | Supported                                                                    |
| Retention of detailed database and per-query metrics                                                                                                                                                                                                                                                                                     | Free up to 7 days, and paid for 1–24 months | 1–24 months retention period included at no additional cost                  |
| Query, graph, and set alarms on database metrics with up to 7 days of retention                                                                                                                                                                                                                                                          | Supported                                   | Supported                                                                    |
| Define fine‐grained access control policies to restrict access to potentially sensitive dimensions such as SQL text                                                                                                                                                                                                                      | Supported                                   | Supported                                                                    |
| Analyze operating system processes happening in your databases with detailed metrics per running process<br>[Amazon RDS<br>Enhanced Monitoring](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.md") is required for this feature to work. | Not supported                               | Supported                                                                    |
| Define and save fleet‐wide monitoring views to assess database health at scale                                                                                                                                                                                                                                                           | Not supported                               | Supported                                                                    |
| Analyze SQL locks with 15 months of retention and a guided UX                                                                                                                                                                                                                                                                            | Not supported                               | Supported only for Aurora PostgreSQL and RDS for PostgreSQL                  |
| Analyze SQL execution plans with 15 months of retention and guided UX                                                                                                                                                                                                                                                                    | Not supported                               | Supported only for Aurora PostgreSQL, RDS for Oracle, and RDS for SQL Server |
| Visualize per‐query statistics                                                                                                                                                                                                                                                                                                           | Not supported                               | Supported                                                                    |
| Analyze slow SQL queriesExport of database logs to CloudWatch Logs is required for<br>this feature to work.                                                                                                                                                                                                                              | Not supported                               | Supported                                                                    |
| View calling services with CloudWatch Application Signals                                                                                                                                                                                                                                                                                | Not supported                               | Supported                                                                    |
| View a consolidated dashboard for all database telemetry, including metrics,<br>logs, events, and applicationsExport of database logs to CloudWatch Logs is required to<br>view database logs in the Database Insights console.                                                                                                          | Not supported                               | Supported                                                                    |
| Import Performance Insights counter metrics into CloudWatch automatically                                                                                                                                                                                                                                                                | Not supported                               | Supported                                                                    |
| View Amazon RDS events in CloudWatch                                                                                                                                                                                                                                                                                                     | Not supported                               | Supported                                                                    |
| Analyze database performance for a time period of your choice with on‐demand analysis                                                                                                                                                                                                                                                    | Not supported                               | Supported                                                                    |

###### Note

Database Insights feature availability differs in different AWS Regions, because not all Advanced Mode features are available in all Regions.

## Data retention

If you enable Database Insights Standard mode, Database Insights includes up to 7 days of detailed database and per-query metrics retention at no additional cost. For retention beyond 7 days, you can configure retention from 1 to 24 months. For pricing information, see [Database Insights pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Database Insights Advanced mode supports retention of detailed database and per-query metrics for 1–24 months, at no additional cost.

For information about detailed database and per-query metrics, see [Amazon CloudWatch metrics for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md").

For information about the CloudWatch metrics collected by Database Insights, see the following topics.

- [Amazon CloudWatch metrics for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.md") in the _Amazon Aurora User Guide_
- [Amazon CloudWatch metrics for Amazon Relational Database Service](../../../AmazonRDS/latest/UserGuide/rds-metrics.md "../../../AmazonRDS/latest/UserGuide/rds-metrics.md") in the _Amazon RDS User Guide_
- [Amazon CloudWatch metrics for Amazon RDS Performance Insights](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Cloudwatch.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Cloudwatch.md") in the _Amazon Aurora User Guide_
- [Amazon CloudWatch metrics for Amazon RDS Performance Insights](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.md") in the _Amazon Aurora User Guide_

## Pricing

For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
