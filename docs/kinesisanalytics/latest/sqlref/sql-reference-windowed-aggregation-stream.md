# Windowed Aggregation on

Streams

To illustrate how windowed aggregation works on Amazon Kinesis data streams, assume that the data
in the following table is flowing through a stream called WEATHERSTREAM.

| ROWTIME               | CITY      | TEMP |
| --------------------- | --------- | ---- |
| 2018-11-01 01:00:00.0 | Denver    | 29   |
| 2018-11-01 01:00:00.0 | Anchorage | 2    |
| 2018-11-01 06:00:00.0 | Miami     | 65   |
| 2018-11-01 07:00:00.0 | Denver    | 32   |
| 2018-11-01 09:00:00.0 | Anchorage | 9    |
| 2018-11-01 13:00:00.0 | Denver    | 50   |
| 2018-11-01 17:00:00.0 | Anchorage | 10   |
| 2018-11-01 18:00:00.0 | Miami     | 71   |
| 2018-11-01 19:00:00.0 | Denver    | 43   |
| 2018-11-02 01:00:00.0 | Anchorage | 4    |
| 2018-11-02 01:00:00.0 | Denver    | 39   |
| 2018-11-02 07:00:00.0 | Denver    | 46   |
| 2018-11-02 09:00:00.0 | Anchorage | 3    |
| 2018-11-02 13:00:00.0 | Denver    | 56   |
| 2018-11-02 17:00:00.0 | Anchorage | 2    |
| 2018-11-02 19:00:00.0 | Denver    | 50   |
| 2018-11-03 01:00:00.0 | Denver    | 36   |
| 2018-11-03 01:00:00.0 | Anchorage | 1    |

Suppose that you want to find the minimum and maximum temperature recorded in the 24-hour
period prior to any given reading, globally, regardless of city. To do this, you define a window
of `RANGE INTERVAL '1' DAY PRECEDING`, and use it in the `OVER` clause for
the `MIN` and `MAX` analytic functions:

```
 SELECT STREAM
        ROWTIME,
        MIN(TEMP) OVER W1 AS WMIN_TEMP,
        MAX(TEMP) OVER W1 AS WMAX_TEMP
 FROM WEATHERSTREAM
 WINDOW W1 AS (
    RANGE INTERVAL '1' DAY PRECEDING
);
```

## Results

| ROWTIME               | WMIN_TEMP | WMAX_TEMP |
| --------------------- | --------- | --------- |
| 2018-11-01 01:00:00.0 | 29        | 29        |
| 2018-11-01 01:00:00.0 | 2         | 29        |
| 2018-11-01 06:00:00.0 | 2         | 65        |
| 2018-11-01 07:00:00.0 | 2         | 65        |
| 2018-11-01 09:00:00.0 | 2         | 65        |
| 2018-11-01 13:00:00.0 | 2         | 65        |
| 2018-11-01 17:00:00.0 | 2         | 65        |
| 2018-11-01 18:00:00.0 | 2         | 71        |
| 2018-11-01 19:00:00.0 | 2         | 71        |
| 2018-11-02 01:00:00.0 | 2         | 71        |
| 2018-11-02 01:00:00.0 | 2         | 71        |
| 2018-11-02 07:00:00.0 | 4         | 71        |
| 2018-11-02 09:00:00.0 | 3         | 71        |
| 2018-11-02 13:00:00.0 | 3         | 71        |
| 2018-11-02 17:00:00.0 | 2         | 71        |
| 2018-11-02 19:00:00.0 | 2         | 56        |
| 2018-11-03 01:00:00.0 | 2         | 56        |
| 2018-11-03 01:00:00.0 | 1         | 56        |

Now, assume that you want to find the minimum, maximum, and average temperature recorded
in the 24-hour period prior to any given reading, broken down by city. To do this, you add a
`PARTITION BY` clause on `CITY` to the window specification, and add
the `AVG` analytic function over the same window to the selection list:

