Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMESTAMP_CMP_DATE function

TIMESTAMP_CMP_DATE compares the value of a timestamp and a date. If the timestamp and
date values are identical, the function returns `0`. If the timestamp is greater
chronologically, the function returns `1`. If the date is greater, the function
returns `-1`.

## Syntax

```
TIMESTAMP_CMP_DATE(*timestamp*, *date*)
```

## Arguments

_timestamp_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

_date_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

## Return type

INTEGER

## Examples

The following example compares LISTTIME to the date `2008-06-18`. Listings
made after this date return `1`; listings made before this date return
`-1`. LISTTIME values are timestamps.

```
`select listid, listtime,
timestamp_cmp_date(listtime, '2008-06-18')
from listing
order by 1, 2, 3
limit 10;`


 `listid | listtime | timestamp_cmp_date
--------+---------------------+--------------------
 1 | 2008-01-24 06:43:29 | -1
 2 | 2008-03-05 12:25:29 | -1
 3 | 2008-11-01 07:35:33 | 1
 4 | 2008-05-24 01:18:37 | -1
 5 | 2008-05-17 02:29:11 | -1
 6 | 2008-08-15 02:08:13 | 1
 7 | 2008-11-15 09:38:15 | 1
 8 | 2008-11-09 05:07:30 | 1
 9 | 2008-09-09 08:03:36 | 1
 10 | 2008-06-17 09:44:54 | -1
(10 rows)`

```
