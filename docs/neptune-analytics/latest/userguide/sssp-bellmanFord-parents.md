# Bellman-Ford single source shortest path (SSSP) parents algorithm

The `.sssp.bellmanFord.parents` algorithm uses the [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm "https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm")
algorithm to find the parent nodes along with the shortest path distances from the source
node to all other nodes in the graph.

Neptune Analytics implements the algorithm such that:

- Positive edge weights must be provided using the `edgeWeightProperty` field
- Negative edge weights are not supported.
- The traversal direction cannot be set to `both`.

## `.sssp.bellmanFord.parents`   syntax

```
CALL neptune.algo.sssp.bellmanFord.parents(
  [`source-node list (required)`],
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

## `.sssp.bellmanFord.parents`   inputs

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting location(s) for the algorithm.

    + Each starting node triggers its own execution of the algorithm.
    + If the source-node list is empty then the query result is also empty.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the source-node list for the algorithm.

- ###### a configuration object that contains:
  - **edgeWeightProperty** _(required)_   –  
    _type:_ `string`;   _example:_ `"distnce"`;
      _default: none_.

  The edge weight predicate for traversal.
  - **edgeWeightType** _(required)_   –  
    _type:_ `string`;   _valid values:_
    `"int"`, `"long"`, `"float"`, `"double"`.

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

## Outputs for the `.sssp.bellmanFord.parents` algorithm

For every node that can be reached from the specified source list, the algorithm
returns:

- **source**   –  
  The source node.
- **node**   –  
  A node found traversing from the source.
- **distance**   –  
  The distance between the source node and the found node.
- **parent**   –  
  The parent of the found node. Note that the parent of the source vertex is itself.

## `.sssp.bellmanFord.parents`   query examples

This is a standalone query, where a source node (or nodes) is explicitly provided:

```
CALL neptune.algo.sssp.bellmanFord.parents(
  ["101"],
  {
    edgeLabels: ["route"],
    edgeWeightProperty: "dist",
    edgeWeightType: "int"
  }
)
```

This is a query integration example, where where `.sssp.bellmanFord.parents` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node list:

```
MATCH (source:airport {code: 'ANC'})
CALL neptune.algo.sssp.bellmanFord.parents(
  source,
  {
    edgeLabels: ["route"],
    edgeWeightProperty: "dist",
    edgeWeightType: "int",
    vertexLabel: "airport",
    traversalDirection: "outbound",
    concurrency: 1
  }
)
YIELD node, parent, distance
RETURN source, node, parent, distance
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.sssp.bellmanFord.parents` output

Here is an example of the output returned by .sssp.bellmanFord.parents when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.sssp.bellmanFord.parents(['101'],
       {edgeWeightProperty: 'dist', edgeWeightType: 'int'})
     yield source, node, parent
     return source, node, parent
     limit 2" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "source": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "prscore": 0.002498496090993285,
          "degree": 308,
          "lon": 100.747001647949,
          "wccid": 2357352929951779,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      },
      "node": {
        "~id": "2709",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 65.4809036254883,
          "elev": 49,
          "longest": 8711,
          "city": "Nadym",
          "type": "airport",
          "region": "RU-YAN",
          "desc": "Nadym Airport",
          "code": "NYM",
          "prscore": 0.00016044313088059425,
          "degree": 18,
          "lon": 72.6988983154297,
          "wccid": 2357352929951779,
          "country": "RU",
          "icao": "USMM",
          "runways": 1
        }
      },
      "parent": {
        "~id": "810",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 55.0125999450684,
          "elev": 365,
          "longest": 11818,
          "city": "Novosibirsk",
          "type": "airport",
          "region": "RU-NVS",
          "desc": "Tolmachevo Airport",
          "code": "OVB",
          "prscore": 0.0012910010991618038,
          "degree": 162,
          "lon": 82.6507034301758,
          "wccid": 2357352929951779,
          "country": "RU",
          "icao": "UNNT",
          "runways": 2
        }
      }
    },
    {
      "source": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "prscore": 0.002498496090993285,
          "degree": 308,
          "lon": 100.747001647949,
          "wccid": 2357352929951779,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      },
      "node": {
        "~id": "2667",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 56.8567008972168,
          "elev": 2188,
          "longest": 6562,
          "city": "Ust-Kut",
          "type": "airport",
          "region": "RU-IRK",
          "desc": "Ust-Kut Airport",
          "code": "UKX",
          "prscore": 0.000058275499999999997,
          "degree": 4,
          "lon": 105.730003356934,
          "wccid": 2357352929951779,
          "country": "RU",
          "icao": "UITT",
          "runways": 1
        }
      },
      "parent": {
        "~id": "1038",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 52.2680015563965,
          "elev": 1675,
          "longest": 10384,
          "city": "Irkutsk",
          "type": "airport",
          "region": "RU-IRK",
          "desc": "Irkutsk Airport",
          "code": "IKT",
          "prscore": 0.0008466026629321277,
          "degree": 84,
          "lon": 104.388999938965,
          "wccid": 2357352929951779,
          "country": "RU",
          "icao": "UIII",
          "runways": 1
        }
      }
    }
  ]
}
```
