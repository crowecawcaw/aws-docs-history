# Promoting a read replica to be a standalone

DB instance

You can promote a read replica into a standalone DB instance. If a source DB instance has several read
replicas, promoting one of the read replicas to a DB instance has no effect on the other
replicas.

When you promote a read replica, RDS reboots the DB instance before making it available. The
promotion process can take several minutes or longer to complete, depending on the size of
the read replica.

![Promoting a read replica](images/read-replica-promote.png)

## Use cases for promoting a read

replica

You might want to promote a read replica to a standalone DB instance for any of the
following reasons:

- **Implementing failure recovery** – You
  can use read replica promotion as a data recovery scheme if the primary DB instance
  fails. This approach complements synchronous replication, automatic failure
  detection, and failover.

If you are aware of the ramifications and limitations of asynchronous
replication and you still want to use read replica promotion for data recovery,
you can. To do this, first create a read replica and then monitor the primary
DB instance for failures. In the event of a failure, do the following:

    1. Promote the read replica.
    2. Direct database traffic to the promoted DB instance.
    3. Create a replacement read replica with the promoted DB instance as its
     source.

- **Upgrading storage configuration** – If
  your source DB instance isn't on the preferred storage configuration, you can create a
  read replica of the instance and upgrade the storage file system configuration.
  This option migrates the file system of the read replica to the preferred
  configuration. You can then promote the read replica to a standalone
  instance.

You can use this option to overcome the scaling limitations on storage and
file size for older 32-bit file systems. For more information, see [Upgrading the storage file system for a DB
instance](USER_PIOPS.md "USER_PIOPS.md").

This option is only available if your source DB instance is _not_
on the latest storage configuration, or if you're modifying the DB instance class
within the same request.

- **Sharding** – Sharding embodies the
  "share-nothing" architecture and essentially involves breaking a large database
  into several smaller databases. One common way to split a database is splitting
  tables that are not joined in the same query onto different hosts. Another
  method is duplicating a table across multiple hosts and then using a hashing
  algorithm to determine which host receives a given update. You can create read
  replicas corresponding to each of your shards (smaller databases) and promote
  them when you decide to convert them into standalone shards. You can then carve
  out the key space (if you are splitting rows) or distribution of tables for each
  of the shards depending on your requirements.
- **Performing DDL operations (MySQL and MariaDB
  only)** – DDL operations, such as creating or rebuilding
  indexes, can take time and impose a significant performance penalty on your DB
  instance. You can perform these operations on a MySQL or MariaDB read replica
  once the read replica is in sync with its primary DB instance. Then you can promote
  the read replica and direct your applications to use the promoted
  instance.

###### Note

If your read replica is an RDS for Oracle DB instance, you can perform a
_switchover_ instead of a promotion. In a switchover, the
source DB instance becomes the new replica, and the replica becomes the new source DB instance.
For more information, see [Performing an Oracle Data Guard switchover](oracle-replication-switchover.md "oracle-replication-switchover.md").

## Characteristics of a promoted

read replica

After you promote the read replica, it ceases to function as a read replica and
becomes a standalone DB instance. The new standalone DB instance has the following
characteristics:

- The standalone DB instance retains the option group and the parameter group of the
  pre-promotion read replica.
- You can create read replicas from the standalone DB instance and perform
  point-in-time restore operations.
- You can't use the DB instance as a replication target because it is no longer a read
  replica.

## Prerequisites for promoting a read

replica

Before you promote a read replica, do the following:

- Review your backup strategy:
  - We recommend that you enable backups and complete at least one backup.
    Backup duration is a function of the number of changes to the database
    since the previous backup.
  - If you have enabled backups on your read replica, configure the
    automated backup window so that daily backups don't interfere with
    read replica promotion.
  - Make sure that your read replica doesn't have the
    `backing-up` status. You can't promote a read replica
    when it is in this state.

- Stop any transactions from being written to the primary DB instance, and then wait
  for RDS to apply all updates to the read replica.

Database updates occur on the read replica after they have occurred on the
primary DB instance. Replication lag can vary significantly. Use the [`Replica Lag`](http://aws.amazon.com/rds/faqs/#105 "http://aws.amazon.com/rds/faqs/#105")
metric to determine when all updates have been made to the read replica.

- (MySQL and MariaDB only) To make changes to a MySQL or MariaDB read replica
  before you promote it, set the `read_only` parameter to
  `0` in the DB parameter group for the read replica. You can then
  perform all needed DDL operations, such as creating indexes, on the read
  replica. Actions taken on the read replica don't affect the performance of the
  primary DB instance.

## Promoting a read replica: basic

steps

The following steps show the general process for promoting a read replica to a DB
instance:

1. Promote the read replica by using the **Promote** option on
   the Amazon RDS console, the AWS CLI command [`promote-read-replica`](../../../cli/latest/reference/rds/promote-read-replica.md "../../../cli/latest/reference/rds/promote-read-replica.md"), or the [`PromoteReadReplica`](../APIReference/API_PromoteReadReplica.md "../APIReference/API_PromoteReadReplica.md") Amazon RDS API operation.

###### Note

The promotion process takes a few minutes to complete. When you promote a
read replica, RDS stops replication and reboots the read replica. When the
reboot is complete, the read replica is available as a new DB instance. 2. (Optional) Modify the new DB instance to be a Multi-AZ deployment. For more
information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md") and [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

###### To promote a read replica to a standalone DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the Amazon RDS console, choose **Databases**.

The **Databases** pane appears. Each read replica
shows **Replica** in the **Role**
column. 3. Choose the read replica that you want to promote. 4. For **Actions**, choose
**Promote**. 5. On the **Promote Read Replica** page, enter the
backup retention period and the backup window for the newly promoted DB
instance. 6. When the settings are as you want them, choose
**Continue**. 7. On the acknowledgment page, choose **Promote Read
Replica**.
To promote a read replica to a standalone DB instance, use the AWS CLI [`promote-read-replica`](../../../cli/latest/reference/rds/promote-read-replica.md "../../../cli/latest/reference/rds/promote-read-replica.md") command.

###### Example

For Linux, macOS, or Unix:

```
aws rds promote-read-replica \
    --db-instance-identifier `myreadreplica`
```

For Windows:

```
aws rds promote-read-replica ^
    --db-instance-identifier `myreadreplica`
```

To promote a read replica to a standalone DB instance, call the Amazon RDS API [`PromoteReadReplica`](../APIReference/API_PromoteReadReplica.md "../APIReference/API_PromoteReadReplica.md") operation with the required
parameter `DBInstanceIdentifier`.
