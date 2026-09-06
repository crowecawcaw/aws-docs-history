

# VAR\_POP
<a name="sql-reference-VARPOP"></a>

Returns the population variance of a non-null set of numbers (nulls being ignored)

VAR\_POP uses the following calculation:
+ (SUM(expr\*expr) - SUM(expr)\*SUM(expr) / COUNT(expr)) / COUNT(expr)

In other words, for a given set of non-null values, using S1 as the sum of the values and S2 as the sum of the squares of the values, VAR\_POP returns the result (S2-S1\*S1/N)/N.

When you use `VAR_POP`, be aware of the following:
+ When the input set has no non-null data, or when applied to an empty set, `VAR_POP` returns `NULL`.
+ If you don't use the `OVER` clause, `VAR_POP` is calculated as an aggregate function. In this case, the aggregate query must contain a [GROUP BY clause](sql-reference-group-by-clause.md) on a monotonic expression based on `ROWTIME` that groups the stream into finite rows. Otherwise, the group is the infinite stream, and the query will never complete and no rows will be emitted. For more information, see [Aggregate Functions](sql-reference-aggregate-functions.md). 
+ A windowed query that uses a `GROUP BY` clause processes rows in a tumbling window. For more information, see [Tumbling Windows (Aggregations Using GROUP BY)](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/tumbling-window-concepts.html).
+ If you use the `OVER` clause, `VAR_POP` is calculated as an analytic function. For more information, see [Analytic Functions](sql-reference-analytic-functions.md).
+ A windowed query that uses an `OVER` clause processes rows in a sliding window. For more information, see [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html) 

## Syntax
<a name="varpop-syntax"></a>

```
 VAR_POP ( [DISTINCT | ALL] number-expression )
```

## Parameters
<a name="varpop-parameters"></a>

### ALL
<a name="varpop-parameters-all"></a>

Includes duplicate values in the input set. `ALL` is the default.

### DISTINCT
<a name="varpop-parameters-distinct"></a>

Excludes duplicate values in the input set.

## Examples
<a name="varpop-examples"></a>

### Example Dataset
<a name="w2aac22c29c20c29b2"></a>

The examples following are based on the sample stock dataset that is part of the [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the sample stock ticker input stream. To learn how to create an Analytics application and configure the sample stock ticker input stream, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Determine the population variance in a column in a tumbling window query
<a name="varpop_example_1"></a>

The following example demonstrates how to use the `VARPOP` function to determine the population variance of the values in a tumbling window of the PRICE column of the example dataset. `DISTINCT` is not specified, so duplicate values are included in the calculation.

#### Using STEP (Recommended)
<a name="varpop_example_step"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4), var_pop_price REAL);

CREATE OR REPLACE  PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM ticker_symbol, VAR_POP(price) AS var_pop_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, STEP(("SOURCE_SQL_STREAM_001".ROWTIME) BY INTERVAL '60' SECOND);
```

#### Using FLOOR
<a name="varpop_example_floor"></a>

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4), var_pop_price REAL);

CREATE OR REPLACE  PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM ticker_symbol, VAR_POP(price) AS var_pop_price
    FROM "SOURCE_SQL_STREAM_001"
    GROUP BY ticker_symbol, FLOOR(("SOURCE_SQL_STREAM_001".ROWTIME - TIMESTAMP '1970-01-01 00:00:00') SECOND / 10 TO SECOND);
```

#### Results
<a name="varpop_example_results"></a>

The preceding examples output a stream similar to the following:

![Table with columns ROWTIME, TICKER_SYMBOL, and VAR_POP_PRICE showing stock data entries.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-varpop-1.png)


### Example 2: Determine the population variance of the values in a columm in a sliding window query
<a name="w2aac22c29c20c29b6"></a>

The following example demonstrates how to use the `VARPOP` function to determine the population variance of the values in a sliding window of the PRICE column of the example dataset. `DISTINCT` is not specified, so duplicate values are included in the calculation.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (ticker_symbol VARCHAR(4), var_pop_price REAL);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM ticker_symbol, VAR_POP(price) OVER TEN_SECOND_SLIDING_WINDOW AS var_pop_price
FROM "SOURCE_SQL_STREAM_001"
 
WINDOW TEN_SECOND_SLIDING_WINDOW AS (
  PARTITION BY ticker_symbol
  RANGE INTERVAL '10' SECOND PRECEDING);
```

The preceding example outputs a stream similar to the following:

![Table showing ROWTIME, TICKER_SYMBOL, and VAR_POP_PRICE columns with sample data rows.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-varpop-2.png)


## See Also
<a name="varpop-seealso"></a>
+ Population standard deviation: [STDDEV\_POP](sql-reference-STDDEVPOP.md)
+ Sample standard deviation: [STDDEV\_SAMP](sql-reference-STDDEVSAMP.md)
+ Sample variance: [VAR\_SAMP](sql-reference-VARSAMP.md)