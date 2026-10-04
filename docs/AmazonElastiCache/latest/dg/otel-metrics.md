

# Monitoring ElastiCache with OpenTelemetry metrics
<a name="otel-metrics"></a>

Amazon ElastiCache emits OpenTelemetry (OTLP) metrics for node-based Valkey replication groups to Amazon CloudWatch. These metrics give you a detailed view of your replication group, with a broad set of metrics from the cache engine and the host, rich attributes for filtering and aggregation, and support for querying with PromQL.

A core set of vended metrics is emitted automatically, at 60-second granularity, at no additional cost. You can also select any metric with a [resource metrics configuration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-metrics-configuration.html) to be emitted at 15-second granularity. Selected metrics are charged by CloudWatch. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## How OpenTelemetry metrics work
<a name="otel-metrics.how-it-works"></a>

Each node in your replication group collects telemetry from the cache engine and from the host that the node runs on, and emits it to CloudWatch as OpenTelemetry metrics. Metrics are emitted per node, and every datapoint carries attributes that identify the account, Region, Availability Zone, replication group, shard, and node that produced it.

Vended metrics are emitted automatically, at 60-second granularity, as soon as the replication group is running. You do not need to configure anything, and they are not charged.

Detailed metrics are emitted only while you select them. To begin emitting them, create a resource metrics configuration for the replication group and list the metrics you want. Those metrics are then emitted at 15-second granularity and charged by CloudWatch. Selecting a metric that is already vended raises its granularity from 60 seconds to 15 seconds, and it is charged while it remains selected. For more information, see [Turning on detailed monitoring](#otel-metrics.detailed-monitoring).

To see which metrics are emitted automatically, see [OpenTelemetry metrics reference for Amazon ElastiCache](otel-metrics-reference.md).

After the metrics reach CloudWatch, you work with them the same way as any other OpenTelemetry metrics in CloudWatch. You can query them with PromQL, explore them in Query Studio, create alarms, and build your own dashboards. For more information, see [Querying your metrics](#otel-metrics.querying).

## Metric attributes
<a name="otel-metrics.attributes"></a>

Every datapoint carries attributes that let you filter and aggregate your metrics at query time. Attributes fall into the following categories.
+ **Resource attributes** identify the AWS account, Region, and Availability Zone, and the replication group, shard, and node that produced the datapoint.
+ **Instrumentation scope attributes** identify ElastiCache as the source of the metric.
+ **Datapoint attributes** provide per-metric dimensions. Every metric reports the replication role of the node that emitted it, and many metrics add attributes that break the metric down further, such as a command name or a network direction.

For the complete list of attributes and the values they take, see [OpenTelemetry metrics reference for Amazon ElastiCache](otel-metrics-reference.md).

## Supported configurations
<a name="otel-metrics.supported"></a>

All node-based Valkey replication groups can emit OpenTelemetry metrics, on any Valkey version, with the exception of replication groups on AWS Outposts. Serverless caches, Redis OSS, and Memcached do not emit OpenTelemetry metrics.

In a global datastore, select metrics separately for each regional replication group.

## Turning on detailed monitoring
<a name="otel-metrics.detailed-monitoring"></a>

Turn on detailed monitoring when you need a metric that is not emitted automatically, or a granularity of 15 seconds.

To turn on detailed monitoring, create a resource metrics configuration for the replication group, identified by its ARN. A replication group can have only one configuration at a time. For more information about resource metrics configurations, see [CloudWatch detailed monitoring for OpenTelemetry metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-metrics-configuration.html) in the *Amazon CloudWatch User Guide*.

**Note**  
Creating, retrieving, updating, and deleting a configuration requires the corresponding `cloudwatch:*ResourceMetricsConfiguration` permissions. Because these operations do not support resource-level permissions, an IAM policy must use `"Resource": "*"`. Scope access with the `cloudwatch:ResourceArn` condition key instead. These are Amazon CloudWatch API operations, not ElastiCache API operations. For the required permissions and for more information, see [CloudWatch detailed monitoring for OpenTelemetry metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-metrics-configuration.html) in the *Amazon CloudWatch User Guide*.

### Using the console
<a name="otel-metrics.detailed-monitoring.using-the-console"></a>

You can turn on detailed monitoring for an existing replication group from its **Metrics** tab, or while you create a replication group.

**To turn on detailed monitoring for an existing replication group**

1. Open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/), and choose your replication group.

1. On the **Metrics** tab, choose **Detailed**.

1. Choose **Configure detailed metrics**.

1. Select the metrics that you want the replication group to emit, then save your changes.

Until you select metrics, the **Detailed** view shows **No detailed metrics configured**.

While you create a replication group, choose **Detailed monitoring** in the **Monitoring** section, then select your metrics.

### Using the AWS CLI
<a name="otel-metrics.detailed-monitoring.using-the-aws-cli"></a>

To emit specific metrics, create a configuration with the `--metric-selections` parameter and list the metrics by name.

```
aws cloudwatch create-resource-metrics-configuration \
    --resource-arn arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster \
    --metric-selections '[{"IncludeMetrics": ["valkey.memory.used", "valkey.commands.processed"]}]'
```

If you omit `--metric-selections`, all available metrics are selected. This includes every vended metric, which moves each one to 15-second granularity and starts charging for it. Because charges are based on the volume of datapoints emitted, we recommend that you select only the metrics that you need.

```
aws cloudwatch create-resource-metrics-configuration \
    --resource-arn arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster
```

To see which metrics a replication group is currently emitting, retrieve its configuration. If no configuration exists, the command returns an error.

```
aws cloudwatch get-resource-metrics-configuration \
    --resource-arn arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster
```

To change which metrics are selected, update the configuration.

```
aws cloudwatch update-resource-metrics-configuration \
    --resource-arn arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster \
    --metric-selections '[{"IncludeMetrics": ["valkey.memory.used", "valkey.keyspace.hits"]}]'
```

**Important**  
The `--metric-selections` parameter completely replaces the previous value. To add a metric to an existing selection, list every metric that you want to emit, not only the new one.

To stop emitting metrics, delete the configuration.

```
aws cloudwatch delete-resource-metrics-configuration \
    --resource-arn arn:aws:elasticache:us-east-1:123456789012:replicationgroup:my-cluster
```

### After you turn on detailed monitoring
<a name="otel-metrics.detailed-monitoring.after-you-turn-on-detailed-monitoring"></a>

Changes to a resource metrics configuration take a few minutes to take effect.

When you delete a replication group, its resource metrics configuration is deleted automatically.

**Note**  
Charges are based on the volume of datapoints emitted for the metrics you select, not on the number of metrics you select. High-cardinality metrics that are broken down by an attribute, such as `valkey.command.calls`, emit a datapoint for each attribute value, so their cost depends on your workload. Metrics that you have not selected are not charged.

## Querying your metrics
<a name="otel-metrics.querying"></a>

You query ElastiCache OpenTelemetry metrics using PromQL, which supports query-time aggregation and calculation across your replication groups, shards, and nodes. You can run queries interactively in Query Studio, use them to create CloudWatch alarms, and add them to dashboards. You can also query them from Amazon Managed Grafana by adding a Prometheus data source that points to the CloudWatch PromQL endpoint.

For more information, see the following topics in the *Amazon CloudWatch User Guide*.
+ [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html)
+ [PromQL querying](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-Querying.html)

For information about querying from Amazon Managed Grafana, see [Query Amazon CloudWatch metrics using PromQL](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-promql.html) in the *Amazon Managed Grafana User Guide*.

**Note**  
Use a time range that contains multiple datapoints. A shorter range can return noisy data, or no data at all. We recommend a time range of at least `[5m]` for metrics emitted every 60 seconds, or at least `[1m]` for metrics emitted every 15 seconds.

### Key PromQL capabilities
<a name="otel-metrics.querying.key-promql-capabilities"></a>

The following example queries demonstrate key operations that PromQL enables for observability. Replace `my-cluster` with your replication group ID and `my-cluster-0001-001` with a node ID.

For a larger set of ready-to-copy queries organized by topic, see [Example queries for common monitoring tasks](otel-metrics-queries.md). For the full list of functions and operators that CloudWatch supports, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) in the *Amazon CloudWatch User Guide*.

