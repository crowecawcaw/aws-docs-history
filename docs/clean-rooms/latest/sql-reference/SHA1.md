# SHA1 function

The SHA1 function uses the SHA1 cryptographic hash function to convert a variable-length
string into a 40-character string that is a text representation of the hexadecimal value of
a 160-bit checksum.

## Syntax

SHA1 is a synonym of [SHA function](SHA.md "SHA.md").

```
SHA1(*string*)
```

## Arguments

_string_

A variable-length string.

## Return type

The SHA1 function returns a 40-character string that is a text representation of the
hexadecimal value of a 160-bit checksum.

## Example

The following example returns the 160-bit value for the word 'AWS Clean Rooms':

```
select sha1('AWS Clean Rooms');

```
