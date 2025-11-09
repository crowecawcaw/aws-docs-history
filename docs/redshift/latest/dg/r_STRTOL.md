Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STRTOL function

Converts a string expression of a number of the specified base to the equivalent
integer value. The converted value must be within the signed 64-bit range.

## Syntax

```
STRTOL(*num\_string*, *base*)
```

## Arguments

_num_string_

String expression of a number to be converted. If
_num_string_ is empty ( `''` ) or begins
with the null character (`'\0'`), the converted value is `0`. If
_num_string_ is a column containing a NULL value,
STRTOL returns `NULL`. The string can begin with any amount of white space,
optionally followed by a single plus '`+`' or minus
'`-`' sign to indicate positive or negative. The default is
'`+`'. If _base_ is `16`, the
string can optionally begin with '`0x`'.

_base_

`INTEGER` between 2 and 36.

## Return type

BIGINT

If _num_string_ is null, the function returns `NULL`.

## Examples

To convert string and base value pairs to integers, use the following examples.

```
`SELECT STRTOL('0xf',16);`

`+--------+
| strtol |
+--------+
| 15 |
+--------+`

`SELECT STRTOL('abcd1234',16);`

`+------------+
| strtol |
+------------+
| 2882343476 |
+------------+`

`SELECT STRTOL('1234567', 10);`

`+---------+
| strtol |
+---------+
| 1234567 |
+---------+`

`SELECT STRTOL('1234567', 8);`

`+--------+
| strtol |
+--------+
| 342391 |
+--------+`

`SELECT STRTOL('110101', 2);`

`+--------+
| strtol |
+--------+
| 53 |
+--------+`

`SELECT STRTOL('\0', 2);`

`+--------+
| strtol |
+--------+
| 0 |
+--------+`
```
