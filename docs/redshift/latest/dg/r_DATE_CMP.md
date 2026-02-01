Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATE_CMP function

DATE_CMP compares two dates. The function returns `0` if the dates are
identical, `1` if _date1_ is greater, and `-1` if
_date2_ is greater.

## Syntax

```
DATE_CMP(*date1, date2*)
```

## Arguments

_date1_

A column of data type `DATE` or an expression that evaluates to a
`DATE` type.

_date2_

A column of data type `DATE` or an expression that evaluates to a
`DATE` type.

## Return type

INTEGER

## Examples

The following query compares the DATE values in the CALDATE column to the date January 4, 2008 and
returns whether the value in CALDATE is before (`-1`), equal to
(`0`), or after (`1`) January 4, 2008:

```
`select caldate, '2008-01-04',
date_cmp(caldate,'2008-01-04')
from date
order by dateid
limit 10;`

 `caldate | ?column? | date_cmp
-----------+------------+----------
2008-01-01 | 2008-01-04 | -1
2008-01-02 | 2008-01-04 | -1
2008-01-03 | 2008-01-04 | -1
2008-01-04 | 2008-01-04 | 0
2008-01-05 | 2008-01-04 | 1
2008-01-06 | 2008-01-04 | 1
2008-01-07 | 2008-01-04 | 1
2008-01-08 | 2008-01-04 | 1
2008-01-09 | 2008-01-04 | 1
2008-01-10 | 2008-01-04 | 1
(10 rows)`
```
