Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# JSON_SIZE function

The JSON_SIZE function returns the number of bytes in the
given `SUPER` expression when serialized into a string.

## Syntax

```
JSON_SIZE(*super\_expression*)

```

## Arguments

_super_expression_

A `SUPER` constant or expression.

## Return type

`INTEGER`

The JSON_SIZE function returns an `INTEGER` indicating
the number of bytes in the input string. This value is
different from the number of characters. For example,
the UTF-8 character ⬤, a black dot, is 3 bytes in size even though it is 1 character.

## Usage notes

JSON_SIZE(x) is functionally identical to
OCTET_LENGTH(JSON_SERIALIZE). However, note that JSON_SERIALIZE returns an error when
the provided `SUPER` expression would exceed the `VARCHAR` limit of the
system when serialized. JSON_SIZE does not have this limitation.

## Examples

To return the length of
a `SUPER` value serialized to a string, use the following example.

```
`SELECT JSON_SIZE(JSON_PARSE('[10001,10002,"⬤"]'));`

`+-----------+
| json_size |
+-----------+
| 19 |
+-----------+`
```

Note that the provided `SUPER` expression is 17 characters long, but
⬤ is a 3-byte character, so JSON_SIZE returns `19`.
