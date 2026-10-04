

# Execution plan
<a name="aurora-analytics-execution-plan"></a>

Aurora PostgreSQL integrates with PostgreSQL's EXPLAIN infrastructure to help you understand how queries are executed, identify pushdown opportunities, and diagnose performance issues. This topic explains how to read foreign table query execution plans, the different plan types, and the factors that influence plan choices.

**Topics**
+ [Plan types](#aurora-analytics-plan-types)
+ [Reading an execution plan: walkthrough](#aurora-analytics-reading-plan-walkthrough)
+ [Using EXPLAIN VERBOSE to see Pushdown SQL](#aurora-analytics-explain-verbose)
+ [Understanding "Unsupported Pushdown Expressions"](#aurora-analytics-unsupported-pushdown)
+ [Tuning queries for full pushdown](#aurora-analytics-tuning-pushdown)
+ [EXPLAIN ANALYZE metrics reference](#aurora-analytics-explain-analyze-metrics)
+ [Tips for execution plan analysis](#aurora-analytics-tips)

## Plan types
<a name="aurora-analytics-plan-types"></a>

Aurora PostgreSQL uses two pushdown strategies, chosen automatically by the planner:

**Topics**
+ [Full query pushdown](#aurora-analytics-full-pushdown)
+ [Table-scan pushdown (fallback)](#aurora-analytics-table-scan-pushdown)

### Full query pushdown
<a name="aurora-analytics-full-pushdown"></a>

The entire query (including JOINs, aggregations, subqueries, CTEs, ORDER BY, and LIMIT) is pushed to the analytics engine. This is the fastest execution path.

You see a single `Custom Scan` node at the top level of the plan:

```
EXPLAIN (COSTS OFF) SELECT status, count(*), sum(total_amount)
FROM ft_orders
WHERE order_date > '2024-01-01'
GROUP BY status
ORDER BY sum(total_amount) DESC
LIMIT 5;
```

```
                 QUERY PLAN
--------------------------------------------
 Custom Scan
   ->  TOP_N
         Top: 5
         Order By: sum(total_amount) DESC
         ->  HASH_GROUP_BY
               Groups: #0
               Aggregates: count_star(), sum(#1)
               ->  READ_PARQUET
                     Table: ft_orders
                     Filters: order_date>'2024-01-01'
                     Projections: status, total_amount
```

Everything inside the `Custom Scan` is executed by the analytics engine using columnar processing.

### Table-scan pushdown (fallback)
<a name="aurora-analytics-table-scan-pushdown"></a>

When the full query contains constructs that can't be pushed to the analytical engine, Aurora PostgreSQL falls back to pushing only the foreign table scan. The scan still pushes down its supported filter conditions and column projections, and the engine reads only the needed columns and rows. The JOINs, sorts, and unsupported operations then run in PostgreSQL.

You see `Custom Scan` nodes nested inside standard PostgreSQL nodes:

```
EXPLAIN (COSTS OFF) SELECT ft.price, soundex(ft.mainroad)
FROM ft_house_price ft
LIMIT 5;
```

```
              QUERY PLAN
--------------------------------------
 Limit
   ->  Custom Scan on ft_house_price
         ->  READ_PARQUET
               Table: ft_house_price
               Projections: price, mainroad
```

Here, `soundex()` is a PostgreSQL function that can't be pushed to the analytics engine. The engine reads the columns (price, mainroad) efficiently via READ\_PARQUET, then PostgreSQL applies `soundex()` locally.

## Reading an execution plan: walkthrough
<a name="aurora-analytics-reading-plan-walkthrough"></a>

The following examples use real execution plans from a TPC-H SF100 dataset (\~34 GB Parquet) on a db.r8gd.8xlarge instance.

**Topics**
+ [Example 1: Full query pushdown (aggregation with filter)](#aurora-analytics-example-full-pushdown-aggregation)
+ [Example 2: Multi-table JOIN with full pushdown](#aurora-analytics-example-multi-table-join)
+ [Example 3: Full query pushdown with a local table](#aurora-analytics-example-local-table)

### Example 1: Full query pushdown (aggregation with filter)
<a name="aurora-analytics-example-full-pushdown-aggregation"></a>

This is TPC-H Query 1, a scan, filter, group-by, and sort on a single large table:

```
EXPLAIN (ANALYZE, VERBOSE, COSTS OFF, TIMING OFF, BUFFERS OFF, SUMMARY OFF)
SELECT l_returnflag, l_linestatus, count(*), sum(l_quantity), avg(l_extendedprice)
FROM ft_lineitem
WHERE l_shipdate <= '1998-09-01'
GROUP BY l_returnflag, l_linestatus
ORDER BY l_returnflag, l_linestatus;
```

```
 Custom Scan (actual rows=4 loops=1)
   Output: aurora_analytics.l_returnflag, aurora_analytics.l_linestatus, aurora_analytics.count, ...
   Pushdown SQL: SELECT l_returnflag, l_linestatus, count(*) AS count, sum(l_quantity) AS sum,
     avg(l_extendedprice) AS avg FROM (SELECT l_quantity::DECIMAL(15,2) AS l_quantity,
     l_extendedprice::DECIMAL(15,2) AS l_extendedprice, l_returnflag::VARCHAR COLLATE "C" AS l_returnflag,
     l_linestatus::VARCHAR COLLATE "C" AS l_linestatus, l_shipdate::DATE AS l_shipdate
     FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_lineitem) ft_lineitem
     WHERE (l_shipdate <= '1998-09-01'::DATE)
     GROUP BY l_returnflag, l_linestatus ORDER BY l_returnflag, l_linestatus
   ->  ORDER_BY (actual rows=4 loops=1)
         Order By: ft_lineitem.l_returnflag ASC, ft_lineitem.l_linestatus ASC
         ->  HASH_GROUP_BY (actual rows=4 loops=1)
               Groups: #0, #1
               Aggregates: count_star(), sum(#2), avg(#3)
               ->  PROJECTION (actual rows=591411581 loops=1)
                     Projections: l_returnflag, l_linestatus, l_quantity, l_extendedprice
                     ->  READ_PARQUET (actual rows=591411581 loops=1)
                           Table: ft_lineitem
                           Filters: l_shipdate<='1998-09-01'::DATE
                           Projections: l_quantity, l_extendedprice, l_returnflag, l_linestatus
                           Total Files Read: 21
                           Rows Removed by Filter: 15303257125
 Analytics Cache Hit Bytes: 4617440kB
 Analytics Remote Read Bytes: 16kB
 S3 HEAD Request Count: 0
 S3 GET Request Count: 2
```

**Reading this plan bottom-up:**

1. **READ\_PARQUET**: Scanned `ft_lineitem` across 21 Parquet files. The filter `l_shipdate <= '1998-09-01'` was pushed to the scan level (predicate pushdown), skipping row groups that didn't match. "Rows Removed by Filter: 15,303,257,125" means billions of row-group entries were eliminated using min/max statistics. Only 4 columns were projected: `l_quantity`, `l_extendedprice`, `l_returnflag`, `l_linestatus`. The other 12 lineitem columns were never read from Amazon S3.

1. **PROJECTION**: Passed 591 million qualifying rows with the 4 projected columns to the aggregation stage.

1. **HASH\_GROUP\_BY**: Grouped by `l_returnflag` and `l_linestatus` (4 distinct combinations), computing `count(*)`, `sum(l_quantity)`, and `avg(l_extendedprice)`. Reduced 591M rows to 4 output rows.

1. **ORDER\_BY**: Sorted the 4 result rows by `l_returnflag`, `l_linestatus`.

1. **Custom Scan (aurora\_analytics)**: Top-level wrapper. Returned 4 rows to PostgreSQL. The `Pushdown SQL` line confirms the entire query was pushed to the analytical engine.

**Cache and S3 metrics:**
+ Cache hit: \~4.5 GB (warm, data was cached from prior runs)
+ Remote read: 16 KB (nearly everything served from cache)
+ 0 HEAD requests, 2 GET requests (minimal Amazon S3 activity)
+ Almost all data was served from the cache, with minimal Amazon S3 activity

### Example 2: Multi-table JOIN with full pushdown
<a name="aurora-analytics-example-multi-table-join"></a>

This is TPC-H Query 5, a 4-table join with filter, aggregation, sort, and limit:

```
EXPLAIN (ANALYZE, VERBOSE, COSTS OFF, TIMING OFF, BUFFERS OFF, SUMMARY OFF)
SELECT n_name, count(*), sum(l_extendedprice * (1 - l_discount)) as revenue
FROM ft_lineitem
JOIN ft_orders ON l_orderkey = o_orderkey
JOIN ft_customer ON o_custkey = c_custkey
JOIN ft_nation ON c_nationkey = n_nationkey
WHERE o_orderdate >= '1994-01-01' AND o_orderdate < '1995-01-01'
GROUP BY n_name
ORDER BY revenue DESC
LIMIT 5;
```

```
 Custom Scan (actual rows=5 loops=1)
   Output: aurora_analytics.n_name, aurora_analytics.count, (aurora_analytics.revenue)::numeric
   Pushdown SQL: SELECT ft_nation.n_name, count(*) AS count,
     sum((ft_lineitem.l_extendedprice * ((1::INTEGER)::numeric - ft_lineitem.l_discount))) AS revenue
     FROM ((((SELECT ... FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_lineitem) ...
     JOIN ... ft_orders ... JOIN ... ft_customer ... JOIN ... ft_nation ...)))
     WHERE ((ft_orders.o_orderdate >= '1994-01-01'::DATE) AND (ft_orders.o_orderdate < '1995-01-01'::DATE))
     GROUP BY ft_nation.n_name
     ORDER BY ... DESC LIMIT 5::INTEGER
   ->  TOP_N (actual rows=5 loops=1)
         Top: 5
         Order By: sum(...) DESC
         ->  HASH_GROUP_BY (actual rows=25 loops=1)
               Groups: #0
               Aggregates: count_star(), sum(#1)
               ->  PROJECTION (actual rows=91044214 loops=1)
                     Projections: n_name, (l_extendedprice * (1.000 - CAST(l_discount AS DECIMAL(18,3))))
                     ->  HASH_JOIN (actual rows=91044214 loops=1)
                           Join Type: INNER
                           Conditions: l_orderkey = o_orderkey
                           ->  READ_PARQUET (actual rows=92006243 loops=1)
                                 Table: ft_lineitem
                                 Projections: l_orderkey, l_extendedprice, l_discount
                                 Dynamic Filters: optional: l_orderkey>=5 AND l_orderkey<=599999975
                                   AND l_orderkey IN BF(o_orderkey)
                                 Total Files Read: 21
                                 Rows Removed by Filter: 15802662463
                           ->  HASH_JOIN (actual rows=22760819 loops=1)
                                 Join Type: INNER
                                 Conditions: c_custkey = o_custkey
                                 ->  HASH_JOIN (actual rows=10099742 loops=1)
                                       Join Type: INNER
                                       Conditions: c_nationkey = n_nationkey
                                       ->  READ_PARQUET (actual rows=10099742 loops=1)
                                             Table: ft_customer
                                             Projections: c_custkey, c_nationkey
                                             Dynamic Filters: optional: c_custkey>=1 AND c_custkey<=14999999
                                               AND c_custkey IN BF(o_custkey)
                                             Total Files Read: 2
                                             Rows Removed by Filter: 856257246
                                       ->  READ_PARQUET (actual rows=25 loops=1)
                                             Table: ft_nation
                                             Projections: n_nationkey, n_name
                                             Total Files Read: 1
                                 ->  READ_PARQUET (actual rows=22760819 loops=1)
                                       Table: ft_orders
                                       Filters: o_orderdate>='1994-01-01'::DATE AND o_orderdate<'1995-01-01'::DATE
                                       Projections: o_orderkey, o_custkey
                                       Total Files Read: 6
                                       Rows Removed by Filter: 4526635795
 Analytics Cache Hit Bytes: 3330521kB
 Analytics Remote Read Bytes: 2514317kB
 S3 HEAD Request Count: 0
 S3 GET Request Count: 4922
```

**Reading this plan bottom-up:**

1. **Four READ\_PARQUET nodes**: Each foreign table is scanned independently:
   + `ft_nation`: 25 rows from 1 file (small dimension table)
   + `ft_customer`: 10M rows from 2 files, with dynamic filter pruning from the orders join
   + `ft_orders`: 22.8M rows from 6 files, after filtering to year 1994 (4.5B rows removed by date filter)
   + `ft_lineitem`: 92M rows from 21 files, with Bloom filter pushdown from the orders join key

1. **Three HASH\_JOIN nodes**: The engine builds hash tables and joins in order:
   + nation ⋈ customer (on `c_nationkey = n_nationkey`)
   + result ⋈ orders (on `o_custkey = c_custkey`)
   + result ⋈ lineitem (on `l_orderkey = o_orderkey`)

1. **Dynamic Filters**: Aurora PostgreSQL passes join key ranges and Bloom filters from the build side to the probe side's scan. The `l_orderkey IN BF(o_orderkey)` means only lineitem rows matching orders keys are read, a significant optimization.

1. **PROJECTION**: Computes `l_extendedprice * (1 - l_discount)` for 91M joined rows.

1. **HASH\_GROUP\_BY**: Groups by `n_name` (25 nations), reduces 91M rows to 25 groups.

1. **TOP\_N**: Takes top 5 by revenue descending.

**Cache and S3 metrics:**
+ Cache hit: \~3.3 GB
+ Remote read: \~2.5 GB (partial cache coverage, some data still cold)
+ 4,922 S3 GET requests across 4 tables (30 total files)
+ Full query pushdown confirmed: all 4 tables joined inside the analytical engine

### Example 3: Full query pushdown with a local table
<a name="aurora-analytics-example-local-table"></a>

A hybrid query that joins a foreign table with a local PostgreSQL (heap) table can be fully pushed down: the analytics engine reads the local table and performs the join and aggregation itself, as long as the query uses only supported functions, data types, and collations. In the following example, `local_supp` is a local heap table joined to the `ft_lineitem` foreign table on integer keys:

```
EXPLAIN (VERBOSE, COSTS OFF)
SELECT ls.s_regionkey, count(*)
FROM ft_lineitem
JOIN local_supp ls ON ft_lineitem.l_suppkey = ls.s_suppkey
WHERE l_shipdate > '1998-01-01'
GROUP BY ls.s_regionkey;
```

```
 Custom Scan
   Output: aurora_analytics.s_regionkey, aurora_analytics.count
   Pushdown SQL: SELECT ls.s_regionkey, count(*) AS count
     FROM ((SELECT l_suppkey::BIGINT AS l_suppkey, l_shipdate::DATE AS l_shipdate
            FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_lineitem) ft_lineitem
       JOIN aurora_analytics.public.local_supp ls ON ((ft_lineitem.l_suppkey = ls.s_suppkey)))
     WHERE (ft_lineitem.l_shipdate > '1998-01-01'::DATE)
     GROUP BY ls.s_regionkey
   ->  HASH_GROUP_BY
         Groups: #0
         Aggregates: count_star()
         ->  PROJECTION
               Projections: s_regionkey
               ->  HASH_JOIN
                     Join Type: INNER
                     Conditions: l_suppkey = CAST(s_suppkey AS BIGINT)
                     ->  READ_PARQUET
                           Table: ft_lineitem
                           Filters: l_shipdate>'1998-01-01'::DATE
                           Projections: l_suppkey
                     ->  POSTGRES_SCAN
                           Table: local_supp
                           Projections: s_suppkey, s_regionkey
```

**Reading this plan:**

1. **Single top-level Custom Scan**: The entire query, including the join with the local table, is pushed to the analytics engine. There are no PostgreSQL nodes (HashAggregate, Hash Join) wrapping it, unlike the table-scan pushdown case above.

1. **POSTGRES\_SCAN (local\_supp)**: The local heap table is read by the analytics engine itself and fed into the pushed-down `HASH_JOIN`. The local table participates in the join *inside* the engine rather than being joined afterward by PostgreSQL.

1. **READ\_PARQUET (ft\_lineitem)**: The foreign table scan pushes the `l_shipdate` filter and projects only `l_suppkey`.

1. **HASH\_JOIN, HASH\_GROUP\_BY**: The join and the `GROUP BY`/`count(*)` aggregation both run inside the engine.

**Key takeaway**: Joining a foreign table with a local table does not force a fallback. As long as every function, data type, and collation in the query is supported, the local table is pushed into the analytics engine and the whole query is pushed down.

Joining a foreign table with a local PostgreSQL table does not by itself prevent full pushdown. The analytics engine can pull a local table into a pushed-down join. Full pushdown is prevented only when the query references something the engine can't push down, such as an unsupported function, data type, or collation. In the following example, the local nation table's n\_name column is character(25), an unsupported type, so Aurora PostgreSQL pushes only the foreign table scan and performs the join in PostgreSQL:

```
EXPLAIN (VERBOSE, COSTS OFF)
SELECT n_name, count(*)
FROM ft_lineitem
JOIN nation ON ft_lineitem.l_suppkey = nation.n_nationkey
WHERE l_shipdate > '1998-01-01'
GROUP BY n_name;
```

```
 HashAggregate
   Output: nation.n_name, count(*)
   Group Key: nation.n_name
   ->  Hash Join
         Output: nation.n_name
         Hash Cond: (l_suppkey = nation.n_nationkey)
         ->  Custom Scan on public.ft_lineitem
               Output: l_orderkey, l_partkey, l_suppkey, ...
               Pushdown SQL: SELECT l_suppkey FROM (SELECT l_suppkey::BIGINT AS l_suppkey,
                 l_shipdate::DATE AS l_shipdate
                 FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_lineitem)
                 ft_lineitem WHERE (l_shipdate > '1998-01-01'::DATE)
               ->  READ_PARQUET
                     Table: ft_lineitem
                     Filters: l_shipdate>'1998-01-01'::DATE
                     Projections: l_suppkey
         ->  Hash
               Output: nation.n_name, nation.n_nationkey
               ->  Seq Scan on public.nation
                     Output: nation.n_name, nation.n_nationkey
 Unsupported Pushdown Expressions:
 1: Type
    Description: character(25)
```

**Reading this plan:**

1. **Plan structure**: Unlike the previous examples, this plan has PostgreSQL nodes (HashAggregate, Hash Join, Seq Scan) wrapping the analytics engine's Custom Scan. This is table-scan pushdown, not full query pushdown.

1. **Custom Scan (ft\_lineitem)**: Aurora PostgreSQL handles only the foreign table scan. It pushes the `l_shipdate > '1998-01-01'` filter and projects only `l_suppkey`, an efficient columnar scan with predicate pushdown.

1. **Seq Scan (nation)**: The local `nation` table is read through PostgreSQL's standard executor (shared\_buffers → Aurora Storage).

1. **Hash Join**: PostgreSQL joins the two result sets using a hash join on `l_suppkey = n_nationkey`.

1. **HashAggregate**: PostgreSQL performs the GROUP BY and count(\*) aggregation.

1. **Unsupported Pushdown Expressions**: The reason full pushdown failed: `character(25)` (the `n_name` column type in the local `nation` table). The `char(n)` type is not supported for pushdown. If this table were a foreign table with `TEXT` columns, full pushdown would succeed.

**Key takeaway**: In table-scan pushdown, Aurora PostgreSQL still provides value through efficient columnar scanning with predicate pushdown and column pruning. PostgreSQL handles only the operations that can't be pushed down (unsupported functions, data types, or collations). Had the local table used a supported type such as `text` with a compatible collation, the entire hybrid join would have been pushed to the analytics engine as a single Custom Scan.

## Using EXPLAIN VERBOSE to see Pushdown SQL
<a name="aurora-analytics-explain-verbose"></a>

`EXPLAIN VERBOSE` reveals the exact SQL sent to the analytics engine:

```
EXPLAIN (VERBOSE, COSTS OFF)
SELECT status, count(*), avg(total_amount)
FROM ft_orders
WHERE order_date > '2024-01-01'
GROUP BY status;
```

```
                              QUERY PLAN
------------------------------------------------------------------------
 Custom Scan
   Output: aurora_analytics.status, aurora_analytics.count, aurora_analytics.avg
   Pushdown SQL: SELECT status, count(*) AS count, avg(total_amount) AS avg
     FROM (SELECT status::VARCHAR COLLATE "C" AS status,
                  total_amount::DECIMAL(12,2) AS total_amount,
                  order_date::TIMESTAMP AS order_date
           FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_orders)
     ft_orders WHERE (order_date > '2024-01-01'::TIMESTAMP)
     GROUP BY status
   ->  HASH_GROUP_BY
         Groups: #0
         Aggregates: count_star(), avg(#1)
         ->  READ_PARQUET
               Table: ft_orders
               Filters: order_date>'2024-01-01'
               Projections: status, total_amount, order_date
```

The `Pushdown SQL` line shows:
+ How PostgreSQL types are cast to the analytical engine's types (for example, `status::VARCHAR COLLATE "C"`)
+ The parameterized file reference (`$aurora_analytics_parameter_1`)
+ The exact WHERE, GROUP BY, and aggregations pushed to the engine

## Understanding "Unsupported Pushdown Expressions"
<a name="aurora-analytics-unsupported-pushdown"></a>

When full query pushdown fails, `EXPLAIN VERBOSE` reports **why** under the "Unsupported Pushdown Expressions" section. This tells you which constructs forced the fallback to table-scan pushdown:

```
EXPLAIN (VERBOSE, COSTS OFF)
SELECT soundex(name), age
FROM ft_passengers
LIMIT 5;
```

```
                              QUERY PLAN
------------------------------------------------------------------------
 Limit
   Output: (soundex(name)), age
   ->  Custom Scan on public.ft_passengers
         Output: soundex(name), age
         Pushdown SQL: SELECT name, age
           FROM (SELECT name::VARCHAR COLLATE "C" AS name,
                        age::DOUBLE AS age
                 FROM system.main.read_parquet($aurora_analytics_parameter_1)
                 AS ft_passengers) ft_passengers
         ->  READ_PARQUET
               Table: ft_passengers
               Projections: name, age
 Unsupported Pushdown Expressions:
 1: Function
    Description: soundex(text)
```

The plan shows:
+ **PostgreSQL handles** the `Limit` and `soundex()` function call
+ **Aurora PostgreSQL handles** only the table scan (reading `name` and `age` columns)
+ **Reason**: `soundex(text)` is not a pushdown-safe function

**Topics**
+ [Categories of unsupported expressions](#aurora-analytics-unsupported-categories)

### Categories of unsupported expressions
<a name="aurora-analytics-unsupported-categories"></a>


| Category | Examples | How to fix | 
| --- | --- | --- | 
| Function | soundex(text), st\_makepoint(...), uuid\_generate\_v4(), UDFs | Rewrite without the function, or accept table-scan pushdown | 
| Type | vector, bytea casts, integer[], geometry | Use supported types in expressions | 
| Operator | \~ (regex), LIKE with non-C collation, <\+> (pgvector) | Use C collation or pushdown-safe operators | 
| Collation | Non-C collation on comparison expressions | Use COLLATE "C" explicitly | 
| Aggregate | percent\_rank(), array\_agg() | Rewrite using supported aggregates | 
| SQL syntax | ONLY keyword, empty target list, recursive CTEs, dynamic data masking | Restructure the query | 

## Tuning queries for full pushdown
<a name="aurora-analytics-tuning-pushdown"></a>

To maximize performance, aim for full query pushdown. Use `EXPLAIN VERBOSE` to check your queries and fix unsupported expressions:

**Step 1: Check your query**

```
EXPLAIN (VERBOSE, COSTS OFF) SELECT ... FROM ft_table ...;
```

Look for "Unsupported Pushdown Expressions" in the output.

**Step 2: Identify the cause**

If present, read the category and description to understand what prevented full pushdown.

**Step 3: Fix the expression**
+ **Unsupported function**: There is no rewrite that pushes an unsupported function down. When a query applies an unsupported function (such as `soundex()`) to a foreign table column, Aurora PostgreSQL automatically falls back to table-scan pushdown: it still pushes the scan, projection, and any supported filters to the analytics engine, and applies the function in PostgreSQL on the returned rows. To regain full pushdown, avoid the unsupported function in queries against foreign tables, or precompute its result in the source data. Otherwise, accept table-scan pushdown, which still gives you efficient columnar scanning.
+ **Non-C collation**: Add explicit `COLLATE "C"` to text comparisons:

  ```
  -- Instead of:
  WHERE name LIKE 'Smith%'
  
  -- Use:
  WHERE name COLLATE "C" LIKE 'Smith%'
  ```
+ **Unsupported type**: Avoid casting to unsupported types in expressions on foreign table columns.

**Step 4: Verify**

After fixing, re-run `EXPLAIN VERBOSE` and confirm "Unsupported Pushdown Expressions" is gone.

## EXPLAIN ANALYZE metrics reference
<a name="aurora-analytics-explain-analyze-metrics"></a>

When using `EXPLAIN ANALYZE`, the following analytics-specific metrics appear at the end of the `EXPLAIN` output, summarizing Amazon S3 and cache activity for the whole query. Each has a corresponding instance-wide Amazon CloudWatch metric you can use for dashboards and alarms across queries:


| Metric | Description | Related metric | 
| --- | --- | --- | 
| Analytics Cache Hit Bytes | Data served from the local on-disk cache | AuroraAnalyticsCacheHit (Amazon CloudWatch, instance-wide) | 
| Analytics Remote Read Bytes | Data fetched from Amazon S3 (cache misses) | AuroraAnalyticsRemoteRead (Amazon CloudWatch, instance-wide) | 
| S3 HEAD Request Count | Number of S3 HEAD requests (metadata checks) | AuroraAnalyticsS3HeadRequest (Amazon CloudWatch, instance-wide) | 
| S3 GET Request Count | Number of S3 GET requests (data fetches) | AuroraAnalyticsS3GetRequest (Amazon CloudWatch, instance-wide) | 

When `aurora_analytics.track_detailed_metrics` is on, each `Custom Scan` node also reports the following per-node execution metrics:


| Metric | Description | Related metric | 
| --- | --- | --- | 
| Total CPU Time | CPU time the analytics engine spent during this node's execution | see analytics\_total\_cpu\_time in aurora\_analytics\_stat\_statements() | 
| Effective Parallelism | Average number of active worker threads during this node's execution | AuroraAnalyticsActiveThreads (Amazon CloudWatch, instance-wide) | 
| Total Thread Wait Time | Time the engine's worker threads spent waiting during this node's execution | see analytics\_total\_thread\_wait\_time in aurora\_analytics\_stat\_statements() | 

## Tips for execution plan analysis
<a name="aurora-analytics-tips"></a>
+ Always use `EXPLAIN VERBOSE` when debugging pushdown behavior. It shows both `Pushdown SQL` and `Unsupported Pushdown Expressions`.
+ A single `Custom Scan` at the top level of the plan = full pushdown (fastest). A `Custom Scan` nested inside PostgreSQL nodes (whether one or several) = table-scan pushdown (slower but still leverages the columnar scan).
+ The `Filters` line under `READ_PARQUET` confirms your WHERE clause was pushed to the scan level. If you see `Filter:` at the `Custom Scan` level instead, the predicate wasn't pushed all the way down.
+ `Projections` under `READ_PARQUET` shows which columns were read from Parquet. A query that projects fewer columns reads less data. Avoid `SELECT *` on foreign tables.
+ `Total Files Read` tells you how many Parquet files were scanned. If this seems high, consider partitioning your data.
+ `Rows Removed by Filter` shows predicate pushdown effectiveness. High values mean the filter is working well at the scan level.