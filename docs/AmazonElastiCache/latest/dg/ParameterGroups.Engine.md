# Engine specific parameters

**Valkey and Redis OSS**

Most Valkey 8 parameters are compatible with Redis OSS 7.1 parameters. Valkey 7.2 parameters are the same as Redis OSS 7 parameters.

If you do not specify a parameter group for your Valkey or Redis OSS cluster, then a default
parameter group appropriate to your engine version will be used. You can't change the
values of any parameters in the default parameter group. However, you can create a
custom parameter group and assign it to your cluster at any time as long as the values
of conditionally modifiable parameters are the same in both parameter groups. For more
information, see [Creating an ElastiCache parameter group](ParameterGroups.Creating.md "ParameterGroups.Creating.md").

###### Topics

- [Valkey and Redis OSS parameters](#ParameterGroups.Redis "#ParameterGroups.Redis")
- [Memcached specific parameters](#ParameterGroups.Memcached "#ParameterGroups.Memcached")

## Valkey and Redis OSS parameters

###### Topics

- [Valkey 9.1 and Valkey 9.0 parameter changes](#ParameterGroups.Valkey.9.0 "#ParameterGroups.Valkey.9.0")
- [Valkey 8.2 parameter changes](#ParameterGroups.Valkey.8.2 "#ParameterGroups.Valkey.8.2")
- [Valkey 8.1 parameter changes](#ParameterGroups.Valkey.8.1 "#ParameterGroups.Valkey.8.1")
- [Valkey 8.0 parameter changes](#ParameterGroups.Valkey.8 "#ParameterGroups.Valkey.8")
- [Valkey 7.2 and Redis OSS 7 parameter changes](#ParameterGroups.Redis.7 "#ParameterGroups.Redis.7")
- [Redis OSS 6.x parameter changes](#ParameterGroups.Redis.6-x "#ParameterGroups.Redis.6-x")
- [Redis OSS 5.0.3 parameter changes](#ParameterGroups.Redis.5-0-3 "#ParameterGroups.Redis.5-0-3")
- [Redis OSS 5.0.0 parameter changes](#ParameterGroups.Redis.5.0 "#ParameterGroups.Redis.5.0")
- [Redis OSS 4.0.10 parameter changes](#ParameterGroups.Redis.4-0-10 "#ParameterGroups.Redis.4-0-10")
- [Redis OSS 3.2.10 parameter changes](#ParameterGroups.Redis.3-2-10 "#ParameterGroups.Redis.3-2-10")
- [Redis OSS 3.2.6 parameter changes](#ParameterGroups.Redis.3-2-6 "#ParameterGroups.Redis.3-2-6")
- [Redis OSS 3.2.4 parameter changes](#ParameterGroups.Redis.3-2-4 "#ParameterGroups.Redis.3-2-4")
- [Redis OSS 2.8.24 (enhanced) added parameters](#ParameterGroups.Redis.2-8-24 "#ParameterGroups.Redis.2-8-24")
- [Redis OSS 2.8.23 (enhanced) added parameters](#ParameterGroups.Redis.2-8-23 "#ParameterGroups.Redis.2-8-23")
- [Redis OSS 2.8.22 (enhanced) added parameters](#ParameterGroups.Redis.2-8-22 "#ParameterGroups.Redis.2-8-22")
- [Redis OSS 2.8.21 added parameters](#ParameterGroups.Redis.2-8-21 "#ParameterGroups.Redis.2-8-21")
- [Redis OSS 2.8.19 added parameters](#ParameterGroups.Redis.2-8-19 "#ParameterGroups.Redis.2-8-19")
- [Redis OSS 2.8.6 added parameters](#ParameterGroups.Redis.2-8-6 "#ParameterGroups.Redis.2-8-6")
- [Redis OSS 2.6.13 parameters](#ParameterGroups.Redis.2-6-13 "#ParameterGroups.Redis.2-6-13")
- [Valkey node-type specific parameters](#ParameterGroups.Valkey.NodeSpecific "#ParameterGroups.Valkey.NodeSpecific")
- [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")

### Valkey 9.1 and Valkey 9.0 parameter changes

**Parameter group family:** valkey9

###### Note

- Valkey 9.0 and above parameter groups are incompatible with Valkey 8.x and Redis OSS.

New parameter group families for Valkey 9.1 and Valkey 9.0:

- `default.valkey9` – Default parameter group for Valkey 9.1 and Valkey 9.0 (cluster mode disabled).
- `default.valkey9.cluster.on` – Default parameter group for Valkey 9.1 and Valkey 9.0 with cluster mode enabled.

New customer-visible parameter in Valkey 9.0| Parameter | Description | Values | Default | Modifiable |
| --- | --- | --- | --- | --- |
| `cluster-databases` | Number of databases available in cluster mode. Set at cluster creation time. | 1 to 10,000 | 0 | No (set at creation) |

### Valkey 8.2 parameter changes

**Parameter group family:** valkey8

###### Note

- Valkey 8.2 parameter changes don't apply to Valkey 8.1
- Valkey 8.0 and above parameter groups are incompatible with Redis OSS 7.2.4.
- in Valkey 8.2, the following commands are unavailable for serverless caches: `commandlog`,
  `commandlog get`, `commandlog help`, `commandlog len`, and `commandlog reset.`

New parameter groups in Valkey 8.2| Name | Details | Description |
| --- | --- | --- |
| search-fanout-target-mode (added in 8.2) | Default: client<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The search-fanout-target-mode configuration parameter controls how search queries are distributed across nodes in a Valkey cluster environment. This setting accepts two values: "throughput" which optimizes for maximum throughput by randomly distributing search queries across all cluster nodes regardless of client type or READONLY status, and "client" which respects client connection characteristics by routing non-READONLY clients to primary nodes only, READONLY clients on replica connections to replica nodes only, and READONLY clients on primary connections randomly across all nodes.<br>The default behavior is "client' mode, meaning the system will respect client connection types and READONLY status for query routing decisions. Use throughput mode for high-volume search workloads where maximum cluster resource utilization is desired, and client mode when you want to maintain read/write separation and respect application-level READONLY connection patterns. |
| search-default-timeout-ms | Default: 50000<br>Permitted values: 1 to 60000<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The default Valkey search query timeout (in milliseconds). |
| search-enable-partial-results | Default: yes<br>Permitted values: yes, no<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: Immediately | Configures the query failure behavior for Valkey search. When enabled, search queries will return partial results if timeouts occur on one or more shards. When disabled, any shard timeout will cause the entire search query to fail and return an error. |

### Valkey 8.1 parameter changes

**Parameter group family:** valkey8

###### Note

- Valkey 8.1 parameter changes don't apply to Valkey 8.0
- Valkey 8.0 and above parameter groups are incompatible with Redis OSS 7.2.4.
- in Valkey 8.1, the following commands are unavailable for serverless caches: `commandlog`,
  `commandlog get`, `commandlog help`, `commandlog len`, and `commandlog reset.`

New parameter groups in Valkey 8.1| Name | Details | Description |
| --- | --- | --- |
| commandlog-request-larger-than (added in 8.1) | Default: 1048576<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The maximum size, in bytes, for requests to be logged by the Valkey Command Log feature. |
| commandlog-large-request-max-len (added in 8.1) | Default: 128<br>Permitted values: 0-1024<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The maximum length of the Valkey Command Log for requests. |
| commandlog-reply-larger-than (added in 8.1) | Default: 1048576<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The maximum size, in bytes, for responses to be logged by the Valkey Command Log feature. |
| commandlog-large-reply-max-len (added in 8.1) | Default: 128<br>Permitted values: 0-1024<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The maximum length of the Valkey Command Log for responses. |

### Valkey 8.0 parameter changes

**Parameter group family:** valkey8

###### Note

Redis OSS 7.2.4 is incompatible with Valkey 8 and above parameter groups.

Specific parameter changes in Valkey 8.0| Name | Details | Description |
| --- | --- | --- |
| repl-backlog-size | Default: 10485760<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The size, in bytes, of the primary node backlog buffer. The backlog is used for recording updates to data at the primary node. When a read replica connects to the primary, it attempts to perform a partial sync (psync), where it applies data from the backlog to catch up with the primary node. If the psync fails, then a full sync is required.<br>The minimum value for this parameter is 16384.<br>Note: Beginning with Redis OSS 2.8.22, this parameter applies to the primary cluster as well as the read replicas. |
| maxmemory-samples | Default: 3<br>Permitted values: 1 to 64<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | For least-recently-used (LRU) and time-to-live (TTL) calculations, this parameter represents the sample size of keys to check. By default, Redis OSS chooses 3 keys and uses the one that was used least recently. |

New parameter groups in Valkey 8.0| Name | Details | Description |
| --- | --- | --- |
| extended-redis-compatibility | Permitted values: yes, no<br>Default: yes<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Extended Redis OSS compatibility mode makes Valkey pretend to be Redis OSS 7.2. Enable this only if you have problems with tools or clients.<br>Customer-facing impacts:<br>• `LOADING` - Redis OSS is loading the dataset in memory<br>• `BUSY` - Redis OSS is busy<br>• `MISCONF` - Redis OSS is configured in either of these ways:<br>+ The `HELLO` command returns "server" => "redis" and "version" => "7.2.4" (our Redis OSS compatibility version).<br>+ The `INFO` field for mode is called "redis\_mode". |

Removed parameter groups in Valkey 8.0| Name | Details | Description |
| --- | --- | --- |
| lazyfree-lazy-eviction | Permitted values: yes, no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete on evictions. |
| lazyfree-lazy-expire | Permitted values: yes, no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete on expired keys. |
| lazyfree-lazy-server-del | Permitted values: yes, no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete for commands which update values. |
| lazyfree-lazy-user-del | Default: no<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the cluster | When the value is set to yes, the DEL command acts the same as UNLINK. |
| replica-lazy-flush | Default: yes<br>Type: boolean<br>Modifiable: No<br>Former name: slave-lazy-flush | Performs an asynchronous flushDB during replica sync. |

### Valkey 7.2 and Redis OSS 7 parameter changes

**Parameter group family:** valkey7

Valkey 7.2 default parameter groups are as follows:

- `default.valkey7` – Use this parameter group, or one
  derived from it, for Valkey (cluster mode disabled) clusters and replication groups.
- `default.valkey7.cluster.on` – Use this parameter group,
  or one derived from it, for Valkey (cluster mode enabled) clusters and replication
  groups.

**Parameter group family:** redis7

Redis OSS 7 default parameter groups are as follows:

- `default.redis7` – Use this parameter group, or one
  derived from it, for Redis OSS (cluster mode disabled) clusters and replication groups.
- `default.redis7.cluster.on` – Use this parameter group,
  or one derived from it, for Redis OSS (cluster mode enabled) clusters and replication
  groups.

**Specific parameter changes**

Parameters added in Redis OSS 7 are as follows. Valkey 7.2 also supports these parameters.

| Name                                  | Details                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cluster-allow-pubsubshard-when-down` | Permitted values: `yes`, `no`<br>Default: `yes`<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                    | When set to the default of yes, allows nodes to serve<br>pubsub shard traffic while the cluster is in a down state, as<br>long as it believes it owns the slots.                                                                                                                                                                                                                   |
| `cluster-preferred-endpoint-type`     | Permitted values: `ip`,<br>`tls-dynamic`<br>Default: `tls-dynamic`<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster. | This value controls what endpoint is returned for<br>MOVED/ASKING requests as well as the endpoint field for<br>`CLUSTER SLOTS` and `CLUSTER SHARDS`.<br>When the value is set to ip, the node will advertise its ip<br>address. When the value is set to tls-dynamic, the node will<br>advertise a hostname when encryption-in-transit is enabled and<br>an ip address otherwise. |
| `latency-tracking`                    | Permitted values: `yes`, `no`<br>Default: `no`<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                     | When set to yes tracks the per command latencies and<br>enables exporting the percentile distribution via the<br>`INFO` latency statistics command, and cumulative<br>latency distributions (histograms) via the `LATENCY`<br>command.                                                                                                                                             |
| `hash-max-listpack-entries`           | Permitted values: `0+`<br>Default: `512`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                          | The maximum number of hash entries in order for the dataset<br>to be compressed.                                                                                                                                                                                                                                                                                                   |
| `hash-max-listpack-value`             | Permitted values: `0+`<br>Default: `64`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                           | The threshold of biggest hash entries in order for the<br>dataset to be compressed.                                                                                                                                                                                                                                                                                                |
| `zset-max-listpack-entries`           | Permitted values: `0+`<br>Default: `128`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                          | The maximum number of sorted set entries in order for the<br>dataset to be compressed.                                                                                                                                                                                                                                                                                             |
| `zset-max-listpack-value`             | Permitted values: `0+`<br>Default: `64`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.                           | The threshold of biggest sorted set entries in order for<br>the dataset to be compressed.                                                                                                                                                                                                                                                                                          |

Parameters changed in Redis OSS 7 are as follows.

| Name              | Details                                                                                                                                                                                                                                          | Description         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| `activerehashing` | Modifiable: `no`. In Redis OSS 7, this parameter is<br>hidden and enabled by default. In order to disable it, you need<br>to create a [support case](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home"). | Modifiable was yes. |

Parameters removed in Redis OSS 7 are as follows.

| Name                       | Details                                                                                                                                              | Description                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `hash-max-ziplist-entries` | Permitted values: `0+`<br>Default: `512`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster. | Use `listpack` instead of `ziplist`<br>for representing small hash encoding  |
| `hash-max-ziplist-value`   | Permitted values: `0+`<br>Default: `64`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.  | Use `listpack` instead of `ziplist`<br>for representing small hash encoding  |
| `zset-max-ziplist-entries` | Permitted values: `0+`<br>Default: `128`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster. | Use `listpack` instead of `ziplist`<br>for representing small hash encoding. |
| `zset-max-ziplist-value`   | Permitted values: `0+`<br>Default: `64`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.  | Use `listpack` instead of `ziplist`<br>for representing small hash encoding. |
| `list-max-ziplist-size`    | Permitted values:<br>Default: `-2`<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster.       | The number of entries allowed per internal list<br>node.                     |

### Redis OSS 6.x parameter changes

**Parameter group family:** redis6.x

Redis OSS 6.x default parameter groups are as follows:

- `default.redis6.x` – Use this parameter group, or one
  derived from it, for Valkey or Redis OSS (cluster mode disabled) clusters and replication groups.
- `default.redis6.x.cluster.on` – Use this parameter
  group, or one derived from it, for Valkey or Redis OSS (cluster mode enabled) clusters and replication
  groups.

###### Note

In Redis OSS engine version 6.2, when the r6gd node family was introduced for use
with [Data tiering in ElastiCache](data-tiering.md "data-tiering.md"), only
_noeviction_, _volatile-lru_ and
_allkeys-lru_ max-memory policies are supported with r6gd
node types.

For more information, see [ElastiCache version 6.2 for Redis OSS (enhanced)](engine-versions.md#redis-version-6.2 "engine-versions.md#redis-version-6.2") and [ElastiCache version 6.0 for Redis OSS (enhanced)](engine-versions.md#redis-version-6.0 "engine-versions.md#redis-version-6.0").

Parameters added in Redis OSS 6.x are as follows.

| Details                                        | Description                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `acl-pubsub-default (added in 6.2)`            | Permitted values: `resetchannels`,<br>`allchannels`<br>Default: `allchannels`<br>Type: string<br>Modifiable: Yes<br>Changes take effect: The existing Redis OSS users associated to<br>the cluster will continue to have existing permissions. Either<br>update the users or reboot the cluster to update the existing<br>Redis OSS users. | Default pubsub channel permissions for ACL users deployed<br>to this cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `cluster-allow-reads-when-down (added in 6.0)` | Default: no<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster                                                                                                                                                                                                                      | When set to yes, a Redis OSS (cluster mode enabled) replication<br>group continues to process read commands even when a node is not<br>able to reach a quorum of primaries.<br>When set to the default of no, the replication group rejects<br>all commands. We recommend setting this value to yes if you are<br>using a cluster with fewer than three node groups or your<br>application can safely handle stale reads.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `tracking-table-max-keys (added in 6.0)`       | Default: 1,000,000<br>Type: number<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster                                                                                                                                                                                                               | To assist client-side caching, Redis OSS supports tracking<br>which clients have accessed which keys.<br>When the tracked key is modified, invalidation messages are<br>sent to all clients to notify them their cached values are no<br>longer valid. This value enables you to specify the upper bound<br>of this table. After this parameter value is exceeded, clients<br>are sent invalidation randomly. This value should be tuned to<br>limit memory usage while still keeping track of enough keys.<br>Keys are also invalidated under low memory conditions.                                                                                                                                                                                                                                                                                                                |
| `acllog-max-len (added in 6.0)`                | Default: 128<br>Type: number<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster                                                                                                                                                                                                                     | This value corresponds to the max number of entries in the<br>ACL log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `active-expire-effort (added in 6.0)`          | Default: 1<br>Type: number<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster                                                                                                                                                                                                                       | Redis OSS deletes keys that have exceeded their time to live by<br>two mechanisms. In one, a key is accessed and is found to be<br>expired. In the other, a periodic job samples keys and causes<br>those that have exceeded their time to live to expire. This<br>parameter defines the amount of effort that Redis OSS uses to expire<br>items in the periodic job.<br>The default value of 1 tries to avoid having more than 10<br>percent of expired keys still in memory. It also tries to avoid<br>consuming more than 25 percent of total memory and to add<br>latency to the system. You can increase this value up to 10 to<br>increase the amount of effort spent on expiring keys. The<br>tradeoff is higher CPU and potentially higher latency. We<br>recommend a value of 1 unless you are seeing high memory usage<br>and can tolerate an increase in CPU utilization. |
| `lazyfree-lazy-user-del (added in 6.0)`        | Default: no<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster                                                                                                                                                                                                                      | When the value is set to yes, the `DEL` command<br>acts the same as `UNLINK`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

Parameters removed in Redis OSS 6.x are as follows.

| Name                     | Details                                                                                                          | Description                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| `lua-replicate-commands` | Permitted values: yes/no<br>Default: yes<br>Type: boolean<br>Modifiable: Yes<br>Changes take effect: Immediately | Always enable Lua effect replication or not in Lua scripts |

### Redis OSS 5.0.3 parameter changes

**Parameter group family:** redis5.0

Redis OSS 5.0 default parameter groups

- `default.redis5.0` – Use this parameter group, or one
  derived from it, for Valkey or Redis OSS (cluster mode disabled) clusters and replication groups.
- `default.redis5.0.cluster.on` – Use this parameter
  group, or one derived from it, for Valkey or Redis OSS (cluster mode enabled) clusters and replication
  groups.

Parameters added in Redis OSS 5.0.3| Name | Details | Description |
| --- | --- | --- |
| `rename-commands` | Default: none<br>Type: string<br>Modifiable: Yes<br>Changes take effect: Immediately across all nodes in the<br>cluster | A space-separated list of renamed Redis OSS commands. The following<br>is a restricted list of commands available for renaming:<br>`APPEND AUTH BITCOUNT BITFIELD BITOP BITPOS BLPOP BRPOP<br>BRPOPLPUSH BZPOPMIN BZPOPMAX CLIENT CLUSTER COMMAND DBSIZE<br>DECR DECRBY DEL DISCARD DUMP ECHO EVAL EVALSHA EXEC EXISTS<br>EXPIRE EXPIREAT FLUSHALL FLUSHDB GEOADD GEOHASH GEOPOS<br>GEODIST GEORADIUS GEORADIUSBYMEMBER GET GETBIT GETRANGE<br>GETSET HDEL HEXISTS HGET HGETALL HINCRBY HINCRBYFLOAT HKEYS<br>HLEN HMGET HMSET HSET HSETNX HSTRLEN HVALS INCR INCRBY<br>INCRBYFLOAT INFO KEYS LASTSAVE LINDEX LINSERT LLEN LPOP<br>LPUSH LPUSHX LRANGE LREM LSET LTRIM MEMORY MGET MONITOR MOVE<br>MSET MSETNX MULTI OBJECT PERSIST PEXPIRE PEXPIREAT PFADD<br>PFCOUNT PFMERGE PING PSETEX PSUBSCRIBE PUBSUB PTTL PUBLISH<br>PUNSUBSCRIBE RANDOMKEY READONLY READWRITE RENAME RENAMENX<br>RESTORE ROLE RPOP RPOPLPUSH RPUSH RPUSHX SADD SCARD SCRIPT<br>SDIFF SDIFFSTORE SELECT SET SETBIT SETEX SETNX SETRANGE<br>SINTER SINTERSTORE SISMEMBER SLOWLOG SMEMBERS SMOVE SORT<br>SPOP SRANDMEMBER SREM STRLEN SUBSCRIBE SUNION SUNIONSTORE<br>SWAPDB TIME TOUCH TTL TYPE UNSUBSCRIBE UNLINK UNWATCH WAIT<br>WATCH ZADD ZCARD ZCOUNT ZINCRBY ZINTERSTORE ZLEXCOUNT<br>ZPOPMAX ZPOPMIN ZRANGE ZRANGEBYLEX ZREVRANGEBYLEX<br>ZRANGEBYSCORE ZRANK ZREM ZREMRANGEBYLEX ZREMRANGEBYRANK<br>ZREMRANGEBYSCORE ZREVRANGE ZREVRANGEBYSCORE ZREVRANK ZSCORE<br>ZUNIONSTORE SCAN SSCAN HSCAN ZSCAN XINFO XADD XTRIM XDEL<br>XRANGE XREVRANGE XLEN XREAD XGROUP XREADGROUP XACK XCLAIM<br>XPENDING GEORADIUS_RO GEORADIUSBYMEMBER_RO LOLWUT XSETID<br>SUBSTR` |

For more information, see [ElastiCache version 5.0.6 for Redis OSS (enhanced)](engine-versions.md#redis-version-5-0.6 "engine-versions.md#redis-version-5-0.6").

### Redis OSS 5.0.0 parameter changes

**Parameter group family:** redis5.0

Redis OSS 5.0 default parameter groups

- `default.redis5.0` – Use this parameter group, or one
  derived from it, for Valkey or Redis OSS (cluster mode disabled) clusters and replication groups.
- `default.redis5.0.cluster.on` – Use this parameter
  group, or one derived from it, for Valkey or Redis OSS (cluster mode enabled) clusters and replication
  groups.

Parameters added in Redis OSS 5.0| Name | Details | Description |
| --- | --- | --- |
| `stream-node-max-bytes` | Permitted values: 0+<br>Default: 4096<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately | The stream data structure is a radix tree of nodes that encode<br>multiple items inside. Use this configuration to specify the maximum<br>size of a single node in radix tree in Bytes. If set to 0, the size<br>of the tree node is unlimited. |
| `stream-node-max-entries` | Permitted values: 0+<br>Default: 100<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately | The stream data structure is a radix tree of nodes that encode<br>multiple items inside. Use this configuration to specify the maximum<br>number of items a single node can contain before switching to a new<br>node when appending new stream entries. If set to 0, the number of<br>items in the tree node is unlimited |
| `active-defrag-max-scan-fields` | Permitted values: 1 to 1000000<br>Default: 1000<br>Type: integer<br>Modifiable: Yes<br>Changes take effect: Immediately | Maximum number of set/hash/zset/list fields that will be<br>processed from the main dictionary scan |
| `lua-replicate-commands` | Permitted values: yes/no<br>Default: yes<br>Type: boolean<br>Modifiable: Yes<br>Changes take effect: Immediately | Always enable Lua effect replication or not in Lua scripts |
| `replica-ignore-maxmemory` | Default: yes<br>Type: boolean<br>Modifiable: No | Determines if replica ignores `maxmemory` setting by<br>not evicting items independent from the primary |

Parameters changed in Redis OSS 5.0| Name | Details | Description |
| --- | --- | --- |
| `active-defrag-cycle-min` | Permitted values: 1-75<br>Default: 5<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Minimal effort for defrag in CPU percentage. |

Redis OSS has renamed several parameters in engine version 5.0 in response to
community feedback. For more information, see [What's New in Redis OSS 5?](https://aws.amazon.com/redis/Whats_New_Redis5/ "https://aws.amazon.com/redis/Whats_New_Redis5/"). The following table lists the new names and how they map to previous
versions.

Parameters renamed in Redis OSS 5.0| Name | Details | Description |
| --- | --- | --- |
| `replica-lazy-flush` | Default: yes<br>Type: boolean<br>Modifiable: No<br>Former name: slave-lazy-flush | Performs an asynchronous flushDB during replica sync. |
| `client-output-buffer-limit-replica-hard-limit` | Default: For values see [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")<br>Type: integer<br>Modifiable: No<br>Former name:<br>client-output-buffer-limit-slave-hard-limit | For Redis OSS read replicas: If a client's output buffer reaches the<br>specified number of bytes, the client will be disconnected. |
| `client-output-buffer-limit-replica-soft-limit` | Default: For values see [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")<br>Type: integer<br>Modifiable: No<br>Former name:<br>client-output-buffer-limit-slave-soft-limit | For Redis OSS read replicas: If a client's output buffer reaches the<br>specified number of bytes, the client will be disconnected, but only<br>if this condition persists for<br>`client-output-buffer-limit-replica-soft-seconds`. |
| `client-output-buffer-limit-replica-soft-seconds` | Default: 60<br>Type: integer<br>Modifiable: No<br>Former name:<br>client-output-buffer-limit-slave-soft-seconds | For Redis OSS read replicas: If a client's output buffer remains at<br>`client-output-buffer-limit-replica-soft-limit` bytes<br>for longer than this number of seconds, the client will be<br>disconnected. |
| `replica-allow-chaining` | Default: no<br>Type: string<br>Modifiable: No<br>Former name: slave-allow-chaining | Determines whether a read replica in Redis OSS can have read replicas<br>of its own. |
| `min-replicas-to-write` | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Former name: min-slaves-to-write<br>Changes Take Effect: Immediately | The minimum number of read replicas which must be available<br>in order for the primary node to accept writes from clients. If<br>the number of available replicas falls below this number, then<br>the primary node will no longer accept write requests.<br>If either this parameter or min-replicas-max-lag is 0, then<br>the primary node will always accept writes requests, even if no<br>replicas are available. |
| `min-replicas-max-lag` | Default: 10<br>Type: integer<br>Modifiable: Yes<br>Former name: min-slaves-max-lag<br>Changes Take Effect: Immediately | The number of seconds within which the primary node must<br>receive a ping request from a read replica. If this amount of<br>time passes and the primary does not receive a ping, then the<br>replica is no longer considered available. If the number of<br>available replicas drops below min-replicas-to-write, then the<br>primary will stop accepting writes at that point.<br>If either this parameter or min-replicas-to-write is 0, then<br>the primary node will always accept write requests, even if no<br>replicas are available. |
| `close-on-replica-write` | Default: yes<br>Type: boolean<br>Modifiable: Yes<br>Former name: close-on-slave-write<br>Changes Take Effect: Immediately | If enabled, clients who attempt to write to a read-only<br>replica will be disconnected. |

Parameters removed in Redis OSS 5.0| Name | Details | Description |
| --- | --- | --- |
| `repl-timeout` | Default: 60<br>Modifiable: No | Parameter is not available in this version. |

### Redis OSS 4.0.10 parameter changes

**Parameter group family:** redis4.0

Redis OSS 4.0.x default parameter groups

- `default.redis4.0` – Use this parameter group, or one
  derived from it, for Valkey or Redis OSS (cluster mode disabled) clusters and replication groups.
- `default.redis4.0.cluster.on` – Use this parameter
  group, or one derived from it, for Valkey or Redis OSS (cluster mode enabled) clusters and replication
  groups.

Parameters changed in Redis OSS 4.0.10| Name | Details | Description |
| --- | --- | --- |
| `maxmemory-policy` | Permitted values: `allkeys-lru`,<br>`volatile-lru`,<br>`allkeys-lfu`,<br>`volatile-lfu`,<br>`allkeys-random`, `volatile-random`,<br>`volatile-ttl`, `noeviction`<br>Default: volatile-lru<br>Type: string<br>Modifiable: Yes<br>Changes take place: immediately | `maxmemory-policy` was added in version 2.6.13. In<br>version 4.0.10 two new permitted values are added:<br>`allkeys-lfu`, which will evict any key using<br>approximated LFU, and `volatile-lfu`, which will evict<br>using approximated LFU among the keys with an expire set. In version<br>6.2, when the r6gd node family was introduced for use with<br>data-tiering, only `noeviction`,<br>`volatile-lru` and `allkeys-lru`<br>max-memory policies are supported with r6gd node types. |

Parameters added in Redis OSS 4.0.10| Name | Details | Description |
| --- | --- | --- |
| **Async<br>deletion parameters** |
| `lazyfree-lazy-eviction` | Permitted values: yes/no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete on evictions. |
| `lazyfree-lazy-expire` | Permitted values: yes/no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete on expired keys. |
| `lazyfree-lazy-server-del` | Permitted values: yes/no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Performs an asynchronous delete for commands which update<br>values. |
| `slave-lazy-flush` | Permitted values: N/A<br>Default: no<br>Type: boolean<br>Modifiable: No<br>Changes take place: N/A | Performs an asynchronous flushDB during slave sync. |
| **LFU<br>parameters** |
| `lfu-log-factor` | Permitted values: any integer > 0<br>Default: 10<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Set the log factor, which determines the number of key hits to<br>saturate the key counter. |
| `lfu-decay-time` | Permitted values: any integer<br>Default: 1<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | The amount of time in minutes to decrement the key<br>counter. |
| **Active<br>defragmentation parameters** |
| `activedefrag` | Permitted values: yes/no<br>Default: no<br>Type: boolean<br>Modifiable: Yes<br>Changes take place: immediately | Enables active defragmentation.<br>NoteIn Valkey and Redis OSS versions 7.0 and above, AWS may automatically perform defragmentation when operationally necessary, regardless of this setting. |
| `active-defrag-ignore-bytes` | Permitted values: 10485760-104857600<br>Default: 104857600<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Minimum amount of fragmentation waste to start active<br>defrag. |
| `active-defrag-threshold-lower` | Permitted values: 1-100<br>Default: 10<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Minimum percentage of fragmentation to start active<br>defrag. |
| `active-defrag-threshold-upper` | Permitted values: 1-100<br>Default: 100<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Maximum percentage of fragmentation at which we use maximum<br>effort. |
| `active-defrag-cycle-min` | Permitted values: 1-75<br>Default: 25<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Minimal effort for defrag in CPU percentage. |
| `active-defrag-cycle-max` | Permitted values: 1-75<br>Default: 75<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Maximal effort for defrag in CPU percentage. |
| **Client<br>output buffer parameters** |
| `client-query-buffer-limit` | Permitted values: 1048576-1073741824<br>Default: 1073741824<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Max size of a single client query buffer. |
| `proto-max-bulk-len` | Permitted values: 1048576-536870912<br>Default: 536870912<br>Type: integer<br>Modifiable: Yes<br>Changes take place: immediately | Max size of a single element request. |

### Redis OSS 3.2.10 parameter changes

**Parameter group family:** redis3.2

ElastiCache for Redis OSS 3.2.10 there are no additional parameters supported.

### Redis OSS 3.2.6 parameter changes

**Parameter group family:** redis3.2

For Redis OSS 3.2.6 there are no additional parameters supported.

### Redis OSS 3.2.4 parameter changes

**Parameter group family:** redis3.2

Beginning with Redis OSS 3.2.4 there are two default parameter groups.

- `default.redis3.2` – When running Redis OSS 3.2.4, specify
  this parameter group or one derived from it, if you want to create a
  Valkey or Redis OSS (cluster mode disabled) replication group and still use the additional features of
  Redis OSS 3.2.4.
- `default.redis3.2.cluster.on` – Specify this parameter
  group or one derived from it, when you want to create a Valkey or Redis OSS (cluster mode enabled)
  replication group.

###### Topics

- [New parameters for Redis OSS 3.2.4](#ParameterGroups.Redis.3-2-4.New "#ParameterGroups.Redis.3-2-4.New")
- [Parameters changed in Redis OSS 3.2.4 (enhanced)](#ParameterGroups.Redis.3-2-4.Changed "#ParameterGroups.Redis.3-2-4.Changed")

#### New parameters for Redis OSS 3.2.4

**Parameter group family:** redis3.2

For Redis OSS 3.2.4 the following additional parameters are supported.

| Name                            | Details                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list-max-ziplist-size`         | Default: -2<br>Type: integer<br>Modifiable: No                                        | Lists are encoded in a special way to save space. The number<br>of entries allowed per internal list node can be specified as a<br>fixed maximum size or a maximum number of elements. For a fixed<br>maximum size, use -5 through -1, meaning:<br>• -5: max size: 64 Kb - not recommended for normal<br>workloads<br>• -4: max size: 32 Kb - not recommended<br>• -3: max size: 16 Kb - not recommended<br>• -2: max size: 8 Kb - recommended<br>• -1: max size: 4 Kb - recommended<br>• Positive numbers mean store up to exactly that<br>number of elements per list node.                                                                                                                                         |
| `list-compress-depth`           | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately    | Lists may also be compressed. Compress depth is the number of<br>quicklist ziplist nodes from each side of the list to exclude<br>from compression. The head and tail of the list are always<br>uncompressed for fast push and pop operations. Settings are:<br>• 0: Disable all compression.<br>• 1: Start compressing with the 1st node in from the<br>head and tail.<br>[head]->node->node->...->node->[tail]<br>All nodes except [head] and [tail]<br>compress.<br>• 2: Start compressing with the 2nd node in from the<br>head and tail.<br>[head]->[next]->node->node->...->node->[prev]->[tail]<br>[head], [next], [prev], [tail] do not compress.<br>All other nodes compress.<br>• Etc.                      |
| `cluster-enabled`               | Default: no/yes \*<br>Type: string<br>Modifiable: No                                  | Indicates whether this is a Valkey or Redis OSS (cluster mode enabled) replication<br>group in cluster mode (yes) or a Valkey or Redis OSS (cluster mode enabled) replication<br>group in non-cluster mode (no). Valkey or Redis OSS (cluster mode enabled) replication<br>groups in cluster mode can partition their data across up to<br>500 node groups.<br>\<br>• Redis OSS 3.2.*x<br>• has two default<br>parameter groups.<br>• `default.redis3.2` – default<br>value `no`.<br>• `default.redis3.2.cluster.on` –<br>default value `yes`.<br>.                                                                                                                                                                   |
| `cluster-require-full-coverage` | Default: no<br>Type: boolean<br>Modifiable: yes<br>Changes Take Effect: Immediately   | When set to `yes`, Valkey or Redis OSS (cluster mode enabled) nodes in<br>cluster mode stop accepting queries if they detect there is<br>at least one hash slot uncovered (no available node is<br>serving it). This way if the cluster is partially down, the<br>cluster becomes unavailable. It automatically becomes<br>available again as soon as all the slots are covered<br>again.<br>However, sometimes you want the subset of the cluster<br>which is working to continue to accept queries for the part<br>of the key space that is still covered. To do so, just set<br>the `cluster-require-full-coverage` option to<br>`no`.                                                                             |
| `hll-sparse-max-bytes`          | Default: 3000<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately | HyperLogLog sparse representation bytes limit. The<br>limit includes the 16 byte header. When a HyperLogLog using<br>the sparse representation crosses this limit, it is<br>converted into the dense representation.<br>A value greater than 16000 is not recommended, because at<br>that point the dense representation is more memory<br>efficient.<br>We recommend a value of about 3000 to have the benefits of<br>the space-efficient encoding without slowing down PFADD too<br>much, which is O(N) with the sparse encoding. The value can<br>be raised to ~10000 when CPU is not a concern, but space is,<br>and the data set is composed of many HyperLogLogs with<br>cardinality in the 0<br>• 15000 range. |
| `reserved-memory-percent`       | Default: 25<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately   | The percent of a node's memory reserved for nondata use.<br>By default, the Redis OSS data footprint grows until it consumes<br>all of the node's memory. If this occurs, then node<br>performance will likely suffer due to excessive memory<br>paging. By reserving memory, you can set aside some of the<br>available memory for non-Redis OSS purposes to help reduce the<br>amount of paging.<br>This parameter is specific to ElastiCache, and is not part of<br>the standard Redis OSS distribution.<br>For more information, see `reserved-memory` and<br>[Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").                                       |

#### Parameters changed in Redis OSS 3.2.4 (enhanced)

**Parameter group family:** redis3.2

For Redis OSS 3.2.4 the following parameters were changed.

| Name                       | Details                                                                                          | Change                                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `activerehashing`          | Modifiable: Yes if the parameter group is not<br>associated with any clusters. Otherwise,<br>no. | Modifiable was No.                                                                                     |
| `databases`                | Modifiable: Yes if the parameter group is not<br>associated with any clusters. Otherwise,<br>no. | Modifiable was No.                                                                                     |
| `appendonly`               | Default: off<br>Modifiable: No                                                                   | If you want to upgrade from an earlier Redis OSS version,<br>you must first turn `appendonly`<br>off.  |
| `appendfsync`              | Default: off<br>Modifiable: No                                                                   | If you want to upgrade from an earlier Redis OSS version,<br>you must first turn `appendfsync`<br>off. |
| `repl-timeout`             | Default: 60<br>Modifiable: No                                                                    | Is now unmodifiable with a default of 60.                                                              |
| `tcp-keepalive`            | Default: 300                                                                                     | Default was 0.                                                                                         |
| `list-max-ziplist-entries` |                                                                                                  | Parameter is no longer available.                                                                      |
| `list-max-ziplist-value`   |                                                                                                  | Parameter is no longer available.                                                                      |

### Redis OSS 2.8.24 (enhanced) added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.24 there are no additional parameters supported.

### Redis OSS 2.8.23 (enhanced) added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.23 the following additional parameter is supported.

| Name                   | Details                                                                                      | Description                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `close-on-slave-write` | Default: yes<br>Type: string (yes/no)<br>Modifiable: Yes<br>Changes Take Effect: Immediately | If enabled, clients who attempt to write to a read-only<br>replica will be disconnected. |

#### How close-on-slave-write works

The `close-on-slave-write` parameter is introduced by Amazon ElastiCache to
give you more control over how your cluster responds when a primary node and a
read replica node swap roles due to promoting a read replica to primary.

![Image: close-on-replica-write, everything working fine](images/ElastiCache-close-on-slave-write-01.png)

If the read-replica cluster is promoted to primary for any reason other than a
Multi-AZ enabled replication group failing over, the client will continue trying
to write to endpoint A. Because endpoint A is now the endpoint for a
read-replica, these writes will fail. This is the behavior for Redis OSS before
ElastiCache introducing `close-on-replica-write` and the behavior if you
disable `close-on-replica-write`.

![Image: close-on-slave-write, writes failing](images/ElastiCache-close-on-slave-write-02.png)

With `close-on-replica-write` enabled, any time a client attempts
to write to a read-replica, the client connection to the cluster is closed. Your
application logic should detect the disconnection, check the DNS table, and
reconnect to the primary endpoint, which now would be endpoint B.

![Image: close-on-slave-write, writing to new primary cluster](images/ElastiCache-close-on-slave-write-03.png)

#### When you might disable close-on-replica-write

If disabling `close-on-replica-write` results in writes to the
failing cluster, why disable `close-on-replica-write`?

As previously mentioned, with `close-on-replica-write` enabled, any
time a client attempts to write to a read-replica the client connection to the
cluster is closed. Establishing a new connection to the node takes time. Thus,
disconnecting and reconnecting as a result of a write request to the replica
also affects the latency of read requests that are served through the same
connection. This effect remains in place until a new connection is established.
If your application is especially read-heavy or very latency-sensitive, you
might keep your clients connected to avoid degrading read performance.

### Redis OSS 2.8.22 (enhanced) added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.22 there are no additional parameters supported.

###### Important

- Beginning with Redis OSS version 2.8.22, `repl-backlog-size`
  applies to the primary cluster as well as to replica clusters.
- Beginning with Redis OSS version 2.8.22, the `repl-timeout`
  parameter is not supported. If it is changed, ElastiCache will overwrite with
  the default (60s), as we do with `appendonly`.

The following parameters are no longer supported.

- _appendonly_
- _appendfsync_
- _repl-timeout_

### Redis OSS 2.8.21 added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.21, there are no additional parameters supported.

### Redis OSS 2.8.19 added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.19 there are no additional parameters supported.

### Redis OSS 2.8.6 added parameters

**Parameter group family:** redis2.8

For Redis OSS 2.8.6 the following additional parameters are supported.

| Name                     | Details                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `min-slaves-max-lag`     | Default: 10<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately               | The number of seconds within which the primary node must<br>receive a ping request from a read replica. If this amount of<br>time passes and the primary does not receive a ping, then the<br>replica is no longer considered available. If the number of<br>available replicas drops below min-slaves-to-write, then the<br>primary will stop accepting writes at that point.<br>If either this parameter or min-slaves-to-write is 0, then the<br>primary node will always accept writes requests, even if no<br>replicas are available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `min-slaves-to-write`    | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                | The minimum number of read replicas which must be available<br>in order for the primary node to accept writes from clients. If<br>the number of available replicas falls below this number, then<br>the primary node will no longer accept write requests.<br>If either this parameter or min-slaves-max-lag is 0, then the<br>primary node will always accept writes requests, even if no<br>replicas are available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `notify-keyspace-events` | Default: (an empty string)<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: Immediately | The types of keyspace events that Redis OSS can notify clients<br>of. Each event type is represented by a single letter:<br>• **K** — Keyspace<br>events, published with a prefix of<br>_\_\_keyspace@<db>\_\__<br>• **E** — Key-event<br>events, published with a prefix of<br>_\_\_keyevent@<db>\_\__<br>• **g** — Generic,<br>non-specific commands such as _DEL_,<br>_EXPIRE_,<br>_RENAME_, etc.<br>• _*$** — String<br>commands<br>• **l** — List<br>commands<br>• **s** — Set<br>commands<br>• **h** — Hash<br>commands<br>• **z** — Sorted set<br>commands<br>• **x** — Expired<br>events (events generated every time a key<br>expires)<br>• **e** — Evicted<br>events (events generated when a key is evicted for<br>maxmemory)<br>• **A** — An alias<br>for *g$lshzxe*<br>**Note:_<br>• Include at least<br>*_K_<br>• or<br>*_E_<br>• in the string so that<br>Amazon ElastiCache can deliver notifications. Event-type<br>characters (such as `x` for expired events)<br>identify what happened, but do not trigger delivery on their<br>own. If you omit *_K_<br>• and<br>**E**, Amazon ElastiCache accepts<br>the configuration without error, but silently disables<br>notifications.<br>You can have any combination of these event types. For<br>example, *AKE<br>• means that Redis OSS can publish<br>notifications of all event types.<br>Do not use any characters other than those listed above;<br>attempts to do so will result in error messages.<br>By default, this parameter is set to an empty string, meaning<br>that keyspace event notification is disabled. |
| `repl-backlog-size`      | Default: 1048576<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately          | The size, in bytes, of the primary node backlog buffer. The<br>backlog is used for recording updates to data at the primary<br>node. When a read replica connects to the primary, it attempts<br>to perform a partial sync (`psync`), where it applies<br>data from the backlog to catch up with the primary node. If the<br>`psync` fails, then a full sync is<br>required.<br>The minimum value for this parameter is 16384.<br>NoteBeginning with Redis OSS 2.8.22, this parameter applies to the<br>primary cluster as well as the read replicas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `repl-backlog-ttl`       | Default: 3600<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately             | The number of seconds that the primary node will retain the<br>backlog buffer. Starting from the time the last replica node<br>disconnected, the data in the backlog will remain intact until<br>`repl-backlog-ttl` expires. If the replica has<br>not connected to the primary within this time, then the primary<br>will release the backlog buffer. When the replica eventually<br>reconnects, it will have to perform a full sync with the<br>primary.<br>If this parameter is set to 0, then the backlog buffer will<br>never be released.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `repl-timeout`           | Default: 60<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately               | Represents the timeout period, in seconds, for:<br>• Bulk data transfer during synchronization, from the<br>read replica's perspective<br>• Primary node timeout from the replica's<br>perspective<br>• Replica timeout from the primary node's<br>perspective                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Redis OSS 2.6.13 parameters

**Parameter group family:** redis2.6

Redis OSS 2.6.13 was the first version of Redis OSS supported by ElastiCache. The following
table shows the Redis OSS 2.6.13 parameters that ElastiCache supports.

| Name                                                                                      | Details                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `activerehashing`                                                                         | Default: yes<br>Type: string (yes/no)<br>Modifiable: Yes<br>Changes take place: At Creation                                                                                     | Determines whether to enable Redis' active rehashing<br>feature. The main hash table is rehashed ten times per second;<br>each rehash operation consumes 1 millisecond of CPU time.<br>This value is set when you create the parameter group. When<br>assigning a new parameter group to a cluster, this value must be<br>the same in both the old and new parameter<br>groups.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `appendonly`                                                                              | Default: no<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | Enables or disables Redis' append only file feature (AOF).<br>AOF captures any Redis OSS commands that change data in the cache,<br>and is used to recover from certain node failures.<br>The default value is _no_, meaning AOF is<br>turned off. Set this parameter to *yes<br>• to<br>enable AOF.<br>For more information, see [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance").<br>NoteAppend Only Files (AOF) is not supported for<br>cache.t2.\<br>• nodes. For nodes of this type,<br>the `appendonly` parameter value is ignored.<br>NoteFor Multi-AZ replication groups, AOF is not<br>allowed.                                                                                                                            |
| `appendfsync`                                                                             | Default: everysec<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                        | When `appendonly` is set to yes, controls how often<br>the AOF output buffer is written to disk:<br>• _no_ — the buffer is flushed<br>to disk on an as-needed basis.<br>• _everysec_ — the buffer is<br>flushed once per second. This is the default.<br>• _always_ — the buffer is<br>flushed every time that data in the cluster is<br>modified.<br>• Appendfsync is not supported for versions 2.8.22 and<br>later.                                                                                                                                                                                                                                                                                                                                                                                    |
| `client-output-buffer-limit-normal-hard-limit`                                            | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | If a client's output buffer reaches the specified number of<br>bytes, the client will be disconnected. The default is zero (no<br>hard limit).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `client-output-buffer-limit-normal-soft-limit`                                            | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | If a client's output buffer reaches the specified number of<br>bytes, the client will be disconnected, but only if this condition<br>persists for<br>`client-output-buffer-limit-normal-soft-seconds`. The<br>default is zero (no soft limit).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `client-output-buffer-limit-normal-soft-seconds`                                          | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | If a client's output buffer remains at<br>`client-output-buffer-limit-normal-soft-limit` bytes<br>for longer than this number of seconds, the client will be<br>disconnected. The default is zero (no time limit).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `client-output-buffer-limit-pubsub-hard-limit`                                            | Default: 33554432<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                       | For Redis OSS publish/subscribe clients: If a client's output<br>buffer reaches the specified number of bytes, the client will be<br>disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `client-output-buffer-limit-pubsub-soft-limit`                                            | Default: 8388608<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                        | For Redis OSS publish/subscribe clients: If a client's output buffer<br>reaches the specified number of bytes, the client will be<br>disconnected, but only if this condition persists for<br>`client-output-buffer-limit-pubsub-soft-seconds`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `client-output-buffer-limit-pubsub-soft-seconds`                                          | Default: 60<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                             | For Redis OSS publish/subscribe clients: If a client's output buffer<br>remains at `client-output-buffer-limit-pubsub-soft-limit`<br>bytes for longer than this number of seconds, the client will be<br>disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `client-output-buffer-limit-slave-hard-limit`                                             | Default: For values see [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")<br>Type: integer<br>Modifiable: No | For Redis OSS read replicas: If a client's output buffer reaches the<br>specified number of bytes, the client will be disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `client-output-buffer-limit-slave-soft-limit`                                             | Default: For values see [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")<br>Type: integer<br>Modifiable: No | For Redis OSS read replicas: If a client's output buffer reaches the<br>specified number of bytes, the client will be disconnected, but only<br>if this condition persists for<br>`client-output-buffer-limit-slave-soft-seconds`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `client-output-buffer-limit-slave-soft-seconds`                                           | Default: 60<br>Type: integer<br>Modifiable: No                                                                                                                                  | For Redis OSS read replicas: If a client's output buffer remains at<br>`client-output-buffer-limit-slave-soft-limit` bytes<br>for longer than this number of seconds, the client will be<br>disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `databases`                                                                               | Default: 16<br>Type: integer<br>Modifiable: No<br>Changes take place: At Creation                                                                                               | The number of logical partitions the databases is split<br>into. We recommend keeping this value low.<br>This value is set when you create the parameter group. When<br>assigning a new parameter group to a cluster, this value must be<br>the same in both the old and new parameter<br>groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `hash-max-ziplist-entries`                                                                | Default: 512<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                            | Determines the amount of memory used for hashes. Hashes with<br>fewer than the specified number of entries are stored using a<br>special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `hash-max-ziplist-value`                                                                  | Default: 64<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                             | Determines the amount of memory used for hashes. Hashes with<br>entries that are smaller than the specified number of bytes are<br>stored using a special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `list-max-ziplist-entries`                                                                | Default: 512<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                            | Determines the amount of memory used for lists. Lists with fewer<br>than the specified number of entries are stored using a special<br>encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `list-max-ziplist-value`                                                                  | Default: 64<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                             | Determines the amount of memory used for lists. Lists with<br>entries that are smaller than the specified number of bytes are<br>stored using a special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `lua-time-limit`                                                                          | Default: 5000<br>Type: integer<br>Modifiable: No                                                                                                                                | The maximum execution time for a Lua script, in milliseconds,<br>before ElastiCache takes action to stop the script. If<br>`lua-time-limit` is exceeded, all Redis OSS commands<br>will return an error of the form _\_\_\_\_-BUSY_.<br>Since this state can cause interference with many essential<br>Redis OSS operations, ElastiCache will first issue a *SCRIPT<br>KILL<br>• command. If this is unsuccessful, ElastiCache will<br>forcibly restart Redis OSS.                                                                                                                                                                                                                                                                                                                                        |
| `maxclients` This value applies to all<br>instance types except those explicity specified | Default: 65000<br>Type: integer<br>Modifiable: No                                                                                                                               | The maximum number of clients that can be connected<br>at one time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| t2.medium Default: 20000<br>Type: integer<br>Modifiable: No                               |
| t2.small Default: 20000<br>Type: integer<br>Modifiable: No                                |
| t2.micro Default: 20000<br>Type: integer<br>Modifiable: No                                |
| t4g.micro Default: 20000<br>Type: integer<br>Modifiable: No                               |
| t3.medium Default: 46000<br>Type: integer<br>Modifiable: No                               |
| t3.small Default: 46000<br>Type: integer<br>Modifiable: No                                |
| t3.micro Default: 20000<br>Type: integer<br>Modifiable: No                                |
| `maxmemory-policy`                                                                        | Default: volatile-lru<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                    | The eviction policy for keys when maximum memory usage is<br>reached. Valid values are: `volatile-lru                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | allkeys-lru | <br>volatile-random | allkeys-random | volatile-ttl | <br>noeviction`<br>For more information, see [Using Valkey or Redis OSS as an<br>LRU cache](https://valkey.io/topics/lru-cache "https://valkey.io/topics/lru-cache"). |
| `maxmemory-samples`                                                                       | Default: 3<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | For least-recently-used (LRU) and time-to-live (TTL)<br>calculations, this parameter represents the sample size of keys to<br>check. By default, Redis OSS chooses 3 keys and uses the one that was<br>used least recently.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `reserved-memory`                                                                         | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | The total memory, in bytes, reserved for non-data usage. By<br>default, the Redis OSS node will grow until it consumes the node's<br>`maxmemory` (see [Redis OSS node-type specific parameters](#ParameterGroups.Redis.NodeSpecific "#ParameterGroups.Redis.NodeSpecific")). If<br>this occurs, then node performance will likely suffer due to<br>excessive memory paging. By reserving memory you can set aside<br>some of the available memory for non-Redis OSS purposes to help<br>reduce the amount of paging.<br>This parameter is specific to ElastiCache, and is not part of the<br>standard Redis OSS distribution.<br>For more information, see `reserved-memory-percent`<br>and [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md"). |
| `set-max-intset-entries`                                                                  | Default: 512<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                            | Determines the amount of memory used for certain kinds of sets<br>(strings that are integers in radix 10 in the range of 64 bit signed<br>integers). Such sets with fewer than the specified number of entries<br>are stored using a special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `slave-allow-chaining`                                                                    | Default: no<br>Type: string<br>Modifiable: No                                                                                                                                   | Determines whether a read replica in Redis OSS can have read replicas<br>of its own.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `slowlog-log-slower-than`                                                                 | Default: 10000<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                          | The maximum execution time, in microseconds, for commands to be<br>logged by the Redis OSS Slow Log feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `slowlog-max-len`                                                                         | Default: 128<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                            | The maximum length of the Redis OSS Slow Log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `tcp-keepalive`                                                                           | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | If this is set to a nonzero value (N), node clients are polled<br>every N seconds to ensure that they are still connected. With the<br>default setting of 0, no such polling occurs. ImportantSome aspects of this parameter changed in Redis OSS version<br>3.2.4. See [Parameters changed in Redis OSS 3.2.4 (enhanced)](#ParameterGroups.Redis.3-2-4.Changed "#ParameterGroups.Redis.3-2-4.Changed").                                                                                                                                                                                                                                                                                                                                                                                                  |
| `timeout`                                                                                 | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                              | The number of seconds a node waits before timing out. Values are:<br>• `0` – never disconnect an idle<br>client.<br>• `1-19` – invalid values.<br>• `>=20` – the number of seconds a node<br>waits before disconnecting an idle client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `zset-max-ziplist-entries`                                                                | Default: 128<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                            | Determines the amount of memory used for sorted sets. Sorted sets<br>with fewer than the specified number of elements are stored using a<br>special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `zset-max-ziplist-value`                                                                  | Default: 64<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: Immediately                                                                                             | Determines the amount of memory used for sorted sets. Sorted sets<br>with entries that are smaller than the specified number of bytes are<br>stored using a special encoding that saves space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

###### Note

If you do not specify a parameter group for your Redis OSS 2.6.13 cluster, then a
default parameter group (`default.redis2.6`) will be used. You cannot
change the values of any parameters in the default parameter group; however, you
can always create a custom parameter group and assign it to your cluster at any
time.

### Valkey node-type specific parameters

The value of
`maxmemory` is the maximum number of bytes available for data storage
on the node. For more information, see [Available memory](https://aws.amazon.com/premiumsupport/knowledge-center/available-memory-elasticache-redis-node/ "https://aws.amazon.com/premiumsupport/knowledge-center/available-memory-elasticache-redis-node/").

###### Note

The `maxmemory` parameter cannot be modified.

| Node type           | Maxmemory (bytes) |
| ------------------- | ----------------- |
| cache.t2.micro      | 581959680         |
| cache.t2.small      | 1665138688        |
| cache.t2.medium     | 3461349376        |
| cache.t3.micro      | 536870912         |
| cache.t3.small      | 1471026299        |
| cache.t3.medium     | 3317862236        |
| cache.t4g.micro     | 536870912         |
| cache.t4g.small     | 1471026299        |
| cache.t4g.medium    | 3317862236        |
| cache.m4.large      | 6892593152        |
| cache.m4.xlarge     | 15328501760       |
| cache.m4.2xlarge    | 31889126359       |
| cache.m4.4xlarge    | 65257290629       |
| cache.m4.10xlarge   | 166047614239      |
| cache.m5.large      | 6854542746        |
| cache.m5.xlarge     | 13891921715       |
| cache.m5.2xlarge    | 27966669210       |
| cache.m5.4xlarge    | 56116178125       |
| cache.m5.12xlarge   | 168715971994      |
| cache.m5.24xlarge   | 337500562842      |
| cache.m6g.large     | 6854542746        |
| cache.m6g.xlarge    | 13891921715       |
| cache.m6g.2xlarge   | 27966669210       |
| cache.m6g.4xlarge   | 56116178125       |
| cache.m6g.8xlarge   | 111325552312      |
| cache.m6g.12xlarge  | 168715971994      |
| cache.m6g.16xlarge  | 225000375228      |
| cache.m7g.large     | 6854542746        |
| cache.m7g.xlarge    | 13891921715       |
| cache.m7g.2xlarge   | 27966669210       |
| cache.m7g.4xlarge   | 56116178125       |
| cache.m7g.8xlarge   | 111325552312      |
| cache.m7g.12xlarge  | 168715971994      |
| cache.m7g.16xlarge  | 225000375228      |
| cache.m8g.large     | 7294178820        |
| cache.m8g.xlarge    | 15222495510       |
| cache.m8g.2xlarge   | 31866224640       |
| cache.m8g.4xlarge   | 65856864256       |
| cache.m8g.8xlarge   | 133838143488      |
| cache.m8g.12xlarge  | 201819422720      |
| cache.m8g.16xlarge  | 269800701952      |
| cache.r4.large      | 13201781556       |
| cache.r4.xlarge     | 26898228839       |
| cache.r4.2xlarge    | 54197537997       |
| cache.r4.4xlarge    | 108858546586      |
| cache.r4.8xlarge    | 218255432090      |
| cache.r4.16xlarge   | 437021573120      |
| cache.r5.large      | 14037181030       |
| cache.r5.xlarge     | 28261849702       |
| cache.r5.2xlarge    | 56711183565       |
| cache.r5.4xlarge    | 113609865216      |
| cache.r5.12xlarge   | 341206346547      |
| cache.r5.24xlarge   | 682485973811      |
| cache.r6g.large     | 14037181030       |
| cache.r6g.xlarge    | 28261849702       |
| cache.r6g.2xlarge   | 56711183565       |
| cache.r6g.4xlarge   | 113609865216      |
| cache.r6g.8xlarge   | 225000375228      |
| cache.r6g.12xlarge  | 341206346547      |
| cache.r6g.16xlarge  | 450000750456      |
| cache.r6gd.xlarge   | 28261849702       |
| cache.r6gd.2xlarge  | 56711183565       |
| cache.r6gd.4xlarge  | 113609865216      |
| cache.r6gd.8xlarge  | 225000375228      |
| cache.r6gd.12xlarge | 341206346547      |
| cache.r6gd.16xlarge | 450000750456      |
| cache.r7g.large     | 14037181030       |
| cache.r7g.xlarge    | 28261849702       |
| cache.r7g.2xlarge   | 56711183565       |
| cache.r7g.4xlarge   | 113609865216      |
| cache.r7g.8xlarge   | 225000375228      |
| cache.r7g.12xlarge  | 341206346547      |
| cache.r7g.16xlarge  | 450000750456      |
| cache.r8g.large     | 15222495510       |
| cache.r8g.xlarge    | 31866224640       |
| cache.r8g.2xlarge   | 65856864256       |
| cache.r8g.4xlarge   | 133838143488      |
| cache.r8g.8xlarge   | 269800701952      |
| cache.r8g.12xlarge  | 405763260416      |
| cache.r8g.16xlarge  | 541725818880      |
| cache.c7gn.large    | 3317862236        |
| cache.c7gn.xlarge   | 6854542746        |
| cache.c7gn.2xlarge  | 13891921715       |
| cache.c7gn.4xlarge  | 27966669210       |
| cache.c7gn.8xlarge  | 56116178125       |
| cache.c7gn.12xlarge | 84357985997       |
| cache.c7gn.16xlarge | 113609865216      |
| cache.c8gn.large    | 3330020474        |
| cache.c8gn.xlarge   | 7294178820        |
| cache.c8gn.2xlarge  | 15222495510       |
| cache.c8gn.4xlarge  | 31866224640       |
| cache.c8gn.8xlarge  | 65856864256       |
| cache.c8gn.12xlarge | 99847503872       |
| cache.c8gn.16xlarge | 133838143488      |

### Redis OSS node-type specific parameters

The value of
`maxmemory` is the maximum number of bytes available for data storage
on the node. For more information, see [Available memory](https://aws.amazon.com/premiumsupport/knowledge-center/available-memory-elasticache-redis-node/ "https://aws.amazon.com/premiumsupport/knowledge-center/available-memory-elasticache-redis-node/").

###### Note

The `maxmemory` parameter cannot be modified.

| Node type           | Maxmemory (bytes) |
| ------------------- | ----------------- |
| cache.t1.micro      | 142606336         |
| cache.t2.micro      | 581959680         |
| cache.t2.small      | 1665138688        |
| cache.t2.medium     | 3461349376        |
| cache.t3.micro      | 536870912         |
| cache.t3.small      | 1471026299        |
| cache.t3.medium     | 3317862236        |
| cache.t4g.micro     | 536870912         |
| cache.t4g.small     | 1471026299        |
| cache.t4g.medium    | 3317862236        |
| cache.m1.small      | 943718400         |
| cache.m1.medium     | 3093299200        |
| cache.m1.large      | 7025459200        |
| cache.m1.xlarge     | 14889779200       |
| cache.m2.xlarge     | 17091788800       |
| cache.m2.2xlarge    | 35022438400       |
| cache.m2.4xlarge    | 70883737600       |
| cache.m3.medium     | 2988441600        |
| cache.m3.large      | 6501171200        |
| cache.m3.xlarge     | 14260633600       |
| cache.m3.2xlarge    | 29989273600       |
| cache.m4.large      | 6892593152        |
| cache.m4.xlarge     | 15328501760       |
| cache.m4.2xlarge    | 31889126359       |
| cache.m4.4xlarge    | 65257290629       |
| cache.m4.10xlarge   | 166047614239      |
| cache.m5.large      | 6854542746        |
| cache.m5.xlarge     | 13891921715       |
| cache.m5.2xlarge    | 27966669210       |
| cache.m5.4xlarge    | 56116178125       |
| cache.m5.12xlarge   | 168715971994      |
| cache.m5.24xlarge   | 337500562842      |
| cache.m6g.large     | 6854542746        |
| cache.m6g.xlarge    | 13891921715       |
| cache.m6g.2xlarge   | 27966669210       |
| cache.m6g.4xlarge   | 56116178125       |
| cache.m6g.8xlarge   | 111325552312      |
| cache.m6g.12xlarge  | 168715971994      |
| cache.m6g.16xlarge  | 225000375228      |
| cache.m7g.large     | 6854542746        |
| cache.m7g.xlarge    | 13891921715       |
| cache.m7g.2xlarge   | 27966669210       |
| cache.m7g.4xlarge   | 56116178125       |
| cache.m7g.8xlarge   | 111325552312      |
| cache.m7g.12xlarge  | 168715971994      |
| cache.m7g.16xlarge  | 225000375228      |
| cache.c1.xlarge     | 6501171200        |
| cache.r3.large      | 14470348800       |
| cache.r3.xlarge     | 30513561600       |
| cache.r3.2xlarge    | 62495129600       |
| cache.r3.4xlarge    | 126458265600      |
| cache.r3.8xlarge    | 254384537600      |
| cache.r4.large      | 13201781556       |
| cache.r4.xlarge     | 26898228839       |
| cache.r4.2xlarge    | 54197537997       |
| cache.r4.4xlarge    | 108858546586      |
| cache.r4.8xlarge    | 218255432090      |
| cache.r4.16xlarge   | 437021573120      |
| cache.r5.large      | 14037181030       |
| cache.r5.xlarge     | 28261849702       |
| cache.r5.2xlarge    | 56711183565       |
| cache.r5.4xlarge    | 113609865216      |
| cache.r5.12xlarge   | 341206346547      |
| cache.r5.24xlarge   | 682485973811      |
| cache.r6g.large     | 14037181030       |
| cache.r6g.xlarge    | 28261849702       |
| cache.r6g.2xlarge   | 56711183565       |
| cache.r6g.4xlarge   | 113609865216      |
| cache.r6g.8xlarge   | 225000375228      |
| cache.r6g.12xlarge  | 341206346547      |
| cache.r6g.16xlarge  | 450000750456      |
| cache.r6gd.xlarge   | 28261849702       |
| cache.r6gd.2xlarge  | 56711183565       |
| cache.r6gd.4xlarge  | 113609865216      |
| cache.r6gd.8xlarge  | 225000375228      |
| cache.r6gd.12xlarge | 341206346547      |
| cache.r6gd.16xlarge | 450000750456      |
| cache.r7g.large     | 14037181030       |
| cache.r7g.xlarge    | 28261849702       |
| cache.r7g.2xlarge   | 56711183565       |
| cache.r7g.4xlarge   | 113609865216      |
| cache.r7g.8xlarge   | 225000375228      |
| cache.r7g.12xlarge  | 341206346547      |
| cache.r7g.16xlarge  | 450000750456      |
| cache.c7gn.large    | 3317862236        |
| cache.c7gn.xlarge   | 6854542746        |
| cache.c7gn.2xlarge  | 13891921715       |
| cache.c7gn.4xlarge  | 27966669210       |
| cache.c7gn.8xlarge  | 56116178125       |
| cache.c7gn.12xlarge | 84357985997       |
| cache.c7gn.16xlarge | 113609865216      |

###### Note

All current generation instance types are created in an Amazon Virtual Private Cloud VPC by
default.

T2 instances do not support Redis OSS AOF.

Redis OSS configuration variables `appendonly` and
`appendfsync` are not supported.

## Memcached specific parameters

**Memcached**

If you do not specify a parameter group for your Memcached cluster, then a default
parameter group appropriate to your engine version will be used. You can't change the
values of any parameters in a default parameter group. However, you can create a custom
parameter group and assign it to your cluster at any time. For more information, see
[Creating an ElastiCache parameter group](ParameterGroups.Creating.md "ParameterGroups.Creating.md").

###### Topics

- [Memcached 1.6.17 changes](#ParameterGroups.Memcached.1.6.17 "#ParameterGroups.Memcached.1.6.17")
- [Memcached 1.6.6 added parameters](#ParameterGroups.Memcached.1-6-6 "#ParameterGroups.Memcached.1-6-6")
- [Memcached 1.5.10 parameter changes](#ParameterGroups.Memcached.1-5-10 "#ParameterGroups.Memcached.1-5-10")
- [Memcached 1.4.34 added parameters](#ParameterGroups.Memcached.1-4-34 "#ParameterGroups.Memcached.1-4-34")
- [Memcached 1.4.33 added parameters](#ParameterGroups.Memcached.1-4-33 "#ParameterGroups.Memcached.1-4-33")
- [Memcached 1.4.24 added parameters](#ParameterGroups.Memcached.1-4-24 "#ParameterGroups.Memcached.1-4-24")
- [Memcached 1.4.14 added parameters](#ParameterGroups.Memcached.1-4-14 "#ParameterGroups.Memcached.1-4-14")
- [Memcached 1.4.5 supported parameters](#ParameterGroups.Memcached.1-4-5 "#ParameterGroups.Memcached.1-4-5")
- [Memcached connection overhead](#ParameterGroups.Memcached.Overhead "#ParameterGroups.Memcached.Overhead")
- [Memcached node-type specific parameters](#ParameterGroups.Memcached.NodeSpecific "#ParameterGroups.Memcached.NodeSpecific")

### Memcached 1.6.17 changes

From Memcached 1.6.17, we no longer support these administrative commands:
`lru_crawler`, `lru`, and `slabs`. With these
changes, you will not be able to enable/disable `lru_crawler` at runtime
via commands. Please enable/disable `lru_crawler` by modifying your
custom parameter group.

### Memcached 1.6.6 added parameters

For Memcached 1.6.6, no additional parameters are supported.

**Parameter group family:** memcached1.6

### Memcached 1.5.10 parameter changes

For Memcached 1.5.10, the following additional parameters are supported.

**Parameter group family:** memcached1.5

| Name                | Details                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `no_modern`         | Default: 1<br>Type: boolean<br>Modifiable: Yes<br>Allowed\_Values: 0,1<br>Changes Take Effect: At launch | An alias for disabling `slab_reassign`,<br>`lru_maintainer_thread`, `lru_segmented`, and`maxconns_fast`<br>commands.<br>When using Memcached 1.5 and higher, `no_modern` also sets the hash\_algorithm to<br>`jenkins`.<br>In addition, when using Memcached 1.5.10, `inline_ascii_reponse` is controlled by the parameter `parallelly`. This means that if `no_modern` is disabled then `inline_ascii_reponse` is disabled. From Memcached engine 1.5.16 onward the `inline_ascii_response` parameter no longer applies, so `no_modern` being abled or disabled has no effect on `inline_ascii_reponse`.<br>If `no_modern` is disabled, then `slab_reassign`, `lru_maintainer_thread`, `lru_segmented`, and `maxconns_fast` WILL be enabled. Since `slab_automove` and `hash_algorithm` parameters are not SWITCH parameters, their setting is based on the configurations in the parameter group.<br>If you want to disable `no_modern` and revert to `modern`, you must configure a custom parameter group to disable this parameter and then reboot for these changes to take effect.<br>NoteThe default configuration value for this parameter has<br>been changed from 0 to 1 as of August 20, 2021. The updated<br>default value will get automatically picked up by new<br>ElastiCache users for each regions after August 20th, 2021.<br>Existing ElastiCache users in the regions before August 20th, 2021<br>need to manually modify their custom parameter groups in<br>order to pick up this new change. |
| `inline_ascii_resp` | Default: 0<br>Type: boolean<br>Modifiable: Yes<br>Allowed\_Values: 0,1<br>Changes Take Effect: At launch | Stores numbers from `VALUE` response, inside an<br>item, using up to 24 bytes. Small slowdown for ASCII<br>`get`, `faster` sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

For Memcached 1.5.10, the following parameters are removed.

| Name                        | Details                                                                                                                                                | Description                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `expirezero_does_not_evict` | Default: 0<br>Type: boolean<br>Modifiable: Yes<br>Allowed\_Values: 0,1<br>Changes Take Effect: At launch                                               | No longer supported in this version.                                                                                                     |
| `modern`                    | Default: 1<br>Type: boolean<br>Modifiable: Yes (requires re-launch if set to<br>`no_modern`)<br>Allowed\_Values: 0,1<br>Changes Take Effect: At launch | No longer supported in this version. Starting with this<br>version, `no-modern` is enabled by default with every<br>launch or re-launch. |

### Memcached 1.4.34 added parameters

For Memcached 1.4.34, no additional parameters are supported.

**Parameter group family:** memcached1.4

### Memcached 1.4.33 added parameters

For Memcached 1.4.33, the following additional parameters are supported.

**Parameter group family:** memcached1.4

| Name                       | Details                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `modern`                   | Default: enabled<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: At launch                                                                                                           | An alias to multiple features. Enabling `modern` is<br>equivalent to turning following commands on and using a murmur3<br>hash algorithm: `slab_reassign`,<br>`slab_automove`, `lru_crawler`,<br>`lru_maintainer`, `maxconns_fast`, and<br>`hash_algorithm=murmur3`.                                          |
| `watch`                    | Default: enabled<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: Immediately<br>Logs can get dropped if user hits their<br>`watcher_logbuf_size` and<br>`worker_logbuf_size` limits. | Logs fetches, evictions or mutations. When, for example, user<br>turns `watch` on, they can see logs when<br>`get`, `set`, `delete`, or<br>`update` occur.                                                                                                                                                    |
| `idle_timeout`             | Default: 0 (disabled)<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: At Launch                                                                                                      | The minimum number of seconds a client will be allowed to idle<br>before being asked to close. Range of values: 0 to<br>86400.                                                                                                                                                                                |
| `track_sizes`              | Default: disabled<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: At Launch                                                                                                          | Shows the sizes each slab group has consumed.<br>Enabling `track_sizes` lets you run `stats<br>sizes` without the need to run `stats<br>sizes_enable`.                                                                                                                                                        |
| `watcher_logbuf_size`      | Default: 256 (KB)<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: At Launch                                                                                                          | The `watch` command turns on stream logging for<br>Memcached. However `watch` can drop logs if the rate<br>of evictions, mutations or fetches are high enough to cause the<br>logging buffer to become full. In such situations, users can<br>increase the buffer size to reduce the chance of log<br>losses. |
| `worker_logbuf_size`       | Default: 64 (KB)<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: At Launch                                                                                                           | The `watch` command turns on stream logging for<br>Memcached. However `watch` can drop logs if the rate<br>of evictions, mutations or fetches are high enough to cause<br>logging buffer get full. In such situations, users can increase<br>the buffer size to reduce the chance of log<br>losses.           |
| `slab_chunk_max`           | Default: 524288 (bytes)<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: At Launch                                                                                                    | Specifies the maximum size of a slab. Setting smaller slab<br>size uses memory more efficiently. Items larger than<br>`slab_chunk_max` are split over multiple<br>slabs.                                                                                                                                      |
| `lru_crawler metadump [all | 1                                                                                                                                                                                                | 2                                                                                                                                                                                                                                                                                                             | 3]` | Default: disabled<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: Immediately | if lru\_crawler is enabled this command dumps all keys.<br>`all | 1   | 2   | 3`<br>• all slabs, or specify a particular<br>slab number |

### Memcached 1.4.24 added parameters

For Memcached 1.4.24, the following additional parameters are supported.

**Parameter group family:** memcached1.4

| Name                        | Details                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `disable_flush_all`         | Default: 0 (disabled)<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: At launch                                                                                                                                               | Add parameter (`-F`) to disable flush\_all. Useful<br>if you never want to be able to run a full flush on production<br>instances.<br>Values: 0, 1 (user can do a `flush_all` when the<br>value is 0).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `hash_algorithm`            | Default: jenkins<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: At launch                                                                                                                                                     | The hash algorithm to be used. Permitted values: murmur3 and<br>jenkins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `lru_crawler`               | Default: 0 (disabled)<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: After restart<br>NoteYou can temporarily enable `lru_crawler` at<br>runtime from the command line. For more information, see the<br>Description column. | Cleans slab classes of items that have expired. This is a low<br>impact process that runs in the background. Currently requires<br>initiating a crawl using a manual command.<br>To temporarily enable, run `lru_crawler enable` at<br>the command line.<br>`lru_crawler 1,3,5` crawls slab classes 1, 3, and 5<br>looking for expired items to add to the freelist.<br>Values: 0,1<br>NoteEnabling `lru_crawler` at the command line<br>enables the crawler until either disabled at the command<br>line or the next reboot. To enable permanently, you must<br>modify the parameter value. For more information, see [Modifying an ElastiCache parameter group](ParameterGroups.Modifying.md "ParameterGroups.Modifying.md"). |
| `lru_maintainer`            | Default: 0 (disabled)<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: At launch                                                                                                                                               | A background thread that shuffles items between the LRUs as<br>capacities are reached. Values: 0, 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `expirezero_does_not_evict` | Default: 0 (disabled)<br>Type: boolean<br>Modifiable: Yes<br>Changes Take Effect: At launch                                                                                                                                               | When used with `lru_maintainer`, makes items with<br>an expiration time of 0 unevictable.<br>WarningThis can crowd out memory available for other evictable<br>items.<br>Can be set to disregard<br>`lru_maintainer`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Memcached 1.4.14 added parameters

For Memcached 1.4.14, the following additional parameters are supported.

**Parameter group family:** memcached1.4

Parameters added in Memcached 1.4.14| Name | Details | Description |
| --- | --- | --- |
| `config_max` | Default: 16<br>Type: integer<br>Modifiable: No | The maximum number of ElastiCache configuration entries. |
| `config_size_max` | Default: 65536<br>Type: integer<br>Modifiable: No | The maximum size of the configuration entries, in bytes. |
| `hashpower_init` | Default: 16<br>Type: integer<br>Modifiable: No | The initial size of the ElastiCache hash table, expressed as a power of<br>two. The default is 16 (2^16), or 65536 keys. |
| `maxconns_fast` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: Yes<br>Changes Take Effect: After restart | Changes the way in which new connections requests are handled<br>when the maximum connection limit is reached. If this parameter is<br>set to 0 (zero), new connections are added to the backlog queue and<br>will wait until other connections are closed. If the parameter is<br>set to 1, ElastiCache sends an error to the client and immediately closes<br>the connection. |
| `slab_automove` | Default: 0<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: After restart | Adjusts the slab automove algorithm: If this parameter is set to<br>0 (zero), the automove algorithm is disabled. If it is set to 1,<br>ElastiCache takes a slow, conservative approach to automatically moving<br>slabs. If it is set to 2, ElastiCache aggressively moves slabs whenever<br>there is an eviction. (This mode is not recommended except for<br>testing purposes.) |
| `slab_reassign` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: Yes<br>Changes Take Effect: After restart | Enable or disable slab reassignment. If this parameter is set to<br>1, you can use the "slabs reassign" command to manually reassign<br>memory. |

### Memcached 1.4.5 supported parameters

**Parameter group family:** memcached1.4

For Memcached 1.4.5, the following parameters are supported.

Parameters added in Memcached 1.4.5| Name | Details | Description |
| --- | --- | --- |
| `backlog_queue_limit` | Default: 1024<br>Type: integer<br>Modifiable: No | The backlog queue limit. |
| `binding_protocol` | Default: auto<br>Type: string<br>Modifiable: Yes<br>Changes Take Effect: After restart | The binding protocol. Permissible values are:<br>`ascii` and `auto`.<br>For guidance on modifying the value of<br>`binding_protocol`, see [Modifying an ElastiCache parameter group](ParameterGroups.Modifying.md "ParameterGroups.Modifying.md"). |
| `cas_disabled` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: Yes<br>Changes Take Effect: After restart | If `1` (true), check and set (CAS) operations will be<br>disabled, and items stored will consume 8 fewer bytes than with CAS<br>enabled. |
| `chunk_size` | Default: 48<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: After restart | The minimum amount, in bytes, of space to allocate for the<br>smallest item's key, value, and flags. |
| `chunk_size_growth_factor` | Default: 1.25<br>Type: float<br>Modifiable: Yes<br>Changes Take Effect: After restart | The growth factor that controls the size of each successive<br>Memcached chunk; each chunk will be<br>`chunk_size_growth_factor` times larger than the<br>previous chunk. |
| `error_on_memory_exhausted` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: Yes<br>Changes Take Effect: After restart | If `1` (true), when there is no more memory to store<br>items, Memcached will return an error rather than evicting<br>items. |
| `large_memory_pages` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: No | If `1` (true), ElastiCache will try to use large memory<br>pages. |
| `lock_down_paged_memory` | Default: 0 (false)<br>Type: Boolean<br>Modifiable: No | If `1` (true), ElastiCache will lock down all paged<br>memory. |
| `max_item_size` | Default: 1048576<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: After restart | The size, in bytes, of the largest item that can be stored in the<br>cluster. |
| `max_simultaneous_connections` | Default: 65000<br>Type: integer<br>Modifiable: No | The maximum number of simultaneous connections. |
| `maximize_core_file_limit` | Default: 0 (false)<br>Type: Boolean<br>Modifiable:<br>Changes Take Effect: After restart | If `1` (true), ElastiCache will maximize the core file<br>limit. |
| `memcached_connections_overhead` | Default: 100<br>Type: integer<br>Modifiable: Yes<br>Changes Take Effect: After restart | The amount of memory to be reserved for Memcached connections and<br>other miscellaneous overhead. For information about this parameter,<br>see [Memcached connection overhead](#ParameterGroups.Memcached.Overhead "#ParameterGroups.Memcached.Overhead"). |
| `requests_per_event` | Default: 20<br>Type: integer<br>Modifiable: No | The maximum number of requests per event for a given connection.<br>This limit is required to prevent resource starvation. |

### Memcached connection overhead

On each node, the memory made available for storing items is the total available
memory on that node (which is stored in the `max_cache_memory` parameter)
minus the memory used for connections and other overhead (which is stored in the
`memcached_connections_overhead` parameter). For example, a node of
type `cache.m5.large` has a `max_cache_memory` of 6537MB. With
the default `memcached_connections_overhead` value of 100MB, the
Memcached process will have 6437MB available to store items.

The default values for the `memcached_connections_overhead` parameter
satisfy most use cases; however, the required amount of allocation for connection
overhead can vary depending on multiple factors, including request rate, payload
size, and the number of connections.

You can change the value of the `memcached_connections_overhead` to
better suit the needs of your application. For example, increasing the value of the
`memcached_connections_overhead` parameter will reduce the amount of
memory available for storing items and provide a larger buffer for connection
overhead. Decreasing the value of the `memcached_connections_overhead`
parameter will give you more memory to store items, but can increase your risk of
swap usage and degraded performance. If you observe swap usage and degraded
performance, try increasing the value of the
`memcached_connections_overhead` parameter.

### Memcached node-type specific parameters

Although most parameters have a single value, some parameters have different
values depending on the node type used. The following table shows the default values
for the `max_cache_memory` and `num_threads` parameters for
each node type. The values on these parameters cannot be modified.

| Node type           | max\_cache\_memory (in megabytes) | num\_threads |
| ------------------- | --------------------------------- | ------------ |
| cache.t2.micro      | 555                               | 1            |
| cache.t2.small      | 1588                              | 1            |
| cache.t2.medium     | 3301                              | 2            |
| cache.t3.micro      | 512                               | 2            |
| cache.t3.small      | 1402                              | 2            |
| cache.t3.medium     | 3364                              | 2            |
| cache.t4g.micro     | 512                               | 2            |
| cache.t4g.small     | 1402                              | 2            |
| cache.t4g.medium    | 3164                              | 2            |
| cache.m4.large      | 6573                              | 2            |
| cache.m4.xlarge     | 11496                             | 4            |
| cache.m4.2xlarge    | 30412                             | 8            |
| cache.m4.4xlarge    | 62234                             | 16           |
| cache.m4.10xlarge   | 158355                            | 40           |
| cache.m5.large      | 6537                              | 2            |
| cache.m5.xlarge     | 13248                             | 4            |
| cache.m5.2xlarge    | 26671                             | 8            |
| cache.m5.4xlarge    | 53516                             | 16           |
| cache.m5.12xlarge   | 160900                            | 48           |
| cache.m5.24xlarge   | 321865                            | 96           |
| cache.m6g.large     | 6537                              | 2            |
| cache.m6g.xlarge    | 13248                             | 4            |
| cache.m6g.2xlarge   | 26671                             | 8            |
| cache.m6g.4xlarge   | 53516                             | 16           |
| cache.m6g.8xlarge   | 107000                            | 32           |
| cache.m6g.12xlarge  | 160900                            | 48           |
| cache.m6g.16xlarge  | 214577                            | 64           |
| cache.m7g.large     | 6537                              | 2            |
| cache.m7g.xlarge    | 13248                             | 4            |
| cache.m7g.2xlarge   | 26671                             | 8            |
| cache.m7g.4xlarge   | 53516                             | 16           |
| cache.m7g.8xlarge   | 107000                            | 32           |
| cache.m7g.12xlarge  | 160900                            | 48           |
| cache.m7g.16xlarge  | 214577                            | 64           |
| cache.m8g.large     | 6956                              | 2            |
| cache.m8g.xlarge    | 14517                             | 4            |
| cache.m8g.2xlarge   | 30390                             | 8            |
| cache.m8g.4xlarge   | 62806                             | 16           |
| cache.m8g.8xlarge   | 127638                            | 32           |
| cache.m8g.12xlarge  | 192470                            | 48           |
| cache.m8g.16xlarge  | 257302                            | 64           |
| cache.r4.large      | 12590                             | 2            |
| cache.r4.xlarge     | 25652                             | 4            |
| cache.r4.2xlarge    | 51686                             | 8            |
| cache.r4.4xlarge    | 103815                            | 16           |
| cache.r4.8xlarge    | 208144                            | 32           |
| cache.r4.16xlarge   | 416776                            | 64           |
| cache.r5.large      | 13387                             | 2            |
| cache.r5.xlarge     | 26953                             | 4            |
| cache.r5.2xlarge    | 54084                             | 8            |
| cache.r5.4xlarge    | 108347                            | 16           |
| cache.r5.12xlarge   | 325400                            | 48           |
| cache.r5.24xlarge   | 650869                            | 96           |
| cache.r6g.large     | 13387                             | 2            |
| cache.r6g.xlarge    | 26953                             | 4            |
| cache.r6g.2xlarge   | 54084                             | 8            |
| cache.r6g.4xlarge   | 108347                            | 16           |
| cache.r6g.8xlarge   | 214577                            | 32           |
| cache.r6g.12xlarge  | 325400                            | 48           |
| cache.r6g.16xlarge  | 429154                            | 64           |
| cache.r7g.large     | 13387                             | 2            |
| cache.r7g.xlarge    | 26953                             | 4            |
| cache.r7g.2xlarge   | 54084                             | 8            |
| cache.r7g.4xlarge   | 108347                            | 16           |
| cache.r7g.8xlarge   | 214577                            | 32           |
| cache.r7g.12xlarge  | 325400                            | 48           |
| cache.r7g.16xlarge  | 429154                            | 64           |
| cache.r8g.large     | 14517                             | 2            |
| cache.r8g.xlarge    | 30390                             | 4            |
| cache.r8g.2xlarge   | 62806                             | 8            |
| cache.r8g.4xlarge   | 127638                            | 16           |
| cache.r8g.8xlarge   | 257302                            | 32           |
| cache.r8g.12xlarge  | 386966                            | 48           |
| cache.r8g.16xlarge  | 516630                            | 64           |
| cache.c7gn.large    | 3164                              | 2            |
| cache.c7gn.xlarge   | 6537                              | 4            |
| cache.c7gn.2xlarge  | 13248                             | 8            |
| cache.c7gn.4xlarge  | 26671                             | 16           |
| cache.c7gn.8xlarge  | 53516                             | 32           |
| cache.c7gn.12xlarge | 325400                            | 48           |
| cache.c7gn.16xlarge | 108347                            | 64           |
| cache.c8gn.large    | 3176                              | 2            |
| cache.c8gn.xlarge   | 6956                              | 4            |
| cache.c8gn.2xlarge  | 14517                             | 8            |
| cache.c8gn.4xlarge  | 30390                             | 16           |
| cache.c8gn.8xlarge  | 62806                             | 32           |
| cache.c8gn.12xlarge | 95222                             | 48           |
| cache.c8gn.16xlarge | 127638                            | 64           |

###### Note

All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC).
