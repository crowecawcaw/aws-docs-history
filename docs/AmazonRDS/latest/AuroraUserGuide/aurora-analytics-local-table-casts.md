

# Joining foreign tables with local tables
<a name="aurora-analytics-local-table-casts"></a>

A *local table* is a regular Aurora PostgreSQL table or materialized view stored in Aurora storage. A *local column* is a column in a local table.

A query that joins a foreign table with a local table performs better with full pushdown than with table-scan pushdown. A local column with an unsupported data type or collation forces the query to fall back to table-scan pushdown.

Instead of changing the column definition, which rewrites the table, add a cast or `COLLATE` clause to the column in your query. To find the blocking columns, check "Unsupported Pushdown Expressions" in the `EXPLAIN VERBOSE` output. For more information, see [Using EXPLAIN VERBOSE to see Pushdown SQL](aurora-analytics-execution-plan.md#aurora-analytics-explain-verbose).

In the following example, `heap_table` has a `character(1)` column and the database default collation is `en_US.UTF-8`. The analytics engine supports neither, so only the foreign table scan is pushed down.

```
postgres=> \d heap_table
               Table "public.heap_table"
 Column |     Type     | Collation | Nullable | Default
--------+--------------+-----------+----------+---------
 col1   | character(1) |           |          |

postgres=> EXPLAIN (VERBOSE, COSTS OFF) SELECT col1 FROM heap_table WHERE EXISTS (SELECT * FROM ft_a);
                                                                 QUERY PLAN
---------------------------------------------------------------------------------------------------------------------------------------------
 Result
   Output: heap_table.col1
   One-Time Filter: (InitPlan 1).col1
   InitPlan 1
     ->  Custom Scan on public.ft_a
           Pushdown SQL: SELECT id FROM (SELECT id::INTEGER AS id FROM system.main.read_parquet($aurora_analytics_parameter_1) AS ft_a) ft_a
           ->  READ_PARQUET
                 Table: ft_a
                 Projections: id
   ->  Seq Scan on public.heap_table
         Output: heap_table.col1
 Query Identifier: -5916225740472533963
 Unsupported Pushdown Expressions:
 1: Collation
    Description: default
 2: Type
    Description: character(1)
```

With `col1::text COLLATE "C"`, the whole query is pushed down.

```
postgres=> EXPLAIN (COSTS OFF) SELECT col1::text COLLATE "C" FROM heap_table WHERE EXISTS (SELECT * FROM ft_a);
                  QUERY PLAN
----------------------------------------------
 Custom Scan
   ->  CROSS_PRODUCT
         ->  POSTGRES_SCAN
               Table: heap_table
         ->  FILTER
               Expression: (#0 = 1)
               ->  UNGROUPED_AGGREGATE
                     Aggregates: count_star()
                     ->  STREAMING_LIMIT
                           ->  READ_PARQUET
                                 Table: ft_a
```

The following table lists the casts and collations for local columns. Apply them wherever the column appears, including `WHERE`, `GROUP BY`, `ORDER BY`, and join conditions.


| Local column type or collation | Cast or collation to use | Example | 
| --- | --- | --- | 
| CHAR(n), VARCHAR(n) | TEXT or VARCHAR without a length | col::text | 
| TIMESTAMP(p), TIMESTAMPTZ(p), TIME(p), TIMETZ(p), INTERVAL(p) with p less than 6 | Same type without a precision, or with precision 6 | col::timestamp | 
| BIT(n), VARBIT(n) | VARBIT without a length | col::varbit | 
| JSONB | JSON | col::json | 
| libc collation, such as en\_US or a libc database default | COLLATE "C" or a predefined ICU collation such as "en-US-x-icu". When you also cast the column, put the collation after the cast. | col::text COLLATE "C" | 

No cast enables full pushdown for `NUMERIC` columns without a precision and scale or with a precision greater than 38, or for types such as `MONEY`, `INET`, `ENUM`, and `XML`. For the types that support pushdown, see [aurora\_analytics\_available\_features()](aurora-analytics-sql-functions-reference.md#aurora-analytics-func-available-features).

**Note**  
`COLLATE "C"` compares and sorts strings by byte value. `ORDER BY`, `min()`, `max()`, and range comparisons can return different results than under the original collation.