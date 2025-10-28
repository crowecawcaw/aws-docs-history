# FIRST_VALUE window function

Given an ordered set of rows, FIRST_VALUE returns the value of the specified expression
with respect to the first row in the window frame.

For information about selecting the last row in the frame, see [LAST_VALUE window function](WF_last_value.md "WF_last_value.md") .

## Syntax

```
FIRST_VALUE( *expression* )[ IGNORE NULLS | RESPECT NULLS ]
OVER (
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list* *frame\_clause* ]
)
```

## Arguments

_expression_

The target column or expression that the function operates on.

IGNORE NULLS

When this option is used with FIRST_VALUE, the function returns the first
value in the frame that is not NULL (or NULL if all values are NULL).

RESPECT NULLS

Indicates that AWS Clean Rooms should include null values in the determination of
which row to use. RESPECT NULLS is supported by default if you do not specify
IGNORE NULLS.

OVER

Introduces the window clauses for the function.

PARTITION BY _expr_list_

Defines the window for the function in terms of one or more expressions.

ORDER BY _order_list_

Sorts the rows within each partition. If no PARTITION BY clause is
specified, ORDER BY sorts the entire table. If you specify an ORDER BY clause,
you must also specify a _frame_clause_.

The results of the FIRST_VALUE function depends on the ordering of the data.
The results are nondeterministic in the following cases:

- When no ORDER BY clause is specified and a partition contains two
  different values for an expression
- When the expression evaluates to different values that correspond to
  the same value in the ORDER BY list.

_frame_clause_

If an ORDER BY clause is used for an aggregate function, an explicit frame
clause is required. The frame clause refines the set of rows in a function's
window, including or excluding sets of rows in the ordered result. The frame
clause consists of the ROWS keyword and associated specifiers. See [Window function syntax summary](Window_functions.md#Window_function_synopsis "Window_functions.md#Window_function_synopsis").

## Return type

These functions support expressions that use primitive AWS Clean Rooms data types. The return
type is the same as the data type of the _expression_.

## Examples

The following example returns the seating capacity for each venue in the VENUE table,
with the results ordered by capacity (high to low). The FIRST_VALUE function is used to
select the name of the venue that corresponds to the first row in the frame: in this
case, the row with the highest number of seats. The results are partitioned by state, so
when the VENUESTATE value changes, a new first value is selected. The window frame is
unbounded so the same first value is selected for each row in each partition.

For California, `Qualcomm Stadium` has the highest number of seats
(`70561`), so this name is the first value for all of the rows in the
`CA` partition.

```
`select venuestate, venueseats, venuename,
first_value(venuename)
over(partition by venuestate
order by venueseats desc
rows between unbounded preceding and unbounded following)
from (select * from venue where venueseats >0)
order by venuestate;`
`venuestate | venueseats | venuename | first_value
-----------+------------+--------------------------------+------------------------------
CA | 70561 | Qualcomm Stadium | Qualcomm Stadium
CA | 69843 | Monster Park | Qualcomm Stadium
CA | 63026 | McAfee Coliseum | Qualcomm Stadium
CA | 56000 | Dodger Stadium | Qualcomm Stadium
CA | 45050 | Angel Stadium of Anaheim | Qualcomm Stadium
CA | 42445 | PETCO Park | Qualcomm Stadium
CA | 41503 | AT&T Park | Qualcomm Stadium
CA | 22000 | Shoreline Amphitheatre | Qualcomm Stadium
CO | 76125 | INVESCO Field | INVESCO Field
CO | 50445 | Coors Field | INVESCO Field
DC | 41888 | Nationals Park | Nationals Park
FL | 74916 | Dolphin Stadium | Dolphin Stadium
FL | 73800 | Jacksonville Municipal Stadium | Dolphin Stadium
FL | 65647 | Raymond James Stadium | Dolphin Stadium
FL | 36048 | Tropicana Field | Dolphin Stadium
...`
```
