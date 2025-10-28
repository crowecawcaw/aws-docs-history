# Strongly connected components algorithm

Strongly connected components (SCC) are the maximally connected subgraphs of a
directed graph where every node is reachable from every other node (in other
words, there exists a path between every node in the subgraph).

Neptune Analytics implements this algorithm using a modified multi-step approach
(see [BFS
and Coloring-based Parallel Algorithms for Strongly Connected Components and Related
Problems](https://www.cs.rpi.edu/~slotag/pub/SCC-IPDPS14.pdf "https://www.cs.rpi.edu/~slotag/pub/SCC-IPDPS14.pdf"), by George M. Slota, Sivasankaran Rajamanickam, and Kamesh Madduri,
IPDPS 2014).

The time complexity of the `.scc` algorithm in the worst case is
`O(|V|+|E|*D)`, where `|V|` is the number of nodes in the graph,
`|E|` is the number of edges in the graph, and `D` is the diameter,
defined as the length of the longest path from one node to another in the graph.

The space complexity is O(|V|), where |V| is the number of vertices in the graph.

## `.scc`  syntax

```
CALL neptune.algo.scc(
  [`source-node list (required)`],
  {
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD node, component
RETURN node, component
```

## `.scc`  inputs

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.
- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel**   _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A node label to filter on.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## `.scc`  outputs

For each source node:

- **node**   –  
  The source node.
- **component**   –  
  The component ID associated with the source node.

If the input node list is empty, the output is empty.

## `.scc`  query examples

This openCypher query has an empty input list, and so will have no output:

```
Match (n)
CALL neptune.algo.scc(n, {edgeLabels: ["route", "contains"]})
YIELD component
RETURN n, component
```

This is a query integration example, where `.scc` follows a
`MATCH` clause that generates its input node list:

```
Match (n)
CALL neptune.algo.scc(n, {})
Yield component
Return n, component
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.scc` output

Here is an example of the output returned by .scc when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.scc({writeProperty: 'sccid'}) YIELD success RETURN success" \
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
          "type": "airport",
          "code": "IAD",
          "lon": -77.45580292,
          "runways": 4,
          "longest": 11500,
          "communityId": 2357352929951971,
          "city": "Washington D.C.",
          "region": "US-VA",
          "desc": "Washington Dulles International Airport",
          "prscore": 0.002264724113047123,
          "degree": 312,
          "wccid": 2357352929951779,
          "ccscore": 0.20877772569656373,
          "country": "US",
          "icao": "KIAD"
        }
      },
      "component": 2357352929966149
    },
    {
      "node": {
        "~id": "12",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 40.63980103,
          "elev": 12,
          "type": "airport",
          "code": "JFK",
          "lon": -73.77890015,
          "runways": 4,
          "longest": 14511,
          "communityId": 2357352929951971,
          "city": "New York",
          "region": "US-NY",
          "desc": "New York John F. Kennedy International Airport",
          "prscore": 0.002885053399950266,
          "degree": 403,
          "wccid": 2357352929951779,
          "ccscore": 0.2199712097644806,
          "country": "US",
          "icao": "KJFK"
        }
      },
      "component": 2357352929966149
    }
  ]
}
```
