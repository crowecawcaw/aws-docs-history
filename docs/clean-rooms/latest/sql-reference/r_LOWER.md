# LOWER function

Converts a string to lowercase. LOWER supports UTF-8 multibyte characters, up to a
maximum of four bytes per character.

## Syntax

```
LOWER(*string*)
```

## Argument

_string_

The input parameter is a VARCHAR string (or any other data type, such as
CHAR, that can be implicitly converted to VARCHAR).

## Return type

The LOWER function returns a character string that is the same data type as the input
string.

## Examples

The following example converts the CATNAME field to lowercase:

```
select catname, lower(catname) from category order by 1,2;

 catname  |   lower
----------+-----------
Classical | classical
Jazz      | jazz
MLB       | mlb
MLS       | mls
Musicals  | musicals
NBA       | nba
NFL       | nfl
NHL       | nhl
Opera     | opera
Plays     | plays
Pop       | pop
(11 rows)
```
