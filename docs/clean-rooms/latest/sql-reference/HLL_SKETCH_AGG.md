# HLL_SKETCH_AGG function

The HLL_SKETCH_AGG aggregate function creates an HLL sketch from the values in the
specified column. It returns an HLLSKETCH data type that encapsulates the input expression
values.

The HLL_SKETCH_AGG aggregate function works with any data type and ignores NULL values.

When there are no rows in a table or all rows are NULL, the resulting sketch has no
index-value pairs such as
`{"version":1,"logm":15,"sparse":{"indices":[],"values":[]}}`.

## Syntax

```
HLL_SKETCH_AGG (*aggregate\_expression*[, lgConfigK ] )
```

## Argument

_aggregate_expression_

Any expression of type INT, BIGINT, STRING, or BINARY against which unique
counting will occur. Any `NULL` values are ignored.

_lgConfigK_

An optional INT constant between 4 and 21 inclusive with default 12. The
log-base-2 of K, where K is the number of buckets or slots for the
sketch.

## Return type

The HLL_SKETCH_AGG function returns a non-NULL BINARY buffer containing the
HyperLogLog sketch computed because of consuming and aggregating all input values in the
aggregation group.

## Examples

The following examples use the HyperLogLog (HLL) algorithm to estimate the distinct
count of values in the `col` column. The `hll_sketch_agg(col, 12)`
function aggregates the values in the col column, creating an HLL sketch using a
precision of 12. The `hll_sketch_estimate()` function is then used to
estimate the distinct count of values based on the generated HLL sketch. The final
result of the query is 3, which represents the estimated distinct count of values in the
`col` column. In this case, the distinct values are 1, 2, and 3.

```
SELECT hll_sketch_estimate(hll_sketch_agg(col, 12))
    FROM VALUES (1), (1), (2), (2), (3) tab(col);
  3

```

The following example also uses the HLL algorithm to estimate the distinct count of
values in the `col` column, but it doesn't specify a precision value for the HLL sketch.
In this case, it uses the default precision of 14. The `hll_sketch_agg(col)`
function takes the values in the `col` column and creates an HyperLogLog (HLL) sketch,
which is a compact data structure that can be used to estimate the distinct count of
elements. The `hll_sketch_estimate(hll_sketch_agg(col))` function takes the
HLL sketch created in the previous step and calculates an estimate of the distinct count
of values in the `col` column. The final result of the query is 3, which
represents the estimated distinct count of values in the `col` column. In
this case, the distinct values are 1, 2, and 3.

```
SELECT hll_sketch_estimate(hll_sketch_agg(col))
FROM VALUES (1), (1), (2), (2), (3) tab(col);
3
```
