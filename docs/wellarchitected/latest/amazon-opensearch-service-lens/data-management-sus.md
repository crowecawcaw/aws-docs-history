# Data management

| AOSSUS03: How do you align data management practices with environmental sustainability objectives? |
| -------------------------------------------------------------------------------------------------- |
|                                                                                                    |

Implementing data management practices in OpenSearch Service is vital for achieving sustainability objectives, improving the efficiency of resource utilization, and achieving environmentally-responsible operations. The significance of incorporating these practices is underscored by several key factors.

Efficient data lifecycle management, involving well-defined policies
for data retention and removal, prevents unnecessary storage costs
and mitigates the environmental impact associated with data storage.
Similarly, the application of policies addressing data redundancy,
compression, and deduplication results in a reduced storage
footprint, optimizing costs and minimizing the need for additional
hardware resources.

Adopting ISM policies automates the lifecycle management of indices
and enables transitions based on criteria such as age or size. This
approach facilitates the movement of infrequently accessed data to
lower-cost storage solutions, which reduces the environmental impact
associated with maintaining high-performance storage for rarely
accessed data.

Efficient data management patterns contribute to the optimization of
computing resources through proper indexing strategies, shard
management, and resource allocation. This optimization minimizes
energy consumption and overall resource usage within the OpenSearch
cluster, which helps your organization align with sustainability
objectives.

Finally, effective data management policies play a crucial role in
optimizing indexing and query patterns. This involves selecting
appropriate data types, using efficient queries, and designing
indices that align with the nature of the data. The outcome is
enhanced performance, faster response times, reduced resource usage,
and a reinforced commitment to sustainability goals in the context
of Amazon OpenSearch Service.

###### Best practices

- [AOSSUS03-BP01 Use Index State Management to manage the
  lifecycle of your dataset](aossus03-bp01.md "aossus03-bp01.md")
- [AOSSUS03-BP02 Reduce unnecessary or redundant data from your
  domain](aossus03-bp02.md "aossus03-bp02.md")
- [AOSSUS03-BP03 Take manual snapshots of your indices only when
  it is difficult to recreate the dataset](aossus03-bp03.md "aossus03-bp03.md")
