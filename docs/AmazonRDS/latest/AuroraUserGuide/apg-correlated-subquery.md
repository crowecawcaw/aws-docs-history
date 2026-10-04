

# Optimizing correlated subqueries in Aurora PostgreSQL
<a name="apg-correlated-subquery"></a>

 A correlated subquery references table columns from the outer query. It is evaluated once for every row returned by the outer query. In the following example, the subquery references a column from table ot. This table is not included in the subquery’s FROM clause, but it is referenced in the outer query’s FROM clause. If table ot has 1 million rows, the subquery needs to be evaluated 1 million times. 

```
SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
```

**Note**  
Subquery transformation and subquery cache are available in Aurora PostgreSQL beginning with version 16.8, while Babelfish for Aurora PostgreSQL supports these features from 4.2.0.
Starting with Babelfish for Aurora PostgreSQL versions 4.6.0 and 5.2.0, the following parameters control these features:  
 babelfishpg\_tsql.apg\_enable\_correlated\_scalar\_transform 
 babelfishpg\_tsql.apg\_enable\_subquery\_cache 
By default, both parameters are turned on.

## Improving Aurora PostgreSQL query performance using subquery transformation
<a name="apg-corsubquery-transformation"></a>

Aurora PostgreSQL can accelerate correlated subqueries by transforming them into equivalent outer joins. This optimization applies to the following two types of correlated subqueries:
+ Subqueries that return a single aggregate value and appear in the SELECT list.

  ```
  SELECT ot.a, ot.b, (SELECT AVG(it.b) FROM it WHERE it.a = ot.a) FROM ot;
  ```
+ Subqueries that return a single aggregate value and appear in a WHERE clause.

  ```
  SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
  ```

### Enabling transformation in the subquery
<a name="apg-corsub-transform"></a>

 To enable the transformation of correlated subqueries into equivalent outer joins, set the `apg_enable_correlated_scalar_transform` parameter to `ON`. The default value of this parameter is `OFF`. 

You can modify the cluster or instance parameter group to set the parameters. To learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

Alternatively, you can configure the setting for just the current session by the following command:

```
SET apg_enable_correlated_scalar_transform TO ON;
```

### Verifying the transformation
<a name="apg-corsub-transform-confirm"></a>

Use the EXPLAIN command to verify if the correlated subquery has been transformed into an outer join in the query plan. 

 When the transformation is enabled, the applicable correlated subquery part will be transformed into outer join. For example: 

```
postgres=> CREATE TABLE ot (a INT, b INT);
CREATE TABLE
postgres=> CREATE TABLE it (a INT, b INT);
CREATE TABLE

postgres=> SET apg_enable_correlated_scalar_transform TO ON;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);

                         QUERY PLAN
--------------------------------------------------------------
 Hash Join
   Hash Cond: (ot.a = apg_scalar_subquery.scalar_output)
   Join Filter: ((ot.b)::numeric < apg_scalar_subquery.avg)
   ->  Seq Scan on ot
   ->  Hash
         ->  Subquery Scan on apg_scalar_subquery
               ->  HashAggregate
                     Group Key: it.a
                     ->  Seq Scan on it
```

The same query is not transformed when the GUC parameter is turned `OFF`. The plan will not have outer join but subplan instead.

```
postgres=> SET apg_enable_correlated_scalar_transform TO OFF;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
                QUERY PLAN
----------------------------------------
 Seq Scan on ot
   Filter: ((b)::numeric < (SubPlan 1))
   SubPlan 1
     ->  Aggregate
           ->  Seq Scan on it
                 Filter: (a = ot.a)
```

### Limitations
<a name="apg-corsub-transform-limitations"></a>
+ The subquery must be in the SELECT list or in one of the conditions in the where clause. Otherwise, it won’t be transformed.
+ The subquery must return an aggregate function. User-defined aggregate functions aren't supported for transformation.
+ A subquery whose return expression isn't a simple aggregate function won't be transformed.
+ The correlated condition in subquery WHERE clauses should be a simple column reference. Otherwise, it won’t be transformed.
+ The correlated condition in subquery where clauses must be a plain equality predicate.
+ The subquery can't contain either a HAVING or a GROUP BY clause.
+ The where clause in the subquery may contain one or more predicates combined with AND.

