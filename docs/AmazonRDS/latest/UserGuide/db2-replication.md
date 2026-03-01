# Working with replicas for Amazon RDS for Db2

RDS for Db2 supports creating replica databases to provide read scaling and disaster recovery
capabilities. You can create replicas in two modes: read-only replicas for offloading read
workloads, and standby replicas for cross-region disaster recovery. RDS for Db2 uses IBM Db2
High Availability Disaster Recovery (HADR) technology for replication. For more information,
see [High availability disaster recovery (HADR)](https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr "https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr") in the IBM Db2 documentation.

A _Db2 replica_ database is a physical copy of your primary database. A
Db2 replica in read-only mode is called a _read replica_. A Db2 replica
in standby mode is called a _standby replica_. Db2 doesn't permit writes
in a replica, but you can promote a replica to make it writable. The promoted replica has
the replicated data to the point when the request was made to promote it. For more
information, see [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

For a summary of the features and behaviors of RDS for Db2 replicas, see [Differences between read replicas for DB engines](USER_ReadRepl.Overview.md "USER_ReadRepl.Overview.md").

## Read-only and standby replicas

When creating or modifying a Db2 replica, you can place it in either of the following
modes:

**Read-only**

This is the default. HADR transmits and applies changes from the source
database to all read replica databases. For read-only replicas, the Db2
environment variable `DB2_HADR_ROS` is set to `ON`.
The isolation level for read queries on the replica database is
`Uncommitted Read`. For more information, see [Isolation level on the active standby database](https://www.ibm.com/docs/en/db2/11.5?topic=standby-isolation-level-active-database "https://www.ibm.com/docs/en/db2/11.5?topic=standby-isolation-level-active-database") in the IBM Db2
documentation.

For general information about read replicas that applies to all DB
engines, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").
For more information about Db2 HADR, see [High availability disaster recovery (HADR)](https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr "https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr") in the IBM Db2
documentation.

**Standby**

For standby replicas, the Db2 environment variable
`DB2_HADR_ROS` is set to `OFF` so that the replica
databases don't accept user connections. The primary use for standby
replicas is cross-Region disaster recovery.

A standby replica can't serve a read-only workload. The standby replica
doesn't have any archive logs.

You can create up to three replicas from one source DB instance. You can create a
combination of read-only and standby DB replicas for the same source DB instance. After
you create a replica, you can change the replica mode. for more information, see [Modifying the RDS for Db2 replica mode](db2-replicas-changing-replica-mode.md "db2-replicas-changing-replica-mode.md").

Before creating replicas, make sure that you meet all requirements. For more
information, see [Requirements and considerations for RDS for Db2 replicas](db2-read-replicas.md "db2-read-replicas.md").

## Database activations

Db2 HADR is configured at the database level. After you create replicas, HADR is set
for all Db2 databases, including `rdsadmin`, which RDS fully manages. Before
you create Db2 replicas, you must explicitly activate all databases. Otherwise, creation
of replicas fails and Amazon RDS emits an event. After a DB instance has one or more
replicas, you can't activate or deactivate any databases on the DB instance by using the
`rdsadmin.activate_database` or `rdsadmin.deactivate_database`
stored procedures. For more information, see [Stored procedures for databases for RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").

## HADR configurations

You can see all HADR configurations for a database by connecting to the database and
then running `db2 get db cfg`.

## Archive log retention

Amazon RDS purges logs from a primary DB instance after the following conditions have been
met:

- The logs are at least two hours old.
- The setting for archive log retention hours has passed.
- The archive logs were successfully replicated to all replica DB instances.
  This condition applies both to DB instances in the same AWS Region and to
  cross-Region DB instances.

For information about setting archive log retention hours, see [rdsadmin.set_archive_log_retention](db2-sp-managing-databases.md#db2-sp-set-archive-log-retention "db2-sp-managing-databases.md#db2-sp-set-archive-log-retention").

Amazon RDS checks and cleans up each database individually. If a database loses the HADR
connection or if information about the connection isn't available, then Amazon RDS skips the
database and doesn't purge the archive logs.

## Outages during Db2 replication

When you create a replica, Amazon RDS takes a DB snapshot of your source DB instance and
begins replication. When the DB snapshot operation begins, the source DB instance
experiences a very brief I/O suspension. The I/O suspension typically lasts about one
second. However, if the source DB instance is a Multi-AZ deployment, then the source DB instance
doesn't experience any I/O suspension. This is because with Multi-AZ deployments, the snapshot is
taken from the secondary DB instance.

The DB snapshot becomes the Db2 replica. Amazon RDS sets the necessary parameters and
permissions for the source database and replica without any service interruption.
Similarly, if you delete a replica, no outage occurs.
