# Supported Regions and DB engines for Amazon RDS Blue/Green Deployments

A blue/green deployment copies a production database environment in a separate, synchronized
staging environment. By using Amazon RDS Blue/Green Deployments, you can make changes to the database
in the staging environment without affecting the production environment. For example, you can
upgrade the major or minor DB engine version, change database parameters, or make schema changes
in the staging environment. When you are ready, you can promote the staging environment to be
the new production database environment. For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md "blue-green-deployments.md").

Blue/green deployments are supported in all AWS Regions.

Blue/green deployments are _not_ supported with the following
engines:

- RDS for Db2
- RDS for SQL Server
- RDS for Oracle

###### Topics

- [Blue/green deployments with RDS for MariaDB](#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.mdb "#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.mdb")
- [Blue/green deployments with RDS for MySQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.mysql "#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.mysql")
- [Blue/green deployments with RDS for PostgreSQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.postgres "#Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.postgres")

## Blue/green deployments with RDS for MariaDB

For RDS for MariaDB, blue/green deployments are supported for the following versions:

- RDS for MariaDB 12.3 (All available versions)
- RDS for MariaDB 11.8 (All available versions)
- RDS for MariaDB 11.4 (All available versions)
- RDS for MariaDB 10.2 and higher 10 versions

## Blue/green deployments with RDS for MySQL

For RDS for MySQL, blue/green deployments are supported for the following versions:

- RDS for MySQL 8.4 (All available versions)
- RDS for MySQL 8.0 (All available versions)
- RDS for MySQL 5.7 (All available versions)

## Blue/green deployments with RDS for PostgreSQL

For RDS for PostgreSQL, blue/green deployments are supported for version 11.1 and all higher
major and minor versions.

###### Note

Under certain conditions, RDS for PostgreSQL uses logical replication instead of physical
replication to keep the green environment in sync with the blue environment. For more
information, see [PostgreSQL replication methods for blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").
