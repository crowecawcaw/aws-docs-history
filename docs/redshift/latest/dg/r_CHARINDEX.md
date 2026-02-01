Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CHARINDEX function

Returns the location of the specified substring within a string.

See [POSITION function](r_POSITION.md "r_POSITION.md") and [STRPOS function](r_STRPOS.md "r_STRPOS.md") for similar functions.

## Syntax

```
CHARINDEX( *substring*, *string* )
```

## Arguments

_substring_

The substring to search for within the
_string_.

_string_

The string or column to be searched.

## Return type

INTEGER

The CHARINDEX function returns an `INTEGER` corresponding to the position of the
substring (one-based, not zero-based). The position is based on the number of
characters, not bytes, so that multi-byte characters are counted as single
characters. CHARINDEX returns `0` if the substring is not found within the string.

## Examples

To return the position of the string `fish` within
the word `dog`, use the following example.

```
`SELECT CHARINDEX('fish', 'dog');`

`+-----------+
| charindex |
+-----------+
| 0 |
+-----------+`
```

To return the position of the string `fish` within
the word `dogfish`, use the following example.

```
`SELECT CHARINDEX('fish', 'dogfish');`

`+-----------+
| charindex |
+-----------+
| 4 |
+-----------+`
```

The following example uses the SALES table from the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the number of distinct sales transactions with a commission
over 999.00 from the SALES table, use the following example. This command counts commissions greater than 999.00 by checking if the decimal is more than 4 places from the beginning of the commission value.

```
`SELECT DISTINCT CHARINDEX('.', commission), COUNT (CHARINDEX('.', commission))
FROM sales
WHERE CHARINDEX('.', commission) > 4
GROUP BY CHARINDEX('.', commission)
ORDER BY 1,2;`

`+-----------+-------+
| charindex | count |
+-----------+-------+
| 5 | 629 |
+-----------+-------+`
```
