Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ROW_NUMBER window function

Assigns an ordinal number of the current row within a group of rows, counting
from 1, based on the ORDER BY expression in the OVER clause. If the optional PARTITION
BY clause is present, the ordinal numbers are reset for each group of rows. Rows with
equal values for the ORDER BY expressions receive the different row numbers
nondeterministically.

## Syntax

```
ROW_NUMBER() OVER(
  [ PARTITION BY *expr\_list* ]
  [ ORDER BY *order\_list* ]
)
```

## Arguments

( )

The function takes no arguments, but the empty parentheses are required.

OVER

The window function clause for the ROW_NUMBER function.

PARTITION BY _expr_list_

Optional. One or more column expressions that divide the results into sets of rows.

ORDER BY _order_list_

Optional. One or more column expressions that defines the order of rows within a set.
If no PARTITION BY is specified, ORDER BY uses the entire table.

If ORDER BY does not produce a unique ordering or is omitted, the order of the rows is
nondeterministic. For more information, see [Unique ordering of data for window
functions](c_Window_functions.md#r_Examples_order_by_WF "c_Window_functions.md#r_Examples_order_by_WF").

## Return type

BIGINT

## Examples

The following examples use the `WINSALES` table. For a description of the `WINSALES` table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

The following example orders the table
by QTY (in ascending order), then assigns a row number to each row. The results are
sorted after the window function results are applied.

```
`SELECT salesid, sellerid, qty,
ROW_NUMBER() OVER(
 ORDER BY qty ASC) AS row
FROM winsales
ORDER BY 4,1;`
`salesid sellerid qty row
---------+----------+-----+-----
 30001 | 3 | 10 | 1
 10001 | 1 | 10 | 2
 10006 | 1 | 10 | 3
 40005 | 4 | 10 | 4
 30003 | 3 | 15 | 5
 20001 | 2 | 20 | 6
 20002 | 2 | 20 | 7
 30004 | 3 | 20 | 8
 10005 | 1 | 30 | 9
 30007 | 3 | 30 | 10
 40001 | 4 | 40 | 11`
```

The following example partitions the table by SELLERID and orders each partition
by QTY (in ascending order), then assigns a row number to each row. The results are
sorted after the window function results are applied.

```
`SELECT salesid, sellerid, qty,
ROW_NUMBER() OVER(
 PARTITION BY sellerid
 ORDER BY qty ASC) AS row_by_seller
FROM winsales
ORDER BY 2,4;`
`salesid | sellerid | qty | row_by_seller
---------+----------+-----+-----
 10001 | 1 | 10 | 1
 10006 | 1 | 10 | 2
 10005 | 1 | 30 | 3
 20001 | 2 | 20 | 1
 20002 | 2 | 20 | 2
 30001 | 3 | 10 | 1
 30003 | 3 | 15 | 2
 30004 | 3 | 20 | 3
 30007 | 3 | 30 | 4
 40005 | 4 | 10 | 1
 40001 | 4 | 40 | 2`
```

The following example shows the results when not using the optional clauses.

```
`SELECT salesid, sellerid, qty, ROW_NUMBER() OVER() AS row
FROM winsales
ORDER BY 4,1;`
`salesid sellerid qty row
---------+----------+-----+-----
 30001 | 3 | 10 | 1
 10001 | 1 | 10 | 2
 10005 | 1 | 30 | 3
 40001 | 4 | 40 | 4
 10006 | 1 | 10 | 5
 20001 | 2 | 20 | 6
 40005 | 4 | 10 | 7
 20002 | 2 | 20 | 8
 30003 | 3 | 15 | 9
 30004 | 3 | 20 | 10
 30007 | 3 | 30 | 11`
```
