# Version Management for ElastiCache

Manage how you would like to update your ElastiCache caches and node-based clusters updated for the Valkey, Memcached, and Redis OSS engines.

## Version management for ElastiCache Serverless Cache

Manage if and when the ElastiCache Serverless cache is upgraded and perform version upgrades on
your own terms and timelines.

ElastiCache Serverless automatically applies the latest minor and patch software version to your cache,
without any impact or downtime to your application. No action is required on your end.

When a new major version is available, ElastiCache Serverless will send you a notification in the console and an event in EventBridge. You can choose to upgrade your cache to the latest major version by modifying your cache using the Console, CLI, or API and selecting the latest engine version. Similar to minor and patch upgrades, major version upgrades are performed without downtime to your application.

## Version management for node-based ElastiCache clusters

When working with node-based ElastiCache clusters, you can control when the software powering your cluster
is upgraded to new versions that are supported by ElastiCache. You can control when to upgrade your cache to the
latest available major, minor, and patch versions. You initiate engine version upgrades to your cluster or replication group by modifying it and specifying a new engine version.

You can control if and when the protocol-compliant software powering your cluster is
upgraded to new versions that are supported by ElastiCache. This level of control enables you
to maintain compatibility with specific versions, test new versions
with your application before deploying in production, and perform version upgrades on
your own terms and timelines.

Because version upgrades might involve some compatibility risk, they don't occur
automatically. You must initiate them.

**Valkey and Redis OSS clusters**

###### Note

- If a Valkey or Redis OSS cluster is replicated across one or more Regions, the engine version is upgraded for secondary Regions
  and then for the primary Region.
- ElastiCache for Redis OSS versions are identified with a semantic version which comprise a major and minor component.
  For example, in Redis OSS 6.2, the major version is 6, and the minor version 2.
  When operating node-based clusters, ElastiCache for Redis OSS also exposes the patch component, e.g. Redis OSS 6.2.1, and the patch version is 1.

Major versions are for API incompatible changes and minor versions are for new functionality added in a backwards-compatible way. Patch versions are for backwards-compatible bug fixes and non-functional changes.

With Valkey and Redis OSS, you initiate engine version upgrades to your cluster or replication group by modifying it
and specifying a new engine version. For more information, see [Modifying a replication group](Replication.md "Replication.md").

**Memcached**

With Memcached, to upgrade to a newer version you must modify your cluster and specify the new engine version
you want to use.
Upgrading to a newer Memcached version is a destructive process – you lose your
data and start with a cold cache.
For more information, see [Modifying an ElastiCache cluster](Clusters.md "Clusters.md").

You should be aware of the following requirements when upgrading from an older version of
Memcached to Memcached version 1.4.33 or newer. `CreateCacheCluster` and
`ModifyCacheCluster` fails under the following conditions:

- If `slab_chunk_max > max_item_size`.
- If `max_item_size modulo slab_chunk_max != 0`.
- If `max_item_size > ((max_cache_memory - memcached_connections_overhead) / 4)`.

