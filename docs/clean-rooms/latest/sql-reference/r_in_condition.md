# IN condition

An IN condition tests a value for membership in a set of values or in a
subquery.

## Syntax

```
*expression* [ NOT ] IN (*expr\_list* | *table\_subquery*)
```

## Arguments

_expression_

A numeric, character, or datetime expression that is evaluated against
the _expr_list_ or _table_subquery_
and must be compatible with the data type of that list or subquery.

_expr_list_

One or more comma-delimited expressions, or one or more sets of
comma-delimited expressions bounded by parentheses.

_table_subquery_

A subquery that evaluates to a table with one or more rows, but is
limited to only one column in its select list.

IN | NOT IN

IN returns true if the expression is a member of the expression list
or query. NOT IN returns true if the expression is not a member. IN and
NOT IN return NULL and no rows are returned in the following cases: If
_expression_ yields null; or if there are no
matching _expr_list_ or
_table_subquery_ values and at least one of these
comparison rows yields null.

## Examples

The following conditions are true only for those values listed:

```
qtysold in (2, 4, 5)
date.day in ('Mon', 'Tues')
date.month not in ('Oct', 'Nov', 'Dec')
```

## Optimization for

Large IN Lists

To optimize query performance, an IN list that includes more than 10 values is
internally evaluated as a scalar array. IN lists with fewer than 10 values are
evaluated as a series of OR predicates. This optimization is supported for
SMALLINT, INTEGER, BIGINT, REAL, DOUBLE PRECISION, BOOLEAN, CHAR, VARCHAR, DATE, TIMESTAMP, and TIMESTAMPTZ data types.

Look at the EXPLAIN output for the query to see the effect of this
optimization. For example:

```
explain select * from sales
QUERY PLAN
--------------------------------------------------------------------
XN Seq Scan on sales  (cost=0.00..6035.96 rows=86228 width=53)
Filter: (salesid = ANY ('{1,2,3,4,5,6,7,8,9,10,11}'::integer[]))
(2 rows)
```
