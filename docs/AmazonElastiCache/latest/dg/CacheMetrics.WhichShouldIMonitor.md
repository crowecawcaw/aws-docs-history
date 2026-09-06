

# Which Metrics Should I Monitor?
<a name="CacheMetrics.WhichShouldIMonitor"></a>

The following CloudWatch metrics offer good insight into ElastiCache performance. In most cases, we recommend that you set CloudWatch alarms for these metrics so that you can take corrective action before performance issues occur.

**Topics**
+ [CPUUtilization](#metrics-cpu-utilization)
+ [EngineCPUUtilization](#metrics-engine-cpu-utilization)
+ [SwapUsage (Valkey and Redis OSS)](#metrics-swap-usage)
+ [Evictions](#metrics-evictions)
+ [CurrConnections](#metrics-curr-connections)
+ [Memory (Valkey and Redis OSS)](#metrics-memory)
+ [Network](#metrics-network)
+ [Latency](#metrics-latency)
+ [Replication](#metrics-replication)
+ [Traffic Management (Valkey and Redis OSS)](#traffic-management)

## CPUUtilization
<a name="metrics-cpu-utilization"></a>

This is a host-level metric reported as a percentage. For more information, see [Host-Level Metrics](CacheMetrics.HostLevel.md).

**Valkey and Redis OSS**

 For smaller node types with 2vCPUs or less, use the `CPUUtilization ` metric to monitor your workload.

Generally speaking, we suggest you set your threshold at 90% of your available CPU. Because Valkey and Redis OSS are both single-threaded, the actual threshold value should be calculated as a fraction of the node's total capacity. For example, suppose you are using a node type that has two cores. In this case, the threshold for CPUUtilization would be 90/2, or 45%. 

You will need to determine your own threshold, based on the number of cores in the cache node that you are using. If you exceed this threshold, and your main workload is from read requests, scale your cluster out by adding read replicas. If the main workload is from write requests, depending on your cluster configuration, we recommend that you:
+ **Valkey or Redis OSS (cluster mode disabled) clusters:** scale up by using a larger cache instance type.
+ **Valkey or Redis OSS (cluster mode enabled) clusters:** add more shards to distribute the write workload across more primary nodes.

**Tip**  
Instead of using the Host-Level metric `CPUUtilization`, Valkey and Redis OSS users might be able to use the metric `EngineCPUUtilization`, which reports the percentage of usage on the Valkey or Redis OSS engine core. To see if this metric is available on your nodes and for more information, see [Metrics for Valkey and Redis OSS](CacheMetrics.Redis.md).

For larger node types with 4vCPUs or more, you may want to use the `EngineCPUUtilization` metric, which reports the percentage of usage on the Valkey or Redis OSS engine core. To see if this metric is available on your nodes and for more information, see [Metrics for Redis OSS](CacheMetrics.Redis.md).

**Memcached**

Because Memcached is multi-threaded, this metric can be as high as 90%. If you exceed this threshold, scale your cluster up by using a larger cache node type or scale out by adding more cache nodes.

## EngineCPUUtilization
<a name="metrics-engine-cpu-utilization"></a>

For larger node types with 4vCPUs or more, you may want to use the `EngineCPUUtilization` metric, which reports the percentage of usage on the Redis OSS engine core. To see if this metric is available on your nodes and for more information, see [Metrics for Valkey and Redis OSS](CacheMetrics.Redis.md).

For more information, see the **CPUs** section at [Monitoring best practices with Amazon ElastiCache for Redis OSS using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## SwapUsage (Valkey and Redis OSS)
<a name="metrics-swap-usage"></a>

This is a host-level metric reported in bytes. For more information, see [Host-Level Metrics](CacheMetrics.HostLevel.md).

The `FreeableMemory` CloudWatch metric being close to 0 (i.e., below 100MB) or `SwapUsage` metric greater than the `FreeableMemory` metric indicates a node is under memory pressure. If this happens, see the following topics:
+ [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.BGSAVE.md)
+ [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md)

## Evictions
<a name="metrics-evictions"></a>

This is a cache engine metric. We recommend that you determine your own alarm threshold for this metric based on your application needs.

If you are using Memcached and exceed your chosen threshold, scale your cluster up by using a larger node type or scale out by adding more nodes.

## CurrConnections
<a name="metrics-curr-connections"></a>

This is a cache engine metric. We recommend that you determine your own alarm threshold for this metric based on your application needs.

An increasing number of *CurrConnections* might indicate a problem with your application; you will need to investigate the application behavior to address this issue. 

For more information, see the **Connections** section at [Monitoring best practices with Amazon ElastiCache for Redis OSS using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## Memory (Valkey and Redis OSS)
<a name="metrics-memory"></a>

Memory is a core aspect of Valkey and Redis OSS. Understanding the memory utilization of your cluster is necessary to avoid data loss and accommodate future growth of your dataset. Statistics about the memory utilization of a node are available in the memory section of the [INFO](https://valkey.io/commands/info) command.

For more information, see the **Memory** section at [Monitoring best practices with Amazon ElastiCache for Redis OSS using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## Network
<a name="metrics-network"></a>

One of the determining factors for the network bandwidth capacity of your cluster is the node type you have selected. For more information about the network capacity of your node, see [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/).

For more information, see the **Network** section at [Monitoring best practices with Amazon ElastiCache for Redis OSS using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## Latency
<a name="metrics-latency"></a>

Measuring response time for an ElastiCache for Valkey instance can be approached in various ways depending on the level of granularity required. The key stages that contribute to the overall server-side response time for ElastiCache for Valkey are command pre-processing, command execution, and command post-processing. 

 Command-specific latency metrics derived from the Valkey [INFO](https://valkey.io/commands/info) command such as GetTypeCmdsLatency and SetTypeCmdsLatency metric focus specifically on executing the core command logic for the Valkey command. These metrics will be helpful if your use case is to determine the command execution time or aggregated latencies per data structure.

The latency metrics `SuccessfulWriteRequestLatency` and `SuccessfulReadRequestLatency` measure the total time that the ElastiCache for Valkey engine takes to respond to a request.

**Note**  
Inflated values for `SuccessfulWriteRequestLatency` and `SuccessfulReadRequestLatency` metrics can occur when using Valkey pipelining with CLIENT REPLY enabled on the Valkey client. Valkey pipelining is a technique for improving performance by issuing multiple commands at once, without waiting for the response to each individual command. To avoid inflated values, we recommend configuring your Valkey client to pipeline commands with [CLIENT REPLY OFF](https://valkey.io/commands/client-reply/).

For more information, see the **Latency** section at [Monitoring best practices with Amazon ElastiCache using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## Replication
<a name="metrics-replication"></a>

The volume of data being replicated is visible via the `ReplicationBytes` metric. Although this metric is representative of the write load on the replication group, it doesn't provide insights into replication health. For this purpose, you can use the `ReplicationLag` metric. 

For more information, see the **Replication** section at [Monitoring best practices with Amazon ElastiCache for Redis OSS using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/).

## Traffic Management (Valkey and Redis OSS)
<a name="traffic-management"></a>

 ElastiCache for Redis OSS automatically manages traffic against a node when more incoming commands are sent to the node than can be processed by Valkey or Redis OSS. This is done to maintain optimal operation and stability of the engine. 

 When traffic is actively managed on a node, the metric `TrafficManagementActive` will emit data points of 1. This indicates that the node may be underscaled for the workload being provided. If this metric remains 1 for long periods of time, evaluate the cluster to decide if scaling up or scaling out is necessary. 

 For more information, see the `TrafficManagementActive` metric on the [Metrics](CacheMetrics.Redis.md) page.