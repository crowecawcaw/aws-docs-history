

# LAG
<a name="sql-reference-lag"></a>

LAG returns the evaluation of the expression (such as the name of a column) for the record that is N records before the current record in a given window. Both offset and default are evaluated with respect to the current record. If there is no such record, LAG instead returns a specified default expression. LAG returns a value of the same type as the expression. 

## Syntax
<a name="sql-reference-lag-syntax"></a>

```
LAG(expr [ , N [ , defaultExpr]]) [ IGNORE NULLS | RESPECT NULLS ] OVER [ window-definition ] 
```

## Parameters
<a name="sql-reference-lag-parameters"></a>

*expr*

An expression that is evaluated on a record.

*N*

The number of records before the current record to query. The default is `1`.

*defaultExpr*

An expression of the same type as *expr* that is returned if the record queried (*n* before the current record) falls outside the window. If not specified, *null* is returned for values that fall outside the window.

**Note**  
The *defaultExpr* expression doesn't replace actual *null* values returned from the source stream.

IGNORE NULLS

A clause that specifies that null values are not counted when determining the offset. For example, suppose that `LAG(expr, 1)` is queried, and the previous record has a null value for *expr*. Then the second record previous is queried, and so on.

RESPECT NULLS

A clause that specifies that null values are counted when determining the offset. This behavior is the default.

OVER *window-specification*

A clause that divides records in a stream partitioned by the time range interval or the number of records. A window specification defines how records in the stream are partitioned, whether by the time range interval or the number of records. 

## Example
<a name="sql-reference-lag-examples"></a>

### Example Dataset
<a name="w2aac22c31b7b9b2"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the input stream for the sample stock ticker. To learn how to create an Analytics application and configure the input stream for the sample stock ticker, see [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Return Values from Previous Records in an OVER Clause
<a name="w2aac22c31b7b9b4"></a>

In this example, the OVER clause divides records in a stream partitioned by the time range interval of '1' minute preceding. The LAG function then retrieves price values from the two previous records that contain the given ticker symbol, skipping records if `price` is null.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4),
    price     DOUBLE,
    previous_price DOUBLE,
    previous_price_2 DOUBLE);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM ticker_symbol, 
         price,
         LAG(price, 1, 0) IGNORE NULLS OVER (
            PARTITION BY ticker_symbol
            RANGE INTERVAL '1' MINUTE PRECEDING),
         LAG(price, 2, 0) IGNORE NULLS OVER (
            PARTITION BY ticker_symbol
            RANGE INTERVAL '1' MINUTE PRECEDING)   
    FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Data table showing stock ticker symbols with corresponding price values and timestamps.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-lag.png)


## Notes
<a name="sql-reference-lag-notes"></a>

LAG is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics streaming SQL extension.