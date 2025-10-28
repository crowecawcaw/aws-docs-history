# The `evaluationStrategy` SPARQL query hint

The `evaluationStrategy` query hint tells the Amazon Neptune query engine that the
fragment of the query annotated should be evaluated from the bottom up, as an independent
unit. This means that no solutions from previous evaluation steps are used to compute the
query fragment. The query fragment is evaluated as a standalone unit, and its produced
solutions are joined with the remainder of the query after it is computed.

Using the `evaluationStrategy` query hint implies a blocking (non-pipelined) query
plan, meaning that the solutions of the fragment annotated with the query hint are
materialized and buffered in main memory. Using this query hint might significantly increase
the amount of main memory needed to evaluate the query, especially if the annotated query
fragment computes a large number of results.

## `evaluationStrategy` SPARQL hint syntax

The `evaluationStrategy` query hint is specified as a triple pattern
included in a SPARQL query.

For clarity, the following syntax uses a `hint` prefix defined
and included in the query to specify the Neptune query-hint namespace:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
hint:SubQuery hint:evaluationStrategy "BottomUp" .
```

###### Available Scopes

- `hint:SubQuery`

###### Note

This query hint is supported only in nested subqueries.

For more information about query hint scopes, see [Scope of SPARQL query hints in Neptune](sparql-query-hints.md#sparql-query-hints-scope "sparql-query-hints.md#sparql-query-hints-scope").

## `evaluationStrategy` SPARQL hint example

This section shows a query written with and without the `evaluationStrategy` query
hint and related optimizations.

For this example, assume that the dataset has the following characteristics:

- It contains 1,000 edges labeled `:connectedTo`.
- Each `component` node is connected to an average of 100 other
  `component` nodes.
- The typical number of four-hop cyclical connections between nodes is around

100.

###### No Query Hint

The following SPARQL query extracts all `component` nodes that are
cyclically connected to each other via four hops:

```
PREFIX : <https://example.com/>
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT * {
  ?component1 :connectedTo ?component2 .
  ?component2 :connectedTo ?component3 .
  ?component3 :connectedTo ?component4 .
  ?component4 :connectedTo ?component1 .
}
```

The approach of the Neptune query engine is to evaluate this query using the following
steps:

- Extract all 1,000 `connectedTo` edges in the graph.
- Expand by 100x (the number of outgoing `connectedTo` edges from
  component2).

Intermediate results: 100,000 nodes.

- Expand by 100x (the number of outgoing `connectedTo` edges from
  component3).

Intermediate results: 10,000,000 nodes.

- Scan the 10,000,000 nodes for the cycle close.

This results in a streaming query plan, which has a constant amount of main
memory.

###### Query Hint and Subqueries

You might want to trade off main memory space for accelerated computation. By
rewriting the query using an `evaluationStrategy` query hint, you can force the
engine to compute a join between two smaller, materialized subsets.

```
PREFIX : <https://example.com/>
          PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT * {
  {
    SELECT * WHERE {
      hint:SubQuery hint:evaluationStrategy "BottomUp" .
      ?component1 :connectedTo ?component2 .
      ?component2 :connectedTo ?component3 .
    }
  }
  {
    SELECT * WHERE {
      hint:SubQuery hint:evaluationStrategy "BottomUp" .
      ?component3 :connectedTo ?component4 .
      ?component4 :connectedTo ?component1 .
    }
  }
}
```

Instead of evaluating the triple patterns in sequence while iteratively using results
from the previous triple pattern as input for the upcoming patterns, the
`evaluationStrategy` hint causes the two subqueries to be evaluated independently.
Both subqueries produce 100,000 nodes for intermediate results, which are then joined
together to form the final output.

In particular, when you run Neptune on the larger instance types, temporarily storing
these two 100,000 subsets in main memory increases memory usage in return for significantly
speeding up evaluation.
