# Monitoring Aurora PostgreSQL Limitless Database with Amazon CloudWatch

CloudWatch metrics for Aurora PostgreSQL Limitless Database are reported under the following dimensions:

- [DBShardGroup](#limitless-monitoring.cw.DBShardGroup "#limitless-monitoring.cw.DBShardGroup")
- [DBShardGroupRouterAggregation](#limitless-monitoring.cw.DBShardGroupRouterAggregate "#limitless-monitoring.cw.DBShardGroupRouterAggregate")
- [DBShardGroupInstance](#limitless-monitoring.cw.DBShardGroupInstance "#limitless-monitoring.cw.DBShardGroupInstance")
- [DBClusterIdentifier](#limitless-monitoring.cw.DBClusterIdentifier "#limitless-monitoring.cw.DBClusterIdentifier")
  For more information on CloudWatch metrics, see [Monitoring Amazon Aurora metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## DBShardGroup metrics

To see `DBShardGroup` metrics for Aurora PostgreSQL Limitless Database in the CloudWatch console, choose **RDS**, and then
choose **DBShardGroup**.

You can track the following CloudWatch metrics:

- `DBShardGroupACUUtilization` – Aurora capacity unit (ACU) usage as a percentage
  calculated from `DBShardGroupCapacity` divided by `DBShardGroupMaxACU`.
- `DBShardGroupCapacity` – Number of ACUs consumed by the writer instances of the DB shard group.
- `DBShardGroupComputeRedundancyCapacity` – Number of ACUs consumed by the standby instances of DB shard group.
- `DBShardGroupMaxACU` – Maximum number of ACUs configured for the DB shard
  group.
- `DBShardGroupMinACU` – Minimum number of ACUs required by the DB shard group.

The `DBShardGroupIdentifier` dimension key is available for aggregating the `DBShardGroup`
metrics.

## DBShardGroupRouterAggregation metrics

To see `DBShardGroupRouterAggregation` metrics for Aurora PostgreSQL Limitless Database in the CloudWatch console, choose
**RDS**, and then choose **DBShardGroupRouterAggregation**.

You can track the following CloudWatch metrics:

- `CommitThroughput` – The average number of commit operations per second across all of the router
  nodes in the DB shard group.
- `DatabaseConnections` – The sum of all connections across all of the router nodes in the DB
  shard group.

## DBShardGroupInstance metrics

A _DBShardGroupInstance_ is the individual DB instance within each shard or router subcluster.

To see `DBShardGroupInstance` metrics for Aurora PostgreSQL Limitless Database in the CloudWatch console, choose **RDS**, and
then choose **DBShardGroupInstance**.

You can track the following CloudWatch metrics:

- `ACUUtilization` – The percentage calculated as the `ServerlessDatabaseCapacity`
  metric divided by the maximum assigned ACU value of the subcluster.
- `AuroraReplicaLag` - For compute redundancy enabled Limitless clusters, this is the amount of
  lag when replicating updates from the primary instance in the subcluster.
- `AuroraReplicaLagMaximum` – For compute redundancy enabled Limitless clusters,
  this is the maximum amount of lag when replicating updates from the primary instance in the subcluster.
  When read replicas are deleted or renamed, there might be a temporary spike in replication lag as the old resource recycles.
  Use this metric to find if a failover occurred due to high replication lag on one of the it's readers.
- `AuroraReplicaLagMinimum` – For compute redundancy enabled Limitless clusters,
  this is the minimum amount of lag when replicating updates from the primary instance in the subcluster.
- `BufferCacheHitRatio` – The percentage of data and indexes served from an instance’s memory
  cache (as opposed to the storage volume).
- `CommitLatency` – The average duration for the engine and storage to complete the commit
  operations for a particular node (router or shard).
- `CommitThroughput` – The average number of commit operations per second.
- `CPUUtilization` – CPU usage as a percentage of the maximum assigned
  ACU value of the subcluster.
- `FreeableMemory` – The amount of unused memory that's available when the shard group is scaled to its maximum capacity.
  This is determined by the assigned ACUs of the shard group. For every ACU the current capacity is below the maximum capacity,
  this value increases by approximately 2 GiB. Thus, this metric doesn't approach zero until the DB shard group is scaled up to the maximum limit.
- `MaximumUsedTransactionIDs` – The age of the oldest unvacuumed transaction ID, in transactions. If this value
  reaches 2,146,483,648 (2^31 - 1,000,000), the database is forced into read-only mode, to avoid transaction ID wraparound. For more
  information, see [Preventing
  transaction ID wraparound failures](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND") in the PostgreSQL documentation.
- `NetworkReceiveThroughput` – The amount of network throughput received from clients by each
  instance in the DB shard group. This throughput doesn't include network traffic between instances in the DB shard
  group and the cluster volume.
- `NetworkThroughput` – The aggregated network throughput (both transmitted and received) between clients and routers,
  and routers and shards in the DB shard group. This throughput doesn't include network traffic between instances in the DB shard group
  and the cluster volume.
- `NetworkTransmitThroughput` – The amount of network throughput sent to clients by each instance
  in the DB shard group. This throughput doesn't include network traffic between instances in the DB shard group and
  the cluster volume.
- `ReadIOPS` – The average number of disk read input/output operations per second (IOPS).
- `ReadLatency` – The average amount time taken per disk read input/output (I/O) operation.
- `ReadThroughput` – The average number of bytes read from disk per second.
- `ServerlessDatabaseCapacity` – The current capacity of the DB shard or router subcluster within the DB shard group.
- `StorageNetworkReceiveThroughput` – The amount of network throughput received from the Aurora
  storage subsystem by each instance in the DB shard group.
- `StorageNetworkThroughput` – The aggregated network throughput both transmitted to and received
  from the Aurora storage subsystem by each instance in the DB shard group.
- `StorageNetworkTransmitThroughput` – The amount of network throughput sent to the Aurora storage
  subsystem by each instance in the DB shard group.
- `SwapUsage` – The amount of swap space used by the DB shard group.
- `TempStorageIOPS` – The average number of I/O operations performed on local storage attached to
  the DB instance. It includes both read and write I/O operations.

`TempStorageIOPS` can be used with `TempStorageThroughput` to diagnose the rare cases where
network activity for transfers between your DB instances and local storage devices is responsible for unexpected
capacity increases.

- `TempStorageThroughput` – The amount of data transferred to and from local storage associated
  with either a router or a shard.
- `WriteIOPS` – The average number of disk write IOPS.
- `WriteLatency` – The average amount time taken per disk write I/O operation.
- `WriteThroughput` – The average number of bytes written to disk per second.

The following dimension keys are available for aggregating the `DBShardGroupInstance` metrics:

- `DBClusterIdentifier` – The Aurora PostgreSQL DB cluster.
- `DBShardGroupIdentifier` – The DB shard group to which the instance belongs.
- `DBShardGroupSubClusterType` – The node type, either `Distributed Transaction Router`
  (router) or `Data Access Shard` (shard).
- `DBShardGroupSubClusterIdentifier` – The name of the router or shard to which the instance
  belongs.

The following are examples of aggregating CloudWatch metrics:

- Total `CPUUtilization` of all instances that belong to a particular shard or router in a DB shard
  group.
- Total `CPUUtilization` of all instances in a DB shard group.

## DBClusterIdentifier metrics

To see `DBClusterIdentifier` metrics for Aurora PostgreSQL Limitless Database in the CloudWatch console, choose **RDS**, and
then choose **DBClusterIdentifier**.

When you use Aurora PostgreSQL Limitless Database, you might have more input/output (I/O) operations than you would for an Aurora DB cluster. You can
track the following CloudWatch metrics for your Limitless Database cluster:

- `VolumeReadIops` – The number of billed read I/O operations from a cluster volume, reported at
  5-minute intervals.
- `VolumeWriteIops` – The number of write disk I/O operations to the cluster volume, reported at
  5-minute intervals.

Aurora PostgreSQL Limitless Database uses the Aurora I/O-Optimized cluster storage configuration. With Aurora I/O-Optimized, you pay a single monthly price for all I/O operations, rather than
paying for every one million I/O requests. For more information, see [Storage configurations for Amazon Aurora DB
clusters](Aurora.Overview.md#aurora-storage-type "Aurora.Overview.md#aurora-storage-type").

You might also use more storage than you would for an Aurora DB cluster. You can track the following CloudWatch metrics for
storage:

- `BackupRetentionPeriodStorageUsed` – The total billed continuous backup storage usage of your
  Aurora PostgreSQL Limitless Database cluster.
- `SnapshotStorageUsed` – The total billed snapshot storage usage of your Aurora PostgreSQL Limitless Database cluster.
- `TotalBackupStorageBilled` – The sum of your costs for automated backup retention and DB cluster
  snapshots.

For more information on backup storage costs, see [Understanding Amazon Aurora backup storage usage](aurora-storage-backup.md "aurora-storage-backup.md").

- `VolumeBytesUsed` – The amount of storage used by your Aurora PostgreSQL Limitless Database cluster, reported at 5-minute
  intervals.
