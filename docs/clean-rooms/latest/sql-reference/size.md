# SIZE function

The SIZE function takes an existing array, map, or string as an argument and returns a
single value representing the size or length of that data structure. It doesn't create a
new data structure. It's used for querying and analyzing the properties of existing data
structures, rather than for creating new ones.

This function is a useful for determining the number of elements in an array or the
length of a string. It can be particularly helpful when working with arrays and other data
structures in SQL, because it allows you to get information about the size or cardinality
of the data.

## Syntax

```
size(expr)
```

## Arguments

_expr_

An ARRAY, MAP, or STRING expression.

## Return type

The SIZE function returns an INTEGER.

## Example

In this example, the SIZE function is applied to the array `['b', 'd', 'c',
 'a']`, and it returns the value `4`, which is the number of elements
in the array.

```
SELECT size(array('b', 'd', 'c', 'a'));
 4
```

In this example, the SIZE function is applied to the map `{'a': 1, 'b':
 2}`, and it returns the value `2`, which is the number of key-value
pairs in the map.

```
SELECT size(map('a', 1, 'b', 2));
 2
```

In this example, the SIZE function is applied to the string `'hello
 world'`, and it returns the value `11`, which is the number of
characters in the string.

```
SELECT size('hello world');
11
```
