Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# VAR_SAMP and VAR_POP window functions

The VAR_SAMP and VAR_POP window functions return the sample and population variance
of a set of numeric values (integer, decimal, or floating-point). See also [VAR_SAMP and VAR_POP functions](r_VARIANCE_functions.md "r_VARIANCE_functions.md").

VAR_SAMP and VARIANCE are synonyms for the same function.

## Syntax

```
VAR_SAMP | VARIANCE | VAR_POP
( [ ALL ] *expression* ) OVER
(
[ PARTITION BY *expr\_list* ]
[ ORDER BY *order\_list*
                        *frame\_clause* ]
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

Defines the window for the function in terms of one or more expressions.

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

The argument types supported by the VARIANCE functions are SMALLINT, INTEGER,
BIGINT, NUMERIC, DECIMAL, REAL, and DOUBLE PRECISION.

Regardless of the data type of the expression, the return type of a VARIANCE
function is a double precision number.
