Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATE_CMP_TIMESTAMPTZ function

DATE_CMP_TIMESTAMPTZ compares a date to a timestamp with time zone and returns
`0` if the values are identical, `1` if _date_
is greater chronologically and `-1` if _timestamptz_ is
greater.

## Syntax

```
DATE_CMP_TIMESTAMPTZ(*date*, *timestamptz*)
```

## Arguments

_date_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

_timestamptz_

A column of data type `TIMESTAMPTZ` or an expression that
implicitly evaluates to a `TIMESTAMPTZ` type.

## Return type

INTEGER

## Examples

The following example compares the date `2008-06-18` to LISTTIME. Listings
made before this date return `1`; listings made after this date return
`-1`.

```
`select listid, '2008-06-18', CAST(listtime AS timestamptz),
date_cmp_timestamptz('2008-06-18', CAST(listtime AS timestamptz))
from listing
order by 1, 2, 3, 4
limit 10;`

 `listid | ?column? | timestamptz | date_cmp_timestamptz
--------+------------+------------------------+----------------------
 1 | 2008-06-18 | 2008-01-24 06:43:29+00 | 1
 2 | 2008-06-18 | 2008-03-05 12:25:29+00 | 1
 3 | 2008-06-18 | 2008-11-01 07:35:33+00 | -1
 4 | 2008-06-18 | 2008-05-24 01:18:37+00 | 1
 5 | 2008-06-18 | 2008-05-17 02:29:11+00 | 1
 6 | 2008-06-18 | 2008-08-15 02:08:13+00 | -1
 7 | 2008-06-18 | 2008-11-15 09:38:15+00 | -1
 8 | 2008-06-18 | 2008-11-09 05:07:30+00 | -1
 9 | 2008-06-18 | 2008-09-09 08:03:36+00 | -1
 10 | 2008-06-18 | 2008-06-17 09:44:54+00 | 1
(10 rows)`
```
