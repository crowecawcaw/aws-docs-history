Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# OCTETINDEX function

The OCTETINDEX function returns the location of a substring within a string as a number of bytes.

## Syntax

```
OCTETINDEX(*substring*, *string*)
```

## Arguments

_substring_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

_string_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

## Return type

INTEGER

The OCTETINDEX function returns an `INTEGER` value corresponding to the position of the _substring_ within the
_string_ as a number of bytes, where the first character in the _string_ is counted as 1.
If the _string_ doesn't contain multibyte characters, the result is equal to the result
of the CHARINDEX function. If the _string_ does not contain the _substring_, the function returns `0`.
If the _substring_ is empty, the function returns `1`.

## Examples

To return the postion of the substring `q` in the string `Amazon Redshift`, use the following example. This example returns `0` because the _substring_ is not in the _string_.

````
`SELECT OCTETINDEX('q', 'Amazon Redshift');`

`+------------+
| octetindex | +------------+
| 0 | +------------+` ``` To return the postion of an empty substring in the string `Amazon Redshift`, use the following example. This example returns `1` because the *substring* is empty. ``` `SELECT OCTETINDEX('', 'Amazon Redshift');` `+------------+
| octetindex | +------------+
| 1 | +------------+` ``` To return the postion of the substring `Redshift` in the string `Amazon Redshift`, use the following example. This example returns `8` because the *substring* begins on the eighth byte of the *string*. ``` `SELECT OCTETINDEX('Redshift', 'Amazon Redshift');` `+------------+
| octetindex | +------------+
| 8 | +------------+` ``` To return the postion of the substring `Redshift` in the string `Amazon Redshift`, use the following example. This example returns `21` because the first six characters of the *string* are double-byte characters. ``` `SELECT OCTETINDEX('Redshift', 'Άμαζον Amazon Redshift');` `+------------+
| octetindex | +------------+
| 21 | +------------+` ```
````
