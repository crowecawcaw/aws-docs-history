

# MD5 function
<a name="s_MD5"></a>

Uses the MD5 cryptographic hash function to convert a variable-length string into a 32-character string that is a text representation of the hexadecimal value of a 128-bit checksum. 

## Syntax
<a name="s_MD5-syntax"></a>

```
MD5(string)
```

## Arguments
<a name="s_MD5-arguments"></a>

 *string*   
A variable-length string.

## Return type
<a name="s_MD5-return-type"></a>

The MD5 function returns a 32-character string that is a text representation of the hexadecimal value of a 128-bit checksum.

## Examples
<a name="s_MD5-examples"></a>

The following example shows the 128-bit value for the string 'AWS Clean Rooms': 

```
select md5('AWS Clean Rooms');
md5
----------------------------------
f7415e33f972c03abd4f3fed36748f7a
(1 row)
```