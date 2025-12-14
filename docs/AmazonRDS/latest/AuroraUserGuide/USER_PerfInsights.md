# Overview of Performance Insights on Amazon Aurora

###### Important

AWS has announced the end-of-life date for Performance Insights: June 30, 2026. After this date, Amazon RDS will no longer support the Performance Insights console experience,
flexible retention periods (1-24 months), and their associated pricing. The Performance Insights API will continue to exist with no pricing changes. Costs for the
Performance Insights API will appear in your AWS bill with the cost of CloudWatch Database Insights.

We recommend that you upgrade any DB clusters
using the paid tier of Performance Insights to the Advanced mode of Database Insights before June 30, 2026.
For information about upgrading to the Advanced mode of Database Insights, see
[Turning on the Advanced mode of Database Insights for Amazon Aurora](USER_DatabaseInsights.md "USER_DatabaseInsights.md").

If you take no action, DB clusters using Performance Insights
will default to using the Standard mode of Database Insights. With Standard mode of Database Insights, you might lose access to performance data history beyond 7 days and might not be able to use execution plans
and on-demand analysis features in the Amazon RDS console. After June 30, 2026 only the Advanced mode of Database Insights will support execution plans and on-demand analysis.

With CloudWatch Database Insights, you can monitor database load for your fleet of databases and analyze and troubleshoot performance at scale.
For more information about Database Insights, see [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").
For pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

By default, RDS enables Performance Insights in the console create wizard for all Amazon RDS engines. If you turn on
Performance Insights at the DB cluster level, RDS enables Performance Insights for every DB instance in the cluster. If you have
more than one database on a DB instance, Performance Insights aggregates performance data.

You can find an overview of Performance Insights for Amazon Aurora
in the following video.

###### Topics

- [Database load](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md")
- [Maximum CPU](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md")
- [Amazon Aurora DB engine, Region, and instance class support
  for Performance Insights](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md")
- [Pricing and data retention for Performance Insights](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md")
