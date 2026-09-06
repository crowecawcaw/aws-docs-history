

# REGEX\_REPLACE
<a name="sql-reference-regex-replace"></a>

REGEX\_REPLACE replaces a substring with an alternative substring. It returns the value of the following Java expression.

```
java.lang.String.replaceAll(regex, replacement)
```

## Syntax
<a name="sql-reference-regex-replace-syntax"></a>

```
REGEX_REPLACE(original VARCHAR(65535), regex VARCHAR(65535), replacement VARCHAR(65535), startPosition int, occurence int)

RETURNS VARCHAR(65535)
```

## Parameters
<a name="sql-reference-regex-replace-parameters"></a>

*original*

The string on which to execute the regex operation.

*regex*

The [regular expression](https://en.wikipedia.org/wiki/Regular_expression) to match. If the encoding for *regex* doesn't match the encoding for *original*, an error is written to the error stream.

*replacement*

The string to replace *regex* matches in the *original* string. If the encoding for *replacement* doesn't match the encoding for *original* or *regex*, an error is written to the error stream.

*startPosition*

The first character in the *original* string to search. If *startPosition* is less than 1, an error is written to the error stream. If *startPosition* is greater than the length of *original*, then *original* is returned.

*occurence*

The occurrence of the string that matches the *regex* expression to replace. If *occurence* is 0, all substrings matching *regex* are replaced. If *occurence* is less than 0, an error is written to the error stream.

## Example
<a name="sql-reference-regex-replace-example"></a>

### Example Dataset
<a name="w2aac22c33c17c11b2"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

To run each example, you need an Amazon Kinesis Analytics application that has the input stream for the sample stock ticker. To learn how to create an Analytics application and configure the input stream for the sample stock ticker, see [Getting Started Exercise](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. 

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Replace All String Values in a Source String with a New Value
<a name="w2aac22c33c17c11b4"></a>

In this example, all character strings in the `sector` field are replaced if they match a regular expression.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
        ticker_symbol VARCHAR(4), 
        SECTOR VARCHAR(24), 
        CHANGE REAL, 
        PRICE REAL);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"

SELECT STREAM   TICKER_SYMBOL,
                REGEX_REPLACE(SECTOR, 'TECHNOLOGY', 'INFORMATION TECHNOLOGY', 1, 0);
                CHANGE,
                PRICE
FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing stock data with columns for rowtime, ticker symbol, sector, change, and price.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-regex-replace.png)


## Notes
<a name="sql-reference-regex-replace-notes"></a>

REGEX\_REPLACE is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics streaming SQL extension.

REGEX\_REPLACE returns `null` if any parameters are `null`.