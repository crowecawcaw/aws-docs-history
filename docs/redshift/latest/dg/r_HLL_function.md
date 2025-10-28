Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HLL function

The HLL function returns the HyperLogLog cardinality of the input expression values.
The HLL function works with any data types except the HLLSKETCH data type. The HLL
function ignores NULL values. When there are no rows in a table or all rows are NULL,
the resulting cardinality is 0.

## Syntax

```
HLL (*aggregate\_expression*)
```

## Argument

_aggregate_expression_

Any valid expression that provides the value to an aggregate, such as a
column name. This function supports any data type as input except HLLSKETCH,
GEOMETRY, GEOGRAPHY, and VARBYTE.

## Return type

The HLL function returns a BIGINT or INT8 value.

## Examples

The following example returns the cardinality of column `an_int` in table
`a_table`.

```
CREATE TABLE a_table(an_int INT);
INSERT INTO a_table VALUES (1), (2), (3), (4);

SELECT hll(an_int) AS cardinality FROM a_table;
cardinality
-------------
4
```
