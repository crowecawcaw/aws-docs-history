

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# GETBIT function
<a name="r_GETBIT"></a>

GETBIT returns the bit value of a binary value at the specified index. 

## Syntax
<a name="r_GETBIT-synopsis"></a>

```
GETBIT(binary_value, index)
```

## Arguments
<a name="r_GETBIT-arguments"></a>

 *binary\_value*   
A binary value of data type `VARBYTE`. 

 *index*   
An index number of the bit in the binary value that is returned. The binary value is a 0-based bit array that is indexed from the rightmost bit (least significant bit) to the leftmost bit (most significant bit).

## Return type
<a name="r_GETBIT-return-type"></a>

`INTEGER`

## Examples
<a name="r_GETBIT-examples"></a>

To return the bit at index `2` of the binary value `from_hex('4d')`, use the following example. The binary representation of `'4d'` is `01001101`.

```
SELECT GETBIT(FROM_HEX('4d'), 2);
               
+--------+
| getbit |
+--------+
|      1 |
+--------+
```

To return the bit at eight index locations of the binary value returned by `from_hex('4d')`, use the following example. The binary representation of `'4d'` is `01001101`.

```
SELECT GETBIT(FROM_HEX('4d'), 7), GETBIT(FROM_HEX('4d'), 6),
  GETBIT(FROM_HEX('4d'), 5), GETBIT(FROM_HEX('4d'), 4),
  GETBIT(FROM_HEX('4d'), 3), GETBIT(FROM_HEX('4d'), 2),
  GETBIT(FROM_HEX('4d'), 1), GETBIT(FROM_HEX('4d'), 0);
               
+--------+--------+--------+--------+--------+--------+--------+--------+
| getbit | getbit | getbit | getbit | getbit | getbit | getbit | getbit |
+--------+--------+--------+--------+--------+--------+--------+--------+
|      0 |      1 |      0 |      0 |      1 |      1 |      0 |      1 |
+--------+--------+--------+--------+--------+--------+--------+--------+
```