

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# REPEAT function
<a name="r_REPEAT"></a>

Repeats a string the specified number of times. If the input parameter is numeric, REPEAT treats it as a string. 

Synonym for [REPLICATE function](r_REPLICATE.md). 

## Syntax
<a name="r_REPEAT-synopsis"></a>

```
REPEAT(string, integer)
```

## Arguments
<a name="r_REPEAT-arguments"></a>

 *string*   
The first input parameter is the string to be repeated. 

 *integer*   
The second parameter is an `INTEGER` indicating the number of times to repeat the string. 

## Return type
<a name="r_REPEAT-return-type"></a>

VARCHAR

## Examples
<a name="r_REPEAT-examples"></a>

The following example uses data from the CATEGORY table in the TICKIT sample database. For more information, see [Sample database](c_sampledb.md). 

To repeat the value of the CATID column in the CATEGORY table three times, use the following example. 

```
SELECT catid, REPEAT(catid,3)
FROM category
ORDER BY 1,2;

+-------+--------+
| catid | repeat |
+-------+--------+
|     1 |    111 |
|     2 |    222 |
|     3 |    333 |
|     4 |    444 |
|     5 |    555 |
|     6 |    666 |
|     7 |    777 |
|     8 |    888 |
|     9 |    999 |
|    10 | 101010 |
|    11 | 111111 |
+-------+--------+
```

The following example demonstrates generating strings up to 16,000,000 bytes:

```
SELECT 
    LEN(REPEAT('X', 5000000)) AS five_million_bytes,
    LEN(REPEAT('Y', 16000000)) AS sixteen_million_bytes;

 five_million_bytes  | sixteen_million_bytes
----------+-----------
 5000000  | 16000000
```