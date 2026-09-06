

# Best practices for working with indexes
<a name="best-practices-indexes"></a>

## Building indexes
<a name="best-practices-building-indexes"></a>

When importing data into Amazon DocumentDB, you should create your indexes before importing large datasets. You can use the [Amazon DocumentDB Index Tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/index-tool) to extract indexes from a running MongoDB instance or mongodump directory, and create those indexes in an Amazon DocumentDB cluster. For more guidance on migrations, see [Migrating and upgrading Amazon DocumentDB](docdb-migration.md).

## Index selectivity
<a name="best-practices-index-selectivity"></a>

Limit index creation to fields where the number of duplicate values is less than 1% of the total number of documents in the collection. As an example, if your collection contains 100,000 documents, only create indexes on fields where the same value occurs 1,000 times or fewer.

Choosing an index with a high number of unique values (that is, a high cardinality) ensures that filter operations return a small number of documents, thereby yielding good performance during index scans. An example of a high-cardinality index is a unique index, which guarantees that equality predicates return at most a single document. Examples of low-cardinality include an index over a Boolean field and an index over day of the week. Due to their poor performance, low cardinality indexes are unlikely to be chosen by the database's query optimizer. At the same time, low cardinality indexes continue to consume resources such as disk space and I/Os. As a rule of thumb, you should target indexes on fields where the typical value frequency is 1% of the total collection size or less.

Additionally, it is recommended to only create indexes on fields that are commonly utilized as a filter and regularly look for unused indexes. For more information, see [How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage).

## Impact of indexes on writing data
<a name="best-practices-impact-writing"></a>

While indexes can improve query performance by avoiding the need to scan every document in a collection, this improvement comes with a tradeoff. For each index on a collection, every time a document is inserted, updated, or deleted, the database must update the collection and write the fields to each of the indexes for the collection. For example, if a collection has nine indexes, the database must perform ten writes before acknowledging the operation to the client. Thus, each additional index incurs additional write latency, I/Os, and increase in the overall utilized storage.

Cluster instances need to be appropriately sized to keep all working set memory. This avoids the need to continuously read index pages from the storage volume, which negatively impacts performance and generates higher I/O costs. For more information, see [Instance sizing](best_practices.md#best_practices-instance_sizing).

For best performance, minimize the number of indexes in your collections, adding only those indexes necessary to improve performance for common queries. While workloads vary, a good guideline is to keep the number of indexes per collection to five or fewer.

## Identifying missing indexes
<a name="best-practices-missing-indexes"></a>

As a best practice, identify missing indexes on a regular basis. For more information, see [How do I identify missing indexes?](user_diagnostics.md#user_diagnostics-identify_missing_indexes).

## Identifying unused indexes
<a name="best-practices-unused-indexes"></a>

As a best practice, identify and remove unused indexes on a regular basis. For more information, see [How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage).