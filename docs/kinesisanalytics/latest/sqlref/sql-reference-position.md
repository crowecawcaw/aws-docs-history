# POSITION

```
 POSITION ( <search-string> IN <source-string> )
 search-string := <character-expression>
 source-string := <character-expression>

```

The POSITION function searches for the first input argument (the search string) within the second input argument (the source string).

If the search string is found within the source string, POSITION returns the character position of the first instance of the search string
(subsequent instances are ignored). If the search string is the empty string, POSITION returns 1.

If the search string is not found, POSITION returns 0.

If either the search string or the source string is null, POSITION returns null.

## Examples

| Function                                 | Result |
| ---------------------------------------- | ------ |
| POSITION ('findme' IN '1234findmeXXX')   | 5      |
| POSITION ('findme' IN '1234not-hereXXX') | 0      |
| POSITION ('1' IN '1234567')              | 1      |
| POSITION ('7' IN '1234567')              | 7      |
| POSITION ('' IN '1234567')               | 1      |

## Limitations

Amazon Kinesis Data Analytics streaming SQL does not support the optional USING CHARACTERS | OCTETS clause defined in SQL:2008; USING CHARACTERS is simply assumed. This is a departure from the standard.
