# Replication with Amazon Aurora MySQL

The Aurora MySQL replication features are key to the high availability and performance of your cluster. Aurora
makes it easy to create or resize clusters with up to 15 Aurora Replicas.

All the replicas work from the same underlying data. If some database instances go offline, others remain
available to continue processing queries or to take over as the writer if needed. Aurora automatically spreads
your read-only connections across multiple database instances, helping an Aurora cluster to support
query-intensive workloads.

In the following topics, you can find information about how Aurora MySQL replication works and how to fine-tune replication settings
for best availability and performance.

###### Topics

- [Using Aurora Replicas](#AuroraMySQL.Replication.Replicas "#AuroraMySQL.Replication.Replicas")
- [Replication options for Amazon Aurora MySQL](#AuroraMySQL.Replication.Options "#AuroraMySQL.Replication.Options")
- [Performance considerations for Amazon Aurora MySQL replication](#AuroraMySQL.Replication.Performance "#AuroraMySQL.Replication.Performance")
- [Configuring replication filters with Aurora MySQL](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Monitoring Amazon Aurora MySQL replication](#AuroraMySQL.Replication.Monitoring "#AuroraMySQL.Replication.Monitoring")
- [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Replication between Aurora and MySQL or between Aurora and another Aurora DB
  cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md")

## Using Aurora Replicas

Aurora Replicas are independent endpoints in an Aurora DB cluster, best used for scaling read operations and
increasing availability. Up to 15 Aurora Replicas can be distributed across the Availability
Zones that a DB cluster spans within an AWS Region. Although the DB cluster volume is made up of multiple
copies of the data for the DB cluster, the data in the cluster volume is represented as a single, logical
volume to the primary instance and to Aurora Replicas in the DB cluster. For more information about Aurora
Replicas, see
[Aurora Replicas](Aurora.md#Aurora.Replication.Replicas "Aurora.md#Aurora.Replication.Replicas").

Aurora Replicas work well for read scaling because they are fully dedicated to read operations on your cluster
volume. Write operations are managed by the primary instance. Because the cluster volume is shared among all
instances in your Aurora MySQL DB cluster, no additional work is required to replicate a copy of the data for
each Aurora Replica. In contrast, MySQL read replicas must replay, on a single thread, all write operations
from the source DB instance to their local data store. This limitation can affect the ability of MySQL read
replicas to support large volumes of read traffic.

With Aurora MySQL, when an Aurora Replica is deleted, its instance endpoint is removed immediately, and the Aurora
Replica is removed from the reader endpoint. If there are statements running on the Aurora Replica that is
being deleted, there is a three minute grace period. Existing statements can finish gracefully during the
grace period. When the grace period ends, the Aurora Replica is shut down and deleted.

###### Important

Aurora Replicas for Aurora MySQL always use the `REPEATABLE READ` default transaction isolation
level for operations on InnoDB tables. You can use the `SET TRANSACTION ISOLATION LEVEL` command
to change the transaction level only for the primary instance of an Aurora MySQL DB cluster. This restriction
avoids user-level locks on Aurora Replicas, and allows Aurora Replicas to scale to support thousands of active
user connections while still keeping replica lag to a minimum.

###### Note

DDL statements that run on the primary instance might interrupt database connections on the associated Aurora
Replicas. If an Aurora Replica connection is actively using a database object, such as a table, and that
object is modified on the primary instance using a DDL statement, the Aurora Replica connection is
interrupted.

###### Note

The China (Ningxia) Region does not support cross-Region read replicas.

## Replication options for Amazon Aurora MySQL

You can set up replication between any of the following options:

- Two Aurora MySQL DB clusters in different AWS Regions, by creating a cross-Region read replica of an Aurora MySQL DB
  cluster.

For more information, see [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

- Two Aurora MySQL DB clusters in the same AWS Region, by using MySQL binary log (binlog) replication.

For more information, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

- An RDS for MySQL DB instance as the source and an Aurora MySQL DB cluster, by creating an Aurora read replica of an RDS for MySQL DB
  instance.

You can use this approach to bring existing and ongoing data changes into Aurora MySQL during migration to Aurora. For more
information, see [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL
DB cluster by using an Aurora read replica](AuroraMySQL.Migrating.RDSMySQL.md "AuroraMySQL.Migrating.RDSMySQL.md").

You can also use this approach to increase the scalability of read queries for your data. You do so by querying the data using
one or more DB instances within a read-only Aurora MySQL cluster. For more information, see [Scaling reads for your MySQL database with Amazon Aurora](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

- An Aurora MySQL DB cluster in one AWS Region and up to five Aurora read-only Aurora MySQL DB clusters in different Regions, by
  creating an Aurora global database.

You can use an Aurora global database to support applications with a world-wide footprint. The primary Aurora MySQL DB cluster
has a Writer instance and up to 15 Aurora Replicas. The read-only secondary Aurora MySQL DB clusters can each be made up of
as many as 16 Aurora Replicas. For more information, see [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md").

###### Note

Rebooting the primary instance of an Amazon Aurora DB cluster also automatically reboots the Aurora Replicas for that DB cluster, to
re-establish an entry point that guarantees read/write consistency across the DB cluster.

## Performance considerations for Amazon Aurora MySQL replication

The following features help you to fine-tune the performance of Aurora MySQL replication.

The replica log compression feature automatically reduces network bandwidth for replication messages. Because each message is
transmitted to all Aurora Replicas, the benefits are greater for larger clusters. This feature involves some CPU overhead on the
writer node to perform the compression. It's always enabled in Aurora MySQL version 2 and version 3.

The binlog filtering feature automatically reduces network bandwidth for replication messages. Because the Aurora Replicas
don't use the binlog information that is included in the replication messages, that data is omitted from the messages sent
to those nodes.

In Aurora MySQL version 2, you can control this feature by changing the `aurora_enable_repl_bin_log_filtering`
parameter. This parameter is on by default. Because this optimization is intended to be transparent, you might turn off this
setting only during diagnosis or troubleshooting for issues related to replication. For example, you can do so to match the
behavior of an older Aurora MySQL cluster where this feature was not available.

Binlog filtering is always enabled in Aurora MySQL version 3.

## Monitoring Amazon Aurora MySQL replication

Read scaling and high availability depend on minimal lag time. You can monitor how far an Aurora Replica is lagging behind the
primary instance of your Aurora MySQL DB cluster by monitoring the Amazon CloudWatch `AuroraReplicaLag` metric. The
`AuroraReplicaLag` metric is recorded in each Aurora Replica.

The primary DB instance also records the `AuroraReplicaLagMaximum` and `AuroraReplicaLagMinimum` Amazon CloudWatch
metrics. The `AuroraReplicaLagMaximum` metric records the maximum amount of lag between the primary DB instance and
each Aurora Replica in the DB cluster. The `AuroraReplicaLagMinimum` metric records the minimum amount of lag between
the primary DB instance and each Aurora Replica in the DB cluster.

If you need the most current value for Aurora Replica lag, you can check the `AuroraReplicaLag` metric in Amazon CloudWatch. The
Aurora Replica lag is also recorded on each Aurora Replica of your Aurora MySQL DB cluster in the
`information_schema.replica_host_status` table. For more information on this table, see [information_schema.replica_host_status](AuroraMySQL.Reference.md#AuroraMySQL.Reference.ISTables.replica_host_status "AuroraMySQL.Reference.md#AuroraMySQL.Reference.ISTables.replica_host_status").

For more information on monitoring RDS instances and CloudWatch metrics, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md "MonitoringAurora.md").
