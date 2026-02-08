# Monitoring DB load with Performance Insights on Amazon RDS

###### Important

AWS has announced the end-of-life date for Performance Insights: June 30, 2026. After this date, Amazon RDS will no longer support the Performance Insights console experience,
flexible retention periods (1-24 months), and their associated pricing. The Performance Insights API will continue to exist with no pricing changes. Costs for the
Performance Insights API will appear in your AWS bill with the cost of CloudWatch Database Insights.

We recommend that you upgrade any DB instances
using the paid tier of Performance Insights to the Advanced mode of Database Insights before June 30, 2026.
For information about upgrading to the Advanced mode of Database Insights, see
[Turning on the Advanced mode of Database Insights for Amazon RDS](USER_DatabaseInsights.md "USER_DatabaseInsights.md").

If you take no action, DB instances using Performance Insights
will default to using the Standard mode of Database Insights. With Standard mode of Database Insights, you might lose access to performance data history beyond 7 days and might not be able to use execution plans
and on-demand analysis features in the Amazon RDS console. After June 30, 2026 only the Advanced mode of Database Insights will support execution plans and on-demand analysis.

With CloudWatch Database Insights, you can monitor database load for your fleet of databases and analyze and troubleshoot performance at scale.
For more information about Database Insights, see [Monitoring Amazon RDS databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").
For pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Performance Insights expands on existing Amazon RDS monitoring
features to illustrate and help you analyze your database performance. With the Performance Insights dashboard, you can visualize the database load on your Amazon RDS DB instance load and filter the load by waits, SQL statements,
hosts, or users. For information about using Performance Insights with Amazon DocumentDB, see _[Amazon DocumentDB Developer Guide](../../../documentdb/latest/developerguide/performance-insights.md "../../../documentdb/latest/developerguide/performance-insights.md")_.

###### Topics

- [Overview of Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md")
- [Turning Performance Insights on and off for Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md")
- [Overview of the Performance Schema for Performance Insights on Amazon RDS for MariaDB or MySQL](USER_PerfInsights.md "USER_PerfInsights.md")
- [Configuring access policies for Performance Insights](USER_PerfInsights.md "USER_PerfInsights.md")
- [Analyzing metrics with the Performance Insights dashboard](USER_PerfInsights.md "USER_PerfInsights.md")
- [Viewing Performance Insights proactive recommendations](USER_PerfInsights.md "USER_PerfInsights.md")
- [Retrieving metrics with the Performance Insights API for Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md")
- [Logging Performance Insights calls using AWS CloudTrail](USER_PerfInsights.md "USER_PerfInsights.md")
- [Performance Insights API and interface VPC endpoints (AWS PrivateLink)](pi-vpc-interface-endpoints.md "pi-vpc-interface-endpoints.md")
