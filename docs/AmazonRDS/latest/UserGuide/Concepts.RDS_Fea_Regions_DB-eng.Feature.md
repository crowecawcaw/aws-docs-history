# Supported

Regions and DB engines for exporting snapshots to S3 in Amazon RDS

You can export RDS DB snapshot data to an Amazon S3 bucket. You can export all types of DB
snapshots—including manual snapshots, automated system snapshots, and snapshots created by
AWS Backup. After the data is exported, you can analyze the exported data directly through tools
like Amazon Athena or Amazon Redshift Spectrum. For more information, see [Exporting DB snapshot data to Amazon S3 for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md").

Exporting snapshots to S3 is not available for the following engines:

- RDS for Db2
- RDS for Oracle
- RDS for SQL Server

###### Topics

- [Export
  snapshots to S3 with RDS for MariaDB](#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.mdb "#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.mdb")
- [Export
  snapshots to S3 with RDS for MySQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.my "#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.my")
- [Export
  snapshots to S3 with RDS for PostgreSQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.pg "#Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.pg")

## Export

snapshots to S3 with RDS for MariaDB

The following Regions and engine versions are available for exporting snapshots to S3 with
RDS for MariaDB.

| Region                     | RDS for MariaDB 11.8   | RDS for MariaDB 11.4   | RDS for MariaDB 10.11  | RDS for MariaDB 10.6   | RDS for MariaDB 10.5   | RDS for MariaDB 10.4   |
| -------------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| US East (N. Virginia)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US East (Ohio)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US West (N. California)    | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US West (Oregon)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Africa (Cape Town)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Hong Kong)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Hyderabad)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Jakarta)     | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Malaysia)    | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Melbourne)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Mumbai)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (New Zealand) | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Osaka)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Seoul)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Singapore)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Sydney)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Taipei)      | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Thailand)    | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Tokyo)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Canada (Central)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Canada West (Calgary)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| China (Beijing)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| China (Ningxia)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Frankfurt)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Ireland)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (London)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Milan)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Paris)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Spain)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Stockholm)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Zurich)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Israel (Tel Aviv)          | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Mexico (Central)           | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Middle East (Bahrain)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Middle East (UAE)          | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| South America (São Paulo)  | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| AWS GovCloud (US-East)     | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| AWS GovCloud (US-West)     | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |

## Export

snapshots to S3 with RDS for MySQL

The following Regions and engine versions are available for exporting snapshots to S3 with
RDS for MySQL.

| Region                     | RDS for MySQL 8.4      | RDS for MySQL 8.0      | RDS for MySQL 5.7 (under RDS Extended Support) |
| -------------------------- | ---------------------- | ---------------------- | ---------------------------------------------- |
| US East (Ohio)             | All available versions | All available versions | All available versions                         |
| US East (N. Virginia)      | All available versions | All available versions | All available versions                         |
| US West (N. California)    | All available versions | All available versions | All available versions                         |
| US West (Oregon)           | All available versions | All available versions | All available versions                         |
| Africa (Cape Town)         | All available versions | All available versions | All available versions                         |
| Asia Pacific (Hong Kong)   | All available versions | All available versions | All available versions                         |
| Asia Pacific (Hyderabad)   | All available versions | All available versions | All available versions                         |
| Asia Pacific (Jakarta)     | All available versions | All available versions | All available versions                         |
| Asia Pacific (Malaysia)    | Not available          | Not available          | Not available                                  |
| Asia Pacific (Melbourne)   | All available versions | All available versions | All available versions                         |
| Asia Pacific (Mumbai)      | All available versions | All available versions | All available versions                         |
| Asia Pacific (New Zealand) | Not available          | Not available          | Not available                                  |
| Asia Pacific (Osaka)       | All available versions | All available versions | All available versions                         |
| Asia Pacific (Seoul)       | All available versions | All available versions | All available versions                         |
| Asia Pacific (Singapore)   | All available versions | All available versions | All available versions                         |
| Asia Pacific (Sydney)      | All available versions | All available versions | All available versions                         |
| Asia Pacific (Taipei)      | Not available          | Not available          | Not available                                  |
| Asia Pacific (Thailand)    | Not available          | Not available          | Not available                                  |
| Asia Pacific (Tokyo)       | All available versions | All available versions | All available versions                         |
| Canada (Central)           | All available versions | All available versions | All available versions                         |
| Canada West (Calgary)      | All available versions | All available versions | All available versions                         |
| China (Beijing)            | All available versions | All available versions | All available versions                         |
| China (Ningxia)            | All available versions | All available versions | All available versions                         |
| Europe (Frankfurt)         | All available versions | All available versions | All available versions                         |
| Europe (Ireland)           | All available versions | All available versions | All available versions                         |
| Europe (London)            | All available versions | All available versions | All available versions                         |
| Europe (Milan)             | All available versions | All available versions | All available versions                         |
| Europe (Paris)             | All available versions | All available versions | All available versions                         |
| Europe (Spain)             | All available versions | All available versions | All available versions                         |
| Europe (Stockholm)         | All available versions | All available versions | All available versions                         |
| Europe (Zurich)            | All available versions | All available versions | All available versions                         |
| Israel (Tel Aviv)          | All available versions | All available versions | All available versions                         |
| Mexico (Central)           | Not available          | Not available          | Not available                                  |
| Middle East (Bahrain)      | All available versions | All available versions | All available versions                         |
| Middle East (UAE)          | All available versions | All available versions | All available versions                         |
| South America (São Paulo)  | All available versions | All available versions | All available versions                         |
| AWS GovCloud (US-East)     | Not available          | Not available          | Not available                                  |
| AWS GovCloud (US-West)     | Not available          | Not available          | Not available                                  |

## Export

snapshots to S3 with RDS for PostgreSQL

The following Regions and engine versions are available for exporting snapshots to S3 with
RDS for PostgreSQL.

| Region                     | RDS for PostgreSQL 17  | RDS for PostgreSQL 16  | RDS for PostgreSQL 15  | RDS for PostgreSQL 14  | RDS for PostgreSQL 13  | RDS for PostgreSQL 12  | RDS for PostgreSQL 11  | RDS for PostgreSQL 10  |
| -------------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| US East (Ohio)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US East (N. Virginia)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US West (N. California)    | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| US West (Oregon)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Africa (Cape Town)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Hong Kong)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Hyderabad)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Jakarta)     | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Malaysia)    | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Melbourne)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Mumbai)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (New Zealand) | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Osaka)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Seoul)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Singapore)   | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Sydney)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Asia Pacific (Taipei)      | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Thailand)    | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Asia Pacific (Tokyo)       | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Canada (Central)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Canada West (Calgary)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| China (Beijing)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| China (Ningxia)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Frankfurt)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Ireland)           | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (London)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Milan)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Paris)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Spain)             | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Stockholm)         | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Europe (Zurich)            | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Israel (Tel Aviv)          | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Mexico (Central)           | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| Middle East (Bahrain)      | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| Middle East (UAE)          | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| South America (São Paulo)  | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions | All available versions |
| AWS GovCloud (US-East)     | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
| AWS GovCloud (US-West)     | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          | Not available          |
