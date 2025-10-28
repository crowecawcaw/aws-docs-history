Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HLL_COMBINE function

The HLL_COMBINE aggregate function returns an HLLSKETCH data type that combines all
input HLLSKETCH values.

The combination of two or more HyperLogLog sketches is a new HLLSKETCH that
encapsulates information about the union of the distinct values that each input sketch
represents. After combining sketches, Amazon Redshift extracts the cardinality of the union of two
or more datasets. For more information on how to combine multiple sketches, see [Example: Return a HyperLogLog sketch
from combining multiple sketches](r_HLL-examples.md#hll-examples-multiple-sketches "r_HLL-examples.md#hll-examples-multiple-sketches").

## Syntax

```
HLL_COMBINE (*hllsketch\_expression*)
```

## Argument

_hllsketch_expression_

Any valid expression that evaluates to an HLLSKETCH type, such as a column name. The input value is the HLLSKETCH data type.

## Return type

The HLL_COMBINE function returns an HLLSKETCH type.

## Examples

The following example returns the combined HLLSKETCH values in the table
`hll_table`.

```
CREATE TABLE a_table(an_int INT, b_int INT);
INSERT INTO a_table VALUES (1,1), (2,1), (3,1), (4,1), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2);

CREATE TABLE hll_table (sketch HLLSKETCH);
INSERT INTO hll_table select hll_create_sketch(an_int) from a_table group by b_int;

SELECT hll_combine(sketch) AS sketches FROM hll_table;
sketches
----------------------------------------------------------------------------------------------------------------------------
{"version":1,"logm":15,"sparse":{"indices":[20812342,20850007,22362299,40314817,42650774,47158030],"values":[1,2,1,3,2,1]}}
(1 row)
```
