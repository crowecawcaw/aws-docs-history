

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# FROM\_VARBYTE function
<a name="r_FROM_VARBYTE"></a>

FROM\_VARBYTE converts a binary value to a character string in the specified format. 

## Syntax
<a name="r_FROM_VARBYTE-synopsis"></a>

```
FROM_VARBYTE(binary_value, format)
```

## Arguments
<a name="r_FROM_VARBYTE-arguments"></a>

 *binary\_value*   
A binary value of data type `VARBYTE`. 

 *format*   
The format of the returned character string. Case insensitive valid values are `hex`, `binary`, `utf8` (also `utf-8` and `utf_8`), and `base64`. 

## Return type
<a name="r_FROM_VARBYTE-return-type"></a>

`VARCHAR`

## Examples
<a name="r_FROM_VARBYTE-examples"></a>

To convert the binary value `'ab'` to hexadecimal, use the following example. 

```
SELECT FROM_VARBYTE('ab', 'hex');
               
+--------------+
| from_varbyte |
+--------------+
|         6162 |
+--------------+
```

To return the binary representation of `'4d'`, use the following example. The binary representation of `'4d'` is the character string `01001101`.

```
SELECT FROM_VARBYTE(FROM_HEX('4d'), 'binary');
               
+--------------+
| from_varbyte |
+--------------+
|     01001101 |
+--------------+
```