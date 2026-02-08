# Supported

Regions and DB engines for Multi-AZ DB clusters in Amazon RDS

A Multi-AZ DB cluster deployment in Amazon RDS provides a high availability deployment mode of Amazon RDS with two
readable standby DB instances. A Multi-AZ DB cluster has a writer DB instance and two reader DB instances in three separate
Availability Zones in the same Region. Multi-AZ DB clusters provide high availability,
increased capacity for read workloads, and lower write latency when compared to Multi-AZ DB instance
deployments. For more information, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md").

Multi-AZ DB clusters aren't available with the following engines:

- RDS for Db2
- RDS for MariaDB
- RDS for Oracle
- RDS for SQL Server

###### Topics

- [Multi-AZ DB clusters with
  RDS for MySQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.MultiAZDBClusters.my "#Concepts.RDS_Fea_Regions_DB-eng.Feature.MultiAZDBClusters.my")
- [Multi-AZ DB clusters with
  RDS for PostgreSQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.MultiAZDBClusters.pg "#Concepts.RDS_Fea_Regions_DB-eng.Feature.MultiAZDBClusters.pg")

## Multi-AZ DB clusters with

RDS for MySQL

The following Regions and engine versions are available for Multi-AZ DB clusters with
RDS for MySQL.

| Region                     | RDS for MySQL 8.4      | RDS for MySQL 8.0      |
| -------------------------- | ---------------------- | ---------------------- |
| US East (N. Virginia)      | All available versions | All available versions |
| US East (Ohio)             | All available versions | All available versions |
| US West (N. California)    | Not available          | Not available          |
| US West (Oregon)           | All available versions | All available versions |
| Africa (Cape Town)         | All available versions | All available versions |
| Asia Pacific (Hong Kong)   | All available versions | All available versions |
| Asia Pacific (Hyderabad)   | All available versions | All available versions |
| Asia Pacific (Jakarta)     | All available versions | All available versions |
| Asia Pacific (Malaysia)    | All available versions | All available versions |
| Asia Pacific (Melbourne)   | All available versions | All available versions |
| Asia Pacific (Mumbai)      | All available versions | All available versions |
| Asia Pacific (New Zealand) | Not available          | Not available          |
| Asia Pacific (Osaka)       | All available versions | All available versions |
| Asia Pacific (Seoul)       | All available versions | All available versions |
| Asia Pacific (Singapore)   | All available versions | All available versions |
| Asia Pacific (Sydney)      | All available versions | All available versions |
| Asia Pacific (Taipei)      | Not available          | Not available          |
| Asia Pacific (Thailand)    | Not available          | Not available          |
| Asia Pacific (Tokyo)       | All available versions | All available versions |
| Canada (Central)           | All available versions | All available versions |
| Canada (Central)           | All available versions | All available versions |
| Canada West (Calgary)      | All available versions | All available versions |
| China (Beijing)            | All available versions | All available versions |
| China (Ningxia)            | All available versions | All available versions |
| Europe (Frankfurt)         | All available versions | All available versions |
| Europe (Ireland)           | All available versions | All available versions |
| Europe (London)            | All available versions | All available versions |
| Europe (Milan)             | All available versions | All available versions |
| Europe (Paris)             | All available versions | All available versions |
| Europe (Spain)             | All available versions | All available versions |
| Europe (Stockholm)         | All available versions | All available versions |
| Europe (Zurich)            | All available versions | All available versions |
| Israel (Tel Aviv)          | All available versions | All available versions |
| Mexico (Central)           | All available versions | All available versions |
| Middle East (Bahrain)      | All available versions | All available versions |
| Middle East (UAE)          | All available versions | All available versions |
| South America (São Paulo)  | All available versions | All available versions |
| AWS GovCloud (US-East)     | Not available          | Not available          |
| AWS GovCloud (US-West)     | Not available          | Not available          |

You can list the available versions in a Region for a given DB instance class
using the AWS CLI. Change the DB instance class to show the available engine versions for it.

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options \
--engine mysql \
--db-instance-class `db.r5d.large` \
--query '*[]|[?SupportsClusters == `true`].[EngineVersion]'  \
--output text
```

For Windows:

```
aws rds describe-orderable-db-instance-options ^
--engine mysql ^
--db-instance-class `db.r5d.large` ^
--query "*[]|[?SupportsClusters == `true`].[EngineVersion]"  ^
--output text
```

## Multi-AZ DB clusters with

RDS for PostgreSQL

The following Regions and engine versions are available for Multi-AZ DB clusters with
RDS for PostgreSQL.

| Region                     | RDS for PostgreSQL 17      | RDS for PostgreSQL 16      | RDS for PostgreSQL 15      | RDS for PostgreSQL 14   | RDS for PostgreSQL 13                    |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- | ----------------------- | ---------------------------------------- |
| US East (N. Virginia)      | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| US East (Ohio)             | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| US West (N. California)    | Not available              | Not available              | Not available              | Not available           | Not available                            |
| US West (Oregon)           | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Africa (Cape Town)         | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Hong Kong)   | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Hyderabad)   | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Jakarta)     | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Malaysia)    | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Melbourne)   | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Mumbai)      | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (New Zealand) | Not available              | Not available              | Not available              | Not available           | Not available                            |
| Asia Pacific (Osaka)       | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Seoul)       | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Singapore)   | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Sydney)      | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Asia Pacific (Taipei)      | Not available              | Not available              | Not available              | Not available           | Not available                            |
| Asia Pacific (Thailand)    | Not available              | Not available              | Not available              | Not available           | Not available                            |
| Asia Pacific (Tokyo)       | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Canada (Central)           | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Canada West (Calgary)      | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| China (Beijing)            | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| China (Ningxia)            | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Frankfurt)         | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Ireland)           | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (London)            | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Milan)             | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Paris)             | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Spain)             | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Stockholm)         | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Europe (Zurich)            | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Israel (Tel Aviv)          | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Mexico (Central)           | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Middle East (Bahrain)      | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| Middle East (UAE)          | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| South America (São Paulo)  | All PostgreSQL 17 versions | All PostgreSQL 16 versions | All PostgreSQL 15 versions | Version 14.5 and higher | Version 13.4 and version 13.7 and higher |
| AWS GovCloud (US-East)     | Not available              | Not available              | Not available              | Not available           | Not available                            |
| AWS GovCloud (US-West)     | Not available              | Not available              | Not available              | Not available           | Not available                            |

You can list the available versions in a Region for a given DB instance class
using the AWS CLI. Change the DB instance class to show the available engine versions for it.

For Linux, macOS, or Unix:

```
aws rds describe-orderable-db-instance-options \
--engine postgres \
--db-instance-class `db.r5d.large` \
--query '*[]|[?SupportsClusters == `true`].[EngineVersion]'  \
--output text
```

For Windows:

```
aws rds describe-orderable-db-instance-options ^
--engine postgres ^
--db-instance-class `db.r5d.large` ^
--query "*[]|[?SupportsClusters == `true`].[EngineVersion]"  ^
--output text
```
