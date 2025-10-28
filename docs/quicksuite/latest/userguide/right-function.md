# Right

`right` returns the rightmost characters from a string, including
spaces. You specify the number of characters to be returned.

## Syntax

```
right(`expression`, `limit`)
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like `'12
 Main Street'`, or a call to another function that
outputs a string.

_limit_

The number of characters to be returned from
_expression_, starting from the last
character in the string.

## Return type

String

## Example

The following example returns the last five characters from a string.

```
right('Seattle Store#14', 12)
```

The following value is returned.

```
tle Store#14
```
