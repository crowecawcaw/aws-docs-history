Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMESTAMPTZ_CMP function

TIMESTAMPTZ_CMP compares the value of two timestamp with time zone values and returns an
integer. If the timestamps are identical, the function returns `0`. If the first
timestamp is greater chronologically, the function returns `1`. If the second
timestamp is greater, the function returns `–1`.

## Syntax

```
TIMESTAMPTZ_CMP(*timestamptz1, timestamptz2*)
```

## Arguments

_timestamptz1_

A column of data type `TIMESTAMPTZ` or an expression that
implicitly evaluates to a `TIMESTAMPTZ` type.

_timestamptz2_

A column of data type `TIMESTAMPTZ` or an expression that
implicitly evaluates to a `TIMESTAMPTZ` type.

## Return type

INTEGER

## Examples

The following example compares timestamps with time zones and shows the results of the
comparison.

```
`SELECT TIMESTAMPTZ_CMP('2008-01-24 06:43:29+00', '2008-01-24 06:43:29+00'), TIMESTAMPTZ_CMP('2008-01-24 06:43:29+00', '2008-02-18 02:36:48+00'), TIMESTAMPTZ_CMP('2008-02-18 02:36:48+00', '2008-01-24 06:43:29+00');`

`timestamptz_cmp | timestamptz_cmp | timestamptz_cmp
-----------------+-----------------+----------------
 0 | -1 | 1`
```
