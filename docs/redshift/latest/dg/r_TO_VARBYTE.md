

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TO\_VARBYTE function
<a name="r_TO_VARBYTE"></a>

TO\_VARBYTE converts a string in a specified format to a binary value. 

## Syntax
<a name="r_TO_VARBYTE-synopsis"></a>

```
TO_VARBYTE(string, format)
```

## Arguments
<a name="r_TO_VARBYTE-arguments"></a>

 *string*   
A `CHAR` or `VARCHAR` string. 

 *format*   
The format of the input string. Case insensitive valid values are `hex`, `binary`, `utf8` (also `utf-8` and `utf_8`), and `base64`. 

## Return type
<a name="r_TO_VARBYTE-return-type"></a>

`VARBYTE`

## Examples
<a name="r_TO_VARBYTE-examples"></a>

To convert the hex `6162` to a binary value, use the following example. The result is automatically shown as the hexadecimal representation of the binary value.

```
SELECT TO_VARBYTE('6162', 'hex');
               
+------------+
| to_varbyte |
+------------+
|       6162 |
+------------+
```

To return the binary representation of `4d`, use the following example. The binary representation of '4d' is `01001101`.

```
SELECT TO_VARBYTE('01001101', 'binary');
               
+------------+
| to_varbyte |
+------------+
|         4d |
+------------+
```

To convert the string `'a'` in UTF-8 to a binary value, use the following example. The result is automatically shown as the hexadecimal representation of the binary value.

```
SELECT TO_VARBYTE('a', 'utf8');
               
+------------+
| to_varbyte |
+------------+
|         61 |
+------------+
```

To convert the string `'4'` in hexadecimal to a binary value, use the following example. If the hexadecimal string length is an odd number, then a `0` is prepended to form a valid hexadecimal number.

```
SELECT TO_VARBYTE('4', 'hex');
               
+------------+
| to_varbyte |
+------------+
|         04 |
+------------+
```