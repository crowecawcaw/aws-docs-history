# Monitoring DB load with Performance Insights on Amazon Aurora

###### Important

AWS has announced the end-of-life date for Performance Insights: July 31, 2026. After this date, Amazon RDS will no longer support the Performance Insights console experience.
The Performance Insights console will redirect to CloudWatch Database Insights. Flexible retention periods (1–24 months) and their associated pricing are preserved
in Standard mode of Database Insights at the same cost as Performance Insights today. The Performance Insights API will continue to exist with no changes. Costs for the
Performance Insights API will appear in your AWS bill with the cost of CloudWatch Database Insights.

We recommend that you review your DB clusters
using Performance Insights and choose the Database Insights mode that best fits your needs before July 31, 2026.
For core monitoring with flexible retention, Standard mode of Database Insights preserves your existing experience and pricing.
For advanced capabilities including fleet-level monitoring, lock diagnostics, and execution plan capture, see
[Turning on the Advanced mode of Database Insights for Amazon Aurora](USER_DatabaseInsights.TurningOnAdvanced.md "USER_DatabaseInsights.TurningOnAdvanced.md").

If you take no action, DB clusters using Performance Insights
will default to using the Standard mode of Database Insights with your existing retention period configured.
Your CloudFormation templates, Terraform configurations, and deployment scripts will continue to work exactly as they do today – all
Performance Insights API parameters, including retention period settings, are fully preserved.
After July 31, 2026, only the Advanced mode of Database Insights will support execution plans and on-demand analysis.

With CloudWatch Database Insights, you can monitor database load for your fleet of databases and analyze and troubleshoot performance at scale.
For more information about Database Insights, see [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md") or
[Register for upcoming workshops](https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement "https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement") to learn more.
For current pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Performance Insights expands on existing Amazon Aurora monitoring
features to illustrate and help you analyze your cluster
performance. With the Performance Insights dashboard, you can visualize the database load on your Amazon Aurora cluster load and filter the load by waits, SQL statements,
hosts, or users. For information about using Performance Insights with Amazon DocumentDB, see _[Amazon DocumentDB Developer Guide](../../../documentdb/latest/developerguide/performance-insights.md "../../../documentdb/latest/developerguide/performance-insights.md")_.

###### Topics

- [Overview of Performance Insights on Amazon Aurora](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md")
- [Turning Performance Insights on and off for Aurora](USER_PerfInsights.Enabling.md "USER_PerfInsights.Enabling.md")
- [Overview of the Performance Schema for Performance Insights on Aurora MySQL](USER_PerfInsights.EnableMySQL.md "USER_PerfInsights.EnableMySQL.md")
- [Configuring access policies for Performance Insights](USER_PerfInsights.access-control.md "USER_PerfInsights.access-control.md")
- [Analyzing metrics with the Performance Insights dashboard](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")
- [Viewing Performance Insights proactive recommendations](USER_PerfInsights.InsightsRecommendationViewDetails.md "USER_PerfInsights.InsightsRecommendationViewDetails.md")
- [Retrieving metrics with the Performance Insights API for Aurora](USER_PerfInsights.API.md "USER_PerfInsights.API.md")
- [Logging Performance Insights calls using AWS CloudTrail](USER_PerfInsights.CloudTrail.md "USER_PerfInsights.CloudTrail.md")
- [Performance Insights API and interface VPC endpoints (AWS PrivateLink)](pi-vpc-interface-endpoints.md "pi-vpc-interface-endpoints.md")
