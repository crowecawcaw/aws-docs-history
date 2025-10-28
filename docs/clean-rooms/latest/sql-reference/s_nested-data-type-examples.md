# Examples of nested data types

For the `struct<given:varchar, family:varchar>` type, there are two
attribute names: `given`, and `family`, each corresponding to a
`varchar` value.

For the `array<varchar>` type, the array is specified as a list of
`varchar`.

The `array<struct<shipdate:timestamp, price:double>>` type refers to
a list of elements with `struct<shipdate:timestamp, price:double>` type.

The `map` data type behaves like an `array` of
`structs`, where the attribute name for each element in the array is
denoted by `key` and it maps to a `value`.

For example, the `map<varchar(20), varchar(20)>` type is treated as
`array<struct<key:varchar(20), value:varchar(20)>>`, where
`key` and `value` refer to the attributes of the map in the
underlying data.

For information about how AWS Clean Rooms enables navigation into arrays and structures, see
[Navigation](query-nested-data.md#navigation "query-nested-data.md#navigation").

For information about how AWS Clean Rooms enables iteration over arrays by navigating the
array using the FROM clause of a query, see [Unnesting queries](query-nested-data.md#unnesting-queries "query-nested-data.md#unnesting-queries").
