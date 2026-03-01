# Supported Regions and DB engines for cross-Region read replicas in Amazon RDS

By using cross-Region read replicas in Amazon RDS, you can create a MariaDB, MySQL, Oracle,
PostgreSQL, or SQL Server read replica in a different Region from the source DB instance. For
more information about cross-Region read replicas, including source and destination Region
considerations, see [Creating a read replica in a different AWS Region](USER_ReadRepl.md "USER_ReadRepl.md").

Cross-Region read replicas are not available for the following engines:

- RDS for Db2

###### Topics

- [Cross-Region read replicas with RDS for MariaDB](#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.mdb "#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.mdb")
- [Cross-Region read replicas with RDS for MySQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.my "#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.my")
- [Cross-Region read replicas with RDS for Oracle](#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.ora "#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.ora")
- [Cross-Region read replicas with RDS for PostgreSQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.pg "#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.pg")
- [Cross-Region read replicas with RDS for SQL Server](#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.sq "#Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.sq")

## Cross-Region read replicas with RDS for MariaDB

Cross-Region read replicas with RDS for MariaDB are available in all Regions for the following
versions:

- RDS for MariaDB 11.8 (All available versions)
- RDS for MariaDB 11.4 (All available versions)
- RDS for MariaDB 10.11 (All available versions)
- RDS for MariaDB 10.6 (All available versions)
- RDS for MariaDB 10.5 (All available versions)
- RDS for MariaDB 10.4 (All available versions)

## Cross-Region read replicas with RDS for MySQL

Cross-Region read replicas with RDS for MySQL are available in all Regions for the following
versions:

- RDS for MySQL 8.4 (All available versions)
- RDS for MySQL 8.0 (All available versions)
- RDS for MySQL 5.7 (All available versions)

## Cross-Region read replicas with RDS for Oracle

Cross-Region read replicas for RDS for Oracle are available in all AWS Regions for all
supported database versions using Enterprise Edition. Replicas are supported only in non-CDBs
and in the single-tenant configuration of the CDB architecture. Cross-Region read replicas
aren't supported in the multi-tenant configuration of the CDB architecture.

For more information on additional requirements for cross-Region read replicas with
RDS for Oracle, see [Requirements and considerations for RDS for Oracle replicas](oracle-read-replicas.md "oracle-read-replicas.md").

## Cross-Region read replicas with RDS for PostgreSQL

Cross-Region read replicas with RDS for PostgreSQL are available in all Regions for the
following versions:

- RDS for PostgreSQL 18 (All available versions)
- RDS for PostgreSQL 17 (All available versions)
- RDS for PostgreSQL 16 (All available versions)
- RDS for PostgreSQL 15 (All available versions)
- RDS for PostgreSQL 14 (All available versions)
- RDS for PostgreSQL 13 (All available versions)
- RDS for PostgreSQL 12 (All available versions)
- RDS for PostgreSQL 11 (All available versions)
- RDS for PostgreSQL 10 (All available versions)

## Cross-Region read replicas with RDS for SQL Server

Cross-Region read replicas with RDS for SQL Server are available in all Regions for the following versions using
Microsoft SQL Server Enterprise Edition:

- RDS for SQL Server 2022
- RDS for SQL Server 2019 (Version 15.00.4073.23 and higher)
- RDS for SQL Server 2017 (Version 14.00.3281.6 and higher)
- RDS for SQL Server 2016 (Version 13.00.6300.2 and higher)
