Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CRC32 function

CRC32 is a function used for error detection. The function uses a CRC32 algorithm to detect changes
between source and target data. The CRC32 function converts a variable-length string
into an 8-character string that is a text representation of the hexadecimal value of a
32 bit-binary sequence. To detect changes between source and target data, use the CRC32
function on the source data and store the output. Then, use the CRC32 function on the
target data and compare that output to the output from the source data.
The outputs will be the same if the data was not modified, and the outputs will be
different if the data was modified.

## Syntax

```
CRC32(*string*)
```

## Arguments

_string_

A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type.

## Return type

The CRC32 function returns an 8-character string that is a text representation of
the hexadecimal value of a 32-bit binary sequence. The Amazon Redshift CRC32 function is
based on the CRC-32C polynomial.

## Examples

To show the 8-bit value for the string `Amazon Redshift`.

````
`SELECT CRC32('Amazon Redshift');`

`+----------+
| crc32 | +----------+
| f2726906 | +----------+` ```
````
