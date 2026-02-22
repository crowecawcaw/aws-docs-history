# Strlen

`strlen` returns the number of characters in a string, including
spaces.

## Syntax

```
strlen(`expression`)
```

## Arguments

_expression_

An expression can be the name of a field that uses the string data
type like `address1`, a literal value like
`'Unknown'`, or another function like
`substring(field_name,0,5)`.

## Return type

Integer

## Example

The following example returns the length of the specified string.

```
strlen('1421 Main Street')
```

The following value is returned.

```
16
```
