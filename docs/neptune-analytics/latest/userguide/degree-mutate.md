# Degree mutate centrality algorithm

The `.degree.mutate` centrality algorithm counts the number of incident edges
of every node in the graph. This measure of how connected the node is can
in turn indicate the node's importance and level of influence in the network. The
`.degree.mutate` algorithm then stores each node's calculated
degree value as a property of the node.

The algorithm returns a single success flag (`true` or `false`),
which indicates whether the writes succeeded or failed.

## `.degree.mutate`   syntax

```
CALL neptune.algo.degree.mutate(
  {
    writeProperty: `A name for the new node property where the degree values will be written`,
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: "`a node label for filtering (optional)`",
    traversalDirection: `traversal direction (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD success
RETURN success
```

## `.degree.mutate`   inputs

###### a configuration object that contains:

- **writeProperty** _(required)_   –  
  _type:_ `string`;   _default: none_.

A name for the new node property that will contain the computed degree values.

- **edgeLabels**   _(optional)_   –  
  _type:_ a list of edge label strings;   _example:_
  `["route", `...`]`;   _default:_ no edge filtering.

To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
provided then all edge labels are processed during traversal.

- **vertexLabel** _(optional)_   –  
  _type:_ `string`;   _default: none_.

A node label for node filtering. If `vertexLabel` is provided, vertices matching the label
are the only vertices that are processed, including vertices in the input list.

- **traversalDirection** _(optional)_   –  
  _type:_ `string`;   _default:_ `"outbound"`.

The direction of edge to follow. Must be one of: `"inbound"`,
`"outbound"`, or `"both"`.

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## Output of the `.degree.mutate` algorithm

The computed degree values are written to a new vertex property using the property
name specified by the `writeProperty` input parameter.

A single Boolean `success` value (`true` or `false`)
is returned, which indicates whether or not the writes succeeded.

## `.degree.mutate` query examples

The example below is a standalone example, where the source vertex list is
explicitly provided in the query.

This query writes the degree values of all nodes in the graph to a new vertex
property called `DEGREE`:

```
CALL neptune.algo.degree.mutate({writeProperty: "DEGREE", edgeLabels: ["route]})
```

After using the mutate algorithm, the newly written properties can then be accessed
in subsequent queries. For example, after the mutate algorithm call above, you could use the
following query to retrieve the `.degree` property of specific nodes:

```
MATCH (n) WHERE id(n) IN ["101", "102", "103"]
RETURN n.DEGREE'
```

## Sample output from `.degree.mutate`

Here is an example of the output returned by .degree.mutate when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.degree.mutate({writeProperty: 'degree'}) YIELD success RETURN success" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    { "success": true }
  ]
}
```
