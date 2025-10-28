# TRIM

```
TRIM ( [ [ <trim-specification> ] [ <trim-character> ] FROM ] <trim-source> )
 <trim-specification> := LEADING | TRAILING | BOTH
 <trim-character> := <character-expression>
 <trim-source> := <character-expression>
```

TRIM removes instances of the specified trim-character from the beginning and/or end of the trim-source string as dictated by the trim-specification (that is, LEADING, TRAILING, or BOTH). If LEADING is specified, only repetitions of the trim character at the beginning of the source string are removed. If TRAILING is specified, only repetitions of the trim character at the end of the source string are removed. If BOTH is specified, or the trim specifier is left out entirely, then repetitions are removed from both the beginning and end of the source string.

If the trim-character is not explicitly specified, it defaults to the space character (' '). Only one trim character is allowed; specifying an empty string or a string longer than one character results in an exception.

If either input is null, null is returned.

## Examples

| Function                                       | Result                  |
| ---------------------------------------------- | ----------------------- |
| `TRIM(' Trim front and back ')`                | `'Trim front and back'` |
| `TRIM (BOTH FROM ' Trim front and back ')`     | `'Trim front and back'` |
| `TRIM (BOTH ' ' FROM ' Trim front and back ')` | `'Trim front and back'` |
| `TRIM (LEADING 'x' FROM 'xxxTrim frontxxx')`   | `'Trim frontxxx'`       |
| `TRIM (TRAILING 'x' FROM 'xxxTrimxBackxxx')`   | `'xxxTrimxBack'`        |
| `TRIM (BOTH 'y' FROM 'xxxNo y to trimxxx')`    | `'xxxNo y to trimxxx'`  |
