

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# MD5 function
<a name="r_MD5"></a>

Uses the MD5 cryptographic hash function to convert a variable-length string into a 32-character string that is a text representation of the hexadecimal value of a 128-bit checksum. 

## Syntax
<a name="r_MD5-syntax"></a>

```
MD5(string)
```

## Arguments
<a name="r_MD5-arguments"></a>

 *string*   
A variable-length string.

## Return type
<a name="r_MD5-return-type"></a>

The MD5 function returns a 32-character string that is a text representation of the hexadecimal value of a 128-bit checksum.

## Examples
<a name="r_MD5-examples"></a>

The following example shows the 128-bit value for the string 'Amazon Redshift': 

```
select md5('Amazon Redshift');
md5
----------------------------------
f7415e33f972c03abd4f3fed36748f7a
(1 row)
```