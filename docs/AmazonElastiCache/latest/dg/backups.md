# Snapshot and restore

Amazon ElastiCache caches running Valkey, Redis OSS, or Serverless Memcached can back up their data by creating a snapshot.
You can use the backup to restore
a cache or seed data to a new cache. The backup consists of the cache’s metadata, along with all of the data in the cache.
All backups are written to Amazon Simple Storage Service (Amazon S3), which provides
durable storage. At any time, you can restore your data by creating a new Valkey, Redis OSS, or Serverless Memcached cache and
populating it with data from a backup. With ElastiCache, you can manage backups using the
AWS Management Console, the AWS Command Line Interface (AWS CLI), and the ElastiCache API.

If you plan to delete a cache and it's important to preserve the data, you can
take an extra precaution. To do this, create a manual backup first, verify that its
status is _available_, and then delete the cache. Doing this makes
sure that if the backup fails, you still have the cache data available. You can retry
making a backup, following the best practices outlined preceding.

###### Topics

- [Backup constraints](#backups-constraints "#backups-constraints")
- [Performance impact of backups of node-based clusters](#backups-performance "#backups-performance")
- [Scheduling automatic backups](backups-automatic.md "backups-automatic.md")
- [Taking manual backups](backups-manual.md "backups-manual.md")
- [Creating a final backup](backups-final.md "backups-final.md")
- [Describing backups](backups-describing.md "backups-describing.md")
- [Copying backups](backups-copying.md "backups-copying.md")
- [Exporting a backup](backups-exporting.md "backups-exporting.md")
- [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md")
- [Deleting a backup](backups-deleting.md "backups-deleting.md")
- [Tagging backups](backups-tagging.md "backups-tagging.md")
- [Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md "backups-seeding-redis.md")

## Backup constraints

Consider the following constraints when planning or making backups:

- Backup and restore are supported only for caches running on
  Valkey, Redis OSS or Serverless Memcached.
- For Valkey or Redis OSS (cluster mode disabled) clusters, backup and restore aren't supported on
  `cache.t1.micro` nodes. All other cache node types are
  supported.
- For Valkey or Redis OSS (cluster mode enabled) clusters, backup and restore are supported for all node
  types.
- During any contiguous 24-hour period, you can create no more than 24 manual backups per serverless cache.
  For Valkey and Redis OSS node-based clusters, you can create no more than 20 manual backups per node in the cluster.
- Valkey or Redis OSS (cluster mode enabled) only supports taking backups on the cluster level (for the API
  or CLI, the replication group level). Valkey or Redis OSS (cluster mode enabled) doesn't support taking
  backups at the shard level (for the API or CLI, the node group level).
- During the backup process, you can't run any other API or CLI operations on
  serverless cache. You can run API or CLI operations on a node-based cluster during backup.
- If you are using Valkey or Redis OSS caches with data tiering, you cannot export a backup to Amazon S3.
- You can restore a backup of a cluster using the r6gd node type only to clusters using the r6gd node type.

## Performance impact of backups of node-based clusters

Backups on serverless caches are transparent to the application with no performance impact.
However, when creating backups for node-based clusters, there can be some performance impact
depending on the available reserved memory. Backups for node-based clusters are not available with ElastiCache for Memcached
but are available with ElastiCache for Redis OSS.

The following are guidelines for improving backup performance for node-based clusters.

- Set the `reserved-memory-percent` parameter – To mitigate
  excessive paging, we recommend that you set the
  _reserved-memory-percent_ parameter. This parameter
  prevents Valkey and Redis OSS from consuming all of the node's available memory, and can
  help reduce the amount of paging. You might also see performance
  improvements by simply using a larger node. For more information about the
  _reserved-memory_ and
  _reserved-memory-percent_ parameters, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").
- Create backups from a read replica – If you are running Valkey or Redis OSS in a
  node group with more than one node, you can take a backup from the primary
  node or one of the read replicas. Because of the system resources required
  during BGSAVE, we recommend that you create backups from one of the read
  replicas. While the backup is being created from the replica, the primary
  node remains unaffected by BGSAVE resource requirements. The primary node
  can continue serving requests without slowing down.

To do this, see [Creating a manual backup (Console)](backups-manual.md#backups-manual-CON "backups-manual.md#backups-manual-CON") and in the **Cluster Name** field in the
**Create Backup** window, choose a replica instead of the default primary node.

If you delete a replication group and request a final backup, ElastiCache always takes
the backup from the primary node. This ensures that you capture the very latest Valkey or Redis OSS data, before the replication group is deleted.
