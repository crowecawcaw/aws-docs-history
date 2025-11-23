# Targets for AWS DMS

You can use different target data stores in different AWS DMS features. The following
sections contain the lists of supported target data stores for each AWS DMS feature.

###### Topics

- [Target endpoints for data migration](#CHAP_Introduction.Targets.DataMigration "#CHAP_Introduction.Targets.DataMigration")
- [Target databases for DMS Fleet Advisor](#CHAP_Introduction.Targets.FleetAdvisor "#CHAP_Introduction.Targets.FleetAdvisor")
- [Target data providers for DMS Schema Conversion](#CHAP_Introduction.Targets.SchemaConversion "#CHAP_Introduction.Targets.SchemaConversion")
- [Target data providers for DMS homogeneous data migrations](#CHAP_Introduction.Targets.HomogeneousDataMigrations "#CHAP_Introduction.Targets.HomogeneousDataMigrations")

## Target endpoints for data migration

You can use the following data stores as target endpoints for data migration using
AWS DMS.

###### On-premises and Amazon EC2 instance databases

- Oracle versions 10g, 11g, 12c, 18c, and 19c for the Enterprise, Standard,
  Standard One, and Standard Two editions
- Microsoft SQL Server versions 2005, 2008, 2008R2, 2012, 2014, 2016, 2017, 2019, and 2022
  for the Enterprise, Standard, Workgroup, and Developer editions

###### Note

AWS DMS doesn't support SQL Server Web and Express editions.

- MySQL versions 5.5, 5.6, 5.7, 8.0, and 8.4
- MariaDB (supported as a MySQL-compatible data target) versions 10.0.24 to
  10.0.28, 10.2, 10.3, 10.4, 10.5, 10.6, and 11.4.3 to 11.4.5.

###### Note

Support for MariaDB as a target is available in all AWS DMS versions
where MySQL is supported.

- PostgreSQL version 9.4 and higher (for versions 9.x), 10.x, 11.x, 12.x, 13.x,
  14.x, 15.x, 16.x, and 17.x.

###### Note

    + AWS DMS only supports PostgreSQL version 15.x in versions 3.5.1
     and higher.
    + AWS DMS only supports PostgreSQL version 16.x in versions 3.5.3
     and higher.
    + AWS DMS only supports PostgreSQL version 17.x in versions 3.6.1
     and higher.

- SAP Adaptive Server Enterprise (ASE) versions 15, 15.5, 15.7, 16, and
  higher
- Redis OSS versions 6.x

###### Amazon RDS instance databases, Amazon Redshift, Amazon Redshift Serverless, Amazon DynamoDB, Amazon S3, Amazon OpenSearch Service, Amazon ElastiCache (Redis OSS), Amazon Kinesis Data Streams, Amazon DocumentDB,

Amazon Neptune, and Apache Kafka

- Oracle versions 11g (versions 11.2.0.3.v1 and higher), 12c, 18c, and 19c for
  the Enterprise, Standard, Standard One, and Standard Two editions
- Microsoft SQL Server versions 2012, 2014, 2016, 2017, 2019, and 2022 for the
  Enterprise, Standard, Workgroup, and Developer editions

###### Note

AWS DMS doesn't support SQL Server Web and Express editions.

- MySQL versions 5.5, 5.6, 5.7, 8.0, and 8.4.
- MariaDB (supported as a MySQL-compatible data target) versions 10.0.24 to
  10.0.28, 10.2, 10.3, 10.4, 10.5, 10.6, and 11.4.3 to 11.4.5.

###### Note

Support for MariaDB as a target is available in all AWS DMS versions
where MySQL is supported.

- PostgreSQL version 10.x, 11.x, 12.x, 13.x, 14.x, 15.x, 16.x, and 17.x.

###### Note

    + AWS DMS only supports PostgreSQL version 15.x in versions 3.5.1
     and higher.
    + AWS DMS only supports PostgreSQL version 16.x in versions 3.5.3
     and higher.
    + AWS DMS only supports PostgreSQL version 17.x in versions 3.6.1
     and higher.

- IBM Db2 LUW versions 11.1 and 11.5
- Amazon Aurora MySQL-Compatible Edition
- Amazon Aurora PostgreSQL-Compatible Edition
- Amazon Aurora PostgreSQL Limitless
- Amazon Aurora Serverless v2
- Amazon Redshift
- Amazon Redshift Serverless
- Amazon S3
- Amazon DynamoDB
- Amazon OpenSearch Service
- Amazon ElastiCache (Redis OSS)
- Amazon Kinesis Data Streams
- Amazon DocumentDB (with MongoDB compatibility)
- Amazon Neptune
- Apache Kafka – [Amazon Managed Streaming for Apache Kafka
  (Amazon MSK)](https://aws.amazon.com/msk/ "https://aws.amazon.com/msk/") and [self-managed Apache Kafka](https://kafka.apache.org/ "https://kafka.apache.org/")
- Babelfish (version 3.2.0 and higher) for Aurora PostgreSQL (versions 15.3/14.8 and
  higher)

For information about working with a specific target, see [Working with AWS DMS endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").

For information about supported source endpoints, see [Source endpoints for data migration](CHAP_Introduction.md#CHAP_Introduction.Sources.DataMigration "CHAP_Introduction.md#CHAP_Introduction.Sources.DataMigration").

## Target databases for DMS Fleet Advisor

DMS Fleet Advisor generates target recommendations using the latest version of the following target
databases.

- Amazon Aurora MySQL
- Amazon Aurora PostgreSQL
- Amazon RDS for MySQL
- Amazon RDS for Oracle
- Amazon RDS for PostgreSQL
- Amazon RDS for SQL Server

For information about target recommendations in DMS Fleet Advisor, see [Using the AWS DMS Fleet Advisor Target Recommendations
feature](fa-recommendations.md "fa-recommendations.md").

For information about supported source databases, see [Source databases for DMS Fleet Advisor](CHAP_Introduction.md#CHAP_Introduction.Sources.FleetAdvisor "CHAP_Introduction.md#CHAP_Introduction.Sources.FleetAdvisor").

## Target data providers for DMS Schema Conversion

DMS Schema Conversion supports the following data providers as targets for your migration
projects.

- Amazon Aurora MySQL 8.0.32
- Amazon Aurora PostgreSQL 14.x, 15.x, 16.x
- Amazon RDS for MySQL 8.0.23
- Amazon RDS for PostgreSQL 14.x, 15.x, 16.x
- Amazon Redshift
- Amazon RDS for Db2 version 11.5.

For information about working with a specific target, see [Creating and setting target data providers in DMS Schema Conversion](data-providers-target.md "data-providers-target.md").

For information about supported source databases, see [Source data providers for DMS Schema Conversion](CHAP_Introduction.md#CHAP_Introduction.Sources.SchemaConversion "CHAP_Introduction.md#CHAP_Introduction.Sources.SchemaConversion").

## Target data providers for DMS homogeneous data migrations

You can use the following data providers as targets for homogeneous data migrations.

- Amazon Aurora MySQL version 5.7 and 8.0
- Amazon Aurora PostgreSQL version 10.4 to 16.x
- Amazon Aurora Serverless v2
- Amazon RDS for MySQL version 5.7 and 8.0
- Amazon RDS for MariaDB version 10.2x
- Amazon RDS for PostgreSQL version 10.4 to 16.x
- Amazon DocumentDB version 4.0, 5.0 and DocumentDB Elastic cluster

For information about working with a specific target, see [Creating and setting a target database to work with AWS DMS schema conversion](dm-data-providers-target.md "dm-data-providers-target.md").

For information about supported source databases, see [Source data providers for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").
