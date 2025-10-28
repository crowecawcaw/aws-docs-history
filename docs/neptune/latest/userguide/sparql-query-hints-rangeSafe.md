# The `rangeSafe` SPARQL query hint

Use this query hint to turn off type promotion for a SPARQL query.

When you submit a SPARQL query that includes a `FILTER` over a numerical
value or range, the Neptune query engine must normally use type promotion when it
executes the query. This means that it has to examine values of every type that could
hold the value you are filtering on.

For example, if you are filtering for values equal to 55, the engine must look for
integers equal to 55, long integers equal to 55L, floats equal to 55.0,
and so forth. Each type promotion requires an additional lookup on storage,
which can cause an apparently simple query to take an unexpectedly long time to
complete.

Often type promotion is unnecessary because you know in advance that you only
need to find values of one specific type. When this is the case, you can speed up your
queries dramatically by using the `rangeSafe` query hint to turn off
type promotion.

## `rangeSafe` SPARQL hint syntax

The `rangeSafe` query hint takes a value of `true` to
turn off type promotion. It also accepts a value of `false` (the default).

**Example.** The following example shows how to
turn off type promotion when filtering for an integer value of `o`
greater than 1:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT * {
   ?s ?p ?o .
   hint:Prior hint:rangeSafe 'true' .
   FILTER (?o > '1'^^<http://www.w3.org/2001/XMLSchema#int>)
```
