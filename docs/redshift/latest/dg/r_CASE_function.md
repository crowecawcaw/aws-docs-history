Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CASE conditional expression

The CASE expression is a conditional expression, similar to if/then/else
statements found in other languages. CASE is used to specify a result when there are
multiple conditions. Use CASE where a SQL expression is valid, such as in a SELECT command.

There are two types of CASE expressions: simple and searched.

- In simple CASE expressions, an expression is compared with a value. When a match
  is found, the specified action in the THEN clause is applied. If no match is found,
  the action in the ELSE clause is applied.
- In searched CASE expressions, each CASE is evaluated based on a Boolean
  expression, and the CASE statement returns the first matching CASE. If no match
  is found among the WHEN clauses, the action in the ELSE clause is
  returned.

## Syntax

Simple CASE statement used to match conditions:

```
CASE *expression*
  WHEN *value* THEN *result*
  [WHEN...]
  [ELSE *result*]
END
```

Searched CASE statement used to evaluate each condition:

```
CASE
  WHEN *condition* THEN *result*
  [WHEN ...]
  [ELSE *result*]
END
```

## Arguments

_expression_

A column name or any valid expression.

_value_

Value that the expression is compared with, such as a numeric constant or
a character string.

_result_

The target value or expression that is returned when an expression or
Boolean condition is evaluated.
The data types of all the result expressions must be convertible to a single output type.

_condition_

A Boolean expression that evaluates to true or false.
If _condition_ is true, the value of the CASE expression is the result that follows the condition, and the remainder of the CASE expression is not processed.
If _condition_ is false, any subsequent WHEN clauses are evaluated.
If no WHEN condition results are true, the value of the CASE expression is the result of the ELSE clause.
If the ELSE clause is omitted and no condition is true, the result is null.

## Examples

The following examples use the VENUE table and SALES table from the sample TICKIT data.
For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

Use a simple CASE expression to replace `New York City` with
`Big Apple` in a query against the VENUE table. Replace all other city
names with `other`.

```
`select venuecity,
 case venuecity
 when 'New York City'
 then 'Big Apple' else 'other'
 end
from venue
order by venueid desc;`
`venuecity | case
-----------------+-----------
Los Angeles | other
New York City | Big Apple
San Francisco | other
Baltimore | other
...`
```

Use a searched CASE expression to assign group numbers based on the PRICEPAID
value for individual ticket sales:

```
`select pricepaid,
 case when pricepaid <10000 then 'group 1'
 when pricepaid >10000 then 'group 2'
 else 'group 3'
 end
from sales
order by 1 desc;`
`pricepaid | case
----------+---------
12624 | group 2
10000 | group 3
10000 | group 3
9996 | group 1
9988 | group 1
...`
```
