

# Best Practices for Parallel Queries in Aurora PostgreSQL
<a name="PostgreSQL.ParallelQueries"></a>

Parallel query execution is a feature in PostgreSQL that allows a single SQL query to be broken into smaller tasks that are processed simultaneously by multiple background worker processes. Instead of executing a query entirely in a single backend process, PostgreSQL can distribute parts of the query, such as scans, joins, aggregations, or sorting, across multiple CPU cores. The *leader process* coordinates this execution and gathers the results from the *parallel workers*.

However, for most production workloads, especially high-concurrency OLTP systems, we recommend disabling automatic parallel query execution. While parallelism can accelerate queries on large datasets in analytics or reporting workloads, it introduces significant risks that often outweigh the benefits in busy production environments.

Parallel execution also introduces significant overhead. Each parallel worker is a full PostgreSQL backend process, which requires process forking (copying memory structures and initializing process state) and authentication (consuming connection slots from your `max_connections` limit). Each worker also consumes its own memory, including `work_mem` for sorting and hashing operations, with multiple workers per query, memory usage multiplies quickly (e.g., 4 workers × 64MB `work_mem` = 256MB per query). As a result, parallel queries can consume considerably more system resources than single-process queries. If not tuned properly, they may lead to CPU saturation (multiple workers overwhelming available processing capacity), increased context switching (the operating system frequently switching between numerous worker processes, adding overhead and reducing throughput), or connection exhaustion (since each parallel worker consumes a connection slot, a single query with 4 workers uses 5 connections total, 1 leader \+ 4 workers, which can quickly exhaust your connection pool under high concurrency, preventing new client connections and causing application failures). These issues are particularly severe under high-concurrency workloads where multiple queries may attempt parallel execution simultaneously.

PostgreSQL decides whether to use parallelism based on cost estimates. In some cases, the planner may automatically switch to a parallel plan if it appears cheaper even when it's not ideal in practice. This can happen if index statistics are outdated or if bloat makes sequential scans appear more attractive than index lookups. Because of this behavior, automatic parallel plans can sometimes introduce regressions in query performance or system stability.

To get the most benefit from parallel queries in Aurora PostgreSQL, it's important to test and tune them based on your workload, monitor system impact, and disable automatic parallel plan selection in favor of query-level control.

## Configuration Parameters
<a name="PostgreSQL.ParallelQueries.ConfigurationParameters"></a>

PostgreSQL uses several parameters to control the behavior and availability of parallel queries. Understanding and tuning these is critical to achieving predictable performance:


| Parameter | Description | Default | 
| --- | --- | --- | 
| max\_parallel\_workers | Maximum number of background worker processes that can run in total | GREATEST($DBInstanceVCPU/2,8) | 
| max\_parallel\_workers\_per\_gather | Maximum number of workers per query plan node (e.g., per Gather) | 2 for Aurora PostgreSQL 17 and earlier versions. 0 for Aurora PostgreSQL 18 and later versions. | 
| parallel\_setup\_cost | Planner cost added for initiating parallel query infrastructure | 1000 | 
| parallel\_tuple\_cost | Cost per tuple processed in parallel mode (impacts planner decision) | 0.1 | 
| force\_parallel\_mode | Forces planner to test parallel plans (off, on, regress) | off | 

### Key Considerations
<a name="PostgreSQL.ParallelQueries.ConfigurationParameters.KeyConsiderations"></a>
+ `max_parallel_workers` controls the total pool of parallel workers. If set too low, some queries may fall back to serial execution.
+ `max_parallel_workers_per_gather` affects how many workers a single query can use. A higher value increases concurrency, but also resource usage.
+ `parallel_setup_cost` and `parallel_tuple_cost` affect the planner's cost model. Lowering these can make parallel plans more likely to be chosen.
+ `force_parallel_mode` is useful for testing but should not be used in production unless necessary.

**Note**  
The default value of the `max_parallel_workers` parameter is dynamically calculated based on instance size using the formula `GREATEST($DBInstanceVCPU/2, 8)`. This means that when you scale your Aurora instance to a larger compute size with more vCPUs, the maximum number of available parallel workers will automatically increase. As a result, queries that previously executed serially or with limited parallelism may suddenly utilize more parallel workers after a scale-up operation, potentially leading to unexpected increases in connection usage, CPU utilization, and memory consumption. It's important to monitor parallel query behavior after any compute scaling event and adjust `max_parallel_workers_per_gather` if necessary to maintain predictable resource usage.

