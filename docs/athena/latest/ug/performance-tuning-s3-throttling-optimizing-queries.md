# Optimize your queries

Use the suggestions in this section for optimizing your SQL queries in Athena.

## Use LIMIT with the ORDER BY clause

The `ORDER BY` clause returns data in a sorted order. This requires
Athena to send all rows of data to a single worker node and then sort the rows. This
type of query can run for a long time or even fail.

For greater efficiency in your queries, look at the top or bottom
`N` values, and then also use a `LIMIT`
clause. This significantly reduces the cost of the sort by pushing both sorting and
limiting to individual worker nodes rather than to a single worker.

## Optimize JOIN clauses

When you join two tables, Athena distributes the table on the right to worker
nodes, and then streams the table on the left to perform the join.

For this reason, specify the larger table on the left side of the join and the
smaller table on the right side of the join. This way, Athena uses less memory and
runs the query with lower latency.

Also note the following points:

- When you use multiple `JOIN` commands, specify tables from
  largest to smallest.
- Avoid cross joins unless they are required by the query.

## Optimize GROUP BY clauses

The `GROUP BY` operator distributes rows based on the `GROUP
 BY` columns to the worker nodes. These columns are referenced in memory
and the values are compared as the rows are ingested. The values are aggregated
together when the `GROUP BY` column matches. In consideration of the way
this process works, it is advisable to order the columns from the highest
cardinality to the lowest.

## Use numbers instead of strings

Because numbers require less memory and are faster to process compared to strings,
use numbers instead of strings when possible.

## Limit the number of columns

To reduce the total amount of memory required to store your data, limit the number
of columns specified in your `SELECT` statement.

## Use regular expressions instead of LIKE

Queries that include clauses such as `LIKE '%string%'` on large strings
can be very computationally intensive. When you filter for multiple values on a
string column, use the [regexp_like()](https://trino.io/docs/current/functions/regexp.html#regexp_like "https://trino.io/docs/current/functions/regexp.html#regexp_like") function and a regular expression instead. This is
particularly useful when you compare a long list of values.

## Use the LIMIT clause

Instead of selecting all columns when you run a query, use the `LIMIT`
clause to return only the columns that you require. This reduces the size of the
dataset that is processed through the query execution pipeline. `LIMIT`
clauses are more helpful when you query tables that have a large of number of
columns that are string-based. `LIMIT` clauses are also helpful when you
perform multiple joins or aggregations on any query.
