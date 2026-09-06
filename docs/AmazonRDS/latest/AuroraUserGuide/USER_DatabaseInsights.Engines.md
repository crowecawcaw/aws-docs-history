

# Amazon Aurora DB engine, Region, and instance class support for Database Insights
<a name="USER_DatabaseInsights.Engines"></a>

The following table provides Amazon Aurora DB engines that support Database Insights.


| Amazon Aurora DB engine | Supported engine versions and Regions | Instance class restrictions | 
| --- | --- | --- | 
| Amazon Aurora MySQL-Compatible Edition | For more information on version and Region availability of Database Insights with Aurora MySQL, see [Database Insights with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy). | Database Insights has the following engine class restrictions:+  db.t2 – Not supported <br />+  db.t3 – Not supported <br />+  db.t4g.micro and db.t4g.small – Not supported  | 
| Amazon Aurora PostgreSQL-Compatible Edition | For more information on version and Region availability of Database Insights with Aurora PostgreSQL, see [Database Insights with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg). | Not applicable | 
| Aurora PostgreSQL Limitless Database | For more information about using Database Insights with Aurora PostgreSQL Limitless Database, see [Monitoring Aurora PostgreSQL Limitless Database with CloudWatch Database Insights](limitless-monitoring.cwdbi.md). | Not applicable | 

Database Insights supports Amazon Aurora serverless.

## Amazon Aurora DB engine, Region, and instance class support for Database Insights features
<a name="database-insights-feature-support"></a>

The following table provides Amazon Aurora DB engines that support Database Insights features.


| Feature | [Pricing tier](https://aws.amazon.com/rds/performance-insights/pricing/) |  [Supported regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions)  |  Supported DB engines  |  [Supported instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Types)  | 
| --- | --- | --- | --- | --- | 
| [SQL statistics for Performance Insights](sql-statistics.md) | All | All | All | All | 
| Analyzing database performance for a period of time | Paid tier only | All | All | All except db.serverless (Aurora serverless) | 
| [Viewing Database Insights proactive recommendations](USER_PerfInsights.InsightsRecommendationViewDetails.md) | Paid tier only | + US East (Ohio)<br />+ US East (N. Virginia)<br />+ US West (N. California)<br />+ US West (Oregon)<br />+ Asia Pacific (Mumbai)<br />+ Asia Pacific (Seoul)<br />+ Asia Pacific (Singapore)<br />+ Asia Pacific (Sydney)<br />+ Asia Pacific (Tokyo)<br />+ Canada (Central)<br />+ Europe (Frankfurt)<br />+ Europe (Ireland)<br />+ Europe (London)<br />+ Europe (Paris)<br />+ Europe (Stockholm)<br />+ South America (São Paulo)  | All | All except db.serverless (Aurora serverless) | 

## Amazon Aurora Region support for Database Insights
<a name="database-insights-region-support"></a>

Aurora supports Database Insights in the following AWS Regions.
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Canada West (Calgary)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Milan)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Stockholm)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Middle East (Bahrain)
+ Middle East (UAE)
+ South America (São Paulo)
+ AWS GovCloud (US-East)
+ AWS GovCloud (US-West)