Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying semi-structured data

With Amazon Redshift, you can query and analyze semi-structured data, such as JSON, Avro, or Ion,
alongside your structured data. Semi-structured data refers to data that has a flexible
schema, allowing for hierarchical or nested structures. The following sections demonstrate
querying semi-structured data using Amazon Redshift's support for open data formats, allowing you to
unlock valuable information from complex data structures.

Amazon Redshift uses the PartiQL language to offer SQL-compatible access to relational,
semi-structured, and nested data.

PartiQL operates with dynamic types. This approach enables intuitive filtering, joining,
and aggregation on the combination of structured, semi-structured, and nested datasets. The
PartiQL syntax uses dotted notation and array subscript for path navigation when accessing
nested data. It also enables the FROM clause items to iterate over arrays and use for
unnest operations. Following, you can find descriptions of the different query patterns
that combine the use of the SUPER data type with path and array navigation, unnesting,
unpivoting, and joins. For more information on PartiQL, see [PartiQL – an SQL-compatible query language for Amazon Redshift](super-partiql.md "super-partiql.md").

## Navigation

Amazon Redshift uses PartiQL to enable navigation into arrays and structures using the [...]
bracket and dot notation respectively. Furthermore, you can mix navigation into
structures using the dot notation and arrays using the bracket notation.
For example, the following statement selects only the third element in an array nested
one level deep in a SUPER object:

```
SELECT super_object.array[2];

 `array
---------------
 third_element`
```

You can use the dot and bracket notation when doing data operations such as
filtering, joining, and aggregating. You can use these notations anywhere in a query
where there are normally column references. For example, the following statement
selects the number of events with the type `UPDATED`.

```
SELECT COUNT(*)
FROM test_json
WHERE all_data.data.pnr.events[0]."eventType" = 'UPDATED';

 `eventType | count
-----------+-------
 "UPDATED" | 1`
```

For more in-depth examples of using PartiQL navigation, see
[Examples of using semi-structured data in Amazon Redshift](super-examples.md "super-examples.md").

## Unnesting queries

To unnest queries, Amazon Redshift provides two ways to iterate over SUPER arrays:
PartiQL syntax and the UNNEST operation in the FROM clause. Both unnesting methods
result in the same output. For information on the UNNEST operation, see
[FROM clause](r_FROM_clause30.md "r_FROM_clause30.md"). For examples of using the UNNEST operation, see
[UNNEST examples](r_FROM_clause-unnest-examples.md "r_FROM_clause-unnest-examples.md").

Amazon Redshift can navigate SUPER arrays using PartiQL syntax in the FROM clause of a query. Using the previous
example, the following example iterates over the attribute values for
`c_orders`.

```
SELECT orders.*, o FROM customer_orders orders, orders.c_orders o;
```

The PartiQL syntax of unnesting using the FROM
clause item `x (AS) y` means that `y` iterates over each (SUPER)
value in (SUPER) array expression x. In this case, `x` is a SUPER expression
and `y` is an alias for `x`.

The left operand can also use the dot and bracket notation for regular navigation. In
the following example, `customer_orders_lineitem c` is the iteration over the
`customer_order_lineitem` base table and `c.c_orders o` is the
iteration over the `c.c_orders` array. To iterate over the
`o_lineitems` attribute, which is an array within an array, you can add
multiple clauses, like so:

```
SELECT c.*, o, l FROM customer_orders_lineitem c, c.c_orders o, o.o_lineitems l;
```

Amazon Redshift also supports an array index when iterating over the array using the AT
keyword. The clause `x AS y AT z` iterates over array `x` and
generates the field `z,` which is the array index. The following example
shows how an array index works.

```
SELECT c_name,
       orders.o_orderkey AS orderkey,
       index AS orderkey_index
FROM customer_orders_lineitem c, c.c_orders AS orders AT index
ORDER BY orderkey_index;

`c_name | orderkey | orderkey_index
-------------------+----------+----------------
Customer#000008251 | 3020007 | 0
Customer#000009452 | 4043971 | 0
 (2 rows)`
```

