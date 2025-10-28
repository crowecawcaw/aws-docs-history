# Closeness centrality mutatealgorithm

The closeness centrality mutate algorithm computes a Closeness Centrality (CC)
metric for
specified nodes in a graph. The CC metric of a node can be used as a positive
measure of how close it is to all other nodes or how central it is in the graph.

The CC metric can be interpreted to show how quickly all other nodes in a network
can be reached from a given node, and how important it is as a central hub for rapid
information flow. It can be used in transportation networks to identify key hub
locations, and in disease-spread modeling to pinpoint central points for targeted
intervention efforts.

The closeness centrality (CC) score of a node is calculated based on the sum of its
distances to all other vertices. The CC score itself is the inverse of that number; in
other words, one divided by that sum. In practice, the calculation is commonly normalized
to use the average length of the shortest paths rather than the actual sum of their lengths.

## `.closenessCentrality.mutate`  syntax

```
CALL neptune.algo.closenessCentrality.mutate(
  [`node list (required)`],
  {
    numSources: `the number of BFS sources to use for computing the CC (required)`
    writeProperty: `name of the node property to write the CC score to (required)`
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: "`a node label for filtering (optional)`",
    traversalDirection: `traversal direction (optional)`,
    normalize: `Boolean, set to `false` to prevent normalization (optional)`
    concurrency: `number of threads to use (optional)`
  }
)
YIELD success
RETURN success
```

## `.closenessCentrality.mutate`  inputs

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting locations for the algorithm.
Each node in the list triggers an execution of the algorithm. If an
empty list is provided, the query result is also empty.

If the algorithm is called following a `MATCH` clause (query
algo integration), the source node list is the result returned by the
`MATCH` clause.

- ###### a configuration object that contains:
  - **numSources** _(required)_   –  
    _type:_ `uint64_t`;   _default: none_.

  The number of BFS sources for computing approximate Closeness Centrality (CC). To compute exact
  closeness centrality, set `numSources` to a number larger than number of vertices,
  such as `maxInt`.

  Because of the computational complexity of the algorithm for large graphs, it's generally best
  to specify a number in the order of thousands to ten thousands, such as 8,192.
  - **writeProperty** _(required)_   –  
    _type:_ `string`;   _default: none_.

  A name for the new node property that will contain the computed CC score of each node.
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **normalize** _(optional)_   –  
    _type:_ `Boolean`;   _default:_ `true`.

  You can use this field to turn off normalization, which is on by default. Without normalization,
  only centrality scores of nodes within the same component can be meaningfully compared. Normalized scores
  can be compared across different connected components.

  The CC is normalizd using the Wasserman-Faust normalization formula for unconnected graphs.
  If there are `n` vertices reachable from vertex `u` (including vertex
  `u` itself), the Wasserman-Faust normalized closeness centrality score of vertex
  `u` is calculated as follows:

  ```
  (n-1)^2 / (|V| - 1) * sum(distance from u to these n vertices)
  ```

  Without normalization, the centrality score of vertex `u` is calculated as:

  ```
  (|V| - 1) / sum(distance from u to all other vertices in the graph)
  ```

  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A node label for node filtering. If a node label is provided, vertices matching the label
  are the only vertices that are included, including vertices in the input list.
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

## `.closenessCentrality.mutate`  outputs

The closeness centrality score of each source node in the input list is written
as a new node property using the property name specified in `writeProperty`.

If the algorithm is invoked as a standalone query, there is no other output.

If the algorithm is invoked following a `MATCH` clause that provides
its source node list (query integration), the algorithm outputs a key column
of the source vertices from the `MATCH` clause and a value column of Booleans
(true or false) that indicate whether the CC value was successfully written to the
node in question.

## Query examples for  `.closenessCentrality.mutate`

This example computes closeness centrality scores and writes them as a new node
property called `ccScore`:

```
CALL neptune.algo.closenessCentrality.mutate(
  {
    numSources: 10,
    writeProperty: "ccScore",
    edgeLabels: ["route"],
    vertexLabel: "airport",
    traversalDirection: "outbound",
    normalize: true,
    concurrency: 1
  }
)
```

Then you can query the `ccScore` property in a subsequent query:

```
MATCH (n) RETURN id(n), n.ccScore limit 5
```

## Sample   `.closenessCentrality.mutate`   output

Here is an example of the output returned by .closenessCentrality.mutate when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.closenessCentrality.mutate(
       {
         writeProperty: 'ccscore',
         numSources: 10
       }
     )
     YIELD success
     RETURN success"
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
