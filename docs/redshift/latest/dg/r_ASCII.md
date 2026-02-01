Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ASCII function

The ASCII function returns the ASCII code, or the Unicode code-point, of the first character in the
string that you specify. The function returns `0` if the string is empty. It returns `NULL` if the string is null.

## Syntax

```
ASCII('*string*')
```

## Argument

_string_

A `CHAR` string or a `VARCHAR` string.

## Return type

INTEGER

## Examples

To return `NULL`, use the following example. The NULLIF function returns `NULL` if the two arguments are the same, so the input argument for the ASCII function is `NULL`. For more information, see [NULLIF function](r_NULLIF_function.md "r_NULLIF_function.md").

```
`SELECT ASCII(NULLIF('',''));`

`+-------+
| ascii |
+-------+
| NULL |
+-------+`
```

To return the ASCII code 0, use the following example.

```
`SELECT ASCII('');`

`+-------+
| ascii |
+-------+
| 0 |
+-------+`
```

To return the ASCII code 97 for the first letter of the word
amazon, use the following example.

```
`SELECT ASCII('amazon');`

`+-------+
| ascii |
+-------+
| 97 |
+-------+`
```

To return the ASCII code 65 for the first letter of the word
Amazon, use the following example.

```
`SELECT ASCII('Amazon');`

`+-------+
| ascii |
+-------+
| 65 |
+-------+`
```
