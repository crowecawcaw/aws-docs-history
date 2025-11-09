# CHAR_LENGTH / CHARACTER_LENGTH

```
 CHAR_LENGTH | CHARACTER_LENGTH ( <character-expression> )

```

Returns the length in characters of the string passed as the input argument. Returns null if
input argument is null.

## Examples

|                                                         |        |
| ------------------------------------------------------- | ------ |
| `<br>CHAR_LENGTH('one')<br>`                            | `3`    |
| `<br>CHAR_LENGTH('')<br>`                               | `0`    |
| `<br>CHARACTER_LENGTH('fred')<br>`                      | `4`    |
| `<br>CHARACTER_LENGTH( cast (null as varchar(16) )<br>` | `null` |
| `<br>CHARACTER_LENGTH( cast ('fred' as char(16) )<br>`  | `16`   |

## Limitations

Amazon Kinesis Data Analytics streaming SQL does not support the optional USING CHARACTERS | OCTETS clause.
This is a departure from the SQL:2008 standard.
