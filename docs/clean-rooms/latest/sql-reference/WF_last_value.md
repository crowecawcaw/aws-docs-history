

# LAST\_VALUE window function
<a name="WF_last_value"></a>

 Given an ordered set of rows, The LAST\_VALUE function returns the value of the expression with respect to the last row in the frame. 

For information about selecting the first row in the frame, see [FIRST\_VALUE window function](WF_first_value.md) .

## Syntax
<a name="WF_last_value-synopsis"></a>

```
LAST_VALUE( expression )[ IGNORE NULLS | RESPECT NULLS ]
OVER (
[ PARTITION BY expr_list ]
[ ORDER BY order_list frame_clause ]
)
```

## Arguments
<a name="WF_last_value-arguments"></a>

 *expression*   
 The target column or expression that the function operates on. 

IGNORE NULLS   
The function returns the last value in the frame that is not NULL (or NULL if all values are NULL). 

RESPECT NULLS   
Indicates that AWS Clean Rooms should include null values in the determination of which row to use. RESPECT NULLS is supported by default if you do not specify IGNORE NULLS. 

OVER   
Introduces the window clauses for the function. 

PARTITION BY *expr\_list*   
Defines the window for the function in terms of one or more expressions. 

ORDER BY *order\_list*   
Sorts the rows within each partition. If no PARTITION BY clause is specified, ORDER BY sorts the entire table. If you specify an ORDER BY clause, you must also specify a *frame\_clause*.   
The results depend on the ordering of the data. The results are nondeterministic in the following cases:   
+ When no ORDER BY clause is specified and a partition contains two different values for an expression 
+ When the expression evaluates to different values that correspond to the same value in the ORDER BY list. 

 *frame\_clause*   
If an ORDER BY clause is used for an aggregate function, an explicit frame clause is required. The frame clause refines the set of rows in a function's window, including or excluding sets of rows in the ordered result. The frame clause consists of the ROWS keyword and associated specifiers. See [Window function syntax summary](Window_functions.md#Window_function_synopsis). 

## Return type
<a name="Supported_data_types_wf_last_value"></a>

These functions support expressions that use primitive AWS Clean Rooms data types. The return type is the same as the data type of the *expression*.

## Examples
<a name="WF_last_value-examples"></a>

The following example returns the seating capacity for each venue in the VENUE table, with the results ordered by capacity (high to low). The LAST\_VALUE function is used to select the name of the venue that corresponds to the last row in the frame: in this case, the row with the least number of seats. The results are partitioned by state, so when the VENUESTATE value changes, a new last value is selected. The window frame is unbounded so the same last value is selected for each row in each partition. 

For California, `Shoreline Amphitheatre` is returned for every row in the partition because it has the lowest number of seats (`22000`). 

```
select venuestate, venueseats, venuename,
last_value(venuename)
over(partition by venuestate
order by venueseats desc
rows between unbounded preceding and unbounded following)
from (select * from venue where venueseats >0)
order by venuestate;

venuestate | venueseats |           venuename            |          last_value
-----------+------------+--------------------------------+------------------------------
CA         |      70561 | Qualcomm Stadium               | Shoreline Amphitheatre
CA         |      69843 | Monster Park                   | Shoreline Amphitheatre
CA         |      63026 | McAfee Coliseum                | Shoreline Amphitheatre
CA         |      56000 | Dodger Stadium                 | Shoreline Amphitheatre
CA         |      45050 | Angel Stadium of Anaheim       | Shoreline Amphitheatre
CA         |      42445 | PETCO Park                     | Shoreline Amphitheatre
CA         |      41503 | AT&T Park                      | Shoreline Amphitheatre
CA         |      22000 | Shoreline Amphitheatre         | Shoreline Amphitheatre
CO         |      76125 | INVESCO Field                  | Coors Field
CO         |      50445 | Coors Field                    | Coors Field
DC         |      41888 | Nationals Park                 | Nationals Park
FL         |      74916 | Dolphin Stadium                | Tropicana Field
FL         |      73800 | Jacksonville Municipal Stadium | Tropicana Field
FL         |      65647 | Raymond James Stadium          | Tropicana Field
FL         |      36048 | Tropicana Field                | Tropicana Field
...
```