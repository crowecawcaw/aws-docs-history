# Optimize queries

Use the query optimization techniques described in this section to make queries run
faster or as workarounds for queries that exceed resource limits in Athena.

## Optimize joins

There are many different strategies for executing joins in a distributed query
engine. Two of the most common are distributed hash joins and queries with complex
join conditions.

### In a distributed hash join, place large tables on the left, small tables on the right

The most common type of join uses an equality comparison as the join
condition. Athena runs this type of join as a distributed hash join.

In a distributed hash join, the engine builds a lookup table (hash table) from
one of the sides of the join. This side is called the _build
side_. The records of the build side are distributed across the
nodes. Each node builds a lookup table for its subset. The other side of the
join, called the _probe side_, is then streamed through the
nodes. The records from the probe side are distributed over the nodes in the
same way as the build side. This enables each node to perform the join by
looking up the matching records in its own lookup table.

When the lookup tables created from the build side of the join don't fit into
memory, queries can fail. Even if the total size of the build side is less than
the available memory, queries can fail if the distribution of the records has
significant skew. In an extreme case, all records could have the same value for
the join condition and have to fit into memory on a single node. Even a query
with less skew can fail if a set of values gets sent to the same node and the
values add up to more than the available memory. Nodes do have the ability to
spill records to disk, but spilling slows query execution and can be
insufficient to prevent the query from failing.

Athena attempts to reorder joins to use the larger relation as the probe side,
and the smaller relation as the build side. However, because Athena does not
manage the data in tables, it has limited information and often must assume that
the first table is the larger and the second table is the smaller.

When writing joins with equality-based join conditions, assume that the table
to the left of the `JOIN` keyword is the probe side and the table to
the right is the build side. Make sure that the right table, the build side, is
the smaller of the tables. If it is not possible to make the build side of the
join small enough to fit into memory, consider running multiple queries that
join subsets of the build table.

### Use EXPLAIN to analyze queries with complex joins

Queries with complex join conditions (for example, queries that use
`LIKE` , `>`, or other operators), are often
computationally demanding. In the worst case, every record from one side of the
join must be compared to every record on the other side of the join. Because the
execution time grows with the square of the number of records, such queries run
the risk of exceeding the maximum execution time.

To find out how Athena will execute your query in advance, you can use the
`EXPLAIN` statement. For more information, see [Using EXPLAIN and EXPLAIN ANALYZE in Athena](athena-explain-statement.md "athena-explain-statement.md") and [Understand Athena EXPLAIN statement results](athena-explain-statement-understanding.md "athena-explain-statement-understanding.md").

## Reduce the scope of window functions, or remove them

Because window functions are resource intensive operations, they can make queries
run slow or even fail with the message **`Query exhausted resources at this
 scale factor`**. Window functions keep all the records that they
operate on in memory in order to calculate their result. When the window is very
large, the window function can run out of memory.

To make sure your queries run within the available memory limits, reduce the size
of the windows that your window functions operate over. To do so, you can add a
`PARTITIONED BY` clause or narrow the scope of existing partitioning
clauses.

### Use non-window functions

