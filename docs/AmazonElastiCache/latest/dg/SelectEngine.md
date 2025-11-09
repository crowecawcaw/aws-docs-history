# Comparing node-based Valkey, Memcached, and Redis OSS clusters

Amazon ElastiCache supports the Valkey, Memcached, and Redis OSS cache engines. Each engine provides some
advantages. Use the information in this topic to help you choose the engine and version that
best meets your requirements.

###### Important

After you create a cache, node-based cluster or replication group, you can upgrade to a
newer engine version, but you cannot downgrade to an older engine version. If you want to use an
older engine version, you must delete the existing cache, node-based cluster or replication group
and create it again with the earlier engine version.

On the surface, the engines look similar. Each of them is an in-memory key-value store.
However, in practice there are significant differences.

###### Choose Memcached if the following apply for you:

- You need the simplest model possible.
- You need to run large nodes with multiple cores or threads.
- You need the ability to scale out and in, adding and removing nodes as demand on your
  system increases and decreases.
- You need to cache objects.

###### Choose Valkey or Redis OSS with ElastiCache if the following apply for you:

- **ElastiCache version 7.2 for Valkey or version 7.0 (Enhanced) for Redis OSS**

You want to use [Functions](https://valkey.io/topics/functions-intro/ "https://valkey.io/topics/functions-intro/"),
[Sharded Pub/Sub](https://valkey.io/topics/pubsub/ "https://valkey.io/topics/pubsub/"), or
[ACL improvements](https://valkey.io/topics/acl/ "https://valkey.io/topics/acl/"). For more information,
see [Redis OSS Version 7.0 (Enhanced)](engine-versions.md#redis-version-7.0 "engine-versions.md#redis-version-7.0").

- **ElastiCache version 6.2 (Enhanced) for Redis OSS**

You want the ability to tier data between memory and SSD using the r6gd node type. For more information, see
[Data tiering](data-tiering.md "data-tiering.md").

- **ElastiCache version 6.0 (Enhanced) for Redis OSS**

You want to authenticate users with role-based access control.

For more information, see [Redis OSS Version 6.0 (Enhanced)](engine-versions.md#redis-version-6.0 "engine-versions.md#redis-version-6.0").

- **ElastiCache version 5.0.0 (Enhanced) for Redis OSS**

You want to use [Redis OSS streams](https://redis.io/topics/streams-intro "https://redis.io/topics/streams-intro"), a log data structure that allows producers to append new items in real time and also allows consumers to consume messages either in a blocking or non-blocking fashion.

For more information, see [Redis OSS Version 5.0.0 (Enhanced)](engine-versions.md#redis-version-5-0 "engine-versions.md#redis-version-5-0").

- **ElastiCache version 4.0.10 (Enhanced) for Redis OSS**

Supports both encryption and dynamically adding or removing shards from your Valkey or Redis OSS (cluster mode enabled) cluster.

For more information, see [Redis OSS Version 4.0.10 (Enhanced)](engine-versions.md#redis-version-4-0-10 "engine-versions.md#redis-version-4-0-10").
The following versions are deprecated, have reached or soon to reach end of life.

- **ElastiCache version 3.2.10 (Enhanced) for Redis OSS**

Supports the ability to dynamically add or remove shards from your Valkey or Redis OSS (cluster mode enabled) cluster.

###### Important

Currently ElastiCache 3.2.10 for Redis OSS doesn't support encryption.

For more information, see the following:

    + [Redis OSS Version 3.2.10 (Enhanced)](engine-versions.md#redis-version-3-2-10 "engine-versions.md#redis-version-3-2-10")
    + Online resharding best practices for Redis OSS, For more information, see the following:




    	- [Best Practices: Online Resharding](best-practices-online-resharding.md "best-practices-online-resharding.md")
    	- [Online Resharding and Shard Rebalancing for Valkey or Redis OSS (Cluster Mode Enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online")
    + For more information on scaling Redis OSS clusters, see [Scaling](Scaling.md "Scaling.md").

- **ElastiCache version 3.2.6 (Enhanced) for Redis OSS**

If you need the functionality of earlier Redis OSS versions plus the following features,
choose 3.2.6:

    + In-transit encryption. For more information, see [Amazon ElastiCache for Redis OSS In-Transit Encryption](in-transit-encryption.md "in-transit-encryption.md").
    + At-rest encryption. For more information, see [Amazon ElastiCache for Redis OSS At-Rest Encryption](at-rest-encryption.md "at-rest-encryption.md").

- **ElastiCache (Cluster mode enabled) version 3.2.4 for Redis OSS**

If you need the functionality of 2.8.x plus the following features, choose 3.2.4 (clustered mode):

    + You need to partition your data across two to 500 node groups (clustered mode
     only).
    + You need geospatial indexing (clustered mode or non-clustered mode).
    + You don't need to support multiple databases.

- **ElastiCache (non-clustered mode) 2.8.x and 3.2.4 (Enhanced) for Redis OSS**

If the following apply for you, 2.8.x or 3.2.4 (non-clustered mode):

    + You need complex data types, such as strings, hashes, lists, sets, sorted sets, and bitmaps.
    + You need to sort or rank in-memory datasets.
    + You need persistence of your key store.
    + You need to replicate your data from the primary to one or more read replicas for read intensive
     applications.
    + You need automatic failover if your primary node fails.
    + You need publish and subscribe (pub/sub) capabilities—to inform
     clients about events on the server.
    + You need backup and restore capabilities for node-based clusters as well as serverless
    caches.
    + You need to support multiple databases.

| Comparison summary of Memcached, Valkey or Redis OSS (cluster mode disabled), and Valkey or Redis OSS (cluster mode enabled) |                                                                   | Memcached                                                | Valkey or Redis OSS (cluster mode disabled)              | Valkey or Redis OSS (cluster mode enabled) |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------ |
| Engine versions+                                                                                                             | 1.4.5 and later                                                   | 4.0.10 and later                                         | 4.0.10 and later                                         |
| Data types                                                                                                                   | Simple ‡                                                          | 2.8.x<br>• Complex \*                                    | 3.2.x and later<br>• Complex †                           |
| Complex †                                                                                                                    |
| Data partitioning                                                                                                            | Yes                                                               | No                                                       | Yes                                                      |
| Cluster is modifiable                                                                                                        | Yes                                                               | Yes                                                      | 3.2.10 and later<br>• Limited                            |
| Online resharding                                                                                                            | No                                                                | No                                                       | 3.2.10 and later                                         |
| Encryption                                                                                                                   | in-transit 1.6.12 and later                                       | 4.0.10 and later                                         | 4.0.10 and later                                         |
| Data tiering                                                                                                                 | No                                                                | 6.2 and later                                            | 6.2 and later                                            |
| Compliance certifications                                                                                                    |
| Compliance Certification<br>FedRAMP<br>HIPAA<br>PCI DSS                                                                      | Yes<br>• 1.6.12 and later<br>Yes<br>• 1.6.12 and later<br>Yes     | 4.0.10 and later<br>4.0.10 and later<br>4.0.10 and later | 4.0.10 and later<br>4.0.10 and later<br>4.0.10 and later |
| Multi-threaded                                                                                                               | Yes                                                               | No                                                       | No                                                       |
| Node type upgrade                                                                                                            | No                                                                | Yes                                                      | Yes                                                      |
| Engine upgrading                                                                                                             | Yes                                                               | Yes                                                      | Yes                                                      |
| High availability (replication)                                                                                              | No                                                                | Yes                                                      | Yes                                                      |
| Automatic failover                                                                                                           | No                                                                | Optional                                                 | Required                                                 |
| Pub/Sub capabilities                                                                                                         | No                                                                | Yes                                                      | Yes                                                      |
| Sorted sets                                                                                                                  | No                                                                | Yes                                                      | Yes                                                      |
| Backup and restore                                                                                                           | For serverless caches only, not applicable to node-based clusters | Yes                                                      | Yes                                                      |
| Geospatial indexing                                                                                                          | No                                                                | 4.0.10 and later                                         | Yes                                                      |
| **Notes:**                                                                                                                   |
| ‡ string, objects (like databases)                                                                                           |
| \<br>• string, sets, sorted sets, lists, hashes, bitmaps, hyperloglog                                                        |
| † string, sets, sorted sets, lists, hashes, bitmaps,<br>hyperloglog, geospatial indexes                                      |
| + Excludes versions which are deprecated, have reached or soon to reach end of life.                                         |

After you choose the engine for your cluster, we recommend that you use the most recent
version of that engine. For more information, see [Supported node types](CacheNodes.md "CacheNodes.md").
