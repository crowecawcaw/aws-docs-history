# Upgrade considerations when working with node-based clusters

###### Note

The following considerations only apply when upgrading node-based clusters. They do not apply to ElastiCache Serverless.

**Valkey and Redis OSS considerations**

When upgrading a node-based Valkey or Redis OSS cluster, consider the following.

- Engine version management is designed so that you can have as much control as possible over
  how patching occurs. However, ElastiCache reserves the right to patch your cluster
  on your behalf in the unlikely event of a critical security vulnerability in
  the system or cache software.
- Beginning with ElastiCache version 7.2 for Valkey and ElastiCache version 6.0 for Redis OSS, ElastiCache will offer a single version for each minor release, rather than offering multiple patch versions.
- Starting with Redis OSS engine version 5.0.6, you can upgrade your cluster version with minimal downtime.
  The cluster is available for reads during the entire upgrade and is available for writes for most of the upgrade duration, except during the failover operation which lasts a few seconds.
- You can also upgrade your ElastiCache clusters with versions earlier than 5.0.6. The process involved is the same but may incur longer failover time during DNS propagation (30s-1m).
- Beginning with Redis OSS 7, ElastiCache supports switching between Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled).
- The Amazon ElastiCache for Redis OSS engine upgrade process is designed to make a best effort to retain your existing data
  and requires successful Redis OSS replication.
- When upgrading the engine, ElastiCache will terminate existing client connections. To minimize downtime during engine upgrades,
  we recommend you implement [best practices for Redis OSS clients](BestPractices.Clients.md "BestPractices.Clients.md")
  with error retries and exponential backoff and the best practices for
  [minimizing downtime during maintenance](BestPractices.md "BestPractices.md").
- You can't upgrade directly from Valkey or Redis OSS (cluster mode disabled) to Valkey or Redis OSS (cluster mode enabled) when you upgrade your
  engine. The following procedure shows you how to upgrade from Valkey or Redis OSS (cluster mode disabled)
  to Valkey or Redis OSS (cluster mode enabled).

###### To upgrade from a Valkey or Redis OSS (cluster mode disabled) to Valkey or Redis OSS (cluster mode enabled) engine version

    1. Make a backup of your Valkey or Redis OSS (cluster mode disabled) cluster or replication group. For more information,
     see [Taking manual backups](backups-manual.md "backups-manual.md").
    2. Use the backup to create and seed a Valkey or Redis OSS (cluster mode enabled) cluster with one shard (node group).
     Specify the new engine version and enable cluster mode when creating the cluster or
     replication group. For more information, see [Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md "backups-seeding-redis.md").
    3. Delete the old Valkey or Redis OSS (cluster mode disabled) cluster or replication group. For more information,
     see [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md") or [Deleting a replication group](Replication.md "Replication.md").
    4. Scale the new Valkey or Redis OSS (cluster mode enabled) cluster or replication group to the number of shards (node groups)
     that you need. For more information, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md")

- When upgrading major engine versions, for example from 5.0.6 to 6.0, you need to also choose a new parameter group that is compatible with the new engine version.
- For single Redis OSS clusters and clusters with Multi-AZ disabled, we recommend that
  sufficient memory be made available to Redis OSS as described in [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md").
  In these cases, the primary is unavailable to service requests during the
  upgrade process.
- For Redis OSS clusters with Multi-AZ enabled, we also recommend that you schedule engine
  upgrades during periods of low incoming write traffic. When upgrading to Redis OSS 5.0.6 or above, the primary cluster continues to be available to service requests during the upgrade process.

Clusters and replication groups with multiple shards are processed and patched as follows:

    + All shards are processed in parallel. Only one upgrade operation is performed
     on a shard at any time.
    + In each shard, all replicas are processed before the primary is processed. If there are
     fewer replicas in a shard, the primary in that shard might be
     processed before the replicas in other shards are finished
     processing.
    + Across all the shards, primary nodes are processed in series.
     Only one primary node is upgraded at a time.

- If encryption is enabled on your current cluster or replication group, you cannot upgrade to
  an engine version that does not support encryption, such as from 3.2.6 to 3.2.10.
  **Memcached considerations**

When upgrading a node-based Memcached cluster, consider the following.

- Engine version management is designed so that you can have as much control as possible over
  how patching occurs. However, ElastiCache reserves the right to patch your cluster
  on your behalf in the unlikely event of a critical security vulnerability in
  the system or cache software.
- Because the Memcached engine does not support persistence, Memcached engine version
  upgrades are always a disruptive process that clears all cache data in the
  cluster.
