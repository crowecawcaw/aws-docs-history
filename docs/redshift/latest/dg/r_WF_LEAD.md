Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LEAD window function

The LEAD window function returns the values for a row at a given offset below
(after) the current row in the partition.

## Syntax

```
LEAD (*value\_expr* [, *offset* ])
[ IGNORE NULLS | RESPECT NULLS ]
OVER ( [ PARTITION BY *window\_partition* ] ORDER BY *window\_ordering* )
```

## Arguments

_value_expr_

The target column or expression that the function operates on.

_offset_

An optional parameter that specifies the number of rows below the
current row to return values for. The offset can be a constant integer or an
expression that evaluates to an integer. If you do not specify an offset,
Amazon Redshift uses `1` as the default value. An offset of
`0` indicates the current row.

IGNORE NULLS

An optional specification that indicates that Amazon Redshift should skip null
values in the determination of which row to use. Null values are included if
IGNORE NULLS is not listed.

###### Note

You can use an NVL or COALESCE expression to replace the null values
with another value. For more information, see [NVL and COALESCE functions](r_NVL_function.md "r_NVL_function.md").

RESPECT NULLS

Indicates that Amazon Redshift should include null values in the determination
of which row to use. RESPECT NULLS is supported by default if you do not
specify IGNORE NULLS.

OVER

Specifies the window partitioning and ordering. The OVER clause cannot
contain a window frame specification.

PARTITION BY _window_partition_

An optional argument that sets the range of records for each group in the
OVER clause.

ORDER BY _window_ordering_

Sorts the rows within each partition.

The LEAD window function supports expressions that use any of the Amazon Redshift data
types. The return type is the same as the type of the
_value_expr_.

## Examples

The following example provides the commission for events in the SALES table for
which tickets were sold on January 1, 2008 and January 2, 2008 and the commission
paid for ticket sales for the subsequent sale. The following example uses the TICKIT sample database.
For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

```
`SELECT eventid, commission, saletime, LEAD(commission, 1) over ( ORDER BY saletime ) AS next_comm
FROM sales
WHERE saletime BETWEEN '2008-01-09 00:00:00' AND '2008-01-10 12:59:59'
LIMIT 10;`

`+---------+------------+---------------------+-----------+
| eventid | commission | saletime | next_comm |
+---------+------------+---------------------+-----------+
| 1664 | 13.2 | 2008-01-09 01:00:21 | 69.6 |
| 184 | 69.6 | 2008-01-09 01:00:36 | 116.1 |
| 6870 | 116.1 | 2008-01-09 01:02:37 | 11.1 |
| 3718 | 11.1 | 2008-01-09 01:05:19 | 205.5 |
| 6772 | 205.5 | 2008-01-09 01:14:04 | 38.4 |
| 3074 | 38.4 | 2008-01-09 01:26:50 | 209.4 |
| 5254 | 209.4 | 2008-01-09 01:29:16 | 26.4 |
| 3724 | 26.4 | 2008-01-09 01:40:09 | 57.6 |
| 5303 | 57.6 | 2008-01-09 01:40:21 | 51.6 |
| 3678 | 51.6 | 2008-01-09 01:42:54 | 43.8 |
+---------+------------+---------------------+-----------+`
```

The following example provides the maximum difference for the commision for events in the SALES table for
and the commission paid for ticket sales for the subsequent sale for the same event. This example shows how
to use LEAD with a GROUP BY clause. Since window functions aren't allowed in aggregate clauses, this example
uses a subquery. The following example uses
the TICKIT sample database.
For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

```
`SELECT eventid, eventname, max(next_comm_diff) as max_commission_difference
FROM
(
 SELECT sales.eventid, eventname, commission - LEAD(commission, 1) over (ORDER BY sales.eventid, saletime) AS next_comm_diff
 FROM sales JOIN event ON sales.eventid = event.eventid
)
GROUP BY eventid, eventname
ORDER BY eventid

LIMIT 10`

`| eventid | eventname | max_commission_difference |
+---------+-----------------------------+---------------------------+
| 1 | Gotterdammerung | 7.95 |
| 2 | Boris Godunov | 227.85 |
| 3 | Salome | 1350.9 |
| 4 | La Cenerentola (Cinderella) | 790.05 |
| 5 | Il Trovatore | 214.05 |
| 6 | L Elisir d Amore | 510.9 |
| 7 | Doctor Atomic | 180.6 |
| 9 | The Fly | 147 |
| 10 | Rigoletto | 186.6 |
+---------+-----------------------------+---------------------------+`
```
