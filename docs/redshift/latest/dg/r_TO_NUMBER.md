Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TO_NUMBER

TO_NUMBER converts a string to a numeric (decimal) value.

###### Note

We recommend that you use `FM` in your format string to suppress padding blanks and zeroes.
For a list of valid formats, see [Numeric format strings](r_Numeric_formating.md "r_Numeric_formating.md").

## Syntax

```
to_number(*string*, *format*)
```

## Arguments

_string_

String to be converted. The format must be a literal value.

_format_

The second argument is a format string that indicates how the character
string should be parsed to create the numeric value. For example, the format
`'FM99D999'` specifies that the string to be converted consists
of five digits with the decimal point in the third position. For example,
`to_number('12.345','FM99D999')` returns `12.345` as
a numeric value. For a list of valid formats, see [Numeric format strings](r_Numeric_formating.md "r_Numeric_formating.md").

## Return type

TO_NUMBER returns a DECIMAL number.

If the conversion to _format_ fails, then an error is returned.

## Examples

The following example converts the string `12,454.8-` to a number:

```
select to_number('12,454.8-', 'FM99G999D9S');

to_number
-----------
-12454.8

```

The following example converts the string `$ 12,454.88` to a number:

```
select to_number('$ 12,454.88', 'FML99G999D99');

to_number
-----------
12454.88

```

The following example converts the string `$ 2,012,454.88` to a number:

```
select to_number('$ 2,012,454.88', 'FML9,999,999.99');

to_number
-----------
2012454.88

```
