

# WINDOW Clause (Sliding Windows)
<a name="sql-reference-window-clause"></a>

The `WINDOW` clause for a sliding windowed query specifies the rows over which analytic functions are computed across a group of rows in relation to the current row. These aggregate functions produce an output row aggregated by the keys in one or more columns for each input row. The `WINDOW` clause in a query specifies records in a stream partitioned by the time range interval or the number of rows, and an additional optional set of columns specified by the `PARTITION BY` clause. You can define named or inline window specifications that can be used in analytic functions and streaming `JOIN` clauses. For more information about analytic functions, see [Analytic Functions](sql-reference-analytic-functions.md).

Aggregate functions in a sliding window query are performed over each column specified in the `OVER` clause. The `OVER` clause can reference a named window specification or can be inline as part of the `SELECT` statement for a pump. The following examples show how to use the `OVER` clause to reference a named window specification and inline in the `SELECT` statement. 

## Syntax
<a name="w2aac20c15c30b7"></a>

```
[WINDOW window_name AS 
(
	{PARTITION BY partition_name 
		RANGE INTERVAL 'interval' {SECOND | MINUTE | HOUR} PRECEDING | 
		ROWS number PRECEDING
, …}
)
```

## OVER Clause
<a name="w2aac20c15c30b9"></a>

The examples following show you how to use the `OVER` clause to reference a named window specification.

**Example 1: OVER Referencing a Named Window Specification**

