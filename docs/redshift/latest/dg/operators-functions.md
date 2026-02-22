Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Operators and functions

With Amazon Redshift, you can perform advanced analytics on large datasets using SUPER data using operators and
functions. Operators and functions for SUPER data are SQL constructs that enable complex analysis and
manipulation of semi-structured data stored in Amazon Redshift tables.

The following sections will cover the syntax, examples, and best practices for using operators and functions
for SUPER data in Amazon Redshift to unlock the full potential of your semi-structured data.

## Arithmetic operators

SUPER values support all basic arithmetic operators +, -, \*, /, % using dynamic
typing. The resultant type of the operation remains as SUPER. For all operators, except
for the binary operator +, the input operands must be numbers. Otherwise, Amazon Redshift
returns null. The distinction between decimals and floating-point values is retained
when Amazon Redshift runs these operators and the dynamic type doesn't change. However,
decimal scale changes when you use multiplications and divisions. Arithmetic overflows
still cause query errors, they aren't changed to null. Binary operator + performs
addition if the inputs are numbers or concatenation if the inputs are string. If one
operand is a string and the other operand is a number, the result is null. Unary prefix
operators + and - returns null if the SUPER value is not a number as shown in the
following example:

```
SELECT (c_orders[0]. o_orderkey + 0.5) * c_orders[0]. o_orderkey / 10 AS math FROM customer_orders_lineitem;
            math
----------------------------
 1757958232200.1500
(1 row)
```

Dynamic typing allows decimal values in SUPER to have different scales. Amazon Redshift treats decimal values as if they are different static types and allows all mathematical operations. Amazon Redshift computes the resulting scale dynamically based on the scales of the operands. If one of the operands is a floating-point number, then Amazon Redshift promotes the other operand to a floating-point number and generates the result as a floating-point number.

## Arithmetic functions

Amazon Redshift supports the following arithmetic functions for SUPER columns. They return null if the input isn't a number:

- FLOOR. For more information, see [FLOOR function](r_FLOOR.md "r_FLOOR.md").
- CEIL and CEILING. For more information, see [CEILING (or CEIL) function](r_CEILING_FLOOR.md "r_CEILING_FLOOR.md").
- ROUND. For more information, see [ROUND function](r_ROUND.md "r_ROUND.md").
- TRUNC. For more information, see [TRUNC function](r_TRUNC.md "r_TRUNC.md").
- ABS. For more information, see [ABS function](r_ABS.md "r_ABS.md").

The following example uses arithmetic functions to query data:

```
SELECT x, FLOOR(x), CEIL(x), ROUND(x)
FROM (
    SELECT (c_orders[0]. o_orderkey + 0.5) * c_orders[0].o_orderkey / 10 AS x
    FROM customer_orders_lineitem
    );

         x          |     floor     |     ceil      |     round
--------------------+---------------+---------------+---------------
 1389636795898.0500  | 1389636795898  | 1389636795899  | 1389636795898
```

The ABS function retains the scale of the input decimal while FLOOR, CEIL. The ROUND
eliminates the scale of the input decimal.

## Array functions

Amazon Redshift supports the following array composition and utility functions:

- ARRAY. For more information, see [ARRAY function](r_array.md "r_array.md").
- ARRAY_CONCAT. For more information, see [ARRAY_CONCAT function](r_array_concat.md "r_array_concat.md").
- ARRAY_CONTAINS. For more information, see [ARRAY_CONTAINS function](array_contains.md "array_contains.md").
- ARRAY_DISTINCT. For more information, see [ARRAY_DISTINCT function](array_distinct.md "array_distinct.md").
- ARRAY_EXCEPT. For more information, see [ARRAY_EXCEPT function](array_except.md "array_except.md").
- ARRAY_FLATTEN. For more information, see [ARRAY_FLATTEN function](array_flatten.md "array_flatten.md").
- ARRAY_INTERSECTION. For more information, see [ARRAY_INTERSECTION function](array_intersection.md "array_intersection.md").
- ARRAY_POSITION. For more information, see [ARRAY_POSITION function](array_position.md "array_position.md").
- ARRAY_POSITIONS. For more information, see [ARRAY_POSITIONS function](array_positions.md "array_positions.md").
- ARRAY_SORT. For more information, see [ARRAY_SORT function](array_sort.md "array_sort.md").
- ARRAY_UNION. For more information, see [ARRAY_UNION function](array_union.md "array_union.md").
- ARRAYS_OVERLAP. For more information, see [ARRAYS_OVERLAP function](arrays_overlap.md "arrays_overlap.md").
- GET_ARRAY_LENGTH. For more information, see [GET_ARRAY_LENGTH function](get_array_length.md "get_array_length.md").
- SPLIT_TO_ARRAY. For more information, see [SPLIT_TO_ARRAY function](split_to_array.md "split_to_array.md").
- SUBARRAY. For more information, see [SUBARRAY function](r_subarray.md "r_subarray.md").

