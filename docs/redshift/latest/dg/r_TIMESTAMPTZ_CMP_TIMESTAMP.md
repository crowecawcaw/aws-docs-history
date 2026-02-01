Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMESTAMPTZ_CMP_TIMESTAMP function

TIMESTAMPTZ_CMP_TIMESTAMP compares the value of a timestamp with time zone expression
with a timestamp expression. If the timestamp with time zone and timestamp values are
identical, the function returns `0`. If the timestamp with time zone is greater
chronologically, the function returns `1`. If the timestamp is greater, the
function returns `–1`.

## Syntax

```
TIMESTAMPTZ_CMP_TIMESTAMP(*timestamptz*, *timestamp*)
```

## Arguments

_timestamptz_

A column of data type `TIMESTAMPTZ` or an expression that
implicitly evaluates to a `TIMESTAMPTZ` type.

_timestamp_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

## Return type

INTEGER

## Examples

The following example compares timestamps with time zones to timestamps and shows the
results of the comparison.

```
`SELECT TIMESTAMPTZ_CMP_TIMESTAMP('2008-01-24 06:43:29+00', '2008-01-24 06:43:29'), TIMESTAMPTZ_CMP_TIMESTAMP('2008-01-24 06:43:29+00', '2008-02-18 02:36:48'), TIMESTAMPTZ_CMP_TIMESTAMP('2008-02-18 02:36:48+00', '2008-01-24 06:43:29');`

`timestamptz_cmp_timestamp | timestamptz_cmp_timestamp | timestamptz_cmp_timestamp
---------------------------+---------------------------+---------------------------
 0 | -1 | 1`
```
