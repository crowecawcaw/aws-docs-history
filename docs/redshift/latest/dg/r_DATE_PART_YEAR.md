Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATE_PART_YEAR function

The DATE_PART_YEAR function extracts the year from a date.

## Syntax

```
DATE_PART_YEAR(*date*)
```

## Argument

_date_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

## Return type

INTEGER

## Examples

The following example finds the year from a date literal.

```
`SELECT DATE_PART_YEAR(date '20220502 04:05:06.789');`

`date_part_year
---------------
2022`
```

The following example extracts the year from the CALDATE column. The values in the
CALDATE column are dates. For more information about the data used in this example, see
[Sample database](c_sampledb.md "c_sampledb.md").

```
`select caldate, date_part_year(caldate)
from date
order by
dateid limit 10;`

 `caldate | date_part_year
-----------+----------------
2008-01-01 | 2008
2008-01-02 | 2008
2008-01-03 | 2008
2008-01-04 | 2008
2008-01-05 | 2008
2008-01-06 | 2008
2008-01-07 | 2008
2008-01-08 | 2008
2008-01-09 | 2008
2008-01-10 | 2008
(10 rows)`
```