The following is an example of iterating over a scalar array.

```
CREATE TABLE bar AS SELECT json_parse('{"scalar_array": [1, 2.3, 45000000]}') AS data;

SELECT element, index FROM bar AS b, b.data.scalar_array AS element AT index;

 `index | element
-------+----------
 0 | 1
 1 | 2.3
 2 | 45000000
(3 rows)`
```

The following example iterates over an array of multiple levels. The example uses
multiple unnest clauses to iterate into the innermost arrays. The
`f.multi_level_array` AS array iterates over
`multi_level_array`. The array AS element is the iteration over the arrays
within `multi_level_array`.

```
CREATE TABLE foo AS SELECT json_parse('[[1.1, 1.2], [2.1, 2.2], [3.1, 3.2]]') AS multi_level_array;

SELECT array, element FROM foo AS f, f.multi_level_array AS array, array AS element;

 `element | array
---------+---------
 1.1 | [1.1,1.2]
 1.2 | [1.1,1.2]
 2.1 | [2.1,2.2]
 2.2 | [2.1,2.2]
 3.1 | [3.1,3.2]
 3.2 | [3.1,3.2]
(6 rows)`
```

For more information about the FROM clause, see [FROM clause](r_FROM_clause30.md "r_FROM_clause30.md").
For more examples of unnesting SUPER queries, see [Examples of using semi-structured data in Amazon Redshift](super-examples.md "super-examples.md").

## Object unpivoting

To perform object unpivoting, Amazon Redshift uses the PartiQL syntax to iterate over SUPER
objects. It does this using the FROM clause of a query along with the UNPIVOT keyword.
In the following example, the expression is the `c.c_orders[0]` object. The example query iterates
over each attribute returned by the object.

```
SELECT attr as attribute_name, json_typeof(val) as value_type
FROM customer_orders_lineitem c, UNPIVOT c.c_orders[0] AS val AT attr
WHERE c_custkey = 9451;

 `attribute_name | value_type
-----------------+------------
 o_orderstatus | string
 o_clerk | string
 o_lineitems | array
 o_orderdate | string
 o_shippriority | number
 o_totalprice | number
 o_orderkey | number
 o_comment | string
 o_orderpriority | string
(9 rows)`
```

As with unnesting, the unpivoting syntax is also an extension of the FROM clause. The
difference is that the unpivoting syntax uses the UNPIVOT keyword to indicate that
it's iterating over an object instead of an array. It uses the AS
`value_alias` for iteration over all the values inside an object, and uses
the AT `attribute_alias` for iterating over all the attributes. Consider the following syntax:

```
UNPIVOT expression AS value_alias [ AT attribute_alias ]
```

Amazon Redshift supports using object unpivoting and array unnesting in a single FROM
clause as follows:

```
SELECT attr as attribute_name, val as object_value
FROM customer_orders_lineitem c, c.c_orders AS o, UNPIVOT o AS val AT attr
WHERE c_custkey = 9451;
```

When you use object unpivoting, Amazon Redshift doesn't support correlated unpivoting.
Specifically, suppose that you have a case where there are multiple examples of
unpivoting in different query levels and the inner unpivoting references the outer one.
Amazon Redshift doesn't support this type of multiple unpivoting.

For more information about the FROM clause, see [FROM clause](r_FROM_clause30.md "r_FROM_clause30.md"). For examples of using pivoting with the SUPER type, see
[Examples of using semi-structured data in Amazon Redshift](super-examples.md "super-examples.md").

## Dynamic typing

