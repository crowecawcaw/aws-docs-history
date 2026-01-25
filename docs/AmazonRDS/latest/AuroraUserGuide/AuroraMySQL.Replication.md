# Replicating Amazon Aurora MySQL DB clusters across AWS Regions

You can create an Amazon Aurora MySQL DB cluster as a read replica in a different AWS Region than the source DB
cluster. Taking this approach can improve your disaster recovery capabilities, let you scale read operations
into an AWS Region that is closer to your users, and make it easier to migrate from one AWS Region to
another.

You can create read replicas of both encrypted and unencrypted DB clusters. The read replica must be encrypted
if the source DB cluster is encrypted.

For each source DB cluster, you can have up to five cross-Region DB clusters that are read replicas.

###### Note

As an alternative to cross-Region read replicas, you can scale read operations with
minimal lag time by using an Aurora global database. An Aurora global database has a
primary Aurora DB cluster in one AWS Region and up to 10 secondary read-only DB
clusters in different Regions. Each secondary DB cluster can include up to 16
(rather than 15) Aurora Replicas. Replication from the primary DB
cluster to all secondaries is handled by the Aurora storage layer rather than by the
database engine, so lag time for replicating changes is minimal—typically,
less than 1 second. Keeping the database engine out of the replication process means
that the database engine is dedicated to processing workloads. It also means that
you don't need to configure or manage the Aurora MySQL binlog (binary logging)
replication. To learn more, see [Using Amazon Aurora Global Database](aurora-global-database.md "aurora-global-database.md").

When you create an Aurora MySQL DB cluster read replica in another AWS Region, you should be aware of the
following:

- Both your source DB cluster and your cross-Region read replica DB cluster can have up to 15
  Aurora Replicas, along with the primary instance for the DB cluster. By using this functionality, you can
  scale read operations for both your source AWS Region and your replication target AWS Region.
- In a cross-Region scenario, there is more lag time between the source DB cluster and the read replica due
  to the longer network channels between AWS Regions.
- Data transferred for cross-Region replication incurs Amazon RDS data transfer charges. The following
  cross-Region replication actions generate charges for the data transferred out of the source AWS Region:
  - When you create the read replica, Amazon RDS takes a snapshot of the source cluster and transfers the
    snapshot to the AWS Region that holds the read replica.
  - For each data modification made in the source databases, Amazon RDS transfers data from the source region
    to the AWS Region that holds the read replica.

For more information about Amazon RDS data transfer pricing, see
[Amazon Aurora pricing](http://aws.amazon.com/rds/aurora/pricing/ "http://aws.amazon.com/rds/aurora/pricing/").

- You can run multiple concurrent create or delete actions for read replicas that reference the same source
  DB cluster. However, you must stay within the limit of five read replicas for each source DB cluster.
- For replication to operate effectively, each read replica should have the same amount of compute and
  storage resources as the source DB cluster. If you scale the source DB cluster, you should also scale the
  read replicas.

###### Topics

- [Before you begin](#AuroraMySQL.Replication.CrossRegion.Prerequisites "#AuroraMySQL.Replication.CrossRegion.Prerequisites")
- [Creating a cross-Region read replica DB cluster for Aurora MySQL](AuroraMySQL.Replication.CrossRegion.md "AuroraMySQL.Replication.CrossRegion.md")
- [Promoting a read replica to a DB cluster for Aurora MySQL](AuroraMySQL.Replication.CrossRegion.md "AuroraMySQL.Replication.CrossRegion.md")
- [Troubleshooting cross-Region replicas for Amazon Aurora MySQL](AuroraMySQL.Replication.CrossRegion.md "AuroraMySQL.Replication.CrossRegion.md")

## Before you begin

Before you can create an Aurora MySQL DB cluster that is a cross-Region read replica, you must turn on binary
logging on your source Aurora MySQL DB cluster. Cross-region replication for Aurora MySQL uses MySQL binary
replication to replay changes on the cross-Region read replica DB cluster.

To turn on binary logging on an Aurora MySQL DB cluster, update the
`binlog_format` parameter for your source DB cluster. The
`binlog_format` parameter is a cluster-level parameter that is in the
default cluster parameter group. If your DB cluster uses the default DB cluster
parameter group, create a new DB cluster parameter group to modify
`binlog_format` settings. We recommend that you set the
`binlog_format` to `MIXED`. However, you can also set
`binlog_format` to `ROW` or `STATEMENT` if you
need a specific binlog format. Reboot your Aurora DB cluster for the change to take
effect.

For more information about using binary logging with Aurora MySQL, see
[Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").
For more information about modifying Aurora MySQL configuration parameters, see
[Amazon Aurora DB cluster and DB instance
parameters](USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups "USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups")
and
[Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
