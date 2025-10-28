# Calculating storage requirements

Most OpenSearch workloads fall into one of two broad categories:

- **Long-lived index**: You write code that
  processes data into one or more OpenSearch indexes and then updates those
  indexes periodically as the source data changes. Some common examples are
  website, document, and ecommerce search.
- **Rolling indexes**: Data continuously flows
  into a set of temporary indexes, with an indexing period and retention
  window (such as a set of daily indexes that is retained for two weeks). Some
  common examples are log analytics, time-series processing, and clickstream
  analytics.
  For long-lived index workloads, you can examine the source data on disk and easily
  determine how much storage space it consumes. If the data comes from multiple
  sources, just add those sources together.

For rolling indexes, you can multiply the amount of data generated during a
representative time period by the retention period. For example, if you generate 200
MiB of log data per hour, that's 4.7 GiB per day, which is 66 GiB of data at any
given time if you have a two-week retention period.

The size of your source data, however, is just one aspect of your storage
requirements. You also have to consider the following:

- **Number of replicas**: Each replica is a
  full copy of the primary shard, the store size of the index shows the size
  taken by the primary and replica shard. By default, each OpenSearch index has
  one replica. We recommend at least one to prevent data loss. Replicas also
  improve search performance, so you might want more if you have a read-heavy
  workload. Use `PUT /my-index/_settings` to update the
  `number_of_replicas` setting for your index.
- **OpenSearch indexing overhead**: The on-disk
  size of an index varies. The total size of the source data plus the index is
  often 110% of the source, with the index up to 10% of the source data. After
  you index your data, you can use the `_cat/indices?v` API and
  `pri.store.size` value to calculate the exact overhead.
  `_cat/allocation?v` also provides a useful summary.
- **Operating system reserved space**: By
  default, Linux reserves 5% of the file system for the `root` user
  for critical processes, system recovery, and to safeguard against disk
  fragmentation problems.
- **OpenSearch Service overhead**: OpenSearch Service reserves 20% of the
  storage space of each instance (up to 20 GiB) for segment merges, logs, and
  other internal operations.

Because of this 20 GiB maximum, the total amount of reserved space can
vary dramatically depending on the number of instances in your domain. For
example, a domain might have three `m6g.xlarge.search` instances,
each with 500 GiB of storage space, for a total of 1.46 TiB. In this case,
the total reserved space is only 60 GiB. Another domain might have 10
`m3.medium.search` instances, each with 100 GiB of storage
space, for a total of 0.98 TiB. Here, the total reserved space is 200 GiB,
even though the first domain is 50% larger.

In the following formula, we apply a "worst-case" estimate for overhead.
This estimate includes additional free space to help minimize the impact of
node failures and Availability Zone outages.
In summary, if you have 66 GiB of data at any given time and want one replica,
your _minimum_ storage requirement is closer to 66 \* 2 \* 1.1 / 0.95 / 0.8 = 191 GiB. You can generalize this calculation as
follows:

**Source data \* (1 + number of replicas) \* (1 + indexing
overhead) / (1 - Linux reserved space) / (1 - OpenSearch Service overhead) = minimum storage
requirement**

Or you can use this simplified version:

**Source data \* (1 + number of replicas) \* 1.45 = minimum
storage requirement**

Insufficient storage space is one of the most common causes of cluster
instability. So you should cross-check the numbers when you [choose instance types, instance counts, and storage
volumes](bp-instances.md "bp-instances.md").

Other storage considerations exist:

- If your minimum storage requirement exceeds 1 PB, see [Petabyte scale in Amazon OpenSearch Service](petabyte-scale.md "petabyte-scale.md").
- If you have rolling indexes and want to use a hot-warm architecture, see
  [UltraWarm storage for Amazon OpenSearch Service](ultrawarm.md "ultrawarm.md").
