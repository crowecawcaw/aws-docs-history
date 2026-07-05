Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# EXCLUDE column\_list

The EXCLUDE column\_list names the columns that are excluded from the query results.
Using the EXCLUDE option is helpful when only a subset of columns need to be excluded from a _wide_ table, which is a table that contains many columns.

###### Topics

- [Syntax](#r_EXCLUDE_list-synopsis "#r_EXCLUDE_list-synopsis")
- [Parameters](#r_EXCLUDE_list-parameters "#r_EXCLUDE_list-parameters")
- [Examples](#r_EXCLUDE_list-examples "#r_EXCLUDE_list-examples")

## Syntax

```
EXCLUDE *column\_list*
```

## Parameters

_column\_list_

A comma-separated list of one or more column names that exist in the tables
referenced by the query. The _column\_list_ can optionally be enclosed in parentheses.
Only column names are supported in the exclude list of column names, not expressions (such as `upper(col1)`) or asterisk (\*).

```
*column-name*, ... | ( *column-name*, ... )
```

For example:

```
SELECT * EXCLUDE col1, col2 FROM tablea;
```

```
SELECT * EXCLUDE (col1, col2) FROM tablea;
```

## Examples

The following examples use the SALES table that contains columns: salesid, listid, sellerid, buyerid, eventid, dateid, qtysold, pricepaid, commission, and saletime.
For more information about the SALES table, see
[Sample database](c_sampledb.md "c_sampledb.md").

The following example returns rows from the SALES table, but excludes the SALETIME column.

```
`SELECT * EXCLUDE saletime FROM sales;`
`salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission
--------+---------+----------+---------+---------+---------+----------+------------+-----------
150314 | 173969 | 48680 | 816 | 8762 | 1827 | 2 | 688 | 103.2
8325 | 8942 | 23600 | 1078 | 2557 | 1828 | 5 | 525 | 78.75
46807 | 52711 | 34388 | 1047 | 2046 | 1828 | 2 | 482 | 72.3
...`
```

The following example returns rows from the SALES table, but excludes the QTYSOLD and SALETIME columns.

```
`SELECT * EXCLUDE (qtysold, saletime) FROM sales;`
`salesid | listid | sellerid | buyerid | eventid | dateid | pricepaid | commission
--------+---------+----------+---------+---------+---------+------------+-----------
150314 | 173969 | 48680 | 816 | 8762 | 1827 | 688 | 103.2
8325 | 8942 | 23600 | 1078 | 2557 | 1828 | 525 | 78.75
46807 | 52711 | 34388 | 1047 | 2046 | 1828 | 482 | 72.3
...`
```

The following example creates a view that returns rows from the SALES table, but excludes the SALETIME column.

```
`CREATE VIEW sales_view AS SELECT * EXCLUDE saletime FROM sales;`
`SELECT * FROM sales_view;`
`salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission
--------+---------+----------+---------+---------+---------+----------+------------+-----------
150314 | 173969 | 48680 | 816 | 8762 | 1827 | 2 | 688 | 103.2
8325 | 8942 | 23600 | 1078 | 2557 | 1828 | 5 | 525 | 78.75
46807 | 52711 | 34388 | 1047 | 2046 | 1828 | 2 | 482 | 72.3
...`
```

The following example selects only the columns that are not excluded into a temp table.

```
`SELECT * EXCLUDE saletime INTO TEMP temp_sales FROM sales;`
`SELECT * FROM temp_sales;`
`salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission
--------+---------+----------+---------+---------+---------+----------+------------+-----------
150314 | 173969 | 48680 | 816 | 8762 | 1827 | 2 | 688 | 103.2
8325 | 8942 | 23600 | 1078 | 2557 | 1828 | 5 | 525 | 78.75
46807 | 52711 | 34388 | 1047 | 2046 | 1828 | 2 | 482 | 72.3
...`
```
