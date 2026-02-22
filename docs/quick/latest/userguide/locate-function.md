# Locate

`locate` locates a substring that you specify within another string,
and returns the number of characters until the first character in the substring. The
function returns 0 if it doesn't find the substring. The function is 1-based.

## Syntax

```
locate(`expression`, `substring`, `start`)
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like `'12
 Main Street'`, or a call to another function that
outputs a string.

_substring_

The set of characters in _expression_ that you
want to locate. The substring can occur one or more times in
_expression_.

_start_

(Optional) If _substring_ occurs more than
once, use _start_ to identify where in the string
the function should start looking for the substring. For example,
suppose that you want to find the second example of a substring and
you think it typically occurs after the first 10 characters. You
specify a _start_ value of 10. It should start
from 1.

## Return type

Integer

## Examples

The following example returns information about where the first occurrence of
the substring 'and' appears in a string.

```
locate('1 and 2 and 3 and 4', 'and')
```

The following value is returned.

```
3
```

The following example returns information about where the first occurrence of
the substring 'and' appears in a string after the fourth character.

```
locate('1 and 2 and 3 and 4', 'and', 4)
```

The following value is returned.

```
9
```
