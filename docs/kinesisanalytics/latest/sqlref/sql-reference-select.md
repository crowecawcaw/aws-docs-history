# SELECT statement

SELECT retrieves rows from streams. You can use SELECT as a top-level statement, or as
part of a query involving set operations, or as part of another statement, including (for
example) when passed as a query into a UDX. For examples, see the topics INSERT, IN, EXISTS,
[CREATE PUMP](sql-reference-create-pump.md "sql-reference-create-pump.md") in this
guide.

The subclauses of the SELECT statement are described in the topics [SELECT clause](sql-reference-select-clause.md "sql-reference-select-clause.md"),
[GROUP BY clause](sql-reference-group-by-clause.md "sql-reference-group-by-clause.md"), Streaming GROUP BY, [ORDER BY clause](sql-reference-order-by-clause.md "sql-reference-order-by-clause.md"),
[HAVING clause](sql-reference-having-clause.md "sql-reference-having-clause.md"), [WINDOW Clause (Sliding Windows)](sql-reference-window-clause.md "sql-reference-window-clause.md") and [WHERE clause](sql-reference-where-clause.md "sql-reference-where-clause.md") in this guide.

## Syntax

```
 <select> :=
    SELECT [ STREAM] [ DISTINCT | ALL ]
    <select-clause>
    FROM <from-clause>
    [ <where-clause> ]
    [ <group-by-clause> ]
    [ <having-clause> ]
    [ <window-clause> ]
    [ <order-by-clause> ]

```

## The STREAM keyword and the principle of streaming

SQL

The SQL query language was designed for querying stored relations, and producing
finite relational results.

The foundation of streaming SQL is the STREAM keyword, which tells the system to compute
the time differential of a relation. The time differential of a relation is the change of
the relation with respect to time. A streaming query computes the change in a relation with
respect to time, or the change in an expression computed from several relations.

To ask for the time-differential of a relation in Amazon Kinesis Data Analytics, we use the STREAM
keyword:

```
SELECT STREAM * FROM Orders

```

If we start running that query at 10:00, it will produce rows at 10:15 and 10:25. At 10:30
the query is still running, waiting for future orders:

```
ROWTIME  orderId custName   product quantity
======== ======= ========== ======= ========
10:15:00     102 Ivy Black  Rice           6
10:25:00     103 John Wu    Apples         3

```

Here, the system is saying 'At 10:15:00 I executed the query SELECT \* FROM Orders and
found one row in the result that was not present at 10:14:59.999'. It generates the row with
a value of 10:15:00 in the ROWTIME column because that is when the row appeared. This is the
core idea of a stream: a relation that keeps updating over time.

You can apply this definition to more complicated queries. For example, the stream

```
SELECT STREAM * FROM Orders WHERE quantity > 5

```

has a row at 10:15 but no row at 10:25, because the relation

```
SELECT * FROM Orders WHERE quantity > 5

```

goes from empty to one row when order 102 is placed at 10:15, but is not affected when
order 103 is placed at 10:25.

We can apply the same logic to queries involving any combination of SQL operators. Queries
involving JOIN, GROUP BY, subqueries, set operations UNION, INTERSECT, EXCEPT, and even
qualifiers such as IN and EXISTS, are well-defined when converted to streams. Queries
combining streams and stored relations are also well-defined.
