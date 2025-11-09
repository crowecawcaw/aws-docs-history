Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LEN function

Returns the length of the specified string as the number of characters.

## Syntax

LEN is a synonym of [LENGTH function](r_LENGTH.md "r_LENGTH.md"), [CHAR_LENGTH function](r_CHAR_LENGTH.md "r_CHAR_LENGTH.md"), [CHARACTER_LENGTH function](r_CHARACTER_LENGTH.md "r_CHARACTER_LENGTH.md"), and [TEXTLEN function](r_TEXTLEN.md "r_TEXTLEN.md").

```
LEN(*expression*)
```

## Argument

_expression_

A `CHAR` string, a `VARCHAR` string, a `VARBYTE` expression, or an expression that implicitly evaluates to a `CHAR`, `VARCHAR`, or `VARBYTE` type.

## Return type

INTEGER

The LEN function returns an integer indicating the number of characters in the
input string.

If the input string is a character string, the LEN function returns the actual number of characters in multi-byte
strings, not the number of bytes. For example, a `VARCHAR(12)` column is required to
store three four-byte Chinese characters. The LEN function will return `3` for that
same string. To get the length of a string in bytes, use the [OCTET_LENGTH](r_OCTET_LENGTH.md "r_OCTET_LENGTH.md") function.

## Usage notes

If _expression_ is a `CHAR` string, trailing spaces are not counted.

If _expression_ is a `VARCHAR` string, trailing spaces are counted.

## Examples

To return the number of bytes and the number of characters in
the string `français`, use the following example.

```
`SELECT OCTET_LENGTH('français'),
LEN('français');`

`+--------------+-----+
| octet_length | len |
+--------------+-----+
| 9 | 8 |
+--------------+-----+`
```

To return the number of bytes and the number of characters in the string `français` without using the OCTET_LENGTH function,
use the following example. For more information, see the [CAST function](r_CAST_function.md "r_CAST_function.md").

```
`SELECT LEN(CAST('français' AS VARBYTE)) as bytes, LEN('français');`

`+-------+-----+
| bytes | len |
+-------+-----+
| 9 | 8 |
+-------+-----+`
```

To return the number of characters in the strings
`cat` with no trailing spaces, `cat` with three trailing
spaces, `cat` with three trailing spaces cast as a `CHAR`
of length 6, and `cat` with three trailing spaces cast as a `VARCHAR`
of length 6, use the following example. Notice that the function does not count trailing spaces for `CHAR` strings, but it does count trailing spaces for `VARCHAR` strings.

```
`SELECT LEN('cat'), LEN('cat '), LEN(CAST('cat ' AS CHAR(6))) AS len_char, LEN(CAST('cat ' AS VARCHAR(6))) AS len_varchar;`

`+-----+-----+----------+-------------+
| len | len | len_char | len_varchar |
+-----+-----+----------+-------------+
| 3 | 6 | 3 | 6 |
+-----+-----+----------+-------------+`
```

The following example uses data from the VENUE table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the 10 longest venue names in the VENUE
table, use the following example.

```
`SELECT venuename, LEN(venuename)
FROM venue
ORDER BY 2 DESC, 1
LIMIT 10;`

`+-----------------------------------------+-----+
| venuename | len |
+-----------------------------------------+-----+
| Saratoga Springs Performing Arts Center | 39 |
| Lincoln Center for the Performing Arts | 38 |
| Nassau Veterans Memorial Coliseum | 33 |
| Jacksonville Municipal Stadium | 30 |
| Rangers BallPark in Arlington | 29 |
| University of Phoenix Stadium | 29 |
| Circle in the Square Theatre | 28 |
| Hubert H. Humphrey Metrodome | 28 |
| Oriole Park at Camden Yards | 27 |
| Dick's Sporting Goods Park | 26 |
+-----------------------------------------+-----+`
```
