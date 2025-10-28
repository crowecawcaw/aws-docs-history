Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LAST_VALUE window function

Given an ordered set of rows,
The LAST_VALUE function
returns the value of the expression with respect to the last row in the frame.

For information about selecting the first row in the frame, see [FIRST_VALUE window function](r_WF_first_value.md "r_WF_first_value.md") .

## Syntax

```
LAST_VALUE( *expression* )[ IGNORE NULLS | RESPECT NULLS ]
OVER (
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list* *frame\_clause* ]
)
```

## Arguments

_expression_

The target column or expression that the function operates on.

IGNORE NULLS

The function returns the last value in
the frame that is not NULL (or NULL if all values are NULL).

RESPECT NULLS

Indicates that Amazon Redshift should include null values in the determination
of which row to use. RESPECT NULLS is supported by default if you do not
specify IGNORE NULLS.

OVER

Introduces the window clauses for the function.

PARTITION BY _expr_list_

Defines the window for the function in terms of one or more expressions.

ORDER BY _order_list_

Sorts the rows within each partition. If no PARTITION BY clause is
specified, ORDER BY sorts the entire table. If you specify an ORDER BY
clause, you must also specify a _frame_clause_.

The results depend on the
ordering of the data. The results are nondeterministic in the following
cases:

- When no ORDER BY clause is specified and a partition contains two
  different values for an expression
- When the expression evaluates to different values that correspond
  to the same value in the ORDER BY list.

_frame_clause_

If an ORDER BY clause is used for an aggregate function, an explicit
frame clause is required. The frame clause refines the set of rows in a
function's window, including or excluding sets of rows in the ordered
result. The frame clause consists of the ROWS keyword and associated
specifiers. See [Window function syntax summary](c_Window_functions.md#r_Window_function_synopsis "c_Window_functions.md#r_Window_function_synopsis").

## Return type

These functions support expressions that use primitive Amazon Redshift data types. The
return type is the same as the data type of the _expression_.

## Examples

The following examples use the VENUE table from the sample TICKIT data.
For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

The following example returns the seating capacity for each venue in the VENUE
table, with the results ordered by capacity (high to low). The LAST_VALUE function
is used to select the name of the venue that corresponds to the last row in the
frame: in this case, the row with the least number of seats. The results are
partitioned by state, so when the VENUESTATE value changes, a new last value is
selected. The window frame is unbounded so the same last value is selected for each
row in each partition.

For California, `Shoreline Amphitheatre` is returned for every row in the partition because it has the
lowest number of seats (`22000`).

```
`select venuestate, venueseats, venuename,
last_value(venuename)
over(partition by venuestate
order by venueseats desc
rows between unbounded preceding and unbounded following)
from (select * from venue where venueseats >0)
order by venuestate;`
`venuestate | venueseats | venuename | last_value
-----------+------------+--------------------------------+------------------------------
CA | 70561 | Qualcomm Stadium | Shoreline Amphitheatre
CA | 69843 | Monster Park | Shoreline Amphitheatre
CA | 63026 | McAfee Coliseum | Shoreline Amphitheatre
CA | 56000 | Dodger Stadium | Shoreline Amphitheatre
CA | 45050 | Angel Stadium of Anaheim | Shoreline Amphitheatre
CA | 42445 | PETCO Park | Shoreline Amphitheatre
CA | 41503 | AT&T Park | Shoreline Amphitheatre
CA | 22000 | Shoreline Amphitheatre | Shoreline Amphitheatre
CO | 76125 | INVESCO Field | Coors Field
CO | 50445 | Coors Field | Coors Field
DC | 41888 | Nationals Park | Nationals Park
FL | 74916 | Dolphin Stadium | Tropicana Field
FL | 73800 | Jacksonville Municipal Stadium | Tropicana Field
FL | 65647 | Raymond James Stadium | Tropicana Field
FL | 36048 | Tropicana Field | Tropicana Field
...`
```
