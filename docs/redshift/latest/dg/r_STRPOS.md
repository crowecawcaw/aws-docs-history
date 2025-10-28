Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STRPOS function

Returns the position of a substring within a specified string.

See [CHARINDEX function](r_CHARINDEX.md "r_CHARINDEX.md") and [POSITION function](r_POSITION.md "r_POSITION.md") for similar functions.

## Syntax

```
STRPOS(*string*, *substring* )
```

## Arguments

_string_

The first input parameter is the `CHAR` or `VARCHAR` string to be searched.

_substring_

The second parameter is the substring to search for within the
_string_.

## Return type

INTEGER

The STRPOS function returns an `INTEGER` corresponding to the position of the
_substring_ (one-based, not zero-based). The position is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters.

## Usage notes

STRPOS returns `0` if the _substring_ is not found within the
_string_.

````
`SELECT STRPOS('dogfish', 'fist');`

`+--------+
| strpos | +--------+
| 0 | +--------+` ``` ## Examples To show the position of `fish` within `dogfish`, use the following example. ``` `SELECT STRPOS('dogfish', 'fish');` `+--------+
| strpos | +--------+
| 4 | +--------+` ``` The following example uses data from the SALES table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md"). To return the number of sales transactions with a COMMISSION over 999.00 from the SALES table, use the following example. ``` `SELECT DISTINCT STRPOS(commission, '.'), COUNT (STRPOS(commission, '.')) FROM sales WHERE STRPOS(commission, '.') > 4 GROUP BY STRPOS(commission, '.') ORDER BY 1, 2;` `+--------+-------+
| strpos | count | +--------+-------+
| 5 | 629 | +--------+-------+` ```
````
