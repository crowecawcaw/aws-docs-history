# Aggregate Functions

Instead of returning a result calculated from a single row, an aggregate function returns a
result calculated from aggregated data contained in a finite set of rows, or from information
about a finite set of rows. An aggregate function may appear in any of the following:

- <selection list> portion of a [SELECT clause](sql-reference-select-clause.md "sql-reference-select-clause.md")
- [ORDER BY clause](sql-reference-order-by-clause.md "sql-reference-order-by-clause.md")
- [HAVING clause](sql-reference-having-clause.md "sql-reference-having-clause.md")
  An aggregate function is different from [Analytic Functions](sql-reference-analytic-functions.md "sql-reference-analytic-functions.md"),
  which are always evaluated relative to a window that must be specified, and so they can't appear
  in a HAVING clause. Other differences are described in the table later in this topic.

Aggregate functions operate slightly differently in aggregate queries on tables than when
you use them in aggregate queries on streams, as follows. If an aggregate query on tables
contains a GROUP BY clause, the aggregate function returns one result per group in the set of
input rows. Lacking an explicit GROUP BY clause is equivalent to GROUP BY (), and returns only
one result for the entire set of input rows.

On streams, an aggregate query must contain an explicit GROUP BY clause on a monotonic
expression based on rowtime. Without one, the sole group is the whole stream, which never ends, preventing any result from being reported. Adding a GROUP BY clause based on a monotonic
expression breaks the stream into finite sets of rows, contiguous in time, and each such set can
then be aggregated and reported.

Whenever a row arrives that changes the value of the monotonic grouping expression, a new
group is started and the previous group is considered complete. Then, the Amazon Kinesis Data Analytics application
outputs the value of the aggregate functions. Note that the GROUP BY clause may also include
other non-monotonic expressions, in which case more than one result per set of rows may be
produced.

Performing an aggregate query on streams is often referred to as streaming aggregation, as
distinct from the windowed aggregation discussed in [Analytic Functions](sql-reference-analytic-functions.md "sql-reference-analytic-functions.md")
and [Windowed Aggregation on
Streams](sql-reference-windowed-aggregation-stream.md "sql-reference-windowed-aggregation-stream.md"). For more information about
stream-to-stream joins, see [JOIN clause](sql-reference-join-clause.md "sql-reference-join-clause.md").

If an input row contains a `null` in a column used as an input to a data analysis
function, the data analysis function ignores the row (except for COUNT).

| Differences Between Aggregate and Analytic Functions                                            | Function Type                           | Outputs                                                                          | Rows or Windows Used                                                                                                                                               | Notes |
| ----------------------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| Aggregate Functions                                                                             | One output row per group of input rows. | All output columns are calculated over the same window or same group of<br>rows. | COUNT DISTINCT is not allowed in streaming aggregation. Statements of the<br>following type are not allowed:<br>SELECT COUNT(DISTINCT x) ... FROM ... GROUP BY ... |
| [Analytic Functions](sql-reference-analytic-functions.md "sql-reference-analytic-functions.md") | One output row for each input row.      | Each output column may be calculated using a different window or partition.      | COUNT DISTINCT can't be used as [Analytic Functions](sql-reference-analytic-functions.md "sql-reference-analytic-functions.md") or in windowed aggregation.        |

## Streaming Aggregation and Rowtime Bounds

Normally, an aggregate query generates a result when a row arrives that changes the value
of the monotonic expression in the GROUP BY.

For example, if the query is grouped by FLOOR(rowtime TO MINUTE), and the rowtime of the current row is 9:59.30, then a new row with a
rowtime of 10:00.00 will trigger the result.

Alternately, a rowtime bound can be used to advance the monotonic expression and enable
the query to return a result.

For example, if the query is grouped by FLOOR(rowtime TO MINUTE), and the rowtime of the current row is 9:59.30, then an incoming rowtime bound of 10:00.00
the query to return a result.

## Aggregate Function List

Amazon Kinesis Data Analytics supports the following aggregate functions:

- [AVG](sql-reference-avg.md "sql-reference-avg.md")
- [COUNT](sql-reference-count.md "sql-reference-count.md")
- [COUNT_DISTINCT_ITEMS_TUMBLING Function](count-distinct-items.md "count-distinct-items.md")
- [EXP_AVG](sql-reference-exp-avg.md "sql-reference-exp-avg.md")
- [FIRST_VALUE](sql-reference-first-value.md "sql-reference-first-value.md")
- [LAST_VALUE](sql-reference-last-value.md "sql-reference-last-value.md")
- [MAX](sql-reference-max.md "sql-reference-max.md")
- [MIN](sql-reference-min.md "sql-reference-min.md")
- [SUM](sql-reference-sum.md "sql-reference-sum.md")
- [TOP_K_ITEMS_TUMBLING Function](top-k.md "top-k.md")

The following SQL uses the AVG aggregate function as part of a query to find the average
age of all employees:

```
SELECT
    AVG(AGE) AS AVERAGE_AGE
FROM SALES.EMPS;

```

Result:

| AVERAGE_AGE |
| ----------- |
| 38          |

To find the average age of employees in each department, we can add an explicit GROUP BY
clause to the query:

```
SELECT
    DEPTNO,
    AVG(AGE) AS AVERAGE_AGE
FROM SALES.EMPS
GROUP BY DEPTNO;
```

Returns:

