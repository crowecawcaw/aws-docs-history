# Sources for AWS DMS

You can use different source data stores in different AWS DMS features. The following
sections contain the lists of supported source data stores for each AWS DMS feature.

###### Topics

- [Source endpoints for data migration](#CHAP_Introduction.Sources.DataMigration "#CHAP_Introduction.Sources.DataMigration")
- [Source databases for DMS Fleet Advisor](#CHAP_Introduction.Sources.FleetAdvisor "#CHAP_Introduction.Sources.FleetAdvisor")
- [Source data providers for DMS Schema Conversion](#CHAP_Introduction.Sources.SchemaConversion "#CHAP_Introduction.Sources.SchemaConversion")
- [Source data providers for DMS homogeneous data migrations](#CHAP_Introduction.Sources.HomogeneousDataMigrations "#CHAP_Introduction.Sources.HomogeneousDataMigrations")

## Source endpoints for data migration

You can use the following data stores as source endpoints for data migration using
AWS DMS.

###### On-premises and EC2 instance databases

- Oracle versions 10.2 and higher (for versions 10.x), 11g and up to 12.2, 18c,
  and 19c for the Enterprise, Standard, Standard One, and Standard Two
  editions
- Microsoft SQL Server versions 2008 (supported in DMS v3.5.4), 2008R2(supported in DMS v3.5.4),
  2012, 2014, 2016, 2017, 2019, and 2022.
  - The
    Enterprise, Standard, Workgroup, Developer, and Web editions support full-load replication.
  - The
    Enterprise, Standard (version 2016 and higher), and Developer editions support CDC (ongoing) replication
    in addition to full-load.
  - The Express
    edition isn't supported.

- MySQL versions 5.5, 5.6, 5.7, 8.0, and 8.4

###### Note

| MySQL and DMS Compatibility | MySQL Version   | DMS Version | Compressed transaction payload supporting |
| --------------------------- | --------------- | ----------- | ----------------------------------------- |
| 8                           | 3.4.0 and above | No          |
| 8.0 (Google Cloud)          | 3.4.6 and above | No          |
| 8.4                         | 3.5.4 and above | No          |

- MariaDB (supported as a MySQL-compatible data source) versions 10.0 (only
  versions 10.0.24 and higher), 10.2, 10.3, 10.4, 10.5, 10.6, and 11.4.3 to
  11.4.5.

###### Note

Support for MariaDB as a source is available in all AWS DMS versions
where MySQL is supported.

- PostgreSQL version 9.4 and higher (for versions 9.x), 10.x, 11.x, 12.x, 13.x
  14.x, 15.x, 16.x, 17.x, and 18.x.

###### Note

    + AWS DMS only supports PostgreSQL version 15.x in versions 3.5.1
     and higher.
    + AWS DMS only supports PostgreSQL version 16.x in versions 3.5.3
     and higher.
    + AWS DMS only supports PostgreSQL version 17.x and 18.x in versions 3.6.1
     and higher.

- MongoDB versions 3.x, 4.0, 4.2, 4.4, 5.0, 6.0 and 7.0.
- SAP Adaptive Server Enterprise (ASE) versions 12.5, 15, 15.5, 15.7, 16, and
  higher
- IBM Db2 for Linux, UNIX, and Windows (Db2 LUW) versions:
  - Version 9.7, all fix packs
  - Version 10.1, all fix packs
  - Version 10.5, all fix packs except for Fix Pack 5
  - Version 11.1, all fix packs
  - Version 11.5, Mods (0-8) with only Fix Pack Zero

- IBM Db2 for z/OS version 12

###### Third-party managed database services:

- Microsoft Azure SQL Database
- Microsoft Azure PostgreSQL Flexible Server versions 11.2, 12.15, 13.11, 14.8, and 15.3.
- Microsoft Azure MySQL Flexible Server versions 5.7 and 8.
- Google Cloud for MySQL versions 5.6, 5.7, and 8.0.
- Google Cloud for PostgreSQL versions 9.6, 10, 11, 12, 13, 14, and 15.
- OCI MySQL Heatwave version 8.0.34.

###### Amazon RDS instance databases, and Amazon Simple Storage Service (Amazon S3)

- Oracle versions 11g (versions 11.2.0.4 and higher) and up to 12.2, 18c, and
  19c for the Enterprise, Standard, Standard One, and Standard Two
  editions.
- Microsoft SQL Server versions 2016, 2017, 2019, and 2022 for the Enterprise,
  Standard, Workgroup, and Developer editions. For more information, see
  [Amazon RDS for Microsoft SQL Server](../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md "../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md") in the
  _Amazon RDS user guide_.

###### Note

AWS DMS does not support SQL Server Express. The Web edition is only
supported for full-load only replication.

- MySQL versions 5.5, 5.6, 5.7, 8.0, and 8.4.

###### Note

| MySQL and DMS Compatibility | MySQL Version   | DMS Version | Compressed transaction payload supporting |
| --------------------------- | --------------- | ----------- | ----------------------------------------- |
| 8                           | 3.4.0 and above | No          |
| 8.0 (Google Cloud)          | 3.4.6 and above | No          |
| 8.4                         | 3.5.4 and above | No          |

- MariaDB (supported as a MySQL-compatible data source) versions 10.0.24 to
  10.0.28, 10.2, 10.3, 10.4, 10.5, 10.6, and 11.4.3 to 11.4.5.

###### Note

Support for MariaDB as a source is available in all AWS DMS versions
where MySQL is supported.

- PostgreSQL version 10.x, 11.x, 12.x, 13.x, 14.x, 15.x, 16.x, 17.x, and 18.x.

###### Note

    + AWS DMS only supports PostgreSQL version 15.x in versions 3.5.1
     and higher.
    + AWS DMS only supports PostgreSQL version 16.x in versions 3.5.3
     and higher.
    + AWS DMS only supports PostgreSQL version 17.x and 18.x in versions 3.6.1
     and higher.

- Amazon Aurora with MySQL compatibility (supported as a MySQL-compatible data
  source)
- Amazon Aurora with PostgreSQL compatibility (supported as a PostgreSQL-compatible
  data source)
- Amazon S3
- Amazon DocumentDB (with MongoDB compatibility) versions 3.6, 4.0, and 5.0.
- Amazon RDS for IBM Db2 LUW.

For information about working with a specific source, see [Working with AWS DMS endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").

For information about supported target endpoints, see [Target endpoints for data migration](CHAP_Introduction.md#CHAP_Introduction.Targets.DataMigration "CHAP_Introduction.md#CHAP_Introduction.Targets.DataMigration").

## Source databases for DMS Fleet Advisor

DMS Fleet Advisor supports the following source databases.

- Microsoft SQL Server version 2012 and up to 2019
- MySQL version 5.6 and up to 8
- Oracle version 11g Release 2 and up to 12c, 19c, and 21c
- PostgreSQL version 9.6 and up to 13

For information about working with a specific source, see [Creating database users for AWS DMS Fleet Advisor](fa-database-users.md "fa-database-users.md").

For the list of databases that DMS Fleet Advisor uses to generate target recommendations,
see [Targets for DMS Fleet Advisor](CHAP_Introduction.md#CHAP_Introduction.Targets.FleetAdvisor "CHAP_Introduction.md#CHAP_Introduction.Targets.FleetAdvisor").

## Source data providers for DMS Schema Conversion

DMS Schema Conversion supports the following data providers as sources for your migration
projects.

- Microsoft SQL Server version 2008 R2, 2012, 2014, 2016, 2017, 2019, and
  2022
- Oracle version 10.2 and higher, 11g and up to 12.2, 18c, and 19c, and Oracle Data Warehouse
- PostgreSQL version 9.2 and higher
- MySQL version 5.5, 5.6, 5.7, and 8.0.
- IBM Db2 for z/OS version 12
- SAP ASE (Sybase ASE) version 16

###### Note

DMS Schema Conversion supports all the Amazon RDS version sources listed in this topic.

Your source data provider can be a self-managed engine running on-premises or on an
Amazon Elastic Compute Cloud (Amazon EC2) instance.

For information about working with a specific source, see [Creating source data providers in DMS Schema Conversion](data-providers-source.md "data-providers-source.md").

For information about supported target databases, see [Target data providers for DMS Schema Conversion](CHAP_Introduction.md#CHAP_Introduction.Targets.SchemaConversion "CHAP_Introduction.md#CHAP_Introduction.Targets.SchemaConversion").

The AWS Schema Conversion Tool (AWS SCT) supports more source and target databases than DMS Schema Conversion. For
information about databases that AWS SCT supports, see [What is the AWS Schema Conversion Tool](../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md "../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md").

## Source data providers for DMS homogeneous data migrations

You can use the following data providers as sources for homogeneous data migrations to on-premises and EC2 instance databases.

- MySQL version 5.7 and 8.0
- MariaDB version 10.2x
- PostgreSQL version 10.4 to 16.x.
- MongoDB version 4.x, 5.x, 6.0, 7.0
- Amazon DocumentDB version 3.6, 4.0, 5.0

You can use the following data providers as sources for homogeneous data migrations to Amazon Relational Database Service instance databases.

- Aurora MySQL version 5.7 and 8.0
- RDS for MySQL version 5.7 and 8.0
- RDS for MariaDB version 10.2.x

Your source data provider can be a self-managed engine running on-premises or on an Amazon EC2 instance.
Also, you can use an Amazon RDS DB instance as a source data provider.

For information about working with a specific source, see [Creating source data providers for homogeneous data migrations in AWS DMS](dm-data-providers-source.md "dm-data-providers-source.md").

For information about supported target databases, see [Target data providers for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Targets.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Targets.HomogeneousDataMigrations").
