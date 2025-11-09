# Query

## Syntax

```
 <query> :=
     <select>
   | <query> <set-operator> [ ALL ] <query>
   | VALUES <row-constructor> { , <row-constructor> }...
   | '(' <query> ')'
  <set-operator> :=
     EXCEPT
   | INTERSECT
   | UNION
  <row-constructor> :=
     [ ROW ] ( <expression> { , <expression> }... )
```

## select

The select box in the chart above represents any SELECT command; that command is described
in detail on its own page.

Set operators (EXCEPT, INTERSECT, UNION)

Set operators combine rows produced by queries using set operations:

- EXCEPT returns all rows that are in the first set but not in the second
- INTERSECT returns all rows that are in both first and second sets
- UNION returns all rows that are in either set

In all cases, the two sets must have the same number of columns, and the column types must
be assignment-compatible. The column names of the resulting relation are the names of the
columns of the first query.

With the ALL keyword, the operators use the semantics of a mathematical
[Multiset](https://en.wikipedia.org/wiki/Multiset "https://en.wikipedia.org/wiki/Multiset")
, meaning that duplicate rows are
not eliminated. For example, if a particular row occurs 5 times in the first set and 2 times in
the second set, then UNION ALL will emit the row 3 + 2 = 5 times.

ALL is not currently supported for EXCEPT or INTERSECT.

All operators are left-associative, and INTERSECT has higher precedence than EXCEPT or
UNION, which have the same precedence. To override default precedence, you can use parentheses.
For example:

```
SELECT * FROM a
UNION
SELECT * FROM b
INTERSECT
SELECT * FROM c
EXCEPT
SELECT * FROM d
EXCEPT
SELECT * FROM E

```

is equivalent to the fully-parenthesized query

```
( ( SELECT * FROM a
    UNION
    ( SELECT * FROM b
      INTERSECT
      SELECT * FROM c) )
  EXCEPT
  SELECT * FROM d )
EXCEPT
SELECT * FROM e
```

## Streaming set operators

UNION ALL is the only set operator that can be applied to streams. Both sides of the
operator must be streams; it is an error if one side is a stream and the other is a
relation.

For example, the following query produces a stream of orders taken over the phone or via the
web:

```
SELECT STREAM *
  FROM PhoneOrders
UNION ALL
SELECT STREAM *
  FROM WebOrders

```

Rowtime generation. The rowtime of a row emitted from streaming UNION ALL is the same as the
timestamp of the input row.

Rowtime bounds: A rowtime bound is an assertion about the future contents of a stream. It
states that the next row in the stream will have a ROWTIME no earlier than the value of the
bound. For example, if a rowtime bound is 2018-12-0223:23:07, this tells the system that the
next row will arrive no earlier than 2018-12-0223:23:07. Rowtime bounds are useful in managing
gaps in data flow, such as those left overnight on a stock exchange.

Amazon Kinesis Data Analytics ensures that the ROWTIME column is ascending by merging the incoming rows on the
basis of the time stamp. If the first set has rows that are timestamped 10:00 and 10:30, and
the second set has only reached 10:15, Kinesis Data Analytics pauses the first set and waits for the
second set to reach 10:30. In this case, it would be advantageous if the producer of the
second set were to send a rowtime bound.

## VALUES operator

The VALUES operator expresses a constant relation in a query. (See also the discussion of
VALUES in the topic SELECT in this guide.)

VALUES can be used as a top-level query, as follows:

```
VALUES 1 + 2 > 3;
EXPR$0
======
FALSE
VALUES
    (42, 'Fred'),
    (34, 'Wilma');
EXPR$0 EXPR$1
====== ======
    42 Fred
    34 Wilma

```

Note that the system has generated arbitrary column names for anonymous expressions. You can
assign column names by putting VALUES into a subquery and using an AS clause:

```
SELECT *
FROM (
    VALUES
        (42, 'Fred'),
        (34, 'Wilma')) AS t (age, name);
AGE NAME
=== =====
 42 Fred
 34 Wilma
```