| DEPTNO | AVERAGE_AGE |
| ------ | ----------- |
| 10     | 30          |
| 20     | 25          |
| 30     | 40          |
| 40     | 57          |

## Examples of Aggregate Queries on Streams (Streaming Aggregation)

For this example, assume that the data in the following table is flowing through the
stream called WEATHERSTREAM.

| ROWTIME               | CITY      | TEMP |
| --------------------- | --------- | ---- |
| 2018-11-01 01:00:00.0 | Denver    | 29   |
| 2018-11-01 01:00:00.0 | Anchorage | 2    |
| 2018-11-01 06:00:00.0 | Miami     | 65   |
| 2018-11-01 07:00:00.0 | Denver    | 32   |
| 2018-11-01 09:00:00.0 | Anchorage | 9    |
| 2018-11-01 13:00:00.0 | Denver    | 50   |
| 2018-11-01 17:00:00.0 | Anchorage | 10   |
| 2018-11-01 18:00:00.0 | Miami     | 71   |
| 2018-11-01 19:00:00.0 | Denver    | 43   |
| 2018-11-02 01:00:00.0 | Anchorage | 4    |
| 2018-11-02 01:00:00.0 | Denver    | 39   |
| 2018-11-02 07:00:00.0 | Denver    | 46   |
| 2018-11-02 09:00:00.0 | Anchorage | 3    |
| 2018-11-02 13:00:00.0 | Denver    | 56   |
| 2018-11-02 17:00:00.0 | Anchorage | 2    |
| 2018-11-02 19:00:00.0 | Denver    | 50   |
| 2018-11-03 01:00:00.0 | Denver    | 36   |
| 2018-11-03 01:00:00.0 | Anchorage | 1    |

If you want to find the minimum and maximum temperature recorded anywhere each day
(globally regardless of city), the minimum and maximum temperature can be calculated using the
aggregate functions MIN and MAX respectively.

To indicate that we want this information on a per-day basis (and to provide a monotonic expression as the argument of the GROUP BY clause),

we use the FLOOR function to round each row's rowtime down to the nearest day:

```
SELECT STREAM
    
    FLOOR(WEATHERSTREAM.ROWTIME to DAY) AS FLOOR_DAY,
    MIN(TEMP) AS MIN_TEMP,
    MAX(TEMP) AS MAX_TEMP
FROM WEATHERSTREAM

GROUP BY FLOOR(WEATHERSTREAM.ROWTIME TO DAY);

```

The result of the aggregate query is shown in the following table.

| FLOOR_DAY             | MIN_TEMP | MAX_TEMP |
| --------------------- | -------- | -------- |
| 2018-11-01 00:00:00.0 | 2        | 71       |
| 2018-11-02 00:00:00.0 | 2        | 56       |

There is no row for 2018-11-03, even though the example data does include temperature
measurements on that day. This is because the rows for 2018-11-03 cannot be aggregated until
all rows for that day are known to have arrived, and that will only happen when either a row
with a rowtime of 2018-11-04 00:00:00.0 (or later) or a rowtime bound of 2018-11-04 00:00:00.0
(or later) arrives. If and when either did arrive, the next result would be as described in
the following table.

| FLOOR_DAY             | MIN_TEMP | MAX_TEMP |
| --------------------- | -------- | -------- |
| 2018-11-03 00:00:00.0 | 1        | 36       |

Let's say that instead of finding the global minimum and maximum temperatures each day, we
want to find the minimum, maximum, and average temperature for each city each day. To do this,
we use the SUM and COUNT aggregate functions to compute the average, and add CITY to the GROUP
BY clause, as shown following:

```
SELECT STREAM
    FLOOR(WEATHERSTREAM.ROWTIME TO DAY) AS FLOOR_DAY,
    
    CITY,
    MIN(TEMP) AS MIN_TEMP,
    MAX(TEMP) AS MAX_TEMP,
    SUM(TEMP)/COUNT(TEMP) AS AVG_TEMP
FROM WEATHERSTREAM
GROUP BY FLOOR(WEATHERSTREAM.ROWTIME TO DAY), CITY;


```

The result of the aggregate query is shown in the following table.

| FLOOR_DAY             | CITY      | MIN_TEMP | MAX_TEMP | AVG_TEMP |
| --------------------- | --------- | -------- | -------- | -------- |
| 2018-11-01 00:00:00.0 | Anchorage | 2        | 10       | 7        |
| 2018-11-01 00:00:00.0 | Denver    | 29       | 50       | 38       |
| 2018-11-01 00:00:00.0 | Miami     | 65       | 71       | 68       |
| 2018-11-02 00:00:00.0 | Anchorage | 2        | 4        | 3        |
| 2018-11-02 00:00:00.0 | Denver    | 39       | 56       | 47       |

In this case, the arrival of rows for a new day's temperature measurements triggers the
aggregation of the previous day's data, grouped by CITY, which then results in one row being
produced per city included in the day's measurements.

Here again, a rowtime bound 2018-11-04 00:00:00.0 could be used to prompt a result for
2018-11-03 prior to any actual measurements for 2018-11-04 coming in is shown in the following
table.

| FLOOR_DAY             | CITY      | MIN_TEMP | MAX_TEMP | AVG_TEMP |
| --------------------- | --------- | -------- | -------- | -------- |
| 2018-11-03 00:00:00.0 | Anchorage | 1        | 1        | 1        |
| 2018-11-03 00:00:00.0 | Denver    | 36       | 36       | 36       |
