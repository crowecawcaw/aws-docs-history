Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SLICE\_NUM Function

Returns an integer corresponding to the slice number in the cluster where the data
for a row is located. SLICE\_NUM takes no parameters.

## Syntax

```
SLICE_NUM()
```

## Return type

The SLICE\_NUM function returns an integer.

## Examples

The following example shows which slices contain data for the first ten EVENT rows
in the EVENTS table:

```
select distinct eventid, slice_num() from event order by eventid limit 10;

 eventid | slice_num
---------+-----------
       1 |         1
       2 |         2
       3 |         3
       4 |         0
       5 |         1
       6 |         2
       7 |         3
       8 |         0
       9 |         1
      10 |         2
(10 rows)
```

The following example returns a code (10000) to show that a query without a FROM
statement runs on the leader node:

```
select slice_num();
slice_num
-----------
10000
(1 row)
```
