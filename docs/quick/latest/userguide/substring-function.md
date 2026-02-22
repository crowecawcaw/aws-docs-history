# Substring

`substring` returns the characters in a string, starting at the
location specified by the _start_ argument and proceeding for the
number of characters specified by the _length_ arguments.

## Syntax

```
substring(`expression`, `start`, `length`)
```

## Arguments

_expression_

An expression can be the name of a field that uses the string data
type like `address1`, a literal value like
`'Unknown'`, or another function like
`substring(field_name,1,5)`.

_start_

The character location to start from. _start_
is inclusive, so the character at the starting position is the first
character in the returned value. The minimum value for _start_ is 1.

_length_

The number of additional characters to include after
_start_. _length_ is
inclusive of _start_, so the last character
returned is (_length_ - 1) after the starting
character.

## Return type

String

## Example

The following example returns the 13th through 19th characters in a string.
The beginning of the string is index 1, so you begin counting at the first
character.

```
substring('Fantasy and Science Fiction',13,7)
```

The following value is returned.

```
Science
```
