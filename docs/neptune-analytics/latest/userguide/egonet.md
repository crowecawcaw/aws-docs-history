# .egonet

This `EgoNet` algorithm finds the (filtered) EgoNet of a vertex to its hopCount-neighbors. An EgoNet,
also known as the egocentric network, is a subgraph of a social network that encapsulates the connections of a
single individual, known as the ego, and all the people they are socially connected to, known as alters.

For each hop, the algorithm gets the `topK` (K is specified per hop by the user via `perHopMaxNeighbor`)
neighbors those have the highest/lowest (based on the `costFunction`) edge weights, and these neighbors become the
source vertices for the next hop. The algorithm assumes the graph is an edge weighted graph.

## `.egonet`   syntax

```
CALL neptune.algo.egonet(
  [`source/ego-node list (required)`],
  {
    hopCount: `fixed hops of traversal (required)`,
    perHopMaxNeighbor: [`list of the max number of top neighor vertices at each hop (required)`],
    perHopEdgeWeightProperty: [`list of edge weight predicates at each hop (required)`],
    edgeWeightType: `numeric type of the specified edgeWeightProperty (required)`,
    edgeLabels: [`list of edge labels for filtering (optional)`],
    perHopVertexLabel: [`list of node labels for filtering at each hop(optional)`],
    perHopTraversalDirection: [`list of traversal directions at each hop (optional, default: outbound)`],
    costFunction: `determines whether the edges having the maximum weights or the minimum weight will be included in the EgoNet (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD egoNode, nodeList, edgeList
RETURN egoNode, nodeList, edgeList
```

## Inputs for the `.egonet` algorithm

- **a source/ego node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting location(s) for the algorithm.

    + Each starting node triggers its own execution of the algorithm.
    + If the source-node list is empty then the query result is also empty.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the source-node list for the algorithm.

- ###### a configuration object that contains:
  - **hopCount** _(required)_   –  
    _type:_ positive integer;  
    _valid values:_ 1, 2 or 3; other values will be rejected.  
    _default:_ none.

  Restricts the number of hops during traversal.
  - **perHopMaxNeighbor** _(required)_   –  
    _type: a list of integers_;  
    _valid values:_ positive integers, or `-1` meaning unlimited;  
    _default:_ none.

  Each integer represents the maximum number of candidate vertices to carry to the next hop. It should have the same size
  as the value of `hopCount`.
  - **perHopEdgeWeightProperty** _(required)_   –  
    _type: a list of strings_;  
    _default:_ none.

  The edge weight predicate for traversal at each hop. If multiple properties exist on an edge having the
  specified name, then one of them is selected at random for the weight value. It should have the same size as
  the value of `hopCount`.
  - **edgeWeightType** _(required)_   –  
    _type: string_;  
    _valid values:_ "int", "long", "float", "double";  
    _default:_ none.

  The numeric data type of the values in the property specified by `perHopEdgeWeightProperty`.
  If an edge contains a property specified by `perHopEdgeWeightProperty` that has a numeric type
  different from what is specified in `edgeWeightType`, the property value is typecast to the type
  specified by `edgeWeightType`.
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **perHopVertexLabel** _(optional)_   –  
    _type:_ a list of vertex label strings;   _default: none_.

  A list of node labels for node filtering at each hop. At each hop, if a node label is provided, vertices
  matching the label are the only vertices that are included, including vertices in the input list. It should
  have the same size as the value of `hopCount`.
  - **perHopTraversalDirection** _(optional)_   –  
    _type:_ a list of strings;  
    _valid values:_ "inbound","outbound", or "both"; _default:_ outbound.

  The direction of edge to follow at each hop. It should have the same size as the value of
  `hopCount`.
  - **costFunction** _(optional)_   –  
    _type:_ `string`;  
    _valid values:_ `"min"`, `"max"`;  
    _default: `"max"`_.

  This determines whether the edges having the maximum weights or the minimum weight will be included in the
  EgoNet adhering the `perHopMaxNeigbor` limits. A `min` value indicates that the edge with
  minimum weights will be included in the EgoNet, whereas a `max` value indicates that the edge with
  maximum weights will be included in the EgoNet.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## Outputs for the `.egonet` algorithm

The .egonet algorithm returns:

- **egoNode**   –  
  The ego vertex for the egonet.
- **nodeList**   –  
  A list of traversed vertices from the ego vertex.
- **edgeList**   –  
  A list of traversed edges from the ego vertex.

## `.egonet`   query examples

This ia a standalone query, where the source node list is
explicitly provided in the query:

```
CALL neptune.algo.egonet(["101"], {
hopCount: 2,
perHopMaxNeighbor: [-1,-1],
edgeLabels: ["route"],
perHopEdgeWeightProperty: ["dist", "dist"],
edgeWeightType: "int",
perHopVertexLabel: ["airport", "airport"],
perHopTraversalDirection: ["outbound", "outbound"],
costFunction: "max",
concurrency: 1
})
YIELD egoNode, nodeList, edgeList
RETURN egoNode, nodeList, edgeList
```

This is a query integration example, where `.egonet` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node list:

```
MATCH (n:airport {code: 'ANC'})
CALL neptune.algo.egonet(n, {
hopCount: 2,
perHopMaxNeighbor: [-1,-1],
edgeLabels: ["route"],
perHopEdgeWeightProperty: ["dist", "dist"],
edgeWeightType: "int",
perHopVertexLabel: ["airport", "airport"],
perHopTraversalDirection: ["outbound", "outbound"],
costFunction: "max",
concurrency: 1
})
YIELD nodeList, edgeList
RETURN n, nodeList, edgeList
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.egonet` output

Here is an example of the output returned by .egonet when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier}
  --query-string "CALL neptune.algo.egonet(["1"], \
  {perHopEdgeWeightProperty: ["dist"], \
  edgeWeightType: "int", \
  hopCount: 1, \
  perHopMaxNeighbor: [3], \
  perHopTraversalDirection: ["both"]}) \
  yield egoNode, edgeList, nodeList \
  return egoNode, edgeList, nodeList" \
  --language open_cypher
  /tmp/out.txt

  cat /tmp/out.txt
{
 "results": [{
 "egoNode": {
 "~id": "1",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "US-GA",
 "runways": 5,
 "country": "US",
 "city": "Atlanta",
 "type": "airport",
 "icao": "KATL",
 "lon": -84.4281005859375,
 "code": "ATL",
 "lat": 33.6366996765137,
 "longest": 12390,
 "elev": 1026,
 "desc": "Hartsfield - Jackson Atlanta International Airport"
 }
},
 "edgeList": [{
 "~id": "neptune_reserved_1_1152921770894950415",
 "~entityType": "relationship",
 "~start": "67",
 "~end": "1",
 "~type": "route",
 "~properties": {
 "dist": 7640
 }
 }, {
 "~id": "neptune_reserved_1_1152922020003053583",
 "~entityType": "relationship",
 "~start": "126",
 "~end": "1",
 "~type": "route",
 "~properties": {
 "dist": 8434
 }
 }, {
 "~id": "neptune_reserved_1_1152921521787699214",
 "~entityType": "relationship",
 "~start": "1",
 "~end": "58",
 "~type": "route",
 "~properties": {
 "dist": 7581
 }
 }],
 "nodeList": [{
 "~id": "126",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "ZA-GT",
 "runways": 2,
 "country": "ZA",
 "city": "Johannesburg",
 "type": "airport",
 "icao": "FAJS",
 "lon": 28.2460002899,
 "code": "JNB",
 "lat": -26.139200210599999,
 "longest": 14495,
 "elev": 5558,
 "desc": "Johannesburg, OR Tambo International Airport"
 }
 }, {
 "~id": "67",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "CN-31",
 "runways": 2,
 "country": "CN",
 "city": "Shanghai",
 "type": "airport",
 "icao": "ZSPD",
 "lon": 121.80500030517599,
 "code": "PVG",
 "lat": 31.1434001922607,
 "longest": 13123,
 "elev": 13,
 "desc": "Shanghai - Pudong International Airport"
 }
 }, {
 "~id": "58",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "AE-DU",
 "runways": 2,
 "country": "AE",
 "city": "Dubai",
 "type": "airport",
 "icao": "OMDB",
 "lon": 55.364398956300001,
 "code": "DXB",
 "lat": 25.2527999878,
 "longest": 13124,
 "elev": 62,
 "desc": "Dubai International Airport"
 }
 }, {
 "~id": "1",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "US-GA",
 "runways": 5,
 "country": "US",
 "city": "Atlanta",
 "type": "airport",
 "icao": "KATL",
 "lon": -84.4281005859375,
 "code": "ATL",
 "lat": 33.6366996765137,
 "longest": 12390,
 "elev": 1026,
 "desc": "Hartsfield - Jackson Atlanta International Airport"
 }
 }]
 }]
}
```
