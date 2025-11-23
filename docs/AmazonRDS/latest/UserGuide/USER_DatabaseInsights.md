# Amazon RDS DB engine, Region, and instance class support

for Database Insights

The following table provides Amazon RDS DB engines that support Database Insights.

| Amazon RDS DB engine                | Supported engine versions and Regions                                                                                                                                                                                                                                               | Instance class restrictions                                                                                                                                                   |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon RDS for MariaDB              | For more information on version and Region availability of Database Insights with RDS for MariaDB, see<br>[Supported<br>Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").    | Database Insights isn't supported for the following instance classes:<br>• db.t2.micro<br>• db.t2.small<br>• db.t3.micro<br>• db.t3.small<br>• db.t4g.micro<br>• db.t4g.small |
| RDS for MySQL                       | For more information on version and Region availability of Database Insights with RDS for MySQL, see<br>[Supported<br>Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").      | Database Insights isn't supported for the following instance classes:<br>• db.t2.micro<br>• db.t2.small<br>• db.t3.micro<br>• db.t3.small<br>• db.t4g.micro<br>• db.t4g.small |
| Amazon RDS for Microsoft SQL Server | For more information on version and Region availability of Database Insights with RDS for SQL Server, see<br>[Supported<br>Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md"). | N/A                                                                                                                                                                           |
| Amazon RDS for PostgreSQL           | For more information on version and Region availability of Database Insights with RDS for PostgreSQL, see<br>[Supported<br>Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md"). | N/A                                                                                                                                                                           |
| Amazon RDS for Oracle               | For more information on version and Region availability of Database Insights with RDS for Oracle, see<br>[Supported<br>Regions and DB engines for Performance Insights in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").     | N/A                                                                                                                                                                           |

## Amazon RDS DB engine, Region, and instance class support

for Database Insights features

The following table provides Amazon RDS DB engines that support Database Insights features.

| Feature                                                                                                                                                                  | [Pricing tier](https://aws.amazon.com/rds/performance-insights/pricing/ "https://aws.amazon.com/rds/performance-insights/pricing/") | [Supported regions](Concepts.md#Concepts.RegionsAndAvailabilityZones.Regions "Concepts.md#Concepts.RegionsAndAvailabilityZones.Regions")                                                                                                                                                                                                                                                                   | [Supported DB engines](Welcome.md#Welcome.Concepts.DBInstance "Welcome.md#Welcome.Concepts.DBInstance") | [Supported instance classes](Concepts.md#Concepts.DBInstanceClass.Types "Concepts.md#Concepts.DBInstanceClass.Types") |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [SQL statistics for Performance Insights](sql-statistics.md "sql-statistics.md")                                                                                         | All                                                                                                                                 | All                                                                                                                                                                                                                                                                                                                                                                                                        | All                                                                                                     | All                                                                                                                   |
| [Analyzing Oracle execution plans using the Performance<br>Insights dashboard for Amazon RDS](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md") | All                                                                                                                                 | All                                                                                                                                                                                                                                                                                                                                                                                                        | RDS for Oracle                                                                                          | All                                                                                                                   |
| [Analyzing database performance for a period of time](USER_PerfInsights.UsingDashboard.md "USER_PerfInsights.UsingDashboard.md")                                         | Paid tier only                                                                                                                      | All                                                                                                                                                                                                                                                                                                                                                                                                        | • RDS for MariaDB<br>• RDS for MySQL<br>• RDS for PostgreSQL                                            | All                                                                                                                   |
| [Viewing Performance Insights proactive recommendations](USER_PerfInsights.md "USER_PerfInsights.md")                                                                    | Paid tier only                                                                                                                      | • US East (Ohio)<br>• US East (N. Virginia)<br>• US West (N. California)<br>• US West (Oregon)<br>• Asia Pacific (Mumbai)<br>• Asia Pacific (Seoul)<br>• Asia Pacific (Singapore)<br>• Asia Pacific (Sydney)<br>• Asia Pacific (Tokyo)<br>• Canada (Central)<br>• Europe (Frankfurt)<br>• Europe (Ireland)<br>• Europe (London)<br>• Europe (Paris)<br>• Europe (Stockholm)<br>• South America (São Paulo) | All                                                                                                     | All                                                                                                                   |

## Amazon RDS Region support

for Database Insights

Amazon RDS supports Database Insights in the following AWS Regions.

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Malaysia)
- Asia Pacific (Melbourne)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Canada West (Calgary)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Europe (Zurich)
- Israel (Tel Aviv)
- Middle East (Bahrain)
- Middle East (UAE)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
