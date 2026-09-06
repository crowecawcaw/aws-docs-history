

# MAX
<a name="sql-reference-max"></a>

Returns the maximum value of a group of values from a windowed query. A windowed query is defined in terms of time or rows. For information about window queries, see [Windowed Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/windowed-sql.html).

When you use MAX, be aware of the following:
+ If you don't use the `OVER` clause, `MAX` is calculated as an aggregate function. In this case, the aggregate query must contain a [GROUP BY clause](sql-reference-group-by-clause.md) on a monotonic expression based on `ROWTIME` that groups the stream into finite rows. Otherwise, the group is the infinite stream, and the query will never complete and no rows will be emitted. For more information, see [Aggregate Functions](sql-reference-aggregate-functions.md). 
+ A windowed query that uses a GROUP BY clause processes rows in a tumbling window. For more information, see [Tumbling Windows (Aggregations Using GROUP BY)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tumbling-window-concepts.html).
+ If you use the `OVER` clause, `MAX` is calculated as an analytic function. For more information, see [Analytic Functions](sql-reference-analytic-functions.md).
+ A windowed query that uses an OVER clause processes rows in a sliding window. For more information, see [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html) 

## Syntax
<a name="w2aac22b7c42b9"></a>

### Tumbling Windowed Query
<a name="w2aac22b7c42b9b2"></a>

```
MAX(number-expression) ... GROUP BY monotonic-expression | time-based-expression
```

### Sliding Windowed Query
<a name="w2aac22b7c42b9b4"></a>

```
MAX(number-expression) OVER window-specification
```

## Parameters
<a name="w2aac22b7c42c11"></a>

*number-expression*

Specifies the value expressions evaluated for each row in the aggregation.

OVER *window-specification*

Divides records in a stream partitioned by the time range interval or the number of rows. A window specification defines how records in the stream are partitioned by the time range interval or the number of rows. 

GROUP BY *monotonic-expression* \| *time-based-expression*

Groups records based on the value of the grouping expression returning a single summary row for each group of rows that has identical values in all columns.

## Examples
<a name="sql-reference-max-examples"></a>

### Example Dataset
<a name="w2aac22b7c42c13b3"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the sample stock ticker input stream. To learn how to create an Analytics application and configure the sample stock ticker input stream, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Return the Maximum Value Using the GROUP BY Clause
<a name="w2aac22b7c42c13b5"></a>

In this example, the aggregate query has a `GROUP BY` clause on `ROWTIME` that groups the stream into finite rows. The `MAX` function is then calculated from the rows returned by the `GROUP BY` clause.

#### Using STEP (recommended)
<a name="sql-reference-max-step"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    max_price     DOUBLE);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
  INSERT INTO "DESTINATION_SQL_STREAM" 
    SELECT STREAM 
        ticker_symbol,
        MAX(Price) AS max_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, STEP("SOURCE_SQL_STREAM_001".ROWTIME BY INTERVAL '60' SECOND);
```

#### Using FLOOR
<a name="sql-reference-max-floor"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    max_price     DOUBLE);
-- CREATE OR REPLACE PUMP to insert into output
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
  INSERT INTO "DESTINATION_SQL_STREAM" 
    SELECT STREAM 
        ticker_symbol,
        MAX(Price) AS max_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, FLOOR("SOURCE_SQL_STREAM_001".ROWTIME TO MINUTE);
```

#### Results
<a name="sql-reference-max-results"></a>

The preceding examples output a stream similar to the following.

![Table showing rowtime, ticker symbol, and max price for four stock entries.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-max-example-1.png)


### Example 2: Return the Maximum Value Using the OVER Clause
<a name="w2aac22b7c42c13b7"></a>

 In this example, the `OVER` clause divides records in a stream partitioned by the time range interval of '1' hour preceding. The `MAX` function is then calculated from the rows returned by the `OVER` clause. 

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4),
    max_price     DOUBLE);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM ticker_symbol, 
        MAX(price) OVER (
            PARTITION BY ticker_symbol
            RANGE INTERVAL '1' HOUR PRECEDING) AS max_price
    FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing rowtime, ticker symbols such as QAZ and QXZ, and corresponding max prices.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-max-example-2.png)


## Usage Notes
<a name="w2aac22b7c42c15"></a>

For string values, MAX is determined by which string is last in the collating sequence.

 If MAX is used as an analytic function and the window being evaluated contains no rows, MAX returns null. For more information, see [Analytic Functions](sql-reference-analytic-functions.md). 

## Related Topics
<a name="w2aac22b7c42c17"></a>
+ [Windowed Queries](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/windowed-sql.html)
+ [Aggregate Functions](sql-reference-aggregate-functions.md)
+ [GROUP BY clause](sql-reference-group-by-clause.md)
+ [Analytic Functions](sql-reference-analytic-functions.md)
+ [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html)
+ [WINDOW Clause (Sliding Windows)](sql-reference-window-clause.md)