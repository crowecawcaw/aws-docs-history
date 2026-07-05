Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# LEFT and RIGHT functions

These functions return the specified number of leftmost or rightmost characters from
a character string.

The number is based on the number of characters, not bytes, so that multibyte
characters are counted as single characters.

## Syntax

```
LEFT( *string*,  *integer* )

RIGHT( *string*,  *integer* )
```

## Arguments

_string_

A `CHAR` string, a `VARCHAR` string, or any expression that evaluates to a `CHAR` or `VARCHAR` string.

_integer_

A positive integer.

## Return type

VARCHAR

## Examples

The following example uses data from the EVENT table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To return the leftmost 5 and rightmost 5 characters from event
names that have event IDs between 1000 and 1005, use the following example.

```
`SELECT eventid, eventname,
LEFT(eventname,5) AS left_5,
RIGHT(eventname,5) AS right_5
FROM event
WHERE eventid BETWEEN 1000 AND 1005
ORDER BY 1;`

`+---------+----------------+--------+---------+
| eventid | eventname | left_5 | right_5 |
+---------+----------------+--------+---------+
| 1000 | Gypsy | Gypsy | Gypsy |
| 1001 | Chicago | Chica | icago |
| 1002 | The King and I | The K | and I |
| 1003 | Pal Joey | Pal J | Joey |
| 1004 | Grease | Greas | rease |
| 1005 | Chicago | Chica | icago |
+---------+----------------+--------+---------+`
```