#### Select a time series: Memory used by a node
<a name="otel-metrics.querying.key-promql-capabilities.select-a-time-series-memory-used-by-a-node"></a>

```
{"valkey.memory.used",
 "@resource.aws.elasticache.replication_group.id"="my-cluster",
 "@resource.aws.elasticache.node.id"="my-cluster-0001-001"}
```

A query is a metric name followed by any number of attribute matchers, enclosed in braces. Names are quoted because they contain dots, and resource attributes take the `@resource.` prefix. Omitting the node matcher returns one time series per node.

#### Basic operations: Memory used by a node as a percentage of its limit
<a name="otel-metrics.querying.key-promql-capabilities.basic-operations-memory-used-by-a-node-as-a-percentage-of-its-limit"></a>

```
100 * {"valkey.memory.used",
       "@resource.aws.elasticache.replication_group.id"="my-cluster",
       "@resource.aws.elasticache.node.id"="my-cluster-0001-001"}
    / {"valkey.memory.max",
       "@resource.aws.elasticache.replication_group.id"="my-cluster",
       "@resource.aws.elasticache.node.id"="my-cluster-0001-001"}
```

PromQL pairs up time series that have identical attributes and calculates a result for each pair. Both metrics here are emitted by the same node, so they pair up; if the two sides carried different attributes, the query would return no result.

