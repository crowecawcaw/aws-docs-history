# Replace

`replace` replaces part of a string with another string that you
specify.

## Syntax

```
replace(`expression`, `substring`, `replacement`)
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like `'12
 Main Street'`, or a call to another function that
outputs a string.

_substring_

The set of characters in _expression_ that you
want to replace. The substring can occur one or more times in
_expression_.

_replacement_

The string you want to have substituted for
_substring_.

## Return type

String

## Example

The following example replaces the substring 'and' with 'or'.

```
replace('1 and 2 and 3', 'and', 'or')
```

The following string is returned.

```
1 or 2 or 3
```
