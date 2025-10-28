# windowSum

The `windowSum` function calculates the sum of the aggregated measure in a
custom window that is partitioned and sorted by specified attributes. Usually, you use
custom window functions on a time series, where your visual shows a metric and a date
field.

Window functions aren't supported for MySQL versions earlier than 8 and MariaDB
versions earlier than 10.2.

## Syntax

The brackets are required. To see which arguments are optional, see the following
descriptions.

```
windowSum
	(
	     `measure`
            , `[sort_order_field ASC/DESC, ...]`
            , `start_index`
            , `end_index`
	     ,`[ partition_field, ... ]`
	)
```

## Arguments

_measure_

The aggregated metric that you want to get the sum for, for example
`sum({Revenue})`.

For the engines MySQL, MariaDB, and Amazon Aurora with MySQL
compatibility, the lookup index is limited to just 1. Window functions
aren't supported for MySQL versions below 8 and MariaDB versions
earlier than 10.2.

_sort attribute_

One or more aggregated fields, either measures or dimensions or both,
that you want to sort the data by, separated by commas. You can either
specify ascending (`ASC`) or descending
(`DESC`) sort order.

Each field in the list is enclosed in {} (curly braces), if it's
more than one word. The entire list is enclosed in [ ] (square
brackets).

_start index_

The start index is a positive integer, indicating _n_ rows above the current row. The start
index counts the available data points above the
current row, rather than counting actual time periods. If your data is
sparse (missing months or years, for example), adjust the indexes
accordingly.

_end index_

The end index is a positive integer, indicating _n_ rows below the current row. The end index
counts the available data points below the current
row, rather than counting actual time periods. If your data is sparse
(missing months or years, for example), adjust the indexes accordingly.

_partition field_

(Optional) One or more dimensions that you want to partition by,
separated by commas.

Each field in the list is enclosed in {} (curly braces), if it's
more than one word. The entire list is enclosed in [ ] (square
brackets).

## Example

The following example calculates the moving sum of `sum(Revenue)`,
sorted by `SaleDate`. The calculation includes two rows above and one row
ahead of the current row.

```
windowSum
	(
	     sum(Revenue),
	     [SaleDate ASC],
	     2,
            1
	)
```

The following example show a trailing 12-month sum.

```
windowSum(sum(Revenue),[SaleDate ASC],12,0)
```

The following screenshot shows the results of this trailing 12-month sum example.
The `sum(Revenue)` field is added to the chart to show the difference
between the revenue and the trailing 12-month sum of revenue.

![](images/windowSum.png)
