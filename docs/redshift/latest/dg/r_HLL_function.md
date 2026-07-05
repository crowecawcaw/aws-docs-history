Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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

_aggregate\_expression_

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
