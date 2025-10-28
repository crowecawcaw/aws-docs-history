# SUBSTRING

```
 SUBSTRING ( <source-string> FROM <start-position> [ FOR <string-length> ] )
 SUBSTRING ( <source-string>, <start-position> [ , <string-length> ] )
 SUBSTRING ( <source-string> SIMILAR <pattern> ESCAPE <escape-char> )
 <source-string> := <character-expression>
 <start-position> := <integer-expression>
 <string-length> := <integer-expression>
 <regex-expression> := <character-expression>
 <pattern> := <character-expression>
 <escape-char> := <character-expression>

```

SUBSTRING extracts a portion of the source string specified in the first argument.
Extraction starts at the value of _start-position_ or the first expression matching
the value of _regex-expression_.

If a value is specified for _string-length_, only that number of characters is
returned. If there aren't that many characters left in the string, only the characters that are
left are returned. If _string-length_ is not specified, the string length defaults to
the remaining length of the input string.

If the start position is less than 1, then the start position is interpreted as if it is 1
and the string length is reduced by (1–start position). For examples, see following. If
the start position is greater than the number of characters in the string, or the length
parameter is 0, the result is an empty string.

## Parameters

_source-string_

The string to search for positional or regular-expression matches.

_start-position_

The first character of _source-string_ to return. If _start-position_ is greater than the length of _source-string_, SUBSTRING returns null.

_string-length_

The number of characters from _source-string_ to return.

_regex-expression_

A pattern of characters to match and return from _source-string_. Only the first match is returned.

_pattern_

A three-part pattern of characters that consists of the following:

- The string to be found before the returned substring
- The returned substring
- The string to be found after the returned substring

The parts are delimited by a double quotation mark (") and a specified escape character.
For more information, see [Similar...Escape](#sql-reference-substring-examples-similar "#sql-reference-substring-examples-similar") Samples following.

## Examples

### FROM/ FOR

| Function                                                    | Result         |
| ----------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SUBSTRING('123456789' FROM 3 FOR 4)                         | 3456           |
| SUBSTRING('123456789' FROM 17 FOR 4)                        | <empty string> |
| SUBSTRING('123456789' FROM -1 FOR 4)                        | 12             |
| SUBSTRING('123456789' FROM 6 FOR 0)                         | <empty string> |
| SUBSTRING('123456789' FROM 8 FOR 4)                         | 89             | ### FROM Regex                                                                                            |
| Function                                                    | Result         |
| ---                                                         | ---            |
| SUBSTRING('TECHNOLOGY' FROM 'L[A-Z]\*')                     | LOGY           |
| SUBSTRING('TECHNOLOGY' FROM 'FOO')                          | null           |
| SUBSTRING('TECHNOLOGY' FROM 'O[A-Z]')                       | OL             | ### Numeric                                                                                               |
| Function                                                    | Result         |
| ---                                                         | ---            |
| SUBSTRING('123456789', 3, 4)                                | 3456           |
| SUBSTRING('123456789', 7, 4)                                | 789            |
| SUBSTRING('123456789', 10, 4)                               | null           | ### Similar...Escape                                                                                      |
| Function                                                    | Result         |
| ---                                                         | ---            |
| SUBSTRING('123456789' SIMILAR '23#"456#"78' ESCAPE '#')     | 456            |
| SUBSTRING('TECHNOLOGY' SIMILAR 'TECH%"NOLO%"GY' ESCAPE '%') | NOLO           | ## Notes <br>• Amazon Kinesis Data Analytics streaming SQL doesn't support the optional 'USING CHARACTERS | OCTETS' clause defined in SQL:2008. USING CHARACTERS is simply assumed. <br>• The second and third forms of the SUBSTRING function listed preceding (using a regular expression, and using commas rather than FROM...FOR) are not part of the SQL:2008 standard. They are part of the streaming SQL extension to Amazon Kinesis Data Analytics. |
