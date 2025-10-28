# Performance and Scaling in Amazon Neptune

Neptune DB clusters and instances scale at three different levels:

- [Storage Scaling](#manage-console-performance-scaling-storage "#manage-console-performance-scaling-storage")
- [Instance Scaling;](#manage-console-performance-scaling-instances "#manage-console-performance-scaling-instances")
- [Read Scaling](#manage-console-performance-scaling-reads "#manage-console-performance-scaling-reads")

## Storage Scaling in Neptune

Neptune storage automatically scales with the data in your cluster volume. As your data
grows, your cluster volume storage grows, up to 128 TiB in all supported regions except China
and GovCloud, where it is limited to 64 TiB.

The size of your cluster volume is checked on an hourly basis to determine your storage
costs.

Storage consumed by your Neptune database is billed in per GB-month increments and I/Os
consumed are billed in per million request increments. You pay only for the storage and I/Os
that your Neptune database consumes, and you don't need to provision in advance.

For pricing information, see the [Neptune
product page](https://aws.amazon.com/neptune/pricing "https://aws.amazon.com/neptune/pricing").

## Instance Scaling in Neptune

You can scale your Neptune DB cluster as needed by modifying the DB instance class for
each DB instance in the DB cluster. Neptune supports several optimized DB instance classes.

## Read Scaling in Neptune

You can achieve read scaling for your Neptune DB cluster by creating up to
15 Neptune replicas in the DB cluster. Each Neptune replica returns the
same data from the cluster volume with minimal replica lag (often considerably less than 100
milliseconds after the primary instance has written an update). As your read traffic
increases, you can create additional Neptune replicas and connect to them directly to
distribute the read load for your DB cluster. Neptune replicas don't have to be of the same
DB instance class as the primary instance.

For information about adding Neptune replicas to a DB cluster, see [Adding reader instances](manage-console-create-replica.md "manage-console-create-replica.md").
