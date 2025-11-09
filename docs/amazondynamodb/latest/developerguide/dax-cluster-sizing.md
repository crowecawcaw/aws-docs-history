# Sizing your DAX cluster

A DAX cluster's total capacity and availability depends on node type and count. More nodes in the cluster increase its read capacity, but not the write capacity. Larger node types (up to r5.8xlarge) can handle more writes, but too few nodes can impact availability when a node failure occurs. For more information about sizing your DAX cluster, see the [DAX cluster sizing guide](DAX.md "DAX.md").

The following sections discuss the different sizing aspects that you should consider to balance node type and count for creating a scalable and cost-efficient cluster.

###### In this section

- [Planning availability](#dax-sizing-availability "#dax-sizing-availability")
- [Planning write throughput](#dax-sizing-write-throughput "#dax-sizing-write-throughput")
- [Planning read throughput](#dax-sizing-read-throughput "#dax-sizing-read-throughput")
- [Planning dataset size](#dax-sizing-dataset-size "#dax-sizing-dataset-size")
- [Calculating approximate cluster capacity requirements](#dax-sizing-cluster-capacity "#dax-sizing-cluster-capacity")
- [Approximating cluster throughput capacity by node type](#dax-sizing-cluster-throughput-capacity "#dax-sizing-cluster-throughput-capacity")
- [Scaling write capacity in DAX clusters](#dax-sizing-scaling-write-capacity "#dax-sizing-scaling-write-capacity")

## Planning availability

When sizing a DAX cluster, you should first focus on its targeted availability. Availability of a clustered service, such as DAX, is a dimension of the total number of nodes in the cluster. Because a single node cluster has no tolerance for failure, its availability is equal to one node. In a 10-node cluster, the loss of a single node has a minimal impact to the cluster's overall capacity. This loss doesn't have a direct impact on availability because the remaining nodes can still fulfill read requests. To resume writes, DAX quickly nominates a new primary node.

DAX is VPC-based. It uses a subnet group to determine which [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") it can run nodes in and which IP addresses to use from the subnets. For production workloads, we highly recommend that you use DAX with at least three nodes in different Availability Zones. This ensures that the cluster has more than one node left to handle requests even if a single node or Availability Zone fails. A cluster can have up to 11 nodes, where one is a primary node and 10 are read replicas.

## Planning write throughput

All DAX clusters have a primary node for write-through requests. The size of the node type for the cluster determines its write capacity. Adding additional read replicas doesn't increase the cluster's write capacity. Therefore, you should consider the write capacity during cluster creation because you can't change the node type later.

If your application needs to write-through DAX to update the item cache, consider increased use of cluster resources to facilitate the write. Writes against DAX consume about 25 times more resources than cache-hit reads. This might require a larger node type than for read-only clusters.

For additional guidance about determining whether write-through or write-around will work best for your application, see [Strategies for writes](DAX.md#DAX.consistency.strategies-for-writes "DAX.md#DAX.consistency.strategies-for-writes").

## Planning read throughput

A DAX cluster's read capacity depends on the cache hit ratio of your workload. Because DAX reads data from DynamoDB when a cache miss occurs, it consumes approximately 10 times more cluster resources than a cache-hit. To increase cache hits, increase the [TTL](dax-config-considerations.md#select-ttl-duration-caches "dax-config-considerations.md#select-ttl-duration-caches") setting of the cache to define the period for which an item is stored in the cache. A higher TTL duration, however, increases the chance of reading older item versions unless updates are written through DAX.

To make sure that the cluster has sufficient read capacity, scale the cluster horizontally as mentioned in [Scaling a cluster horizontally](dax-cluster-operations.md#dax-cluster-horizontal-scaling "dax-cluster-operations.md#dax-cluster-horizontal-scaling"). Adding more nodes adds read replicas to the pool of resources, while removing nodes reduces read capacity. When you select the number of nodes and their sizes for a cluster, consider both the minimum and maximum amount of read capacity needed. If you can't horizontally scale a cluster with smaller node types to meet your read requirements, use a larger node type.

## Planning dataset size

Each available node type has a set memory size for DAX to cache data. If a node type is too small, the working set of data that an application requests won't fit in memory and results in cache misses. Because larger nodes support larger caches, use a node type larger than the estimated data set that you need to cache. A larger cache also improves the cache hit ratio.

You might get diminishing returns for caching items with few repeated reads. Calculate the memory size for frequently accessed items and make sure the cache is large enough to store that data set.

## Calculating approximate cluster capacity requirements

You can estimate your workload's total capacity needs to help you select the appropriate size and quantity of cluster nodes. To do this estimation, calculate the variable _normalized request per second_ (Normalized RPS). This variable represents the total units of work your application requires the DAX cluster to support, including cache hits, cache misses, and writes. To calculate the Normalized RPS, use the following inputs:

- `ReadRPS_CacheHit` – Specifies the number of reads per second that result in a cache hit.
- `ReadRPS_CacheMiss` – Specifies the number of reads per second that result in a cache miss.
- `WriteRPS` – Specifies the number of writes per second that will go through DAX.
- `DaxNodeCount` – Specifies the number of nodes in the DAX cluster.
- `Size` – Specifies the size of the item being written or read in KB rounded up to the nearest KB.
- `10x_ReadMissFactor` – Represents a value of 10. When a cache miss occurs, DAX uses approximately 10 times more resources than cache hits.
- `25x_WriteFactor` – Represents a value of 25 because a DAX write-through uses approximately 25 times more resources than cache hits.

Using the following formula, you can calculate the Normalized RPS.

```
Normalized RPS = (ReadRPS_CacheHit * Size) + (ReadRPS_CacheMiss * Size * 10x_ReadMissFactor) + (WriteRequestRate * 25x_WriteFactor * Size * DaxNodeCount)
```

For example, consider the following input values:

- `ReadRPS_CacheHit` = 50,000
- `ReadRPS_CacheMiss` = 1,000
- `ReadMissFactor` = 1
- `Size` = 2 KB
- `WriteRPS` = 100
- `WriteFactor` = 1
- `DaxNodeCount` = 3

By substituting these values in the formula, you can calculate the Normalized RPS as follows.

```
Normalized RPS = (50,000 Cache Hits/Sec * 2KB) + (1,000 Cache Misses/Sec * 2KB * 10) + (100 Writes/Sec * 25 * 2KB * 3)
```

In this example, the calculated value of Normalized RPS is 135,000. However, this Normalized RPS value doesn't account for keeping cluster utilization below 100% or node loss. We recommend that you factor in additional capacity. To do this, determine the greater of two multiplying factors: target utilization or node loss tolerance. Then, multiply the Normalized RPS by the greater factor to obtain a _target request per second_ (Target RPS).

- **Target utilization**

Because performance impacts increase cache misses, we don't recommend running the DAX cluster at 100% utilization. Ideally, you should keep cluster utilization at or below 70%. To achieve this, multiply the Normalized RPS by 1.43.

- **Node loss tolerance**

If a node fails, your application must be able to distribute its requests among the remaining nodes. To make sure nodes stay below 100% utilization, choose a node type large enough to absorb extra traffic until the failed node comes back online. For a cluster with fewer nodes, each node must tolerate larger traffic increases when one node fails.

If a primary node fails, DAX automatically fails over to a read replica and designates it as the new primary. If a replica node fails, other nodes in the DAX cluster can still serve requests until the failed node is recovered.

For example, a 3-node DAX cluster with a node failure requires an additional 50% capacity on the remaining two nodes. This requires a multiplying factor of 1.5. Conversely, an 11-node cluster with a failed node requires an additional 10% capacity on the remaining nodes or a multiplying factor of 1.1.

Using the following formula, you can calculate the Target RPS.

```
Target RPS = Normalized RPS * CEILING(TargetUtilization, NodeLossTolerance)
```

For example, to calculate Target RPS, consider the following values:

- `Normalized RPS` = 135,000
- `TargetUtilization` = 1.43

Because we're aiming for a maximum cluster utilization of 70%, we're setting `TargetUtilization` to 1.43.

- `NodeLossTolerance` = 1.5

Say that we're using a 3-node cluster, therefore, we're setting `NodeLossTolerance` to 50% capacity.

By substituting these values in the formula, you can calculate the Target RPS as follows.

```
Target RPS = 135,000 * CEILING(1.43, 1.5)
```

In this example, because the value of `NodeLossTolerance` is greater than `TargetUtilization`, we calculate the value of Target RPS with `NodeLossTolerance`. This gives us a Target RPS of 202,500, which is the total amount of capacity the DAX cluster must support. To determine the number of nodes you'll need in a cluster, map the Target RPS to an appropriate column in the [following table](#dax-sizing-cluster-throughput-capacity "#dax-sizing-cluster-throughput-capacity"). For this example of a Target RPS of 202,500, you need the dax.r5.large node type with three nodes.

## Approximating cluster throughput capacity by node type

Using the [Target RPS formula](#Target-RPS-formula "#Target-RPS-formula"), you can estimate cluster capacity for different node types. The following table shows approximate capacities for clusters with 1, 3, 5, and 11 node types. These capacities don't replace the need to perform load testing of DAX with your own data and request patterns. Additionally, these capacities don't include [t-type](DAX.md "DAX.md") instances because of their lack of fixed CPU capacity. The unit for all values in the following table is Normalized RPS.

| Node type (memory)      | 1 node | 3 nodes | 5 nodes | 11 nodes |
| ----------------------- | ------ | ------- | ------- | -------- |
| dax.r5.24xlarge (768GB) | 1M     | 3M      | 5M      | 11M      |
| dax.r5.16xlarge (512GB) | 1M     | 3M      | 5M      | 11M      |
| dax.r5.12xlarge (384GB) | 1M     | 3M      | 5M      | 11M      |
| dax.r5.8xlarge (256GB)  | 1M     | 3M      | 5M      | 11M      |
| dax.r5.4xlarge (128GB)  | 600k   | 1.8M    | 3M      | 6.6M     |
| dax.r5.2xlarge (64GB)   | 300k   | 900k    | 1.5M    | 3.3M     |
| dax.r5.xlarge (32GB)    | 150k   | 450k    | 750k    | 1.65M    |
| dax.r5.large (16GB)     | 75k    | 225k    | 375k    | 825k     |

Because of the maximum limit of 1 million NPS (network operations per second) for each node, nodes of types dax.r5.8xlarge or larger don't contribute additional cluster capacity. Node types larger than 8xlarge might not contribute to total throughput capacity of the cluster. However, such node types can be helpful for storing a larger working data set in memory.

## Scaling write capacity in DAX clusters

Each write to DAX consumes 25 normalized requests on every node. Because there's a 1 million RPS limit for each node, a DAX cluster is limited to 40,000 writes per second, not accounting for read usage.

If your use case requires more than 40,000 writes per second in the cache, you must use separate DAX clusters and shard the writes among them. Similar to DynamoDB, you can hash the partition key for the data you're writing to the cache. Then, use modulus to determine which shard to write the data to.

The following example calculates the hash of an input string. It then calculates the modulus of the hash value with 10.

```
def hash_modulo(input_string):
    # Compute the hash of the input string
    hash_value = hash(input_string)

    # Compute the modulus of the hash value with 10
    bucket_number = hash_value % 10

    return bucket_number

#Example usage
if _name_ == "_main_":
    input_string = input("Enter a string: ")
    result = hash_modulo(input_string)
    print(f"The hash modulo 10 of '{input_string}' is: {result}.")
```
