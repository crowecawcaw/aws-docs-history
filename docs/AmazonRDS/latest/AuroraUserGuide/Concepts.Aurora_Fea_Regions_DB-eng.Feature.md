# Supported Regions and Aurora DB engines for Performance Insights

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

Performance Insights expands on existing Amazon RDS monitoring features to illustrate
and help you analyze your database performance. With the Performance Insights dashboard,
you can visualize the database load on your Amazon RDS DB instance load and filter the
load by waits, SQL statements, hosts, or users. For more information, see [Overview of Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

For the region, DB engine, and instance class support information for Performance Insights features,
see [Amazon Aurora DB engine, Region, and instance class support for Performance Insights features](USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport "USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport").

###### Topics

- [Performance Insights with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy")
- [Performance Insights with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg")
- [Performance Insights with Aurora Serverless](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.serverless "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.serverless")

## Performance Insights with Aurora MySQL

###### Note

Engine version support is different for Performance Insights with Aurora MySQL
if you have parallel query turned on. For more information on parallel query,
see [Parallel query for Amazon Aurora MySQL](aurora-mysql-parallel-query.md "aurora-mysql-parallel-query.md").

###### Topics

- [Performance Insights with Aurora MySQL and parallel query turned off](#Feature.PerfInsights.regions.amy.pq "#Feature.PerfInsights.regions.amy.pq")
- [Performance Insights with Aurora MySQL and parallel query turned on](#Feature.PerfInsights.regions.amy.pqoff "#Feature.PerfInsights.regions.amy.pqoff")

### Performance Insights with Aurora MySQL and parallel query turned off

The following Regions and engine versions are available for Performance
Insights with Aurora MySQL and parallel query turned off.

| Region                     | Aurora MySQL version 3 | Aurora MySQL version 2 |
| -------------------------- | ---------------------- | ---------------------- |
| US East (N. Virginia)      | All versions           | All versions           |
| US East (Ohio)             | All versions           | All versions           |
| US West (N. California)    | All versions           | All versions           |
| US West (Oregon)           | All versions           | All versions           |
| Africa (Cape Town)         | All versions           | All versions           |
| Asia Pacific (Hong Kong)   | All versions           | All versions           |
| Asia Pacific (Hyderabad)   | All versions           | All versions           |
| Asia Pacific (Jakarta)     | All versions           | All versions           |
| Asia Pacific (Malaysia)    | All versions           | All versions           |
| Asia Pacific (Melbourne)   | All versions           | All versions           |
| Asia Pacific (Mumbai)      | All versions           | All versions           |
| Asia Pacific (New Zealand) | All versions           | All versions           |
| Asia Pacific (Osaka)       | All versions           | All versions           |
| Asia Pacific (Seoul)       | All versions           | All versions           |
| Asia Pacific (Singapore)   | All versions           | All versions           |
| Asia Pacific (Sydney)      | All versions           | All versions           |
| Asia Pacific (Taipei)      | All versions           | All versions           |
| Asia Pacific (Thailand)    | All versions           | All versions           |
| Asia Pacific (Tokyo)       | All versions           | All versions           |
| Canada (Central)           | All versions           | All versions           |
| Canada West (Calgary)      | All versions           | All versions           |
| China (Beijing)            | All versions           | All versions           |
| China (Ningxia)            | All versions           | All versions           |
| Europe (Frankfurt)         | All versions           | All versions           |
| Europe (Ireland)           | All versions           | All versions           |
| Europe (London)            | All versions           | All versions           |
| Europe (Milan)             | All versions           | All versions           |
| Europe (Paris)             | All versions           | All versions           |
| Europe (Spain)             | All versions           | All versions           |
| Europe (Stockholm)         | All versions           | All versions           |
| Europe (Zurich)            | All versions           | All versions           |
| Israel (Tel Aviv)          | All versions           | All versions           |
| Mexico (Central)           | All versions           | All versions           |
| Middle East (Bahrain)      | All versions           | All versions           |
| Middle East (UAE)          | All versions           | All versions           |
| South America (São Paulo)  | All versions           | All versions           |
| AWS GovCloud (US-East)     | All versions           | All versions           |
| AWS GovCloud (US-West)     | All versions           | All versions           |

### Performance Insights with Aurora MySQL and parallel query turned on

The following Regions and engine versions are available for Performance
Insights with Aurora MySQL and parallel query turned on.

| Region                     | Aurora MySQL version 3 | Aurora MySQL version 2    |
| -------------------------- | ---------------------- | ------------------------- |
| US East (N. Virginia)      | Not available          | Version 2.09.0 and higher |
| US East (Ohio)             | Not available          | Version 2.09.0 and higher |
| US West (N. California)    | Not available          | Version 2.09.0 and higher |
| US West (Oregon)           | Not available          | Version 2.09.0 and higher |
| Africa (Cape Town)         | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Hong Kong)   | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Hyderabad)   | Not available          | All versions              |
| Asia Pacific (Jakarta)     | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Malaysia)    | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Melbourne)   | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Mumbai)      | Not available          | Version 2.09.0 and higher |
| Asia Pacific (New Zealand) | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Osaka)       | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Seoul)       | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Singapore)   | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Sydney)      | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Taipei)      | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Thailand)    | Not available          | Version 2.09.0 and higher |
| Asia Pacific (Tokyo)       | Not available          | Version 2.09.0 and higher |
| Canada (Central)           | Not available          | Version 2.09.0 and higher |
| Canada West (Calgary)      | Not available          | Version 2.09.0 and higher |
| China (Beijing)            | Not available          | Version 2.09.0 and higher |
| China (Ningxia)            | Not available          | Version 2.09.0 and higher |
| Europe (Frankfurt)         | Not available          | Version 2.09.0 and higher |
| Europe (Ireland)           | Not available          | Version 2.09.0 and higher |
| Europe (London)            | Not available          | Version 2.09.0 and higher |
| Europe (Milan)             | Not available          | Version 2.09.0 and higher |
| Europe (Paris)             | Not available          | Version 2.09.0 and higher |
| Europe (Spain)             | Not available          | Version 2.09.0 and higher |
| Europe (Stockholm)         | Not available          | Version 2.09.0 and higher |
| Europe (Zurich)            | Not available          | Version 2.09.0 and higher |
| Israel (Tel Aviv)          | Not available          | Version 2.09.0 and higher |
| Mexico (Central)           | Not available          | Version 2.09.0 and higher |
| Middle East (Bahrain)      | Not available          | Version 2.09.0 and higher |
| Middle East (UAE)          | Not available          | Version 2.09.0 and higher |
| South America (São Paulo)  | Not available          | Version 2.09.0 and higher |
| AWS GovCloud (US-East)     | Not available          | Version 2.09.0 and higher |
| AWS GovCloud (US-West)     | Not available          | Version 2.09.0 and higher |

