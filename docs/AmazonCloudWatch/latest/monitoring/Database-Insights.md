# CloudWatch Database Insights

Use CloudWatch Database Insights to monitor and troubleshoot Amazon Aurora MySQL, Amazon Aurora PostgreSQL, Amazon Aurora PostgreSQL Limitless, Amazon RDS for SQL Server, RDS for MySQL, RDS for PostgreSQL, RDS for Oracle, and RDS for MariaDB databases at scale.

With Database Insights, you can monitor your database fleet with pre-built, opinionated dashboards. To help you analyze the performance of your fleet, the Database Insights dashboards display curated metrics and visualizations, and you 
 can customize these dashboards.
 By presenting metrics in a single dashboard for all databases in your fleet, Database Insights allows you to monitor your databases simultaneously.

For example, you can use Database Insights to find a database that is performing poorly within a fleet of hundreds of database instances. You can then choose that instance and use Database Insights to troubleshoot issues.

For information about engine, AWS Region, and instance class support, see 
 [Aurora DB engine, Region, and instance class support for Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Engines.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Engines.html") 
 and [Amazon RDS DB engine, Region, and instance class support for Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Engines.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Engines.html").

Database Insights supports monitoring workloads only within the same AWS account.

To get started with Database Insights, see the following topics.


###### Topics


* [Get started with CloudWatch Database Insights](Database-Insights-Get-Started.md "Database-Insights-Get-Started.md")
* [Viewing the Fleet Health Dashboard for CloudWatch Database Insights](Database-Insights-Fleet-Health-Dashboard.md "Database-Insights-Fleet-Health-Dashboard.md")
* [Viewing the Database Instance Dashboard for
 CloudWatch Database Insights](Database-Insights-Database-Instance-Dashboard.md "Database-Insights-Database-Instance-Dashboard.md")
* [Troubleshooting for CloudWatch Database Insights](Database-Insights-Troubleshooting.md "Database-Insights-Troubleshooting.md")

## Modes for Database Insights


Database Insights has an Advanced mode and a Standard mode. Standard mode is the default for Database Insights, and you can turn on the Advanced mode for your database.
 


The following table shows which features CloudWatch supports for the Advanced mode and Standard mode of Database Insights.




| Feature | Standard mode | Advanced mode |
| --- | --- | --- |
| Analyze the top contributors to DB Load by dimension | Supported | Supported |
| Query, graph, and set alarms on database metrics with up to 7 days of retention | Supported | Supported |
| Define fine‐grained access control policies to restrict access to potentially sensitive dimensions such as SQL text | Supported | Supported |
| Analyze operating system processes happening in your databases with detailed metrics per running process [Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html") is required for this feature to work. | Not supported | Supported |
| Create and save fleet‐wide monitoring views to assess health across hundreds of databases | Not supported | Supported |
| Analyze SQL locks with 15 months of retention and a guided UX | Not supported | Supported only for Aurora PostgreSQL |
| Analyze SQL execution plans with 15 months of retention and guided UX | Not supported | Supported only for Aurora PostgreSQL, RDS for Oracle, and RDS for SQL Server |
| Visualize per‐query statistics | Not supported | Supported |
| Analyze slow SQL queriesExport of database logs to CloudWatch Logs is required for this feature to work. | Not supported | Supported |
| View calling services with CloudWatch Application Signals | Not supported | Supported |
| View a consolidated dashboard for all database telemetry, including metrics, logs, events, and applicationsExport of database logs to CloudWatch Logs is required to view database logs in the Database Insights console. | Not supported | Supported |
| Import Performance Insights counter metrics into CloudWatch automatically | Not supported | Supported |
| View Amazon RDS events in CloudWatch | Not supported | Supported |
| Analyze database performance for a time period of your choice with on‐demand analysis | Not supported | Supported only for Aurora PostgreSQL, Aurora MySQL, RDS for PostgreSQL, RDS for MySQL, RDS for MariaDB, and RDS for Oracle | ###### Note Database Insights feature availability differs in different AWS Regions, because not all Advanced Mode features are available in all Regions. ## Data retention The Advanced mode of Database Insights retains 15 months of metrics collected by Performance Insights. If Performance Insights is enabled for the Standard mode, Amazon RDS retains 7 days of Performance Insights counter metrics. For information about counter metrics for Performance Insights, see [Performance Insights counter metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html"). For information about the retention period for CloudWatch metrics collected by Database Insights, see the following topics. <br>• [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html") in the *Amazon Aurora User Guide* <br>• [Amazon CloudWatch metrics for Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html") in the *Amazon RDS User Guide* <br>• [Amazon CloudWatch metrics for Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Cloudwatch.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Cloudwatch.html") in the *Amazon Aurora User Guide* <br>• [Amazon CloudWatch metrics for Amazon RDS Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.html") in the *Amazon Aurora User Guide* ## How Database Insights integrates with Performance Insights Performance Insights is a database performance monitoring service. Database Insights builds upon and extends the capabilities of Performance Insights. Database Insights adds monitoring, analysis, and optimization features. To enable the Advanced mode of Database Insights, you must enable Performance Insights. Database Insights imports Performance Insights counter metrics into CloudWatch automatically. The Advanced mode of Database Insights automatically retains 15 months of all metrics collected by Database Insights, including Performance Insights metrics and CloudWatch metrics. This automatically happens for you when you enable Advanced mode in an instance, with no further configuration needed. For information about Performance Insights counter metrics, see [Performance Insights counter metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html") in the *Amazon Aurora User Guide*. ## Pricing For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
