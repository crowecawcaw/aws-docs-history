# Analyzing metrics with the Performance Insights dashboard

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

The Performance Insights dashboard contains database performance information to help you analyze and troubleshoot
performance issues. On the main dashboard page, you can view information about the database load. You can "slice" DB
load by dimensions such as wait events or SQL.

###### Performance Insights dashboard

- [Overview of the Performance Insights dashboard](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Accessing the Performance Insights dashboard](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Analyzing DB load by wait events](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Analyzing database performance for a period of time](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Analyzing queries with the Top SQL tab in Performance Insights](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md")
- [Analyzing top Oracle PDB load](USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md "USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.md")
- [Analyzing execution plans using the Performance Insights dashboard for Amazon RDS](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
