# Building for efficiency with functions

User-defined functions are not single-shard optimized by default, but they can be configured to execute as single-shard operations. Functions can encapsulate logic and ensure it is executed in a single-shard optimized manner.

## Why single-shard operations are important

Resource utilization is important for performance and cost efficiency. Single-shard operations use significantly fewer resources compared to cross-shard operations. For example, when executing a function to insert one million rows, single-shard execution uses approximately 90.5 ACUs compared to 126.5 ACUs for cross-shard execution—a 35% improvement in resource efficiency.

Single-shard execution also provides:

- 35% higher throughput than cross-shard operations
- More predictable response times
- Better scalability as data grows

## Single-shard operations and functions

Functions execute on shards when either of these prerequisites are met:

- The function is created as immutable and included in a single-shard optimized query
- The function is distributed by a user

Functions that execute on shards perform and scale better because they execute where the data is located.

## Functions and volatility

To check a function's volatility, use this query on PostgreSQL's system tables:

```
SELECT DISTINCT nspname, proname, provolatile
FROM pg_proc PRO
JOIN pg_namespace NSP ON PRO.pronamespace = NSP.oid
WHERE proname IN ('random', 'md5');
```

Example output:

```
  nspname   | proname | provolatile
------------+---------+-------------
 pg_catalog | md5     | i
 pg_catalog | random  | v
(2 rows)
```

In this example, `md5()` is immutable and `random()` is volatile. This means that a single-shard optimized statement that includes `md5()` remains single-shard optimized, while a statement that includes `random()` does not.

Example with immutable function:

```
EXPLAIN ANALYZE
SELECT pg_catalog.md5('123')
FROM s1.t1
WHERE col_a = 776586194
  AND col_b = 654849524
  AND col_c = '3ac2f2affb02987159ccd6ebd23e1ae5';
```

```
                          QUERY PLAN
----------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
               (actual time=3.409..3.409 rows=1 loops=1)
 Single Shard Optimized
 Planning Time: 0.313 ms
 Execution Time: 4.253 ms
(4 rows)
```

Example with volatile function:

```
EXPLAIN ANALYZE
SELECT pg_catalog.random()
FROM s1.t1
WHERE col_a = 776586194
  AND col_b = 654849524
  AND col_c = '3ac2f2affb02987159ccd6ebd23e1ae5';
```

```
                          QUERY PLAN
------------------------------------------------------
 Foreign Scan on t1_fs00001 t1
   (cost=100.00..15905.15 rows=1 width=8)
   (actual time=0.658..0.658 rows=1 loops=1)
 Planning Time: 0.263 ms
 Execution Time: 2.892 ms
(3 rows)
```

The output shows that `md5()` is pushed down and executed as single-shard optimized, while `random()` is not.

## Distributing functions

A function that accesses data on only one shard should execute on that shard to gain performance benefits. The function must be distributed, and the function signature must include the complete shard key—all columns in the shard key must be passed as parameters to the function.

Example function:

```
CREATE OR REPLACE FUNCTION s1.func1(
    param_a bigint,
    param_b bigint,
    param_c char(100)
)
RETURNS int AS $$
DECLARE
    res int;
BEGIN
    SELECT COUNT(*) INTO res
    FROM s1.t1
    WHERE s1.t1.col_a = param_a
      AND s1.t1.col_b = param_b
      AND s1.t1.col_c = param_c;

    RETURN res;
END
$$ LANGUAGE plpgsql;
```

Before distribution, the function is not single-shard optimized:

```
EXPLAIN ANALYZE
SELECT * FROM s1.func1(776586194, 654849524, '3ac2f2affb02987159ccd6ebd23e1ae5');
```

```
                                              QUERY PLAN
------------------------------------------------------------------------------------------------------
 Function Scan on func1  (cost=0.25..0.26 rows=1 width=4)
                         (actual time=37.503..37.503 rows=1 loops=1)
 Planning Time: 0.901 ms
 Execution Time: 51.647 ms
(3 rows)
```

To distribute the function:

```
SELECT rds_aurora.limitless_distribute_function(
    's1.func1(bigint,bigint,character)',
    ARRAY['param_a','param_b','param_c'],
    's1.t1'
);
```

After distribution, the function is single-shard optimized:

```
EXPLAIN ANALYZE
SELECT * FROM s1.func1(776586194, 654849524, '3ac2f2affb02987159ccd6ebd23e1ae5');
```

```
                                           QUERY PLAN
------------------------------------------------------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
               (actual time=4.332..4.333 rows=1 loops=1)
 Single Shard Optimized
 Planning Time: 0.857 ms
 Execution Time: 5.116 ms
(4 rows)
```

