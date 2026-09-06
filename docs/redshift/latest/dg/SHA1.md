

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHA1 function
<a name="SHA1"></a>

The SHA1 function uses the SHA1 cryptographic hash function to convert a variable-length string into a 40-character string that is a text representation of the hexadecimal value of a 160-bit checksum.

## Syntax
<a name="SHA1-syntax"></a>

SHA1 is a synonym of [SHA function](SHA.md) and [FUNC\_SHA1 function](FUNC_SHA1.md). 

```
SHA1(string)
```

## Arguments
<a name="SHA1-arguments"></a>

 *string*   
A variable-length string.

## Return type
<a name="SHA1-returm-type"></a>

The SHA1 function returns a 40-character string that is a text representation of the hexadecimal value of a 160-bit checksum. 

## Example
<a name="SHA1-example"></a>

The following example returns the 160-bit value for the word 'Amazon Redshift': 

```
select sha1('Amazon Redshift');
```