

# Amazon RDS DB engine, Region, and instance class support for Database Insights
<a name="USER_DatabaseInsights.Engines"></a>

The following table provides Amazon RDS DB engines that support Database Insights.


|  Amazon RDS DB engine  | Supported engine versions and Regions | Instance class restrictions | 
| --- | --- | --- | 
| Amazon RDS for MariaDB | For more information on version and Region availability of Database Insights with RDS for MariaDB, see [Supported Regions and DB engines for Database Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.md). | Database Insights isn't supported for the following instance classes:+  db.t2.micro <br />+  db.t2.small <br />+  db.t3.micro <br />+  db.t3.small <br />+  db.t4g.micro <br />+  db.t4g.small  | 
| RDS for MySQL | For more information on version and Region availability of Database Insights with RDS for MySQL, see [Supported Regions and DB engines for Database Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.md). | Database Insights isn't supported for the following instance classes:+  db.t2.micro <br />+  db.t2.small <br />+  db.t3.micro <br />+  db.t3.small <br />+  db.t4g.micro <br />+  db.t4g.small  | 
| Amazon RDS for Microsoft SQL Server | For more information on version and Region availability of Database Insights with RDS for SQL Server, see [Supported Regions and DB engines for Database Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.md). | N/A | 
| Amazon RDS for PostgreSQL | For more information on version and Region availability of Database Insights with RDS for PostgreSQL, see [Supported Regions and DB engines for Database Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.md). | N/A | 
| Amazon RDS for Oracle | For more information on version and Region availability of Database Insights with RDS for Oracle, see [Supported Regions and DB engines for Database Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.md). | N/A | 

## Amazon RDS DB engine, Region, and instance class support for Database Insights features
<a name="database-insights-feature-support"></a>

The following table provides Amazon RDS DB engines that support Database Insights features.


| Feature | [Pricing tier](https://aws.amazon.com/rds/performance-insights/pricing/) |  [Supported regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions)  |  [ Supported DB engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html#Welcome.Concepts.DBInstance)  |  [Supported instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Types)  | 
| --- | --- | --- | --- | --- | 
| [SQL statistics for Performance Insights](sql-statistics.md) | All | All | All | All | 
| Analyzing execution plans | All | All | RDS for Oracle | All | 
| Analyzing database performance for a period of time | Paid tier only | All |  + RDS for MariaDB<br />+ RDS for MySQL<br />+ RDS for PostgreSQL  | All | 
| [Viewing Database Insights proactive recommendations](USER_PerfInsights.InsightsRecommendationViewDetails.md) | Paid tier only | + US East (Ohio)<br />+ US East (N. Virginia)<br />+ US West (N. California)<br />+ US West (Oregon)<br />+ Asia Pacific (Mumbai)<br />+ Asia Pacific (Seoul)<br />+ Asia Pacific (Singapore)<br />+ Asia Pacific (Sydney)<br />+ Asia Pacific (Tokyo)<br />+ Canada (Central)<br />+ Europe (Frankfurt)<br />+ Europe (Ireland)<br />+ Europe (London)<br />+ Europe (Paris)<br />+ Europe (Stockholm)<br />+ South America (São Paulo)  | All | All | 

## Amazon RDS Region support for Database Insights
<a name="database-insights-region-support"></a>

Amazon RDS supports Database Insights in the following AWS Regions.
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