Dynamic typing doesn't require explicit casting of data that is extracted from the
dot and bracket paths. Amazon Redshift uses dynamic typing to process schemaless SUPER data
without the need to declare the data types before you use them in your query. Dynamic
typing uses the results of navigating into SUPER data columns without having to
explicitly cast them into Amazon Redshift types. Dynamic typing is most useful in joins and GROUP
BY clauses. The following example uses a SELECT statement that requires no explicit
casting of the dot and bracket expressions to the usual Amazon Redshift types. For information about
type compatibility and conversion, see [Type compatibility and conversion](c_Supported_data_types.md#r_Type_conversion "c_Supported_data_types.md#r_Type_conversion").

Consider the following example, which looks for rows where the status of an order is `shipped`:

```
SELECT c_orders[0].o_orderkey
FROM customer_orders_lineitem
WHERE c_orders[0].o_orderstatus = 'shipped';
```

The equality sign in this sample query evaluates to `true` when the value of
c_orders[0].o_orderstatus
is the string ‘shipped’. In all other cases, the equality sign evaluates to `false`,
including the cases where the arguments of the equality are different types.
For example, if the order status is an integer, its row won't be selected.

### Dynamic and static typing

Without using dynamic typing, you can't determine whether c_orders[0].o_orderstatus
is a string, an integer, or a structure. You can only determine that
c_orders[0].o_orderstatus is a SUPER data type, which can be an Amazon Redshift scalar, an array,
or a structure. The static type of c_orders[0].o_orderstatus is a SUPER data type.
Conventionally, a type is implicitly a static type in SQL.

Amazon Redshift uses dynamic typing to the processing of schemaless data. When the query
evaluates the data, c_orders[0].o_orderstatus turns out to be a specific type. For
example, evaluating c_orders[0].o_orderstatus on the first record
of customer_orders_lineitem may result into an integer. Evaluating on the second record
may result into a string. These are the dynamic types of the expression.

When using an SQL operator or function with dot and bracket expressions that have
dynamic types, Amazon Redshift produces results similar to using standard SQL operator or
function with the respective static types. In this example, when the dynamic type of the
path expression is a string, the comparison with the string ‘P’ is meaningful. Whenever
the dynamic type of c_orders[0].o_orderstatus is any other data type except being a
string, the equality returns false. Other functions return null when mistyped arguments
are used.

The following example writes the previous query with static typing:

```
SELECT c_custkey
FROM customer_orders_lineitem
WHERE CASE WHEN JSON_TYPEOF(c_orders[0].o_orderstatus) = 'string'
           THEN c_orders[0].o_orderstatus::VARCHAR = 'P'
           ELSE FALSE END;
```

Note the following distinction between equality predicates and comparison predicates. In
the previous example, if you replace the equality predicate with a less-than-or-equal
predicate, the semantics produce null instead of false.

```
SELECT c_orders[0]. o_orderkey
FROM customer_orders_lineitem
WHERE c_orders[0].o_orderstatus <= 'P';
```

In this example, if c_orders[0].o_orderstatus is a string, Amazon Redshift returns true if it
is alphabetically equal to or smaller than ‘P’. Amazon Redshift returns false if it is
alphabetically larger than 'P'. However, if c_orders[0].o_orderstatus is not a string,
Amazon Redshift returns null since Amazon Redshift can't compare values of different types, as shown
in the following query:

```
SELECT c_custkey
FROM customer_orders_lineitem
WHERE CASE WHEN JSON_TYPEOF(c_orders[0].o_orderstatus) = 'string'
           THEN c_orders[0].o_orderstatus::VARCHAR <= 'P'
           ELSE NULL END;
```

Dynamic typing doesn't exclude from comparisons of types that are minimally comparable. For example, you can convert both CHAR and VARCHAR Amazon Redshift scalar types to SUPER. They are comparable as strings, including ignoring trailing white-space characters similar to Amazon Redshift CHAR and VARCHAR types. Similarly, integers, decimals, and floating-point values are comparable as SUPER values. Specifically for decimal columns, each value can also have a different scale. Amazon Redshift still considers them as dynamic types.

Amazon Redshift also supports equality on objects and arrays that are evaluated as deep equal,
such as evaluating deep into objects or arrays and comparing all attributes. Use deep
equal with caution, because the process of performing deep equal can be
time-consuming.

### Using dynamic typing for

joins

For joins, dynamic typing automatically matches values with different dynamic types
without performing a long CASE WHEN analysis to find out what data types may appear. For
example, assume that your organization changed the format that it was using for part
keys over time.

The initial integer part keys issued are replaced by string part keys, such as ‘A55’,
and later replaced again by array part keys, such as [‘X’, 10] combining a string and a number.
Amazon Redshift doesn't have to perform a lengthy case analysis about part keys and can use joins,
as shown in the following example.

```
SELECT c.c_name
    ,l.l_extendedprice
    ,l.l_discount
FROM customer_orders_lineitem c
    ,c.c_orders o
    ,o.o_lineitems l
    ,supplier_partsupp s
    ,s.s_partsupps ps
WHERE l.l_partkey = ps.ps_partkey
AND c.c_nationkey = s.s_nationkey
ORDER BY c.c_name;
```

The following example shows how complex and inefficient the same query can be without using dynamic typing:

```
SELECT c.c_name
    ,l.l_extendedprice
    ,l.l_discount
FROM customer_orders_lineitem c
    ,c.c_orders o
    ,o.o_lineitems l
    ,supplier_partsupp s
    ,s.s_partsupps ps
WHERE CASE WHEN IS_INTEGER(l.l_partkey) AND IS_INTEGER(ps.ps_partkey)
           THEN l.l_partkey::integer = ps.ps_partkey::integer
           WHEN IS_VARCHAR(l.l_partkey) AND IS_VARCHAR(ps.ps_partkey)
           THEN l.l_partkey::varchar = ps.ps_partkey::varchar
           WHEN IS_ARRAY(l.l_partkey) AND IS_ARRAY(ps.ps_partkey)
                AND IS_VARCHAR(l.l_partkey[0]) AND IS_VARCHAR(ps.ps_partkey[0])
                AND IS_INTEGER(l.l_partkey[1]) AND IS_INTEGER(ps.ps_partkey[1])
           THEN l.l_partkey[0]::varchar = ps.ps_partkey[0]::varchar
                AND l.l_partkey[1]::integer = ps.ps_partkey[1]::integer
           ELSE FALSE END
AND c.c_nationkey = s.s_nationkey
ORDER BY c.c_name;
```

## Lax semantics

By default, navigation operations on SUPER values return null instead of returning an
error out when the navigation is invalid. Object navigation is invalid if the SUPER
value is not an object or if the SUPER value is an object but doesn't contain the
attribute name used in the query. For example, the following query accesses an invalid
attribute name in the SUPER data column cdata:

```
SELECT c.c_orders.something FROM customer_orders_lineitem c;
```

Array navigation returns null if the SUPER value is not an array or the array index is
out of bounds. The following query returns null because c_orders[1][1] is out of bounds.

```
SELECT c.c_orders[1][1] FROM customer_orders_lineitem c;
```

Lax semantics is especially useful when using dynamic typing to cast a SUPER value.
Casting a SUPER value to the wrong type returns null instead of an error if the cast is
invalid. For example, the following query returns null because it can't cast the
string value 'Good' of the object attribute o_orderstatus to INTEGER. Amazon Redshift returns
an error for a VARCHAR to INTEGER cast but not for a SUPER cast.

```
SELECT c.c_orders.o_orderstatus::integer FROM customer_orders_lineitem c;
```

## Order by

Amazon Redshift doesn't define SUPER comparisons among
values with different dynamic types. A SUPER value that is a string is
neither smaller nor larger than a SUPER value that is a number. To use
ORDER BY clauses with SUPER columns, Amazon Redshift defines a total ordering
among different types to be observed when Amazon Redshift ranks SUPER values using
ORDER BY clauses. The order among dynamic types is boolean, number,
string, array, object.

For an example of using GROUP BY and ORDER BY in a SUPER query, see
[Filtering semi-structured data](super-examples.md#super-examples-filter "super-examples.md#super-examples-filter").
