

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# OCTETINDEX function
<a name="OCTETINDEX"></a>

The OCTETINDEX function returns the location of a substring within a string as a number of bytes.

## Syntax
<a name="OCTETINDEX-synopsis"></a>

```
OCTETINDEX(substring, string)
```

## Arguments
<a name="OCTETINDEX-arguments"></a>

 *substring*   
A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type. 

 *string*   
A `CHAR` string, a `VARCHAR` string, or an expression that implicitly evaluates to a `CHAR` or `VARCHAR` type. 

## Return type
<a name="OCTETINDEX-return-type"></a>

 INTEGER   
The OCTETINDEX function returns an `INTEGER` value corresponding to the position of the *substring* within the *string* as a number of bytes, where the first character in the *string* is counted as 1. If the *string* doesn't contain multibyte characters, the result is equal to the result of the CHARINDEX function. If the *string* does not contain the *substring*, the function returns `0`. If the *substring* is empty, the function returns `1`. 

## Examples
<a name="OCTETINDEX-examples"></a>

To return the position of the substring `q` in the string `Amazon Redshift`, use the following example. This example returns `0` because the *substring* is not in the *string*.

```
SELECT OCTETINDEX('q', 'Amazon Redshift');

+------------+
| octetindex |
+------------+
|          0 |
+------------+
```

To return the position of an empty substring in the string `Amazon Redshift`, use the following example. This example returns `1` because the *substring* is empty.

```
SELECT OCTETINDEX('', 'Amazon Redshift');

+------------+
| octetindex |
+------------+
|          1 |
+------------+
```

To return the position of the substring `Redshift` in the string `Amazon Redshift`, use the following example. This example returns `8` because the *substring* begins on the eighth byte of the *string*.

```
SELECT OCTETINDEX('Redshift', 'Amazon Redshift');

+------------+
| octetindex |
+------------+
|          8 |
+------------+
```

To return the position of the substring `Redshift` in the string `Amazon Redshift`, use the following example. This example returns `21` because the first six characters of the *string* are double-byte characters.

```
SELECT OCTETINDEX('Redshift', 'Άμαζον Amazon Redshift');

+------------+
| octetindex |
+------------+
|         21 |
+------------+
```