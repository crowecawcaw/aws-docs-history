# Engine versions

This section covers the supported Valkey and Redis OSS engine versions.

###### Topics

- [MemoryDB version 7.3](#engine-version-7.3 "#engine-version-7.3")
- [MemoryDB version 7.2.6](#valkey-version-7.2.6 "#valkey-version-7.2.6")
- [MemoryDB version 7.1 (enhanced)](#engine-version-7.1 "#engine-version-7.1")
- [MemoryDB version 7.0 (enhanced)](#engine-version-7.0 "#engine-version-7.0")
- [MemoryDB with Redis OSS version 6.2 (enhanced)](#engine-version-6-x "#engine-version-6-x")
- [Upgrading engine versions](#versionmanagement "#versionmanagement")

## MemoryDB version 7.3

On December 1 2024, MemoryDB 7.3 was released. MemoryDB version 7.3 supports Multi-Region clusters, enabling you build multi-Region applications with up to 99.999% availability with extremely low latency.
MemoryDB Multi-Region is currently supported in the following AWS Regions: US East (N. Virginia and Ohio), US West (Oregon, N. California), Europe (Ireland, Frankfurt, and London), and Asia Pacific (Tokyo, Sydney, Mumbai, Seoul and Singapore). For more information see [MemoryDB Multi-Region](multi-region.md "multi-region.md").

## MemoryDB version 7.2.6

On October 8 2024, Valkey 7.2.6 was released. Valkey 7.2.6 has similar compatibility differences with previous versions of Redis OSS 7.2.5. Here are the main differences between Valkey and Redis OSS 7.0 and 7.1:

- New WITHSCORE option for ZRANK and ZREVRANK commands
- CLIENT NO-TOUCH for clients to run commands without affecting LRU/LFU of keys.
- New command CLUSTER MYSHARDID that returns the Shard ID of the node to logically group nodes in cluster mode based on replication.
- Performance and memory optimizations for various data types.

Here are the potentially breaking behavior changes between Valkey 7.2 and Redis OSS 7.1 (or 7.0):

- When calling PUBLISH with a RESP3 client that's also subscribed to the same channel,
  the order is changed and the reply is sent before the published message.
- Client side tracking for scripts now tracks the keys that are read by the
  script, instead of the keys that are declared by the caller of EVAL / FCALL.
- Freeze time sampling occurs during command execution and in scripts.
- When a blocked command is being unblocked, checks such as ACL, OOM, and others are
  re-evaluated.
- ACL failure error message text and error codes are unified.
- A blocked stream command that's released when key no longer exists carries a different error code (-NOGROUP or -WRONGTYPE instead of -UNBLOCKED).
- The command stats are updated for blocked commands only when the command
  actually executes.
- The internal storage of ACL users no longer removes redundant command
  and category rules. This may alter the way those rules are displayed as part
  of ACL SAVE, ACL GETUSER and ACL LIST.
- Any client connections created for TLS-based replication use SNI if possible.
- XINFO STREAM: The seen-time response field now denotes the last attempted interaction instead of the last successful interaction. The new active-time response field now denotes the last successful interaction.
- XREADGROUP and X[AUTO]CLAIM create the consumer regardless of whether it was
  able to perform some reading/claiming.
- ACL default newly created user set sanitize-payload flag in ACL LIST/GETUSER.
- The HELLO command does not affect the client state unless successful.
- NAN replies are normalized to a single nan type, similar to the current behavior of inf.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 7.2 release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES")
(Valkey 7.2 includes all changes from Redis OSS up to version 7.2.4) and [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES") at Valkey on GitHub.

## MemoryDB version 7.1 (enhanced)

MemoryDB version 7.1 adds support for vector search capabilities in all Regions, as well as
critical bug fixes and performance enhancements.

- **[Vector Search Feature:](vector-search.md "vector-search.md")**
  Vector search can be used with existing MemoryDB functionality. Applications which don't use vector search won't be affected by its presence.
  Vector search is available in MemoryDB version 7.1 onward in in all Regions.
  Please refer to the documentation [here](vector-search.md "vector-search.md") for further information.

###### Note

MemoryDB version 7.1 is compatible with Redis OSS v7.0. For more information on the Redis OSS 7.0 release,
see [Redis OSS 7.0 Release Notes](https://raw.githubusercontent.com/antirez/redis/7.0/00-RELEASENOTES "https://raw.githubusercontent.com/antirez/redis/7.0/00-RELEASENOTES") at Redis OSS on GitHub.

## MemoryDB version 7.0 (enhanced)

MemoryDB 7.0 adds a number of improvements and support for new functionality:

- [Functions](https://valkey.io/docs/topics/functions-intro/ "https://valkey.io/docs/topics/functions-intro/"): MemoryDB 7 adds support for Functions, and provides a managed
  experience enabling developers to execute [LUA scripts](https://valkey.io/docs/manual/programmability/eval-intro/ "https://valkey.io/docs/manual/programmability/eval-intro/")
  with application logic stored on the MemoryDB cluster, without requiring clients to
  re-send the scripts to the server with every connection.
- [ACL
  improvements](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/"): MemoryDB 7 adds support for the next version
  of Access Control Lists (ACLs). With MemoryDB OSS Valkey 7 or Redis OSS 7, clients can
  now specify multiple sets of permissions on specific keys or keyspaces.
- [Sharded Pub/Sub](https://valkey.io/topics/pubsub/ "https://valkey.io/topics/pubsub/"):
  MemoryDB 7 adds support to run Pub/Sub functionality in a sharded way when running
  MemoryDB in Cluster Mode Enabled (CME). Pub/Sub capabilities enable publishers to
  issue messages to any number of subscribers on a channel. With Amazon MemoryDB Valkey 7 and Redis OSS 7
  channels are bound to a shard in the MemoryDB cluster, eliminating the need to propagate
  channel information across shards. This results in improved scalability.
- Enhanced I/O multiplexing: MemoryDB Valkey 7 and Redis OSS version 7 introduces enhanced I/O
  multiplexing, which delivers increased throughput and reduced latency for high-throughput
  workloads that have many concurrent client connections to an MemoryDB cluster.
  For example, when using a cluster of r6g.4xlarge nodes and running 5200 concurrent clients, you can achieve up to 46% increased throughput (read and write operations per second) and up to 21% decreased P99 latency, compared with MemoryDB version 6.

For more information on Valkey, see [Valkey](https://valkey.io/ "https://valkey.io/")

For more information on the Valkey 7.2 release, see [Redis OSS 7.2.4 Release Notes](https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/d2c8a4b91e8c0e6aefd1f5bc0bf582cddbe046b7/00-RELEASENOTES")
(Valkey 7.2 includes all changes from Redis OSS up to version 7.2.4) and [Valkey 7.2 release notes](https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES "https://github.com/valkey-io/valkey/blob/7.2/00-RELEASENOTES") at Valkey on GitHub.

## MemoryDB with Redis OSS version 6.2 (enhanced)

MemoryDB introduces the next version of the Redis OSS engine, which includes
[Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md"), automatic version upgrade support, client-side caching and significant operational improvements.

Redis engine version 6.2.6 also introduces support for native JavaScript Object Notation (JSON) format, a simple, schemaless way to encode complex datasets
inside Redis OSS clusters. With JSON support, you can leverage the performance and Redis OSS APIs for applications that operate over JSON.
For more information, see [Getting started with JSON](json-gs.md "json-gs.md").
Also included is JSON-related metric `JsonBasedCmds` that is incorporated into CloudWatch to monitor the usage of this datatype. For more information,
see [Metrics for MemoryDB](metrics.md "metrics.md").

With Redis OSS 6, MemoryDB will offer a single version for each Redis OSS minor release, rather than offering multiple patch versions.
This is designed to minimize confusion and ambiguity on having to choose from multiple minor versions.
MemoryDB will also automatically manage the minor and patch version of your running clusters, ensuring improved performance and enhanced security. This will be handled
through standard customer-notification channels via a service update campaign. For more information, see [Service updates in MemoryDB](service-updates.md "service-updates.md").

If you do not specify the engine version during creation, MemoryDB will automatically select the preferred Redis OSS version for you.
On the other hand, if you specify the engine version by using `6.2`, MemoryDB will automatically invoke the preferred patch version of Redis OSS 6.2 that is available.

For example, when you create a cluster, you set the `--engine-version` parameter to `6.2`.
The cluster will be launched with the current available preferred patch version at the creation time.

Any request with a full engine version value will be rejected, an exception will be thrown and the process will fail.

When calling the `DescribeEngineVersions` API, the `EngineVersion` parameter value will be set to 6.2
and the actual full engine version will be returned in the `EnginePatchVersion` field.

For more information on the Redis OSS 6.2 release, see [Redis 6.2 Release Notes](https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES "https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES") at Redis OSS on GitHub.

## Upgrading engine versions

MemoryDB by default automatically manages the patch version of your running clusters through service updates.
You can additionally opt out from auto minor version upgrade if you set the `AutoMinorVersionUpgrade` property of your clusters to false.
However, you can not opt out from auto patch version upgrade.

You can control if and when the protocol-compliant software powering your cluster is
upgraded to new versions that are supported by MemoryDB before auto upgrade starts. This level of control enables you
to maintain compatibility with specific versions, test new versions
with your application before deploying in production, and perform version upgrades on
your own terms and timelines.

You can also upgrade from an existing MemoryDB with Redis OSS engine to a Valkey engine.

You can initiate engine version upgrades to your cluster in the following ways:

- By updating it
  and specifying a new engine version. For more information, see [Modifying a MemoryDB cluster](clusters.md "clusters.md").
- Applying the service update for the corresponding engine version. For more information, see [Service updates in MemoryDB](service-updates.md "service-updates.md").

Note the following:

- You can upgrade to a newer engine version, but you can't downgrade to an older engine
  version. If you want to use an older engine version, you must delete the
  existing cluster and create it anew with the older engine version.
- We recommend periodically upgrading to the latest major version, since most major improvements are not back ported to older versions.
  As MemoryDB expands availability to a new AWS Region, MemoryDB supports the two most recent `MAJOR.MINOR` versions at that time for the new Region.
  For example, if a new AWS region launches and the latest `MAJOR.MINOR` MemoryDB versions are 7.0 and 6.2, MemoryDB will support
  versions 7.0 and 6.2 in the new AWS Region. As newer `MAJOR.MINOR` versions of MemoryDB are released,
  MemoryDB will continue to add support for the newly released MemoryDB versions. To learn more about choosing Regions for MemoryDB, see
  [Supported Regions & endpoints](regionsandazs.md#supportedregions "regionsandazs.md#supportedregions").
- Engine version management is designed so that you can have as much control as possible over
  how patching occurs. However, MemoryDB reserves the right to patch your cluster
  on your behalf in the unlikely event of a critical security vulnerability in
  the system or software.
- MemoryDB will offer a single version for each Valkey or Redis OSS minor release, rather than offering multiple patch versions. This is designed to minimize confusion and ambiguity on having to choose from multiple versions.
  MemoryDB will also automatically manage the minor and patch version of your running clusters, ensuring improved performance and enhanced security. This will be handled
  through standard customer-notification channels via a service update campaign.
  For more information, see [Service updates in MemoryDB](service-updates.md "service-updates.md").
- You can upgrade your cluster version with minimal downtime.
  The cluster is available for reads during the entire upgrade and is available for writes for most of the upgrade duration, except during the failover operation which lasts a few seconds.
- We recommend that you perform engine
  upgrades during periods of low incoming write traffic.

Clusters with multiple shards are processed and patched as follows:

    + Only one upgrade operation is performed
     per shard at any time.
    + In each shard, all replicas are processed before the primary is processed. If there are
     fewer replicas in a shard, the primary in that shard might be
     processed before the replicas in other shards are finished
     processing.
    + Across all the shards, primary nodes are processed in series.
     Only one primary node is upgraded at a time.

###### Topics

- [How to upgrade engine versions](#versionmanagement.howto "#versionmanagement.howto")
- [Resolving blocked Redis OSS engine upgrades](#resolving-blocked-engine-upgrades "#resolving-blocked-engine-upgrades")

### How to upgrade engine versions

You initiate version upgrades to your cluster by modifying it
using the MemoryDB console, the AWS CLI, or the MemoryDB API and specifying a newer
engine version. For more information, see the following topics.

- [Using the AWS Management Console](clusters.md#clusters.modifyclusters.viewdetails "clusters.md#clusters.modifyclusters.viewdetails")
- [Using the AWS CLI](clusters.md#clusters.modify.cli "clusters.md#clusters.modify.cli")
- [Using the MemoryDB API](clusters.md#clusters.modify.api "clusters.md#clusters.modify.api")

### Resolving blocked Redis OSS engine upgrades

As shown in the following table,
your Redis OSS engine upgrade operation is blocked if you have a pending scale up operation.

| Pending operations          | Blocked operations       |
| --------------------------- | ------------------------ |
| Scale up                    | Immediate engine upgrade |
| Engine upgrade              | Immediate scale up       |
| Scale up and engine upgrade | Immediate scale up       |
| Immediate engine upgrade    |
