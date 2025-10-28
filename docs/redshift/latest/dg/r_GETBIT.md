Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GETBIT function

GETBIT returns the bit value of a binary value at the specified index.

## Syntax

```
GETBIT(*binary\_value*, *index*)
```

## Arguments

_binary_value_

A binary value of data type `VARBYTE`.

_index_

An index number of the bit in the binary value that is returned. The binary value is a 0-based bit array that is indexed
from the rightmost bit (least significant bit) to the leftmost bit (most significant bit).

## Return type

`INTEGER`

## Examples

To return the bit at index `2` of the binary value `from_hex('4d')`, use the following example.
The binary representation of `'4d'` is `01001101`.

````
`SELECT GETBIT(FROM_HEX('4d'), 2);`

`+--------+
| getbit | +--------+
| 1 | +--------+` ``` To return the bit at eight index locations of the binary value returned by `from_hex('4d')`, use the following example. The binary representation of `'4d'` is `01001101`. ``` `SELECT GETBIT(FROM_HEX('4d'), 7), GETBIT(FROM_HEX('4d'), 6), GETBIT(FROM_HEX('4d'), 5), GETBIT(FROM_HEX('4d'), 4), GETBIT(FROM_HEX('4d'), 3), GETBIT(FROM_HEX('4d'), 2), GETBIT(FROM_HEX('4d'), 1), GETBIT(FROM_HEX('4d'), 0);` `+--------+--------+--------+--------+--------+--------+--------+--------+
| getbit | getbit | getbit | getbit | getbit | getbit | getbit | getbit | +--------+--------+--------+--------+--------+--------+--------+--------+
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | +--------+--------+--------+--------+--------+--------+--------+--------+` ```
````
