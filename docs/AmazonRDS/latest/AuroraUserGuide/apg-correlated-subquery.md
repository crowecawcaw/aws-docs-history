# Optimizing correlated subqueries in

Aurora PostgreSQL

A correlated subquery references table columns from the outer query. It is evaluated once
for every row returned by the outer query. In the following example, the subquery references
a column from table ot. This table is not included in the subquery’s FROM clause, but it is
referenced in the outer query’s FROM clause. If table ot has 1 million rows, the subquery
needs to be evaluated 1 million times.

```
SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);

```

###### Note

- Subquery transformation and subquery cache are available in Aurora PostgreSQL beginning
  with version 16.8, while Babelfish for Aurora PostgreSQL supports these features from 4.2.0.
- Starting with Babelfish for Aurora PostgreSQL versions 4.6.0 and 5.2.0, the following parameters control these features:

      + babelfishpg\_tsql.apg\_enable\_correlated\_scalar\_transform
      + babelfishpg\_tsql.apg\_enable\_subquery\_cache

  By default, both parameters are turned on.

## Improving Aurora PostgreSQL query performance using

subquery transformation

Aurora PostgreSQL can accelerate correlated subqueries by transforming them into
equivalent outer joins. This optimization applies to the following two types of
correlated subqueries:

- Subqueries that return a single aggregate value and appear in the SELECT
  list.

```
SELECT ot.a, ot.b, (SELECT AVG(it.b) FROM it WHERE it.a = ot.a) FROM ot;
```

- Subqueries that return a single aggregate value and appear in a WHERE
  clause.

```
SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
```

### Enabling transformation in the

subquery

To enable the transformation of correlated subqueries into equivalent outer
joins, set the `apg_enable_correlated_scalar_transform` parameter to
`ON`. The default value of this parameter is
`OFF`.

You can modify the cluster or instance parameter group to set the parameters. To
learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Alternatively, you can configure the setting for just the current session by the
following command:

```
SET apg_enable_correlated_scalar_transform TO ON;
```

### Verifying the transformation

Use the EXPLAIN command to verify if the correlated subquery has been transformed
into an outer join in the query plan.

When the transformation is enabled, the applicable correlated subquery part will
be transformed into outer join. For example:

```
postgres=> CREATE TABLE ot (a INT, b INT);
CREATE TABLE
postgres=> CREATE TABLE it (a INT, b INT);
CREATE TABLE

postgres=> SET apg_enable_correlated_scalar_transform TO ON;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
`QUERY PLAN
--------------------------------------------------------------
 Hash Join
 Hash Cond: (ot.a = apg_scalar_subquery.scalar_output)
 Join Filter: ((ot.b)::numeric < apg_scalar_subquery.avg)
 -> Seq Scan on ot
 -> Hash
 -> Subquery Scan on apg_scalar_subquery
 -> HashAggregate
 Group Key: it.a
 -> Seq Scan on it`
```

The same query is not transformed when the GUC parameter is turned
`OFF`. The plan will not have outer join but subplan instead.

```
postgres=> SET apg_enable_correlated_scalar_transform TO OFF;
SET
postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT AVG(it.b) FROM it WHERE it.a = ot.a);
                `QUERY PLAN
----------------------------------------
 Seq Scan on ot
 Filter: ((b)::numeric < (SubPlan 1))
 SubPlan 1
 -> Aggregate
 -> Seq Scan on it
 Filter: (a = ot.a)`
```

### Limitations

- The subquery must be in the SELECT list or in one of the conditions in the
  where clause. Otherwise, it won’t be transformed.
- The subquery must return an aggregate function. User-defined aggregate
  functions aren't supported for transformation.
- A subquery whose return expression isn't a simple aggregate function won't
  be transformed.
- The correlated condition in subquery WHERE clauses should be a simple
  column reference. Otherwise, it won’t be transformed.
- The correlated condition in subquery where clauses must be a plain
  equality predicate.
- The subquery can't contain either a HAVING or a GROUP BY clause.
- The where clause in the subquery may contain one or more predicates
  combined with AND.

###### Note

The performance impact of transformation varies depending on your schema,
data, and workload. Correlated subquery execution with transformation can
significantly improve performance as the number of rows produced by the outer
query increases. We strongly recommend that you test this feature in a
non-production environment with your actual schema, data, and workload before
enabling it in a production environment.

## Using subquery cache to improve Aurora PostgreSQL query

performance

Aurora PostgreSQL supports subquery cache to store the results of correlated subqueries. This
feature skips repeated correlated subquery executions when subquery results are already in
the cache.

### Understanding subquery cache

