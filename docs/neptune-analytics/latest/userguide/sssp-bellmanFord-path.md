# Bellman-Ford single source single target shortest path algorithm

The `.sssp.bellmanFord.path` algorithm uses the Bellman-Ford algorithm to find the shortest path along
with the shortest path distances from a source node to a target node in the graph. If there are multiple shortest paths
between the source node and the target node, only one will be returned. The algorithm can run only weighted, with
`edgeWeightProperty` provided.

Neptune Analytics implements the algorithm such that:

- Positive edge weights must be provided using the `edgeWeightProperty` field.
- Negative edge weights are not supported.
- The traversal direction cannot be set to `both`.

## `.sssp.bellmanFord.path`   syntax

```
CALL neptune.algo.sssp.bellmanFord.path(
  [`source node(s) (required)`], [`target node(s) (required)`]
  {
    edgeWeightProperty: `edge weight predicate for traversal (required)`
    edgeWeightType: `numeric type of the edge weight property (required)`
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    traversalDirection: `traversal direction (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD `the outputs to generate (source and/or node)`
RETURN `the outputs to return`
```

## `.sssp.bellmanFord.path`   inputs

- **source node(s)**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting location(s) for the algorithm.

    + Each starting node triggers its own execution of the algorithm.
    + If the source node(s) is empty then the query result is also empty.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the source node(s) for the algorithm.

- **target node(s)**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the ending location(s) for the algorithm.

    + Each source-target node pair produces an output of the algorithm.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the target node(s) for the algorithm.

- ###### a configuration object that contains:
  - **edgeWeightProperty** _(required)_   –  
    _type:_ `string`;   _default: none_.

  The edge weight predicate for traversal.
  - **edgeWeightType** _(required)_   –  
    _type:_ `string`;   _valid values:_ `"int"`,
    `"long"`, `"float"`, `"double"`.

  The numeric data type of the values in the property specified by `edgeWeightProperty`.
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel**   _(optional)_   –  
    _type:_ `string`;   _example:_
    `"airport"`;  *default:* no node filtering.

  A node label for node filtering. If a node label is provided, vertices matching the label are the only
  vertices that are included, including vertices in the input list.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default:_ `"outbound"`.

  The direction of edge to follow. Must be one of: `"inbound"` or `"outbound"`.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## Outputs for the `.sssp.bellmanFord.path` algorithm

For every pair of source and target nodes, the algorithm returns:

- **source**   –  
  The source vertex.
- **target**   –  
  The target vertex.
- **distance**   –  
  The total shortest path distance from source to target.
- **vertexPath**   –  
  A list of vertices in the path in visit order (including the source and the target).
- **allDistances**   –  
  A list of cumulative distances to the vertices in the traversal path (including the source and the target).
- **path**   –  
  An openCypher path object representing the shortest path between the source and the target. (A list of vertices from the
  source vertex to the target vertex, interleaved with the corresponding edges, representing the shortest path. Sequence
  of vertex id (source), edge id, vertex id, edge id, ..., vertex id (target)).
  - Starts and ends with a vertex, and has edges in between each vertex.
  - Includes the source and the target vertices.

## `.sssp.bellmanFord.path`   query examples

This is a standalone query, where a source node and target node are explicitly provided:

```
CALL neptune.algo.sssp.bellmanFord.path(
  "9", "37",
  {
    edgeLabels: ["route"],
    edgeWeightProperty: "dist",
    edgeWeightType: "int"
  }
)
```

This is a query integration example, where `.sssp.bellmanFord.path` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node(s) and target node(s):

```
MATCH (source:airport {code: 'FLL'})
MATCH (target:airport {code: 'HNL'})
CALL neptune.algo.sssp.bellmanFord.path(
  source, target,
  {
    edgeLabels: ["route"],
    edgeWeightProperty: "dist",
    edgeWeightType: "int",
    vertexLabel: "airport",
    traversalDirection: "outbound",
    concurrency: 1
  }
)
YIELD distance, vertexPath, allDistances, path
RETURN source, target, distance, vertexPath, allDistances, path
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes are returned; and that every source-target node pair produces
an output, which can result in a very large query output if a large number of nodes are returned.
Use `LIMIT` or put conditions on the `MATCH` clause to restrict its output
appropriately.

## Sample `.sssp.bellmanFord.path` output

Here is an example of the output returned by .sssp.bellmanFord.path when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n:airport {code: 'FLL'})
  MATCH (m:airport {code: 'HNL'})
  CALL neptune.algo.sssp.bellmanFord.path(n, m, {
  edgeWeightProperty: "dist",
  edgeWeightType: "int",
  edgeLabels: ["route"],
  vertexLabel: "airport",
  traversalDirection: "outbound",
  concurrency: 1
  })
  YIELD source, target, distance, vertexPath, allDistances, path
  RETURN source, target, distance, vertexPath, allDistances, path" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [{
      "source": {
        "~id": "9",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-FL",
          "runways": 2,
          "country": "US",
          "city": "Fort Lauderdale",
          "type": "airport",
          "icao": "KFLL",
          "lon": -80.152702331542997,
          "code": "FLL",
          "lat": 26.0725994110107,
          "longest": 9000,
          "elev": 64,
          "desc": "Fort Lauderdale/Hollywood International Airport"
        }
      },
      "target": {
        "~id": "37",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-HI",
          "runways": 4,
          "country": "US",
          "city": "Honolulu",
          "type": "airport",
          "icao": "PHNL",
          "lon": -157.92199707031199,
          "code": "HNL",
          "lat": 21.318700790405298,
          "longest": 12312,
          "elev": 13,
          "desc": "Honolulu International Airport"
        }
      },
      "distance": 4854,
      "vertexPath": [{
          "~id": "9",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-FL",
            "runways": 2,
            "country": "US",
            "city": "Fort Lauderdale",
            "type": "airport",
            "icao": "KFLL",
            "lon": -80.152702331542997,
            "code": "FLL",
            "lat": 26.0725994110107,
            "longest": 9000,
            "elev": 64,
            "desc": "Fort Lauderdale/Hollywood International Airport"
          }
        }, {
          "~id": "11",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-TX",
            "runways": 5,
            "country": "US",
            "city": "Houston",
            "type": "airport",
            "icao": "KIAH",
            "lon": -95.341400146484403,
            "code": "IAH",
            "lat": 29.984399795532202,
            "longest": 12001,
            "elev": 96,
            "desc": "George Bush Intercontinental"
          }
        }, {
          "~id": "37",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-HI",
            "runways": 4,
            "country": "US",
            "city": "Honolulu",
            "type": "airport",
            "icao": "PHNL",
            "lon": -157.92199707031199,
            "code": "HNL",
            "lat": 21.318700790405298,
            "longest": 12312,
            "elev": 13,
            "desc": "Honolulu International Airport"
          }
        }],
      "allDistances": [0, 964, 4854],
      "path": [{
          "~id": "9",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-FL",
            "runways": 2,
            "country": "US",
            "city": "Fort Lauderdale",
            "type": "airport",
            "icao": "KFLL",
            "lon": -80.152702331542997,
            "code": "FLL",
            "lat": 26.0725994110107,
            "longest": 9000,
            "elev": 64,
            "desc": "Fort Lauderdale/Hollywood International Airport"
          }
        }, {
          "~id": "neptune_reserved_1_1152921504607567884",
          "~entityType": "relationship",
          "~start": "9",
          "~end": "11",
          "~type": "route",
          "~properties": {
            "dist": 964
          }
        }, {
          "~id": "11",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-TX",
            "runways": 5,
            "country": "US",
            "city": "Houston",
            "type": "airport",
            "icao": "KIAH",
            "lon": -95.341400146484403,
            "code": "IAH",
            "lat": 29.984399795532202,
            "longest": 12001,
            "elev": 96,
            "desc": "George Bush Intercontinental"
          }
        }, {
          "~id": "neptune_reserved_1_1152921508902600717",
          "~entityType": "relationship",
          "~start": "11",
          "~end": "37",
          "~type": "route",
          "~properties": {
            "dist": 3890
          }
        }, {
          "~id": "37",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-HI",
            "runways": 4,
            "country": "US",
            "city": "Honolulu",
            "type": "airport",
            "icao": "PHNL",
            "lon": -157.92199707031199,
            "code": "HNL",
            "lat": 21.318700790405298,
            "longest": 12312,
            "elev": 13,
            "desc": "Honolulu International Airport"
          }
        }]
    }]
}
```
