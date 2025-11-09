# Requirements and considerations for RDS for Db2

replicas

Db2 replica requirements fall into several categories: licensing and versioning, backup
and restore considerations, replication behavior, and general operational considerations.
Before creating a Db2 replica, familiarize yourself with the following requirements and
considerations.

## Version and

licensing requirements for RDS for Db2 replicas

Before you create an RDS for Db2 replica, review the following information about versions
and licensing models:

- **Supported versions** – All Db2 11.5
  versions support replica DB instances.

Source and replica DB instances must use the same major version. Db2 replicas
support minor version upgrades but not major version upgrades. For information
about upgrading DB instances, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

###### Note

When upgrading a source DB instance, all replicas are automatically
upgraded to maintain version compatibility.

- **Valid licensing models and replica modes**
  – Both Db2 Advanced Edition (AE) and Standard Edition (SE) can create
  replicas in read-only or standby mode for both the Bring Your Own License (BYOL)
  model and the Db2 license through AWS Marketplace model.
- **Custom parameter group** – You must
  specify a custom parameter group for the replica.

For replicas that use the BYOL model, this custom parameter group must include
your IBM Site ID and IBM Customer ID. For more information, see [IBM IDs for bring your own
license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info "db2-licensing.md#db2-prereqs-ibm-info"). You
can specify this custom parameter group for the replica by using the AWS Management Console,
the AWS CLI , or the RDS API.

- **vCPU count** varies by replica mode and
  licensing model:
  - **Standby replicas** always use two vCPUs
    regardless of DB instance size.
    - **BYOL model** – AWS License Manager
      configurations show that RDS for Db2 DB instances use two
      vCPUs.
    - **Db2 license through AWS Marketplace
      model** – Bills reflect license costs for
      two vCPUs.

  - **Read-only replicas** use the same vCPU
    count as the DB instance size.
    - **BYOL model** – AWS License Manager
      configurations show that RDS for Db2 DB instances use the same
      number of vCPUs that match the DB instance size.
    - **Db2 license through AWS Marketplace
      model** – Bills reflect license costs for
      the same number of vCPUs that match the DB instance size.

## Backup and restore

considerations for RDS for Db2 replicas

Replica backups have different behavior than primary database backups. Consider the
following backup and restore requirements:

- To create snapshots of RDS for Db2 replicas or turn on automatic backups, make
  sure to set the backup retention period manually. Automatic backups aren't
  turned on by default.
- When you restore a replica backup, you restore to the database time, not the
  time that the backup was taken. The _database time_ refers
  to the latest applied transaction time of the data in the backup. The difference
  is significant because a replica can lag behind the primary database for minutes
  or hours. When there are multiple databases, RDS for Db2 uses the earliest database
  time.

To find the difference, run the AWS CLI [describe-db-snapshots](../../../cli/latest/reference/rds/describe-db-snapshots.md "../../../cli/latest/reference/rds/describe-db-snapshots.md") command or call the RDS API [DescribeDBSnapshots](../APIReference/API_DescribeDBSnapshots.md "../APIReference/API_DescribeDBSnapshots.md") operation. Compare the
`SnapshotDatabaseTime` value to the
`OriginalSnapshotCreateTime` value. The
`SnapshotDatabaseTime` value is the database time of the replica
backup. The `OriginalSnapshotCreateTime` value is the latest applied
transaction on the primary database.

For more information about backups and restoring backups, see [Working with RDS for Db2 replica backups](db2-read-replicas.md "db2-read-replicas.md").

## Replication considerations

for RDS for Db2 replicas

Db2 replicas use HADR technology with specific limitations and behaviors. Review the
following replication considerations:

- Replication uses Db2 HADR for all databases on the RDS for Db2 DB
  instance.
- Replication doesn't support the `LOAD` command. If you run the
  `LOAD` command from the source DB instance, you will receive
  inconsistent data.
- RDS for Db2 doesn't replicate the following items:
  - Storage access. Be aware of data, such as external tables, that rely
    on storage access.
  - Non-inline LOBs.
  - Binaries of external stored procedures (in C or Java).

- For standby replicas, RDS for Db2 replicates the following items:
  - Local users, except master users
  - Database configuration parameters

- For read-only replicas, RDS for Db2 replicates the following items:
  - Local users, except master users
  - SID group mappings

## Miscellaneous

considerations for RDS for Db2 replicas

Additional operational considerations apply to Db2 replicas. Review the following
items:

- RDS for Db2 replicates database configurations to the replicas. When RDS for Db2
  promotes a replica, it deactivates and activates each database.
- RDS for Db2 replicates the local users, but not the master user, and SID group
  mappings to the replicas. You can modify the master user on the replica. For
  more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
- All databases must be in an active state. For information about activating
  databases, see [Stored procedures for databases for
  RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").
- All stored procedures for creating, dropping, restoring, or rolling forward
  databases must be completed before creating a replica. For information about
  these stored procedures, see [Stored procedures for databases for
  RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").
- When the replica is created, Amazon RDS sets the database-level parameter
  `blocknonlogged` for all databases on the source DB instance to
  `YES`. When the source replica becomes a standalone instance
  again, Amazon RDS sets the value back to `NO`. For more information, see
  [blocknonlogged - Block creation of tables that allow non-logged activity
  configuration parameter](https://www.ibm.com/docs/en/db2/11.1?topic=dcp-blocknonlogged-block-creation-tables-that-allow-non-logged-activity "https://www.ibm.com/docs/en/db2/11.1?topic=dcp-blocknonlogged-block-creation-tables-that-allow-non-logged-activity") in the IBM Db2 documentation.
- When the replica is created, Amazon RDS sets the database-level parameter
  `logindexbuild` for all databases on the source DB instance to
  `YES`. When the source replica becomes a standalone instance
  again, Amazon RDS sets the value back to `NO`. For more information, see
  [logindexbuild - Log index pages created configuration parameter](https://www.ibm.com/docs/en/db2/11.1?topic=parameters-logindexbuild-log-index-pages-created "https://www.ibm.com/docs/en/db2/11.1?topic=parameters-logindexbuild-log-index-pages-created") in
  the IBM Db2 documentation.