The following example shows an aggregate function that references the window specification with the name W1. In this example, the average price is calculated over the set of records specified by the `W1` window specification. To learn more about how to use the OVER clause with a window specification, see [Examples](#sql-reference-window-clause-examples), following.

```
AVG(price) OVER W1 AS avg_price 
```

**Example 2: OVER Referencing an Inline Window Specification**

 The following example shows an aggregate function that references an inline window specification. In this example, the average price is calculated over each input row with an inline window specification. To learn more about how to use the OVER clause with a window specification, see [Examples](#sql-reference-window-clause-examples), following. 

```
AVG(price) OVER (
    PARTITION BY ticker_symbol
    RANGE INTERVAL '1' HOUR PRECEDING) AS avg_price
```

For more information about aggregate functions and the OVER clause, see [Aggregate Functions](sql-reference-aggregate-functions.md).

## Parameters
<a name="w2aac20c15c30c11"></a>

*window-name*

Specifies a unique name that can be referenced from OVER clauses or subsequent window definitions. The name is used in analytic functions and streaming `JOIN` clauses. For more information about analytic functions, see [Analytic Functions](sql-reference-analytic-functions.md).

AS

Defines the named window specification for the `WINDOW` clause. 

PARTITION BY *partition-name*

Divides rows into groups that share the same values. After rows are partitioned, the window function computes all rows that fall into the same partition as the current row.

RANGE INTERVAL *'interval'* {SECOND \| MINUTE \| HOUR} PRECEDING

Specifies the window boundaries from the time range interval. The window function computes all rows that fall into the same time interval as the current row.

ROWS *number* PRECEDING

Specifies the window boundaries from the number of rows. The window function computes all rows that fall into the same number of rows.

## Examples
<a name="sql-reference-window-clause-examples"></a>

### Example Dataset
<a name="w2aac20c15c30c13b3"></a>

The examples following are based on the sample stock dataset that is part of [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. To run each example, you need an Amazon Kinesis Analytics application that has the sample stock ticker input stream. To learn how to create an Analytics application and configure the sample stock ticker input stream, see [Getting Started](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/get-started-exercise.html) in the *Amazon Kinesis Analytics Developer Guide*. For additional samples, see [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html).

The sample stock dataset has the schema following.

```
(ticker_symbol  VARCHAR(4),
sector          VARCHAR(16),
change          REAL,
price           REAL)
```

### Example 1: Time-Based Sliding Window That References a Named Window Specification
<a name="w2aac20c15c30c13b5"></a>

This example defines a named window specification with a partition boundary of one minute preceding the current row. The `OVER` clause of the `SELECT` statement for the pump references the named window specification. 

```
WINDOW W1 AS (
    PARTITION BY ticker_symbol 
    RANGE INTERVAL '1' MINUTE PRECEDING);
```

To run this example, create the stock sample application and run and save the SQL code following.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4), 
    min_price     DOUBLE, 
    max_price     DOUBLE, 
    avg_price     DOUBLE);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM ticker_symbol,
        MIN(price) OVER W1 AS min_price,
        MAX(price) OVER W1 AS max_price,
        AVG(price) OVER W1 AS avg_price
    FROM "SOURCE_SQL_STREAM_001"
    WINDOW W1 AS (
        PARTITION BY ticker_symbol 
        RANGE INTERVAL '1' MINUTE PRECEDING);
```

The preceding example outputs a stream similar to the following.

![Table showing stock ticker data with columns for rowtime, ticker symbol, min price, max price, and avg price.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-analytic-functions-example-1.png)


### Example 2: Row-Based Sliding Window That References a Named Window Specification
<a name="w2aac20c15c30c13b7"></a>

This example defines a named window specification with a partition boundary of two rows preceding the current row and ten rows preceding the current row. The `OVER` clause of the `SELECT` statement for the pump references the named window specification. 

```
 WINDOW
    last2rows AS (PARTITION BY ticker_symbol ROWS 2 PRECEDING),
    last10rows AS (PARTITION BY ticker_symbol ROWS 10 PRECEDING);
```

To run this example, create the stock sample application and run and save the SQL code following.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol      VARCHAR(4), 
    price              DOUBLE, 
    avg_last2rows      DOUBLE, 
    avg_Last10rows     DOUBLE);
CREATE OR REPLACE PUMP "myPump" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM ticker_symbol, 
    price, 
    AVG(price) OVER last2rows, 
    AVG(price) OVER last10rows
FROM SOURCE_SQL_STREAM_001
WINDOW
    last2rows AS (PARTITION BY ticker_symbol ROWS 2 PRECEDING),
    last10rows AS (PARTITION BY ticker_symbol ROWS 10 PRECEDING);
```

The preceding example outputs a stream similar to the following.

![Table showing stock data with columns for rowtime, ticker symbol, price, and averages.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-analytic-functions-example-2.png)


### Example 3: Time-Based Sliding Window with Inline Window Specification
<a name="w2aac20c15c30c13b9"></a>

This example defines an inline window specification with a partition boundary of one minute preceding the current row. The `OVER` clause of the `SELECT` statement for the pump uses the inline window specification.

To run this example, create the stock sample application and run and save the SQL code following.

```
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4),
    price         DOUBLE,
    avg_price     DOUBLE);
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
    INSERT INTO "DESTINATION_SQL_STREAM"
    SELECT STREAM ticker_symbol, price, 
        AVG(Price) OVER (
            PARTITION BY ticker_symbol
            RANGE INTERVAL '1' HOUR PRECEDING) AS avg_price
    FROM "SOURCE_SQL_STREAM_001"
```

The preceding example outputs a stream similar to the following.

![Table showing stock data with columns for rowtime, ticker symbol, price, and average price.](http://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/images/sql-reference-analytic-functions-example-3.png)


## Usage Notes
<a name="w2aac20c15c30c15"></a>

### 
<a name="w2aac20c15c30c15b2"></a>

For the WINDOW clause and endpoints, Amazon Kinesis Analytics SQL follows SQL-2008 standards for windows over a range. 

To include the endpoints of an hour, you can use the window syntax following.

```
WINDOW HOUR AS (RANGE INTERVAL '1' HOUR PRECEDING) 
```

To not include the endpoints of the previous hour, you can use the window syntax following.

```
WINDOW HOUR AS (RANGE INTERVAL '59:59.999' MINUTE TO SECOND(3) PRECEDING);
```

For more information, see [Allowed and Disallowed Window Specifications](sql-reference-allowed-disallowed-window.md).

## Related Topics
<a name="w2aac20c15c30c17"></a>
+ [Sliding Windows](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/sliding-window-concepts.html) in the Kinesis Developer Guide
+ [Aggregate Functions](sql-reference-aggregate-functions.md)
+ [SELECT statement](sql-reference-select.md)
+ [CREATE STREAM](sql-reference-create-stream.md) statement
+ [CREATE PUMP](sql-reference-create-pump.md) statement