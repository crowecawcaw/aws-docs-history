Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# OCTET_LENGTH function

Returns the length of the specified string as the number of bytes.

## Syntax

```
OCTET_LENGTH(*expression*)
```

## Argument

_expression_

A `CHAR` string, a `VARCHAR` string, a `VARBYTE` expression, or an expression that implicitly evaluates to a `CHAR`, `VARCHAR`, or `VARBYTE` type.

## Return type

INTEGER

The OCTET_LENGTH function returns an integer indicating the number of bytes in the
input string.

If the input string is a character string, the [LEN](r_LEN.md "r_LEN.md") function
returns the actual number of characters in multi-byte strings, not the number of
bytes. For example, a `VARCHAR(12)` column is required to
store three four-byte Chinese characters. The OCTET_LENGTH function will return `12` for that string, and the LEN function will return `3` for that
same string.

## Usage notes

If _expression_ is a `CHAR` string, the function returns the length of the `CHAR` string. For example, the output of a `CHAR(6)` input is a `CHAR(6)`.

If _expression_ is a `VARCHAR` string, trailing spaces are counted.

## Examples

To return the number of bytes when the string `francais` with three trailing spaces is cast to a `CHAR` and a `VARCHAR` type, use the following example. For more information, see the [CAST function](r_CAST_function.md "r_CAST_function.md").

````
`SELECT OCTET_LENGTH(CAST('francais ' AS CHAR(15))) AS octet_length_char, OCTET_LENGTH(CAST('francais ' AS VARCHAR(15))) AS octet_length_varchar;`

`+-------------------+----------------------+
| octet_length_char | octet_length_varchar | +-------------------+----------------------+
| 15 | 11 | +-------------------+----------------------+` ``` To return the number of bytes and the number of characters in the string `français`, use the following example. ``` `SELECT OCTET_LENGTH('français'), LEN('français');` `+--------------+-----+
| octet_length | len | +--------------+-----+
| 9 | 8 | +--------------+-----+` ``` To return the number of bytes when the string `français` is cast as a `VARBYTE`, use the following example. ``` `SELECT OCTET_LENGTH(CAST('français' AS VARBYTE));` `+--------------+
| octet_length | +--------------+ | 9 | +--------------+` ```
````
