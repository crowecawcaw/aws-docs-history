# Choosing the number of shards

After you understand your storage requirements, you can investigate your indexing
strategy. By default in OpenSearch Service, each index is divided into five primary shards and one
replica (total of 10 shards). This behavior differs from open source OpenSearch,
which defaults to one primary and one replica shard. Because you can't easily change
the number of primary shards for an existing index, you should decide about shard
count _before_ indexing your first document.

The overall goal of choosing a number of shards is to distribute an index evenly
across all data nodes in the cluster. However, these shards shouldn't be too large
or too numerous. A general guideline is to try to keep shard size between
10–30 GiB for workloads where search latency is a key performance objective,
and 30–50 GiB for write-heavy workloads such as log analytics.

Large shards can make it difficult for OpenSearch to recover from failure, but
because each shard uses some amount of CPU and memory, having too many small shards
can cause performance issues and out of memory errors. In other words, shards should
be small enough that the underlying OpenSearch Service instance can handle them, but not so small
that they place needless strain on the hardware.

For example, suppose you have 66 GiB of data. You don't expect that number to
increase over time, and you want to keep your shards around 30 GiB each. Your number
of shards therefore should be approximately 66 \* 1.1 / 30 = 3. You can generalize
this calculation as follows:

**(Source data + room to grow) \* (1 + indexing overhead) /
desired shard size = approximate number of primary shards**

This equation helps compensate for data growth over time. If you expect those same
66 GiB of data to quadruple over the next year, the approximate number of shards is
(66 + 198) \* 1.1 / 30 = 10. Remember, though, you don't have those extra 198 GiB of
data _yet_. Check to make sure that this
preparation for the future doesn't create unnecessarily tiny shards that consume
huge amounts of CPU and memory in the present. In this case, 66 \* 1.1 / 10 shards =
7.26 GiB per shard, which will consume extra resources and is below the recommended
size range. You might consider the more middle-of-the-road approach of six shards,
which leaves you with 12-GiB shards today and 48-GiB shards in the future. Then
again, you might prefer to start with three shards and reindex your data when the
shards exceed 50 GiB.

A far less common issue involves limiting the number of shards per node. If you
size your shards appropriately, you typically run out of disk space long before
encountering this limit. For example, an `m6g.large.search` instance has
a maximum disk size of 512 GiB. If you stay below 80% disk usage and size your
shards at 20 GiB, it can accommodate approximately 20 shards. Elasticsearch 7._x_ and later, and all versions of OpenSearch
up to 2.15, have a limit of _1,000_ shards per
node. To adjust the maximum shards per node, configure the
`cluster.max_shards_per_node` setting. For OpenSearch 2.17 and later, OpenSearch Service supports 1000 shards for every 16GB of JVM heap memory up to a maximum of 4000 shards per node. For an example, see [Cluster settings](https://opensearch.org/docs/latest/opensearch/rest-api/cluster-settings/#request-body "https://opensearch.org/docs/latest/opensearch/rest-api/cluster-settings/#request-body"). For more information about shard count, see [Shard count quotas](limits.md#shard-count "limits.md#shard-count").

Sizing shards appropriately almost always keeps you below this limit, but you can
also consider the number of shards for each GiB of Java heap. On a given node, have
no more than 25 shards per GiB of Java heap. For example, an
`m5.large.search` instance has a 4-GiB heap, so each node should have
no more than 100 shards. At that shard count, each shard is roughly 5 GiB in size,
which is well below our recommendation.
