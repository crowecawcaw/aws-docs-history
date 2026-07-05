# Storage behavior

The Optimized engine stores data in two structures, each optimized for its
purpose.

| Structure         | Format                                         | Purpose                                              |
| ----------------- | ---------------------------------------------- | ---------------------------------------------------- |
| Analytics storage | Apache Parquet (columnar, natively compressed) | Aggregations, joins, range scans, and trend analysis |
| Search index      | Lucene inverted index                          | Phrase, fuzzy, and wildcard matching                 |

Parquet replaces three of Lucene's on-disk structures (doc values, BKD trees, and
stored fields) with a single compressed columnar format. The inverted index is
retained for full-text search. This architecture significantly reduces storage
requirements for typical observability workloads with search enabled.

## Storage tiers

The Optimized engine uses the [Multi-tier storage for Amazon OpenSearch Service](multi-tier-storage.md "multi-tier-storage.md") architecture,
which combines Amazon S3 with local instance storage and is powered by OpenSearch
Optimized Instances.

| Tier | Purpose                                               | Instances                                         |
| ---- | ----------------------------------------------------- | ------------------------------------------------- |
| Hot  | Active ingestion and frequent queries                 | OpenSearch Optimized Instances (OR1, OR2, or OM2) |
| Warm | Infrequent queries and extended retention (read-only) | OI2 instances with managed storage                |

Amazon S3 backs both Parquet files and inverted-index segments for
durability. Use Index State Management (ISM) policies to transition data from hot
to warm based on age, shard size, or other conditions.

###### Important

On the Optimized engine, the warm tier is _read-only_.
Although the general multi-tier storage architecture supports writes to the
warm tier, Optimized domains do not support write operations in the warm tier. Ingest data into the hot tier and use Index State Management (ISM) policies
to transition it to warm.
