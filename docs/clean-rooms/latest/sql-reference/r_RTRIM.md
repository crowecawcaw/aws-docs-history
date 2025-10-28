# RTRIM function

The RTRIM function trims a specified set of characters from the end of a string. Removes
the longest string containing only characters in the trim characters list. Trimming is
complete when a trim character
doesn't
appear in the input string.

## Syntax

```
RTRIM( *string*, *trim\_chars* )
```

## Arguments

_string_

A string column, expression, or string literal to be trimmed.

_trim_chars_

A string column, expression, or string literal that represents the
characters to be trimmed from the end of _string_. If not
specified, a space is used as the trim character.

## Return type

A string that is the same data type as the _string_
argument.

## Example

The following example trims leading and trailing blanks from the string `' abc
 '`:

```
`select ' abc ' as untrim, rtrim(' abc ') as trim;`
`untrim | trim
----------+------
 abc | abc`
```

The following example removes the trailing `'xyz'` strings from the string
`'xyzaxyzbxyzcxyz'`. The trailing occurrences of `'xyz'` are
removed, but occurrences that are internal within the string are not removed.

```
`select 'xyzaxyzbxyzcxyz' as untrim,
rtrim('xyzaxyzbxyzcxyz', 'xyz') as trim;`
`untrim | trim
-----------------+-----------
 xyzaxyzbxyzcxyz | xyzaxyzbxyzc`
```

The following example removes the trailing parts from the string
`'setuphistorycassettes'` that match any of the characters in the
_trim_chars_ list `'tes'`. Any `t`,
`e`, or `s` that occur before another character that is not in
the _trim_chars_ list at the ending of the input string are removed.

```
`SELECT rtrim('setuphistorycassettes', 'tes');`
`rtrim
-----------------
 setuphistoryca`
```

The following example trims the characters 'Park' from the end of VENUENAME where
present:

```
`select venueid, venuename, rtrim(venuename, 'Park')
from venue
order by 1, 2, 3
limit 10;`
`venueid | venuename | rtrim
--------+----------------------------+-------------------------
 1 | Toyota Park | Toyota
 2 | Columbus Crew Stadium | Columbus Crew Stadium
 3 | RFK Stadium | RFK Stadium
 4 | CommunityAmerica Ballpark | CommunityAmerica Ballp
 5 | Gillette Stadium | Gillette Stadium
 6 | New York Giants Stadium | New York Giants Stadium
 7 | BMO Field | BMO Field
 8 | The Home Depot Center | The Home Depot Cente
 9 | Dick's Sporting Goods Park | Dick's Sporting Goods
 10 | Pizza Hut Park | Pizza Hut`
```

Note that RTRIM removes any of the characters `P`, `a`,
`r`, or `k` when they appear at the end of a VENUENAME.
