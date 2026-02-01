Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Aggregate functions

###### Topics

- [ANY_VALUE
  function](r_ANY_VALUE.md "r_ANY_VALUE.md")
- [APPROXIMATE PERCENTILE_DISC
  function](r_APPROXIMATE_PERCENTILE_DISC.md "r_APPROXIMATE_PERCENTILE_DISC.md")
- [AVG function](r_AVG.md "r_AVG.md")
- [COUNT function](r_COUNT.md "r_COUNT.md")
- [LISTAGG function](r_LISTAGG.md "r_LISTAGG.md")
- [MAX function](r_MAX.md "r_MAX.md")
- [MEDIAN function](r_MEDIAN.md "r_MEDIAN.md")
- [MIN function](r_MIN.md "r_MIN.md")
- [PERCENTILE_CONT function](r_PERCENTILE_CONT.md "r_PERCENTILE_CONT.md")
- [STDDEV_SAMP and STDDEV_POP functions](r_STDDEV_functions.md "r_STDDEV_functions.md")
- [SUM function](r_SUM.md "r_SUM.md")
- [VAR_SAMP and VAR_POP functions](r_VARIANCE_functions.md "r_VARIANCE_functions.md")
  Aggregate functions compute a single result value from a set of input values.

SELECT statements using aggregate functions can include two optional clauses: GROUP BY
and HAVING. The syntax for these clauses is as follows (using the COUNT function as an
example):

```
SELECT count (*) *expression* FROM *table\_reference*
WHERE *condition* [GROUP BY *expression* ] [ HAVING *condition*]
```

The GROUP BY clause aggregates and groups results by the unique values in a specified
column or columns. The HAVING clause restricts the results returned to rows where a
particular aggregate condition is true, such as count (\*) > 1. The HAVING clause is used
in the same way as WHERE to restrict rows based on the value of a column. For an example of
these additional clauses, see the [COUNT](r_COUNT.md "r_COUNT.md").

Aggregate functions don't accept nested aggregate functions or window functions as
arguments.
