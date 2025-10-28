# LEN function

Returns the length of the specified string as the number of characters.

## Syntax

LEN is a synonym of [LENGTH function](r_LENGTH.md "r_LENGTH.md"), [CHAR_LENGTH function](r_CHAR_LENGTH.md "r_CHAR_LENGTH.md"), [CHARACTER_LENGTH function](r_CHARACTER_LENGTH.md "r_CHARACTER_LENGTH.md"), and [TEXTLEN function](r_TEXTLEN.md "r_TEXTLEN.md").

```
LEN(*expression*)
```

## Argument

_expression_

The input parameter is a
CHAR or
VARCHAR
or an alias of one of the valid input types.

## Return type

The LEN function returns an integer indicating the number of characters in the input
string.

If the input string is a character string, the LEN function returns the actual number
of characters in multi-byte strings, not the number of bytes. For example, a VARCHAR(12)
column is required to store three four-byte Chinese characters. The LEN function will
return 3 for that same string.

## Usage notes

Length calculations do not count trailing spaces for fixed-length character strings
but do count them for variable-length strings.

## Example

The following example returns the number of bytes and the number of characters in the
string `français`.

```
select octet_length('français'),
len('français');

octet_length  | len
--------------+-----
           9  |   8

```

The following example returns the number of characters in the strings
`cat` with no trailing spaces and `cat` with three trailing
spaces:

```
select len('cat'), len('cat   ');
 len | len
-----+-----
   3 |   6

```

The following example returns the ten longest VENUENAME entries in the VENUE table:

```
select venuename, len(venuename)
from venue
order by 2 desc, 1
limit 10;

venuename                               | len
----------------------------------------+-----
Saratoga Springs Performing Arts Center |  39
Lincoln Center for the Performing Arts  |  38
Nassau Veterans Memorial Coliseum       |  33
Jacksonville Municipal Stadium          |  30
Rangers BallPark in Arlington           |  29
University of Phoenix Stadium           |  29
Circle in the Square Theatre            |  28
Hubert H. Humphrey Metrodome            |  28
Oriole Park at Camden Yards             |  27
Dick's Sporting Goods Park              |  26

```
