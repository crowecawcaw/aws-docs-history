

# Weakly connected components algorithm
<a name="wcc"></a>

The Weakly Connected Components (WCC) algorithm finds the weakly-connected components in a directed graph. A weakly-connected component is a group of nodes in which every node is reachable from every other node when edge directions are ignored. Weakly connected components are the maximal connected subgraphs of an undirected graph.

Identifying weakly-connected components helps in understanding the overall connectivity and structure of the graph. Weakly-connected components can be used in transportation networks to identify disconnected regions that may require improved connectivity, and in social networks to find isolated groups of users with limited interactions, and in webpage analysis to pinpoint sections with low accessibility.

The time complexity of the WCC algorithm is `O(|E|logD)`, where `|E|` is the number of edges in the graph, and `D` is the diameter (the length of the longest path from one node to any other node) of the graph.

The memory used by the WCC algorithm is approximately \|V\| \* 20 bytes.

## `.wcc`  syntax
<a name="wcc-syntax"></a>

```
CALL neptune.algo.wcc(
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

## `.wcc`  inputs
<a name="wcc-inputs"></a>
+ **a source node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  The node or nodes to use as the starting locations for the algorithm. Each node in the list triggers an execution of the algorithm. If an empty list is provided, the query result is also empty.

  If the algorithm is called following a `MATCH` clause (query algo integration), the source query list is the result returned by the `MATCH` clause. 
+ 

**a configuration object that contains:**
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **vertexLabel** *(optional)*   –   *type:* `string`;   *default: none*.

    A node label for node filtering. If a node label is provided, only nodes matching the label are considered. This includes the nodes in the source node lists.
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## `.wcc`  outputs
<a name="wcc-outputs"></a>

For each source node:
+ **node**   –   The source node.
+ **component**   –   The component ID associated with the source node.

If the input node list is empty, the output is empty.

## `.wcc`  query examples
<a name="wcc-query-examples"></a>

This is a standalone example, where the source node list is explicitly provided in the query:

```
CALL neptune.algo.wcc(
  ["101"],
  {
    edgeLabels: ["route"],
    vertexLabel: "airport",
    concurrency: 0
  }
)
YIELD node, component
RETURN node, component
```

This is a query integration example, where `.wcc` follows a `MATCH` clause and uses the output of the MATCH clause as its source node list:

```
MATCH (n) WHERE n.region = 'US-WA'
CALL neptune.algo.wcc( 
  n, 
  {
    edgeLabels: ["route"],
    vertexLabel: "airport"
  }
)
YIELD component
RETURN n, component
```

## Sample `.wcc` output
<a name="wcc-sample-output"></a>

Here is an example of the output returned by .wcc when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n)
                       CALL neptune.algo.wcc(n)
                       YIELD node, component
                       RETURN node, component
                       LIMIT 2"
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
          "lon": -77.45580292,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KIAD",
          "runways": 4
        }
      },
      "component": 2357352929951779
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
          "lon": -73.77890015,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KJFK",
          "runways": 4
        }
      },
      "component": 2357352929951779
    }
  ]
}
```