

# Low used and redundant indexes
<a name="anti-pattern-low-used-redundant-indexes"></a>

## Overview
<a name="low-indexes-overview"></a>

Indexes improve overall query performance of workloads, but come with costs. Each index consumes storage and I/O resources, and write operations need to update all indexes on the collection. If your database contains unused, underutilized, or redundant indexes, it results in overhead to the cluster, leading to performance degradation. Multiple unnecessary indexes create an anti-pattern that causes performance issues, increased storage costs, and higher operational overhead.

**Sub optimal indexing scenarios**
+ **Unused Indexes**: Indexes created for one-time queries, or in earlier product iterations that are no longer accessed by current query patterns. To identify unused indexes on a collection you can use indexStats. For more information, see [How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage).
+ **Redundant Indexes**: Multiple indexes covering overlapping key patterns or identical query patterns. Example: A single-key index on attribute A becomes redundant when a composite index covers both attribute A and B, since the composite index can handle queries on attribute A alone.
+ **Over-Indexing**: Creating indexes "just in case" without analyzing actual query patterns or performance requirements.
+ **Low Cardinality Indexes**: Indexes on fields with few distinct values (e.g., boolean fields, status flags) that provide minimal query optimization benefit.

## Impact on Cluster Performance
<a name="low-indexes-impact"></a>
+ **Storage and IO**: Each index consumes storage space and IO resources, contributing to overall costs. If an index is unused or redundant, it represents unnecessary cost on your cluster.
+ **Degraded Write Performance**: Insert, update, and delete operations must maintain indexes, creating overhead that consumes resources. Unused or redundant indexes add unnecessary overhead to these operations.
+ **Memory and CPU Pressure**: Indexes compete for buffer pool memory and may evict frequently accessed data if the working set doesn't fit in instance memory resulting in suboptimal BufferCacheHitRatio. The system also consumes CPU resources maintaining index structures.

## Tools available to identify index optimization opportunities
<a name="low-indexes-tools"></a>
+ Index Review Tool:
+ Index Cardinality Detection Tool

**Gathering the toolkit:**

```
git clone https://github.com/awslabs/amazon-documentdb-tools.git
```

**1. Index Review Tool**

The index review tool analyzes all collections and indexes to provide a listing of indexes, their usage patterns, and identifies redundant indexes on your Amazon DocumentDB cluster. Execute this tool on all cluster instances for comprehensive analysis. For more information, see [Index Review Tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/performance/index-review).

**Usage:**

```
cd performance/index-review/

python3 index-review.py --server-alias <server-alias> --uri <mongodb-uri>
```

**Output Files**
+ `{server-alias}-collections.csv`: Collection-level statistics
+ `{server-alias}-indexes.csv`: Detailed index usage metrics
+ `{server-alias}-{timestamp}-index-review.json`: Raw data for further analysis

**Note**  
Run for each instance in the cluster with an independent alias to generate stats from each instance, and then run the tool to get you a cumulative analysis

Eg: `python3 index-review.py --files "{server-alias}-{timestamp}-index-review.json, {server-alias}-{timestamp}-index-review.json" --server-alias full-review`

**2. Index Cardinality Detection Tool**

This tool identifies indexes with low cardinality that are inefficient for query performance.

**Usage**

```
cd performance/index-cardinality-detection/

python3 detect-cardinality.py --uri <mongodb-uri>
```

**Parameters**
+ `--threshold`: Cardinality threshold percentage (default: 1%)
+ `--sample-count`: Number of documents to sample (default: 100,000)
+ `--max-collections`: Maximum collections to scan per database (default: 100)

For more information, see [https://aws.amazon.com/blogs/database/detect-and-fix-low-cardinality-indexes-in-amazon-documentdb/](https://aws.amazon.com/blogs/database/detect-and-fix-low-cardinality-indexes-in-amazon-documentdb/)

## Remediation strategies
<a name="low-indexes-remediation"></a>

**1. Unused and redundant Index Removal**

```
// Example: Drop unused index
db.collection.dropIndex("unused_index_name")
```

**Note**  
Indexes should never be dropped without discussing with all interested parties and testing performance.

**2. Low Cardinality Index Optimization**
+ Use partial indexes with filters
+ Convert single low-cardinality indexes to compound indexes