You can construct SUPER arrays from values in Amazon Redshift data types using the ARRAY
function, including other SUPER values. The following example uses the variadic function
ARRAY:

```
SELECT ARRAY(1, c.c_custkey, NULL, c.c_name, 'abc') FROM customer_orders_lineitem c;
                               array
 -------------------------------------------------------
[1,8401,null,""Customer#000008401"",""abc""]
[1,9452,null,""Customer#000009452"",""abc""]
[1,9451,null,""Customer#000009451"",""abc""]
[1,8251,null,""Customer#000008251"",""abc""]
[1,5851,null,""Customer#000005851"",""abc""]
(5 rows)
```

The following example uses array concatenation with the ARRAY_CONCAT function:

```
SELECT ARRAY_CONCAT(JSON_PARSE('[10001,10002]'),JSON_PARSE('[10003,10004]'));

             array_concat
------------------------------------
 [10001,10002,10003,10004]
(1 row)
```

The following example uses array manipulation with the SUBARRAY function which
returns a subset of the input array.

```
SELECT SUBARRAY(ARRAY('a', 'b', 'c', 'd', 'e', 'f'), 2, 3);

   subarray
---------------
 ["c","d","e"]
(1 row))
```

The following example merges multiple levels of arrays into a single array using
ARRAY_FLATTEN:

```
SELECT x, ARRAY_FLATTEN(x) FROM (SELECT ARRAY(1, ARRAY(2, ARRAY(3, ARRAY()))) AS x);

     x           | array_flatten
 ----------------+---------------
 [1,[2,[3,[]]]]  | [1,2,3]
(1 row)
```

Array functions ARRAY_CONCAT and ARRAY_FLATTEN use dynamic typing rules. They return
a null instead of an error if the input isn't an array. The GET_ARRAY_LENGTH function
returns the length of a SUPER array given an object or array path.

```
SELECT c_name
FROM customer_orders_lineitem
WHERE GET_ARRAY_LENGTH(c_orders) = (
    SELECT MAX(GET_ARRAY_LENGTH(c_orders))
    FROM customer_orders_lineitem
    );
```

The following example splits a string to an array of strings using SPLIT_TO_ARRAY.
The function uses a delimiter as an optional parameter. If no delimiter is absent, then
the default is a comma.

```
SELECT SPLIT_TO_ARRAY('12|345|6789', '|');

   split_to_array
---------------------
 ["12","345","6789"]
(1 row)
```

## Collation behavior