Sometimes queries with window functions can be rewritten without window
functions. For example, instead of using `row_number` to find the top
`N` records, you can use `ORDER BY` and
`LIMIT`. Instead of using `row_number` or
`rank` to deduplicate records, you can use aggregate functions
like [max_by](https://trino.io/docs/current/functions/aggregate.html#max_by "https://trino.io/docs/current/functions/aggregate.html#max_by"), [min_by](https://trino.io/docs/current/functions/aggregate.html#min_by "https://trino.io/docs/current/functions/aggregate.html#min_by"), and [arbitrary](https://trino.io/docs/current/functions/aggregate.html#arbitrary "https://trino.io/docs/current/functions/aggregate.html#arbitrary").

For example, suppose you have a dataset with updates from a sensor. The sensor
periodically reports its battery status and includes some metadata like
location. If you want to know the last battery status for each sensor and its
location, you can use this query:

```
SELECT sensor_id,
       arbitrary(location) AS location,
       max_by(battery_status, updated_at) AS battery_status
FROM sensor_readings
GROUP BY sensor_id
```

Because metadata like location is the same for every record, you can use the
`arbitrary` function to pick any value from the group.

To get the last battery status, you can use the `max_by` function.
The `max_by` function picks the value for a column from the record
where the maximum value of another column was found. In this case, it returns
the battery status for the record with the last update time within the group.
This query runs faster and uses less memory than an equivalent query with a
window function.

## Optimize aggregations

When Athena performs an aggregation, it distributes the records across worker nodes
using the columns in the `GROUP BY` clause. To make the task of matching
records to groups as efficient as possible, the nodes attempt to keep records in
memory but spill them to disk if necessary.

It is also a good idea to avoid including redundant columns in `GROUP
 BY` clauses. Because fewer columns require less memory, a query that
describes a group using fewer columns is more efficient. Numeric columns also use
less memory than strings. For example, when you aggregate a dataset that has both a
numeric category ID and a category name, use only the category ID column in the
`GROUP BY` clause.

Sometimes queries include columns in the `GROUP BY` clause to work
around the fact that a column must either be part of the `GROUP BY`
clause or an aggregate expression. If this rule is not followed, you can receive an
error message like the following:

**`EXPRESSION_NOT_AGGREGATE: line 1:8: 'category' must be an aggregate
 expression or appear in GROUP BY clause`**

To avoid having to add a redundant columns to the `GROUP BY` clause,
you can use the [arbitrary](https://trino.io/docs/current/functions/aggregate.html#arbitrary "https://trino.io/docs/current/functions/aggregate.html#arbitrary") function, as in the following example.

```
SELECT country_id,
       arbitrary(country_name) AS country_name,
       COUNT(*) AS city_count
FROM world_cities
GROUP BY country_id
```

The `ARBITRARY` function returns an arbitrary value from the group. The
function is useful when you know all records in the group have the same value for a
column, but the value does not identify the group.

## Optimize top N queries

The `ORDER BY` clause returns the results of a query in sorted order.
Athena uses distributed sort to run the sort operation in parallel on multiple
nodes.

If you don't strictly need your result to be sorted, avoid adding an `ORDER
 BY` clause. Also, avoid adding `ORDER BY` to inner queries if
they are not strictly necessary. In many cases, the query planner can remove
redundant sorting, but this is not guaranteed. An exception to this rule is if an
inner query is doing a top `N` operation, such as finding the
`N` most recent, or `N` most common values.

When Athena sees `ORDER BY` together with `LIMIT`, it
understands that you are running a top `N` query and uses dedicated
operations accordingly.

###### Note

Although Athena can also often detect window functions like
`row_number` that use top `N`, we recommend the
simpler version that uses `ORDER BY` and `LIMIT`. For more
information, see [Reduce the scope of window functions, or remove them](#performance-tuning-optimizing-window-functions "#performance-tuning-optimizing-window-functions").

## Include only required columns

If you don't strictly need a column, don't include it in your query. The less data
a query has to process, the faster it will run. This reduces both the amount of
memory required and the amount of data that has to be sent between nodes. If you are
using a columnar file format, reducing the number columns also reduces the amount of
data that is read from Amazon S3.

Athena has no specific limit on the number of columns in a result, but how queries
are executed limits the possible combined size of columns. The combined size of
columns includes their names and types.

For example, the following error is caused by a relation that exceeds the size
limit for a relation descriptor:

**`GENERIC_INTERNAL_ERROR:
 io.airlift.bytecode.CompilationException`**

To work around this issue, reduce the number of columns in the query, or create
subqueries and use a `JOIN` that retrieves a smaller amount of data. If
you have queries that do `SELECT *` in the outermost query, you should
change the `*` to a list of only the columns that you need.

## Optimize queries by using approximations

Athena has support for [approximation
aggregate functions](https://trino.io/docs/current/functions/aggregate.html#appro "https://trino.io/docs/current/functions/aggregate.html#appro") for counting distinct values, the most frequent
values, percentiles (including approximate medians), and creating histograms. Use
these functions whenever exact values are not needed.

Unlike `COUNT(DISTINCT col)` operations, [approx_distinct](https://trino.io/docs/current/functions/aggregate.html#approx_distinct "https://trino.io/docs/current/functions/aggregate.html#approx_distinct") uses much less memory and runs faster. Similarly, using
[numeric_histogram](https://trino.io/docs/current/functions/aggregate.html#numeric_histogram "https://trino.io/docs/current/functions/aggregate.html#numeric_histogram") instead of [histogram](https://trino.io/docs/current/functions/aggregate.html#histogram "https://trino.io/docs/current/functions/aggregate.html#histogram") uses approximate methods and therefore less memory.

## Optimize LIKE

You can use `LIKE` to find matching strings, but with long strings,
this is compute intensive. The [regexp_like](https://trino.io/docs/current/functions/regexp.html#regexp_like "https://trino.io/docs/current/functions/regexp.html#regexp_like") function is in most cases a faster alternative, and also
provides more flexibility.

Often you can optimize a search by anchoring the substring that you are looking
for. For example, if you're looking for a prefix, it is much better to use
'`substr`%' instead of
'%`substr`%'. Or, if you're using
`regexp_like`, '^`substr`'.

## Use UNION ALL instead of UNION

`UNION ALL` and `UNION` are two ways to combine the results of
two queries into one result. `UNION ALL` concatenates the records from
the first query with the second, and `UNION` does the same, but also
removes duplicates. `UNION` needs to process all the records and find the
duplicates, which is memory and compute intensive, but `UNION ALL` is a
relatively quick operation. Unless you need to deduplicate records, use `UNION
 ALL` for the best performance.

## Use UNLOAD for large result sets

When the results of a query are expected to be large (for example, tens of
thousands of rows or more), use UNLOAD to export the results. In most cases, this is
faster than running a regular query, and using `UNLOAD` also gives you
more control over the output.

When a query finishes executing, Athena stores the result as a single uncompressed
CSV file on Amazon S3. This takes longer than `UNLOAD`, not only because the
result is uncompressed, but also because the operation cannot be parallelized. In
contrast, `UNLOAD` writes results directly from the worker nodes and
makes full use of the parallelism of the compute cluster. In addition, you can
configure `UNLOAD` to write the results in compressed format and in other
file formats such as JSON and Parquet.

For more information, see [UNLOAD](unload.md "unload.md").

## Use CTAS or Glue ETL to materialize frequently used aggregations

'Materializing' a query is a way of accelerating query performance by storing
pre-computed complex query results (for example, aggregations and joins) for reuse
in subsequent queries.

If many of your queries include the same joins and aggregations, you can
materialize the common subquery as a new table and then run queries against that
table. You can create the new table with [Create a table from query results (CTAS)](ctas.md "ctas.md"), or a dedicated ETL tool like [Glue
ETL](https://aws.amazon.com/glue "https://aws.amazon.com/glue").

For example, suppose you have a dashboard with widgets that show different aspects
of an orders dataset. Each widget has its own query, but the queries all share the
same joins and filters. An order table is joined with a line items table, and there
is a filter to show only the last three months. If you identify the common features
of these queries, you can create a new table that the widgets can use. This reduces
duplication and improves performance. The disadvantage is that you must keep the new
table up to date.

## Reuse query results

It's common for the same query to run multiple times within a short duration. For
example, this can occur when multiple people open the same data dashboard. When you
run a query, you can tell Athena to reuse previously calculated results. You specify
the maximum age of the results to be reused. If the same query was previously run
within that time frame, Athena returns those results instead of running the query
again. For more information, see [Reuse query results in Athena](reusing-query-results.md "reusing-query-results.md") here in the
_Amazon Athena User Guide_ and [Reduce cost and improve query performance with Amazon Athena Query Result
Reuse](https://aws.amazon.com/blogs/big-data/reduce-cost-and-improve-query-performance-with-amazon-athena-query-result-reuse/ "https://aws.amazon.com/blogs/big-data/reduce-cost-and-improve-query-performance-with-amazon-athena-query-result-reuse/") in the _AWS Big Data Blog_.
