Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# POSITION function

Returns the location of the specified substring within a string.

See [CHARINDEX function](r_CHARINDEX.md "r_CHARINDEX.md") and [STRPOS function](r_STRPOS.md "r_STRPOS.md") for similar functions.

## Syntax

```
POSITION(*substring* IN *string* )
```

## Arguments

_substring_

The substring to search for within the _string_.

_string_

The string or column to be searched.

## Return type

The POSITION function returns an `INTEGER` corresponding to the position of the
substring (one-based, not zero-based). The position is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters. POSITION returns `0` if the substring is not found within the string.

## Examples

To return the position of the string `fish` within
the word `dog`, use the following example.

```
`SELECT POSITION('fish' IN 'dog');`

`+-----------+
| position |
+-----------+
| 0 |
+-----------+`
```

To return the position of the string `fish` within
the word `dogfish`, use the following example.

```
`SELECT POSITION('fish' IN 'dogfish');`

`+-----------+
| position |
+-----------+
| 4 |
+-----------+`
```

The following example uses the SALES table from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the number of distinct sales transactions with a commission
over 999.00 from the SALES table, use the following example. This command counts commissions greater than 999.00 by checking if the decimal is more than 4 places from the beginning of the commission value.

```
`SELECT DISTINCT POSITION('.' IN commission), COUNT (POSITION('.' IN commission))
FROM sales
WHERE POSITION('.' IN commission) > 4
GROUP BY POSITION('.' IN commission)
ORDER BY 1,2;`

`+-----------+-------+
| position | count |
+-----------+-------+
| 5 | 629 |
+-----------+-------+`
```
