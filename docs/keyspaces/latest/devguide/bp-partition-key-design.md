# How to use partition keys effectively in Amazon Keyspaces

The primary key that uniquely identifies each row in an Amazon Keyspaces table can consist of one or
multiple partition key columns, which determine which partitions the data is stored in,
and one or more optional clustering column, which define how data is clustered and
sorted within a partition.

Because the partition key establishes the number of partitions your data is stored in and
how the data is distributed across these partitions, how you chose your partition key
can have a significant impact upon the performance of your queries. In general, you
should design your application for uniform activity across all partitions on disk.

Distributing read and write activity of your application evenly across all partitions
helps to minimize throughput costs and this applies to on-demand as well as provisioned
read/write capacity modes. For example, if you are using provisioned capacity mode, you
can determine the access patterns that your application needs, and estimate the total
read capacity units (RCU) and write capacity units (WCU) that each table requires. Amazon Keyspaces
supports your access patterns using the throughput that you provisioned as long as the
traffic against a given partition does not exceed 3,000 RCUs and 1,000 WCUs.

When a partition experiences sustained high read or write throughput, depending on traffic patterns Amazon Keyspaces
may automatically split the partition into two new partitions. Each new partition contains a subset of the
original partition's rows, distributing the throughput evenly across both partitions.

Amazon Keyspaces offers additional flexibility in your per-partition throughput provisioning by providing
burst capacity, for more information see [Use burst
capacity effectively in Amazon Keyspaces](throughput-bursting.md "throughput-bursting.md").

###### Topics

- [Use write sharding to evenly distribute workloads across partitions](bp-partition-key-sharding.md "bp-partition-key-sharding.md")
