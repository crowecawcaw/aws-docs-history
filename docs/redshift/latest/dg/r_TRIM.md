Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TRIM function

Trims a string by blanks or specified characters.

## Syntax

```
TRIM( [ BOTH | LEADING | TRAILING ] [*trim\_chars* FROM ] *string* )
```

## Arguments

BOTH | LEADING | TRAILING

(Optional) Specifies where to trim characters from. Use BOTH to remove leading and trailing characters,
use LEADING to remove leading characters only, and use TRAILING to remove trailing characters only.
If this parameter is omitted, both leading and trailing characters are trimmed.

_trim_chars_

(Optional) The characters to be trimmed from the string. If this
parameter is omitted, blanks are trimmed.

_string_

The string to be trimmed.

## Return type

The TRIM function returns a `VARCHAR` or `CHAR` string. If you use the TRIM function
with a SQL command, Amazon Redshift implicitly converts the results to `VARCHAR`. If you use
the TRIM function in the SELECT list for a SQL function, Amazon Redshift does not implicitly
convert the results, and you might need to perform an explicit conversion to avoid a
data type mismatch error. See the [CAST function](r_CAST_function.md "r_CAST_function.md") and [CONVERT function](r_CONVERT_function.md "r_CONVERT_function.md") functions for information about explicit
conversions.

## Examples

To trim both leading and trailing blanks from the string
`dog` , use the following example.

```
`SELECT TRIM(' dog ');`

`+-------+
| btrim |
+-------+
| dog |
+-------+`
```

To trim both leading and trailing blanks from the string
`dog` , use the following example.

```
`SELECT TRIM(BOTH FROM ' dog ');`

`+-------+
| btrim |
+-------+
| dog |
+-------+`
```

To remove the leading double quotation marks from the string
`"dog"`, use the following example.

```
`SELECT TRIM(LEADING '"' FROM'"dog"');`

`+-------+
| ltrim |
+-------+
| dog" |
+-------+`
```

To remove the trailing double quotation marks from the string
`"dog"`, use the following example.

```
`SELECT TRIM(TRAILING '"' FROM'"dog"');`

`+-------+
| rtrim |
+-------+
| "dog |
+-------+`
```

TRIM removes any of the characters in _trim_chars_ when they
appear at the beginning or end of _string_. The following example trims
the characters 'C', 'D', and 'G' when they appear at the beginning or end of VENUENAME, which
is a `VARCHAR` column. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

```
`SELECT venueid, venuename, TRIM('CDG' FROM venuename)
FROM venue
WHERE venuename LIKE '%Park'
ORDER BY 2
LIMIT 7;`

`+---------+----------------------------+---------------------------+
| venueid | venuename | btrim |
+---------+----------------------------+---------------------------+
| 121 | AT&T Park | AT&T Park |
| 109 | Citizens Bank Park | itizens Bank Park |
| 102 | Comerica Park | omerica Park |
| 9 | Dick's Sporting Goods Park | ick's Sporting Goods Park |
| 97 | Fenway Park | Fenway Park |
| 112 | Great American Ball Park | reat American Ball Park |
| 114 | Miller Park | Miller Park |
+---------+----------------------------+---------------------------+`
```
