# AOSPERF01-BP02 Check shard-to-CPU ratio

Shards are allocated a minimum of 1.5 vCPUs per shard, supporting
efficient processing and scalability.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** The Shard-to-CPU
ratio is maintained at a minimum level of 1.5 vCPUs per shard. This
may vary depending on the use case. Search use cases might require a
higher ratio, while log analytics use cases may work with a smaller
ratio.

**Benefits of establishing this best
practice:**

- A minimum shard-to-CPU ratio of 1.5 helps support each shard
  with sufficient processing power, reducing the risk of
  bottlenecks and promoting performance during indexing or search
  operations.
- By provisioning at least 1.5 vCPUs per shard, you can scale your
  cluster more efficiently, either by scaling up (increasing
  instance size) or out (adding more data nodes), to meet changing
  workload demands without sacrificing performance.

## Implementation guidance

During indexing or search operations, each shard should use at
least one vCPU to process requests. To guarantee sufficient
processing capacity, maintain a minimum shard-to-CPU ratio of
1:1.5. This means that if you have 10 shards in your cluster, for
example, you should provision at least 15 vCPUs (10 x 1.5 = 15).
You can scale up or out to meet the needs of your cluster based on
the total number of shards their density in your data nodes.

In addition to the recommended shard-to-CPU ratio, for more detail, see [AOSPERF01-BP01](aosperf01-bp01.md "aosperf01-bp01.md"). This helps to align
shard sizes with your workload requirements.

## Resources

- [Sharding
  strategy](../../../opensearch-service/latest/developerguide/bp.md#bp-sharding-strategy "../../../opensearch-service/latest/developerguide/bp.md#bp-sharding-strategy")
