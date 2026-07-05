Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# HLL\_CREATE\_SKETCH function

The HLL\_CREATE\_SKETCH function returns an HLLSKETCH data type that encapsulates the
input expression values. The HLL\_CREATE\_SKETCH function works with any data type and
ignores NULL values. When there are no rows in a table or all rows are NULL, the
resulting sketch has no index-value pairs such as
`{"version":1,"logm":15,"sparse":{"indices":[],"values":[]}}`.

## Syntax

```
HLL_CREATE_SKETCH (*aggregate\_expression*)
```

## Argument

_aggregate\_expression_

Any valid expression that provides the value to an aggregate, such as a
column name. NULL values are ignored. This function supports any data type
as input except HLLSKETCH, GEOMETRY, GEOGRAPHY, and VARBYTE.

## Return type

The HLL\_CREATE\_SKETCH function returns an HLLSKETCH value.

## Examples

The following example returns the HLLSKETCH type for column `an_int` in
table `a_table`. A JSON object is used to represent a sparse HyperLogLog
sketch when importing, exporting, or printing sketches. A string representation (in
Base64 format) is used to represent a dense HyperLogLog sketch.

```
CREATE TABLE a_table(an_int INT);
INSERT INTO a_table VALUES (1), (2), (3), (4);

SELECT hll_create_sketch(an_int) AS sketch FROM a_table;
sketch
-------------------------------------------------------------------------------------------------------
{"version":1,"logm":15,"sparse":{"indices":[20812342,20850007,22362299,47158030],"values":[1,2,1,1]}}
(1 row)
```
