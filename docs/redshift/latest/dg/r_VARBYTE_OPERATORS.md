Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# VARBYTE operators

The following table lists the VARBYTE operators.
The operator works with binary value of data type VARBYTE.
If one or both inputs is null, the result is null.

## Supported operators

| Operator | Description           | Return type |
| -------- | --------------------- | ----------- | ------------- | --------- |
| <        | Less than             | `BOOLEAN`   |
| <=       | Less than or equal    | `BOOLEAN`   |
| =        | Equal                 | `BOOLEAN`   |
| >        | Greater than          | `BOOLEAN`   |
| >=       | Greater than or equal | `BOOLEAN`   |
| != or <> | Not equal             | `BOOLEAN`   |
|          |                       |             | Concatenation | `VARBYTE` |
| +        | Concatenation         | `VARBYTE`   |
| ~        | Bitwise not           | `VARBYTE`   |
| &        | Bitwise and           | `VARBYTE`   |
|          |                       | Bitwise or  | `VARBYTE`     |
| #        | Bitwise xor           | `VARBYTE`   |

## Examples

In the following examples, the value of `'a'::VARBYTE` is `61` and
the value of `'b'::VARBYTE` is `62`. The `::` casts the strings into the `VARBYTE` data type. For more information about casting data types, see [CAST](r_CAST_function.md "r_CAST_function.md").

To compare if `'a'` is less than `'b'` using the `<` operator, use the following example.

```
`SELECT 'a'::VARBYTE < 'b'::VARBYTE AS less_than;`

`+-----------+
| less_than |
+-----------+
| true |
+-----------+`
```

To compare if `'a'` equals `'b'` using the `=` operator, use the following example.

```
`SELECT 'a'::VARBYTE = 'b'::VARBYTE AS equal;`

`+-------+
| equal |
+-------+
| false |
+-------+`
```

To concatenate two binary values using the `||` operator, use the following example.

```
`SELECT 'a'::VARBYTE || 'b'::VARBYTE AS concat;`

`+--------+
| concat |
+--------+
| 6162 |
+--------+`
```

To concatenate two binary values using the `+` operator, use the following example.

```
`SELECT 'a'::VARBYTE + 'b'::VARBYTE AS concat;`

`+--------+
| concat |
+--------+
| 6162 |
+--------+`
```

To negate each bit of the input binary value using the FROM_VARBYTE function, use the following example. The string `'a'` evaluates to `01100001`. For more information, see [FROM_VARBYTE](r_FROM_VARBYTE.md "r_FROM_VARBYTE.md").

```
`SELECT FROM_VARBYTE(~'a'::VARBYTE, 'binary');`

`+--------------+
| from_varbyte |
+--------------+
| 10011110 |
+--------------+`
```

To apply the `&` operator on the two input binary values, use the following example. The string `'a'` evaluates to `01100001`
and `'b'` evaluates to `01100010`.

```
`SELECT FROM_VARBYTE('a'::VARBYTE & 'b'::VARBYTE, 'binary');`

`+--------------+
| from_varbyte |
+--------------+
| 01100000 |
+--------------+`
```
