Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DIFFERENCE function

The DIFFERENCE function compares the American Soundex codes of two strings. The function returns an `INTEGER` to indicate the number of matching characters between the Soundex codes.

A Soundex code is a string that is four characters long. A Soundex code represents how a word sounds rather than how it is spelled. For example, `Smith` and `Smyth` have the same Soundex code.

## Syntax

```
DIFFERENCE(*string1*, *string2*)
```

## Arguments

_string1_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

_string2_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

## Return type

INTEGER

The DIFFERENCE function returns an `INTEGER` value from 0–4 that counts the number of matching characters in
the American Soundex codes of the two strings. A Soundex code has 4 characters, so the DIFFERENCE function returns `4`
when all 4 characters of the strings' American Soundex code values are the same.

DIFFERENCE returns `0` if one of the two strings is empty. The function returns `1` if neither string contains valid characters.

The DIFFERENCE function converts only English alphabetical lowercase or uppercase ASCII
characters, including a–z and A–Z. DIFFERENCE ignores other characters.

## Examples

To compare the Soundex values of the strings `%` and `@`, use the following example. The function returns `1` because neither string contains valid characters.

````
`SELECT DIFFERENCE('%', '@');`

`+------------+
| difference | +------------+
| 1 | +------------+` ``` To compare the Soundex values of `Amazon` and an empty string, use the following example. The function returns `0` because one of the two strings is empty. ``` `SELECT DIFFERENCE('Amazon', '');` `+------------+
| difference | +------------+
| 0 | +------------+` ``` To compare the Soundex values of the strings `Amazon` and `Ama`, use the following example. The function returns `2` because 2 characters of the strings' Soundex values are the same. ``` `SELECT DIFFERENCE('Amazon', 'Ama');` `+------------+
| difference | +------------+
| 2 | +------------+` ``` To compare the Soundex values of the strings `Amazon` and `+-*/%Amazon`, use the following example. The function returns `4` because all 4 characters of the strings' Soundex values are the same. Notice that the function ignores the invalid characters `+-*/%` in the second string. ``` `SELECT DIFFERENCE('Amazon', '+-*/%Amazon');` `+------------+
| difference | +------------+
| 4 | +------------+` ``` To compare the Soundex values of the strings `AC/DC` and `Ay See Dee See`, use the following example. The function returns `4` because all 4 characters of the strings' Soundex values are the same. ``` `SELECT DIFFERENCE('AC/DC', 'Ay See Dee See');` `+------------+
| difference | +------------+
| 4 | +------------+` ```
````