With SUPER, you can set the collation of a column with [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md"), take the
default collation set with [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md"), and set the
collation of an expression with the [COLLATE function](r_COLLATE.md "r_COLLATE.md").

The collation setting applies to all comparison operators and string values stored in
SUPER, whether they are string values, strings inside SUPER arrays, or values of a SUPER
object. For SUPER objects, the collation behavior only applies to the values and not to
the attributes. For example, a comparison of values that have the case insensitive
collation of `{"attribute": "a"} = {"attribute": "A"}` returns true, while
`{"attribute": "a"} = {"ATTRIBUTE": "a"}` returns false.

## Information functions

SUPER data columns support inspection functions that return the dynamic type and other
type information about the SUPER value. The most common example is the JSON_TYPEOF
scalar function that returns a VARCHAR with values boolean, number, string, object,
array, or null, depending on the dynamic type of the SUPER value. Amazon Redshift supports the
following boolean functions for SUPER data columns:

- [IS_ARRAY function](r_is_array.md "r_is_array.md")
- [IS_BIGINT function](r_is_bigint.md "r_is_bigint.md")
- [IS_CHAR function](r_is_char.md "r_is_char.md")
- [IS_DECIMAL function](r_is_decimal.md "r_is_decimal.md")
- [IS_FLOAT function](r_is_float.md "r_is_float.md")
- [IS_INTEGER function](r_is_integer.md "r_is_integer.md")
- [IS_OBJECT function](r_is_object.md "r_is_object.md")
- [IS_SCALAR function](r_is_scalar.md "r_is_scalar.md")
- [IS_SMALLINT function](r_is_smallint.md "r_is_smallint.md")
- [IS_VARCHAR function](r_is_varchar.md "r_is_varchar.md")

For more information on SUPER type information functions, see
[SUPER type information functions](c_Type_Info_Functions.md "c_Type_Info_Functions.md").

## Object functions

Following are the SQL object functions that Amazon Redshift supports to create and operate on SUPER type objects:

- [GET_NUMBER_ATTRIBUTES function](get_number_attributes.md "get_number_attributes.md")
- [LOWER_ATTRIBUTE_NAMES function](r_lower_attribute_names.md "r_lower_attribute_names.md")
- [OBJECT function](r_object_function.md "r_object_function.md")
- [OBJECT_TRANSFORM function](r_object_transform_function.md "r_object_transform_function.md")
- [UPPER_ATTRIBUTE_NAMES function](r_upper_attribute_names.md "r_upper_attribute_names.md")

For more information on object functions, see
[Object functions](Object_Functions.md "Object_Functions.md").

## String functions

To use string functions with string literals in the SUPER data type, you must
convert the string literal to string type before applying the functions. Functions return
null if the input is not a string literal.

[String functions](String_functions_header.md "String_functions_header.md") now support up to
16,000,000 bytes.

The following example uses SUBSTRING to extract the preview of a string with size 5,000,000 bytes
stored in a SUPER JSON object

```
CREATE TABLE customer_data (
   customer_id INT,
   profile SUPER
);

INSERT INTO customer_data VALUES (
   1,
   JSON_PARSE('{"name": "John Doe", "description": "' || REPEAT('A', 5000000) || '"}')
);

SELECT
   customer_id,
   profile.name::VARCHAR AS name,
   SUBSTRING(profile.description::VARCHAR, 1, 50) AS description_preview
FROM customer_data;

 `customer_id | name | description_preview
-------------+----------+----------------------------------------------------
 1 | John Doe | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`

```

The following example demonstrates LEFT, RIGHT, and CONCAT functions on string literals from a SUPER array:

```
CREATE TABLE documents (
   doc_id INT,
   chapters SUPER
);

INSERT INTO documents VALUES (
   1,
   JSON_PARSE('["' || REPEAT('hello', 400000) || '", "' || REPEAT('world', 600000) || '"]')
);

SELECT
   doc_id,
   LEFT(chapters[0]::VARCHAR, 20) AS chapter1_start,
   RIGHT(chapters[1]::VARCHAR, 20) AS chapter2_end,
   LEN(CONCAT(chapters[0]::VARCHAR, chapters[1]::VARCHAR)) AS concat_size
FROM documents;

 `doc_id | chapter1_start | chapter2_end | concat_size
--------+----------------------+----------------------+-------------
 1 | hellohellohellohello | worldworldworldworld | 5000000`

```

The following example stores standalone string in SUPER:

```
CREATE TABLE text_storage (
   text_id INT,
   content SUPER
);

INSERT INTO text_storage VALUES
   (1, REPEAT('A', 8000000)),
   (2, REPEAT('B', 16000000));

SELECT
   text_id,
   LEN(content::VARCHAR) AS content_length
FROM text_storage;

 `text_id | content_length
---------+----------------
 1 | 8000000
 2 | 16000000`

```
