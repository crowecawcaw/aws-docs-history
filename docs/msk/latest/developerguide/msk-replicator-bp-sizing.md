

# Sizing and partitions
<a name="msk-replicator-bp-sizing"></a>

The number of partitions on your source and target MSK clusters directly impacts replication performance. Having too few or too many partitions can impact performance.

The following table shows the recommended minimum number of partitions for getting the throughput you want with MSK Replicator.


**Throughput and recommended minimum number of partitions**  

| Throughput (MB/s) | Minimum number of partitions required | 
| --- | --- | 
| 50 | 167 | 
| 100 | 334 | 
| 250 | 833 | 
| 500 | 1666 | 
| 1000 | 3333 | 

Verify that you have enough read and write capacity in your source and target MSK clusters to support the replication traffic. MSK Replicator acts as a consumer for your source cluster (egress) and as a producer for your target cluster (ingress). Therefore, you should provision cluster capacity to support the replication traffic in addition to other traffic on your clusters.

We recommend that you provision identical capacity for your source and target clusters, and account for the replication throughput when calculating how much capacity you need.