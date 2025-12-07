# Oracle Active Data Guard and MySQL replicas

With AWS DMS, you can create and manage Oracle Active Data Guard and MySQL replicas to achieve high availability and data redundancy for your databases. Oracle Active Data Guard provides a physical standby database that remains synchronized with the primary database, while MySQL replicas maintain an identical copy of data from a source database instance.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                    |
| -------------------------------- | ---------------------------------- | ------------------------- | ------------------------------------------------------------------ |
| Three star feature compatibility | N/A                                | N/A                       | Distribute load, applications, or users across multiple instances. |

## Oracle usage

Oracle Active Data Guard (ADG) is a synced database architecture with primary and standby databases. The difference between Data Guard and ADG is that ADG standby databases allow read access only.

The following diagram illustrates the ADG architecture.

![Active Data Guard architecture](images/pb-active-data-guard.png)

- **Primary DB** — The main database open to read and write operations.
- **Redo/Archive** — The redo files and archives that store the redo entries for recovery operations.
- **Data Broker** — The data guard broker service is responsible for all failover and syncing operations.
- **Standby DB** — The secondary database that allows read operations only. This database remains in recovery mode until it is shut down or becomes the primary (failover or switchover).
- **Log Apply** — Runs all the redo log entries from the redo and archives files on the standby db.
- **Redo/Archive** — Contains the redo files and archives that are synced from the primary log and archive files.
- **Data Broker** — The Data Guard broker service is responsible for all failover and syncing operations.

All components use SQL\*NET protocol.

**Special features**

- You can select asynchronously for best performance or synchronously for best data protection.
- You can temporarily convert a standby database to a snapshot database and allow read/write operations. When you are done running QA, testing, loads, or other operations, it can be switched back to standby.
- A sync gap can be specified between the primary and standby databases to account for human errors (for example, creating 12 hours gap of sync).

For more information, see [Creating a Physical Standby Database](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/creating-oracle-data-guard-physical-standby.html#GUID-B511FB6E-E3E7-436D-94B5-071C37550170 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/creating-oracle-data-guard-physical-standby.html#GUID-B511FB6E-E3E7-436D-94B5-071C37550170") in the _Oracle documentation_.

## MySQL usage

You can use Aurora replicas for scaling read operations and increasing availability such as Oracle Active Data Guard, but with less configuration and administration. You can easily manage many replicas from the Amazon RDS console. Alternatively, you can use the AWS CLI for automation.

When you create Aurora MySQL instances, use one of the two following replication options:

- **Multi-AZ (Availability Zone)** — Create a replicating instance in a different region.
- **Instance Read Replicas** — Create a replicating instance in the same region.

For instance options, you can use one of the two following options:

- Create Aurora Replica.
- Create Cross Region Read Replica.

The main differences between these two options are:

- Cross Region creates a new reader cluster in a different region. Use Cross Region for a higher level of Higher Availability and to keep data closer to the end users.
- Cross Region has more lag between the two instances.
- Additional charges apply for transferring data between two regions.

To view the most current lag value between the primary and replicas, query the `mysql.ro_replica_status` table and check the `Replica_lag_in_msec` column. This column value is provided to Amazon CloudWatch as the ReplicaLag metric. The values in the `mysql.ro_replica_status` are also provided in the `INFORMATION_SCHEMA.REPLICA_HOST_STATUS` table in your Aurora MySQL DB cluster.

DDL statements that run on the primary instance may interrupt database connections on the associated Aurora Replicas. If an Aurora Replica connection is actively using a database object such as a table, and that object is modified on the primary instance using a DDL statement, the Aurora Replica connection is interrupted.

Rebooting the primary instance of an Amazon Aurora database cluster also automatically reboots the Aurora Replicas for that database cluster.

Before you create a cross region replica, turn on the `binlog_format` parameter.

When using Multi-AZ, the primary database instance switches over automatically to the standby replica if any of the following conditions occur:

- The primary database instance fails.
- An Availability Zone outage.
- The database instance server type is changed.
- The operating system of the database instance is undergoing software patching.
- A manual failover of the database instance was initiated using reboot with failover.

### Examples

The following walkthrough demonstrates how to create a replica reader.

1. Sign in to your AWS console and choose **RDS**.
2. Choose **Instance actions** and choose **Create cross-Region read replica**.
3. Enter all required details and choose **Create**.

After the replica is created, you can run read and write operations on the primary instance and read-only operations on the replica.

For more information, see [Single-master replication with Amazon Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.md"), [Replicating Amazon Aurora MySQL DB clusters](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.md"), and [Creating an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.CreateInstance.Console.ReadOnlyInstance "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md#Aurora.CreateInstance.Console.ReadOnlyInstance") in the _User Guide for Aurora_.
