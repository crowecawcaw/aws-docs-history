# Closeness centrality algorithm

The closeness centrality algorithm computes a Closeness Centrality (CC) metric for
specified nodes in a graph. The CC metric of a node can be used as a positive
measure of how close it is to all other nodes or how central it is in the graph.

The CC metric can be interpreted to show how quickly all other nodes in a network
can be reached from a given node, and how important it is as a central hub for rapid
information flow. It can be used in transportation networks to identify key hub
locations, and in disease-spread modeling to pinpoint central points for targeted
intervention efforts.

The closeness centrality (CC) score of a node is calculated based on the sum of its
distances to all other nodes. The CC score itself is the inverse of that number; in
other words, one divided by that sum. In practice, the calculation is commonly normalized
to use the average length of the shortest paths rather than the actual sum of their lengths.

## `.closenessCentrality`  syntax

```
CALL neptune.algo.closenessCentrality(
  [`node list (required)`],
  {
    numSources: `the number of BFS sources to use for computing the CC (required)`
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    traversalDirection: `traversal direction (optional)`,
    normalize: `Boolean, set to `false` to prevent normalization (optional)`
    concurrency: `number of threads to use (optional)`
  }
)
YIELD node, score
RETURN node, score
```

## Inputs for the `.closenessCentrality` algorithm

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting locations for the algorithm.
Each node in the list triggers an execution of the algorithm. If an
empty list is provided, the query result is also empty.

If the algorithm is called following a `MATCH` clause (query
algo integration), the source query list is the result returned by the
`MATCH` clause.

- ###### a configuration object that contains:
  - **numSources** _(required)_   –  
    _type:_ `unsigned long`;   _default: none_.

  The number of BFS sources for computing approximate Closeness Centrality (CC). To compute exact
  closeness centrality, set `numSources` to a number larger than number of nodes,
  such as `maxInt`.

  Because of the computational complexity of the algorithm for large graphs, it's generally best
  to specify a number in the order of thousands to ten thousands, such as 8,192.
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

  A node label for node filtering. If a node label is provided, nodes matching the label
  are the only nodes that are included, including nodes in the input list.
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

## Outputs for the `.closenessCentrality` algorithm

- **node**   –  
  A key column of the input nodes.
- **score**   –  
  A key column of the corresponding closeness-centrality (CC) scores for those nodes.

If the input node list is empty, the output is empty.

## `.closenessCentrality`  query examples

This is a standalone example, where the source node list is explicitly provided in
the query:

```
CALL neptune.algo.closenessCentrality(
  ["101"],
  {
    numSources: 10,
    edgeLabels: ["route"],
    vertexLabel: "airport",
    traversalDirection: "outbound",
    normalize: true,
    concurrency: 1
  }
)
YIELD node, score
RETURN node, score
```

This is a query integration example, where `.closenessCentrality.mutate`
follows a `MATCH` clause and uses the output of the `MATCH`
clause as its list of source nodes:

```
Match (n)
CALL neptune.algo.closenessCentrality(
  n,
  {
    numSources: 10,
    edgeLabels: ["route"],
    vertexLabel: "airport",
    traversalDirection: "outbound",
    normalize: true,
    concurrency: 1
  }
)
YIELD score
RETURN n, score
```

This is a query integration examples that returns the nodes with the 10 highest CC scores:

```
CALL neptune.algo.closenessCentrality(
  n,
  {
    edgeLabels: ["route"],
    numSources: 10
  }
)
YIELD score
RETURN n, score
ORDER BY score DESC
LIMIT 10"
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample   `.closenessCentrality`   output

Here is an example of the output returned by .closenessCentrality when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.closenessCentrality(n, {numSources: 10}) YIELD node, score RETURN node, score limit 2" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "node": {
        "~id": "10",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 38.94449997,
          "elev": 313,
          "longest": 11500,
          "city": "Washington D.C.",
          "type": "airport",
          "region": "US-VA",
          "desc": "Washington Dulles International Airport",
          "code": "IAD",
          "prscore": 0.002264724113047123,
          "degree": 312,
          "lon": -77.45580292,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KIAD",
          "runways": 4
        }
      },
      "score": 0.20877772569656373
    },
    {
      "node": {
        "~id": "12",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 40.63980103,
          "elev": 12,
          "longest": 14511,
          "city": "New York",
          "type": "airport",
          "region": "US-NY",
          "desc": "New York John F. Kennedy International Airport",
          "code": "JFK",
          "prscore": 0.002885053399950266,
          "degree": 403,
          "lon": -73.77890015,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KJFK",
          "runways": 4
        }
      },
      "score": 0.2199712097644806
    }
  ]
}
```
