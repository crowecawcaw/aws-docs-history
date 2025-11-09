Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TO_HEX function

TO_HEX converts a number or binary value to a hexadecimal representation.

## Syntax

```
TO_HEX(*value*)
```

## Arguments

_value_

Either a number or binary value (`VARBYTE`) to be converted.

## Return type

`VARCHAR`

## Examples

To convert a number to its hexadecimal representation, use the following example.

```
`SELECT TO_HEX(2147676847);`

`+----------+
| to_hex |
+----------+
| 8002f2af |
+----------+`
```

To convert the `VARBYTE` representation of `'abc'` to a hexadecimal number, use the followign example.

```
`SELECT TO_HEX('abc'::VARBYTE);`

`+--------+
| to_hex |
+--------+
| 616263 |
+--------+`
```

To create a table, insert the `VARBYTE` representation of `'abc'` to a hexadecimal number,
and select the column with the value, use the following example.

```
`CREATE TABLE t (vc VARCHAR);
INSERT INTO t SELECT TO_HEX('abc'::VARBYTE);
SELECT vc FROM t;`

`+--------+
| vc |
+--------+
| 616263 |
+--------+`
```

To show that when casting a `VARBYTE` value to `VARCHAR` the format is UTF-8, use the following example.

```
`CREATE TABLE t (vc VARCHAR);
INSERT INTO t SELECT 'abc'::VARBYTE::VARCHAR;

SELECT vc FROM t;`

`+-----+
| vc |
+-----+
| abc |
+-----+`
```
