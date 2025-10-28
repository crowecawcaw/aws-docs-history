# STR_TO_MAP function

The STR_TO_MAP function is a string-to-map conversion function. It converts a string
representation of a map (or dictionary) into an actual map data structure.

This function is useful when you need to work with map data structures in SQL, but the
data is initially stored as a string. By converting the string representation to an actual
map, you can then perform operations and manipulations on the map data.

## Syntax

```
str_to_map(text[, pairDelim[, keyValueDelim]])
```

## Arguments

_text_

A STRING expression that represents the map.

_pairDelim_

An optional STRING literal that specifies how to separate entries. It
defaults to a comma (`','`).

_keyValueDelim_

An optional STRING literal that specifies how to separate each key-value
pair. It defaults to a colon (`':'`).

## Return type

The STR_TO_MAP function returns a MAP of STRING for both keys and values. Both
_pairDelim_ and _keyValueDelim_ are treated as
regular expressions.

## Example

The following example takes the input string and the two delimiter arguments, and
converts the string representation into an actual map data structure. In this specific
example, the input string `'a:1,b:2,c:3'` represents a map with the following
key-value pairs: `'a'` is the key, and `'1'` is the value.
`'b'` is the key, and `'2'` is the value. `'c'` is
the key, and `'3'` is the value. The `','` delimiter is used to
separate the key-value pairs, and the `':'` delimiter is used to separate the
key and value within each pair. The output of this query is:
`{"a":"1","b":"2","c":"3"}`. This is the resulting map data structure,
where the keys are `'a'`, `'b'`, and `'c'`, and the
corresponding values are `'1'`, `'2'`, and
`'3'`.

```
SELECT str_to_map('a:1,b:2,c:3', ',', ':');
 {"a":"1","b":"2","c":"3"}
```

The following example demonstrates that the STR_TO_MAP function expects the input
string to be in a specific format, with the key-value pairs delimited correctly. If the
input string doesn't match the expected format, the function will still attempt to
create a map, but the resulting values may not be as expected.

```
SELECT str_to_map('a');
 {"a":null}
```
