# Best practices

Follow these best practices to optimize performance and cost when running domains with the
Optimized engine.

## Keep shards per node under 500

Avoid exceeding 500 shards per data node. A high shard count increases cluster
coordination overhead and can degrade query performance and cluster stability. Monitor
shard counts as you scale your ingestion volume. Use Index State
Management (ISM) policies to manage index lifecycle.

## Minimize keyword sub-fields

On the Optimized engine, Parquet columnar storage handles sorting and aggregations
natively without requiring `.keyword` sub-fields. When you define your
index mappings, consider omitting keyword sub-fields for text fields that you do not
need exact-match filtering on. Removing unnecessary keyword sub-fields from your
mappings reduces storage consumption and ingestion overhead.

## Prefer match queries over wildcard queries

Use `match` or `match_phrase` for text search instead of
`like` (wildcard) patterns. Match queries leverage the Lucene inverted
index efficiently, although wildcard queries are more resource-intensive and might result in
slower response times.

## Size coordinator nodes appropriately

If you enable dedicated coordinator nodes, use a ratio of 1 coordinator node for
every 5 data nodes. Choose a coordinator node instance type with the same memory
configuration as your data nodes to ensure that query planning and result merging
have sufficient resources.

## Optimize indexing and storage

Log data has predictable patterns. Timestamps increase monotonically, status
codes repeat frequently, and messages are variable-length strings. Match your encoding,
compression, bloom filter, and index sort settings to these patterns for optimal storage
efficiency and query performance.

### Parquet encoding

Choose encodings that match the data characteristics of each field type.

