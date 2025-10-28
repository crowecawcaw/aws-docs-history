Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# BOOL_AND function

The BOOL_AND function operates on a single Boolean or integer column or
expression. This function applies similar logic to the BIT_AND and BIT_OR functions. For
this function, the return type is a Boolean value (`true` or
`false`).

If all values in a set are true, the BOOL_AND function returns
`true` (`t`). If any value is false, the function returns
`false` (`f`).

## Syntax

```
BOOL_AND ( [DISTINCT | ALL] *expression* )
```

## Arguments

_expression_

The target column or expression that the function operates on. This
expression must have a BOOLEAN or integer data type. The return type of the
function is BOOLEAN.

DISTINCT | ALL

With the argument DISTINCT, the function eliminates all duplicate values
for the specified expression before calculating the result. With the
argument ALL, the function retains all duplicate values. ALL is the default.
For more information, see [DISTINCT support for
bit-wise aggregations](c_bitwise_aggregate_functions.md#distinct-support-for-bit-wise-aggregations "c_bitwise_aggregate_functions.md#distinct-support-for-bit-wise-aggregations").

## Examples

You can use the Boolean functions against either Boolean expressions or integer
expressions. For example, the following query return results from the standard USERS
table in the TICKIT database, which has several Boolean columns.

The BOOL_AND function returns
`false` for all five rows. Not all users in each of those states likes
sports.

```
select state, bool_and(likesports) from users
group by state order by state limit 5;

state | bool_and
------+---------
AB    | f
AK    | f
AL    | f
AZ    | f
BC    | f
(5 rows)
```
