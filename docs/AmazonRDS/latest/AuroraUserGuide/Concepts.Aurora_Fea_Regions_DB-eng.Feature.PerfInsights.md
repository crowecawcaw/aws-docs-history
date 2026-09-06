

# Supported Regions and Aurora DB engines for Database Insights
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights"></a>

Database Insights expands on existing Amazon RDS monitoring features to illustrate and help you analyze your database performance. With the Database Insights dashboard, you can visualize the database load on your Amazon RDS DB instance load and filter the load by waits, SQL statements, hosts, or users. For more information, see [Overview of Database Insights on Amazon Aurora](USER_PerfInsights.Overview.md). 

For the region, DB engine, and instance class support information for Database Insights features, see [Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.html).

**Topics**
+ [Database Insights with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy)
+ [Database Insights with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg)
+ [Database Insights with Aurora Serverless](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.serverless)

## Database Insights with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy"></a>

**Note**  
Engine version support is different for Database Insights with Aurora MySQL if you have parallel query turned on. For more information on parallel query, see [Parallel query for Amazon Aurora MySQL](aurora-mysql-parallel-query.md).

**Topics**
+ [Database Insights with Aurora MySQL and parallel query turned off](#Feature.PerfInsights.regions.amy.pq)
+ [Database Insights with Aurora MySQL and parallel query turned on](#Feature.PerfInsights.regions.amy.pqoff)

### Database Insights with Aurora MySQL and parallel query turned off
<a name="Feature.PerfInsights.regions.amy.pq"></a>

The following Regions and engine versions are available for Performance Insights with Aurora MySQL and parallel query turned off.


| Region | Aurora MySQL version 3 | Aurora MySQL version 8.4 | Aurora MySQL version 2 | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | All versions | All versions | All versions | 
| US East (Ohio) | All versions | All versions | All versions | 
| US West (N. California) | All versions | All versions | All versions | 
| US West (Oregon) | All versions | All versions | All versions | 
| Africa (Cape Town) | All versions | All versions | All versions | 
| Asia Pacific (Hong Kong) | All versions | All versions | All versions | 
| Asia Pacific (Hyderabad) | All versions | All versions | All versions | 
| Asia Pacific (Jakarta) | All versions | All versions | All versions | 
| Asia Pacific (Malaysia) | All versions | All versions | All versions | 
| Asia Pacific (Melbourne) | All versions | All versions | All versions | 
| Asia Pacific (Mumbai) | All versions | All versions | All versions | 
| Asia Pacific (New Zealand) | All versions | All versions | All versions | 
| Asia Pacific (Osaka) | All versions | All versions | All versions | 
| Asia Pacific (Seoul) | All versions | All versions | All versions | 
| Asia Pacific (Singapore) | All versions | All versions | All versions | 
| Asia Pacific (Sydney) | All versions | All versions | All versions | 
| Asia Pacific (Taipei) | All versions | All versions | All versions | 
| Asia Pacific (Thailand) | All versions | All versions | All versions | 
| Asia Pacific (Tokyo) | All versions | All versions | All versions | 
| Canada (Central) | All versions | All versions | All versions | 
| Canada West (Calgary) | All versions | All versions | All versions | 
| China (Beijing) | All versions | All versions | All versions | 
| China (Ningxia) | All versions | All versions | All versions | 
| Europe (Frankfurt) | All versions | All versions | All versions | 
| Europe (Ireland) | All versions | All versions | All versions | 
| Europe (London) | All versions | All versions | All versions | 
| Europe (Milan) | All versions | All versions | All versions | 
| Europe (Paris) | All versions | All versions | All versions | 
| Europe (Spain) | All versions | All versions | All versions | 
| Europe (Stockholm) | All versions | All versions | All versions | 
| Europe (Zurich) | All versions | All versions | All versions | 
| Israel (Tel Aviv) | All versions | All versions | All versions | 
| Mexico (Central) | All versions | All versions | All versions | 
| Middle East (Bahrain) | All versions | All versions | All versions | 
| Middle East (UAE) | All versions | All versions | All versions | 
| South America (São Paulo) | All versions | All versions | All versions | 
| AWS GovCloud (US-East) | All versions | All versions | All versions | 
| AWS GovCloud (US-West) | All versions | All versions | All versions | 

### Database Insights with Aurora MySQL and parallel query turned on
<a name="Feature.PerfInsights.regions.amy.pqoff"></a>

The following Regions and engine versions are available for Performance Insights with Aurora MySQL and parallel query turned on.


| Region | Aurora MySQL version 3 | Aurora MySQL version 8.4 | Aurora MySQL version 2 | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | Not available | Not available | Version 2.09.0 and higher | 
| US East (Ohio) | Not available | Not available | Version 2.09.0 and higher | 
| US West (N. California) | Not available | Not available | Version 2.09.0 and higher | 
| US West (Oregon) | Not available | Not available | Version 2.09.0 and higher | 
| Africa (Cape Town) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Hong Kong) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Hyderabad) | Not available | Not available | All versions | 
| Asia Pacific (Jakarta) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Malaysia) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Melbourne) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Mumbai) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (New Zealand) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Osaka) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Seoul) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Singapore) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Sydney) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Taipei) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Thailand) | Not available | Not available | Version 2.09.0 and higher | 
| Asia Pacific (Tokyo) | Not available | Not available | Version 2.09.0 and higher | 
| Canada (Central) | Not available | Not available | Version 2.09.0 and higher | 
| Canada West (Calgary) | Not available | Not available | Version 2.09.0 and higher | 
| China (Beijing) | Not available | Not available | Version 2.09.0 and higher | 
| China (Ningxia) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Frankfurt) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Ireland) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (London) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Milan) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Paris) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Spain) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Stockholm) | Not available | Not available | Version 2.09.0 and higher | 
| Europe (Zurich) | Not available | Not available | Version 2.09.0 and higher | 
| Israel (Tel Aviv) | Not available | Not available | Version 2.09.0 and higher | 
| Mexico (Central) | Not available | Not available | Version 2.09.0 and higher | 
| Middle East (Bahrain) | Not available | Not available | Version 2.09.0 and higher | 
| Middle East (UAE) | Not available | Not available | Version 2.09.0 and higher | 
| South America (São Paulo) | Not available | Not available | Version 2.09.0 and higher | 
| AWS GovCloud (US-East) | Not available | Not available | Version 2.09.0 and higher | 
| AWS GovCloud (US-West) | Not available | Not available | Version 2.09.0 and higher | 

## Database Insights with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg"></a>

The following Regions and engine versions are available for Database Insights with Aurora PostgreSQL.


| Region | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | Aurora PostgreSQL 12 | Aurora PostgreSQL 11 | Aurora PostgreSQL 10 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| US East (N. Virginia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US East (Ohio) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (N. California) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (Oregon) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Africa (Cape Town) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hong Kong) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hyderabad) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Jakarta) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Malaysia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Melbourne) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Mumbai) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (New Zealand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Osaka) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Seoul) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Singapore) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Sydney) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Taipei) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Thailand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Tokyo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada West (Calgary) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Beijing) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Ningxia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Frankfurt) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Ireland) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (London) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Milan) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Paris) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Spain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Stockholm) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Zurich) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Israel (Tel Aviv) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Mexico (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (Bahrain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (UAE) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| South America (São Paulo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-East) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-West) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 

## Database Insights with Aurora Serverless
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.serverless"></a>

Aurora serverless supports Database Insights for all MySQL-compatible and PostgreSQL-compatible versions. We recommend that you set the minimum capacity to at least 2 Aurora capacity units (ACUs).