```
 SELECT STREAM
        ROWTIME,
        CITY,
        MIN(TEMP) over W1 AS WMIN_TEMP,
        MAX(TEMP) over W1 AS WMAX_TEMP,
        AVG(TEMP) over W1 AS WAVG_TEMP
 FROM AGGTEST.WEATHERSTREAM
 WINDOW W1 AS (
        PARTITION BY CITY
        RANGE INTERVAL '1' DAY PRECEDING
 );
```

### Results

| ROWTIME               | CITY      | WMIN_TEMP | WMAX_TEMP | WAVG_TEMP |
| --------------------- | --------- | --------- | --------- | --------- |
| 2018-11-01 01:00:00.0 | Denver    | 29        | 29        | 29        |
| 2018-11-01 01:00:00.0 | Anchorage | 2         | 2         | 2         |
| 2018-11-01 06:00:00.0 | Miami     | 65        | 65        | 65        |
| 2018-11-01 07:00:00.0 | Denver    | 29        | 32        | 30        |
| 2018-11-01 09:00:00.0 | Anchorage | 2         | 9         | 5         |
| 2018-11-01 13:00:00.0 | Denver    | 29        | 50        | 37        |
| 2018-11-01 17:00:00.0 | Anchorage | 2         | 10        | 7         |
| 2018-11-01 18:00:00.0 | Miami     | 65        | 71        | 68        |
| 2018-11-01 19:00:00.0 | Denver    | 29        | 50        | 38        |
| 2018-11-02 01:00:00.0 | Anchorage | 2         | 10        | 6         |
| 2018-11-02 01:00:00.0 | Denver    | 29        | 50        | 38        |
| 2018-11-02 07:00:00.0 | Denver    | 32        | 50        | 42        |
| 2018-11-02 09:00:00.0 | Anchorage | 3         | 10        | 6         |
| 2018-11-02 13:00:00.0 | Denver    | 39        | 56        | 46        |
| 2018-11-02 17:00:00.0 | Anchorage | 2         | 10        | 4         |
| 2018-11-02 19:00:00.0 | Denver    | 39        | 56        | 46        |
| 2018-11-03 01:00:00.0 | Denver    | 36        | 56        | 45        |
| 2018-11-03 01:00:00.0 | Anchorage | 1         | 4         | 2         |

## Examples of Rowtime Bounds and Windowed

Aggregation

This is an example of a windowed aggregate query:

```
 SELECT STREAM ROWTIME, ticker, amount, SUM(amount)
    OVER (
        PARTITION BY ticker
        RANGE INTERVAL '1' HOUR PRECEDING)
 AS hourlyVolume
 FROM Trades

```

Because this is a query on a stream, rows pop out of this query as soon as they go in. For
example, given the following inputs:

```
Trades: IBM 10 10 10:00:00
Trades: ORCL 20 10:10:00
Trades.bound: 10:15:00
Trades: ORCL 15 10:25:00
Trades: IBM 30 11:05:00
Trades.bound: 11:10:00

```

In this example, the output is as follows:

```
Trades: IBM 10 10 10:00:00
Trades: ORCL 20 20 10:10:00
Trades.bound: 10:15:00
Trades: ORCL 15 35 10:25:00
Trades: IBM 30 30 11:05:00
Trades.bound: 11:10:00

```

The rows still hang around behind the scenes for an hour, and thus the second ORCL row
output has a total of 35; but the original IBM trade falls outside the "hour preceding"
window, and so it is excluded from the IBM sum.

## Example

Some business problems seem to need totals over the whole history of a stream, but this is
usually not practical to compute. However, such business problems are often solvable by
looking at the last day, the last hour, or the last N records. Sets of such records are called
_windowed aggregates_.

They are easy to compute in a stream database, and can be expressed in ANSI (SQL:2008)
standard SQL as follows:

```
SELECT STREAM ticker,
      avg(price) OVER lastHour AS avgPrice,
      max(price) OVER lastHour AS maxPrice
   FROM Bids
   WINDOW lastHour AS  (
      PARTITION BY ticker
      RANGE INTERVAL '1' HOUR PRECEDING)
```

##

###### Note

The `Interval_clause` must be of one of the following appropriate types:

- Integer literal with ROWS
- Numeric value for RANGE over a numeric column
- INTERVAL for a RANGE over a date/time/timestamp