## Performance Insights with Aurora PostgreSQL

The following Regions and engine versions are available for Performance Insights
with Aurora PostgreSQL.

| Region                     | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | Aurora PostgreSQL 12 | Aurora PostgreSQL 11 | Aurora PostgreSQL 10 |
| -------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| US East (N. Virginia)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| US East (Ohio)             | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| US West (N. California)    | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| US West (Oregon)           | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Africa (Cape Town)         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Hong Kong)   | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Hyderabad)   | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Jakarta)     | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Malaysia)    | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Melbourne)   | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Mumbai)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (New Zealand) | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Osaka)       | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Seoul)       | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Singapore)   | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Sydney)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Taipei)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Thailand)    | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Asia Pacific (Tokyo)       | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Canada (Central)           | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Canada West (Calgary)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| China (Beijing)            | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| China (Ningxia)            | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Frankfurt)         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Ireland)           | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (London)            | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Milan)             | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Paris)             | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Spain)             | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Stockholm)         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Europe (Zurich)            | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Israel (Tel Aviv)          | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Mexico (Central)           | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Middle East (Bahrain)      | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| Middle East (UAE)          | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| South America (São Paulo)  | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| AWS GovCloud (US-East)     | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |
| AWS GovCloud (US-West)     | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         | All versions         |

## Performance Insights with Aurora Serverless

Aurora Serverless v2 supports Performance Insights for all MySQL-compatible and
PostgreSQL-compatible versions. We recommend that you set the minimum capacity to at
least 2 Aurora capacity units (ACUs).

Aurora Serverless v1 doesn't support Performance Insights.
