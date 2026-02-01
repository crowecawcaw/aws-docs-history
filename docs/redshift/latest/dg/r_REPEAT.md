Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# REPEAT function

Repeats a string the specified number of times. If the input parameter is numeric,
REPEAT treats it as a string.

Synonym for [REPLICATE function](r_REPLICATE.md "r_REPLICATE.md").

## Syntax

```
REPEAT(*string*, *integer*)
```

## Arguments

_string_

The first input parameter is the string to be repeated.

_integer_

The second parameter is an `INTEGER` indicating the number of times to
repeat the string.

## Return type

VARCHAR

## Examples

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

To repeat the value of the CATID column in the CATEGORY table
three times, use the following example.

```
`SELECT catid, REPEAT(catid,3)
FROM category
ORDER BY 1,2;`

`+-------+--------+
| catid | repeat |
+-------+--------+
| 1 | 111 |
| 2 | 222 |
| 3 | 333 |
| 4 | 444 |
| 5 | 555 |
| 6 | 666 |
| 7 | 777 |
| 8 | 888 |
| 9 | 999 |
| 10 | 101010 |
| 11 | 111111 |
+-------+--------+`
```

The following example demonstrates generating strings up to 16,000,000 bytes:

```
SELECT
    LEN(REPEAT('X', 5000000)) AS five_million_bytes,
    LEN(REPEAT('Y', 16000000)) AS sixteen_million_bytes;

 `five_million_bytes | sixteen_million_bytes
----------+-----------
 5000000 | 16000000`
```
