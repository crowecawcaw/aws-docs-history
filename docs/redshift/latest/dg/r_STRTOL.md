

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STRTOL function
<a name="r_STRTOL"></a>

Converts a string expression of a number of the specified base to the equivalent integer value. The converted value must be within the signed 64-bit range. 

## Syntax
<a name="r_STRTOL-syntax"></a>

```
STRTOL(num_string, base)
```

## Arguments
<a name="r_STRTOL-arguments"></a>

 *num\_string*   
String expression of a number to be converted. If *num\_string* is empty ( `''` ) or begins with the null character (`'\0'`), the converted value is `0`. If *num\_string* is a column containing a NULL value, STRTOL returns `NULL`. The string can begin with any amount of white space, optionally followed by a single plus '`+`' or minus '`-`' sign to indicate positive or negative. The default is '`+`'. If *base* is `16`, the string can optionally begin with '`0x`'. 

*base*  
`INTEGER` between 2 and 36.

## Return type
<a name="r_STRTOL-return-type"></a>

BIGINT  
If *num\_string* is null, the function returns `NULL`.

## Examples
<a name="r_STRTOL-examples"></a>

To convert string and base value pairs to integers, use the following examples.

```
SELECT STRTOL('0xf',16);

+--------+
| strtol |
+--------+
|     15 |
+--------+

SELECT STRTOL('abcd1234',16);

+------------+
|   strtol   |
+------------+
| 2882343476 |
+------------+

SELECT STRTOL('1234567', 10);

+---------+
| strtol  |
+---------+
| 1234567 |
+---------+

SELECT STRTOL('1234567', 8);

+--------+
| strtol |
+--------+
| 342391 |
+--------+

SELECT STRTOL('110101', 2);

+--------+
| strtol |
+--------+
|     53 |
+--------+

SELECT STRTOL('\0', 2);

+--------+
| strtol |
+--------+
|      0 |
+--------+
```