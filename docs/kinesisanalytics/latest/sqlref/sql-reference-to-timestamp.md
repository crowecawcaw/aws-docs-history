# TO_TIMESTAMP

Converts a Unix timestamp to a SQL timestamp in 'YYYY-MM-DD HH:MM:SS' format.

## Syntax

```
TO_TIMESTAMP(unixEpoch)
```

## Parameters

_unixEpoch_

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed
as a BIGINT.

## Example

### Example Dataset

The examples following are based on the sample stock dataset that is part of
[Getting Started
Exercise](../dev/get-started-exercise.md "../dev/get-started-exercise.md") in the _Amazon Kinesis Analytics Developer
Guide_.

###### Note

The sample dataset has been modified to include a Unix timestamp value (CHANGE_TIME).

To run each example, you need an Amazon Kinesis Analytics application that has the
input stream for the sample stock ticker. To learn how to create an Analytics
application and configure the input stream for the sample stock ticker, see [Getting Started Exercise](../dev/get-started-exercise.md "../dev/get-started-exercise.md") in
the _Amazon Kinesis Analytics Developer Guide_.

The sample stock dataset has the schema following.

```

(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
change_time     BIGINT,    --The UNIX timestamp value
price           REAL)

```

### Example 1: Convert a Unix Timestamp to a SQL Timestamp

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

![Table showing stock data with columns for time, ticker symbol, sector, change, and price.](images/sql-reference-to-timestamp.png)

## Notes

TO_TIMESTAMP is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics streaming SQL
extension.
