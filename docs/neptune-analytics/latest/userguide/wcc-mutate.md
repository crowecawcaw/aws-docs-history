# Weakly connected components mutate algorithm

The mutate variant of the weakly connected components (WCC) algorithm performs the
weakly connected components calculation over the entire graph unless the configuration
parameters establish a filter, and each traversed node's calculated WCC value is
stored as a property on the node.

## `.wcc.mutate`  syntax

```
CALL neptune.algo.wcc.mutate(
  {
    writeProperty: `the name for the node property to which to write component IDs`
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD success
RETURN success
```

## `.wcc.mutate`  inputs

Inputs for `.wcc.mutate` are passed in a configuration object that contains:

- **`writeProperty`**   _(required)_   –  
  _type:_ `string`;   _default: none_.

A name for the new node property where the component IDs will be written.

- **edgeLabels**   _(optional)_   –  
  _type:_ a list of edge label strings;   _example:_
  `["route", `...`]`;   _default:_ no edge filtering.

To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
provided then all edge labels are processed during traversal.

- **`vertexLabel`**   _(optional)_   –  
  _type:_ `string`;   _default: none_.

The node label to filter on for traversing. Only nodes matching
this label will be traversed. For example: `"airport"`.

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## `.wcc.mutate`  outputs

**success**:  The computed component IDs are
written as a new property on each node using the property name specified by
`writeProperty`, and a single `success` flag (`true`
or `false`) is returned to indicate whether or not the writes succeeded.

## `.wcc.mutate`  query examples

This query writes the calculated component ID of each vertex in the graph to a
new property of the vertex named `CCID`:

```
CALL neptune.algo.wcc.mutate(
  {
    writeProperty: "CCID",
    edgeLabels: ["route"],
    vertexLabel: "airport",
    concurrency: 2
  }
)
```

After the mutate algorithm call above, the following query can retrieve the CCID
property of a specific node:

```
MATCH (n: airport {code: "SEA"})
RETURN n.CCID
```

## Sample `.wcc.mutate` output

Here is an example of the output returned by .wcc.mutate when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.wcc.mutate({writeProperty: 'wccid'}) YIELD success RETURN success"
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "success": true
    }]
}
```
