# Prerequisites for Migrating from a SQL Server database to Amazon Aurora MySQL

The following prerequisites are required to complete this walkthrough:

- An understanding of Amazon Relational Database Service (Amazon RDS), the applicable database technologies, and SQL.
- Create a user with AWS Identity and Access Management (IAM) credentials that allows you to launch Amazon RDS and AWS Database Migration Service (AWS DMS) instances in your AWS Region. For information about IAM credentials, see [Setting up for Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM "../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM").
- An understanding of the Amazon Virtual Private Cloud (Amazon VPC) service and security groups. For information about using Amazon VPC with Amazon RDS, see [Amazon Virtual Private Cloud (VPCs) and Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md"). For information about Amazon RDS security groups, see [Amazon RDS Security Groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md").
- An understanding of the supported features and limitations of AWS DMS. For information about AWS DMS, see https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html.
- An understanding of how to work with Microsoft SQL Server as a source and Amazon Aurora MySQL as a target. For information about working with SQL Server as a source, see [Using a SQL Server Database as a Source](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md"). Aurora MySQL is a MySQL-compatible database. For information about working with Aurora MySQL as a target, see [Using a MySQL-Compatible database as a target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md").
- An understanding of the supported data type conversion options for SQL Server and Aurora MySQL. For information about data types for SQL Server as a source, see [Source Data Types for Microsoft SQL Server](../userguide/CHAP_Reference.Source.SQLServer.md "../userguide/CHAP_Reference.Source.SQLServer.md"). For information about data types for Aurora MySQL; as a target, see [Target Data Types for MySQL](../userguide/CHAP_Reference.Target.MySQL.md "../userguide/CHAP_Reference.Target.MySQL.md").
- Size your target Aurora MySQL database host. DBAs should be aware of the load profile of the current source SQL Server database host. Consider CPU, memory, and IOPS. With Amazon RDS, you can size up the target database host, or reduce it, after the migration. If this is the first time that you’re migrating to Aurora MySQL, we recommended that you have extra capacity to account for performance issues and tuning opportunities.
- Audit your source SQL Server database. For each schema and all the objects under each schema, determine whether any of the objects are no longer being used. Deprecate these objects on the source SQL Server database, because there’s no need to migrate them if they aren’t being used.
- Decide between these migration options: migrate existing data only or migrate existing data and replicate ongoing changes.

      + If you migrate existing data only, the migration is a one-time data transfer from a SQL Server source database to the Aurora MySQL target database. If the source database remains open to changes during the migration, these changes must be applied to the target database after the migration is complete.


      ###### Note

      If the SQL Server database is an Amazon RDS database, replication is not supported, and you must use the option to migrate existing data only.
      + If you migrate existing data and replicate ongoing changes, one option is to replicate the source database changes. Replication keeps the source and target databases in sync with each other during the migration process and can reduce database downtime. With this option, you complete an initial sync operation and then configure MS-REPLICATION. This option requires the Standard, Enterprise, or Developer SQL Server edition. You enable MS-REPLICATION for each SQL Server instance that you want to use as a database source.
      + If you want to migrate existing data and replicate ongoing changes, another option is change data capture (CDC) instead of replication. This option allows AWS DMS to perform ongoing migration of data. In the case of CDC, AWS DMS uses the CDC tables to enable ongoing database migration. This option requires the Standard, Enterprise or Developer edition of SQL Server.

  For more information about AWS DMS, see [Getting started with Database Migration Service](../userguide/CHAP_GettingStarted.md "../userguide/CHAP_GettingStarted.md").
