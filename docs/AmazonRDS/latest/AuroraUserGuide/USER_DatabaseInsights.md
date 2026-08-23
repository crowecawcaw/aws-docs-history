# Monitoring Amazon Aurora databases with CloudWatch Database Insights

Monitor the database load (DB Load) for your fleet of Amazon Aurora DB instances with Database Insights. DB Load measures the level of session activity in your database. You can use Database Insights to analyze and troubleshoot the performance of your Amazon Aurora databases at scale.

With Database Insights, you can visualize the DB Load on your fleet of databases and filter the load by waits, SQL statements, hosts, or users.

By default, RDS enables the Standard mode of Database Insights for your Amazon Aurora databases. When you turn on the Advanced mode of Database Insights for a DB cluster, RDS enables Database Insights for every DB instance in the cluster.

For information about using Database Insights in the Amazon CloudWatch console, see [CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md") in the _Amazon CloudWatch User Guide_.

## Pricing

For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Amazon Aurora DB engine, Region, and instance class support for Database Insights](USER_DatabaseInsights.Engines.md "USER_DatabaseInsights.Engines.md")
- [Turning on the Advanced mode of Database Insights for Amazon Aurora](USER_DatabaseInsights.TurningOnAdvanced.md "USER_DatabaseInsights.TurningOnAdvanced.md")
- [Turning on the Standard mode of Database Insights for Amazon Aurora](USER_DatabaseInsights.TurningOnStandard.md "USER_DatabaseInsights.TurningOnStandard.md")
- [Configuring your database to monitor slow SQL queries with Database Insights for Amazon Aurora](USER_DatabaseInsights.SlowSQL.md "USER_DatabaseInsights.SlowSQL.md")
- [Considerations for Database Insights for Amazon Aurora](USER_DatabaseInsights.Considerations.md "USER_DatabaseInsights.Considerations.md")
- [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md")
