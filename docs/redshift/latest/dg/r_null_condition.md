Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Null condition

The null condition tests for nulls, when a value is missing or unknown.

## Syntax

```
*expression* IS [ NOT ] NULL
```

## Arguments

_expression_

Any expression such as a column.

IS NULL

Is true when the expression's value is null and false when it has
a value.

IS NOT NULL

Is false when the expression's value is null and true when it has
a value.

## Example

This example indicates how many times the SALES table contains null in the
QTYSOLD field:

```
select count(*) from sales
where qtysold is null;
count
-------
0
(1 row)
```
