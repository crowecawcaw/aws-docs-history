# Which Metrics Should I Monitor?

The following CloudWatch metrics offer good insight into MemoryDB performance. In most cases, we
recommend that you set CloudWatch alarms for these metrics so that you can take corrective
action before performance issues occur.

###### Metrics to Monitor

- [CPUUtilization](#metrics-cpu-utilization "#metrics-cpu-utilization")
- [EngineCPUUtilization](#metrics-engine-cpu-utilization "#metrics-engine-cpu-utilization")
- [SwapUsage](#metrics-swap-usage "#metrics-swap-usage")
- [Evictions](#metrics-evictions "#metrics-evictions")
- [CurrConnections](#metrics-curr-connections "#metrics-curr-connections")
- [Memory](#metrics-memory "#metrics-memory")
- [Network](#metrics-network "#metrics-network")
- [Latency](#metrics-latency "#metrics-latency")
- [Replication](#metrics-replication "#metrics-replication")

## CPUUtilization

This is a host-level metric reported as a percentage. For more information, see [Host-Level Metrics](metrics.md "metrics.md").

For smaller node types with 2vCPUs or less, use the `CPUUtilization` metric to monitor your workload.

Generally speaking, we suggest you set your threshold at 90% of your available CPU. Because Valkey and Redis OSS are single-threaded, the actual threshold value should be calculated as a fraction of the node's total capacity. For example, suppose you are using a node type that has two cores.
In this case, the threshold for CPUUtilization would be 90/2, or 45%. To find the number of cores (vCPUs) your node type has, see [MemoryDB Pricing](https://aws.amazon.com/memorydb/pricing/?p=ps "https://aws.amazon.com/memorydb/pricing/?p=ps").

You will need to determine your own threshold, based on the number of cores in the node that you are using. If you exceed this threshold, and your main workload is
from read requests, scale your cluster out by adding read replicas. If the
main workload is from write requests, we recommend that you add more shards to distribute the write workload across more primary nodes.

###### Tip

Instead of using the Host-Level metric `CPUUtilization`, you might be able to
use the metric `EngineCPUUtilization`, which reports the percentage of usage on the Valkey or Redis OSS engine core. To see if this metric is available on your nodes and for more information, see
[Metrics for MemoryDB](metrics.md "metrics.md").

For larger node types with 4vCPUs or more, you may want to use the `EngineCPUUtilization` metric, which reports the percentage of usage on the Valkey or Redis OSS engine core. To see if this metric is available on your nodes and for more information, see [Metrics for MemoryDB](metrics.md "metrics.md").

## EngineCPUUtilization

For larger node types with 4vCPUs or more, you may want to use the `EngineCPUUtilization` metric, which reports the percentage of usage on the Valkey or Redis OSS engine core. To see if this metric is available on your nodes and for more information, see [Metrics for MemoryDB](metrics.md "metrics.md").

## SwapUsage

This is a host-level metric reported in bytes. For more information, see [Host-Level Metrics](metrics.md "metrics.md").

If either the `FreeableMemory` CloudWatch metric is close to 0 (i.e., below 100MB), or the `SwapUsage` metric is greater than the `FreeableMemory` metric, then a node could be under memory pressure.

## Evictions

This is a engine metric. We recommend that you determine your own alarm
threshold for this metric based on your application needs.

## CurrConnections

This is a engine metric. We recommend that you determine your own alarm threshold for
this metric based on your application needs.

An increasing number of _CurrConnections_ might indicate a problem with your
application; you will need to investigate the application behavior to address this issue.

## Memory

Memory is a core aspect of Valkey and of Redis OSS. Understanding the memory utilization of your cluster is necessary to avoid data loss and accommodate future growth of your dataset.

Statistics about the memory utilization of a node are available in the memory section of the [INFO](https://valkey.io/commands/info "https://valkey.io/commands/info") command.

## Network

One of the determining factors for the network bandwidth capacity of your cluster is the node type you have selected. For more information about the network
capacity of your node, see [Amazon MemoryDB pricing](https://aws.amazon.com/memorydb/pricing/ "https://aws.amazon.com/memorydb/pricing/").

## Latency

The latency metrics `SuccessfulWriteRequestLatency` and `SuccessfulReadRequestLatency` measure the total time that MemoryDB for the Valkey engine takes to respond to a request.

###### Note

Inflated values for `SuccessfulWriteRequestLatency` and `SuccessfulReadRequestLatency` metrics may occur when using Valkey pipelining with CLIENT REPLY enabled on the Valkey client. Valkey pipelining is a technique for improving performance by issuing multiple commands at once, without waiting for the response to each individual command. To avoid inflated values, we recommend configuring your Redis client to pipeline commands with [CLIENT REPLY OFF](https://valkey.io/commands/client-reply/ "https://valkey.io/commands/client-reply/").

## Replication

The volume of data being replicated is visible via the `ReplicationBytes` metric. You can monitor `MaxReplicationThroughput` against the replication capacity throughput.
It is recommended to add more shards when reaching the maximum replication capacity throughput.

`ReplicationDelayedWriteCommands` can also indicate if the workload is exceeding the maximum replication capacity throughput.

For more information about replication in MemoryDB, see [Understanding MemoryDB replication](replication.md "replication.md")