PostgreSQL’s Memoize node is the key part of subquery cache. The Memoize node
maintains a hash table in local cache to map from input parameter values to query result
rows. The memory limit for the hash table is the product of work_mem and
hash_mem_multiplier. To learn more, see [Resource
Consumption](https://www.postgresql.org/docs/16/runtime-config-resource.html "https://www.postgresql.org/docs/16/runtime-config-resource.html").

During query execution, subquery cache uses Cache Hit Rate (CHR) to estimate whether
the cache is improving query performance and to decide at query runtime whether to
continue using the cache. CHR is the ratio of the number of cache hits to the total
number of requests. For example, if a correlated subquery needs to be executed 100
times, and 70 of those execution results can be retrieved from the cache, the CHR is
0.7.

For every apg_subquery_cache_check_interval number of cache misses, the benefit of
subquery cache is evaluated by checking whether the CHR is larger than
apg_subquery_cache_hit_rate_threshold. If not, the cache will be deleted from memory,
and the query execution will return to the original, uncached subquery re-execution.

### Parameters that control subquery cache

behavior

The following table lists the parameters that control the behavior of the subquery
cache.

| Parameter                             | Description                                                                         | Default | Allowed      |
| ------------------------------------- | ----------------------------------------------------------------------------------- | ------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apg_enable_subquery_cache             | Enables the use of cache for correlated scalar subqueries.                          | OFF     | ON, OFF      |
| apg_subquery_cache_check_interval     | Sets the frequency, in number of cache misses, to evaluate subquery cache hit rate. | 500     | 0–2147483647 |
| apg_subquery_cache_hit_rate_threshold | Sets the threshold for subquery cache hit rate.                                     | 0.3     | 0.0–1.0      | ###### Note <br>• Larger values of `apg_subquery_cache_check_interval` may improve the accuracy of the CHR-based cache benefit estimation, but will increase the cache overhead, since CHR won’t get evaluated until the cache table has `apg_subquery_cache_check_interval` rows. <br>• Larger values of `apg_subquery_cache_hit_rate_threshold` bias towards abandoning subquery cache and returning back to the original, uncached subquery re-execution. You can modify the cluster or instance parameter group to set the parameters. To learn more, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). Alternatively, you can configure the setting for just the current session by the following command: `SET apg_enable_subquery_cache TO ON;` ### Turning on subquery cache in Aurora PostgreSQL When subquery cache is enabled, Aurora PostgreSQL applies cache to save subquery results. The query plan will then have a Memoize node under SubPlan. For example, the following command sequence shows the estimated query execution plan of a simple correlated subquery without subquery cache. `` postgres=> SET apg_enable_subquery_cache TO OFF; SET postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a); `QUERY PLAN ------------------------------------ Seq Scan on ot Filter: (b < (SubPlan 1)) SubPlan 1 -> Seq Scan on it Filter: (a = ot.a)` `` After turning on `apg_enable_subquery_cache`, the query plan will contain a Memoize node under the SubPlan node, indicating that the subquery is planning to use cache. `` postgres=> SET apg_enable_subquery_cache TO ON; SET postgres=> EXPLAIN (COSTS FALSE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a); `QUERY PLAN ------------------------------------ Seq Scan on ot Filter: (b < (SubPlan 1)) SubPlan 1 -> Memoize Cache Key: ot.a Cache Mode: binary -> Seq Scan on it Filter: (a = ot.a)` `` The actual query execution plan contains more details of the subquery cache, including cache hits and cache misses. The following output shows the actual query execution plan of the above example query after inserting some values to the tables. `` postgres=> EXPLAIN (COSTS FALSE, TIMING FALSE, ANALYZE TRUE) SELECT ot.a, ot.b FROM ot WHERE ot.b < (SELECT it.b FROM it WHERE it.a = ot.a); `QUERY PLAN ----------------------------------------------------------------------------- Seq Scan on ot (actual rows=2 loops=1) Filter: (b < (SubPlan 1)) Rows Removed by Filter: 8 SubPlan 1 -> Memoize (actual rows=0 loops=10) Cache Key: ot.a Cache Mode: binary Hits: 4 Misses: 6 Evictions: 0 Overflows: 0 Memory Usage: 1kB -> Seq Scan on it (actual rows=0 loops=6) Filter: (a = ot.a) Rows Removed by Filter: 4` `` The total cache hit number is 4, and the total cache miss number is 6. If the total number of hits and misses is less than the number of loops in the Memoize node, it means that the CHR evaluation did not pass and the cache was cleaned up and abandoned at some point. The subquery execution then returned back to the original uncached re-execution. ### Limitations Subquery cache does not support certain patterns of correlated subqueries. Those types of queries will be run without cache, even if subquery cache is turned on: <br>• IN/EXISTS/ANY/ALL correlated subqueries <br>• Correlated subqueries containing nondeterministic functions. <br>• Correlated subqueries that reference outer table columns with datatypes that don't support hashing or equality operations. |
