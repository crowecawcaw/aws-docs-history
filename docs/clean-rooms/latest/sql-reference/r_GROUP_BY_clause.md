# GROUP BY clause

The GROUP BY clause identifies the grouping columns for the query. Grouping columns must be
declared when the query computes aggregates with standard functions such as SUM, AVG, and COUNT.
If an aggregate function is present in the SELECT expression, any column in the SELECT expression
that is not in an aggregate function must be in the GROUP BY clause.

For more information, see [AWS Clean Rooms SQL functions](sql-functions-topic.md "sql-functions-topic.md").

## Syntax

```
GROUP BY group_by_clause [, ...]

group_by_clause := {
    *expr* |
        ROLLUP ( *expr* [, ...] ) |
        }
```

## _Parameters_

_expr_

The list of columns or expressions must match the list of non-aggregate expressions in
the select list of the query. For example, consider the following simple query.

```
select listid, eventid, sum(pricepaid) as revenue,
count(qtysold) as numtix
from sales
group by listid, eventid
order by 3, 4, 2, 1
limit 5;

listid | eventid | revenue | numtix
-------+---------+---------+--------
89397  |      47 |   20.00 |      1
106590 |      76 |   20.00 |      1
124683 |     393 |   20.00 |      1
103037 |     403 |   20.00 |      1
147685 |     429 |   20.00 |      1
(5 rows)
```

In this query, the select list consists of two aggregate expressions. The first uses the
SUM function and the second uses the COUNT function. The remaining two columns, LISTID and
EVENTID, must be declared as grouping columns.

Expressions in the GROUP BY clause can also reference the select list by using ordinal
numbers. For example, the previous example could be abbreviated as follows.

```
select listid, eventid, sum(pricepaid) as revenue,
count(qtysold) as numtix
from sales
group by 1,2
order by 3, 4, 2, 1
limit 5;

listid | eventid | revenue | numtix
-------+---------+---------+--------
89397  |      47 |   20.00 |      1
106590 |      76 |   20.00 |      1
124683 |     393 |   20.00 |      1
103037 |     403 |   20.00 |      1
147685 |     429 |   20.00 |      1
(5 rows)
```

_ROLLUP_

You can use the aggregation extension ROLLUP to perform the work of multiple GROUP BY
operations in a single statement. For more information on aggregation extensions and related
functions, see [Aggregation extensions](r_GROUP_BY_aggregation-extensions.md "r_GROUP_BY_aggregation-extensions.md").
