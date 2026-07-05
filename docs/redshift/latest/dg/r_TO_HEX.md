Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# TO\_HEX function

TO\_HEX converts a number or binary value to a hexadecimal representation.

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
