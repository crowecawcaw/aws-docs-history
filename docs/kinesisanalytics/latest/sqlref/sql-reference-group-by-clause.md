# GROUP BY clause

## Syntax Chart for the GROUP BY Clause

(To see where this clause fits, see [SELECT statement](sql-reference-select.md "sql-reference-select.md"))

For example, GROUP BY <column name-or-expression>, where:

- the expression can be an aggregate; and,
- any column name used in the GROUP BY clause must also be in the SELECT statement.
  Additionally, a column that is not named in or derivable from the GROUP BY clause cannot appear
  in the SELECT statement except within aggregations, such as SUM (allOrdersValue).

What derivable means is that a column specified in the GROUP BY clause enables access to the column you want to
include in the SELECT clause. If a column is derivable, the SELECT statement can specify it even though it is not
explicitly named in the GROUP BY clause.

Example: If the key to a table is in the GROUP BY clause, then
any of that table's columns can appear in the select-list because, given that key, such columns are considered accessible.

The GROUP BY clause groups selected rows based on the value of the grouping expressions, returning a single summary row
of information for each group of rows that have identical values in all columns.

Note that for these purposes, the value NULL is considered equal to itself and not equal to any other value.
These are the same semantics as for the IS NOT DISTINCT FROM operator.

## Streaming GROUP BY

GROUP BY can be used in a streaming query as long
as one of the grouping expressions is a non-constant monotonic or time-based expression. This requirement is necessary in order for Amazon Kinesis Data Analytics to make progress, as explained below.

A monotonic expression is one that always moves in the same direction: it either ascends-or-stays-the-same,
or it descends-or-stays the same; it doesn't reverse direction. It does not need to be strictly ascending or strictly descending,
that is, every value always above the previous one or every value always below the previous one.
A constant expression falls under the definition of monotonic -- it is technically both ascending and descending
-- but is clearly unsuitable for these purposes. For more information about monotonicity, see
[Monotonic Expressions and Operators](sql-reference-monotonic-expressions-operators.md "sql-reference-monotonic-expressions-operators.md").

Consider the following query:

```
SELECT STREAM prodId, COUNT(*)
FROM Orders
GROUP BY prodId

```

The query is intended to compute the number of orders for each product, as a stream. However, since Orders is an infinite stream, Amazon Kinesis Data Analytics
can never know that it has seen all orders for a given product, can never complete a particular row's total, and therefore can never output a row. Rather than allow a
query that can never emit a row, the Amazon Kinesis Data Analytics validator rejects the query.

The syntax for streaming GROUP BY is as follows:

`GROUP BY <monotonic 
 or time-based expression> ,`

`<column name-or-expression, ...>`

where any column name used in the GROUP BY clause needs to be in the SELECT statement; the expression can be an aggregate. Additionally, a column name that does not
appear in the GROUP BY clause cannot appear in the SELECT statement except within aggregations, or if, as above,
access to the column can be created from column that you specify in the GROUP BY clause.

For example, the following query, which computes the product counts per hour,
uses the monotonic expression FLOOR(Orders.ROWTIME TO HOUR) is therefore valid:

```
SELECT STREAM FLOOR(Orders.ROWTIME TO HOUR) AS theHour, prodId, COUNT(*)
FROM Orders
GROUP BY FLOOR(Orders.ROWTIME TO HOUR), prodId

```

One of the expressions in the GROUP BY must be monotonic or time-based. For example GROUP BY FLOOR(S.ROWTIME) TO HOUR will yield one output row per hour for the previous
hour's input rows. The GROUP BY can specify additional partitioning terms. For example, GROUP BY FLOOR(S.ROWTIME) TO HOUR, USERID will yield one output row per hour per USERID
value. If you know for a fact that an expression is monotonic, you can declare it so by using the
[Monotonic Function](sql-reference-monotonic.md "sql-reference-monotonic.md"). If the actual data are not monotonic, the resulting system behavior is indeterminate: results
may not be as expected or desired.

See the topic [Monotonic Function](sql-reference-monotonic.md "sql-reference-monotonic.md") in this guide for more details.

Duplicate rowtimes can occur in a stream, and as long as the ROWTIME value is the same, the GROUP BY operation will keep accumulating rows. In order to emit a row, the
ROWTIME value has to change at some point.
