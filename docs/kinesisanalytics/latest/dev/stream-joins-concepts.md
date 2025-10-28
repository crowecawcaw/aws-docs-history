After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Streaming Data Operations: Stream Joins

You can have multiple in-application streams in your application. You can write
`JOIN` queries to correlate data arriving on these streams. For example,
suppose that you have the following in-application streams:

- **OrderStream** – Receives stock orders being placed.

```
(orderId `SqlType`, ticker `SqlType`, amount `SqlType`, ROWTIME TimeStamp)
```

- **TradeStream** – Receives resulting stock trades for those
  orders.

```
(tradeId `SqlType`, orderId `SqlType`, ticker `SqlType`, amount `SqlType`, ticker `SqlType`, amount `SqlType`, ROWTIME TimeStamp)
```

The following are `JOIN` query examples that correlate data on these streams.

## Example 1: Report Orders Where There Are Trades Within One

Minute of the Order Being Placed

In this example, your query joins both the `OrderStream` and
`TradeStream`. However, because we want only trades placed one minute
after the orders, the query defines the 1-minute window over the
`TradeStream`. For information about windowed queries, see [Sliding Windows](sliding-window-concepts.md "sliding-window-concepts.md").

```
SELECT STREAM
     ROWTIME,
     o.orderId, o.ticker, o.amount AS orderAmount,
     t.amount AS tradeAmount
FROM OrderStream AS o
JOIN TradeStream OVER (RANGE INTERVAL '1' MINUTE PRECEDING) AS t
ON   o.orderId = t.orderId;
```

You can define the windows explicitly using the `WINDOW` clause and writing the
preceding query as follows:

```
SELECT STREAM
    ROWTIME,
    o.orderId, o.ticker, o.amount AS orderAmount,
    t.amount AS tradeAmount
FROM OrderStream AS o
JOIN TradeStream OVER t
ON o.orderId = t.orderId
WINDOW t AS
    (RANGE INTERVAL '1' MINUTE PRECEDING)
```

When you include this query in your application code, the application code runs
continuously. For each arriving record on the `OrderStream`, the application
emits an output if there are trades within the 1-minute window following the order being
placed.

The join in the preceding query is an inner join where the query emits records in
`OrderStream` for which there is a matching record in
`TradeStream` (and vice versa). Using an outer join you can create another
interesting scenario. Suppose that you want stock orders for which there are no trades
within one minute of stock order being placed, and trades reported within the same
window but for some other orders. This is example of an _outer join_.

```
SELECT STREAM
    ROWTIME,
    o.orderId, o.ticker, o.amount AS orderAmount,
    t.ticker, t.tradeId, t.amount AS tradeAmount,
FROM OrderStream AS o
LEFT OUTER JOIN TradeStream OVER (RANGE INTERVAL '1' MINUTE PRECEDING) AS t
ON    o.orderId = t.orderId;
```