**Note**  
The performance impact of transformation varies depending on your schema, data, and workload. Correlated subquery execution with transformation can significantly improve performance as the number of rows produced by the outer query increases. We strongly recommend that you test this feature in a non-production environment with your actual schema, data, and workload before enabling it in a production environment.

## Using subquery cache to improve Aurora PostgreSQL query performance
<a name="apg-subquery-cache"></a>

 Aurora PostgreSQL supports subquery cache to store the results of correlated subqueries. This feature skips repeated correlated subquery executions when subquery results are already in the cache. 

### Understanding subquery cache
<a name="apg-subquery-cache-understand"></a>

 PostgreSQL’s Memoize node is the key part of subquery cache. The Memoize node maintains a hash table in local cache to map from input parameter values to query result rows. The memory limit for the hash table is the product of work\_mem and hash\_mem\_multiplier. To learn more, see [Resource Consumption](https://www.postgresql.org/docs/16/runtime-config-resource.html). 

 During query execution, subquery cache uses Cache Hit Rate (CHR) to estimate whether the cache is improving query performance and to decide at query runtime whether to continue using the cache. CHR is the ratio of the number of cache hits to the total number of requests. For example, if a correlated subquery needs to be executed 100 times, and 70 of those execution results can be retrieved from the cache, the CHR is 0.7.

For every apg\_subquery\_cache\_check\_interval number of cache misses, the benefit of subquery cache is evaluated by checking whether the CHR is larger than apg\_subquery\_cache\_hit\_rate\_threshold. If not, the cache will be deleted from memory, and the query execution will return to the original, uncached subquery re-execution. 

### Parameters that control subquery cache behavior
<a name="apg-subquery-cache-parameters"></a>

The following table lists the parameters that control the behavior of the subquery cache.


|  Parameter  | Description  | Default | Allowed  | 
| --- | --- | --- | --- | 
| apg\_enable\_subquery\_cache | Enables the use of cache for correlated scalar subqueries. | OFF | ON, OFF | 
| apg\_subquery\_cache\_check\_interval | Sets the frequency, in number of cache misses, to evaluate subquery cache hit rate.  | 500 | 0–2147483647 | 
| apg\_subquery\_cache\_hit\_rate\_threshold | Sets the threshold for subquery cache hit rate. | 0.3 | 0.0–1.0 | 

**Note**  
Larger values of `apg_subquery_cache_check_interval` may improve the accuracy of the CHR-based cache benefit estimation, but will increase the cache overhead, since CHR won’t get evaluated until the cache table has `apg_subquery_cache_check_interval` rows. 
Larger values of `apg_subquery_cache_hit_rate_threshold` bias towards abandoning subquery cache and returning back to the original, uncached subquery re-execution. 

You can modify the cluster or instance parameter group to set the parameters. To learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

Alternatively, you can configure the setting for just the current session by the following command:

```
SET apg_enable_subquery_cache TO ON;
```

### Turning on subquery cache in Aurora PostgreSQL
<a name="apg-subquery-cache-turningon"></a>

When subquery cache is enabled, Aurora PostgreSQL applies cache to save subquery results. The query plan will then have a Memoize node under SubPlan. 

 For example, the following command sequence shows the estimated query execution plan of a simple correlated subquery without subquery cache. 

```
postgres=> SET apg_enable_subquery_cache TO OFF;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a);

             QUERY PLAN
------------------------------------
 Seq Scan on ot
   Filter: (b < (SubPlan 1))
   SubPlan 1
     ->  Seq Scan on it
           Filter: (a = ot.a)
```

After turning on `apg_enable_subquery_cache`, the query plan will contain a Memoize node under the SubPlan node, indicating that the subquery is planning to use cache.

```
postgres=> SET apg_enable_subquery_cache TO ON;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a);

             QUERY PLAN
------------------------------------
 Seq Scan on ot
   Filter: (b < (SubPlan 1))
   SubPlan 1
     ->  Memoize
           Cache Key: ot.a
           Cache Mode: binary
           ->  Seq Scan on it
                 Filter: (a = ot.a)
```

 The actual query execution plan contains more details of the subquery cache, including cache hits and cache misses. The following output shows the actual query execution plan of the above example query after inserting some values to the tables. 

```
postgres=> EXPLAIN (COSTS FALSE, TIMING FALSE, ANALYZE TRUE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a);
            QUERY PLAN
-----------------------------------------------------------------------------
 Seq Scan on ot (actual rows=2 loops=1)
   Filter: (b < (SubPlan 1))
   Rows Removed by Filter: 8
   SubPlan 1
     ->  Memoize (actual rows=0 loops=10)
           Cache Key: ot.a
           Cache Mode: binary
           Hits: 4  Misses: 6  Evictions: 0  Overflows: 0  Memory Usage: 1kB
           ->  Seq Scan on it (actual rows=0 loops=6)
                 Filter: (a = ot.a)
                 Rows Removed by Filter: 4
```

The total cache hit number is 4, and the total cache miss number is 6. If the total number of hits and misses is less than the number of loops in the Memoize node, it means that the CHR evaluation did not pass and the cache was cleaned up and abandoned at some point. The subquery execution then returned back to the original uncached re-execution.

### Limitations
<a name="apg-subquery-cache-limitations"></a>

Subquery cache does not support certain patterns of correlated subqueries. Those types of queries will be run without cache, even if subquery cache is turned on:
+ IN/EXISTS/ANY/ALL correlated subqueries
+ Correlated subqueries containing nondeterministic functions. 
+ Correlated subqueries that reference outer table columns with datatypes that don't support hashing or equality operations.

## Improving Aurora PostgreSQL query performance using subquery window transformation
<a name="apg-corsubquery-window-transformation"></a>

Aurora PostgreSQL can accelerate correlated aggregate subqueries by transforming them into equivalent window functions. This optimization applies to scalar correlated subqueries in a WHERE clause that compare an outer expression against an aggregate, such as the following query pattern:

```
SELECT o.id, o.amount
FROM orders o, products p
WHERE p.id = o.product_id
  AND o.amount < (
    SELECT 0.2 * avg(o2.amount)
    FROM orders o2
    WHERE o2.product_id = p.id
  );
```

The transformation is a plan-level rewrite that changes only the execution plan, not the query results.

**Note**  
Subquery window transformation is available in Aurora PostgreSQL beginning with version 18.6, while Babelfish for Aurora PostgreSQL supports this feature from 6.2.0 onwards. For Babelfish for Aurora PostgreSQL, the feature is controlled by the `babelfishpg_tsql.apg_enable_subquery_to_window_transform` parameter, which is turned `ON` by default.

### When to use subquery window transformation
<a name="apg-corsub-window-transform-when"></a>

Consider enabling this transformation if you have queries that match the self-correlation pattern: an outer row compared against an aggregate computed over the same table with a correlation condition.

This transformation is complementary to the existing correlated subquery transformation, which rewrites correlated subqueries as outer joins. The subquery window transformation rewrites them as window functions instead. The two transformations cover different patterns:
+ The correlated subquery transformation applies to subqueries in both the SELECT list and the WHERE clause. The subquery must return an aggregate function such as `avg(x)` or `count(*)`, without any surrounding expression.
+ The subquery window transformation applies only to WHERE-clause subqueries that use the self-correlation pattern, where the subquery's table also appears in the outer FROM. It additionally supports cases where the aggregate is combined with a constant factor (for example, `0.2 * avg(o2.amount)`) that the correlated subquery transformation can't handle.

You can enable both transformations at the same time. When a query qualifies for both, the subquery window transformation is applied; when it qualifies for only one, that transformation is applied.

### Enabling subquery window transformation
<a name="apg-corsub-window-transform-enable"></a>

To enable the transformation of correlated aggregate subqueries into window functions, set the `apg_enable_subquery_to_window_transform` parameter to `ON`. The default value of this parameter is `OFF`.

You can modify the cluster or instance parameter group to set the parameters. To learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).

