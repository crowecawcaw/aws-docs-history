# ARRAY_JOIN function

The ARRAY_JOIN function takes two arguments: The first argument is the input array that
will be joined. The second argument is the separator string that will be used to
concatenate the array elements. This function is useful when you need to convert an array
of strings (or any other data type) into a single concatenated string. This can be helpful
in scenarios where you want to present an array of values as a single formatted string,
such as for display purposes or for use in further processing.

## Syntax

```
array_join(array, delimiter[, nullReplacement])
```

## Arguments

_array_

Any ARRAY type, but its elements are interpreted as strings.

_delimiter_

A STRING used to separate the concatenated array elements.

_nullReplacement_

A STRING used to express a NULL value in the result.

## Return type

The ARRAY_JOIN function returns a STRING where the elements of array are separated by
delimiter and null elements are substituted for `nullReplacement`. If
`nullReplacement` is omitted, `null` elements are filtered out.
If any argument is `NULL`, the result is `NULL`.

## Examples

In this example, the ARRAY_JOIN function takes the array `['hello',
 'world']` and joins the elements using the separator `' '` (a space
character). The resulting output is the string `'hello world'`.

```
SELECT array_join(array('hello', 'world'), ' ');
 hello world
```

In this example, the ARRAY_JOIN function takes the array `['hello', null,
 'world']` and joins the elements using the separator `' '` (a space
character). The `null` value is replaced with the provided replacement string
`','` (a comma). The resulting output is the string `'hello ,
 world'`.

```
SELECT array_join(array('hello', null ,'world'), ' ', ',');
 hello , world
```
