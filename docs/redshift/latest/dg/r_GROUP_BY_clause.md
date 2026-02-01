Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GROUP BY clause

The GROUP BY clause identifies the grouping columns for the query.
It is used to group together those rows in a table that have the same values in all the columns listed.
The order in which the columns are listed does not matter.
The outcome is to combine each set of rows having common values into one group row that represents all rows in the group.
Use a GROUP BY to eliminate redundancy in the output and to compute aggregates that apply to the groups.
Grouping columns must be declared when the query computes aggregates with standard functions such as SUM, AVG, and COUNT.
For more information, see [Aggregate functions](c_Aggregate_Functions.md "c_Aggregate_Functions.md").

## Syntax

```
[ GROUP BY  *expression* [, ...] | ALL | *aggregation\_extension*  ]
```

where _aggregation_extension_ is one of the following:

```
GROUPING SETS ( () | *aggregation\_extension* [, ...] ) |
ROLLUP ( *expr* [, ...] ) |
CUBE ( *expr* [, ...] )

```

## Parameters

_expression_

The list of columns or expressions must match the list of non-aggregate
expressions in the select list of the query. For example, consider the
following simple query.

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

In this query, the select list consists of two aggregate expressions. The first
uses the SUM function and the second uses the COUNT function. The remaining two
columns, LISTID and EVENTID, must be declared as grouping columns.

Expressions in the GROUP BY clause can also reference the select list
by using ordinal numbers. For example, the previous example could be
abbreviated as follows.

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

ALL

ALL indicates to group by all columns specified in the SELECT list except those that are aggregated. For example, consider the
following query which groups by `col1` and `col2`
without having to specify them individually in the GROUP BY clause.
The column `col3` is the argument of the `SUM` function and thus not grouped.

```
SELECT col1, col2 sum(col3) FROM testtable GROUP BY ALL
```

If you EXCLUDE a column in the SELECT list, the GROUP BY ALL clause does not group the results based on that specific column.

```
SELECT * EXCLUDE col3 FROM testtable GROUP BY ALL
```

**aggregation_extension**

You can use the aggregation extensions GROUPING SETS, ROLLUP, and CUBE
to perform the work of multiple GROUP BY operations in a single statement.
For more information on aggregation extensions and related functions, see
[Aggregation extensions](r_GROUP_BY_aggregation-extensions.md "r_GROUP_BY_aggregation-extensions.md").

## Examples

The following examples use the SALES table that contains columns: salesid, listid, sellerid, buyerid, eventid, dateid, qtysold, pricepaid, commission, and saletime.
For more information about the SALES table, see
[Sample database](c_sampledb.md "c_sampledb.md").

The following example query groups by `salesid` and `listid`
without having to specify them individually in the GROUP BY clause.
The column `qtysold` is the argument of the `SUM` function and thus not grouped.

```
`SELECT salesid, listid, sum(qtysold) FROM sales GROUP BY ALL;`
`salesid | listid | sum
--------+---------+------
33095 | 36572 | 2
88268 | 100813 | 4
110917 | 127048 | 1
...`
```

The following example query excludes several columns in the SELECT list, so GROUP BY ALL only groups salesid and listid.

```
`SELECT * EXCLUDE sellerid, buyerid, eventid, dateid, qtysold, pricepaid, commission, saletime
FROM sales GROUP BY ALL;`
`salesid | listid
--------+---------
33095 | 36572
88268 | 100813
110917 | 127048
...`
```