The value `(max_cache_memory - memcached_connections_overhead)` is the node's
memory useable for data.
For more information, see [Memcached connection overhead](ParameterGroups.md#ParameterGroups.Memcached.Overhead "ParameterGroups.md#ParameterGroups.Memcached.Overhead").

## Supported engines and versions

ElastiCache serverless caches support ElastiCache version 7.2 for Valkey and above, ElastiCache version 1.6 for Memcached and above, and ElastiCache 7.0 for Redis OSS and above.

Node-based ElastiCache clusters support ElastiCache version 7.2 for Valkey and above, ElastiCache version 1.4.5 for Memcached and above, and ElastiCache 4.0.10 for Redis OSS and above.

###### Node-based ElastiCache clusters support the following Valkey versions:

- [Supported Valkey versions](#supported-engine-versions.valkey "#supported-engine-versions.valkey")
- [Valkey 8.2](#valkey-version-8.2 "#valkey-version-8.2")
- [Valkey 8.1](#valkey-version-8.1 "#valkey-version-8.1")
- [Valkey 8.0](#valkey-version-8 "#valkey-version-8")
- [ElastiCache version 7.2.6 for Valkey](#valkey-version-7.2.6 "#valkey-version-7.2.6")

### Supported Valkey versions

Supported Valkey versions below. Note that Valkey supports most features available in ElastiCache version 7.2 for Redis OSS by default.

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

### ElastiCache version 8.2 for Valkey

Here are some of the new features introduced in Valkey 8.2 (compared to ElastiCache Valkey 8.1):

- ElastiCache for Valkey v8.2 provides native support for [vector search](vector-search.md "vector-search.md"), delivering latency as low as microseconds-the lowest latency vector search with the highest throughput and best price-performance at 95%+ recall rate among popular vector databases on AWS.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/").

ElastiCache version 8.2 for Valkey enhances Valkey 8.1 with vector search capabilities based on [valkey-search module](https://github.com/valkey-io/valkey-search "https://github.com/valkey-io/valkey-search"). For more information on the Valkey 8.2 release, see [release notes](https://github.com/valkey-io/valkey-search/blob/main/00-RELEASENOTES "https://github.com/valkey-io/valkey-search/blob/main/00-RELEASENOTES") for valkey-search. Please note that ElastiCache v8.2 is compatible with Valkey v8.1.

### ElastiCache version 8.1 for Valkey

Here are some of the new features introduced in Valkey 8.1 (compared to ElastiCache Valkey 8.0):

- A [new hash table](https://valkey.io/blog/new-hash-table/ "https://valkey.io/blog/new-hash-table/") implementation that reduces memory overhead to lower memory usage by as much as 20% for common key/value patterns.
- Native support for [Bloom filters](https://valkey.io/topics/bloomfilters/ "https://valkey.io/topics/bloomfilters/"), a new data type allowing you to perform lookups using as much as 98% less memory compared to using the Set data type.
- New command [COMMANDLOG](https://valkey.io/commands/commandlog-get/ "https://valkey.io/commands/commandlog-get/") that records slow executions, large requests, and large replies.
- New conditional update support to the SET command using IFEQ argument.
- Performance improvements, including up to 45% lower latency for the ZRANK command, up to 12x faster performance for PFMERGE and PFCOUNT, and up to 514% higher throughput for BITCOUNT.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 8.1 release, see [Valkey 8.1 Release Notes](https://github.com/valkey-io/valkey/blob/8.1/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/8.1/00-RELEASENOTES")

### ElastiCache version 8.0 for Valkey

Here are some of the new features introduced in Valkey 8.0 (compared to ElastiCache Valkey 7.2.6):

- Memory efficiency improvements, allowing users to store up to 20% more data per node without any application changes.
- Newly-introduced per-slot metrics infrastructure for node-based clusters, providing detailed visibility into the performance and resource usage of individual slots.
- ElastiCache Serverless for Valkey 8.0 can double the supported requests per second (RPS) every 2-3 minutes, reaching 5M RPS per cache from zero in under 13 minutes, with consistent sub-millisecond p50 read latency.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 8 release, see [Valkey 8 Release Notes](https://github.com/valkey-io/valkey/blob/8.0/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/8.0/00-RELEASENOTES")

### ElastiCache version 7.2.6 for Valkey

On October 10 2024, ElastiCache version 7.2.6 for Valkey was released. Here are some of the new features introduced in 7.2 (compared to ElastiCache version 7.1 for Redis OSS):

- Performance and memory optimizations for various data types: memory optimization for list and set type keys, speed optimization for sorted sets commands, performance optimization for commands with multiple keys in cluster mode, pub/sub performance improvements, performance optimization for SCAN, SSCAN, HSCAN, ZSCAN commands and numerous other smaller optimizations.
- New WITHSCORE option for ZRANK and ZREVRANK commands
- CLIENT NO-TOUCH for clients to run commands without affecting LRU/LFU of keys.
- New command CLUSTER MYSHARDID that returns the Shard ID of the node to logically group nodes in cluster mode based on replication.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the ElastiCache version 7.2 for Valkey release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES")
(ElastiCache version 7.2 for Valkey includes all changes from ElastiCache version 7.1 for Redis OSS up to ElastiCache version 7.2.4 for Redis OSS). [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES") at Valkey on GitHub.
