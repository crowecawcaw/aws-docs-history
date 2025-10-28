Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LPAD and RPAD functions

These functions prepend or append characters to a string, based on a specified
length.

## Syntax

```
LPAD(*string1*, *length*, [ *string2* ])
```

```
RPAD(*string1*, *length*, [ *string2* ])
```

## Arguments

_string1_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

_length_

An integer that defines the length of the result of the function. The
length of a string is based on the number of characters, not bytes, so that
multi-byte characters are counted as single characters. If
_string1_ is longer than the specified length, it is
truncated (on the right). If _length_ is zero or a negative
number, the result of the function is an empty string.

_string2_

(Optional) One or more characters that are prepended or appended to
_string1_. If this argument is not
specified, spaces are used.

## Return type

VARCHAR

## Examples

The following examples use data from the EVENT table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To truncate a specified set of event names to 20 characters and prepend the shorter
names with spaces, use the following example.

````
`SELECT LPAD(eventname, 20) FROM event
WHERE eventid BETWEEN 1 AND 5 ORDER BY 1;`

`+---------------------+
| lpad | +---------------------+
| Salome |
| Il Trovatore |
| Boris Godunov |
| Gotterdammerung |
|La Cenerentola (Cind | +-----------------------+` ``` To truncate the same set of event names to 20 characters but append the shorter names with `0123456789`, use the following example. ``` `SELECT RPAD(eventname, 20,'0123456789') FROM event WHERE eventid BETWEEN 1 AND 5 ORDER BY 1;` `+----------------------+
| rpad | +----------------------+
| Boris Godunov0123456 |
| Gotterdammerung01234 |
| Il Trovatore01234567 |
| La Cenerentola (Cind |
| Salome01234567890123 | +----------------------+` ```
````