## Identify Parallel Queries Usage
<a name="PostgreSQL.ParallelQueries.IdentifyUsage"></a>

Queries may flip to parallel plans based on data distribution or statistics. For example:

```
SELECT count(*) FROM customers WHERE last_login < now() - interval '6 months';
```

This query might use an index for recent data, but switch to a parallel sequential scan for historical data.

You can log query execution plans by loading the `auto_explain` module. To learn more, see [Logging execution plans of queries](https://aws.amazon.com/premiumsupport/knowledge-center/rds-postgresql-tune-query-performance/#) in the AWS knowledge center.

You can monitor query execution plans in your Aurora PostgreSQL DB instance to detect the execution plans contributing to current database load and to track performance statistics of execution plans over time using the `aurora_compute_plan_id` parameter. To learn more, see [Monitoring query execution plans and peak memory for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.Plans.html)

You can monitor [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights-Database-Instance-Dashboard.html) for Parallel Query related wait events. To learn more about Parallel Query related wait events, go through [IPC:parallel wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-ipc-parallel.html)

From PostgreSQL version 18, you can monitor parallel worker activity using new columns in [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW) and [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html):
+ `parallel_workers_to_launch`: Number of parallel workers planned to be launched
+ `parallel_workers_launched`: Number of parallel workers actually launched

These metrics help identify discrepancies between planned and actual parallelism, which can indicate resource constraints or configuration issues. Use the following queries to monitor parallel execution:

For Database-level parallel worker metrics:

```
SELECT datname, parallel_workers_to_launch, parallel_workers_launched
FROM pg_stat_database
WHERE datname = current_database();
```

For Query-level parallel worker metrics

```
SELECT query, parallel_workers_to_launch, parallel_workers_launched
FROM pg_stat_statements
ORDER BY parallel_workers_launched;
```

## How to Control Parallelism
<a name="PostgreSQL.ParallelQueries.ControlParallelism"></a>

There are several ways to control query parallelism, each designed for different scenarios and requirements.

To disable automatic parallelism globally, [modify your parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Modifying.html) to set:

```
max_parallel_workers_per_gather = 0;
```

For persistent, user-specific settings, the ALTER ROLE command provides a way to set parameters that will apply to all future sessions for a particular user.

For example:

`ALTER ROLE username SET max_parallel_workers_per_gather = 4;` ensures that every time this user connects to the database, their sessions will use this parallel worker setting when required.

Session-level control can be achieved using the SET command, which modifies parameters for the duration of the current database session. This is particularly useful when you need to temporarily adjust settings without affecting other users or future sessions. Once set, these parameters remain in effect until explicitly reset or until the session ends. The commands are straightforward:

```
SET max_parallel_workers_per_gather = 4;
-- Run your queries
RESET max_parallel_workers_per_gather;
```

For even more granular control, SET LOCAL allows you to modify parameters for a single transaction. This is ideal when you need to adjust settings for a specific set of queries within a transaction, after which the settings automatically revert to their previous values. This approach helps prevent unintended effects on other operations within the same session.

### Utilize Query Plan Management (QPM)
<a name="PostgreSQL.ParallelQueries.ControlParallelism.QPM"></a>

In Aurora PostgreSQL, the Query Plan Management (QPM) feature is designed to ensure plan adaptability and stability, regardless of database environment changes that might cause query plan regression. For more information, see [Overview of Aurora PostgreSQL query plan management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.overview.html). QPM provides some control over the optimizer. Review approved plans in QPM to ensure they align with current parallelism settings. Update or remove outdated plans that may be forcing suboptimal parallel execution.

You can also fix the plans using pg\_hint\_plan. For more information, see [Fixing plans using pg\_hint\_plan](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Maintenance.html#AuroraPostgreSQL.Optimize.Maintenance.pg_hint_plan). You can use the hint named `Parallel` to enforce parallel execution. For more information, see the [Hints for parallel plans](https://github.com/ossc-db/pg_hint_plan/blob/master/docs/hint_table.md#hints-for-parallel-plans).

## Diagnosing Parallel Query Behavior
<a name="PostgreSQL.ParallelQueries.Diagnosing"></a>

Use `EXPLAIN (ANALYZE, VERBOSE)` to confirm whether a query used parallel execution:
+ Look for nodes such as `Gather`, `Gather Merge`, or `Parallel Seq Scan`.
+ Compare plans with and without parallelism.

To disable parallelism temporarily for comparison:

```
SET max_parallel_workers_per_gather = 0;
EXPLAIN ANALYZE <your_query>;
RESET max_parallel_workers_per_gather;
```