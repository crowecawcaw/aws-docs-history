# Replication with Amazon Aurora PostgreSQL

Following, you can find information about replication with Amazon Aurora PostgreSQL, including
how to monitor and use logical replication.

###### Topics

- [Using Aurora Replicas](#AuroraPostgreSQL.Replication.Replicas "#AuroraPostgreSQL.Replication.Replicas")
- [Improving the read
  availability of Aurora Replicas](#AuroraPostgreSQL.Replication.Replicas.SRO "#AuroraPostgreSQL.Replication.Replicas.SRO")
- [Monitoring Aurora PostgreSQL
  replication](#AuroraPostgreSQL.Replication.Monitoring "#AuroraPostgreSQL.Replication.Monitoring")
- [Overview of PostgreSQL logical
  replication with Aurora](AuroraPostgreSQL.Replication.md "AuroraPostgreSQL.Replication.md")
- [Setting up logical
  replication for your Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md")
- [Turning off logical
  replication](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md")
- [Monitoring the
  write-through cache and logical slots for Aurora PostgreSQL logical replication](AuroraPostgreSQL.Replication.md "AuroraPostgreSQL.Replication.md")
- [Example: Using
  logical replication with Aurora PostgreSQL DB clusters](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md")
- [Example: Logical
  replication using Aurora PostgreSQL and AWS Database Migration Service](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md")
- [Configuring IAM
  authentication for logical replication connections](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md")

## Using Aurora Replicas

An _Aurora Replica_ is an independent endpoint in an Aurora DB
cluster, best used for scaling read operations and increasing availability. An Aurora DB
cluster can include up to 15 Aurora Replicas located throughout the
Availability Zones of the Aurora DB cluster's AWS Region.

The DB cluster volume is made up of multiple copies of the data for the DB cluster.
However, the data in the cluster volume is represented as a single, logical volume to
the primary writer DB instance and to Aurora Replicas in the DB cluster. For more
information about Aurora Replicas, see [Aurora Replicas](Aurora.md#Aurora.Replication.Replicas "Aurora.md#Aurora.Replication.Replicas").

Aurora Replicas work well for read scaling because they're fully dedicated to read
operations on your cluster volume. The writer DB instance manages write operations. The
cluster volume is shared among all instances in your Aurora PostgreSQL DB cluster. Thus, no
extra work is needed to replicate a copy of the data for each Aurora Replica.

With Aurora PostgreSQL, when an Aurora Replica is deleted, its instance endpoint is removed
immediately, and the Aurora Replica is removed from the reader endpoint. If there are
statements running on the Aurora Replica that is being deleted, there is a three minute
grace period. Existing statements can finish gracefully during the grace period. When
the grace period ends, the Aurora Replica is shut down and deleted.

Aurora PostgreSQL DB clusters support Aurora Replicas in different AWS Regions, using
Aurora global database. For more information, see [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md").

###### Note

With the read availability feature, if you want to reboot the Aurora Replicas in
the DB cluster, you have to perform it manually. For the DB clusters created prior
to this feature rebooting the writer DB instance automatically reboots the Aurora
Replicas. The automatic reboot re-establishes an entry point that guarantees
read/write consistency across the DB cluster.

## Improving the read

availability of Aurora Replicas

Aurora PostgreSQL improves the read availability in the DB cluster by continuously serving
the read requests when the writer DB instance restarts or when the Aurora Replica is
unable to keep up with the write traffic.

The read availability feature is available by default on the following versions of
Aurora PostgreSQL:

- 16.1 and all higher versions
- 15.2 and higher 15 versions
- 14.7 and higher 14 versions
- 13.10 and higher 13 versions
- 12.14 and higher 12 versions

The read availability feature is supported by Aurora global database in the following
versions:

- 16.1 and all higher versions
- 15.4 and higher 15 versions
- 14.9 and higher 14 versions
- 13.12 and higher 13 versions
- 12.16 and higher 12 versions

To use the read availability feature for a DB cluster created on one of these versions
prior to this launch, restart the writer instance of the DB cluster.

When you modify static parameters of your Aurora PostgreSQL DB cluster, you must restart
the writer instance so that the parameter changes take effect. For example, you must
restart the writer instance when you set the value of `shared_buffers`. With
the read availability feature of Aurora Replicas, the DB cluster maintains improved
availability, reducing the impact on it when the writer instance restarts. The reader
instances don't restart and continue to respond to the read requests. To apply static
parameter changes, reboot each individual reader instance.

An Aurora PostgreSQL DB cluster's Aurora Replica can recover from replication errors
such as writer restarts, failover, slow replication, and network issues by quickly
recovering to in-memory database state after it reconnects with the writer. This
approach allows Aurora Replica instances to reach consistency with the latest storage
updates while the client database is still available.

The in-progress transactions that conflict with replication recovery might receive an
error but the client can retry these transactions, after the readers catch up with the
writer.

### Monitoring Aurora

Replicas

You can monitor the Aurora Replicas when recovering from a writer disconnect. Use
the metrics below to check for the latest information about the reader instance and
to track in-process read-only transactions.

- The `aurora_replica_status` function is updated to return the
  most up-to-date information for the reader instance when it is still
  connected. The last update time stamp in `aurora_replica_status`
  is always empty for the row corresponding to the DB instance that the query
  is executed on. This indicates that the reader instance has the latest
  data.
- When the Aurora replica disconnects from the writer instance and
  reconnects back, the following database event is emitted:

`Read replica has been disconnected from the writer instance and
 reconnected.`

- When a read-only query is canceled due to a recovery conflict, you might
  see one or more of the following error messages in the database error
  log:

`Canceling statement due to conflict with recovery`.

`User query may not have access to page data to replica
 disconnect.`

`User query might have tried to access a file that no longer
 exists.`

`When the replica reconnects, you will be able to repeat your
 command.`

### Limitations

The following limitations apply to Aurora Replicas with the read availability
feature:

- Aurora Replicas of secondary DB cluster can restart if the data can't be
  streamed from the writer instance during replication recovery.
- Aurora Replicas don't support online replication recovery if one is
  already in progress and will restart.
- Aurora Replicas will restart when your DB instance is nearing the
  transaction ID wraparound. For more information on transaction ID
  wraparound, see [Preventing Transaction ID Wraparound
  Failures](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND                     ").
- Aurora Replicas can restart when the replication process is blocked under
  certain circumstances.

## Monitoring Aurora PostgreSQL

replication

Read scaling and high availability depend on minimal lag time. You can monitor how far
an Aurora Replica is lagging behind the writer DB instance of your Aurora PostgreSQL DB
cluster by monitoring the Amazon CloudWatch `ReplicaLag` metric. Because Aurora
Replicas read from the same cluster volume as the writer DB instance, the
`ReplicaLag` metric has a different meaning for an Aurora PostgreSQL DB
cluster. The `ReplicaLag` metric for an Aurora Replica indicates the lag for
the page cache of the Aurora Replica compared to that of the writer DB instance.

For more information on monitoring RDS instances and CloudWatch metrics, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md "MonitoringAurora.md").
