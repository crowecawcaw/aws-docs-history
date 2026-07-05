Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# EXISTS condition

EXISTS conditions test for the existence of rows in a subquery, and return true if
a subquery returns at least one row. If NOT is specified, the condition returns true
if a subquery returns no rows.

## Syntax

```
[ NOT ] EXISTS (*table\_subquery*)
```

## Arguments

EXISTS

Is true when the _table\_subquery_ returns at least
one row.

NOT EXISTS

Is true when the _table\_subquery_ returns no
rows.

_table\_subquery_

A subquery that evaluates to a table with one or more columns and one
or more rows.

## Example

This example returns all date identifiers, one time each, for each date that
had a sale of any kind:

```
select dateid from date
where exists (
select 1 from sales
where date.dateid = sales.dateid
)
order by dateid;

dateid
--------
1827
1828
1829
...
```
