Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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

Is true when the _table_subquery_ returns at least
one row.

NOT EXISTS

Is true when the _table_subquery_ returns no
rows.

_table_subquery_

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
