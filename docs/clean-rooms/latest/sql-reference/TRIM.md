# TRIM function

Trims a string by removing leading and trailing blanks or by removing leading and
trailing characters that match an optional specified string.

## Syntax

```
TRIM( [ BOTH ] [ *trim\_chars* FROM ] string
```

## Arguments

_trim_chars_

(Optional) The characters to be trimmed from the string. If this parameter
is omitted, blanks are trimmed.

_string_

The string to be trimmed.

## Return type

The TRIM function returns a VARCHAR or CHAR string. If you use the TRIM function with
a SQL command, AWS Clean Rooms implicitly converts the results to VARCHAR. If you use the TRIM
function in the SELECT list for a SQL function, AWS Clean Rooms does not implicitly convert the
results, and you might need to perform an explicit conversion to avoid a data type
mismatch error. See the [CAST function](CAST_function.md "CAST_function.md")
function for information about explicit conversions.

## Example

The following example trims leading and trailing blanks from the string `' abc
 '`:

```
`select ' abc ' as untrim, trim(' abc ') as trim;`
`untrim | trim
----------+------
 abc | abc`
```

The following example removes the double quotation marks that surround the string
`"dog"`:

```
`select trim('"' FROM '"dog"');`
`btrim
-------
dog`
```

TRIM removes any of the characters in _trim_chars_ when they
appear at the beginning of _string_. The following example trims the
characters 'C', 'D', and 'G' when they appear at the beginning of VENUENAME, which is a
VARCHAR column.

```
`select venueid, venuename, trim(venuename, 'CDG')
from venue
where venuename like '%Park'
order by 2
limit 7;`
`venueid | venuename | btrim
--------+----------------------------+--------------------------
 121 | ATT Park | ATT Park
 109 | Citizens Bank Park | itizens Bank Park
 102 | Comerica Park | omerica Park
 9 | Dick's Sporting Goods Park | ick's Sporting Goods Park
 97 | Fenway Park | Fenway Park
 112 | Great American Ball Park | reat American Ball Park
 114 | Miller Park | Miller Park`
```