You can confirm single-shard optimization by checking the `sso_calls` column in `rds_aurora.limitless_stat_statements`:

```
subcluster_id | subcluster_type | calls | sso_calls |                query
--------------+-----------------+-------+-----------+--------------------------------------
 2            | router          |     2 |         1 | SELECT * FROM s1.func1( $1, $2, $3 )
 3            | router          |     1 |         1 | SELECT * FROM s1.func1( $1, $2, $3 )
(2 rows)
```

## Functions and efficiency patterns

Executing logic close to the data is more efficient, and functions play a key role in achieving this. There are two main use cases for improving efficiency with functions:

1. Extracting shard key from complex data to invoke a separate single-shard optimized function
2. Turning cross-shard workloads into single-shard optimized by separating cross-shard logic from single-shard optimized statements

### Extracting shard key from complex data

Consider a function with signature `s3.func3(p_json_doc json)` that performs several database operations. These operations will execute across all shards within a transaction that spans all shards. If the JSON document contains the shard key, you can build a single-shard optimized function to perform the database operations.

Original pattern:

```
s3.func3(p_json_doc json)
    database operation 1;
    database operation 2;
    database operation 3;
```

Optimized pattern:

```
s3.func3(p_json_doc json)
DECLARE
    v_a bigint;
BEGIN
    v_a := (p_json_doc->>'field_a')::bigint;
    SELECT s3.func3_INNER(v_a, p_json_doc);
END;
```

Where the inner function does:

```
s3.func3_INNER(p_a, p_json_doc)
    database operation 1 WHERE shard_key = p_a;
    database operation 2 WHERE shard_key = p_a;
    database operation 3 WHERE shard_key = p_a;
```

In this pattern, the shard key is encapsulated in a complex datatype or deducible from other parameters. Logic, data access, and functions can determine, extract, or construct the shard key, then invoke a single-shard optimized function that performs operations concerning only a single shard. Since the application interface doesn't change, optimization is comparatively easy to test.

### Deferring shard key from other functions or data

Another design pattern applies when logic or data access calculates or determines the shard key. This is useful when a function can be executed on a single shard for most invocations, but occasionally requires cross-shard execution.

Original pattern:

```
NEWORD(INTEGER, …) RETURNS NUMERIC
DECLARE
    all_whid_local := true;
    LOOP through the order lines
        Generate warehouse ID;
        IF generated warehouse ID == input warehouse ID
        THEN
            ol_supply_whid := input warehouse ID;
        ELSE
            all_whid_local := false;
            ol_supply_whid := generated warehouse ID;
        END IF;
        …
    END LOOP;
    …
    RETURN no_s_quantity;
```

Optimized pattern with separate functions:

```
CREATE OR REPLACE FUNCTION NEWORD_sso(no_w_id INTEGER, …)
RETURNS NUMERIC
…
    RETURN no_s_quantity;
    …
END;
LANGUAGE 'plpgsql';

SELECT rds_aurora.limitless_distribute_function(
    'NEWORD_sso(int,…)',
    ARRAY['no_w_id'],
    'warehouse'
);

CREATE OR REPLACE FUNCTION NEWORD_crosshard(no_w_id INTEGER, …)
RETURNS NUMERIC
…
    RETURN no_s_quantity;
    …
END;
LANGUAGE 'plpgsql';
```

Then have the main function call either the single-shard optimized or cross-shard version:

```
IF all_whid_local THEN
    SELECT NEWORD_sso(…) INTO no_s_quantity;
ELSE
    SELECT NEWORD_crosshard(…) INTO no_s_quantity;
END IF;
```

This approach allows the majority of invocations to benefit from single-shard optimization while maintaining correct behavior for cases that require cross-shard execution.

## Checking for single-shard operations

Use `EXPLAIN` to verify whether a statement is single-shard optimized. The output explicitly reports "Single Shard Optimized" for optimized operations.

Cross-shard invocation before distribution:

```
                       QUERY PLAN
---------------------------------------------------------------------
 Function Scan on func1  (cost=0.25..0.26 rows=1 width=4)
                         (actual time=59.622..59.623 rows=1 loops=1)
 Planning Time: 0.925 ms
 Execution Time: 60.211 ms
```

Single-shard invocation after distribution:

```
                       QUERY PLAN
----------------------------------------------------------------------
 Foreign Scan  (cost=100.00..101.00 rows=100 width=0)
               (actual time=4.576..4.577 rows=1 loops=1)
 Single Shard Optimized
 Planning Time: 1.483 ms
 Execution Time: 5.404 ms
```

The difference in execution times demonstrates the performance benefit of single-shard optimization.
