# Overview of RDS for Oracle replicas

An _Oracle replica_ database is a physical copy of your primary database. An Oracle replica in read-only mode is called a
_read replica_. An Oracle replica in mounted mode is called a _mounted replica_. Oracle Database
doesn't permit writes in a replica, but you can promote a replica to make it writable. The promoted read replica has the replicated data to
the point when the request was made to promote it.

The following video provides a helpful overview of RDS for Oracle disaster recovery.

For more information, see the blog post [Managed disaster recovery with
Amazon RDS for Oracle cross-Region automated backups - Part 1](https://aws.amazon.com/blogs/database/managed-disaster-recovery-with-amazon-rds-for-oracle-cross-region-automated-backups-part-1/ "https://aws.amazon.com/blogs/database/managed-disaster-recovery-with-amazon-rds-for-oracle-cross-region-automated-backups-part-1/") and [Managed disaster recovery with Amazon RDS for Oracle cross-Region
automated backups - Part 2](https://aws.amazon.com/blogs/database/part-2-managed-disaster-recovery-with-amazon-rds-for-oracle-xrab/ "https://aws.amazon.com/blogs/database/part-2-managed-disaster-recovery-with-amazon-rds-for-oracle-xrab/").

###### Topics

- [Read-only and mounted replicas](#oracle-read-replicas.overview.modes "#oracle-read-replicas.overview.modes")
- [Read replicas of CDBs](#oracle-read-replicas.overview.data-guard "#oracle-read-replicas.overview.data-guard")
- [Archived redo log retention](#oracle-read-replicas.overview.log-retention "#oracle-read-replicas.overview.log-retention")
- [Outages during Oracle
  replication](#oracle-read-replicas.overview.outages "#oracle-read-replicas.overview.outages")

## Read-only and mounted replicas

When creating or modifying an Oracle replica, you can place it in either of the following modes:

Read-only

This is the default. Active Data Guard transmits and applies changes from the source database to all read replica
databases.

You can create up to five read replicas from one source DB instance. For general information about read replicas that
applies to all DB engines, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md"). For information about Oracle
Data Guard, see [Oracle Data Guard concepts and administration](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/oracle-data-guard-concepts.html#GUID-F78703FB-BD74-4F20-9971-8B37ACC40A65 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/oracle-data-guard-concepts.html#GUID-F78703FB-BD74-4F20-9971-8B37ACC40A65") in the Oracle documentation.

Mounted

In this case, replication uses Oracle Data Guard, but the replica database doesn't accept user connections. The primary use
for mounted replicas is cross-Region disaster recovery.

A mounted replica can't serve a read-only workload. The mounted replica deletes archived redo log files after it applies
them, regardless of the archived log retention policy.

You can create a combination of mounted and read-only DB replicas for the same source DB instance. You can change a read-only replica to
mounted mode, or change a mounted replica to read-only mode. In either case, the Oracle database preserves the archived log retention
setting.

## Read replicas of CDBs

RDS for Oracle supports Data Guard read replicas for Oracle Database 19c and 21c CDBs in both single-tenant and multi-tenant configurations.
You can create, manage, and promote read replicas in a
CDB just as you can in a non-CDB. Mounted replicas are also supported. You get the
following benefits:

- Managed disaster recovery, high availability, and read-only access to your
  replicas
- The ability to create read replicas in a different AWS Region.
- Integration with the existing RDS read replica APIs: [CreateDBInstanceReadReplica](../APIReference/API_CreateDBInstanceReadReplica.md "../APIReference/API_CreateDBInstanceReadReplica.md"), [PromoteReadReplica](../APIReference/API_PromoteReadReplica.md "../APIReference/API_PromoteReadReplica.md"), and [SwitchoverReadReplica](../APIReference/API_SwitchoverReadReplica.md "../APIReference/API_SwitchoverReadReplica.md")

To use this feature, you need an Active Data Guard license and an Oracle Database
Enterprise Edition license for both the replica and primary DB instances. There are no
additional costs related to using CDB architecture. You pay only for your DB instances.

For more information about the single-tenant and multi-tenant configurations of the
CDB architecture, see [Overview of RDS for Oracle CDBs](Oracle.Concepts.md "Oracle.Concepts.md").

## Archived redo log retention

If a primary DB instance has no cross-Region read replicas, Amazon RDS for Oracle keeps a minimum of two hours of archived redo logs on the
source DB instance. This is true regardless of the setting for `archivelog retention hours` in
`rdsadmin.rdsadmin_util.set_configuration`.

RDS purges logs from the source DB instance after two hours or after the archive log retention hours setting has passed, whichever is
longer. RDS purges logs from the read replica after the archive log retention hours setting has passed only if they have been successfully
applied to the database.

In some cases, a primary DB instance might have one or more cross-Region read replicas. If so, Amazon RDS for
Oracle keeps the transaction logs on the source DB instance until they have been transmitted and applied to
all cross-Region read replicas. For information about `rdsadmin.rdsadmin_util.set_configuration`,
see [Retaining archived redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

## Outages during Oracle

replication

When you create a read replica, Amazon RDS takes a DB snapshot of your source DB instance and begins
replication. The source DB instance experiences a very brief I/O suspension when the DB snapshot operation
begins. The I/O suspension typically lasts about one second. You can avoid the I/O suspension if
the source DB instance is a Multi-AZ deployment, because in that case the snapshot is taken from the
secondary DB instance.

The DB snapshot becomes the Oracle replica. Amazon RDS sets the necessary parameters and
permissions for the source database and replica without service interruption. Similarly,
if you delete a replica, no outage occurs.
