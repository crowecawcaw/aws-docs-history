# TopK hop-limited single source (weighted) shortest path algorithm

The `.topksssp`algorithm finds the single-source weighted shortest paths
from a source node to its neighbors out to the distance specified by `maxDepth`.
It accumulates the path lengths using the edge weights along the paths and then returns a
sorted list of the shortest paths.

## `.topksssp`   syntax

```
CALL neptune.algo.topksssp(
  [`source-node list (required)`],
  {
    hopCount: `maximum hops on the shortest path (required)`,
    perHopLimits: [`a list of the maximum number of nodes to carry forward at each hop (required)`],
    edgeLabels: [`list of edge labels for filtering (optional)`],
    edgeWeightProperty: `a numeric edge property to weight the traversal (optional)`,
    edgeWeightType: `numeric type of the specified edgeWeightProperty (optional)`,
    vertexLabel: `a node label for filtering (optional)`,
    traversalDirection: `traversal direction (optional, default: outbound)`,
    costFunction: `determines whether the topK distances are in ascending or descending order (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD source, node, distance
RETURN source, node, distance
```

## Inputs for the `topksssp` algorithm

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting location(s) for the algorithm.

    + Each starting node triggers its own execution of the algorithm.
    + If the source-node list is empty then the query result is also empty.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the source-node list for the algorithm.

- ###### a configuration object that contains:
  - **hopCount** _(required)_   –  
    _type:_ positive integer;   _default:_ none.

  Restricts the number of hops on a shortest path, which restricts the number of iterations of the
  SSSP algorithm to be used.
  - **perHopLimits** _(required)_   –  
    _type: a list of integers_;  
    _valid values:_ positive integers, or `-1` meaning unlimited;  
    _default:_ none.

  Each integer represents the maximum number of candidate vertices to carry to the next hop.
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **edgeWeightProperty** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  The edge weight predicate to for traversal. If no property is specified then the algorithm runs
  unweighted. If multiple properties exist on an edge having the specified name, then one of them is
  selected at random for the weight value.
  - **edgeWeightType** _(optional)_   –  
    _type:_ `string`;   _valid values:_
    `"int"`, `"long"`, `"float"`, `"double"`.

  The numeric data type of the values in the property specified by `edgeWeightProperty`.
  If the `edgeWeightProperty` is not present, `edgeWeightType` is ignored
  and the algorithm runs unweighted. If an edge contains a property specified by
  `edgeWeightProperty` that has a numeric type different from what is specified in
  `edgeWeightType`, the property value is typecast to the type specified by
  `edgeWeightType`.
  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A node label for node filtering. If a node label is provided, vertices matching the label
  are the only vertices that are included, including vertices in the input list.
  - **costFunction** _(optional)_   –  
    _type:_ `string`;  
    _valid values:_ `"min"`, `"max"`;  
    _default: `"min"`_.

  Specifies the ordering of the topK distances returned. A `"min"` value indicates that the topK distances
  between the source and target vertices should be returned in descending order, whereas a `"max"` value
  indicates that they should be returned in ascending order.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## Outputs for the `topksssp` algorithm

For every node that can be reached from the specified source list, the algorithm
returns:

- **source**   –  
  The source node.
- **node**   –  
  A node found traversing from the source.
- **distance**   –  
  The distance between the source node and the found node.

## `.topksssp`   query examples

This ia a standalone query, where the source node list is
explicitly provided in the query:

```
CALL neptune.algo.topksssp(
  ["101"],
  {
    edgeLabels: ["route"],
    hopCount: 3,
    perHopLimits: [10, 100, 1000],
    edgeWeightProperty: "dist",
    edgeWeightType: "int"
  }
)
```

This is a query integration example, where `.topksssp` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node list:

```
MATCH (n) WHERE id(n) IN ["108","109"]
CALL neptune.algo.topksssp(
  n,
  {
    edgeLabels: ["route"],
    edgeWeightProperty: "dist",
    edgeWeightType: "int",
    hopCount: 5,
    perHopLimits: [5,10,15,20,25]
  }
)
YIELD distance
RETURN n, collect(distance) AS distances'
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.topksssp` output

Here is an example of the output returned by .topksssp when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier}
  --query-string "CALL neptune.algo.topksssp(['101'], {hopCount: 2, perHopLimits: [3, 5]})
      YIELD source, node, distance
      RETURN source, node, distance limit 2" \
  --language open_cypher
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
        "~id": "170",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 40.8860015869,
          "elev": 294,
          "longest": 8622,
          "city": "Naples",
          "type": "airport",
          "region": "IT-72",
          "desc": "Naples International Airport",
          "code": "NAP",
          "prscore": 0.001119577675126493,
          "degree": 222,
          "lon": 14.2908000946,
          "wccid": 2357352929951779,
          "country": "IT",
          "icao": "LIRN",
          "runways": 1
        }
      },
      "distance": 2.0
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
      "distance": 2.0
    }
  ]
}
```
