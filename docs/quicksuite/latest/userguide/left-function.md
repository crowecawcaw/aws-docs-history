# Left

`left` returns the leftmost characters from a string, including spaces.
You specify the number of characters to be returned.

## Syntax

```
left(`expression`, `limit`)
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like `'12
 Main Street'`, or a call to another function that
outputs a string.

_limit_

The number of characters to be returned from
_expression_, starting from the first
character in the string.

## Return type

String

## Example

The following example returns the first 3 characters from a string.

```
left('Seattle Store #14', 3)
```

The following value is returned.

```
Sea
```
