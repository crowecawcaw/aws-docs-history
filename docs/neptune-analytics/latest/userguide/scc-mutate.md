# Strongly connected components mutate algorithm

[Strongly connected components (SCC)](scc.md "scc.md") are the maximally
connected subgraphs of a directed graph, where every node is reachable from every other
node (in other words, there exists a path between every node in the subgraph).

The time complexity of the `.scc-mutate` algorithm in the worst case is
`O(|V|+|E|*D)`, where `|V|` is the number of nodes in the graph,
`|E|` is the number of edges in the graph, and `D` is the diameter,
the length of the longest path from one node to another in the graph.

The space complexity is O(|V|), where |V| is the number of vertices in the graph.

## `.scc.mutate`  syntax

```
CALL neptune.algo.scc.mutate(
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

## Inputs for the `.scc.mutate` algorithm

Inputs for `.scc.mutate` are passed in a configuration object that contains:

- **writeProperty**   _(required)_   –  
  _type:_ `string`;   _default: none_.

A name for the new node property where the component IDs will be written.

- **edgeLabels**   _(optional)_   –  
  _type:_ a list of edge label strings;   _example:_
  `["route", `...`]`;   _default:_ no edge filtering.

To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
provided then all edge labels are processed during traversal.

- **vertexLabel**   _(optional)_   –  
  _type:_ `string`;   _default: none_.

The node label to filter on for traversing. Only nodes matching
this label will be traversed. For example: `"airport"`.

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## Outputs for the `.scc.mutate` algorithm

The computed strongly connected component IDs are written as a new node property
using the specified property name. A single success flag (true or false) is returned
to indicate whether the computation and writes succeeded or failed.

## `.scc.mutate`  query example

```
CALL neptune.algo.scc.mutate(
  {
    writeProperty: "SCOMM_ID",
    edgeLabels: ["route", ..],
    vertexLabel: "airport",
    concurrency: 2
  }
)
```

## Sample  `.scc.mutate`  output

Here is an example of the output returned by .scc.mutate when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.scc.mutate({writeProperty: 'sccid'}) YIELD success RETURN success" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "success": true
    }
  ]
}
```
