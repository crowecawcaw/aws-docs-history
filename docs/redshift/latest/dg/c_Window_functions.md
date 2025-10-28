Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Window functions

By using window functions, you can create analytic business queries
more efficiently. Window functions operate on a partition or "window" of a result set, and
return a value for every row in that window. In contrast, non-windowed functions perform
their calculations with respect to every row in the result set. Unlike group functions that
aggregate result rows, window functions retain all rows in the table expression.

The values returned are calculated by using values from the sets of rows in that
window. For each row in the table, the window defines a set of rows that is used to compute
additional attributes. A window is defined using a window specification (the OVER clause),
and is based on three main concepts:

- _Window partitioning,_ which forms groups of rows (PARTITION
  clause)
- _Window ordering_, which defines an order or sequence of rows
  within each partition (ORDER BY clause)
- _Window frames_, which are defined relative to each row to further
  restrict the set of rows (ROWS specification)
  Window functions are the last set of operations performed in a query except for the
  final ORDER BY clause. All joins and all WHERE, GROUP BY, and HAVING clauses are completed
  before the window functions are processed. Therefore, window functions can appear only in
  the select list or ORDER BY clause. You can use multiple window functions within a single
  query with different frame clauses. You can also use window functions in other scalar
  expressions, such as CASE.

Window functions can't be nested. For example, an aggregate function [SUM](r_SUM.md "r_SUM.md")
can appear inside a window function [SUM](r_WF_SUM.md "r_WF_SUM.md"),
but a window function SUM can't appear inside another window function SUM.
The following is not supported because a window function is nested in another window function.

```
SELECT SUM(SUM(selectcol) OVER (PARTITION BY ordercol)) OVER (Partition by ordercol) FROM t;
```

## Window function syntax summary

Window functions follow a standard syntax, which is as follows.

```
*function* (*expression*) OVER (
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list* [ *frame\_clause* ] ] )
```

Here, _function_ is one of the functions described in this
section.

The _expr_list_ is as follows.

```
*expression* | *column\_name* [, *expr\_list* ]
```

The _order_list_ is as follows.

```
*expression* | *column\_name* [ ASC | DESC ]
[ NULLS FIRST | NULLS LAST ]
[, *order\_list* ]
```

The _frame_clause_ is as follows.

```
ROWS
{ UNBOUNDED PRECEDING | *unsigned\_value* PRECEDING | CURRENT ROW } |

{ BETWEEN
{ UNBOUNDED PRECEDING | *unsigned\_value* { PRECEDING | FOLLOWING } | CURRENT ROW}
AND
{ UNBOUNDED FOLLOWING | *unsigned\_value* { PRECEDING | FOLLOWING } | CURRENT ROW }}
```

### Arguments

_function_

The window function. For details, see the individual function descriptions.

OVER

The clause that defines the window specification. The OVER clause is
mandatory for window functions, and differentiates window functions from
other SQL functions.

PARTITION BY _expr_list_

(Optional) The PARTITION BY clause subdivides the result set into
partitions, much like the GROUP BY clause. If a partition clause is present,
the function is calculated for the rows in each partition. If no partition
clause is specified, a single partition contains the entire table, and the
function is computed for that complete table.

The ranking functions DENSE_RANK, NTILE, RANK, and ROW_NUMBER require a
global comparison of all the rows in the result set. When a PARTITION BY
clause is used, the query optimizer can run each aggregation in parallel by
spreading the workload across multiple slices according to the partitions.
If the PARTITION BY clause is not present, the aggregation step must be run serially on a single slice, which can have a significant negative
impact on performance, especially for large clusters.

Amazon Redshift doesn't support string literals in PARTITION BY clauses.

ORDER BY _order_list_

(Optional) The window function is applied to the rows within each
partition sorted according to the order specification in ORDER BY. This
ORDER BY clause is distinct from and completely unrelated to ORDER BY
clauses in the _frame_clause_. The ORDER BY
clause can be used without the PARTITION BY clause.

For ranking functions, the ORDER BY clause identifies the measures
for the ranking values. For aggregation functions, the partitioned rows must
be ordered before the aggregate function is computed for each frame. For
more about window function types, see [Window functions](c_Window_functions.md "c_Window_functions.md").

Column identifiers or expressions that evaluate to column identifiers are
required in the order list. Neither constants nor constant expressions can
be used as substitutes for column names.

NULLS values are treated as their own group, sorted and ranked according
to the NULLS FIRST or NULLS LAST option. By default, NULL values are sorted
and ranked last in ASC ordering, and sorted and ranked first in DESC
ordering.

Amazon Redshift doesn't support string literals in ORDER BY clauses.

If the ORDER BY clause is omitted, the order of the rows is
nondeterministic.

###### Note

