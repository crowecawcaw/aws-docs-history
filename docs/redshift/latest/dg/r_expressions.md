Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Expressions

###### Topics

- [Simple expressions](#r_expressions-simple-expressions "#r_expressions-simple-expressions")
- [Compound expressions](r_compound_expressions.md "r_compound_expressions.md")
- [Expression lists](r_expression_lists.md "r_expression_lists.md")
- [Scalar subqueries](r_scalar_subqueries.md "r_scalar_subqueries.md")
- [Function expressions](r_function_expressions.md "r_function_expressions.md")
  An expression is a combination of one or more values, operators, or functions that
  evaluate to a value. The data type of an expression is generally that of its components.

## Simple expressions

A simple expression is one of the following:

- A constant or literal value
- A column name or column reference
- A scalar function
- An aggregate (set) function
- A window function
- A scalar subquery

Examples of simple expressions include:

```
5+12
dateid
sales.qtysold * 100
sqrt (4)
max (qtysold)
(select max (qtysold) from sales)
```
