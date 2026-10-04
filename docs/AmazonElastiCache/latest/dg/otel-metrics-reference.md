

# OpenTelemetry metrics reference for Amazon ElastiCache
<a name="otel-metrics-reference"></a>

This topic lists the OpenTelemetry metrics that Amazon ElastiCache emits for node-based Valkey replication groups, along with the attributes that accompany them. For an introduction to the feature, including how to enable it, see [Monitoring ElastiCache with OpenTelemetry metrics](otel-metrics.md).

Most metrics are emitted by every node in the replication group and are identified by a metric name, a tier, a type, a unit, and a set of attributes. Some metrics are emitted only under specific conditions, as noted in the metric's description.

## Vended and detailed metrics
<a name="otel-metrics-reference.tiers"></a>

The **Tier** column of the tables in this topic shows how each metric becomes available.


| Tier | Description | 
| --- | --- | 
| Vended | Emitted automatically, at no additional cost. | 
| Detailed only | Emitted only while the metric is selected in a resource metrics configuration. | 

Vended metrics cover the measurements most replication groups need, and they are available without any action on your part. Turn on detailed monitoring when you want a finer granularity, or a metric that the vended tier does not include. For more information, see [Turning on detailed monitoring](otel-metrics.md#otel-metrics.detailed-monitoring).

## Common attributes
<a name="otel-metrics-reference.common-attributes"></a>

Every metric carries a common set of attributes that identify where the datapoint came from. Use these attributes to filter and aggregate your metrics in PromQL.

When CloudWatch ingests OpenTelemetry metrics, the OTLP data model is flattened into PromQL labels. The label name you use in a query depends on the OTLP scope that the attribute belongs to.


| OTLP scope | Prefix for attributes | Example | 
| --- | --- | --- | 
| Resource | @resource. | @resource.aws.elasticache.node.id | 
| Instrumentation scope | @instrumentation. | @instrumentation.@name | 
| Datapoint | None, or @datapoint. | valkey.role | 

For more information about the label structure and query syntax, see [PromQL querying](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-Querying.html) in the *Amazon CloudWatch User Guide*.

### Resource attributes
<a name="otel-metrics-reference.common-attributes.resource-attributes"></a>

Resource attributes identify the account, the location, and the ElastiCache resource that produced the datapoint. In a PromQL query, prefix these attributes with `@resource.`.


| Attribute | Example value | Description | 
| --- | --- | --- | 
| cloud.provider | aws | The cloud provider. | 
| cloud.region | us-east-1 | The AWS Region that the node runs in. | 
| cloud.availability\_zone\_id | use1-az1 | The ID of the Availability Zone that the node runs in. | 
| cloud.account.id | 123456789012 | The AWS account ID that owns the replication group. | 
| cloud.resource\_id | arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster | The ARN of the replication group. | 
| aws.elasticache.replication\_group.id | my-cluster | The ID of the replication group. | 
| aws.elasticache.shard.id | my-cluster-0001 | The ID of the shard that contains the node. | 
| aws.elasticache.node.id | my-cluster-0001-001 | The ID of the node that emitted the datapoint. | 
| aws.elasticache.engine.name | valkey | The name of the cache engine. | 
| aws.elasticache.engine.version | 8.1.0 | The version of the cache engine. | 

### Instrumentation scope attributes
<a name="otel-metrics-reference.common-attributes.instrumentation-scope-attributes"></a>

The instrumentation scope identifies ElastiCache as the source of the metrics. The scope name and version are scope *fields*, which you query using the double `@` form.


| PromQL label | Example value | Description | 
| --- | --- | --- | 
| @instrumentation.@name | cloudwatch.aws/elasticache | The instrumentation scope name. | 
| @instrumentation.@version | 1.0.0 | The instrumentation scope version. | 
| @instrumentation.cloudwatch.solution | vended \| detailed | The tier that emitted the datapoint. Use it to identify which datapoints were charged. | 

### Datapoint attributes
<a name="otel-metrics-reference.common-attributes.datapoint-attributes"></a>

Datapoint attributes are queried as bare labels, or optionally with the `@datapoint.` prefix. The following attribute is present on every metric.


| Attribute | Values | Description | 
| --- | --- | --- | 
| valkey.role | primary \| replica | The replication role of the node that emitted the datapoint. | 

Many metrics carry additional datapoint attributes that break the metric down further. These are listed in the **Additional attributes** column of the metric tables.

## Metric types
<a name="otel-metrics-reference.metric-types"></a>

The **Type** column of the metric tables gives the OpenTelemetry instrument that each metric is emitted as, which determines how you query it.


| Type | Meaning | Querying | 
| --- | --- | --- | 
| Counter | A cumulative sum that only increases, accumulated over the lifetime of the node, such as the number of commands processed | Use rate for a per-second value, or increase for a total over a time range. The cumulative value itself is rarely useful. Values are additive, so aggregating across nodes or shards with sum is meaningful | 
| UpDownCounter | A sum that can increase or decrease, such as the number of connected clients | Query it directly. Values are additive, so aggregating across nodes with sum is meaningful | 
| Gauge | A value sampled at a point in time, such as a ratio or a percentage | Query it directly. Values are not additive, so aggregating across nodes with sum is usually meaningless. Use avg, max or min instead | 
| ExponentialHistogram | A distribution of values rather than a single value | Use histogram\_quantile to read a percentile from it | 

## Metrics
<a name="otel-metrics-reference.metrics"></a>

The `valkey.*` metrics are reported by the cache engine through the `INFO` command, and the **INFO field** column gives the field that each metric is collected from. For information about these fields, see [INFO](https://valkey.io/commands/info/) in the Valkey command reference. The `system.*` and `process.*` metrics are reported by the operating system: `system.*` metrics describe the host as a whole, and `process.*` metrics describe the Valkey process specifically.

The ElastiCache console shows a display name for each metric alongside the metric name that appears here.

### Clients
<a name="otel-metrics-reference.metrics.clients"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.clients.connected | Vended | UpDownCounter | {client} | connected\_clients | — | The number of current client connections, excluding replicas. | 
| valkey.clients.max | Vended | Gauge | {client} | maxclients | — | The configured maxclients limit. This limit applies to the sum of client connections, replica connections, and cluster bus connections. | 
| valkey.clients.blocked | Vended | UpDownCounter | {client} | blocked\_clients | — | The number of clients pending on a blocking call, such as BLPOP, BLMOVE, or BZPOPMIN. | 
| valkey.clients.tracking | Detailed only | UpDownCounter | {client} | tracking\_clients | — | The number of clients in client-side caching tracking mode. | 
| valkey.clients.pubsub | Detailed only | UpDownCounter | {client} | pubsub\_clients | — | The number of clients in publish/subscribe mode. | 
| valkey.clients.watching | Detailed only | UpDownCounter | {client} | watching\_clients | — | The number of clients with an active WATCH. | 
| valkey.clients.in\_timeout\_table | Detailed only | UpDownCounter | {client} | clients\_in\_timeout\_table | — | The number of clients tracked in the timeout table. | 
| valkey.clients.cluster\_connections | Detailed only | UpDownCounter | {connection} | cluster\_connections | — | An approximation of the number of sockets used by the cluster bus. | 
| valkey.clients.max\_input\_buffer | Detailed only | Gauge | By | client\_recent\_max\_input\_buffer | — | The size of the largest recent client input buffer. | 
| valkey.clients.max\_output\_buffer | Detailed only | Gauge | By | client\_recent\_max\_output\_buffer | — | The size of the largest recent client output buffer. | 
| valkey.clients.evicted | Detailed only | Counter | {event} | evicted\_clients | — | The number of clients evicted because of the maxmemory-clients limit. | 
| valkey.clients.output\_buffer\_disconnections | Detailed only | Counter | {event} | client\_output\_buffer\_limit\_disconnections | — | The number of clients disconnected for exceeding the output buffer limit. | 
| valkey.clients.query\_buffer\_disconnections | Detailed only | Counter | {event} | client\_query\_buffer\_limit\_disconnections | — | The number of clients disconnected for exceeding the query buffer limit. | 
| valkey.clients.reply\_buffer\_expands | Detailed only | Counter | {event} | reply\_buffer\_expands | — | The number of client reply buffer expansion events. | 
| valkey.clients.reply\_buffer\_shrinks | Detailed only | Counter | {event} | reply\_buffer\_shrinks | — | The number of client reply buffer shrink events. | 

### Connections
<a name="otel-metrics-reference.metrics.connections"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.connections.received | Vended | Counter | {connection} | total\_connections\_received | — | The total number of connections accepted by the node. | 
| valkey.connections.rejected | Vended | Counter | {connection} | rejected\_connections | — | The number of connections rejected because the maxclients limit was reached. | 

### Commands
<a name="otel-metrics-reference.metrics.commands"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.commands.processed | Vended | Counter | {command} | total\_commands\_processed | — | The total number of commands processed by the node. | 

### Commands by command name
<a name="otel-metrics-reference.metrics.commands-by-command-name"></a>

The following metrics break command activity down by individual command. They are collected from the per-command `cmdstat_<command>` entries that `INFO` returns, where `<command>` is the name of the command.


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.command.calls | Vended | Counter | {call} | cmdstat\_<command>: calls | valkey.command, valkey.command.type, valkey.command.category | The number of calls for each command. | 
| valkey.command.duration | Vended | Counter | s | cmdstat\_<command>: usec | valkey.command, valkey.command.type, valkey.command.category | The total execution time for each command. | 
| valkey.command.rejected\_calls | Detailed only | Counter | {call} | cmdstat\_<command>: rejected\_calls | valkey.command, valkey.command.type, valkey.command.category | The number of rejected calls for each command. | 
| valkey.command.failed\_calls | Detailed only | Counter | {call} | cmdstat\_<command>: failed\_calls | valkey.command, valkey.command.type, valkey.command.category | The number of failed calls for each command. | 

The `valkey.command` attribute contains the command name in uppercase, for example `SET` or `GET`. For a command that has subcommands, the attribute contains the command name and the subcommand name separated by a space, for example `OBJECT ENCODING` or `CLUSTER INFO`.

The `valkey.command.type` and `valkey.command.category` attributes classify each command, so that you can aggregate command activity without listing command names. Use `valkey.command.type` to separate reads from writes, and `valkey.command.category` to group commands by the data type or the functional area that they belong to.


| Attribute | Values | Description | 
| --- | --- | --- | 
| valkey.command.type | read \| write | Whether the command reads or writes data. | 
| valkey.command.category | string, hash, list, set, sortedset, bitmap, hyperloglog, geo, stream, json, bloomfilter, search, generic, pubsub, scripting, transactions, connection, cluster, server | The data type or the functional area that the command belongs to. | 

**Note**  
Not every command carries both attributes. `valkey.command.type` is present only for commands that read or write data, so commands such as `PING`, `SUBSCRIBE`, and `MULTI` are emitted without it. Write queries so that they do not depend on an attribute that a command does not have. For example, a query that matches `valkey.command.type` returns only the commands that report a type. A given `valkey.command.category` value appears only while your workload calls commands in that category.

### Keyspace
<a name="otel-metrics-reference.metrics.keyspace"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.keyspace.hits | Vended | Counter | {hit} | keyspace\_hits | — | The number of successful key lookups. | 
| valkey.keyspace.misses | Vended | Counter | {miss} | keyspace\_misses | — | The number of failed key lookups. | 

### Keys
<a name="otel-metrics-reference.metrics.keys"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.keys.expired | Vended | Counter | {key} | expired\_keys | — | The total number of keys that have expired. | 
| valkey.keys.evicted | Vended | Counter | {key} | evicted\_keys | — | The number of keys evicted because of the maxmemory limit. | 
| valkey.keys.tracked | Vended | UpDownCounter | {key} | tracking\_total\_keys | — | The number of keys tracked for client-side caching. | 
| valkey.keys.expired\_fields | Vended | Counter | {field} | expired\_fields | — | The number of hash fields that expired through a per-field time to live (TTL). | 
| valkey.keys.expired\_stale\_percentage | Detailed only | Gauge | % | expired\_stale\_perc | — | The estimated percentage of keys that have probably expired but are still in the keyspace. | 
| valkey.keys.watched | Detailed only | UpDownCounter | {key} | total\_watched\_keys | — | The number of keys under WATCH across all clients. | 
| valkey.keys.blocking | Detailed only | UpDownCounter | {key} | total\_blocking\_keys | — | The number of distinct keys that have a blocked client. | 
| valkey.keys.blocking\_on\_nokey | Detailed only | UpDownCounter | {key} | total\_blocking\_keys\_on\_nokey | — | The number of blocking keys that have one or more clients waiting to be unblocked when the key is deleted. | 

### Memory
<a name="otel-metrics-reference.metrics.memory"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.memory.used | Vended | UpDownCounter | By | used\_memory | — | The total memory used by the cache engine. | 
| valkey.memory.used.dataset | Vended | UpDownCounter | By | used\_memory\_dataset | — | The memory used by the dataset, which is used memory minus overhead. | 
| valkey.memory.max | Vended | Gauge | By | maxmemory | — | The configured maxmemory limit. | 
| valkey.memory.fragmentation\_ratio | Vended | Gauge | 1 | mem\_fragmentation\_ratio | — | The ratio of resident set size to used memory. | 
| valkey.memory.allocator\_frag\_bytes | Vended | UpDownCounter | By | allocator\_frag\_bytes | — | The allocator-level fragmentation, in bytes. | 
| valkey.memory.allocator\_frag\_ratio | Vended | Gauge | 1 | allocator\_frag\_ratio | — | The allocator fragmentation ratio. This is the true external fragmentation metric, rather than valkey.memory.fragmentation\_ratio. | 
| valkey.memory.not\_counted\_for\_evict | Vended | UpDownCounter | By | mem\_not\_counted\_for\_evict | — | The used memory that is not counted for key eviction, which is mainly transient replica and append-only file (AOF) buffers. | 
| valkey.memory.used.overhead | Detailed only | UpDownCounter | By | used\_memory\_overhead | — | The memory used for internal structures and buffers, excluding the dataset. | 
| valkey.memory.used.startup | Detailed only | UpDownCounter | By | used\_memory\_startup | — | The memory consumed at engine startup. | 
| valkey.memory.used.vm\_eval | Detailed only | UpDownCounter | By | used\_memory\_vm\_eval | — | The memory used by the script VM engine for the EVAL framework. This memory is not part of used memory. | 
| valkey.memory.used.scripts | Detailed only | UpDownCounter | By | used\_memory\_scripts | — | The memory overhead of EVAL scripts and functions. This memory is part of used memory. | 
| valkey.memory.used.functions | Detailed only | UpDownCounter | By | used\_memory\_functions | — | The memory overhead of function scripts. This memory is part of used memory. | 
| valkey.memory.fragmentation\_bytes | Detailed only | UpDownCounter | By | mem\_fragmentation\_bytes | — | The fragmentation between resident set size and used memory, in bytes. | 
| valkey.memory.clients.normal | Detailed only | UpDownCounter | By | mem\_clients\_normal | — | The buffer memory used by normal clients. | 
| valkey.memory.clients.replica | Detailed only | UpDownCounter | By | mem\_clients\_slaves | — | The buffer memory used by replica clients. Replica buffers share memory with the replication backlog, so this metric can report 0 when replicas do not increase memory usage. | 
| valkey.memory.cluster\_links | Detailed only | UpDownCounter | By | mem\_cluster\_links | — | The buffer memory used by cluster bus links. | 
| valkey.memory.replication\_backlog | Detailed only | UpDownCounter | By | mem\_replication\_backlog | — | The memory used by the replication backlog. | 
| valkey.memory.replication\_buffers | Detailed only | UpDownCounter | By | mem\_total\_replication\_buffers | — | The total memory used by replication buffers. | 
| valkey.memory.lazyfree\_pending\_objects | Detailed only | UpDownCounter | {object} | lazyfree\_pending\_objects | — | The number of objects waiting to be freed as a result of UNLINK, or of FLUSHDB and FLUSHALL with the ASYNC option. | 
| valkey.memory.lazyfreed\_objects | Detailed only | Counter | {object} | lazyfreed\_objects | — | The total number of objects freed lazily. | 

### Defragmentation
<a name="otel-metrics-reference.metrics.defragmentation"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.defrag.hits | Vended | Counter | {hit} | active\_defrag\_hits | — | The number of reallocations performed by active defragmentation. | 
| valkey.defrag.misses | Detailed only | Counter | {miss} | active\_defrag\_misses | — | The number of value reallocations that active defragmentation started and then aborted. | 
| valkey.defrag.running | Detailed only | Gauge | % | active\_defrag\_running | — | The percentage of CPU that active defragmentation intends to use. The value is 0 when active defragmentation is not running. | 
| valkey.defrag.key\_hits | Detailed only | Counter | {key} | active\_defrag\_key\_hits | — | The number of keys that were actively defragmented. | 
| valkey.defrag.key\_misses | Detailed only | Counter | {key} | active\_defrag\_key\_misses | — | The number of keys that were skipped by active defragmentation. | 
| valkey.defrag.duration | Detailed only | Counter | s | total\_active\_defrag\_time | — | The total time that memory fragmentation was over the limit. | 

### Network
<a name="otel-metrics-reference.metrics.network"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.network.input | Detailed only | Counter | By | total\_net\_input\_bytes | — | The total bytes read from the network by the cache engine. | 
| valkey.network.output | Detailed only | Counter | By | total\_net\_output\_bytes | — | The total bytes written to the network by the cache engine. | 
| valkey.network.input.replication | Detailed only | Counter | By | total\_net\_repl\_input\_bytes | — | The total replication bytes read. | 
| valkey.network.output.replication | Detailed only | Counter | By | total\_net\_repl\_output\_bytes | — | The total replication bytes written. | 

### Replication
<a name="otel-metrics-reference.metrics.replication"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.replication.offset | Vended | Gauge | By | master\_repl\_offset | — | The replication offset of the node. | 
| valkey.replication.is\_primary | Vended | Gauge | {state} | role | — | Set to 1 if the node is a primary, otherwise 0. | 
| valkey.replication.link\_healthy | Vended | Gauge | {state} | master\_link\_status | — | Set to 1 if the link from the replica to its primary is up, otherwise 0. Emitted on replicas. | 
| valkey.replication.connected\_replicas | Detailed only | UpDownCounter | {replica} | connected\_slaves | — | The number of connected replicas. | 
| valkey.replication.last\_io\_seconds\_ago | Detailed only | Gauge | s | master\_last\_io\_seconds\_ago | — | The time since the last interaction with the primary. Emitted on replicas. | 
| valkey.replication.sync.in\_progress | Detailed only | Gauge | {state} | master\_sync\_in\_progress | — | Set to 1 while an initial full synchronization is running, otherwise 0. Emitted on replicas. | 
| valkey.replication.sync.left\_bytes | Detailed only | Gauge | By | master\_sync\_left\_bytes | — | The bytes remaining before an in-progress full synchronization is complete. The value can be negative when the total size is unknown. Emitted on replicas. | 
| valkey.replication.backlog\_active | Detailed only | Gauge | {state} | repl\_backlog\_active | — | Set to 1 if the replication backlog is active, otherwise 0. | 
| valkey.replication.backlog\_size | Detailed only | Gauge | By | repl\_backlog\_size | — | The configured size of the replication backlog. | 
| valkey.replication.backlog\_histlen | Detailed only | UpDownCounter | By | repl\_backlog\_histlen | — | The number of bytes currently held in the replication backlog. | 
| valkey.replication.replicas\_buffer\_size | Detailed only | UpDownCounter | By | replicas\_repl\_buffer\_size | — | The replication stream data currently accumulated during dual-channel replication. | 
| valkey.replication.replicas\_waiting\_psync | Detailed only | UpDownCounter | {replica} | replicas\_waiting\_psync | — | The number of replicas waiting for partial resynchronization during dual-channel replication. | 
| valkey.replication.sync.full | Detailed only | Counter | {sync} | sync\_full | — | The number of full resynchronizations served to replicas. | 
| valkey.replication.sync.partial\_ok | Detailed only | Counter | {sync} | sync\_partial\_ok | — | The number of partial resynchronizations served successfully. | 
| valkey.replication.sync.partial\_err | Detailed only | Counter | {sync} | sync\_partial\_err | — | The number of partial resynchronizations that could not be served. | 

### Persistence
<a name="otel-metrics-reference.metrics.persistence"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.persistence.rdb.save\_in\_progress | Vended | Gauge | {state} | rdb\_bgsave\_in\_progress | — | Set to 1 while an RDB save is running, including an RDB save for diskless replication, otherwise 0. | 
| valkey.persistence.rdb.changes\_since\_save | Detailed only | UpDownCounter | {change} | rdb\_changes\_since\_last\_save | — | The number of writes since the last successful save. | 

### Publish/subscribe
<a name="otel-metrics-reference.metrics.publish-subscribe"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.pubsub.channels | Vended | UpDownCounter | {channel} | pubsub\_channels | — | The number of active global publish/subscribe channels. | 
| valkey.pubsub.shard\_channels | Vended | UpDownCounter | {channel} | pubsubshard\_channels | — | The number of active sharded publish/subscribe channels. | 
| valkey.pubsub.patterns | Detailed only | UpDownCounter | {pattern} | pubsub\_patterns | — | The number of active publish/subscribe pattern subscriptions. | 

### Socket I/O
<a name="otel-metrics-reference.metrics.socket-i-o"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.io.reads\_processed | Detailed only | Counter | {event} | total\_reads\_processed | — | The number of socket read events processed by the event loop. | 
| valkey.io.writes\_processed | Detailed only | Counter | {event} | total\_writes\_processed | — | The number of socket write events processed by the event loop. | 
| valkey.io.threaded.reads\_processed | Detailed only | Counter | {event} | io\_threaded\_reads\_processed | — | The number of client reads handled by I/O threads. | 
| valkey.io.threaded.writes\_processed | Detailed only | Counter | {event} | io\_threaded\_writes\_processed | — | The number of client writes handled by I/O threads. | 
| valkey.io.threaded.prefetch\_batches | Detailed only | Counter | {batch} | io\_threaded\_total\_prefetch\_batches | — | The number of command prefetch batches executed by I/O threads. | 
| valkey.io.threaded.prefetch\_entries | Detailed only | Counter | {entry} | io\_threaded\_total\_prefetch\_entries | — | The number of entries prefetched by I/O threads. | 

The `valkey.io.threaded.*` metrics are emitted only when I/O threading is enabled.

### Event loop
<a name="otel-metrics-reference.metrics.event-loop"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.eventloop.cycles | Detailed only | Counter | {cycle} | eventloop\_cycles | — | The total number of event loop iterations. | 
| valkey.eventloop.duration | Detailed only | Counter | s | eventloop\_duration\_sum | — | The total time spent in the event loop, including I/O and command processing. | 
| valkey.eventloop.command.duration | Detailed only | Counter | s | eventloop\_duration\_cmd\_sum | — | The total time spent executing commands in the event loop. This is a subset of valkey.eventloop.duration. | 

### Scripts and functions
<a name="otel-metrics-reference.metrics.scripts-and-functions"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.scripts.cached | Detailed only | UpDownCounter | {script} | number\_of\_cached\_scripts | — | The number of scripts in the script cache. | 
| valkey.scripts.evicted | Detailed only | Counter | {script} | evicted\_scripts | — | The number of scripts evicted from the script cache. | 
| valkey.functions.count | Detailed only | UpDownCounter | {function} | number\_of\_functions | — | The number of registered functions. | 
| valkey.functions.libraries.count | Detailed only | UpDownCounter | {library} | number\_of\_libraries | — | The number of loaded function libraries. | 

### Client-side caching
<a name="otel-metrics-reference.metrics.client-side-caching"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.tracking.items | Detailed only | UpDownCounter | {item} | tracking\_total\_items | — | The number of tracked items, which is the sum of the number of clients tracking each key. | 
| valkey.tracking.prefixes | Detailed only | UpDownCounter | {prefix} | tracking\_total\_prefixes | — | The number of prefixes tracked in broadcast mode. | 

### Access control
<a name="otel-metrics-reference.metrics.access-control"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.acl.denied | Vended | Counter | {request} | acl\_access\_denied\_<reason> | valkey.acl.denied.reason | The number of requests denied by access control, broken down by reason. | 

The `valkey.acl.denied.reason` attribute takes one of the following values.


| Value | Description | 
| --- | --- | 
| auth | Authentication failures. | 
| cmd | Commands denied by an access control list (ACL). | 
| channel | Publish/subscribe channel accesses denied by an ACL. | 
| key | Key accesses denied by an ACL. | 
| tls\_cert | TLS client certificate authentication failures. | 

### Errors
<a name="otel-metrics-reference.metrics.errors"></a>

The following metric is collected from the `errorstat_<prefix>` entries that `INFO` returns, where `<prefix>` is an error prefix such as `ERR` or `WRONGTYPE`.


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.errors | Vended | Counter | {error} | errorstat\_<prefix>: count | valkey.error.type | The number of error replies, broken down by error type. | 

The `valkey.error.type` attribute contains the error prefix that the cache engine returned, which is the first word of the error reply, for example `ERR`, `WRONGTYPE`, `NOAUTH`, or `OOM`. Because the attribute reports the prefix rather than the full message, each value represents a class of error rather than one specific error.

### Traffic management
<a name="otel-metrics-reference.metrics.traffic-management"></a>


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.throttling.active | Vended | Gauge | {state} | — | — | Set to 1 while traffic management is active, otherwise 0. Datapoints of 1 can indicate that the node is underscaled for the workload. | 

### Durability
<a name="otel-metrics-reference.metrics.durability"></a>

The following metrics are emitted for replication groups that use a durability configuration with a bounded recovery point objective (RPO).


| Metric | Tier | Type | Unit | INFO field | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | --- | 
| valkey.durability.lag | Vended | Gauge | s | — | — | The age of the oldest write that has not yet been persisted to the Multi-AZ transactional log. | 
| valkey.durability.buffer\_exceeded\_errors | Vended | Counter | {error} | — | — | The number of writes rejected because the durability window was exceeded. Writes are rejected as valkey.durability.lag approaches 10 seconds. | 

### Process
<a name="otel-metrics-reference.metrics.process"></a>


| Metric | Tier | Type | Unit | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | 
| process.cpu.time | Vended | Counter | s | cpu.mode, thread.type | The CPU time consumed by the cache engine process. | 
| process.paging.faults | Vended | Counter | {fault} | system.paging.fault.type | The number of major page faults for the cache engine process. Minor faults are not reported. | 

The additional attributes take the following values.


| Attribute | Values | Description | 
| --- | --- | --- | 
| cpu.mode | user \| system | Whether the CPU time was spent in user mode or system mode. | 
| thread.type | main | The type of thread that consumed the CPU time. Only the main thread is reported, so this metric does not include CPU time consumed by I/O threads. | 
| system.paging.fault.type | major | The type of page fault. Only major faults are reported. | 

### Host memory
<a name="otel-metrics-reference.metrics.host-memory"></a>


| Metric | Tier | Type | Unit | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | 
| system.memory.usage | Vended | UpDownCounter | By | system.memory.state = free | The host memory, by state. The free state reports freeable memory. | 
| system.paging.usage | Vended | UpDownCounter | By | system.paging.state = used | The host swap space, by state. The used state reports swap space in use. | 

### Host network
<a name="otel-metrics-reference.metrics.host-network"></a>


| Metric | Tier | Type | Unit | Additional attributes | Description | 
| --- | --- | --- | --- | --- | --- | 
| system.network.io | Vended | Counter | By | network.io.direction | The total bytes transferred on the host network interface. | 
| system.network.packet.count | Vended | Counter | {packet} | network.io.direction | The total packets transferred on the host network interface. | 
| system.network.io.rate | Vended | ExponentialHistogram | By/s | network.io.direction | The distribution of the per-second byte rate on the host network interface. The interface is sampled once a second, and each datapoint is the distribution of those per-second rates. | 
| system.network.packet.rate | Vended | ExponentialHistogram | {packet}/s | network.io.direction | The distribution of the per-second packet rate on the host network interface. The interface is sampled once a second, and each datapoint is the distribution of those per-second rates. | 
| system.network.allowance\_exceeded | Vended | Counter | {packet} | network.allowance\_exceeded.reason | The number of packets that were queued or dropped because a network allowance was exceeded, broken down by reason. The counters increment for each affected packet, not once for each time the allowance was exceeded. | 
| system.network.bandwidth.limit | Vended | Gauge | By/s | — | The baseline network bandwidth for the node's instance type. The limit is the same in each direction and applies to each direction separately. | 

The additional attributes take the following values.


| Attribute | Values | Description | 
| --- | --- | --- | 
| network.io.direction | receive \| transmit | The direction of the network traffic. | 
| network.allowance\_exceeded.reason | bandwidth\_in \| bandwidth\_out \| pps \| conntrack | The allowance that was exceeded: inbound bandwidth, outbound bandwidth, packets per second, or tracked connections. | 