In any parallel system such as Amazon Redshift, when an ORDER BY clause
doesn't produce a unique and total ordering of the data, the order
of the rows is nondeterministic. That is, if the ORDER BY expression
produces duplicate values (a partial ordering), the return order of those
rows might vary from one run of Amazon Redshift to the next. In turn, window
functions might return unexpected or inconsistent results. For more
information, see [Unique ordering of data for window
functions](#r_Examples_order_by_WF "#r_Examples_order_by_WF").

_column_name_

Name of a column to be partitioned by or ordered by.

ASC | DESC

Option that defines the sort order for the expression, as follows:

- ASC: ascending (for example, low to high for numeric values and 'A'
  to 'Z' for character strings). If no option is specified, data is
  sorted in ascending order by default.
- DESC: descending (high to low for numeric values; 'Z' to 'A' for
  strings).

NULLS FIRST | NULLS LAST

Option that specifies whether NULLS should be ordered first, before
non-null values, or last, after non-null values. By default, NULLS are
sorted and ranked last in ASC ordering, and sorted and ranked first in DESC
ordering.

_frame_clause_

For aggregate functions, the frame clause further refines the set of rows
in a function's window when using ORDER BY. It enables you to include or
exclude sets of rows within the ordered result. The frame clause consists of
the ROWS keyword and associated
specifiers.

The frame clause doesn't apply to ranking functions. Also, the frame
clause isn't required when no ORDER BY clause is used in the OVER clause for
an aggregate function. If an ORDER BY clause is used for an aggregate
function, an explicit frame clause is required.

When no ORDER BY clause is specified, the implied frame is unbounded,
equivalent to ROWS BETWEEN UNBOUNDED PRECEDING AND
UNBOUNDED FOLLOWING.

ROWS

This clause defines the window frame by specifying a
physical offset from the current
row.

This clause specifies the rows in the current window or partition that
the value in the current row is to be combined with. It uses arguments that
specify row position, which can be before or after the current row. The
reference point for all window frames is the current row. Each row becomes
the current row in turn as the window frame slides forward in the
partition.

The frame can be a simple set of rows up to and including the current
row.

```
{UNBOUNDED PRECEDING | *offset* PRECEDING | CURRENT ROW}
```

Or it can be a set of rows between two boundaries.

```
BETWEEN
{ UNBOUNDED PRECEDING | *offset* { PRECEDING | FOLLOWING } | CURRENT ROW }
AND
{ UNBOUNDED FOLLOWING | *offset* { PRECEDING | FOLLOWING } | CURRENT ROW }
```

UNBOUNDED PRECEDING indicates that the window starts at the first row of
the partition; _offset_ PRECEDING indicates that the
window starts a number of rows equivalent to the value of offset before the
current row. UNBOUNDED PRECEDING is the default.

CURRENT ROW indicates the window begins or ends at the current row.

UNBOUNDED FOLLOWING indicates that the window ends at the last row of the
partition; _offset_ FOLLOWING indicates that the window
ends a number of rows equivalent to the value of offset after the current
row.

_offset_ identifies a physical
number of rows before or after the current row. In this case,
_offset_ must be a constant that evaluates to a
positive numeric value. For example, 5 FOLLOWING ends the frame five rows
after the current row.

Where BETWEEN is not specified, the frame is implicitly bounded by the
current row. For example, `ROWS 5 PRECEDING` is equal to
`ROWS BETWEEN 5 PRECEDING AND CURRENT ROW`. Also, `ROWS
 UNBOUNDED FOLLOWING` is equal to `ROWS BETWEEN CURRENT ROW AND
 UNBOUNDED FOLLOWING`.

###### Note

You can't specify a frame in which the starting boundary is
greater than the ending boundary. For example, you can't specify any of
the following frames.

```
between 5 following and 5 preceding
between current row and 2 preceding
between 3 following and current row
```

## Unique ordering of data for window

functions

If an ORDER BY clause for a window function doesn't produce a unique and
total ordering of the data, the order of the rows is nondeterministic. If the ORDER BY
expression produces duplicate values (a partial ordering), the return order of those
rows can vary in multiple runs. In this case, window functions can also return
unexpected or inconsistent results.

For example, the following query returns different results over multiple runs.
These different results occur because `order by dateid` doesn't produce
a unique ordering of the data for the SUM window function.

```
select dateid, pricepaid,
sum(pricepaid) over(order by dateid rows unbounded preceding) as sumpaid
from sales
group by dateid, pricepaid;

dateid | pricepaid |   sumpaid
--------+-----------+-------------
1827 |   1730.00 |     1730.00
1827 |    708.00 |     2438.00
1827 |    234.00 |     2672.00
...

select dateid, pricepaid,
sum(pricepaid) over(order by dateid rows unbounded preceding) as sumpaid
from sales
group by dateid, pricepaid;

dateid | pricepaid |   sumpaid
--------+-----------+-------------
1827 |    234.00 |      234.00
1827 |    472.00 |      706.00
1827 |    347.00 |     1053.00
...
```

In this case, adding a second ORDER BY column to the window function can solve
the problem.

```
select dateid, pricepaid,
sum(pricepaid) over(order by dateid, pricepaid rows unbounded preceding) as sumpaid
from sales
group by dateid, pricepaid;

dateid | pricepaid | sumpaid
--------+-----------+---------
1827 |    234.00 |  234.00
1827 |    337.00 |  571.00
1827 |    347.00 |  918.00
...
```

## Supported functions

Amazon Redshift supports two types of window functions: aggregate and ranking.

Following are the supported aggregate functions:

- [AVG window function](r_WF_AVG.md "r_WF_AVG.md")
- [COUNT window function](r_WF_COUNT.md "r_WF_COUNT.md")
- [CUME_DIST window function](r_WF_CUME_DIST.md "r_WF_CUME_DIST.md")
- [DENSE_RANK window function](r_WF_DENSE_RANK.md "r_WF_DENSE_RANK.md")
- [FIRST_VALUE window function](r_WF_first_value.md "r_WF_first_value.md")
- [LAG window function](r_WF_LAG.md "r_WF_LAG.md")
- [LAST_VALUE window function](r_WF_last_value.md "r_WF_last_value.md")
- [LEAD window function](r_WF_LEAD.md "r_WF_LEAD.md")
- [LISTAGG window function](r_WF_LISTAGG.md "r_WF_LISTAGG.md")
- [MAX window function](r_WF_MAX.md "r_WF_MAX.md")
- [MEDIAN window function](r_WF_MEDIAN.md "r_WF_MEDIAN.md")
- [MIN window function](r_WF_MIN.md "r_WF_MIN.md")
- [NTH_VALUE window function](r_WF_NTH.md "r_WF_NTH.md")
- [PERCENTILE_CONT window function](r_WF_PERCENTILE_CONT.md "r_WF_PERCENTILE_CONT.md")
- [PERCENTILE_DISC window function](r_WF_PERCENTILE_DISC.md "r_WF_PERCENTILE_DISC.md")
- [RATIO_TO_REPORT window function](r_WF_RATIO_TO_REPORT.md "r_WF_RATIO_TO_REPORT.md")
- [STDDEV_SAMP and STDDEV_POP window functions](r_WF_STDDEV.md "r_WF_STDDEV.md") (STDDEV_SAMP and STDDEV are synonyms)
- [SUM window function](r_WF_SUM.md "r_WF_SUM.md")
- [VAR_SAMP and VAR_POP window functions](r_WF_VARIANCE.md "r_WF_VARIANCE.md") (VAR_SAMP and VARIANCE are synonyms)

Following are the supported ranking functions:

- [DENSE_RANK window function](r_WF_DENSE_RANK.md "r_WF_DENSE_RANK.md")
- [NTILE window function](r_WF_NTILE.md "r_WF_NTILE.md")
- [PERCENT_RANK window function](r_WF_PERCENT_RANK.md "r_WF_PERCENT_RANK.md")
- [RANK window function](r_WF_RANK.md "r_WF_RANK.md")
- [ROW_NUMBER window function](r_WF_ROW_NUMBER.md "r_WF_ROW_NUMBER.md")

## Sample table for window function examples

You can find specific window function examples with each function
description. Some of the examples use a table named WINSALES, which contains 11
rows, as shown following.

| SALESID | DATEID     | SELLERID | BUYERID | QTY | QTY_SHIPPED |
| ------- | ---------- | -------- | ------- | --- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 30001   | 8/2/2003   | 3        | B       | 10  | 10          |
| 10001   | 12/24/2003 | 1        | C       | 10  | 10          |
| 10005   | 12/24/2003 | 1        | A       | 30  |             |
| 40001   | 1/9/2004   | 4        | A       | 40  |             |
| 10006   | 1/18/2004  | 1        | C       | 10  |             |
| 20001   | 2/12/2004  | 2        | B       | 20  | 20          |
| 40005   | 2/12/2004  | 4        | A       | 10  | 10          |
| 20002   | 2/16/2004  | 2        | C       | 20  | 20          |
| 30003   | 4/18/2004  | 3        | B       | 15  |             |
| 30004   | 4/18/2004  | 3        | B       | 20  |             |
| 30007   | 9/7/2004   | 3        | C       | 30  |             | The following script creates and populates the sample WINSALES table. `CREATE TABLE winsales( salesid int, dateid date, sellerid int, buyerid char(10), qty int, qty_shipped int); INSERT INTO winsales VALUES (30001, '8/2/2003', 3, 'b', 10, 10), (10001, '12/24/2003', 1, 'c', 10, 10), (10005, '12/24/2003', 1, 'a', 30, null), (40001, '1/9/2004', 4, 'a', 40, null), (10006, '1/18/2004', 1, 'c', 10, null), (20001, '2/12/2004', 2, 'b', 20, 20), (40005, '2/12/2004', 4, 'a', 10, 10), (20002, '2/16/2004', 2, 'c', 20, 20), (30003, '4/18/2004', 3, 'b', 15, null), (30004, '4/18/2004', 3, 'b', 20, null), (30007, '9/7/2004', 3, 'c', 30, null);` |
