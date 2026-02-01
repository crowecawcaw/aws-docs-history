Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMESTAMP_CMP_TIMESTAMPTZ function

TIMESTAMP_CMP_TIMESTAMPTZ compares the value of a timestamp expression with a timestamp
with time zone expression. If the timestamp and timestamp with time zone values are
identical, the function returns `0`. If the timestamp is greater
chronologically, the function returns `1`. If the timestamp with time zone is
greater, the function returns `–1`.

## Syntax

```
TIMESTAMP_CMP_TIMESTAMPTZ(*timestamp*, *timestamptz*)
```

## Arguments

_timestamp_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

_timestamptz_

A column of data type `TIMESTAMPTZ` or an expression that
implicitly evaluates to a `TIMESTAMPTZ` type.

## Return type

INTEGER

## Examples

The following example compares timestamps to timestamps with time zones and shows the
results of the comparison.

```
`SELECT TIMESTAMP_CMP_TIMESTAMPTZ('2008-01-24 06:43:29', '2008-01-24 06:43:29+00'), TIMESTAMP_CMP_TIMESTAMPTZ('2008-01-24 06:43:29', '2008-02-18 02:36:48+00'), TIMESTAMP_CMP_TIMESTAMPTZ('2008-02-18 02:36:48', '2008-01-24 06:43:29+00');`

`timestamp_cmp_timestamptz | timestamp_cmp_timestamptz | timestamp_cmp_timestamptz
---------------------------+---------------------------+--------------------------
 0 | -1 | 1`
```
