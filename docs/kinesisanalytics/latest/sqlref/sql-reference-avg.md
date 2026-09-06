

# AVG
<a name="sql-reference-avg"></a>

Returns the average of a group of values from a windowed query. A windowed query is defined in terms of time or rows. For information about windowed queries, see [Windowed Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/windowed-sql.html). To return an exponentially weighted average of a stream of value expressions selected in a specified time window, see [EXP\_AVG](sql-reference-exp-avg.md).

When you use AVG, be aware of the following:
+ If you don't use the `OVER` clause, `AVG` is calculated as an aggregate function. In this case, the aggregate query must contain a [GROUP BY clause](sql-reference-group-by-clause.md) on a monotonic expression based on `ROWTIME` that groups the stream into finite rows. Otherwise, the group is the infinite stream, and the query will never complete and no rows will be emitted. For more information, see [Aggregate Functions](sql-reference-aggregate-functions.md). 
+ A windowed query that uses a GROUP BY clause processes rows in a tumbling window. For more information, see [Tumbling Windows (Aggregations Using GROUP BY)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tumbling-window-concepts.html).
+ If you use the `OVER` clause, `AVG` is calculated as an analytic function. For more information, see [Analytic Functions](sql-reference-analytic-functions.md).
+ A windowed query that uses an OVER clause processes rows in a sliding window. For more information, see [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html) 

## Syntax
<a name="w2aac22b7c30b9"></a>

### Tumbling Windowed Query
<a name="w2aac22b7c30b9b2"></a>

```
AVG(number-expression) ... GROUP BY monotonic-expression | time-based-expression
```

### Sliding Windowed Query
<a name="w2aac22b7c30b9b4"></a>

```
AVG([DISTINCT | ALL] number-expression) OVER window-specification
```

## Parameters
<a name="w2aac22b7c30c11"></a>

DISTINCT

Performs the aggregate function only on each unique instance of a value.

ALL

Performs the aggregate function on all values. `ALL` is the default.

*number-expression*

Specifies the value expressions evaluated for each row in the aggregation.

OVER *window-specification*

Divides records in a stream partitioned by the time range interval or the number of rows. A window specification defines how records in the stream are partitioned by the time range interval or the number of rows. 

GROUP BY *monotonic-expression* \| *time-based-expression*

Groups records based on the value of the grouping expression, returning a single summary row for each group of rows that has identical values in all columns.

## Examples
<a name="sql-reference-avg-examples"></a>

### Example Dataset
<a name="w2aac22b7c30c13b2"></a>

The examples following are based on the sample stock dataset that is part of the [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the sample stock ticker input stream. To learn how to create an Analytics application and configure the sample stock ticker input stream, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Return the Average of Values Using the GROUP BY Clause
<a name="avg_example_1"></a>

In this example, the aggregate query has a `GROUP BY` clause on `ROWTIME` that groups the stream into finite rows. The `AVG` function is then calculated from the rows returned by the `GROUP BY` clause.

#### Using STEP (Recommended)
<a name="avg_example_1_step"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    avg_price     DOUBLE);  
    
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
  INSERT INTO "DESTINATION_SQL_STREAM" 
    SELECT STREAM 
        ticker_symbol,
        AVG(price) AS avg_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, 
        STEP("SOURCE_SQL_STREAM_001".ROWTIME BY INTERVAL '60' SECOND);
```

#### Using FLOOR
<a name="avg_example_1_floor"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    avg_price     DOUBLE);  

CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
  INSERT INTO "DESTINATION_SQL_STREAM" 
    SELECT STREAM 
        ticker_symbol,
        AVG(price) AS avg_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, 
        FLOOR("SOURCE_SQL_STREAM_001".ROWTIME TO MINUTE);
```

#### Results
<a name="avg_example_1_results"></a>

The preceding examples output a stream similar to the following.

![Table showing rowtime, ticker symbols such as NFS and WAS, and average prices.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-avg-example-1.png)


### Example 2: Return the Average of Values Using the OVER Clause
<a name="w2aac22b7c30c13b6"></a>

 In this example, the `OVER` clause divides records in a stream partitioned by the time range interval of '1' hour preceding. The `AVG` function is then calculated from the rows returned by the `OVER` clause. 

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4),
    avg_price     DOUBLE);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM ticker_symbol, 
        AVG(price) OVER (
            PARTITION BY ticker_symbol
            RANGE INTERVAL '1' HOUR PRECEDING) AS avg_price
    FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing rowtime, ticker symbols such as AAPL and TGT, and average prices.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-avg-example-2.png)


## Usage Notes
<a name="w2aac22b7c30c15"></a>

Amazon Kinesis Analytics doesn't support `AVG` applied to interval types. This functionality is a departure from the SQL:2008 standard.

 When used as an analytic function, `AVG` returns null if the window being evaluated contains no rows, or if all rows contain null values. For more information, see [Analytic Functions](sql-reference-analytic-functions.md). AVG also returns null for a `PARTITION BY` clause for which the partition within the window matching the input row contains no rows or all rows are null. For more information about `PARTITION BY`, see [WINDOW Clause (Sliding Windows)](sql-reference-window-clause.md). 

 `AVG` ignores null values from the set of values or a numeric expression. For example, each of the following return the value of 2: 
+ AVG(1, 2, 3) = 2
+ AVG(1,null, 2, null, 3, null) = 2

## Related Topics
<a name="w2aac22b7c30c17"></a>
+ [Windowed Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/windowed-sql.html)
+ [EXP\_AVG](sql-reference-exp-avg.md)
+ [Aggregate Functions](sql-reference-aggregate-functions.md)
+ [GROUP BY clause](sql-reference-group-by-clause.md)
+ [Analytic Functions](sql-reference-analytic-functions.md)
+ [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html)
+ [WINDOW Clause (Sliding Windows)](sql-reference-window-clause.md)