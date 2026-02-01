Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# BOOL_OR function

The BOOL_OR function operates on a single Boolean or integer column or expression.
This function applies similar logic to the BIT_AND and BIT_OR functions. For this
function, the return type is a Boolean value (`true`,
`false`, or `NULL`).

If one or more values in a set is `true`, the BOOL_OR function returns
`true` (`t`). If all values in a set are `false`,
the function returns `false` (`f`). NULL can be returned if the value is unknown.

## Syntax

```
BOOL_OR ( [DISTINCT | ALL] *expression* )
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
See [DISTINCT support for
bit-wise aggregations](c_bitwise_aggregate_functions.md#distinct-support-for-bit-wise-aggregations "c_bitwise_aggregate_functions.md#distinct-support-for-bit-wise-aggregations").

## Examples

You can use the Boolean functions with either Boolean expressions or integer
expressions. For example, the following query return results from the standard USERS
table in the TICKIT database, which has several Boolean columns.

The BOOL_OR function returns
`true` for all five rows. At least one user in each of those states likes
sports.

```
select state, bool_or(likesports) from users
group by state order by state limit 5;

state | bool_or
------+--------
AB    | t
AK    | t
AL    | t
AZ    | t
BC    | t
(5 rows)
```

The following example returns NULL.

```
`SELECT BOOL_OR(NULL = '123')`
               `bool_or
------
NULL`
```
