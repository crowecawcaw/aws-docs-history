Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DENSE_RANK window function

The DENSE_RANK window function determines the rank of a value in a group of values,
based on the ORDER BY expression in the OVER clause. If the optional PARTITION BY clause
is present, the rankings are reset for each group of rows. Rows with equal values for
the ranking criteria receive the same rank. The DENSE_RANK function differs from RANK in
one respect: if two or more rows tie, there is no gap in the sequence of ranked values.
For example, if two rows are ranked `1`, the next rank is `2`.

You can have ranking functions with different PARTITION BY and ORDER BY clauses in
the same query.

## Syntax

```
DENSE_RANK() OVER
(
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list* ]
)
```

## Arguments

( )

The function takes no arguments, but the empty parentheses are required.

OVER

The window clauses for the DENSE_RANK function.

PARTITION BY _expr_list_

(Optional) One or more expressions that define the window.

ORDER BY _order_list_

(Optional) The expression on which the ranking values are based. If no
PARTITION BY is specified, ORDER BY uses the entire table. If ORDER BY is
omitted, the return value is `1` for all rows.

If ORDER BY doesn't produce a unique ordering, the order of the rows
is nondeterministic. For more information, see [Unique ordering of data for window
functions](c_Window_functions.md#r_Examples_order_by_WF "c_Window_functions.md#r_Examples_order_by_WF").

## Return type

`BIGINT`

## Examples

The following examples use the sample table for window functions. For more information, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

The following example orders the table by the quantity sold and assigns both a
dense rank and a regular rank to each row. The results are sorted after the window
function results are applied.

````
`SELECT salesid, qty,
DENSE_RANK() OVER(ORDER BY qty DESC) AS d_rnk,
RANK() OVER(ORDER BY qty DESC) AS rnk
FROM winsales
ORDER BY 2,1;`

`+---------+-----+-------+-----+
| salesid | qty | d_rnk | rnk | +---------+-----+-------+-----+
| 10001 | 10 | 5 | 8 |
| 10006 | 10 | 5 | 8 |
| 30001 | 10 | 5 | 8 |
| 40005 | 10 | 5 | 8 |
| 30003 | 15 | 4 | 7 |
| 20001 | 20 | 3 | 4 |
| 20002 | 20 | 3 | 4 |
| 30004 | 20 | 3 | 4 |
| 10005 | 30 | 2 | 2 |
| 30007 | 30 | 2 | 2 |
| 40001 | 40 | 1 | 1 | +---------+-----+-------+-----+` ``` Note the difference in rankings assigned to the same set of rows when the DENSE\_RANK and RANK functions are used side by side in the same query. The following example partitions the table by sellerid, orders each partition by the quantity, and assigns a dense rank to each row. The results are sorted after the window function results are applied. ``` `SELECT salesid, sellerid, qty, DENSE_RANK() OVER(PARTITION BY sellerid ORDER BY qty DESC) AS d_rnk FROM winsales ORDER BY 2,3,1;` `+---------+----------+-----+-------+
| salesid | sellerid | qty | d_rnk | +---------+----------+-----+-------+
| 10001 | 1 | 10 | 2 |
| 10006 | 1 | 10 | 2 |
| 10005 | 1 | 30 | 1 |
| 20001 | 2 | 20 | 1 |
| 20002 | 2 | 20 | 1 |
| 30001 | 3 | 10 | 4 |
| 30003 | 3 | 15 | 3 |
| 30004 | 3 | 20 | 2 |
| 30007 | 3 | 30 | 1 |
| 40005 | 4 | 10 | 2 |
| 40001 | 4 | 40 | 1 | +---------+----------+-----+-------+` ``` To successfully use the last example, use the following command to insert a row into the WINSALES table. This row has the same buyerid, sellerid, and qtysold as another row. This will cause two rows to tie in the last example and thus will show the difference between the DENSE\_RANK and RANK functions. ``` `INSERT INTO winsales VALUES(30009, '2/2/2003', 3, 'b', 20, NULL);` ``` The following example partitions the table by buyerid and sellerid, orders each partition by the quantity, and assigns both a dense rank and a regular rank to each row. The results are sorted after the window function is applied. ``` `SELECT salesid, sellerid, qty, buyerid, DENSE_RANK() OVER(PARTITION BY buyerid, sellerid ORDER BY qty DESC) AS d_rnk, RANK() OVER (PARTITION BY buyerid, sellerid ORDER BY qty DESC) AS rnk FROM winsales ORDER BY rnk;` `+---------+----------+-----+---------+-------+-----+
| salesid | sellerid | qty | buyerid | d_rnk | rnk | +---------+----------+-----+---------+-------+-----+
| 20001 | 2 | 20 | b | 1 | 1 |
| 30007 | 3 | 30 | c | 1 | 1 |
| 10006 | 1 | 10 | c | 1 | 1 |
| 10005 | 1 | 30 | a | 1 | 1 |
| 20002 | 2 | 20 | c | 1 | 1 |
| 30009 | 3 | 20 | b | 1 | 1 |
| 40001 | 4 | 40 | a | 1 | 1 |
| 30004 | 3 | 20 | b | 1 | 1 |
| 10001 | 1 | 10 | c | 1 | 1 |
| 40005 | 4 | 10 | a | 2 | 2 |
| 30003 | 3 | 15 | b | 2 | 3 |
| 30001 | 3 | 10 | b | 3 | 4 | +---------+----------+-----+---------+-------+-----+` ```
````
