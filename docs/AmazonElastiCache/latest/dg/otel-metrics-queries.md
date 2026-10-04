

# Example queries for common monitoring tasks
<a name="otel-metrics-queries"></a>

The following queries answer common questions about a node-based Valkey replication group. Each one is ready to copy into a CloudWatch dashboard, and you can edit any of them to suit your own workload.

Every query is grouped by topic and collapsed. Expand an entry to see the query it contains.

Some queries use metrics that are emitted only while they are selected in a resource metrics configuration. These queries are marked **Requires detailed monitoring**, and return no data until you select the metrics that they name. For more information, see [Turning on detailed monitoring](otel-metrics.md#otel-metrics.detailed-monitoring).

**Note**  
These queries assume that you understand the PromQL constructs they use. For an introduction to each construct, with worked examples, see [Querying your metrics](otel-metrics.md#otel-metrics.querying).

## Substituting your own values
<a name="otel-metrics-queries.substituting-your-own-values"></a>

Replace the following placeholders with values from your own replication group.


| Placeholder | Replace with | 
| --- | --- | 
| my-cluster | Your replication group ID | 
| my-cluster-0001-001 | A node ID | 
| prod-.\* | A regular expression that matches the replication group IDs you want | 

**Note**  
A query can return at most 500 time series. Queries that break results down by node and by command can exceed that limit on a large replication group, in which case the response is truncated. Aggregate the result, or narrow it with a more specific label matcher.

**Note**  
The ranges in these queries, such as `[5m]`, suit a metric emitted every 60 seconds. If you have selected a metric, it is emitted every 15 seconds and you can shorten its ranges to `[1m]` for a more responsive result.

## Turning a query into an alarm
<a name="otel-metrics-queries.turning-a-query-into-an-alarm"></a>

A PromQL alarm carries its threshold inside the query. To turn any of these queries into an alarm, append a comparison. The query then returns a series only while the condition is true, and the alarm tracks each returned series separately. For example, the following query returns a series for each node that is using more than 90 percent of its memory limit.

```
100 * {"valkey.memory.used", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    / {"valkey.memory.max",  "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    > 90
```

Choose a threshold that suits your workload. A query that already ends in a comparison, such as `== 0`, can be used as an alarm unchanged. For how a PromQL alarm evaluates a query, see [Creating alarms from queries](otel-metrics.md#otel-metrics.alarms).

## Memory and capacity
<a name="otel-metrics-queries.memory-and-capacity"></a>

### Memory used as a percentage of the maxmemory limit
<a name="otel-metrics-queries.memory-and-capacity.memory-used-as-a-percentage-of-the-maxmemory-limit"></a>

```
100 * {"valkey.memory.used", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    / {"valkey.memory.max",  "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

A ratio against the configured limit, so it is comparable across different configurations.

### When memory is forecast to reach the limit
<a name="otel-metrics-queries.memory-and-capacity.when-memory-is-forecast-to-reach-the-limit"></a>

```
100 * predict_linear({"valkey.memory.used",
                      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[1h], 3600)
    / on ("@resource.aws.elasticache.node.id")
      {"valkey.memory.max", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

`predict_linear` fits the trend of the last hour and projects it one hour ahead, so a value over 100 means that the node is projected to reach `maxmemory` within the hour. A linear fit does not model a workload that grows in steps.

### Memory counted toward eviction, as a percentage of the limit
<a name="otel-metrics-queries.memory-and-capacity.memory-counted-toward-eviction-as-a-percentage-of-the-limit"></a>

```
100 * ( {"valkey.memory.used",                  "@resource.aws.elasticache.replication_group.id"="my-cluster"}
      - {"valkey.memory.not_counted_for_evict", "@resource.aws.elasticache.replication_group.id"="my-cluster"} )
    / {"valkey.memory.max",                     "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

The engine excludes some memory when deciding whether to evict, so this tracks the eviction decision more closely than total memory use does.

### Memory overhead ratio
<a name="otel-metrics-queries.memory-and-capacity.memory-overhead-ratio"></a>

**Requires detailed monitoring:** `valkey.memory.used.overhead`

```
100 * {"valkey.memory.used.overhead", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    / {"valkey.memory.used",          "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

A high share usually points to client buffer growth or replication backlog rather than dataset size.

### Peak memory over a window
<a name="otel-metrics-queries.memory-and-capacity.peak-memory-over-a-window"></a>

```
max_over_time({"valkey.memory.used",
               "@resource.aws.elasticache.replication_group.id"="my-cluster"}[24h])
```

The range sets the period, up to 7 days.

### How fast the dataset is growing
<a name="otel-metrics-queries.memory-and-capacity.how-fast-the-dataset-is-growing"></a>

```
deriv({"valkey.memory.used",
       "@resource.aws.elasticache.replication_group.id"="my-cluster"}[30m])
```

`deriv` is used because `valkey.memory.used` can decrease as well as increase, so `rate` does not apply.

## CPU and compute
<a name="otel-metrics-queries.cpu-and-compute"></a>

### Engine CPU as a percentage of one vCPU
<a name="otel-metrics-queries.cpu-and-compute.engine-cpu-as-a-percentage-of-one-vcpu"></a>

```
100 * sum without ("cpu.mode") (
        rate({"process.cpu.time",
              "thread.type"="main",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

The main thread is single-threaded, so approaching 100 percent means the engine is saturated regardless of how many vCPUs the node has.

### User vs system CPU split
<a name="otel-metrics-queries.cpu-and-compute.user-vs-system-cpu-split"></a>

```
100 * sum by ("cpu.mode", "@resource.aws.elasticache.node.id") (
        rate({"process.cpu.time",
              "thread.type"="main",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### How fast swap is growing
<a name="otel-metrics-queries.cpu-and-compute.how-fast-swap-is-growing"></a>

```
deriv({"system.paging.usage",
       "system.paging.state"="used",
       "@resource.aws.elasticache.replication_group.id"="my-cluster"}[30m])
```

A sustained positive value means the host is still moving pages to swap, which is worse than a steady non-zero figure.

### Host page-fault rate
<a name="otel-metrics-queries.cpu-and-compute.host-page-fault-rate"></a>

```
rate({"process.paging.faults",
      "system.paging.fault.type"="major",
      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Only major faults are reported. They require disk access, so a sustained rate indicates memory pressure.

## Throughput and commands
<a name="otel-metrics-queries.throughput-and-commands"></a>

### Total command rate per node
<a name="otel-metrics-queries.throughput-and-commands.total-command-rate-per-node"></a>

```
rate({"valkey.commands.processed", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

### Read vs write command rate
<a name="otel-metrics-queries.throughput-and-commands.read-vs-write-command-rate"></a>

```
sum by ("valkey.command.type") (
  rate({"valkey.command.calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Write ratio
<a name="otel-metrics-queries.throughput-and-commands.write-ratio"></a>

```
100 * sum(rate({"valkey.command.calls", "valkey.command.type"="write",
                "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / sum(rate({"valkey.command.calls", "valkey.command.type"=~"read|write",
                "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Commands that neither read nor write, such as `PING`, carry no `valkey.command.type`, so the denominator counts reads and writes only.

### Top 10 commands by call rate
<a name="otel-metrics-queries.throughput-and-commands.top-10-commands-by-call-rate"></a>

```
topk(10, sum by ("valkey.command") (
  rate({"valkey.command.calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])))
```

### Call rate per individual command
<a name="otel-metrics-queries.throughput-and-commands.call-rate-per-individual-command"></a>

```
sum by ("valkey.command") (
  rate({"valkey.command.calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Call rate for a specific set of commands
<a name="otel-metrics-queries.throughput-and-commands.call-rate-for-a-specific-set-of-commands"></a>

```
sum by ("valkey.command") (
  rate({"valkey.command.calls",
        "valkey.command"=~"GET|MGET|HGET|LRANGE",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Command rate by category
<a name="otel-metrics-queries.throughput-and-commands.command-rate-by-category"></a>

```
sum by ("valkey.command.category") (
  rate({"valkey.command.calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Rate for one data type
<a name="otel-metrics-queries.throughput-and-commands.rate-for-one-data-type"></a>

```
sum(rate({"valkey.command.calls", "valkey.command.category"="sortedset",
          "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### TPS of each shard
<a name="otel-metrics-queries.throughput-and-commands.tps-of-each-shard"></a>

```
sum by ("@resource.aws.elasticache.shard.id") (
  rate({"valkey.commands.processed",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Compare shards against each other to find imbalance.

### Each node's share of its shard's traffic
<a name="otel-metrics-queries.throughput-and-commands.each-node-s-share-of-its-shard-s-traffic"></a>

```
  rate({"valkey.commands.processed",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
/ on ("@resource.aws.elasticache.shard.id") group_left
  sum by ("@resource.aws.elasticache.shard.id") (
    rate({"valkey.commands.processed",
          "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

## Latency (per command)
<a name="otel-metrics-queries.latency-per-command"></a>

### Average latency per command, in microseconds
<a name="otel-metrics-queries.latency-per-command.average-latency-per-command-in-microseconds"></a>

```
1e6 * sum by ("valkey.command") (
        rate({"valkey.command.duration",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / (sum by ("valkey.command") (
        rate({"valkey.command.calls",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])) > 0)
```

`1e6` converts seconds to microseconds. The result is an average over the range.

### Slowest commands right now
<a name="otel-metrics-queries.latency-per-command.slowest-commands-right-now"></a>

```
topk(5,
  1e6 * sum by ("valkey.command") (rate({"valkey.command.duration",
            "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
      / (sum by ("valkey.command") (rate({"valkey.command.calls",
            "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])) > 0))
```

### Average read latency vs average write latency
<a name="otel-metrics-queries.latency-per-command.average-read-latency-vs-average-write-latency"></a>

```
1e6 * sum by ("valkey.command.type") (
        rate({"valkey.command.duration",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / (sum by ("valkey.command.type") (
        rate({"valkey.command.calls",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])) > 0)
```

### Average latency by command category
<a name="otel-metrics-queries.latency-per-command.average-latency-by-command-category"></a>

```
1e6 * sum by ("valkey.command.category") (
        rate({"valkey.command.duration",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / (sum by ("valkey.command.category") (
        rate({"valkey.command.calls",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])) > 0)
```

### Aggregate average command latency across the replication group
<a name="otel-metrics-queries.latency-per-command.aggregate-average-command-latency-across-the-replication-group"></a>

```
1e6 * sum(rate({"valkey.command.duration",
                "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / sum(rate({"valkey.command.calls",
                "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

## Cache effectiveness
<a name="otel-metrics-queries.cache-effectiveness"></a>

### Keyspace hit ratio
<a name="otel-metrics-queries.cache-effectiveness.keyspace-hit-ratio"></a>

```
100 * sum(rate({"valkey.keyspace.hits",   "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / (sum(rate({"valkey.keyspace.hits",  "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
     + sum(rate({"valkey.keyspace.misses","@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])))
```

### Eviction rate
<a name="otel-metrics-queries.cache-effectiveness.eviction-rate"></a>

```
rate({"valkey.keys.evicted", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Keys are evicted only under an eviction policy. Under `noeviction`, writes are rejected instead.

### Expiration rate
<a name="otel-metrics-queries.cache-effectiveness.expiration-rate"></a>

```
rate({"valkey.keys.expired", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

### Per-field (hash TTL) expiration rate
<a name="otel-metrics-queries.cache-effectiveness.per-field-hash-ttl-expiration-rate"></a>

```
rate({"valkey.keys.expired_fields", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

## Connections and clients
<a name="otel-metrics-queries.connections-and-clients"></a>

### Connection utilization vs maxclients
<a name="otel-metrics-queries.connections-and-clients.connection-utilization-vs-maxclients"></a>

```
100 * {"valkey.clients.connected", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    / {"valkey.clients.max",       "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

A ratio against the configured limit, so it is comparable across different configurations.

### Rejected-connection rate
<a name="otel-metrics-queries.connections-and-clients.rejected-connection-rate"></a>

```
rate({"valkey.connections.rejected", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

### Connection acceptance rate
<a name="otel-metrics-queries.connections-and-clients.connection-acceptance-rate"></a>

```
rate({"valkey.connections.received", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

A high rate can indicate that clients are not pooling connections.

## Client buffer pressure
<a name="otel-metrics-queries.client-buffer-pressure"></a>

### Clients disconnected for exceeding the output buffer limit
<a name="otel-metrics-queries.client-buffer-pressure.clients-disconnected-for-exceeding-the-output-buffer-limit"></a>

**Requires detailed monitoring:** `valkey.clients.output_buffer_disconnections`

```
rate({"valkey.clients.output_buffer_disconnections",
      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

A disconnection is data the client never received.

### Clients disconnected for exceeding the query buffer limit
<a name="otel-metrics-queries.client-buffer-pressure.clients-disconnected-for-exceeding-the-query-buffer-limit"></a>

**Requires detailed monitoring:** `valkey.clients.query_buffer_disconnections`

```
rate({"valkey.clients.query_buffer_disconnections",
      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

A disconnection is a request that was never completed.

### Clients evicted due to the client-memory limit
<a name="otel-metrics-queries.client-buffer-pressure.clients-evicted-due-to-the-client-memory-limit"></a>

**Requires detailed monitoring:** `valkey.clients.evicted`

```
rate({"valkey.clients.evicted", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Eviction means client memory reached its configured cap.

## Replication and durability
<a name="otel-metrics-queries.replication-and-durability"></a>

### Replica link down
<a name="otel-metrics-queries.replication-and-durability.replica-link-down"></a>

```
{"valkey.replication.link_healthy", "valkey.role"="replica",
 "@resource.aws.elasticache.replication_group.id"="my-cluster"} == 0
```

Returns a series only for a replica whose link is down, so it can be used as an alarm unchanged.

### Sync in progress
<a name="otel-metrics-queries.replication-and-durability.sync-in-progress"></a>

**Requires detailed monitoring:** `valkey.replication.sync.in_progress`

```
{"valkey.replication.sync.in_progress", "@resource.aws.elasticache.replication_group.id"="my-cluster"} == 1
```

### Write throughput on each primary
<a name="otel-metrics-queries.replication-and-durability.write-throughput-on-each-primary"></a>

```
deriv({"valkey.replication.offset", "valkey.role"="primary",
       "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Reported in bytes per second.

### Durability buffer-exceeded errors
<a name="otel-metrics-queries.replication-and-durability.durability-buffer-exceeded-errors"></a>

```
rate({"valkey.durability.buffer_exceeded_errors",
      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Every occurrence is a rejected write.

## Persistence
<a name="otel-metrics-queries.persistence"></a>

### RDB save in progress
<a name="otel-metrics-queries.persistence.rdb-save-in-progress"></a>

```
{"valkey.persistence.rdb.save_in_progress", "@resource.aws.elasticache.replication_group.id"="my-cluster"} == 1
```

Expected during backups and diskless replication.

## Network
<a name="otel-metrics-queries.network"></a>

### Network utilization vs the instance baseline
<a name="otel-metrics-queries.network.network-utilization-vs-the-instance-baseline"></a>

```
100 * rate({"system.network.io",
            "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
    / on ("@resource.aws.elasticache.node.id") group_left
      {"system.network.bandwidth.limit",
       "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

A ratio against the limit the instance reports, so it is comparable across node types. The limit applies to each direction separately, so each direction is compared against the whole limit.

### Inbound utilization only
<a name="otel-metrics-queries.network.inbound-utilization-only"></a>

```
100 * rate({"system.network.io", "network.io.direction"="receive",
            "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
    / on ("@resource.aws.elasticache.node.id")
      {"system.network.bandwidth.limit",
       "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

Inbound traffic is measured against the whole limit, not half of it.

### Network allowance exceedance by reason
<a name="otel-metrics-queries.network.network-allowance-exceedance-by-reason"></a>

```
sum by ("network.allowance_exceeded.reason") (
  rate({"system.network.allowance_exceeded",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

An exceedance means packets were queued or dropped.

### Inbound/outbound throughput per node
<a name="otel-metrics-queries.network.inbound-outbound-throughput-per-node"></a>

```
rate({"system.network.io", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

To compare against the limit, use [Network utilization vs the instance baseline](#otel-metrics-queries.network.network-utilization-vs-the-instance-baseline).

### Peak network utilization vs the baseline, per direction
<a name="otel-metrics-queries.network.peak-network-utilization-vs-the-baseline-per-direction"></a>

```
100 * histogram_quantile(0.99,
        {"system.network.io.rate", "@resource.aws.elasticache.replication_group.id"="my-cluster"})
    / on ("@resource.aws.elasticache.node.id") group_left
      {"system.network.bandwidth.limit", "@resource.aws.elasticache.replication_group.id"="my-cluster"}
```

The p99 of the distribution catches bursts that an averaged value smooths away.

### p99 inbound byte-rate (micro-burst detection)
<a name="otel-metrics-queries.network.p99-inbound-byte-rate-micro-burst-detection"></a>

```
histogram_quantile(0.99,
  {"system.network.io.rate", "network.io.direction"="receive",
   "@resource.aws.elasticache.replication_group.id"="my-cluster"})
```

Reveals one-second bursts that an average hides.

### p99 packet rate
<a name="otel-metrics-queries.network.p99-packet-rate"></a>

```
histogram_quantile(0.99,
  {"system.network.packet.rate", "network.io.direction"="receive",
   "@resource.aws.elasticache.replication_group.id"="my-cluster"})
```

### Packet rate per node, per direction
<a name="otel-metrics-queries.network.packet-rate-per-node-per-direction"></a>

```
rate({"system.network.packet.count", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Packet rate limits are separate from bandwidth limits. Exceeding one is reported as a `pps` allowance exceedance.

### Replication throughput of each primary
<a name="otel-metrics-queries.network.replication-throughput-of-each-primary"></a>

**Requires detailed monitoring:** `valkey.network.output.replication`

```
sum by ("@resource.aws.elasticache.node.id") (
  rate({"valkey.network.output.replication", "valkey.role"="primary",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

This counts the bytes sent to every replica, so it scales with the number of replicas. For write throughput, see [Write throughput on each primary](#otel-metrics-queries.replication-and-durability.write-throughput-on-each-primary).

### Replication share of network
<a name="otel-metrics-queries.network.replication-share-of-network"></a>

**Requires detailed monitoring:** `valkey.network.output`, `valkey.network.output.replication`

```
rate({"valkey.network.output.replication", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
/
rate({"valkey.network.output",             "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

### Inbound engine traffic
<a name="otel-metrics-queries.network.inbound-engine-traffic"></a>

**Requires detailed monitoring:** `valkey.network.input`

```
rate({"valkey.network.input", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[1m])
```

Compare against host-level network metrics to separate engine traffic from total traffic.

## Errors and rejections
<a name="otel-metrics-queries.errors-and-rejections"></a>

### Error reply rate by error code
<a name="otel-metrics-queries.errors-and-rejections.error-reply-rate-by-error-code"></a>

```
sum by ("valkey.error.type") (
  rate({"valkey.errors", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Top error codes
<a name="otel-metrics-queries.errors-and-rejections.top-error-codes"></a>

```
topk(5, sum by ("valkey.error.type") (
  rate({"valkey.errors", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])))
```

### Rejected-call rate per command
<a name="otel-metrics-queries.errors-and-rejections.rejected-call-rate-per-command"></a>

**Requires detailed monitoring:** `valkey.command.rejected_calls`

```
sum by ("valkey.command") (
  rate({"valkey.command.rejected_calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Failed-call rate per command
<a name="otel-metrics-queries.errors-and-rejections.failed-call-rate-per-command"></a>

**Requires detailed monitoring:** `valkey.command.failed_calls`

```
sum by ("valkey.command") (
  rate({"valkey.command.failed_calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

### Failed calls by command category
<a name="otel-metrics-queries.errors-and-rejections.failed-calls-by-command-category"></a>

**Requires detailed monitoring:** `valkey.command.failed_calls`

```
sum by ("valkey.command.category") (
  rate({"valkey.command.failed_calls",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

## Access control and security
<a name="otel-metrics-queries.access-control-and-security"></a>

### Access-denied rate by reason
<a name="otel-metrics-queries.access-control-and-security.access-denied-rate-by-reason"></a>

```
sum by ("valkey.acl.denied.reason") (
  rate({"valkey.acl.denied", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

A denial is either a misconfigured client or an unauthorized attempt.

### Authentication failure rate
<a name="otel-metrics-queries.access-control-and-security.authentication-failure-rate"></a>

```
sum(rate({"valkey.acl.denied", "valkey.acl.denied.reason"="auth",
          "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Sustained failures indicate either a credential problem or a brute-force attempt.

## Event loop
<a name="otel-metrics-queries.event-loop"></a>

### Event-loop utilization
<a name="otel-metrics-queries.event-loop.event-loop-utilization"></a>

**Requires detailed monitoring:** `valkey.eventloop.duration`

```
rate({"valkey.eventloop.duration", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

The fraction of time that the main thread is busy. The event loop is the engine's serialization point, so latency rises sharply as this approaches 1.

### Share of event-loop time spent executing commands
<a name="otel-metrics-queries.event-loop.share-of-event-loop-time-spent-executing-commands"></a>

**Requires detailed monitoring:** `valkey.eventloop.command.duration`, `valkey.eventloop.duration`

```
rate({"valkey.eventloop.command.duration", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
/
rate({"valkey.eventloop.duration",         "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

A falling share points to engine overhead such as replication or defragmentation.

### Average event-loop cycle time (microseconds)
<a name="otel-metrics-queries.event-loop.average-event-loop-cycle-time-microseconds"></a>

**Requires detailed monitoring:** `valkey.eventloop.cycles`, `valkey.eventloop.duration`

```
1e6 * rate({"valkey.eventloop.duration", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
    / rate({"valkey.eventloop.cycles",   "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

`1e6` converts seconds to microseconds.

### Event-loop cycle rate
<a name="otel-metrics-queries.event-loop.event-loop-cycle-rate"></a>

**Requires detailed monitoring:** `valkey.eventloop.cycles`

```
rate({"valkey.eventloop.cycles", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Read with the average cycle time: a falling cycle rate together with rising cycle duration is the signature of a stall. An idle node still shows a floor from timer activity.

### Event-loop time not spent on CPU
<a name="otel-metrics-queries.event-loop.event-loop-time-not-spent-on-cpu"></a>

**Requires detailed monitoring:** `valkey.eventloop.duration`

```
  rate({"valkey.eventloop.duration", "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
- on ("@resource.aws.elasticache.node.id")
  sum without ("cpu.mode") (
    rate({"process.cpu.time", "thread.type"="main",
          "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Event-loop duration is wall-clock time and CPU time is time on the processor, so the two normally track each other. A sustained gap means that the main thread is busy but waiting on something other than CPU, such as swap or a fork for a background save.

## Fleet-wide and cross-resource patterns
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns"></a>

### Top 10 nodes by memory across every prod replication group
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns.top-10-nodes-by-memory-across-every-prod-replication-group"></a>

```
topk(10, {"valkey.memory.used",
          "@resource.aws.elasticache.replication_group.id"=~"prod-.*"})
```

### Command rate rolled up by replication group
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns.command-rate-rolled-up-by-replication-group"></a>

```
sum by ("@resource.aws.elasticache.replication_group.id") (
  rate({"valkey.commands.processed",
        "@resource.aws.elasticache.replication_group.id"=~"prod-.*"}[5m]))
```

### Highest-error clusters in the fleet
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns.highest-error-clusters-in-the-fleet"></a>

```
topk(5, sum by ("@resource.aws.elasticache.replication_group.id") (
  rate({"valkey.errors",
        "@resource.aws.elasticache.replication_group.id"=~"prod-.*"}[5m])))
```

### Network throughput rolled up by Availability Zone
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns.network-throughput-rolled-up-by-availability-zone"></a>

```
sum by ("@resource.cloud.availability_zone_id", "network.io.direction") (
  rate({"system.network.io", "@resource.aws.elasticache.replication_group.id"=~"prod-.*"}[5m]))
```

### Write throughput of each shard
<a name="otel-metrics-queries.fleet-wide-and-cross-resource-patterns.write-throughput-of-each-shard"></a>

```
sum by ("@resource.aws.elasticache.shard.id") (
  deriv({"valkey.replication.offset", "valkey.role"="primary",
         "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Compare with [TPS of each shard](#otel-metrics-queries.throughput-and-commands.tps-of-each-shard) to see whether write traffic and total traffic are balanced the same way.