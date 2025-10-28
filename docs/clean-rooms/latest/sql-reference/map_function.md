# MAP constructor function

The MAP constructor function creates a map with the given key/value pairs.

Constructor functions like MAP are useful when you need to create new data structures
programmatically within your SQL queries. They allow you to build complex data structures
that can be used in further data processing or analysis.

## Syntax

```
map(key0, value0, key1, value1, ...)
```

## Arguments

_key0_

An expression of any comparable type. All _key0_ must share a least common type.

_value0_

An expression of any type. All _valueN_
must share a least common type.

## Returns

The MAP function returns a MAP with keys typed as the least common type of _key0_ and values typed as the least common type of
_value0_.

## Examples

The following example creates a new map with two key-value pairs: The key
`1.0` is associated with the value `'2'`. The key
`3.0` is associated with the value `'4'`. The resulting map is
then returned as the output of the SQL statement.

```
SELECT map(1.0, '2', 3.0, '4');
 {1.0:"2",3.0:"4"}
```
