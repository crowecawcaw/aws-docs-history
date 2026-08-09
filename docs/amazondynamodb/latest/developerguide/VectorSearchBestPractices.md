# Best practices for vector indexes

The following recommendations help you design vector indexes that are accurate,
performant, and cost-effective.

## Choose your embedding model and dimensions first

The embedding model you use determines the number of dimensions your vectors have,
and you set `Dimensions` when you create the index. You cannot change the
number of dimensions after creation. Decide on an embedding model before you create
the index, and use the same model to generate both stored vectors and query vectors.
Fewer dimensions reduce search, write, and storage cost, but higher-dimensional models can
capture more semantic detail. Choose the smallest number of dimensions that meets your
relevance requirements. See [Generating vector embeddings](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Embeddings "VectorSearchWorkingWith.md#VectorSearchWorkingWith.Embeddings").

## Match the distance function to your embeddings

Choose the distance function that matches how your embedding model represents
similarity. `COSINE` compares direction and ignores magnitude, which suits
most text embedding models. `EUCLIDEAN` measures absolute distance and is
sensitive to magnitude. `DOT_PRODUCT` is also sensitive to magnitude. If you
use it, normalize your embeddings to unit length so that scores reflect direction
rather than vector length. You cannot change the distance function after you create the
index, so validate your choice against a representative dataset first. See
[How distance functions rank results](VectorSearch.md#VectorSearchWorkingWith.Ranking "VectorSearch.md#VectorSearchWorkingWith.Ranking").

## Choose a partition key that matches your query patterns

A partition key restricts each `SearchVectors` call to the portion of
the vector index that belongs to a single partition key value. The call does not
search the entire index. Searching less data lowers cost, can improve latency and recall, and
horizontally scales throughput across partition key values.

You must supply the partition key value in
`SearchConditionExpression` on every search. Each search is scoped to
exactly one partition key value. Choose a partition key that matches the query
patterns your application supports.

For example, if you store location-based data by US state, you have approximately
50 partition key values. Each state holds a meaningful number of vectors for good
recall. The 50 partitions provide up to approximately 50x horizontal throughput
scaling. This works when every search targets a single state.

Avoid extreme cardinality in either direction:

- **Too high** (for example, a unique item
  ID) – Each partition contains a single item with no neighbors to compare,
  which produces poor recall.
- **Too low** (for example, a boolean) –
  Most items land in one partition, which limits throughput scaling and
  reduces the latency and cost benefits.

To filter further within a partition, use inline filter attributes.

**Throughput example.** Consider a 768-dimensional
embedding model (such as Cohere Embed v3) with 1 KB of non-vector item data,
giving a total item size of approximately 4 KB (768 dimensions × 4 bytes + 1 KB).
With this item size, the per-partition-key limits translate to:

- **Search:** 1 GBps ÷ 4 KB ≈ 250,000
  vectors examined per second per partition key value. As the number of
  vectors in a partition grows, each search examines more data and you
  will approach this limit sooner.
- **Write:** 10 MBps ÷ 4 KB ≈ 2,500 vector
  writes per second per partition key value

Spreading your data across more partition key values multiplies these limits.
For example, 50 partition key values provide up to 50× the aggregate search and
write throughput. If your workload exceeds these per-partition-key limits, contact
AWS Support.

## Keep embeddings in sync with source content

DynamoDB does not recompute embeddings for you. Whenever you change the source content
that an embedding represents, regenerate the vector with the same embedding model and
write it back to the item. Otherwise the index continues to return results based on the
stale vector. Consider capturing content changes with DynamoDB Streams and using a
downstream process to regenerate and rewrite affected embeddings.

## Project only the attributes you need

`SearchVectors` cannot return attributes that are not projected into
the vector index. Projecting more attributes increases index storage and
write cost. Project the attributes your application reads directly from search results,
and retrieve the rest with a follow-up `GetItem` or
`BatchGetItem` on the base table when you need them.

## Use multiple indexes to compare embedding models

You can create up to 5 vector indexes on a single table. Use separate indexes to
evaluate different embedding models or model versions side by side. Store each
model's embeddings in a different vector attribute and create a vector index for
each. This lets you compare search quality between models against the same
underlying data without migrating your production index.

For example, when upgrading from one model version to another, create a second
index with the new model's dimensions and distance function. Backfill it with
embeddings from the new model, run test queries against both indexes, and compare
relevance. Once satisfied, migrate your application to the new index and delete the
old one.
