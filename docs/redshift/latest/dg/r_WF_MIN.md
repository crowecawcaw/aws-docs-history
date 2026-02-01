Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MIN window function

The MIN window function returns the minimum of the input expression values. The MIN
function works with numeric values and ignores NULL values.

## Syntax

```
MIN ( [ ALL ] *expression* ) OVER
(
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list* *frame\_clause* ]
)
```

## Arguments

_expression_

The target column or expression that the function operates on.

ALL

With the argument ALL, the function retains all duplicate values from the
expression. ALL is the default. DISTINCT is not supported.

OVER

Specifies the window clauses for the aggregation functions. The OVER
clause distinguishes window aggregation functions from normal set
aggregation functions.

PARTITION BY _expr_list_

Defines the window for the MIN function in terms of one or more
expressions.

ORDER BY _order_list_

Sorts the rows within each partition. If no PARTITION BY is specified,
ORDER BY uses the entire table.

_frame_clause_

If an ORDER BY clause is used for an aggregate function, an explicit
frame clause is required. The frame clause refines the set of rows in a
function's window, including or excluding sets of rows within the ordered
result. The frame clause consists of the ROWS keyword and associated
specifiers. See [Window function syntax summary](c_Window_functions.md#r_Window_function_synopsis "c_Window_functions.md#r_Window_function_synopsis").

## Data types

Accepts any data type as input. Returns the same data type as
_expression_.

## Examples

The following example shows the sales ID, quantity, and minimum quantity from the beginning of the data
window:

```
select salesid, qty,
min(qty) over
(order by salesid rows unbounded preceding)
from winsales
order by salesid;

salesid | qty | min
---------+-----+-----
10001 |  10 |  10
10005 |  30 |  10
10006 |  10 |  10
20001 |  20 |  10
20002 |  20 |  10
30001 |  10 |  10
30003 |  15 |  10
30004 |  20 |  10
30007 |  30 |  10
40001 |  40 |  10
40005 |  10 |  10
(11 rows)
```

For a description of the WINSALES table, see [Sample table for window function examples](c_Window_functions.md#r_Window_function_example "c_Window_functions.md#r_Window_function_example").

The following example shows the sales ID, quantity, and minimum quantity in a
restricted frame:

```
select salesid, qty,
min(qty) over
(order by salesid rows between 2 preceding and 1 preceding) as min
from winsales
order by salesid;

salesid | qty | min
---------+-----+-----
10001 |  10 |
10005 |  30 |  10
10006 |  10 |  10
20001 |  20 |  10
20002 |  20 |  10
30001 |  10 |  20
30003 |  15 |  10
30004 |  20 |  10
30007 |  30 |  15
40001 |  40 |  20
40005 |  10 |  30
(11 rows)
```