#### Convert a counter to a rate: Inbound network throughput of each node
<a name="otel-metrics.querying.key-promql-capabilities.convert-a-counter-to-a-rate-inbound-network-throughput-of-each-node"></a>

```
rate({"system.network.io",
      "network.io.direction"="receive",
      "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

Because the query matches only on the replication group, it returns one series for each node, and all of them appear on the same chart. Counters are cumulative, so `rate` converts one into a per-second rate over the time range in brackets. It also accounts for the total resetting to zero when a node restarts or fails over.

#### Aggregations
<a name="otel-metrics.querying.key-promql-capabilities.aggregations"></a>

Aggregation operators combine several time series into fewer series, either collapsing them into a single result or grouping them into buckets.

##### Aggregate all matching time series: Total memory used across a replication group
<a name="otel-metrics.querying.key-promql-capabilities.aggregations.aggregate-all-matching-time-series-total-memory-used-across-a-replication-group"></a>

```
sum({"valkey.memory.used",
     "valkey.role"="primary",
     "@resource.aws.elasticache.replication_group.id"="my-cluster"})
```

Filtering on `valkey.role` counts only primaries, which hold the data that every replica in their shard replicates. `valkey.role` is a datapoint attribute, so unlike the resource attributes it takes no prefix.

##### Aggregate into buckets: Transactions per second (TPS) of each shard
<a name="otel-metrics.querying.key-promql-capabilities.aggregations.aggregate-into-buckets-transactions-per-second-tps-of-each-shard"></a>

```
sum by ("@resource.aws.elasticache.shard.id") (
  rate({"valkey.commands.processed",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

A `by` clause aggregates into groups rather than into a single value, so this query returns one TPS figure for each shard, combining every node in that shard. A `by` clause also keeps only the attributes it names and discards the rest, so these results no longer identify the Region or account. Use a `without` clause to keep every attribute except the ones you name.

##### Aggregate all but one attribute: CPU utilization of the cache engine on each node
<a name="otel-metrics.querying.key-promql-capabilities.aggregations.aggregate-all-but-one-attribute-cpu-utilization-of-the-cache-engine-on-each-node"></a>

```
100 * sum without ("cpu.mode") (
        rate({"process.cpu.time",
              "thread.type"="main",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

`rate` converts cumulative CPU seconds into CPU seconds per second, and summing `without` the `cpu.mode` attribute combines user and system time, giving the percentage of a single vCPU consumed by the engine's main thread. Using `without` rather than `by` keeps the resource attributes, so each node reports separately. Only the main thread is reported, so this query does not include CPU time consumed by I/O threads.

#### Combine functions, aggregations and operations: Average latency of each command
<a name="otel-metrics.querying.key-promql-capabilities.combine-functions-aggregations-and-operations-average-latency-of-each-command"></a>

```
1e6 * sum by ("valkey.command") (
        rate({"valkey.command.duration",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
    / (sum by ("valkey.command") (
        rate({"valkey.command.calls",
              "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])) > 0)
```

ElastiCache emits the cumulative execution time and the cumulative call count for each command, so dividing one rate by the other gives the average duration of a call, in microseconds. Both sides are aggregated by `valkey.command` so that each command's execution time is divided by its own call count, and the `> 0` comparison excludes commands that were not called during the time range.

#### Match attributes with a regular expression: TPS for a set of commands across replication groups
<a name="otel-metrics.querying.key-promql-capabilities.match-attributes-with-a-regular-expression-tps-for-a-set-of-commands-across-replication-groups"></a>

```
sum by ("valkey.command") (
  rate({"valkey.command.calls",
        "valkey.command"=~"GET|MGET|HGET|LRANGE",
        "@resource.aws.elasticache.replication_group.id"=~"prod-.*"}[5m]))
```

The `=~` operator matches an attribute against a regular expression, and works on any attribute; use `!~` to exclude values that match. Expressions are anchored, so `"valkey.command"=~"GET"` matches only `GET` and not `GETRANGE` — end an expression with `.*` to match a prefix.

#### Compare across nodes: Each node's share of its shard's traffic
<a name="otel-metrics.querying.key-promql-capabilities.compare-across-nodes-each-node-s-share-of-its-shard-s-traffic"></a>

```
  rate({"valkey.commands.processed",
        "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
/ on ("@resource.aws.elasticache.shard.id") group_left
  sum by ("@resource.aws.elasticache.shard.id") (
    rate({"valkey.commands.processed",
          "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m]))
```

Dividing each node's command rate by the total rate of its shard gives the share of the shard's traffic that each node handles. Aggregating by shard reduces the denominator to one value per shard, and `on` restricts the match to the shard attribute so that each node is divided by the total of its own shard. `group_left` allows that single shard total to be matched against every node in the shard.

#### Other useful functions
<a name="otel-metrics.querying.key-promql-capabilities.other-useful-functions"></a>

##### Read a percentile from a histogram: Peak inbound network throughput
<a name="otel-metrics.querying.key-promql-capabilities.other-useful-functions.read-a-percentile-from-a-histogram-peak-inbound-network-throughput"></a>

```
histogram_quantile(0.99,
  {"system.network.io.rate",
   "network.io.direction"="receive",
   "@resource.aws.elasticache.replication_group.id"="my-cluster"})
```

Two metrics, `system.network.io.rate` and `system.network.packet.rate`, are exponential histograms rather than single values. The network interface is sampled once a second, and each datapoint carries the distribution of those per-second rates, so `histogram_quantile` reads a percentile from it. The first argument is the quantile, where `0.99` is the 99th percentile. Reading a high percentile reveals one-second bursts that an averaged value would smooth away.

##### Smooth a series, and find a peak: Fragmentation over a window, and peak memory over a day
<a name="otel-metrics.querying.key-promql-capabilities.other-useful-functions.smooth-a-series-and-find-a-peak-fragmentation-over-a-window-and-peak-memory-over-a-day"></a>

```
avg_over_time(
  {"valkey.memory.allocator_frag_ratio",
   "@resource.aws.elasticache.replication_group.id"="my-cluster"}[5m])
```

`avg_over_time` averages a metric across a time window, which suppresses brief spikes that would otherwise dominate a chart or trigger an alarm. `max_over_time` is its counterpart and reports the highest value in the window, which is how you find a peak over a period that you choose:

```
max_over_time(
  {"valkey.memory.used",
   "@resource.aws.elasticache.replication_group.id"="my-cluster"}[24h])
```

Both functions require a range in square brackets, and the range is limited to 7 days.

##### Find highest values: The busiest nodes across every replication group
<a name="otel-metrics.querying.key-promql-capabilities.other-useful-functions.find-highest-values-the-busiest-nodes-across-every-replication-group"></a>

```
topk(5,
  sum without ("cpu.mode") (
    rate({"process.cpu.time", "thread.type"="main"}[5m])))
```

`topk` returns only the highest N series, which turns a query that would return hundreds of series into a short, readable list. Because this query has no replication group matcher, it ranks nodes across every replication group that emits the metric. `bottomk` does the same for the lowest values.

**Note**  
A query can return at most 500 time series. On a large replication group, a query that breaks results down by both node and command can exceed that limit and return a truncated response. Aggregate the result, or narrow it with a more specific label matcher.

### Creating alarms from queries
<a name="otel-metrics.alarms"></a>

You can create a CloudWatch alarm from a PromQL query, which lets you alarm on values that are calculated at query time, such as a percentage of a limit or a comparison between nodes.

Three characteristics of a PromQL alarm affect how you write the query.

**The threshold is part of the query.** You add a comparison operator and a value to the query, and the query returns only the series that satisfy the comparison. For example, this query returns a series only for nodes that are using more than 90 percent of their memory limit:

```
100 * {"valkey.memory.used",    "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    / {"valkey.memory.max",     "@resource.aws.elasticache.replication_group.id"="my-cluster"}
    > 90
```

**One alarm can watch every node.** Each series that the query returns is tracked independently as a contributor, and the alarm enters the `ALARM` state when any contributor is breaching. You do not need a separate alarm for each node, and you do not need to aggregate the query to a single value. The attributes of a breaching series identify which node or shard is responsible.

**You control sensitivity with durations.** A PromQL alarm takes an evaluation interval, a pending period, and a recovery period:


| Setting | Effect | 
| --- | --- | 
| Evaluation interval | How often the query runs. Valid values are 10, 20, 30, or any multiple of 60, up to 3600 seconds | 
| Pending period | How long a contributor must breach continuously before the alarm enters the ALARM state | 
| Recovery period | How long a contributor must stop breaching before it returns to the OK state | 

The following command creates an alarm from the memory query above.

```
aws cloudwatch put-metric-alarm \
    --alarm-name my-cluster-memory-high \
    --evaluation-criteria '{"PromQLCriteria":{"Query":"<query>","PendingPeriod":300,"RecoveryPeriod":600}}' \
    --evaluation-interval 60
```

**Note**  
Set the evaluation interval no shorter than the interval at which the metric is emitted. A shorter interval re-evaluates the same datapoints. For a vended metric, use 60 seconds or longer. The range in a query, such as `[5m]`, sets how much data each evaluation covers, not how often the alarm evaluates, so an alarm can evaluate more often than its range.

Use the pending period, rather than a long averaging window inside the query, to keep brief spikes from raising an alarm. A pending period of 300 seconds requires 5 minutes of continuous breaching, which is easier to reason about than smoothing the query.

Because a contributor is considered recovered once its series stops being returned, an alarm also recovers when the series disappears for any other reason. A metric that is broken down by an attribute only produces a series while your workload generates that attribute value, so an alarm on a specific command or error type returns to `OK` when your workload stops using it.

### Learning more about PromQL
<a name="otel-metrics.querying.learning-more-about-promql"></a>

CloudWatch PromQL supports many more functions and features than these examples show, including additional aggregation operators, comparisons against earlier time periods, and functions for smoothing and forecasting. For the full language reference and further examples, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) and [PromQL querying](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-Querying.html) in the *Amazon CloudWatch User Guide*.

## Pricing
<a name="otel-metrics.pricing"></a>

Vended metrics are emitted at no additional cost. Metrics that you select for detailed monitoring are billed by Amazon CloudWatch by the volume of datapoints emitted. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).