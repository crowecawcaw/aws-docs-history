

# UNIX\_TIMESTAMP
<a name="sql-reference-unix-timestamp"></a>

Converts a SQL timestamp to a Unix timestamp that is expressed in milliseconds since '1970-01-01 00:00:00' UTC and that is a BIGINT.

## Syntax
<a name="sql-reference-unix-timestamp-syntax"></a>

```
UNIX_TIMESTAMP(timeStampExpr)
```

## Parameters
<a name="sql-reference-unix-timestamp-parameters"></a>

*timeStampExpr*

A SQL TIMESTAMP value.

## Example
<a name="sql-reference-unix-timestamp-examples"></a>

### Example Dataset
<a name="w2aac22c17c19c43b9b2"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

**Note**  
The sample dataset has been modified to include a Timestamp value (CHANGE\_TIME).

To run each example, you need an Amazon Kinesis Analytics application that has the input stream for the sample stock ticker. To learn how to create an Analytics application and configure the input stream for the sample stock ticker, see [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
change_time     TIMESTAMP,    --The timestamp value to convert
price           REAL)
```

### Example 1: Convert a Timestamp to a UNIX Timestamp
<a name="w2aac22c17c19c43b9b4"></a>

In this example, the `change_time` value in the source stream is converted to a TIMESTAMP value in the in-application stream.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
        ticker_symbol VARCHAR(4), 
        SECTOR VARCHAR(16), 
        CHANGE REAL,
        CHANGE_TIME BIGINT, 
        PRICE REAL);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM   TICKER_SYMBOL,
                SECTOR,
                CHANGE,
                UNIX_TIMESTAMP(CHANGE_TIME),
                PRICE
FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing stock data with columns for rowtime, ticker symbol, sector, change, and price.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-unix-timestamp.png)


## Notes
<a name="sql-reference-unix-timestamp-notes"></a>

UNIX\_TIMESTAMP is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics streaming SQL extension.