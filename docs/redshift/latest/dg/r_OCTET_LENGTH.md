

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# OCTET\_LENGTH function
<a name="r_OCTET_LENGTH"></a>

Returns the length of the specified string as the number of bytes. 

## Syntax
<a name="r_OCTET_LENGTH-synopsis"></a>

```
OCTET_LENGTH(expression)
```

## Argument
<a name="r_OCTET_LENGTH-argument"></a>

 *expression*   
A `CHAR` string, a `VARCHAR` string, a `VARBYTE` expression, or an expression that implicitly evaluates to a `CHAR`, `VARCHAR`, or `VARBYTE` type. 

## Return type
<a name="r_OCTET_LENGTH-return-type"></a>

 INTEGER   
The OCTET\_LENGTH function returns an integer indicating the number of bytes in the input string.   
If the input string is a character string, the [LEN](r_LEN.md) function returns the actual number of characters in multi-byte strings, not the number of bytes. For example, a `VARCHAR(12)` column is required to store three four-byte Chinese characters. The OCTET\_LENGTH function will return `12` for that string, and the LEN function will return `3` for that same string.

## Usage notes
<a name="r_OCTET_LENGTH_usage_notes"></a>

If *expression* is a `CHAR` string, the function returns the length of the `CHAR` string. For example, the output of a `CHAR(6)` input is a `CHAR(6)`. 

If *expression* is a `VARCHAR` string, trailing spaces are counted. 

## Examples
<a name="r_OCTET_LENGTH-example"></a>

To return the number of bytes when the string `francais` with three trailing spaces is cast to a `CHAR` and a `VARCHAR` type, use the following example. For more information, see the [CAST function](r_CAST_function.md).

```
SELECT OCTET_LENGTH(CAST('francais   ' AS CHAR(15))) AS octet_length_char, OCTET_LENGTH(CAST('francais   ' AS VARCHAR(15))) AS octet_length_varchar;

+-------------------+----------------------+
| octet_length_char | octet_length_varchar |
+-------------------+----------------------+
|                15 |                   11 |
+-------------------+----------------------+
```

To return the number of bytes and the number of characters in the string `français`, use the following example.

```
SELECT OCTET_LENGTH('français'), LEN('français');

+--------------+-----+
| octet_length | len |
+--------------+-----+
|            9 |   8 |
+--------------+-----+
```

To return the number of bytes when the string `français` is cast as a `VARBYTE`, use the following example.

```
SELECT OCTET_LENGTH(CAST('français' AS VARBYTE));

+--------------+
| octet_length |
+--------------+
|            9 |
+--------------+
```