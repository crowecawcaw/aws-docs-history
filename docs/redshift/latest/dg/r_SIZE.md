Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SIZE

Returns the binary in-memory size of a `SUPER` type constant or expression as an `INTEGER`.

## Syntax

```
SIZE(*super\_expression*)
```

## Arguments

_super_expression_

A `SUPER` type constant or expression.

## Return type

`INTEGER`

## Examples

To use SIZE to get the in-memory size of several `SUPER` type expressions, use the following example.

````
`CREATE TABLE test_super_size(a SUPER);

INSERT INTO test_super_size
VALUES
 (null),
 (TRUE),
 (JSON_PARSE('[0,1,2,3]')),
 (JSON_PARSE('{"a":0,"b":1,"c":2,"d":3}'))
;

SELECT a, SIZE(a)
FROM test_super_size
ORDER BY 2, 1;`

`+---------------------------+------+
| a | size | +---------------------------+------+
| true | 4 |
| NULL | 4 |
| [0,1,2,3] | 23 |
| {"a":0,"b":1,"c":2,"d":3} | 52 | +---------------------------+------+` ```
````
