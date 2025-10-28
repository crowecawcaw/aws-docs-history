# The `joinOrder` SPARQL query hint

When you submit a SPARQL query, the Amazon Neptune query engine investigates the structure
of the query. It reorders parts of the query and tries to minimize the amount of work required
for evaluation and query response time.

For example, a sequence of connected triple patterns is typically not evaluated in the
given order. It is reordered using heuristics and statistics such as the selectivity of the
individual patterns and how they are connected through shared variables. Additionally, if your
query contains more complex patterns such as subqueries, FILTERs, or complex OPTIONAL or MINUS
blocks, the Neptune query engine reorders them where possible, aiming for an efficient
evaluation order.

For more complex queries, the order in which Neptune chooses to evaluate the query might
not always be optimal. For instance, Neptune might miss instance data-specific characteristics
(such as hitting power nodes in the graph) that emerge during query evaluation.

If you know the exact characteristics of the data and want to manually dictate the order
of the query execution, use the Neptune `joinOrder` query hint to specify that
the query be evaluated in the given order.

## `joinOrder` SPARQL hint syntax

The `joinOrder` query hint is specified as a triple pattern included in a
SPARQL query.

For clarity, the following syntax uses a `hint` prefix defined
and included in the query to specify the Neptune query-hint namespace:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
`scope` hint:joinOrder "Ordered" .
```

###### Available Scopes

- `hint:Query`
- `hint:Group`

For more information about query hint scopes, see [Scope of SPARQL query hints in Neptune](sparql-query-hints.md#sparql-query-hints-scope "sparql-query-hints.md#sparql-query-hints-scope").

## `joinOrder` SPARQL hint example

This section shows a query written with and without the `joinOrder` query
hint and related optimizations.

For this example, assume that the dataset contains the following:

- A single person named `John` that `:likes` 1,000 persons,
  including `Jane`.
- A single person named `Jane` that `:likes` 10 persons,
  including `John`.

###### No Query Hint

The following SPARQL query extracts all the pairs of people named `John`
and `Jane` who both like each other from a set of social networking
data:

```
PREFIX : <https://example.com/>
SELECT ?john ?jane {
  ?person1 :name "Jane" .
  ?person1 :likes ?person2 .
  ?person2 :name "John" .
  ?person2 :likes ?person1 .
}
```

The Neptune query engine might evaluate the statements in a different order than
written. For example, it might choose to evaluate in the following order:

1. Find all persons named `John`.
2. Find all persons connected to `John` by a
   `:likes` edge.
3. Filter this set by persons named `Jane`.
4. Filter this set by those connected to `John` by a
   `:likes` edge.

According to the dataset, evaluating in this order results in 1,000 entities being
extracted in the second step. The third step narrows this down to the single node,
`Jane`. The final step then determines that `Jane` also
`:likes` the `John` node.

###### Query Hint

It would be favorable to start with the `Jane` node because she has only 10
outgoing `:likes` edges. This reduces the amount of work during the evaluation
of the query by avoiding the extraction of the 1,000 entities during the second
step.

The following example uses the **joinOrder** query hint to ensure that the `Jane` node and its outgoing
edges are processed first by disabling all automatic join reordering for the query:

```
PREFIX : <https://example.com/>
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT ?john ?jane {
  hint:Query hint:joinOrder "Ordered" .
  ?person1 :name "Jane" .
  ?person1 :likes ?person2 .
  ?person2 :name "John" .
  ?person2 :likes ?person1 .
}
```

An applicable real-world scenario might be a social network application in which persons
in the network are classified as either influencers with many connections or normal users
with few connections. In such a scenario, you could ensure that the normal user
(`Jane`) is processed before the influencer (`John`) in a query like
the preceding example.

###### Query Hint and Reorder

You can take this example one step further. If you know that the `:name`
attribute is unique to a single node, you could speed up the query by reordering and using
the `joinOrder` query hint. This step ensures that the unique nodes are
extracted first.

```
PREFIX : <https://example.com/>
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT ?john ?jane {
  hint:Query hint:joinOrder "Ordered" .
  ?person1 :name "Jane" .
  ?person2 :name "John" .
  ?person1 :likes ?person2 .
  ?person2 :likes ?person1 .
}
```

In this case, you can reduce the query to the following single actions in each
step:

1. Find the single person node with `:name`
   `Jane`.
2. Find the single person node with `:name`
   `John`.
3. Check that the first node is connected to the second with a
   `:likes` edge.
4. Check that the second node is connected to the first with a `:likes`
   edge.

###### Important

If you choose the wrong order, the `joinOrder` query hint can lead to
significant performance drops. For example, the preceding example would be inefficient if
the `:name` attributes were not unique. If all 100 nodes were named
`Jane` and all 1,000 nodes were named `John`, then the query would
end up checking 1,000 \* 100 (100,000) pairs for `:likes` edges.
