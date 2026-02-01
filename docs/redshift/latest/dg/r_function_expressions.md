Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Function expressions

## Syntax

Any built-in can be used as an expression. The syntax for a function call is
the name of a function followed by its argument list in parentheses.

```
*function* ( [*expression* [, *expression*...]] )
```

## Arguments

_function_

Any built-in function. For some example functions, see [SQL functions reference](c_SQL_functions.md "c_SQL_functions.md").

_expression_

Any expression(s) matching the data type and parameter count expected
by the function.

## Examples

```
abs (variable)
select avg (qtysold + 3) from sales;
select dateadd (day,30,caldate) as plus30days from date;
```
