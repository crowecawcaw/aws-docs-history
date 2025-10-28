Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATE_CMP_TIMESTAMP function

DATE_CMP_TIMESTAMP compares a date to a timestamp and returns `0` if the
values are identical, `1` if _date_ is greater
chronologically and `-1` if _timestamp_ is greater.

## Syntax

```
DATE_CMP_TIMESTAMP(*date*, *timestamp*)
```

## Arguments

_date_

A column of data type `DATE` or an expression that evaluates to a
`DATE` type.

_timestamp_

A column of data type `TIMESTAMP` or an expression that evaluates
to a `TIMESTAMP` type.

## Return type

INTEGER

## Examples

The following example compares the date `2008-06-18` to LISTTIME. The values of the column LISTTIME are timestamps. Listings
made before this date return `1`; listings made after this date return
`-1`.

```
`select listid, '2008-06-18', listtime,
date_cmp_timestamp('2008-06-18', listtime)
from listing
order by 1, 2, 3, 4
limit 10;`

 `listid | ?column? | listtime | date_cmp_timestamp
--------+------------+---------------------+--------------------
 1 | 2008-06-18 | 2008-01-24 06:43:29 | 1
 2 | 2008-06-18 | 2008-03-05 12:25:29 | 1
 3 | 2008-06-18 | 2008-11-01 07:35:33 | -1
 4 | 2008-06-18 | 2008-05-24 01:18:37 | 1
 5 | 2008-06-18 | 2008-05-17 02:29:11 | 1
 6 | 2008-06-18 | 2008-08-15 02:08:13 | -1
 7 | 2008-06-18 | 2008-11-15 09:38:15 | -1
 8 | 2008-06-18 | 2008-11-09 05:07:30 | -1
 9 | 2008-06-18 | 2008-09-09 08:03:36 | -1
 10 | 2008-06-18 | 2008-06-17 09:44:54 | 1
(10 rows)`
```
