# Optimize CloudTrail Lake queries

This page provides guidance about how to optimize CloudTrail Lake queries to improve
performance and reliability. It covers specific optimization techniques as well as
workarounds for common query failures.

###### Topics

- [Recommendations for optimizing queries](#lake-queries-tuning "#lake-queries-tuning")
- [Workarounds for query failures](#lake-queries-troubleshooting "#lake-queries-troubleshooting")

## Recommendations for optimizing queries

Follow the recommendations in this section to optimize your queries.

###### Recommendations:

- [Optimize aggregations](#query-optimization-aggregation "#query-optimization-aggregation")
- [Use approximation
  techniques](#query-optimization-approximation "#query-optimization-approximation")
- [Limit query results](#query-optimization-limit "#query-optimization-limit")
- [Optimize LIKE queries](#query-optimization-like "#query-optimization-like")
- [Use UNION ALL instead of
  UNION](#query-optimization-union "#query-optimization-union")
- [Include only required
  columns](#query-optimization-reqcolumns "#query-optimization-reqcolumns")
- [Reduce window function scope](#query-optimization-windows "#query-optimization-windows")

### Optimize aggregations

Excluding redundant columns in `GROUP BY` clauses can improve
performance as fewer columns require less memory. For example, in the following
query, we can use the `arbitrary` function on a redundant column like
`eventType` to improve the performance. The `arbitrary`
function on `eventType` is used to pick the field value randomly from the
group as the value is the same and doesn't need to be included in the `GROUP
 BY` clause.

```
SELECT eventName, eventSource, arbitrary(eventType), count(*)
FROM $EDS_ID
GROUP BY eventName, eventSource
```

It's possible to improve the performance of the `GROUP BY` function by
ordering the list of fields within the `GROUP BY` in decreasing order of
their unique value count (cardinality). For example, while getting the number of
events of a type in each AWS Region, performance can be improved by using the
`eventName`, `awsRegion` order in the `GROUP
 BY` function instead of `awsRegion`, `eventName` as
there are more unique values of `eventName` than there are of
`awsRegion`.

```
SELECT eventName, awsRegion, count(*)
FROM $EDS_ID
GROUP BY eventName, awsRegion
```

### Use approximation

techniques

Whenever exact values are not needed for counting distinct values, use [approximate aggregate functions](https://trino.io/docs/current/functions/aggregate.html#approximate-aggregate-functions "https://trino.io/docs/current/functions/aggregate.html#approximate-aggregate-functions") to find the most frequent values. For
example, [`approx_distinct`](https://trino.io/docs/current/functions/aggregate.html#approx_distinct "https://trino.io/docs/current/functions/aggregate.html#approx_distinct") uses much less memory and runs faster
than the `COUNT(DISTINCT fieldName)` operation.

### Limit query results

If only a sample response is needed for a query, restrict the results to a small
number of rows by using the `LIMIT` condition. Otherwise, the query will
return large results and take more time for query execution.

Using `LIMIT` along with `ORDER BY` can provide results for
the top or bottom N records faster as it reduces the amount of memory needed and
time taken to sort.

```
SELECT * FROM $EDS_ID
ORDER BY eventTime
LIMIT 100;
```

### Optimize LIKE queries

You can use `LIKE` to find matching strings, but with long strings,
this is compute intensive. The [`regexp_like`](https://trino.io/docs/current/functions/regexp.html#regexp_like "https://trino.io/docs/current/functions/regexp.html#regexp_like") function is in most cases a faster
alternative.

Often, you can optimize a search by anchoring the substring that you're looking
for. For example, if you're looking for a prefix, it's better to use
'`substr`%' instead of '%`substr`%' with the
`LIKE` operator and '^`substr`' with the
`regexp_like` function.

### Use `UNION ALL` instead of

`UNION`

`UNION ALL` and `UNION` are two ways to combine the results
of two queries into one result but `UNION` removes duplicates.
`UNION` needs to process all the records and find the duplicates,
which is memory and compute intensive, but `UNION ALL` is a relatively
quick operation. Unless you need to deduplicate records, use `UNION ALL`
for the best performance.

### Include only required

columns

If you don't need a column, don't include it in your query. The less data a query
has to process, the faster it will run. If you have queries that do `SELECT
 *` in the outermost query, you should change the `*` to a list
of columns that you need.

The `ORDER BY` clause returns the results of a query in sorted order.
When sorting larger amount of data, if required memory is not available,
intermediate sorted results are written to disk which can slow down query execution.
If you don't strictly need your result to be sorted, avoid adding an `ORDER
 BY` clause. Also, avoid adding `ORDER BY` to inner queries if
it is not strictly necessary.

### Reduce window function scope

[Window
functions](https://trino.io/docs/current/functions/window.html "https://trino.io/docs/current/functions/window.html") keep all the records that they operate on in memory in order
to calculate their result. When the window is very large, the window function can
run out of memory. To make sure that queries run within the available memory limits,
reduce the size of the windows that your window functions operate over by adding a
`PARTITION BY` clause.

Sometimes queries with window functions can be rewritten without window functions.
For example, instead of using `row_number` or `rank`, you can
use aggregate functions like [`max_by`](https://trino.io/docs/current/functions/aggregate.html#max_by "https://trino.io/docs/current/functions/aggregate.html#max_by") or [`min_by`](https://trino.io/docs/current/functions/aggregate.html#min_by "https://trino.io/docs/current/functions/aggregate.html#min_by").

The following query finds the alias most recently assigned to each KMS key using
`max_by`.

```
SELECT element_at(requestParameters, 'targetKeyId') as keyId,
max_by(element_at(requestParameters, 'aliasName'), eventTime) as mostRecentAlias
FROM $EDS_ID
WHERE eventsource = 'kms.amazonaws.com'
AND eventName in ('CreateAlias', 'UpdateAlias')
AND eventTime > DATE_ADD('week', -1, CURRENT_TIMESTAMP)
GROUP BY element_at(requestParameters, 'targetKeyId')
```

In this case, the `max_by` function returns the alias for the record
with the latest event time within the group. This query runs faster and uses less
memory than an equivalent query with a window function.

## Workarounds for query failures

This section provides workarounds for common query failures.

###### Query failures:

- [Query fails because response is too large](#large-responses "#large-responses")
- [Query fails due to resource exhaustion](#exhausted-resources "#exhausted-resources")

### Query fails because response is too large

A query can fail if the response is too large resulting in the message
`**Query response is too large**`.
If this occurs, you can reduce the aggregation scope.

Aggregation functions like `array_agg` can cause at least one row in
the query response to be very large causing the query to fail. For example, using
`array_agg(eventName)` instead of `array_agg(DISTINCT
 eventName)` will increase the response size a lot due to duplicated event
names from the selected CloudTrail events.

### Query fails due to resource exhaustion

If sufficient memory is not available during the execution of memory intensive
operations like joins, aggregations and window functions, intermediate results are
spilled to disk, but spilling slows query execution and can be insufficient to
prevent the query from failing with `**Query exhausted
 resources at this scale factor**`. This can be fixed by
retrying the query.

If the above errors persist even after optimizing the query, you can scope down
the query using the `eventTime` of the events and execute the query
multiple times in smaller intervals of the original query time range.
