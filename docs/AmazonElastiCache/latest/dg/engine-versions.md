# Engine versions and upgrading in ElastiCache

This section covers the supported Valkey, Memcached, and Redis OSS engines and how to upgrade.
Note that all features available with Redis OSS 7.2 are available in Valkey 7.2 and above by default.
You can also upgrade from some existing ElastiCache for Redis OSS engines to a Valkey engine.

## ElastiCache version 8.2 for Valkey

Here are some of the new features introduced in Valkey 8.2 (compared to ElastiCache Valkey 8.1):

- ElastiCache for Valkey v8.2 provides native support for [vector search](vector-search.md "vector-search.md"), delivering latency as low as microseconds-the lowest latency vector search with the highest throughput and best price-performance at 95%+ recall rate among popular vector databases on AWS.

For more information on Valkey, see [Valkey.](https://valkey.io/ "https://valkey.io/")

ElastiCache version 8.2 for Valkey enhances Valkey 8.1 with vector search capabilities based on [valkey-search module](https://github.com/valkey-io/valkey-search "https://github.com/valkey-io/valkey-search"). For more information on the Valkey 8.2 release, see [release notes](https://github.com/valkey-io/valkey-search/blob/main/00-RELEASENOTES "https://github.com/valkey-io/valkey-search/blob/main/00-RELEASENOTES") for valkey-search. Please note that ElastiCache v8.2 is compatible with Valkey v8.1.

## ElastiCache version 8.1 for Valkey

Here are some of the new features introduced in Valkey 8.1 (compared to ElastiCache Valkey 8.0):

- A [new hash table](https://valkey.io/blog/new-hash-table/ "https://valkey.io/blog/new-hash-table/") implementation that reduces memory overhead to lower memory usage by as much as 20% for common key/value patterns.
- Native support for [Bloom filters](https://valkey.io/topics/bloomfilters/ "https://valkey.io/topics/bloomfilters/"), a new data type allowing you to perform lookups using as much as 98% less memory compared to using the Set data type.
- New command [COMMANDLOG](https://valkey.io/commands/commandlog-get/ "https://valkey.io/commands/commandlog-get/") that records slow executions, large requests, and large replies.
- New conditional update support to the SET command using IFEQ argument.
- Performance improvements, including up to 45% lower latency for the ZRANK command, up to 12x faster performance for PFMERGE and PFCOUNT, and up to 514% higher throughput for BITCOUNT.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 8.1 release, see [Valkey 8.1 Release Notes](https://github.com/valkey-io/valkey/blob/8.1/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/8.1/00-RELEASENOTES")

## ElastiCache version 8.0 for Valkey

Here are some of the new features introduced in Valkey 8.0 (compared to ElastiCache Valkey 7.2.6):

- Memory efficiency improvements, allowing users to store up to 20% more data per node without any application changes.
- Newly-introduced per-slot metrics infrastructure for node-based clusters, providing detailed visibility into the performance and resource usage of individual slots.
- ElastiCache Serverless for Valkey 8.0 can double the supported requests per second (RPS) every 2-3 minutes, reaching 5M RPS per cache from zero in under 13 minutes, with consistent sub-millisecond p50 read latency.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 8 release, see [Valkey 8 Release Notes](https://github.com/valkey-io/valkey/blob/8.0/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/8.0/00-RELEASENOTES")

## ElastiCache version 7.2.6 for Valkey

On October 10 2024, ElastiCache version 7.2.6 for Valkey was released. Here are some of the new features introduced in 7.2 (compared to ElastiCache version 7.1 for Redis OSS):

- Performance and memory optimizations for various data types: memory optimization for list and set type keys, speed optimization for sorted sets commands, performance optimization for commands with multiple keys in cluster mode, pub/sub performance improvements, performance optimization for SCAN, SSCAN, HSCAN, ZSCAN commands and numerous other smaller optimizations.
- New WITHSCORE option for ZRANK and ZREVRANK commands
- CLIENT NO-TOUCH for clients to run commands without affecting LRU/LFU of keys.
- New command CLUSTER MYSHARDID that returns the Shard ID of the node to logically group nodes in cluster mode based on replication.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the ElastiCache version 7.2 for Valkey release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES")
(ElastiCache version 7.2 for Valkey includes all changes from ElastiCache version 7.1 for Redis OSS up to ElastiCache version 7.2.4 for Redis OSS). [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES") at Valkey on GitHub.

## Supported Redis OSS engine versions

ElastiCache Serverless caches and node-based clusters support all Redis OSS versions 7.1 and before.

- [ElastiCache version 7.1 for Redis OSS (enhanced)](#redis-version-7.1 "#redis-version-7.1")

###### Node-based ElastiCache clusters support the following Redis OSS versions:

- [ElastiCache version 7.1 for Redis OSS (enhanced)](#redis-version-7.1 "#redis-version-7.1")
- [ElastiCache version 7.0 for Redis OSS (enhanced)](#redis-version-7.0 "#redis-version-7.0")
- [ElastiCache version 6.2 for Redis OSS (enhanced)](#redis-version-6.2 "#redis-version-6.2")
- [ElastiCache version 6.0 for Redis OSS (enhanced)](#redis-version-6.0 "#redis-version-6.0")
- [ElastiCache version 5.0.6 for Redis OSS (enhanced)](#redis-version-5-0.6 "#redis-version-5-0.6")
- [ElastiCache version 5.0.5 for Redis OSS (deprecated, use version 5.0.6)](#redis-version-5-0.5 "#redis-version-5-0.5")
- [ElastiCache version 5.0.4 for Redis OSS (deprecated, use version 5.0.6)](#redis-version-5-0.4 "#redis-version-5-0.4")
- [ElastiCache version 5.0.3 for Redis OSS (deprecated, use version 5.0.6)](#redis-version-5-0.3 "#redis-version-5-0.3")
- [ElastiCache version 5.0.0 for Redis OSS (deprecated, use version 5.0.6)](#redis-version-5-0 "#redis-version-5-0")
- [ElastiCache version 4.0.10 for Redis OSS (enhanced)](#redis-version-4-0-10 "#redis-version-4-0-10")
- [Past End of Life (EOL) versions (3.x)](#redis-version-3-2-10-scheduled-eol "#redis-version-3-2-10-scheduled-eol")
- [Past End of Life (EOL) versions (2.x)](#redis-version-2-x-eol "#redis-version-2-x-eol")

### ElastiCache version 7.1 for Redis OSS (enhanced)

This release contains performance improvements which enable workloads to drive
higher throughput and lower operation latencies. ElastiCache version 7.1 for Redis OSS introduces [two main enhancements](https://aws.amazon.com/blogs/database/achieve-over-500-million-requests-per-second-per-cluster-with-amazon-elasticache-for-redis-7-1/ "https://aws.amazon.com/blogs/database/achieve-over-500-million-requests-per-second-per-cluster-with-amazon-elasticache-for-redis-7-1/") :

We extended the enhanced I/O threads functionality to also handle the
presentation layer logic. By presentation layer, we mean the Enhanced I/O
threads which are now not only reading client input, but also parsing the
input into Redis OSS binary command format. This is then forwarded to the main
thread for execution which provides performance gain. Improved Redis OSS memory access pattern. Execution steps from many data
structure operations are interleaved, to ensure parallel memory access and
reduced memory access latency. When running ElastiCache on Graviton3-based
`R7g.4xlarge` or larger, customers can achieve over 1 million
requests per second per node. With the performance improvements to ElastiCache for Redis OSS v7.1, customers can achieve up to 100% more throughput and 50% lower
P99 latency relative to ElastiCache for Redis OSS v7.0. These enhancements are enabled
on node sizes with at least 8 physical cores (`2xlarge` on
Graviton, and `4xlarge` on x86), regardless of the CPU type and
require no client changes.

###### Note

ElastiCache v7.1 is compatible with Redis OSS v7.0.

### ElastiCache version 7.0 for Redis OSS (enhanced)

ElastiCache for Redis OSS 7.0 adds a number of improvements and support for new functionality:

- [Functions](https://valkey.io/topics/functions-intro/ "https://valkey.io/topics/functions-intro/"): ElastiCache for Redis OSS 7 adds support for Redis OSS Functions, and provides a managed experience enabling developers to execute
  [LUA scripts](https://valkey.io/topics/eval-intro/ "https://valkey.io/topics/eval-intro/") with application logic stored on the ElastiCache
  cluster, without requiring clients to re-send the scripts to the server with
  every connection.
- [ACL
  improvements](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/"): Valkey and Redis OSS 7 adds support for the next
  version of Access Control Lists (ACLs). Clients can now specify multiple sets of permissions on specific keys or
  keyspaces in Valkey and Redis OSS.
- [Sharded
  Pub/Sub](https://valkey.io/topics/pubsub/ "https://valkey.io/topics/pubsub/"): ElastiCache for Valkey and Redis OSS 7 adds support to run Pub/Sub
  functionality in a sharded way when running ElastiCache in Cluster Mode Enabled
  (CME). Pub/Sub capabilities enable publishers to issue messages to any
  number of subscribers on a channel. Channels
  are bound to a shard in the ElastiCache cluster, eliminating the need to
  propagate channel information across shards resulting in improved
  scalability.
- Enhanced I/O multiplexing: ElastiCache for Valkey and Redis OSS 7 introduces enhanced
  I/O multiplexing, which delivers increased throughput and reduced latency
  for high-throughput workloads that have many concurrent client connections
  to an ElastiCache cluster. For example, when using a cluster of r6g.xlarge
  nodes and running 5200 concurrent clients, you can achieve up to 72%
  increased throughput (read and write operations per second) and up to 71%
  decreaseed P99 latency, compared with ElastiCache version 6 for Redis OSS.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/").
For more information on the Redis OSS 7.0 release, see [Redis OSS 7.0 Release Notes](https://github.com/redis/redis/blob/7.0/00-RELEASENOTES "https://github.com/redis/redis/blob/7.0/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 6.2 for Redis OSS (enhanced)

ElastiCache for Redis OSS 6.2 includes performance improvements for TLS-enabled clusters using x86
node types with 8 vCPUs or more or Graviton2 node types with 4 vCPUs or more. These
enhancements improve throughput and reduce client connection establishment time by
offloading encryption to other vCPUs. With Redis OSS 6.2, you can also manage access to
Pub/Sub channels with Access Control List (ACL) rules.

With this version, we also introduce support for data tiering on cluster nodes
containing locally attached NVMe SSD. For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").

Redis OSS engine version 6.2.6 also introduces support for native JavaScript Object
Notation (JSON) format, a simple, schemaless way to encode complex datasets inside
Redis OSS clusters. With JSON support, you can leverage the performance and Redis OSS APIs
for applications that operate over JSON. For more information, see [Getting
started with JSON](json-gs.md "json-gs.md"). Also included are JSON-related metrics,
`JsonBasedCmds` and `JsonBasedCmdsLatency`, that are
incorporated into CloudWatch to monitor the usage of this datatype. For more information,
see [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md").

You specify the engine version by using 6.2. ElastiCache will automatically invoke the
preferred patch version of Redis OSS 6.2 that is available. For example, when you
create/modify a cluster, you set the `--engine-version` parameter
to 6.2. The cluster will be launched with the current available preferred patch
version of Redis OSS 6.2 at the creation/modification time. Specifying engine version
6.x in the API will result in the latest minor version of Redis OSS 6.

For existing 6.0 clusters, you can opt-in to the next auto minor version upgrade
by setting the `AutoMinorVersionUpgrade` parameter to `yes` in
the `CreateCacheCluster`, `ModifyCacheCluster`,
`CreateReplicationGroup` or `ModifyReplicationGroup` APIs.
ElastiCache will upgrade the minor version of your existing 6.0 clusters to 6.2 using
self-service updates. For more information, see [Self-service
updates in Amazon ElastiCache](Self-Service-Updates.md "Self-Service-Updates.md").

When calling the DescribeCacheEngineVersions API, the `EngineVersion`
parameter value will be set to 6.2 and the actual engine version with the patch
version will be returned in the `CacheEngineVersionDescription`
field.

For more information on the Redis OSS 6.2 release, see [Redis OSS 6.2 Release Notes](https://github.com/redis/redis/blob/6.2/00-RELEASENOTES "https://github.com/redis/redis/blob/6.2/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 6.0 for Redis OSS (enhanced)

Amazon ElastiCache introduces the next version of ElastiCache for the Redis OSS engine, which includes
[Authenticating Users with Role Based Access Control](Clusters.md "Clusters.md"), client-side
caching and significant operational improvements.

Beginning with Redis OSS 6.0, ElastiCache will offer a single version for each Redis OSS
minor release, rather than offering multiple patch versions. ElastiCache will
automatically manage the patch version of your running clusters, ensuring
improved performance and enhanced security.

You can also opt-in to the next auto minor version upgrade by setting the
`AutoMinorVersionUpgrade` parameter to `yes` and ElastiCache
will manage the minor version upgrade, through self-service updates. For more
information, see [Service updates in ElastiCache](Self-Service-Updates.md "Self-Service-Updates.md").

You specify the engine version by using `6.0`. ElastiCache will
automatically invoke the preferred patch version of Redis OSS 6.0 that is available. For
example, when you create/modify a cluster, you set the
`--engine-version` parameter to 6.0. The cluster will be launched
with the current available preferred patch version of Redis OSS 6.0 at the
creation/modification time. Any request with a specific patch version value will be
rejected, an exception will be thrown and the process will fail.

When calling the DescribeCacheEngineVersions API, the `EngineVersion`
parameter value will be set to 6.0 and the actual engine version with the patch
version will be returned in the `CacheEngineVersionDescription`
field.

For more information on the Redis OSS 6.0 release, see [Redis OSS 6.0 Release Notes](https://github.com/redis/redis/blob/6.0/00-RELEASENOTES "https://github.com/redis/redis/blob/6.0/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 5.0.6 for Redis OSS (enhanced)

Amazon ElastiCache introduces the next version of ElastiCache for the Redis OSS engine, which includes bug
fixes and the following cumulative updates:

- Engine stability guarantee in special conditions.
- Improved Hyperloglog error handling.
- Enhanced handshake commands for reliable replication.
- Consistent message delivery tracking via `XCLAIM`
  command.
- Improved `LFU` field management in objects.
- Enhanced transaction management when using `ZPOP`.
- Ability to rename commands: A parameter called
  `rename-commands` that allows you to rename potentially
  dangerous or expensive Redis OSS commands that might cause accidental data loss,
  such as `FLUSHALL` or `FLUSHDB`. This is similar to
  the rename-command configuration in open source Redis OSS. However, ElastiCache
  has improved the experience by providing a fully managed workflow. The
  command name changes are applied immediately, and automatically propagated
  across all nodes in the cluster that contain the command list. There is no
  intervention required on your part, such as rebooting nodes.

The following examples demonstrate how to modify existing parameter
groups. They include the `rename-commands` parameter, which is a
space-separated list of commands you want to rename:

```
aws elasticache modify-cache-parameter-group --cache-parameter-group-name `custom_param_group`
--parameter-name-values "ParameterName=rename-commands,  ParameterValue='flushall restrictedflushall'" --region `region`

```

In this example, the _rename-commands_
parameter is used to rename the `flushall` command to
`restrictedflushall`.

To rename multiple commands, use the following:

```
aws elasticache modify-cache-parameter-group --cache-parameter-group-name `custom_param_group`
--parameter-name-values "ParameterName=rename-commands,  ParameterValue='flushall restrictedflushall flushdb restrictedflushdb''" --region `region`

```

To revert any change, re-run the command and exclude any renamed values
from the `ParameterValue` list that you want to retain, as shown
following:

```
aws elasticache modify-cache-parameter-group --cache-parameter-group-name `custom_param_group`
--parameter-name-values "ParameterName=rename-commands,  ParameterValue='flushall restrictedflushall'" --region `region`

```

In this case, the `flushall` command is renamed to
`restrictedflushall` and any other renamed commands revert to
their original command names.

###### Note

When renaming commands, you are restricted to the following
limitations:

    + All renamed commands should be alphanumeric.
    + The maximum length of new command names is 20 alphanumeric
     characters.
    + When renaming commands, ensure that you update the parameter
     group associated with your cluster.
    + To prevent a command's use entirely, use the keyword
     `blocked`, as shown following:



    ```
    aws elasticache modify-cache-parameter-group --cache-parameter-group-name `custom_param_group`
    --parameter-name-values "ParameterName=rename-commands,  ParameterValue='flushall blocked'" --region `region`

    ```

For more information on the parameter changes and a list of what commands
are eligible for renaming, see [Redis OSS 5.0.3 parameter changes](ParameterGroups.md#ParameterGroups.Redis.5-0-3 "ParameterGroups.md#ParameterGroups.Redis.5-0-3").

- Redis OSS Streams: This models a log data structure that allows producers to
  append new items in real time. It also allows consumers to consume messages
  either in a blocking or nonblocking fashion. Streams also allow consumer
  groups, which represent a group of clients to cooperatively consume
  different portions of the same stream of messages, similar to [Apache Kafka](https://kafka.apache.org/documentation/ "https://kafka.apache.org/documentation/"). For
  more information, see [Streams](https://valkey.io/topics/streams-intro "https://valkey.io/topics/streams-intro").
- Support for a family of stream commands, such as `XADD`,
  `XRANGE` and `XREAD`. For more information, see
  [Streams Commands](https://valkey.io/commands/#stream "https://valkey.io/commands/#stream").
- A number of new and renamed parameters. For more information, see [Redis OSS 5.0.0 parameter changes](ParameterGroups.md#ParameterGroups.Redis.5.0 "ParameterGroups.md#ParameterGroups.Redis.5.0").
- A new Redis OSS metric, `StreamBasedCmds`.
- Slightly faster snapshot time for Redis OSS nodes.

###### Important

ElastiCache has back-ported two critical bug fixes from [Redis OSS open source version 5.0.1](https://github.com/redis/redis/blob/5.0/00-RELEASENOTES "https://github.com/redis/redis/blob/5.0/00-RELEASENOTES"). They are listed following:

- RESTORE mismatch reply when certain keys have already expired.
- The `XCLAIM` command can potentially return a wrong entry
  or desynchronize the protocol.
  Both of these bug fixes are included in ElastiCache for Redis OSS support for Redis OSS engine
  version 5.0.0 and are consumed in future version updates.

For more information, see [Redis OSS 5.0.6 Release Notes](https://github.com/redis/redis/blob/5.0/00-RELEASENOTES "https://github.com/redis/redis/blob/5.0/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 5.0.5 for Redis OSS (deprecated, use version 5.0.6)

Amazon ElastiCache introduces the next version of ElastiCache for the Redis OSS engine;. It includes online
configuration changes for ElastiCache of auto-failover clusters during all planned
operations. You can now scale your cluster, upgrade the Redis OSS engine version and
apply patches and maintenance updates while the cluster stays online and continues
serving incoming requests. It also includes bug fixes.

For more information, see [Redis OSS 5.0.5 Release Notes](https://github.com/redis/redis/blob/5.0/00-RELEASENOTES "https://github.com/redis/redis/blob/5.0/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 5.0.4 for Redis OSS (deprecated, use version 5.0.6)

Amazon ElastiCache introduces the next version of the Redis OSS engine supported by ElastiCache.
It includes the following enhancements:

- Engine stability guarantee in special conditions.
- Improved Hyperloglog error handling.
- Enhanced handshake commands for reliable replication.
- Consistent message delivery tracking via `XCLAIM`
  command.
- Improved `LFU` field management in objects.
- Enhanced transaction management when using `ZPOP`.

For more information, see [Redis OSS 5.0.4 Release Notes](https://github.com/redis/redis/blob/5.0/00-RELEASENOTES "https://github.com/redis/redis/blob/5.0/00-RELEASENOTES") at Redis OSS on GitHub.

### ElastiCache version 5.0.3 for Redis OSS (deprecated, use version 5.0.6)

Amazon ElastiCache introduces the next version of ElastiCache for the Redis OSS engine,
which includes bug fixes.

### ElastiCache version 5.0.0 for Redis OSS (deprecated, use version 5.0.6)

Amazon ElastiCache introduces the next major version of ElastiCache for the Redis OSS engine. ElastiCache version 5.0.0 for Redis OSS
brings support for the following improvements:

- Redis OSS Streams: This models a log data structure that allows producers to
  append new items in real time. It also allows consumers to consume messages
  either in a blocking or nonblocking fashion. Streams also allow consumer
  groups, which represent a group of clients to cooperatively consume
  different portions of the same stream of messages, similar to [Apache Kafka](https://kafka.apache.org/documentation/ "https://kafka.apache.org/documentation/"). For
  more information, see [Streams](https://valkey.io/topics/streams-intro "https://valkey.io/topics/streams-intro").
- Support for a family of stream commands, such as `XADD`,
  `XRANGE` and `XREAD`. For more information, see
  [Streams Commands](https://valkey.io/commands/#stream "https://valkey.io/commands/#stream").
- A number of new and renamed parameters. For more information, see [Redis OSS 5.0.0 parameter changes](ParameterGroups.md#ParameterGroups.Redis.5.0 "ParameterGroups.md#ParameterGroups.Redis.5.0").
- A new Redis OSS metric, `StreamBasedCmds`.
- Slightly faster snapshot time for Redis OSS nodes.

### ElastiCache version 4.0.10 for Redis OSS (enhanced)

Amazon ElastiCache introduces the next major version of ElastiCache for the Redis OSS engine.
ElastiCache version 4.0.10 for Redis OSS brings support for the following improvements:

- Both online cluster resizing and encryption in a single ElastiCache version.
  For more information, see the following:
  - [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md")
  - [Online resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online")
  - [Data security in Amazon ElastiCache](encryption.md "encryption.md")

- A number of new parameters. For more information, see [Redis OSS 4.0.10 parameter changes](ParameterGroups.md#ParameterGroups.Redis.4-0-10 "ParameterGroups.md#ParameterGroups.Redis.4-0-10").
- Support for family of memory commands, such as `MEMORY`. For
  more information, see [Commands](https://valkey.io/commands "https://valkey.io/commands") (search on MEMO).
- Support for memory defragmentation while online thus allowing more
  efficient memory utilization and more memory available for your data.
- Support for asynchronous flushes and deletes. ElastiCache for Redis OSS supports commands
  like `UNLINK`, `FLUSHDB` and `FLUSHALL` to
  run in a different thread from the main thread. Doing this helps improve
  performance and response times for your applications by freeing memory
  asynchronously.
- A new Redis OSS metric, `ActiveDefragHits`. For more information,
  see [Metrics for Redis OSS](../../../AmazonCloudWatch/latest/monitoring/CacheMetrics.md "../../../AmazonCloudWatch/latest/monitoring/CacheMetrics.md").

Redis OSS (cluster mode disabled) users running ElastiCache version 3.2.10 for Redis OSS can use the console to upgrade
their clusters via online upgrade.

| Comparing ElastiCache cluster resizing and encryption support                                                                                                                                                 |       | Version |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------- | ---------------- |
| Feature                                                                                                                                                                                                       | 3.2.6 | 3.2.10  | 4.0.10 and later |
| Online cluster resizing \*                                                                                                                                                                                    | No    | Yes     | Yes              |
| In-transit encryption \*\*                                                                                                                                                                                    | Yes   | No      | Yes              |
| At rest encryption \*\*                                                                                                                                                                                       | Yes   | No      | Yes              |
| \<br>• Adding, removing, and rebalancing<br>shards.                                                                                                                                                           |
| \*\<br>• Required for FedRAMP, HIPAA, and PCI DSS<br>compliant applications. For more information, see [Compliance validation for Amazon ElastiCache](elasticache-compliance.md "elasticache-compliance.md"). |

### Past End of Life (EOL) versions (3.x)

#### ElastiCache version 3.2.10 for Redis OSS (enhanced)

Amazon ElastiCache introduces the next major version of ElastiCache for the Redis OSS engine.
ElastiCache version 3.2.10 for Redis OSS (enchanced) introduces online cluster resizing to add or remove shards from the
cluster while it continues to serve incoming I/O requests. ElastiCache for Redis OSS 3.2.10 users have
all the functionality of earlier Redis OSS versions except the ability to encrypt their
data. This ability is currently available only in version 3.2.6.

| Comparing ElastiCache versions 3.2.6 and 3.2.10 for Redis OSS                                                                                                                                                 |       | Version |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------- |
| Feature                                                                                                                                                                                                       | 3.2.6 | 3.2.10  |
| Online cluster resizing \*                                                                                                                                                                                    | No    | Yes     |
| In-transit encryption \*\*                                                                                                                                                                                    | Yes   | No      |
| At rest encryption \*\*                                                                                                                                                                                       | Yes   | No      |
| \<br>• Adding, removing, and rebalancing shards.                                                                                                                                                              |
| \*\<br>• Required for FedRAMP, HIPAA, and PCI DSS compliant applications. For<br>more information, see [Compliance validation for Amazon ElastiCache](elasticache-compliance.md "elasticache-compliance.md"). |

For more information, see the following:

- [Online resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online")
- [Online cluster resizing](best-practices-online-resharding.md "best-practices-online-resharding.md")

#### ElastiCache version 3.2.6 for Redis OSS (enhanced)

Amazon ElastiCache introduces the next major version of ElastiCache for the Redis OSS engine.
ElastiCache version 3.2.6 for Redis OSS users have access to all the functionality of earlier Redis OSS versions, plus the
option to encrypt their data. For more information, see the following:

- [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md "in-transit-encryption.md")
- [At-Rest Encryption in ElastiCache](at-rest-encryption.md "at-rest-encryption.md")
- [Compliance validation for Amazon ElastiCache](elasticache-compliance.md "elasticache-compliance.md")

#### ElastiCache version 3.2.4 for Redis OSS (enhanced)

Amazon ElastiCache version 3.2.4 introduces the next major version of ElastiCache for the Redis OSS engine.
ElastiCache 3.2.4 users have all the functionality of earlier Redis OSS versions available to them, plus the option to
run in _cluster mode_ or _non-cluster mode_.
The following table summarizes .

| Comparing Redis OSS 3.2.4 non-cluster mode and cluster mode                                     | Feature                 | Non-cluster mode                   | Cluster mode |
| ----------------------------------------------------------------------------------------------- | ----------------------- | ---------------------------------- | ------------ |
| Data partitioning                                                                               | No                      | Yes                                |
| Geospatial indexing                                                                             | Yes                     | Yes                                |
| Change node type                                                                                | Yes                     | Yes \*                             |
| Replica scaling                                                                                 | Yes                     | Yes \*                             |
| Scale out                                                                                       | No                      | Yes \*                             |
| Database support                                                                                | Multiple                | Single                             |
| Parameter group                                                                                 | `default.redis3.2` \*\* | `default.redis3.2.cluster.on` \*\* |
| \*  See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md") |
| \*\* Or one derived from it.                                                                    |

###### Notes:

- **Partitioning** –
  the ability to split your data across 2 to 500 node groups (shards)
  with replication support for each node group.
- **Geospatial indexing** –
  Redis OSS 3.2.4 introduces support for geospatial indexing via six GEO commands.
  For more information, see the Redis OSS GEO\* command documentation [Commands: GEO](http://valkey.io/commands#geo "http://valkey.io/commands#geo") on the Valkey Commands page (filtered for GEO).

For information about additional Redis OSS 3 features, see [Redis OSS 3.2 release notes](https://github.com/redis/redis/blob/3.2/00-RELEASENOTES "https://github.com/redis/redis/blob/3.2/00-RELEASENOTES") and [Redis OSS 3.0 release notes](https://github.com/redis/redis/blob/3.0/00-RELEASENOTES "https://github.com/redis/redis/blob/3.0/00-RELEASENOTES").

Currently ElastiCache managed Valkey or Redis OSS (cluster mode enabled) does not support the following Redis OSS 3.2 features:

- Replica migration
- Cluster rebalancing
- Lua debugger

ElastiCache disables the following Redis OSS 3.2 management commands:

- `cluster meet`
- `cluster replicate`
- `cluster flushslots`
- `cluster addslots`
- `cluster delslots`
- `cluster setslot`
- `cluster saveconfig`
- `cluster forget`
- `cluster failover`
- `cluster bumpepoch`
- `cluster set-config-epoch`
- `cluster reset`

For information about Redis OSS 3.2.4 parameters, see [Redis OSS 3.2.4 parameter changes](ParameterGroups.md#ParameterGroups.Redis.3-2-4 "ParameterGroups.md#ParameterGroups.Redis.3-2-4").

### Past End of Life (EOL) versions (2.x)

#### ElastiCache version 2.8.24 for Redis OSS (enhanced)

Redis OSS improvements added since version 2.8.23 include bug fixes and logging of
bad memory access addresses. For more information, see [Redis OSS 2.8 release notes](https://github.com/redis/redis/blob/2.8/00-RELEASENOTES "https://github.com/redis/redis/blob/2.8/00-RELEASENOTES").

#### ElastiCache version 2.8.23 for Redis OSS (enhanced)

Redis OSS improvements added since version 2.8.22 include bug fixes. For more
information, see [Redis OSS 2.8 release notes](https://github.com/redis/redis/blob/2.8/00-RELEASENOTES "https://github.com/redis/redis/blob/2.8/00-RELEASENOTES"). This release also includes support for the
new parameter `close-on-slave-write` which, if enabled, disconnects
clients who attempt to write to a read-only replica.

For more information on Redis OSS 2.8.23 parameters, see [Redis OSS 2.8.23 (enhanced) added parameters](ParameterGroups.md#ParameterGroups.Redis.2-8-23 "ParameterGroups.md#ParameterGroups.Redis.2-8-23") in the ElastiCache User
Guide.

#### ElastiCache version 2.8.22 for Redis OSS (enhanced)

Redis OSS improvements added since version 2.8.21 include the following:

- Support for forkless backups and synchronizations, which allows you to
  allocate less memory for backup overhead and more for your application.
  For more information, see [How synchronization and backup are implemented](Replication.Redis.md "Replication.Redis.md"). The forkless process
  can impact both latency and throughput. When there is high write
  throughput, when a replica re-syncs, it can be unreachable for the
  entire time it is syncing.
- If there is a failover, replication groups now recover faster because
  replicas perform partial syncs with the primary rather than full syncs
  whenever possible. Additionally, both the primary and replicas no longer
  use the disk during syncs, providing further speed gains.
- Support for two new CloudWatch metrics.
  - `ReplicationBytes` – The number of bytes a
    replication group's primary cluster is sending to the read
    replicas.
  - `SaveInProgress` – A binary value that
    indicates whether or not there is a background save process
    running.
    For more information, see [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md").

- A number of critical bug fixes in replication PSYNC behavior. For more
  information, see [Redis OSS 2.8 release notes](https://github.com/redis/redis/blob/2.8/00-RELEASENOTES "https://github.com/redis/redis/blob/2.8/00-RELEASENOTES").
- To maintain enhanced replication performance in Multi-AZ replication
  groups and for increased cluster stability, non-ElastiCache replicas are no
  longer supported.
- To improve data consistency between the primary cluster and replicas
  in a replication group, the replicas no longer evict keys independent of
  the primary cluster.
- Redis OSS configuration variables `appendonly` and
  `appendfsync` are not supported on Redis OSS version 2.8.22
  and later.
- In low-memory situations, clients with a large output buffer might be
  disconnected from a replica cluster. If disconnected, the client needs
  to reconnect. Such situations are most likely to occur for PUBSUB
  clients.

#### ElastiCache version 2.8.21 for Redis OSS

Redis OSS improvements added since version 2.8.19 include a number of bug fixes.
For more information, see [Redis OSS 2.8 release notes](https://github.com/redis/redis/blob/2.8/00-RELEASENOTES "https://github.com/redis/redis/blob/2.8/00-RELEASENOTES").

#### ElastiCache version 2.8.19 for Redis OSS

Redis OSS improvements added since version 2.8.6 include the following:

- Support for HyperLogLog. For more information, see [Redis OSS new data structure:
  HyperLogLog](http://antirez.com/news/75 "http://antirez.com/news/75").
- The sorted set data type now has support for lexicographic range
  queries with the new commands `ZRANGEBYLEX`,
  `ZLEXCOUNT`, and `ZREMRANGEBYLEX`.
- To prevent a primary node from sending stale data to replica nodes,
  the master SYNC fails if a background save (`bgsave`) child
  process is aborted.
- Support for the _HyperLogLogBasedCommands_ CloudWatch
  metric. For more information, see [Metrics for Valkey and Redis OSS](CacheMetrics.md "CacheMetrics.md").

#### ElastiCache version 2.8.6 for Redis OSS

Redis OSS improvements added since version 2.6.13 include the following:

- Improved resiliency and fault tolerance for read replicas.
- Support for partial resynchronization.
- Support for user-defined minimum number of read replicas that must be
  available at all times.
- Full support for pub/sub—notifying clients of events on the
  server.
- Automatic detection of a primary node failure and failover of your
  primary node to a secondary node.

#### ElastiCache version 2.6.13 for Redis OSS

ElastiCache version 2.6.13 for Redis OSS was the initial version of ElastiCache that supported Redis OSS.
Multi-AZ is not supported on ElastiCache version 2.6.13 for Redis OSS.

## ElastiCache versions for Redis OSS end of life schedule

This section defines end of life (EOL) dates for older major versions as they are
announced. This allows you to make version and upgrade decisions for the future.

###### Note

ElastiCache versions from 5.0.0 to 5.0.5 for Redis OSS are deprecated. Use versions 5.0.6 or
greater.

The following table shows the schedule of [Extended Support](extended-support.md "extended-support.md") for ElastiCache for Redis OSS engines.

**Extended Support and End of Life schedule**

| Major Engine Version | End of Standard Support | Start of Extended Support Y1 Premium | Start of Extended Support Y2 Premium | Start of Extended Support Y3 Premium | End of Extended Support and version EOL |
| -------------------- | ----------------------- | ------------------------------------ | ------------------------------------ | ------------------------------------ | --------------------------------------- |
| Redis OSS v4         | 1/31/2026               | 2/1/2026                             | 2/1/2027                             | 2/1/2028                             | 1/31/2029                               |
| Redis OSS v5         | 1/31/2026               | 2/1/2026                             | 2/1/2027                             | 2/1/2028                             | 1/31/2029                               |
| Redis OSS v6         | 1/31/2027               | 2/1/2027                             | 2/1/2028                             | 2/1/2029                             | 1/31/2030                               |

The following table summarizes each version and its announced EOL date, as well as the recommended upgrade target version.

**Past EOL**

| Source Major Version | Source Minor Versions                                            | Recommended Upgrade Target                                                                                                  | EOL Date         |
| -------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Version 3            | 3.2.4, 3.2.6 and 3.2.10                                          | Version 6.2 or higher<br>NoteFor US-ISO-EAST-1, US-ISO-WEST-1, and US-ISOB-EAST-1 Regions,<br>we recommend 5.0.6 or higher. | July 31, 2023    |
| Version 2            | 2.8.24, 2.8.23, 2.8.22, 2.8.21, 2.8.19, 2.8.12, 2.8.6,<br>2.6.13 | Version 6.2 or higher<br>NoteFor US-ISO-EAST-1, US-ISO-WEST-1, and US-ISOB-EAST-1 Regions,<br>we recommend 5.0.6 or higher. | January 13, 2023 |

## Supported ElastiCache for Memcached versions

ElastiCache supports the following Memcached versions and upgrading to newer versions. When
upgrading to a newer version, pay careful attention to the conditions that if not met
cause your upgrade to fail.

###### ElastiCache for Memcached Versions

- [ElastiCache version 1.6.22 for Memcached](#memcached-version-1-6-22 "#memcached-version-1-6-22")
- [ElastiCache version 1.6.17 for Memcached](#memcached-version-1-6-17 "#memcached-version-1-6-17")
- [ElastiCache version 1.6.12 for Memcached](#memcached-version-1-6-12 "#memcached-version-1-6-12")
- [ElastiCache version 1.6.6 for Memcached](#memcached-version-1-6-6 "#memcached-version-1-6-6")
- [ElastiCache version 1.5.16 for Memcached](#memcached-version-1-5-16 "#memcached-version-1-5-16")
- [ElastiCache version 1.5.10 for Memcached](#memcached-version-1-5-10 "#memcached-version-1-5-10")
- [ElastiCache version 1.4.34 for Memcached](#memcached-version-1-4-34 "#memcached-version-1-4-34")
- [ElastiCache version 1.4.33 for Memcached](#memcached-version-1-4-33 "#memcached-version-1-4-33")
- [ElastiCache version 1.4.24 for Memcached](#memcached-version-1-4-24 "#memcached-version-1-4-24")
- [ElastiCache version 1.4.14 for Memcached](#memcached-version-1-4-14 "#memcached-version-1-4-14")
- [ElastiCache version 1.4.5 for Memcached](#memcached-version-1-4-5 "#memcached-version-1-4-5")

### ElastiCache version 1.6.22 for Memcached

ElastiCache for Memcached version 1.6.22 for Memcached adds support for Memcached version 1.6.22. It includes no new features, but
does include bug fixes and cumulative updates from [Memcached
1.6.18](https://github.com/memcached/memcached/wiki/ReleaseNotes1618 "https://github.com/memcached/memcached/wiki/ReleaseNotes1618").

For more information, see [ReleaseNotes1622](https://github.com/memcached/memcached/wiki/ReleaseNotes1622 "https://github.com/memcached/memcached/wiki/ReleaseNotes1622") at Memcached on GitHub.

### ElastiCache version 1.6.17 for Memcached

ElastiCache for Memcached version 1.6.17 for Memcached adds support for Memcached engine version 1.6.17. It includes no new features, but
does include bug fixes and cumulative updates from [Memcached
1.6.17](https://github.com/memcached/memcached/wiki/ReleaseNotes1617 "https://github.com/memcached/memcached/wiki/ReleaseNotes1617").

For more information, see [ReleaseNotes1617](https://github.com/memcached/memcached/wiki/ReleaseNotes1617 "https://github.com/memcached/memcached/wiki/ReleaseNotes1617") at Memcached on GitHub.

### ElastiCache version 1.6.12 for Memcached

ElastiCache for Memcached version 1.6.12 for Memcached adds support for Memcached engine 1.6.12 and encryption in-transit. It
also includes bug fixes and cumulative updates from [Memcached
1.6.6](https://github.com/memcached/memcached/wiki/ReleaseNotes166 "https://github.com/memcached/memcached/wiki/ReleaseNotes166").

For more information, see [ReleaseNotes1612](https://github.com/memcached/memcached/wiki/ReleaseNotes1612 "https://github.com/memcached/memcached/wiki/ReleaseNotes1612") at Memcached on GitHub.

### ElastiCache version 1.6.6 for Memcached

ElastiCache for Memcached version 1.6.6 for Memcached adds support for Memcached version 1.6.6. It includes no new features, but
does include bug fixes and cumulative updates from [Memcached
1.5.16](https://github.com/memcached/memcached/wiki/ReleaseNotes1.5.16 "https://github.com/memcached/memcached/wiki/ReleaseNotes1.5.16"). ElastiCache for Memcached does not include support for [Extstore](https://memcached.org/extstore "https://memcached.org/extstore").

For more information, see [ReleaseNotes166](https://github.com/memcached/memcached/wiki/ReleaseNotes166 "https://github.com/memcached/memcached/wiki/ReleaseNotes166") at Memcached on GitHub.

### ElastiCache version 1.5.16 for Memcached

ElastiCache version 1.5.16 for Memcached adds support for Memcached version 1.5.16. It includes no new
features, but does include bug fixes and cumulative updates from [Memcached
1.5.14](https://github.com/memcached/memcached/wiki/ReleaseNotes1514 "https://github.com/memcached/memcached/wiki/ReleaseNotes1514") and [Memcached
1.5.15](https://github.com/memcached/memcached/wiki/ReleaseNotes1515 "https://github.com/memcached/memcached/wiki/ReleaseNotes1515").

For more information, see [Memcached
1.5.16 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1516 "https://github.com/memcached/memcached/wiki/ReleaseNotes1516") at Memcached on GitHub.

### ElastiCache version 1.5.10 for Memcached

ElastiCache version 1.5.10 for Memcached supports the following Memcached
features:

- Automated slab rebalancing.
- Faster hash table lookups with `murmur3` algorithm.
- Segmented LRU algorithm.
- LRU crawler to background-reclaim memory.
- `--enable-seccomp`: A compile-time option.

It also introduces the `no_modern` and `inline_ascii_resp`
parameters. For more information, see [Memcached 1.5.10 parameter changes](ParameterGroups.md#ParameterGroups.Memcached.1-5-10 "ParameterGroups.md#ParameterGroups.Memcached.1-5-10").

Memcached improvements added since ElastiCache version 1.4.34 for Memcached
include the following:

- Cumulative fixes, such as ASCII multigets, CVE-2017-9951 and limit crawls
  for `metadumper`.
- Better connection management by closing connections at the connection
  limit.
- Improved item-size management for item size above 1MB.
- Better performance and memory-overhead improvements by reducing memory
  requirements per-item by a few bytes.

For more information, see [Memcached 1.5.10 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1510 "https://github.com/memcached/memcached/wiki/ReleaseNotes1510") at Memcached on GitHub.

### ElastiCache version 1.4.34 for Memcached

ElastiCache version 1.4.34 for Memcached adds no new features to version 1.4.33. Version
1.4.34 is a bug fix release that is larger than the usual such release.

For more information, see [Memcached
1.4.34 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1434 "https://github.com/memcached/memcached/wiki/ReleaseNotes1434") at Memcached on GitHub.

### ElastiCache version 1.4.33 for Memcached

Improvements added since version 1.4.24 include the following:

- Ability to dump all of the metadata for a particular slab class, a list of
  slab classes, or all slab classes. For more information, see [Memcached 1.4.31 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1431 "https://github.com/memcached/memcached/wiki/ReleaseNotes1431").
- Improved support for large items over the 1 megabyte default. For more
  information, see [Memcached 1.4.29 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1429 "https://github.com/memcached/memcached/wiki/ReleaseNotes1429").
- Ability to specify how long a client can be idle before being asked to
  close.

Ability to dynamically increase the amount of memory available to
Memcached without having to restart the cluster. For more information, see
[Memcached 1.4.27 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1427 "https://github.com/memcached/memcached/wiki/ReleaseNotes1427").

- Logging of `fetchers`, `mutations`, and
  `evictions` are now supported. For more information, see
  [Memcached 1.4.26 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1426 "https://github.com/memcached/memcached/wiki/ReleaseNotes1426").
- Freed memory can be reclaimed back into a global pool and reassigned to
  new slab classes. For more information, see [Memcached 1.4.25 Release Notes](https://github.com/memcached/memcached/wiki/ReleaseNotes1425 "https://github.com/memcached/memcached/wiki/ReleaseNotes1425").
- Several bug fixes.
- Some new commands and parameters. For a list, see [Memcached 1.4.33 added parameters](ParameterGroups.md#ParameterGroups.Memcached.1-4-33 "ParameterGroups.md#ParameterGroups.Memcached.1-4-33").

### ElastiCache version 1.4.24 for Memcached

Improvements added since version 1.4.14 include the following:

- Least recently used (LRU) management using a background process.
- Added the option of using _jenkins_ or
  _murmur3_ as your hash algorithm.
- Some new commands and parameters. For a list, see [Memcached 1.4.24 added parameters](ParameterGroups.md#ParameterGroups.Memcached.1-4-24 "ParameterGroups.md#ParameterGroups.Memcached.1-4-24").
- Several bug fixes.

### ElastiCache version 1.4.14 for Memcached

Improvements added since version 1.4.5 include the following:

- Enhanced slab rebalancing capability.
- Performance and scalability improvement.
- Introduced the _touch_ command to update the expiration
  time of an existing item without fetching it.
- Auto discovery—the ability for client programs to automatically
  determine all of the cache nodes in a cluster, and to initiate and maintain
  connections to all of these nodes.

### ElastiCache version 1.4.5 for Memcached

ElastiCache version 1.4.5 for Memcached was the initial engine and version supported by
Amazon ElastiCache for Memcached.
