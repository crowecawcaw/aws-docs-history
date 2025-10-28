# OVERLAY

```
 OVERLAY ( <original-string>
           PLACING <replacement-string>
           FROM <start-position>
           [ FOR <string-length> ]
         )
 <original-string> := <character-expression>
 <replacement-string> := <character-expression>
 <start-position> := <integer-expression>
 <string-length> := <integer-expression>

```

The OVERLAY function is used to replace a portion of the first string argument (the original string) with the second string argument (the replacement string).

The start position indicates the character position in the original string where the replacement string should be overlaid. The optional string length parameter determines how many characters of the original string to replace (if not specified, it defaults to the length of the replacement string). If there are more characters in the replacement string than are left in the original string, the remaining characters are simply appended.

If the start position is greater than the length of the original string, the replacement string is simply appended. If the start position is less than 1, then ( 1 - start position) characters of the replacement string is prepended to the result, and the rest overlaid on the original (see examples below).

If the string length is less than zero, an exception is raised.

If any of the input arguments are null, the result is null.

## Examples

| Function                                     | Result   |
| -------------------------------------------- | -------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OVERLAY ('12345' PLACING 'foo' FROM 1)       | foo45    |
| OVERLAY ('12345' PLACING 'foo' FROM 0)       | foo345   |
| OVERLAY ('12345' PLACING 'foo' FROM -2)      | foo12345 |
| OVERLAY ('12345' PLACING 'foo' FROM 4)       | 123foo   |
| OVERLAY ('12345' PLACING 'foo' FROM 17)      | 12345foo |
| OVERLAY ('12345' PLACING 'foo' FROM 2 FOR 0) | 1foo2345 |
| OVERLAY ('12345' PLACING 'foo' FROM 2 FOR 2) | 1foo45   |
| OVERLAY ('12345' PLACING 'foo' FROM 2 FOR 9) | 1foo     | ## Limitations Amazon Kinesis Data Analytics does not support the optional USING CHARACTERS | OCTETS clause defined in SQL:2008; USING CHARACTERS is simply assumed. Strict SQL:2008 also requires that a start position less than 1 return a null result, rather than the behavior described above. These are departures from the standard. |
