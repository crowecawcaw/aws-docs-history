# Choosing your node size

The node size you select for your ElastiCache cluster impacts costs, performance, and fault tolerance.

## Node size (Valkey and Redis OSS)

For information about the benefits of Graviton processors, see [AWS Graviton
Processor](https://aws.amazon.com/pm/ec2-graviton/ "https://aws.amazon.com/pm/ec2-graviton/").

Answering the following questions can help you determine the minimum node type you
need for your Valkey or Redis OSS implementation:

- Do you expect throughput-bound workloads with multiple client
  connections?

If this is the case and you're running Redis OSS version 5.0.6 or higher, you can
get better throughput and latency with our enhanced I/O feature, where available
CPUs are used for offloading the client connections, on behalf of the Redis OSS engine. If you're running Redis OSS version 7.0.4 or higher, on top of enhanced I/O,
you will get additional acceleration with enhanced I/O multiplexing, where each
dedicated network IO thread pipelines commands from multiple clients into the
Redis OSS engine, taking advantage of Redis OSS' ability to efficiently process commands
in batches. In ElastiCache for Redis OSS v7.1 and above, we extended the enhanced I/O
threads functionality to also handle the presentation layer logic. By
presentation layer, what we mean is that Enhanced I/O threads are now not only
reading client input, but also parsing the input into Redis OSS binary command
format, which is then forwarded to the main thread for execution, providing
performance gain. Refer to the [blog post](https://aws.amazon.com/blogs/database/achieve-over-500-million-requests-per-second-per-cluster-with-amazon-elasticache-for-redis-7-1/ "https://aws.amazon.com/blogs/database/achieve-over-500-million-requests-per-second-per-cluster-with-amazon-elasticache-for-redis-7-1/") and the [supported versions](VersionManagement.md#supported-engine-versions "VersionManagement.md#supported-engine-versions")
page for additional details.

- Do you have workloads that access a small percentage of their data
  regularly?

If this is the case and you are running on Redis OSS engine version 6.2 or later,
you can leverage data tiering by choosing the r6gd node type. With data tiering,
least-recently used data is stored in SSD. When it is retrieved there is a small
latency cost, which is balanced by cost savings. For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").

For more information, see [Supported node types](CacheNodes.md "CacheNodes.md").

- How much total memory do you need for your data?

To get a general estimate, take the size of the items that you want to cache.
Multiply this size by the number of items that you want to keep in the cache at
the same time. To get a reasonable estimation of the item size, first serialize
your cache items, then count the characters. Then divide this over the number of
shards in your cluster.

For more information, see [Supported node types](CacheNodes.md "CacheNodes.md").

- What version of Redis OSS are you running?

Redis OSS versions before 2.8.22 require you to reserve more memory for failover,
snapshot, synchronizing, and promoting a replica to primary operations. This
requirement occurs because you must have sufficient memory available for all
writes that occur during the process.

Redis OSS version 2.8.22 and later use a forkless save process that requires less
available memory than the earlier process.

For more information, see the following:

    + [How synchronization and backup are implemented](Replication.Redis.md "Replication.Redis.md")
    + [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md")

- How write-heavy is your application?

Write heavy applications can require significantly more available memory,
memory not used by data, when taking snapshots or failing over. Whenever the
`BGSAVE` process is performed, you must have sufficient memory
that is unused by data to accommodate all the writes that transpire during the
`BGSAVE` process. Examples are when taking a snapshot, when
syncing a primary cluster with a replica in a cluster, and when enabling the
append-only file (AOF) feature. Another is when promoting a replica to primary
(if you have Multi-AZ enabled). The worst case is when all of your data is
rewritten during the process. In this case, you need a node instance size with
twice as much memory as needed for data alone.

For more detailed information, see [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md").

- Will your implementation be a standalone Valkey or Redis OSS (cluster mode disabled) cluster, or a
  Valkey or Redis OSS (cluster mode enabled) cluster with multiple shards?

###### Valkey or Redis OSS (cluster mode disabled) cluster

If you're implementing a Valkey or Redis OSS (cluster mode disabled) cluster, your node type must be
able to accommodate all your data plus the necessary overhead as described
in the previous bullet.

For example, suppose that you estimate that the total size of all your items
is 12 GB. In this case, you can use a `cache.m3.xlarge` node with
13.3 GB of memory or a `cache.r3.large` node with 13.5 GB of memory.
However, you might need more memory for `BGSAVE` operations. If your
application is write-heavy, double the memory requirements to at least 24 GB.
Thus, use either a `cache.m3.2xlarge` with 27.9 GB of memory or a
`cache.r3.xlarge` with 30.5 GB of memory.

###### Valkey or Redis OSS (cluster mode enabled) with multiple shards

If you're implementing a Valkey or Redis OSS (cluster mode enabled) cluster with multiple shards, then
the node type must be able to accommodate `bytes-for-data-and-overhead
 / number-of-shards` bytes of data.

For example, suppose that you estimate that the total size of all your items
to be 12 GB and you have two shards. In this case, you can use a
`cache.m3.large` node with 6.05 GB of memory (12 GB / 2).
However, you might need more memory for `BGSAVE` operations. If your
application is write-heavy, double the memory requirements to at least 12 GB per
shard. Thus, use either a `cache.m3.xlarge` with 13.3 GB of memory or
a `cache.r3.large` with 13.5 GB of memory.

- Are you using Local Zones?

[Local
Zones](Local_zones.md "Local_zones.md") enable you to place resources such as an ElastiCache cluster in
multiple locations close to your users. But when you choose your node size,
be aware that the available node sizes are limited to the following at this
time, regardless of capacity requirements:

    + Current generation:


    **M5 node types:**
    `cache.m5.large`, `cache.m5.xlarge`,
     `cache.m5.2xlarge`, `cache.m5.4xlarge`,
     `cache.m5.12xlarge`, `cache.m5.24xlarge`



    **R5 node types:**
    `cache.r5.large`, `cache.r5.xlarge`,
     `cache.r5.2xlarge`, `cache.r5.4xlarge`,
     `cache.r5.12xlarge`,
     `cache.r5.24xlarge`


    **T3 node types:**
    `cache.t3.micro`, `cache.t3.small`,
     `cache.t3.medium`

While your cluster is running, you can monitor the memory usage, processor
utilization, cache hits, and cache misses metrics that are published to CloudWatch. You might
notice that your cluster doesn't have the hit rate that you want or that keys are
being evicted too often. In these cases, you can choose a different node size with
larger CPU and memory specifications.

When monitoring CPU usage, remember Valkey and Redis OSS are single-threaded. Thus, multiply the
reported CPU usage by the number of CPU cores to get that actual usage. For example, a
four-core CPU reporting a 20-percent usage rate is actually the one core Redis OSS is
running at 80 percent utilization.

## Node size (Memcached)

Memcached clusters contain one or more nodes with the cluster's data partitioned
across the nodes. Because of this, the memory needs of the cluster and the memory of a
node are related, but not the same. You can attain your needed cluster memory capacity
by having a few large nodes or several smaller nodes. Further, as your needs change, you
can add nodes to or remove nodes from the cluster and thus pay only for what you
need.

The total memory capacity of your cluster is calculated by multiplying the number of
nodes in the cluster by the RAM capacity of each node after deducting system overhead.
The capacity of each node is based on the node type.

```
cluster_capacity = number_of_nodes * (node_capacity - system_overhead)
```

The number of nodes in the cluster is a key factor in the availability of your cluster
running Memcached. The failure of a single node can have an impact on the availability
of your application and the load on your backend database. In such a case, ElastiCache
provisions a replacement for a failed node and it gets repopulated. To reduce this
availability impact, spread your memory and compute capacity over more nodes with
smaller capacity, rather than using fewer high-capacity nodes.

In a scenario where you want to have 35 GB of cache memory, you can set up any of the
following configurations:

- 11 `cache.t2.medium` nodes with 3.22 GB of memory and 2 threads
  each = 35.42 GB and 22 threads.
- 6 `cache.m4.large` nodes with 6.42 GB of memory and 2 threads each
  = 38.52 GB and 12 threads.
- 3 `cache.r4.large` nodes with 12.3 GB of memory and 2 threads each
  = 36.90 GB and 6 threads.
- 3 `cache.m4.xlarge` nodes with 14.28 GB of memory and 4 threads
  each = 42.84 GB and 12 threads.

| Comparing node options                                   | Node type | Memory (in GiB) | Cores   | Hourly cost \* | Nodes needed | Total memory (in GiB) | Total cores | Monthly cost † |
| -------------------------------------------------------- | --------- | --------------- | ------- | -------------- | ------------ | --------------------- | ----------- | -------------- |
| cache.t2.medium                                          | 3.22      | 2               | $ 0.068 | 11             | 35.42        | 22                    | $ 538.56    |
| cache.m4.large                                           | 6.42      | 2               | $ 0.156 | 6              | 38.52        | 12                    | $ 673.92    |
| cache.m4.xlarge                                          | 14.28     | 4               | $ 0.311 | 3              | 42.84        | 12                    | $ 671.76    |
| cache.m5.xlarge                                          | 12.93     | 4               | $ 0.311 | 3              | 38.81        | 12                    | $ 671.76    |
| cache.m6g.large                                          | 6.85      | 2               | $ 0.147 | 6              | 41.1         | 12                    | $ 635       |
| cache.r4.large                                           | 12.3      | 2               | $ 0.228 | 3              | 36.9         | 6                     | $ 492.48    |
| cache.r5.large                                           | 13.07     | 2               | $ 0.216 | 3              | 39.22        | 6                     | $ 466.56    |
| cache.r6g.large                                          | 13.07     | 2               | $ 0.205 | 3              | 42.12        | 6                     | $ 442       |
| \<br>• Hourly cost per node as of October 8,<br>2020.    |
| † Monthly cost at 100% usage for 30 days (720<br>hours). |

These options each provide similar memory capacity but different computational
capacity and cost. To compare the costs of your specific options, see [Amazon ElastiCache Pricing](https://aws.amazon.com/elasticache/pricing/ "https://aws.amazon.com/elasticache/pricing/").

For clusters running Memcached, some of the available memory on each node is used for
connection overhead. For more information, see [Memcached connection
overhead](ParameterGroups.md#ParameterGroups.Memcached.Overhead "ParameterGroups.md#ParameterGroups.Memcached.Overhead")

Using multiple nodes requires spreading the keys across them. Each node has its own
endpoint. For easy endpoint management, you can use the ElastiCache the Auto Discovery
feature, which enables client programs to automatically identify all of the nodes in a
cluster. For more information, see [Automatically identify nodes in your cluster (Memcached)](AutoDiscovery.md "AutoDiscovery.md").

In some cases, you might be unsure how much capacity you need. If so, for testing we
recommend starting with one `cache.m5.large` node. Then monitor the memory
usage, CPU utilization, and cache hit rate with the ElastiCache metrics that are published to
Amazon CloudWatch. For more information on CloudWatch metrics for ElastiCache, see [Monitoring use with CloudWatch Metrics](CacheMetrics.md "CacheMetrics.md"). For production and larger
workloads, the R5 nodes provide the best performance and RAM cost value.

If your cluster doesn't have the hit rate that you want, you can easily add more
nodes to increase the total available memory in your cluster.

If your cluster is bound by CPU but has sufficient hit rate, set up a new cluster with
a node type that provides more compute power.
