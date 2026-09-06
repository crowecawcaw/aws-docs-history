

# Strongly connected components algorithm
<a name="scc"></a>

Strongly connected components (SCC) are the maximally connected subgraphs of a directed graph where every node is reachable from every other node (in other words, there exists a path between every node in the subgraph).

Neptune Analytics implements this algorithm using a modified multi-step approach (see [BFS and Coloring-based Parallel Algorithms for Strongly Connected Components and Related Problems](https://www.cs.rpi.edu/~slotag/pub/SCC-IPDPS14.pdf), by George M. Slota, Sivasankaran Rajamanickam, and Kamesh Madduri, IPDPS 2014).

The time complexity of the `.scc` algorithm in the worst case is `O(|V|+|E|*D)`, where `|V|` is the number of nodes in the graph, `|E|` is the number of edges in the graph, and `D` is the diameter, defined as the length of the longest path from one node to another in the graph.

The space complexity is O(\|V\|), where \|V\| is the number of vertices in the graph.

## `.scc`  syntax
<a name="scc-syntax"></a>

```
CALL neptune.algo.scc(
  [{{source-node list (required)}}],
  {
    edgeLabels: [{{list of edge labels for filtering (optional)}}],
    vertexLabel: {{a node label for filtering (optional)}},
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD node, component
RETURN node, component
```

## `.scc`  inputs
<a name="scc-inputs"></a>
+ **a source node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.
+ 

**a configuration object that contains:**
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **vertexLabel**   *(optional)*   –   *type:* `string`;   *default: none*.

    A node label to filter on.
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## `.scc`  outputs
<a name="scc-outputs"></a>

For each source node:
+ **node**   –   The source node.
+ **component**   –   The component ID associated with the source node.

If the input node list is empty, the output is empty.

## `.scc`  query examples
<a name="scc-examples"></a>

This is a query integration example, where `.scc` follows a `MATCH` clause that generates its input node list:

```
MATCH (n)
CALL neptune.algo.scc(n, {edgeLabels: ["route", "contains"]})
YIELD component
RETURN n, component
```

This is another query integration example:

```
MATCH (n)
CALL neptune.algo.scc(n, {})
YIELD component
RETURN n, component
```

## Sample `.scc` output
<a name="scc-sample-output"></a>

Here is an example of the output returned by .scc when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n) CALL neptune.algo.scc(n) YIELD node, component RETURN node, component LIMIT 2" \
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