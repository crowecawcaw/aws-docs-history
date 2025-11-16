# Replication with Amazon Aurora

There are several replication options with Aurora. Each Aurora DB cluster has built-in
replication between multiple DB instances in the same cluster. You can also set up
replication with your Aurora cluster as the source or the target. When you replicate data
into or out of an Aurora cluster, you can choose between built-in features such as Aurora
global databases or the traditional replication mechanisms for the MySQL or PostgreSQL DB
engines. You can choose the appropriate options based on which one provides the right
combination of high availability, convenience, and performance for your needs. The following
sections explain how and when to choose each technique.

###### Topics

- [Aurora Replicas](#Aurora.Replication.Replicas "#Aurora.Replication.Replicas")
- [Replication with Aurora MySQL](#Aurora.Replication.AuroraMySQL "#Aurora.Replication.AuroraMySQL")
- [Replication with
  Aurora PostgreSQL](#Aurora.Replication.AuroraPostgreSQL "#Aurora.Replication.AuroraPostgreSQL")

## Aurora Replicas

When you create a second, third, and so on DB instance in an Aurora provisioned DB
cluster, Aurora automatically sets up replication from the writer DB instance to all the
other DB instances. These other DB instances are read-only and are known as Aurora
Replicas. We also refer to them as reader instances when discussing the ways that you
can combine writer and reader DB instances within a cluster.

Aurora Replicas have two main purposes. You can issue queries to them to scale the read
operations for your application. You typically do so by connecting to the reader
endpoint of the cluster. That way, Aurora can spread the load for read-only connections
across as many Aurora Replicas as you have in the cluster. Aurora Replicas also help to
increase availability. If the writer instance in a cluster becomes unavailable, Aurora
automatically promotes one of the reader instances to take its place as the new
writer.

An Aurora DB cluster can contain up to 15 Aurora Replicas. The Aurora
Replicas can be distributed across the Availability Zones that a DB cluster spans within
an AWS Region.

The data in your DB cluster has its own high availability and reliability features,
independent of the DB instances in the cluster. If you aren't familiar with Aurora
storage features, see [Overview of Amazon Aurora storage](Aurora.Overview.md#Aurora.Overview.Storage "Aurora.Overview.md#Aurora.Overview.Storage"). The DB cluster volume is physically made
up of multiple copies of the data for the DB cluster. The primary instance and the Aurora
Replicas in the DB cluster all see the data in the cluster volume as a single logical
volume.

As a result, all Aurora Replicas return the same data for query results with minimal
replica lag. This lag is usually much less than 100 milliseconds after the primary
instance has written an update. Replica lag varies depending on the rate of database
change. That is, during periods where a large amount of write operations occur for the
database, you might see an increase in replica lag.

###### Note

Aurora Replica restarts automatically, when it loses communication with the writer
DB instance for more than 60 seconds in the following Aurora PostgreSQL versions:

- 14.6 and older versions
- 13.9 and older versions
- 12.13 and older versions
- All Aurora PostgreSQL 11 versions
  With the read availability feature, the Aurora Replicas don't restart
  automatically. For more information on the read availability feature and the
  versions where it is applicable, see [Improving the read
  availability of Aurora Replicas](AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Replicas.SRO "AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Replicas.SRO").

Aurora Replicas work well for read scaling because they are fully dedicated to read
operations on your cluster volume. Write operations are managed by the primary instance.
Because the cluster volume is shared among all DB instances in your DB cluster, minimal
additional work is required to replicate a copy of the data for each Aurora
Replica.

To increase availability, you can use Aurora Replicas as failover targets. That is, if
the primary instance fails, an Aurora Replica is promoted to the primary instance. There
is a brief interruption during which read and write requests made to the primary
instance fail with an exception.

Promoting an Aurora Replica by failover is much faster than recreating the primary
instance. If your Aurora DB cluster doesn't include any Aurora Replicas, then your DB
cluster isn't available while your DB instance is recovering from the failure.

When failover happens, some of the Aurora Replicas might be rebooted, depending on the
DB engine version. For example, in Aurora MySQL, Aurora restarts only the writer DB
instance and the failover target during a failover. For more information about the
rebooting behavior of different Aurora DB engine versions, see [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](USER_RebootCluster.md "USER_RebootCluster.md"). For information
about what happens to page caches when rebooting or failover, see [Survivable page cache](Aurora.Overview.md#Aurora.Overview.CacheWarming "Aurora.Overview.md#Aurora.Overview.CacheWarming").

For high-availability scenarios, we recommend that you create one or more Aurora
Replicas. These should be of the same DB instance class as the primary instance and in
different Availability Zones for your Aurora DB cluster. For more information about Aurora
Replicas as failover targets, see [Fault tolerance for an Aurora DB
cluster](Concepts.md#Aurora.Managing.FaultTolerance "Concepts.md#Aurora.Managing.FaultTolerance").

You can't create an encrypted Aurora Replica for an unencrypted Aurora DB cluster.
You can't create an unencrypted Aurora Replica for an encrypted Aurora DB cluster.

###### Tip

You can use Aurora Replicas within an Aurora cluster as your only form of
replication to keep your data highly available. You can also combine the built-in
Aurora replication with the other types of replication. Doing so can help to provide
an extra level of high availability and geographic distribution of your data.

For details on how to create an Aurora Replica, see [Adding Aurora Replicas to a DB cluster](aurora-replicas-adding.md "aurora-replicas-adding.md").

## Replication with Aurora MySQL

In addition to Aurora Replicas, you have the following options for replication with
Aurora MySQL:

- Aurora MySQL DB clusters in different AWS Regions.
  - You can replicate data across multiple Regions by using an Aurora
    global database. For details, see [High availability across AWS
    Regions with Aurora global databases](Concepts.md#Concepts.AuroraHighAvailability.GlobalDB "Concepts.md#Concepts.AuroraHighAvailability.GlobalDB")
  - You can create an Aurora read replica of an Aurora MySQL DB cluster in a
    different AWS Region, by using MySQL binary log (binlog) replication.
    Each cluster can have up to five read replicas created this way, each in
    a different Region.

- Two Aurora MySQL DB clusters in the same Region, by using MySQL binary log
  (binlog) replication.
- An RDS for MySQL DB instance as the source of data and an Aurora MySQL DB
  cluster, by creating an Aurora read replica of an RDS for MySQL DB instance.
  Typically, you use this approach for migration to Aurora MySQL, rather than for
  ongoing replication.

For more information about replication with Aurora MySQL, see [Replication with Amazon Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md").

## Replication with

Aurora PostgreSQL

In addition to Aurora Replicas, you have the following options for replication with
Aurora PostgreSQL:

- An Aurora primary DB cluster in one Region and up to 10 read-only secondary
  DB clusters in different Regions by using an Aurora global database.
  Aurora PostgreSQL doesn't support cross-Region Aurora Replicas. However, you can
  use Aurora global database to scale your Aurora PostgreSQL DB cluster's read
  capabilities to more than one AWS Region and to meet availability goals. For
  more information, see [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md").
- Two Aurora PostgreSQL DB clusters in the same Region, by using PostgreSQL's
  logical replication feature.
- An RDS for PostgreSQL DB instance as the source of data and an Aurora PostgreSQL DB
  cluster, by creating an Aurora read replica of an RDS for PostgreSQL DB instance.
  Typically, you use this approach for migration to Aurora PostgreSQL, rather than for
  ongoing replication.

For more information about replication with Aurora PostgreSQL, see [Replication with Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
