

# DML limitations and other information for Aurora PostgreSQL Limitless Database
<a name="limitless-reference.DML-limitations"></a>

The following topics describe limitations or provide more information for DML and query processing SQL commands in Aurora PostgreSQL Limitless Database.

**Topics**
+ [ANALYZE](#limitless-reference.DML-limitations.ANALYZE)
+ [CLUSTER](#limitless-reference.DML-limitations.CLUSTER)
+ [EXPLAIN](#limitless-reference.DML-limitations.EXPLAIN)
+ [INSERT](#limitless-reference.DML-limitations.INSERT)
+ [UPDATE](#limitless-reference.DML-limitations.UPDATE)
+ [VACUUM](#limitless-reference.DML-limitations.VACUUM)

## ANALYZE
<a name="limitless-reference.DML-limitations.ANALYZE"></a>

The `ANALYZE` command collects statistics about the contents of tables in the database. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries. For more information, see [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html) in the PostgreSQL documentation.

In Aurora PostgreSQL Limitless Database, the `ANALYZE` command collects table statistics across all routers and shards when it runs.

To prevent the calculation of statistics on every router during `ANALYZE` runs, table statistics are calculated on one of the routers and then copied to peer routers.

## CLUSTER
<a name="limitless-reference.DML-limitations.CLUSTER"></a>

The `CLUSTER` command physically reorders a table based on an index. The index must already have been defined on the table. In Aurora PostgreSQL Limitless Database, the clustering is local to the part of the index that's present on each shard.

For more information, see [CLUSTER](https://www.postgresql.org/docs/current/sql-cluster.html) in the PostgreSQL documentation.

## EXPLAIN
<a name="limitless-reference.DML-limitations.EXPLAIN"></a>

You use the following parameter to configure the output from the `EXPLAIN` command:
+ `rds_aurora.limitless_explain_options` – What to include in the `EXPLAIN` output. The default value is `single_shard_optimization`: whether plans are single-shard optimized is shown, but shard plans aren't included.

In this example, the `EXPLAIN` output doesn't show plans from shards.

```
postgres_limitless=> EXPLAIN SELECT * FROM employees where id =25;

                      QUERY PLAN
------------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
 Single Shard Optimized
(2 rows)
```

Now we set the `rds_aurora.limitless_explain_options` to include `shard_plans` and `single_shard_optimization`. We can view the execution plans of statements on both routers and shards. In addition, we disable the `enable_seqscan` parameter to enforce that index scan is used on the shard layer.

```
postgres_limitless=> SET rds_aurora.limitless_explain_options = shard_plans, single_shard_optimization;
SET

postgres_limitless=> SET enable_seqscan = OFF;
SET

postgres_limitless=> EXPLAIN SELECT * FROM employees WHERE id = 25;

                                                        QUERY PLAN
--------------------------------------------------------------------------------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
   Remote Plans from Shard postgres_s4:
         Index Scan using employees_ts00287_id_idx on employees_ts00287 employees_fs00003  (cost=0.14..8.16 rows=1 width=15)
           Index Cond: (id = 25)
 Single Shard Optimized
(5 rows)
```

For more information on the `EXPLAIN` command, see [EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) in the PostgreSQL documentation.

## INSERT
<a name="limitless-reference.DML-limitations.INSERT"></a>

Most `INSERT` commands are supported in Aurora PostgreSQL Limitless Database.

PostgreSQL doesn't have an explicit `UPSERT` command, but it does support `INSERT ... ON CONFLICT` statements.

`INSERT ... ON CONFLICT` isn't supported if the conflict action has a subquery or a mutable function:

```
-- RANDOM is a mutable function.
INSERT INTO sharded_table VALUES (1, 100) ON CONFLICT (id) DO UPDATE SET other_id = RANDOM();

ERROR: Aurora Limitless Tables doesn't support pushdown-unsafe functions with DO UPDATE clauses.
```

For more information on the `INSERT` command, see [INSERT](https://www.postgresql.org/docs/current/sql-insert.html) in the PostgreSQL documentation.

## UPDATE
<a name="limitless-reference.DML-limitations.UPDATE"></a>

Updating the shard key isn't supported. For example, you have a sharded table called `customers`, with a shard key `customer_id`. The following DML statements cause errors:

```
postgres_limitless=> UPDATE customers SET customer_id = 11 WHERE customer_id =1;
ERROR:  Shard key column update is not supported

postgres_limitless=> UPDATE customers SET customer_id = 11 WHERE customer_name='abc';
ERROR:  Shard key column update is not supported
```

To update a shard key, first you have to `DELETE` the row with the shard key, then `INSERT` a new row with the updated shard key value.

For more information on the `UPDATE` command, see [Updating data](https://www.postgresql.org/docs/current/dml-update.html) in the PostgreSQL documentation.

## VACUUM
<a name="limitless-reference.DML-limitations.VACUUM"></a>

You can perform vacuuming on both sharded and reference tables. The following `VACUUM` functions are fully supported in Aurora PostgreSQL Limitless Database:
+ VACUUM
+ [ANALYZE](#limitless-reference.DML-limitations.ANALYZE)
+ DISABLE\_PAGE\_SKIPPING
+ FREEZE
+ FULL
+ INDEX\_CLEANUP
+ PARALLEL
+ PROCESS\_TOAST
+ TRUNCATE
+ VERBOSE

`VACUUM` on Aurora PostgreSQL Limitless Database has the following limitations:
+ The [pg\_visibility\_map](https://www.postgresql.org/docs/current/pgvisibility.html) extension isn't supported.
+ Checking for unused indexes with the [pg\_stat\_all\_indexes](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-INDEXES-VIEW) view isn't supported.
+ Consolidated views for [pg\_stat\_user\_indexes](https://www.postgresql.org/docs/current/monitoring-stats.html), [pg\_class](https://www.postgresql.org/docs/current/catalog-pg-class.html), and [pg\_stats](https://www.postgresql.org/docs/current/view-pg-stats.html) aren't implemented.

For more information on the `VACUUM` command, see [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html) in the PostgreSQL documentation. For more information on how vacuuming works in Aurora PostgreSQL Limitless Database, see [Reclaiming storage space by vacuuming](limitless-vacuum.md).