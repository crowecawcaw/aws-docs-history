

# TO\_TIMESTAMP
<a name="sql-reference-to-timestamp"></a>

Converts a Unix timestamp to a SQL timestamp in 'YYYY-MM-DD HH:MM:SS' format. 

## Syntax
<a name="sql-reference-to-timestamp-syntax"></a>

```
TO_TIMESTAMP(unixEpoch)
```

## Parameters
<a name="sql-reference-to-timestamp-parameters"></a>

*unixEpoch*

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed as a BIGINT.

## Example
<a name="sql-reference-to-timestamp-examples"></a>

### Example Dataset
<a name="w2aac22c17c19c41b9b2"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

**Note**  
The sample dataset has been modified to include a Unix timestamp value (CHANGE\_TIME).

To run each example, you need an Amazon Kinesis Analytics application that has the input stream for the sample stock ticker. To learn how to create an Analytics application and configure the input stream for the sample stock ticker, see [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
change_time     BIGINT,    --The UNIX timestamp value
price           REAL)
```

### Example 1: Convert a Unix Timestamp to a SQL Timestamp
<a name="w2aac22c17c19c41b9b4"></a>

In this example, the `change_time` value in the source stream is converted to a SQL TIMESTAMP value in the in-application stream.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    sector VARCHAR(64), 
    change REAL, 
    change_time TIMESTAMP, 
    price REAL);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM   TICKER_SYMBOL,
                SECTOR,
                CHANGE,
                TO_TIMESTAMP(CHANGE_TIME), 
                PRICE

FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing stock data with columns for time, ticker symbol, sector, change, and price.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-to-timestamp.png)


## Notes
<a name="sql-reference-to-timestamp-notes"></a>

TO\_TIMESTAMP is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics streaming SQL extension.