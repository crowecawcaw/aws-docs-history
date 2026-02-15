# Querying nested data

AWS Clean Rooms offers SQL-compatible access to relational and nested data.

AWS Clean Rooms uses dotted notation and array subscript for path navigation when accessing nested
data. It also enables the FROM clause items to iterate over arrays and use for
unnest operations. The following topics provide descriptions of the different query patterns
that combine the use of the array/struct/map data type with path and array navigation,
unnesting, and joins.

###### Topics

- [Navigation](#navigation "#navigation")
- [Unnesting queries](#unnesting-queries "#unnesting-queries")
- [Lax semantics](#lax-semantics "#lax-semantics")
- [Types of introspection](#types-of-introspection "#types-of-introspection")

## Navigation

AWS Clean Rooms enables navigation into arrays and structures using the `[...]` bracket
and dot notation respectively. Furthermore, you can mix navigation into structures using
the dot notation and arrays using the bracket notation.

###### Example

For example, the following example query assumes that the `c_orders` array
data column is an array with a structure and an attribute is named
`o_orderkey`.

```
SELECT cust.c_orders[0].o_orderkey FROM customer_orders_lineitem AS cust;
```

You can use the dot and bracket notations in all types of queries, such as filtering,
join, and aggregation. You can use these notations in a query in which there are normally
column references.

###### Example

The following example uses a SELECT statement that filters results.

```
SELECT count(*) FROM customer_orders_lineitem WHERE c_orders[0].o_orderkey IS NOT NULL;
```

###### Example

The following example uses the bracket and dot navigation in both GROUP BY and ORDER
BY clauses.

```
SELECT c_orders[0].o_orderdate,
       c_orders[0].o_orderstatus,
       count(*)
FROM customer_orders_lineitem
WHERE c_orders[0].o_orderkey IS NOT NULL
GROUP BY c_orders[0].o_orderstatus,
         c_orders[0].o_orderdate
ORDER BY c_orders[0].o_orderdate;
```

## Unnesting queries

To unnest queries, AWS Clean Rooms enables iteration over arrays. It does this by navigating the
array using the FROM clause of a query.

###### Example

Using the previous example, the following example iterates over the attribute values
for `c_orders`.

```
SELECT o FROM customer_orders_lineitem c, c.c_orders o;
```

The unnesting syntax is an extension of the FROM clause. In standard SQL, the FROM
clause `x (AS) y` means that `y` iterates over each tuple in relation
`x`. In this case, `x` refers to a relation and `y`
refers to an alias for relation `x`. Similarly, the syntax of unnesting using
the FROM clause item `x (AS) y` means that `y` iterates over each
value in array expression `x`. In this case, `x` is an array
expression and `y` is an alias for `x`.

The left operand can also use the dot and bracket notation for regular navigation.

###### Example

In the previous example:

- `customer_orders_lineitem c` is the iteration over the
  `customer_order_lineitem` base table
- `c.c_orders o` is the iteration over the `c.c_orders
 array`
  To iterate over the `o_lineitems` attribute, which is an array within an
  array, you add multiple clauses.

```
SELECT o, l FROM customer_orders_lineitem c, c.c_orders o, o.o_lineitems l;
```

AWS Clean Rooms also supports an array index when iterating over the array using the
AT keyword. The clause `x AS y AT z` iterates over array
`x` and generates the field `z`, which is the array index.

###### Example

The following example shows how an array index works.

```
SELECT c_name,
       orders.o_orderkey AS orderkey,
       index AS orderkey_index
FROM customer_orders_lineitem c, c.c_orders AS orders AT index
ORDER BY orderkey_index;
c_name             | orderkey | orderkey_index
-------------------+----------+----------------
Customer#000008251 | 3020007  |        0
Customer#000009452 | 4043971  |        0  (2 rows)
```

###### Example

The following example iterates over a scalar array.

```
CREATE TABLE bar AS SELECT json_parse('{"scalar_array": [1, 2.3, 45000000]}') AS data;

SELECT index, element FROM bar AS b, b.data.scalar_array AS element AT index;

 index | element
-------+----------
     0 | 1
1 | 2.3
2 | 45000000
(3 rows)
```

###### Example

The following example iterates over an array of multiple levels. The example uses
multiple unnest clauses to iterate into the innermost arrays. The
`f.multi_level_array`
AS array iterates over `multi_level_array`. The array
AS element is the iteration over the arrays within
`multi_level_array`.

```
CREATE TABLE foo AS SELECT json_parse('[[1.1, 1.2], [2.1, 2.2], [3.1, 3.2]]') AS multi_level_array;

SELECT array, element FROM foo AS f, f.multi_level_array AS array, array AS element;

   array   | element
-----------+---------
 [1.1,1.2] | 1.1
 [1.1,1.2] | 1.2
 [2.1,2.2] | 2.1
 [2.1,2.2] | 2.2
 [3.1,3.2] | 3.1
 [3.1,3.2] | 3.2
(6 rows)
```

## Lax semantics

By default, navigation operations on nested data values return null instead of returning
an error out when the navigation is invalid. Object navigation is invalid if the nested
data value is not an object or if the nested data value is an object but doesn't contain
the attribute name used in the query.

###### Example

For example, the following query accesses an invalid attribute name in the nested
data column `c_orders`:

```
SELECT c.c_orders.something FROM customer_orders_lineitem c;
```

Array navigation returns null if the nested data value is not an array or the array
index is out of bounds.

###### Example

The following query returns null because `c_orders[1][1]` is out of
bounds.

```
SELECT c.c_orders[1][1] FROM customer_orders_lineitem c;
```

## Types of introspection

Nested data type columns support inspection functions that return the type and other
type information about the value. AWS Clean Rooms supports the following boolean functions
for nested data columns:

- DECIMAL_PRECISION
- DECIMAL_SCALE
- IS_ARRAY
- IS_BIGINT
- IS_CHAR
- IS_DECIMAL
- IS_FLOAT
- IS_INTEGER
- IS_OBJECT
- IS_SCALAR
- IS_SMALLINT
- IS_VARCHAR
- JSON_TYPEOF

All these functions return false if the input value is null. IS_SCALAR, IS_OBJECT, and
IS_ARRAY are mutually exclusive and cover all possible values except for null. To infer the
types corresponding to the data, AWS Clean Rooms uses the JSON_TYPEOF function that returns the type
of (the top level of) the nested data value as shown in the following example:

```
SELECT JSON_TYPEOF(r_nations) FROM region_nations;
 json_typeof
 -------------
array
(1 row)
```

```
SELECT JSON_TYPEOF(r_nations[0].n_nationkey) FROM region_nations;
 json_typeof
 -------------
 number
```
