Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# INTERVAL_CMP function

INTERVAL_CMP compares two intervals and returns `1` if the first interval is
greater, `-1` if the second interval is greater, and `0` if the
intervals are equal. For more information, see [Examples of interval literals without
qualifier syntax](r_interval_literals.md "r_interval_literals.md").

## Syntax

```
INTERVAL_CMP(*interval1, interval2*)
```

## Arguments

_interval1_

An interval literal value.

_interval2_

An interval literal value.

## Return type

INTEGER

## Examples

The following example compares the value of `3 days` to `1
 year`.

```
`select interval_cmp('3 days','1 year');`

`interval_cmp
--------------
-1`
```

This example compares the value `7 days` to `1 week`.

```
`select interval_cmp('7 days','1 week');`

`interval_cmp
--------------
0`
```

The following example compares the value of `1 year` to `3
 days`.

```
`select interval_cmp('1 year','3 days');`

`interval_cmp
--------------
1`
```
