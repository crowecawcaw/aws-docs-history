# AOSPERF01-BP03 Check the number of shards per GiB of heap

memory

Prevent inefficient resource utilization by keeping each data node's
heap under a shard load of 25.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Each data node's
heap memory should support no more than 25 shards, thereby
optimizing resource utilization and enhancing query performance.

**Benefits of establishing this best
practice:**

- Improved query performance
- Reduce risks of running out of memory while executing the
  queries

## Implementation guidance

Amazon OpenSearch Service allocates approximately half of each
data node's physical memory, up to 32 GB, for the Java Virtual
Machine (JVM) and OpenSearch. In a system with 16 GB of memory,
this amounts to roughly 8 GB reserved for the JVM.

Additionally, the total number of shards a node can handle is
directly related to its JVM heap memory size. To maintain an
optimal balance, strive for a shard-to-JVM-heap-memory ratio of
approximately 25:1. For example, with 16 GB of memory (and thus 8
GB allocated to the JVM), you should aim for no more than 200
shards per node (25 x 8 = 200).

For further guidance on optimal shard sizing, see [AOSPERF04-BP01](aosperf04-bp01.md "aosperf04-bp01.md")
and [AOSPERF04-BP02](aosperf04-bp02.md "aosperf04-bp02.md").

## Resources

- [Sharding
  strategy](../../../opensearch-service/latest/developerguide/bp.md#bp-sharding-strategy "../../../opensearch-service/latest/developerguide/bp.md#bp-sharding-strategy")
- [Choosing
  the number of shards](../../../opensearch-service/latest/developerguide/bp-sharding.md "../../../opensearch-service/latest/developerguide/bp-sharding.md")
- [Sizing
  OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md")
