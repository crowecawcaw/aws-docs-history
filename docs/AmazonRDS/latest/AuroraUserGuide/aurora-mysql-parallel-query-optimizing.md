# Optimizing parallel query in Aurora MySQL

To optimize your DB cluster for parallel query, consider which DB clusters would benefit from parallel query and whether to upgrade for parallel query. Then, tune your workload and create schema objects for parallel query.

###### Contents

- [Planning for a parallel query cluster](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-planning "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-planning")
  - [Checking Aurora MySQL version compatibility for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility")

- [Upgrade considerations for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade")
  - [Upgrading parallel query clusters to Aurora MySQL version 3](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-pqv2 "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-pqv2")
  - [Upgrading to Aurora MySQL 2.09 and higher](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-2.09 "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-2.09")

- [Performance tuning for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-performance "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-performance")
- [Creating schema objects to take advantage of parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-tables "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-tables")

## Planning for a parallel query cluster

Planning for a DB cluster that has parallel query turned on requires making some choices. These include performing setup steps
(either creating or restoring a full Aurora MySQL cluster) and deciding how broadly to turn on parallel query across your DB
cluster.

Consider the following as part of planning:

- If you use Aurora MySQL that's compatible with MySQL 5.7, you must create a provisioned cluster. Then you turn on parallel query using the
  `aurora_parallel_query` parameter.

If you have an existing Aurora MySQL cluster, you don't have to create a new cluster to use parallel query. You can associate your cluster, or
specific DB instances in the cluster, with a parameter group that has the `aurora_parallel_query` parameter turned on. By doing so, you
can reduce the time and effort to set up the relevant data to use with parallel query.

- Plan for any large tables that you need to reorganize so that you can use parallel query when accessing them. You might
  need to create new versions of some large tables where parallel query is useful. For example, you might need to remove
  full-text search indexes. For details, see [Creating schema objects to take advantage of parallel query](#aurora-mysql-parallel-query-tables "#aurora-mysql-parallel-query-tables").

### Checking Aurora MySQL version compatibility for parallel query

To check which Aurora MySQL versions are compatible with parallel query clusters, use the
`describe-db-engine-versions` AWS CLI command and check the value of the `SupportsParallelQuery`
field. The following code example shows how to check which combinations are available for parallel query clusters in a
specified AWS Region. Make sure to specify the full `--query` parameter string on a single line.

```
aws rds describe-db-engine-versions --region us-east-1 --engine aurora-mysql \
--query '*[]|[?SupportsParallelQuery == `true`].[EngineVersion]' --output text
```

The preceding commands produce output similar to the following. The output might vary depending on which Aurora MySQL versions
are available in the specified AWS Region.

```
5.7.mysql_aurora.2.11.1
5.7.mysql_aurora.2.11.2
5.7.mysql_aurora.2.11.3
5.7.mysql_aurora.2.11.4
5.7.mysql_aurora.2.11.5
5.7.mysql_aurora.2.11.6
5.7.mysql_aurora.2.12.0
5.7.mysql_aurora.2.12.1
5.7.mysql_aurora.2.12.2
5.7.mysql_aurora.2.12.3
5.7.mysql_aurora.2.12.4
8.0.mysql_aurora.3.04.0
8.0.mysql_aurora.3.04.1
8.0.mysql_aurora.3.04.2
8.0.mysql_aurora.3.04.3
8.0.mysql_aurora.3.05.2
8.0.mysql_aurora.3.06.0
8.0.mysql_aurora.3.06.1
8.0.mysql_aurora.3.07.0
8.0.mysql_aurora.3.07.1
```

After you start using parallel query with a cluster, you can monitor performance and
remove obstacles to parallel query usage. For those instructions, see
[Performance tuning for parallel query](#aurora-mysql-parallel-query-performance "#aurora-mysql-parallel-query-performance").

## Upgrade considerations for parallel query

Depending on the original and destination versions when you upgrade a parallel query cluster, you might
find enhancements in the types of queries that parallel query can optimize. You might also find that
you don't need to specify a special engine mode parameter for parallel query. The following sections
explain the considerations when you upgrade a cluster that has parallel query turned on.

### Upgrading parallel query clusters to Aurora MySQL version 3

Several SQL statements, clauses, and data types have new or improved parallel query support starting in
Aurora MySQL version 3. When you upgrade from a release that's earlier than version 3, check whether additional
queries can benefit from parallel query optimizations. For information about these parallel query enhancements,
see [Column data types](aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-datatypes "aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-datatypes"),
[Partitioned tables](aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-partitioning "aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-partitioning"),
and [Aggregate functions, GROUP BY clauses, and HAVING clauses](aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-aggregation "aurora-mysql-parallel-query-sql.md#aurora-mysql-parallel-query-sql-aggregation").

If you're upgrading a parallel query cluster from Aurora MySQL 2.08 or lower, also learn about changes in how to turn on
parallel query. To do so, read [Upgrading to Aurora MySQL 2.09 and higher](#aurora-mysql-parallel-query-upgrade-2.09 "#aurora-mysql-parallel-query-upgrade-2.09").

In Aurora MySQL version 3, hash join optimization is turned on by default. The `aurora_disable_hash_join`
configuration option from earlier versions isn't used.

### Upgrading to Aurora MySQL 2.09 and higher

In Aurora MySQL version 2.09 and higher, parallel query works for provisioned clusters and doesn't require the
`parallelquery` engine mode parameter. Thus, you don't need to create a new cluster or restore from an
existing snapshot to use parallel query with these versions. You can use the upgrade procedures described in [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md") to upgrade your cluster to such a
version. You can upgrade an older cluster regardless of whether it was a parallel query cluster or a provisioned cluster. To
reduce the number of choices in the **Engine version** menu, you can choose **Show versions that
support the parallel query feature** to filter the entries in that menu. Then choose Aurora MySQL 2.09 or
higher.

After you upgrade an earlier parallel query cluster to Aurora MySQL 2.09 or higher, you turn on parallel query in the upgraded
cluster. Parallel query is turned off by default in these versions, and the procedure for enabling it is different. The hash
join optimization is also turned off by default and must be turned on separately. Thus, make sure that you turn on these
settings again after the upgrade. For instructions on doing so, see [Turning parallel query on and off in Aurora MySQL](aurora-mysql-parallel-query-enabling.md "aurora-mysql-parallel-query-enabling.md") and [Turning on hash join for parallel query clusters](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join").

In particular, you turn on parallel query by using the configuration parameters `aurora_parallel_query=ON` and
`aurora_disable_hash_join=OFF` instead of `aurora_pq_supported` and `aurora_pq`. The
`aurora_pq_supported` and `aurora_pq` parameters are deprecated in the newer Aurora MySQL
versions.

In the upgraded cluster, the `EngineMode` attribute has the value `provisioned`
instead of `parallelquery`. To check whether parallel query is available for a specified
engine version, now you check the value of the `SupportsParallelQuery` field in the output
of the `describe-db-engine-versions` AWS CLI command. In earlier Aurora MySQL versions, you checked
for the presence of `parallelquery` in the `SupportedEngineModes` list.

After you upgrade to Aurora MySQL version 2.09 or higher, you can take advantage of the following features. These features
aren't available to parallel query clusters running older Aurora MySQL versions.

- Performance Insights. For more information, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").
- Backtracking. For more information, see [Backtracking an Aurora DB cluster](AuroraMySQL.Managing.md "AuroraMySQL.Managing.md").
- Stopping and starting the cluster. For more information, see [Stopping and starting an Amazon Aurora DB cluster](aurora-cluster-stop-start.md "aurora-cluster-stop-start.md").

## Performance tuning for parallel query

To manage the performance of a workload with parallel query, make sure that parallel query is used for the
queries where this optimization helps the most.

To do so, you can do the following:

- Make sure that your biggest tables are compatible with parallel query.
  You might change table properties or recreate some tables so that queries
  for those tables can take advantage of the parallel query optimization.
  To learn how, see [Creating schema objects to take advantage of parallel query](#aurora-mysql-parallel-query-tables "#aurora-mysql-parallel-query-tables").
- Monitor which queries use parallel query.
  To learn how, see [Monitoring parallel query for Aurora MySQL](aurora-mysql-parallel-query-monitoring.md "aurora-mysql-parallel-query-monitoring.md").
- Verify that parallel query is being used for the most data-intensive and long-running queries,
  and with the right level of concurrency for your workload.
  To learn how, see [Verifying which statements use parallel query for Aurora MySQL](aurora-mysql-parallel-query-verifying.md "aurora-mysql-parallel-query-verifying.md").
- Fine-tune your SQL code to turn on parallel query to apply to the queries that you
  expect. To learn how, see
  [SQL constructs for parallel query in Aurora MySQL](aurora-mysql-parallel-query-sql.md "aurora-mysql-parallel-query-sql.md").

## Creating schema objects to take advantage of parallel query

Before you create or modify tables that you plan to use for parallel query, make sure to familiarize yourself
with the requirements described in
[Prerequisites](aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-prereqs "aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-prereqs") and
[Limitations](aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations "aurora-mysql-parallel-query.md#aurora-mysql-parallel-query-limitations").

Because parallel query requires tables to use the `ROW_FORMAT=Compact` or `ROW_FORMAT=Dynamic` setting,
check your Aurora configuration settings for any changes to the `INNODB_FILE_FORMAT`
configuration option. Issue the `SHOW TABLE STATUS` statement to confirm the row
format for all the tables in a database.

Before changing your schema to turn on parallel query to work with more tables, make sure
to test. Your tests should confirm if parallel query results in a net increase in performance
for those tables. Also, make sure that the schema requirements for parallel query are
otherwise compatible with your goals.

For example, before switching from `ROW_FORMAT=Compressed` to `ROW_FORMAT=Compact` or
`ROW_FORMAT=Dynamic`, test the performance of workloads for the original and new tables. Also,
consider other potential effects such as increased data volume.
