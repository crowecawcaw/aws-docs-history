Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMESTAMP_CMP function

Compares the value of two timestamps and returns an integer. If the timestamps are
identical, the function returns `0`. If the first timestamp is greater, the
function returns `1`. If the second timestamp is greater, the function returns `-1`.

## Syntax

```
TIMESTAMP_CMP(*timestamp1*, *timestamp2*)
```

## Arguments

_timestamp1_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

_timestamp2_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

## Return type

INTEGER

## Examples

The following example compares timestamps and shows the results of the
comparison.

```
`SELECT TIMESTAMP_CMP('2008-01-24 06:43:29', '2008-01-24 06:43:29'), TIMESTAMP_CMP('2008-01-24 06:43:29', '2008-02-18 02:36:48'), TIMESTAMP_CMP('2008-02-18 02:36:48', '2008-01-24 06:43:29');`

`timestamp_cmp | timestamp_cmp | timestamp_cmp
---------------+---------------+---------------
 0 | -1 | 1`
```

The following example compares the LISTTIME and SALETIME for a listing. The value for
TIMESTAMP_CMP is `-1` for all listings because the timestamp for the sale is after the
timestamp for the listing.

```
`select listing.listid, listing.listtime,
sales.saletime, timestamp_cmp(listing.listtime, sales.saletime)
from listing, sales
where listing.listid=sales.listid
order by 1, 2, 3, 4
limit 10;`

 `listid | listtime | saletime | timestamp_cmp
--------+---------------------+---------------------+---------------
 1 | 2008-01-24 06:43:29 | 2008-02-18 02:36:48 | -1
 4 | 2008-05-24 01:18:37 | 2008-06-06 05:00:16 | -1
 5 | 2008-05-17 02:29:11 | 2008-06-06 08:26:17 | -1
 5 | 2008-05-17 02:29:11 | 2008-06-09 08:38:52 | -1
 6 | 2008-08-15 02:08:13 | 2008-08-31 09:17:02 | -1
 10 | 2008-06-17 09:44:54 | 2008-06-26 12:56:06 | -1
 10 | 2008-06-17 09:44:54 | 2008-07-10 02:12:36 | -1
 10 | 2008-06-17 09:44:54 | 2008-07-16 11:59:24 | -1
 10 | 2008-06-17 09:44:54 | 2008-07-22 02:23:17 | -1
 12 | 2008-07-25 01:45:49 | 2008-08-04 03:06:36 | -1
(10 rows)`
```

This example shows that TIMESTAMP_CMP returns a 0 for identical timestamps:

```
`select listid, timestamp_cmp(listtime, listtime)
from listing
order by 1 , 2
limit 10;`

 `listid | timestamp_cmp
--------+---------------
 1 | 0
 2 | 0
 3 | 0
 4 | 0
 5 | 0
 6 | 0
 7 | 0
 8 | 0
 9 | 0
 10 | 0
(10 rows)`
```
