# Parallel query for Amazon Aurora MySQL

This topic describes the parallel query performance optimization for Amazon Aurora MySQL-Compatible Edition. This feature uses a special processing
path for certain data-intensive queries, taking advantage of the Aurora shared storage architecture. Parallel query works best with
Aurora MySQL DB clusters that have tables with millions of rows and analytic queries that take minutes or hours to complete.

###### Topics

- [Overview of parallel query for Aurora MySQL](#aurora-mysql-parallel-query-overview "#aurora-mysql-parallel-query-overview")
- [Creating a parallel query DB cluster in Aurora MySQL](aurora-mysql-parallel-query-creating-cluster.md "aurora-mysql-parallel-query-creating-cluster.md")
- [Turning parallel query on and off in Aurora MySQL](aurora-mysql-parallel-query-enabling.md "aurora-mysql-parallel-query-enabling.md")
- [Optimizing parallel query in Aurora MySQL](aurora-mysql-parallel-query-optimizing.md "aurora-mysql-parallel-query-optimizing.md")
- [Verifying which statements use parallel query for Aurora MySQL](aurora-mysql-parallel-query-verifying.md "aurora-mysql-parallel-query-verifying.md")
- [Monitoring parallel query for Aurora MySQL](aurora-mysql-parallel-query-monitoring.md "aurora-mysql-parallel-query-monitoring.md")
- [SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md")

## Overview of parallel query for Aurora MySQL

Aurora MySQL parallel query is an optimization that parallelizes some of the I/O and computation involved
in processing data-intensive queries. The work that is parallelized includes retrieving rows from
storage, extracting column values, and determining which rows match the conditions in the
`WHERE` clause and join clauses. This data-intensive work is delegated (in database
optimization terms, _pushed down_) to multiple nodes in the Aurora
distributed storage layer. Without parallel query, each query brings all the scanned data to a single
node within the Aurora MySQL cluster (the head node) and performs all the query processing there.

###### Tip

The PostgreSQL database engine also has a feature called "parallel query." That feature is unrelated to Aurora
parallel query.

When the parallel query feature is turned on, the Aurora MySQL engine automatically
determines when queries can benefit, without requiring SQL changes such as hints or table
attributes. In the following sections, you can find an explanation of when parallel query is
applied to a query. You can also find how to make sure that parallel query is applied where it
provides the most benefit.

###### Note

The parallel query optimization provides the most benefit for long-running queries that take minutes
or hours to complete. Aurora MySQL generally doesn't perform parallel query optimization for inexpensive
queries. It also generally doesn't perform parallel query optimization if another optimization
technique makes more sense, such as query caching, buffer pool caching, or index lookups. If you find
that parallel query isn't being used when you expect it, see
[Verifying which statements use parallel query for Aurora MySQL](aurora-mysql-parallel-query-verifying.md "aurora-mysql-parallel-query-verifying.md").

###### Topics

- [Benefits](#aurora-mysql-parallel-query-benefits "#aurora-mysql-parallel-query-benefits")
- [Architecture](#aurora-mysql-parallel-query-architecture "#aurora-mysql-parallel-query-architecture")
- [Prerequisites](#aurora-mysql-parallel-query-prereqs "#aurora-mysql-parallel-query-prereqs")
- [Limitations](#aurora-mysql-parallel-query-limitations "#aurora-mysql-parallel-query-limitations")
- [I/O costs with parallel query](#aurora-mysql-parallel-query-cost "#aurora-mysql-parallel-query-cost")

### Benefits

With parallel query, you can run data-intensive analytic queries on Aurora MySQL
tables. In many cases, you can get an order-of-magnitude performance improvement over
the traditional division of labor for query processing.

Benefits of parallel query include the following:

- Improved I/O performance, due to parallelizing physical read requests across multiple
  storage nodes.
- Reduced network traffic. Aurora doesn't transmit entire data pages from storage nodes
  to the head node and then filter out unnecessary rows and columns afterward. Instead, Aurora
  transmits compact tuples containing only the column values needed for the result set.
- Reduced CPU usage on the head node, due to pushing down function processing, row filtering, and
  column projection for the `WHERE` clause.
- Reduced memory pressure on the buffer pool. The pages processed by the parallel query
  aren't added to the buffer pool. This approach reduces the chance of a data-intensive scan
  evicting frequently used data from the buffer pool.
- Potentially reduced data duplication in your extract, transform, load (ETL) pipeline, by
  making it practical to perform long-running analytic queries on existing data.

### Architecture

The parallel query feature uses the major architectural principles of Aurora MySQL:
decoupling the database engine from the storage subsystem, and reducing network traffic by
streamlining communication protocols. Aurora MySQL uses these techniques to speed up
write-intensive operations such as redo log processing. Parallel query applies the same
principles to read operations.

###### Note

The architecture of Aurora MySQL parallel query differs from that of similarly named features in other
database systems. Aurora MySQL parallel query doesn't involve symmetric multiprocessing (SMP) and
so doesn't depend on the CPU capacity of the database server. The parallel processing happens in the
storage layer, independent of the Aurora MySQL server that serves as the query coordinator.

By default, without parallel query, the processing for an Aurora query involves transmitting raw data to a
single node within the Aurora cluster (the _head node_). Aurora then performs all further
processing for that query in a single thread on that single node. With parallel query, much of this
I/O-intensive and CPU-intensive work is delegated to nodes in the storage layer. Only the compact rows of
the result set are transmitted back to the head node, with rows already filtered, and column values already
extracted and transformed. The performance benefit comes from the reduction in network traffic, reduction in
CPU usage on the head node, and parallelizing the I/O across the storage nodes. The amount of parallel I/O,
filtering, and projection is independent of the number of DB instances in the Aurora cluster that runs the
query.

### Prerequisites

Using all features of parallel query requires an Aurora MySQL DB cluster that's running version 2.09 or higher. If you already have a cluster
that you want to use with parallel query, you can upgrade it to a compatible version and turn on parallel query afterward. In that case, make sure to
follow the upgrade procedure in [Upgrade considerations for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade") because the
configuration setting names and default values are different in these newer versions.

The DB instances in your cluster must use the `db.r*` instance classes.

Make sure that hash join optimization is turned on for your cluster. To learn how, see [Turning on hash join for parallel query clusters](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join").

To customize parameters such as `aurora_parallel_query` and `aurora_disable_hash_join`,
you must have a custom parameter group that you use with your cluster. You can
specify these parameters individually for each DB instance by using a DB parameter group. However, we recommend that you
specify them in a DB cluster parameter group. That way, all DB instances in your cluster inherit the same
settings for these parameters.

### Limitations

The following limitations apply to the parallel query feature:

- Parallel query isn't supported with the Aurora I/O-Optimized DB cluster storage configuration.
- You can't use parallel query with the db.t2 or db.t3 instance classes. This limitation applies even if you
  request parallel query using the `aurora_pq_force` session variable.
- Parallel query doesn't apply to tables using the `COMPRESSED` or `REDUNDANT` row formats. Use the
  `COMPACT` or `DYNAMIC` row formats for tables you plan to use with parallel query.
- Aurora uses a cost-based algorithm to determine whether to use the parallel query mechanism for each SQL statement. Using certain SQL
  constructs in a statement can prevent parallel query or make parallel query unlikely for that statement. For information about compatibility of SQL
  constructs with parallel query, see [SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md").
- Each Aurora DB instance can run only a certain number of parallel query sessions at one time. If a query has multiple parts that use
  parallel query, such as subqueries, joins, or `UNION` operators, those phases run in sequence. The statement only counts as a single
  parallel query session at any one time. You can monitor the number of active sessions using the [parallel query status variables](aurora-mysql-parallel-query-monitoring.md "aurora-mysql-parallel-query-monitoring.md"). You can check the limit on concurrent sessions for a
  given DB instance by querying the status variable `Aurora_pq_max_concurrent_requests`.
- Parallel query is available in all AWS Regions that Aurora supports. For most AWS Regions, the minimum required Aurora MySQL version
  to use parallel query is 2.09.
- Parallel query is designed to improve the performance of data-intensive queries. It isn't designed for lightweight
  queries.
- We recommend that you use reader nodes for SELECT statements, especially data-intensive ones.

### I/O costs with parallel query

If your Aurora MySQL cluster uses parallel query, you might see an increase in `VolumeReadIOPS` values. Parallel
queries don't use the buffer pool. Thus, although the queries are fast, this optimized processing can result in an
increase in read operations and associated charges.

Parallel query I/O costs for your query are metered at the storage layer, and will be the same or larger with parallel
query turned on. Your benefit is the improvement in query performance. There are two reasons for potentially higher I/O
costs with parallel query:

- Even if some of the data in a table is in the buffer pool, parallel query requires all data to be scanned at the
  storage layer, incurring I/O costs.
- Running a parallel query doesn't warm up the buffer pool. As a result, consecutive runs of the same parallel query
  incur the full I/O cost.