Alternatively, you can configure the setting for just the current session by the following command:

```
SET apg_enable_subquery_to_window_transform TO ON;
```

To disable the transformation, set the parameter to `OFF` using the same methods. Changes take effect without an instance reboot; session-level SET is immediate, and parameter-group changes apply to new connections.

**Note**  
For Babelfish for Aurora PostgreSQL, only `babelfishpg_tsql.apg_enable_subquery_to_window_transform` controls whether the transformation applies. The `apg_enable_subquery_to_window_transform` parameter has no effect under the T-SQL dialect.

### Verifying the transformation
<a name="apg-corsub-window-transform-verify"></a>

Use the EXPLAIN command to verify if the correlated subquery has been transformed into a window function in the query plan.

When the transformation is enabled, the query plan contains a `WindowAgg` node instead of a `SubPlan` node. For example:

```
postgres=> SET apg_enable_subquery_to_window_transform TO ON;
SET
postgres=> EXPLAIN (COSTS FALSE)
SELECT o.id, o.amount
FROM orders o, products p
WHERE p.id = o.product_id
  AND o.amount < (
    SELECT 0.2 * avg(o2.amount)
    FROM orders o2
    WHERE o2.product_id = p.id
  );

                      QUERY PLAN
------------------------------------------------------
 Subquery Scan on _sw
   Filter: (_sw.amount < (0.2 * _sw._w_agg_result))
   ->  WindowAgg
         Window: w1 AS (PARTITION BY o.product_id)
         ->  Sort
               Sort Key: o.product_id
               ->  Hash Join
                     Hash Cond: (o.product_id = p.id)
                     ->  Seq Scan on orders o
                     ->  Hash
                           ->  Seq Scan on products p
```

