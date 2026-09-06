

# STDDEV\_SAMP
<a name="sql-reference-STDDEVSAMP"></a>

Returns the statistical standard deviation of all values in <number-expression>, evaluated for each row remaining in the group and defined as the square root of the [VAR\_SAMP](sql-reference-VARSAMP.md).

When you use `STDDEV_SAMP`, be aware of the following:
+ When the input set has no non-null data, `STDDEV_SAMP` returns `NULL`.
+ If you don't use the `OVER` clause, `STDDEV_SAMP` is calculated as an aggregate function. In this case, the aggregate query must contain a [GROUP BY clause](sql-reference-group-by-clause.md) on a monotonic expression based on `ROWTIME` that groups the stream into finite rows. Otherwise, the group is the infinite stream, and the query will never complete and no rows will be emitted. For more information, see [Aggregate Functions](sql-reference-aggregate-functions.md). 
+ A windowed query that uses a GROUP BY clause processes rows in a tumbling window. For more information, see [Tumbling Windows (Aggregations Using GROUP BY)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tumbling-window-concepts.html).
+ If you use the `OVER` clause, `STDDEV_SAMP` is calculated as an analytic function. For more information, see [Analytic Functions](sql-reference-analytic-functions.md).
+ A windowed query that uses an OVER clause processes rows in a sliding window. For more information, see [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html) 
+ `STD_DEV` is an alias of `STDDEV_SAMP`.

## Syntax
<a name="stddevsamp-syntax"></a>

```
 STDDEV_SAMP ( [DISTINCT | ALL] number-expression )
```

## Parameters
<a name="stddevsamp-parameters"></a>

### ALL
<a name="stddevsamp-parameters-all"></a>

Includes duplicate values in the input set. `ALL` is the default.

### DISTINCT
<a name="stddevsamp-parameters-distinct"></a>

Excludes duplicate values in the input set.

## Examples
<a name="stddevsamp-examples"></a>

### Example Dataset
<a name="w2aac22c29c18c23b2"></a>

The examples following are based on the sample stock dataset that is part of the [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the sample stock ticker input stream. To learn how to create an Analytics application and configure the sample stock ticker input stream, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Determine the statistical standard deviation of the values in a column in a tumbling window query
<a name="w2aac22c29c18c23b4"></a>

The following example demonstrates how to use the `STDDEV_SAMP` function to determine the standard deviation of the values in a tumbling window of the PRICE column of the example dataset. `DISTINCT` is not specified, so duplicate values are included in the calculation.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4), stddev_samp_price REAL);

CREATE OR REPLACE  PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM ticker_symbol, STDDEV_SAMP(price) AS stddev_samp_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, FLOOR(("SOURCE_SQL_STREAM_001".ROWTIME - TIMESTAMP '1970-01-01 00:00:00') SECOND / 10 TO SECOND);
```

### Results
<a name="stddev-example-results"></a>

The preceding examples output a stream similar to the following:

![Table with columns ROWTIME, TICKER_SYMBOL, and STDDEV_SAMP_PRICE showing stock data for AMZN, WSB, JKL, and QXZ.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-stddev-samp-1.png)


### Example 2: Determine the statistical standard deviation of the values in a columm in a sliding window query
<a name="w2aac22c29c18c23c10"></a>

The following example demonstrates how to use the `STDDEV_SAMP` function to determine the standard deviation of the values in a sliding window of the PRICE column of the example dataset. `DISTINCT` is not specified, so duplicate values are included in the calculation.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4), stddev_samp_price REAL);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM ticker_symbol, STDDEV_SAMP(price) OVER TEN_SECOND_SLIDING_WINDOW AS stddev_samp_price
FROM "SOURCE_SQL_STREAM_001"
 
WINDOW TEN_SECOND_SLIDING_WINDOW AS (
  PARTITION BY ticker_symbol
  RANGE INTERVAL '10' SECOND PRECEDING);
```

The preceding example outputs a stream similar to the following:

![Table with columns ROWTIME, TICKER_SYMBOL, and STDDEV_SAMP_PRICE showing stock data rows.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-stddev-samp-2.png)


## See Also
<a name="stddevsamp-seealso"></a>
+ Population standard deviation: [STDDEV\_POP](sql-reference-STDDEVPOP.md)
+ Sample variance: [VAR\_SAMP](sql-reference-VARSAMP.md)
+ Population variance: [VAR\_POP](sql-reference-VARPOP.md)