| Field type                                                                            | Recommended encoding  | Reason                                                                                                                                                                    |
| ------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@timestamp`                                                                          | DELTA\_BINARY\_PACKED | Timestamps increase monotonically. Deltas are small and<br>compress well.                                                                                                 |
| Low-cardinality keywords (`log.level`,<br>`status_code`, `region`,<br>`service.name`) | RLE\_DICTIONARY       | Few distinct values. Dictionary plus run-length encoding<br>yields near-zero per-row overhead.                                                                            |
| High-cardinality IDs (`trace_id`,<br>`span_id`, `request_id`)                         | DELTA\_BYTE\_ARRAY    | Stores variable-length byte arrays incrementally. More compact<br>than PLAIN for fixed-format strings such as UUIDs or hex-encoded<br>IDs that share structural patterns. |
| Floating-point metrics (`response_time`,<br>`cpu_usage`)                              | BYTE\_STREAM\_SPLIT   | Separates mantissa and exponent bytes for better compression<br>of numeric series.                                                                                        |
| `message` (long text)                                                                 | PLAIN (default)       | Variable-length unstructured text does not benefit from<br>specialized encoding.                                                                                          |

### Per-field compression

By default, text and keyword fields use ZSTD compression, and other fields use
LZ4\_RAW. With per-field compression, you can balance storage efficiency against query
latency.

ZSTD

Best for large text fields and high-cardinality strings where
compression ratio matters more than decode speed.

LZ4\_RAW (default for numeric)

Best for numeric, timestamp, and low-cardinality fields scanned
frequently by aggregations and range queries.

SNAPPY

Best for CPU-constrained nodes with high ingestion rates.

For low-cardinality keyword fields that you primarily use in aggregations and range queries, consider overriding the default ZSTD with LZ4\_RAW for faster decode speed.

### Bloom filters

Enable bloom filters on fields that you frequently filter with equality
predicates. When a field is used only for equality filtering (not range queries
or full-text search), you can also disable the Lucene keyword index on that
field to avoid maintaining additional structures.

**Low-cardinality fields**
(`log.level`, `status_code`, `service.name`,
`region`) — Bloom filters are small and lookups are fast. Query
performance remains consistent while you save storage by disabling the Lucene
keyword index on these fields.

**High-cardinality fields**
(`trace_id`, `request_id`, `user_id`) —
Bloom filters can still eliminate row groups and reduce storage compared to a
full inverted index, but the filter itself becomes larger and each probe does
more work. Use bloom filters on high-cardinality fields when storage savings
are the priority and you can tolerate slightly higher per-query overhead.

### Index sort

Index sort controls the physical order of documents within each segment. When
documents are sorted, adjacent rows in the same Parquet column tend to share values,
which improves compression. This is especially effective with RLE and dictionary encoding.

For log analytics, sort by a low-cardinality field first (to create long value
runs), then by timestamp (to keep events within each group in order):

- Sorting by `service.name` groups all logs from the same service
  together. RLE\_DICTIONARY compresses these runs to near-zero overhead.
- Within each service group, `@timestamp` descending ensures tight
  delta values between adjacent rows. DELTA\_BINARY\_PACKED encodes these
  efficiently.
- Other correlated fields (`host.name`, `log.level`,
  `region`) also benefit because they cluster naturally when the
  primary sort groups by service.

| Sort position  | Recommended field                                                                             | Reason                                                                           |
| -------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| 1st (primary)  | Lowest-cardinality field you commonly filter on<br>(`service.name`, `host.name`,<br>`region`) | Creates the longest value runs and enables row group pruning<br>on filters.      |
| 2nd            | `@timestamp`                                                                                  | Maintains temporal ordering within each group and enables<br>time-range pruning. |
| 3rd (optional) | Secondary categorical field (`log.level`)                                                     | Further improves run lengths, with diminishing<br>returns.                       |

Consider the following trade-offs when enabling index sort:

- Sort adds CPU cost during segment merges. For high ingestion rates, limit
  to one or two sort fields.
- Choose sort fields that align with your most frequent query filters. A
  sorted field enables row group min/max pruning in addition to compression
  benefits.

### Combined example

The following index configuration applies encoding, compression, bloom filter, and
index sort recommendations together:

```
PUT my-logs
{
  "settings": {
    "index.sort.field": ["service.name", "@timestamp"],
    "index.sort.order": ["asc", "desc"],
    "index.parquet.encoding.field": [
      "@timestamp",
      "log.level",
      "status_code",
      "service.name",
      "region",
      "response_time",
      "trace_id"
    ],
    "index.parquet.encoding.value": [
      "DELTA_BINARY_PACKED",
      "RLE_DICTIONARY",
      "RLE_DICTIONARY",
      "RLE_DICTIONARY",
      "RLE_DICTIONARY",
      "BYTE_STREAM_SPLIT",
      "DELTA_BYTE_ARRAY"
    ],
    "index.parquet.compression.field": ["message", "trace_id", "@timestamp", "response_time"],
    "index.parquet.compression.value": ["ZSTD", "ZSTD", "LZ4_RAW", "LZ4_RAW"],
    "index.parquet.bloom_filter_enabled.field": [
      "log.level", "status_code", "service.name", "region"
    ],
    "index.parquet.bloom_filter_enabled.value": [true, true, true, true]
  },
  "mappings": {
    "properties": {
      "@timestamp": { "type": "date" },
      "message": { "type": "text" },
      "host.name": { "type": "keyword" },
      "trace_id": { "type": "keyword" },
      "span_id": { "type": "keyword" },
      "service.name": {
        "type": "keyword",
        "index": false
      },
      "log.level": {
        "type": "keyword",
        "index": false
      },
      "status_code": {
        "type": "keyword",
        "index": false
      },
      "region": {
        "type": "keyword",
        "index": false
      },
      "response_time": { "type": "float" }
    }
  }
}
```

###### Index settings apply at creation time only

You set Parquet encoding, compression, bloom filter, and index sort settings at
index creation time. You cannot change them on existing indices. To apply these
recommendations, update your index template so that newly created indices use the
optimized settings.

## Tune accuracy for distributed top-N queries

Distributed grouped top-N queries (those that group by a key, sort by an aggregate,
and limit the output) use oversampling to balance accuracy and performance. Each shard
returns only its local top slice to the coordinator rather than shuffling every
group.

You can control this trade-off with the
`analytics.shard_bucket_oversampling_factor` cluster setting:

| Property | Value                 |
| -------- | --------------------- |
| Type     | Float                 |
| Default  | `1.5`                 |
| Dynamic  | Yes (cluster setting) |

Each shard returns `ceil(N × factor) + N` groups, where N is the
`head` limit. The approximation can only undercount a group, never
overcount it. A group is dropped from a shard when its rows fall below that shard's
local cutoff.

| Value                     | Accuracy    | Cost                                                                                                |
| ------------------------- | ----------- | --------------------------------------------------------------------------------------------------- |
| `0.0`                     | Exact       | Highest. Every group is shuffled. Very high-cardinality group-bys<br>might hit the circuit breaker. |
| Low (for example, `5`)    | Approximate | Lowest latency and memory.                                                                          |
| High (for example, `100`) | Near-exact  | More data shuffled. Converges to exact as the factor grows.                                         |

Raise the factor when grouped top-N results undercount. The value needed scales
with how skewed the key's distribution is and how deep the `head` limit
goes. Set to `0` to disable oversampling and return exact results.

Example:

```
PUT _cluster/settings
{
  "transient": { "analytics.shard_bucket_oversampling_factor": 5.0 }
}
```