The same query is not transformed when the GUC parameter is turned `OFF`. The plan will not have a `WindowAgg` node but a `SubPlan` instead.

```
postgres=> SET apg_enable_subquery_to_window_transform TO OFF;
SET
postgres=> EXPLAIN (COSTS FALSE)
SELECT o.id, o.amount
FROM orders o, products p
WHERE p.id = o.product_id
  AND o.amount < (
    SELECT 0.2 * avg(o2.amount)
    FROM orders o2
    WHERE o2.product_id = p.id
  );

                 QUERY PLAN
---------------------------------------------
 Hash Join
   Hash Cond: (o.product_id = p.id)
   Join Filter: (o.amount < (SubPlan 1))
   ->  Seq Scan on orders o
   ->  Hash
         ->  Seq Scan on products p
   SubPlan 1
     ->  Aggregate
           ->  Seq Scan on orders o2
                 Filter: (product_id = p.id)
```

**Note**  
For Babelfish for Aurora PostgreSQL, use the following commands to verify the transformation.  
To turn the transformation on or off within a session:  

```
SELECT set_config('babelfishpg_tsql.apg_enable_subquery_to_window_transform', 'true', false);
SELECT set_config('babelfishpg_tsql.apg_enable_subquery_to_window_transform', 'false', false);
```
To view the query plan:  

```
SET BABELFISH_SHOWPLAN_ALL ON
-- run your query
SET BABELFISH_SHOWPLAN_ALL OFF
```

### Limitations
<a name="apg-corsub-window-transform-limitations"></a>

If a query doesn't meet these conditions, it runs with its original plan; no error is raised.
+ The transformation applies only to a scalar subquery in the outer query's WHERE clause. Subqueries in the SELECT list, and subqueries nested inside an OR condition, aren't transformed. AND with other predicates is supported.
+ The subquery's FROM clause must reference exactly one table, and that same table must appear exactly once in the outer query's FROM clause. References through a view or CTE don't count as the same table.
+ The outer query must use only inner joins throughout. Outer joins, LATERAL references, CTEs, window functions, and grouping sets (CUBE, ROLLUP, GROUPING SETS) anywhere in the outer query disqualify it.
+ The subquery target must be a supported built-in aggregate (SUM, COUNT, AVG, MIN, or MAX), optionally combined with literal constants (for example, `0.2 * avg(o2.amount)`). Ordered-set and user-defined aggregates such as ARRAY\_AGG, STRING\_AGG, JSON\_AGG, and PERCENTILE\_CONT aren't supported.
+ The correlated predicate must be a plain equality (=) between simple column references on both sides. Compound keys (multiple ANDed equalities) are allowed as long as every outer-side column belongs to the same outer table. Additional non-correlated predicates on the subquery table may be combined with AND.
+ The subquery can't contain a GROUP BY, HAVING, LIMIT, ORDER BY, DISTINCT, or FOR UPDATE clause; set operations (UNION, INTERSECT, EXCEPT); set-returning functions; window functions; CTEs; nested subqueries; or volatile functions such as `random()` or `clock_timestamp()`.
+ The join between the correlated table and any other outer table must be on a column with a primary-key or unique constraint, so that at most one row from the other outer table matches each row from the correlated table.

**Note**  
The performance impact of the transformation varies depending on your schema, data, and workload. Correlated subquery execution with window function transformation can significantly improve performance as the number of rows produced by the outer query increases. We strongly recommend that you test this feature in a non-production environment with your actual schema, data, and workload before enabling it in a production environment.