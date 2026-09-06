

# Auto migrating databases to Amazon RDS using AWS Database Migration Service
<a name="USER_DMS_migration"></a>

You can use the RDS console to migrate a database from an EC2, on-prem or other cloud provider instance to RDS. AWS Database Migration Service (AWS DMS) is used for this. For more information about it, see [What is AWS Database Migration Service?](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) in the *AWS Database Migration Service User Guide*.

To begin the migration, you must create an equivalent RDS DB instance. After you create your target database, you can import your source into it. For source databases smaller than 1TiB, this migration action reduces the time and resources required to migrate your data into RDS.

## Overview
<a name="USER_DMS_migration-overview"></a>

The RDS console allows you to migrate EC2, on-prem or other cloud provider database into equivalent RDS database. You must create an RDS database to enable migration from the console.

**Note**  
For the databases to be equivalent, they must have the same database engine and compatible engine versions.

This approach can be used for the following database engines:
+ MySQL
+ MariaDB
+ PostgreSQL

The migration process involves the following steps:
+ Create an equivalent database in RDS. Then, set up a proper network between source and target. For EC2 instances in the same region, account, and VPC, network setup can be skipped. For more information, see [Setting up a network](https://docs.aws.amazon.com/dms/latest/userguide/dm-network.html) in the *AWS Database Migration Service User Guide*. For instructions on creating your database, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).
+ Choose the type of replication for your database:
  + **Full load migration** – RDS copies the complete source database to the target database, creating new tables in the target when necessary.
**Note**  
This option requires downtime. Your target RDS database will be unavailable to applications during the migration process.
  + **Full load and change data capture (CDC) migration** – Similar to full load migration, with this option, RDS copies over the complete source database to the target database. However, after the full load migration, RDS applies any captured changes in the source to the target database. Change data capture collects changes to the database logs by using the database engine's native API.
**Note**  
This option requires downtime. Your target RDS database will be unavailable to applications during the migration process.
  + **Change data capture (CDC)** – Use this option to keep your target database available through the migration. RDS migrates ongoing changes in your source database to the target database.
+ RDS creates the necessary resources to facilitate the migration. Once RDS creates the required resources, it notifies you about the resources created and allows you to initiate the data transfer.

  The time required to complete the migration depends on the type of replication and the size of the source database.

## Prerequisites
<a name="USER_DMS_migration-Prerequisites"></a>
+ [Setting up a network](https://docs.aws.amazon.com/dms/latest/userguide/dm-network.html) (for EC2s in the same region, account and VPC, it can be skipped)
+ Setting up source and target databases
  + **MySQL and MariaDB**

    Please follow the following basic prerequisites for your source database:
    + [Using MySQL or MariaDB as a source](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-mysql.html)

    Please follow the following basic prerequisites for your target database:
    + [Using MySQL or MariaDB as a target](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target-mysql.html)

    Additionally when migrating from a MySQL source database, your RDS account must have the Replication Admin role. You must also have the proper privileges applied for that role.
  + **PostgreSQL**

    Please follow the following prerequisites for your source database:
    + [Using PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-postgresql.html)

    Please follow the following prerequisites for your target database:
    + [Using PostgreSQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target-postgresql.html)
**Note**  
Some AWS DMS transactions are idle for some time before the DMS engine uses them again. By using the parameter `idle_in_transaction_session_timeout` in PostgreSQL versions 9.6 and higher, you can cause idle transactions to time out and fail.

## Limitations
<a name="USER_DMS_migration-Limitations"></a>

The following limitations apply to the auto-migrate process:
+ Your target database status must be **Available** to begin source database migration.
+ You can migrate your source database only to a database:
  + that is not a member of a cluster
  + that uses a supported version of MySQL, PostgreSQL, or MariaDB as listed [here](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html#CHAP_Introduction.Sources.HomogeneousDataMigrations)
+ [Limitations of DMS](https://docs.aws.amazon.com/dms/latest/userguide/data-migrations.html#data-migrations-limitations)

**Note**  
Although underlying AWS DMS tool supports selection rules for certain migration scenarios, the auto-migrating databases to RDS feature does not.