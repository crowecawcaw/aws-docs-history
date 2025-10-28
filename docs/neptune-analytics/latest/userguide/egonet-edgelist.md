# .egonet.edgeList

This `EgoNet EdgeList` algorithm is the same as the standard `EgoNet` algorithm,
except that this variant has a different output schema, which returns the `EgoNet` in an edge list form.

## `.egonet.edgeList`   syntax

```
CALL neptune.algo.egonet.edgeList(
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
YIELD egoNode, source, target, weight
RETURN egoNode, source, target, weight
```

## Inputs for the `.egonet.edgeList` algorithm

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

## Outputs for the `.egonet.edgeList` algorithm

The .egonet.edgeList algorithm returns:

- **egoNode**   –  
  The ego vertex of the egonet.
- **source**   –  
  The source vertex of an edge in the weighted edge list.
- **target**   –  
  The source vertex of an edge in the weighted edge list.
- **weight**   –  
  The edge weight of the source-target edge in the weighted edge list.

## `.egonet.edgeList`   query examples

This ia a standalone query, where the source node list is
explicitly provided in the query:

```
CALL neptune.algo.egonet.edgeList(["101"], {
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
YIELD egoNode, source, target, weight
RETURN egoNode, source, target, weight
```

This is a query integration example, where `.egonet.edgeList` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node list:

```
MATCH (n:airport {code: 'ANC'})
CALL neptune.algo.egonet.edgeList(n, {
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
YIELD source, target, weight
RETURN n, source, target, weight
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.egonet.edgeList` output

Here is an example of the output returned by .egonet.edgeList when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier}
  --query-string "CALL neptune.algo.egonet(["1"], \
  {perHopEdgeWeightProperty: ["dist", "dist"], \
  edgeWeightType: "int", \
  hopCount: 2, \
  perHopMaxNeighbor: [30, 30], \
  perHopTraversalDirection: ["both", "both"]}) \
  YIELD egoNode, source, target, weight \
  RETURN egoNode, source, target, weight limit 2" \
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
 "source": {
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
 "target": {
 "~id": "27",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "US-CA",
 "runways": 3,
 "country": "US",
 "city": "Long Beach",
 "type": "airport",
 "icao": "KLGB",
 "lon": -118.15200040000001,
 "code": "LGB",
 "lat": 33.817699429999998,
 "longest": 10003,
 "elev": 60,
 "desc": "Long Beach Airport"
 }
 },
 "weight": 2460
 }, {
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
 "source": {
 "~id": "134",
 "~entityType": "node",
 "~labels": ["airport"],
 "~properties": {
 "region": "PE-LIM",
 "runways": 1,
 "country": "PE",
 "city": "Lima",
 "type": "airport",
 "icao": "SPIM",
 "lon": -77.1143035889,
 "code": "LIM",
 "lat": -12.021900176999999,
 "longest": 11506,
 "elev": 113,
 "desc": "Lima, Jorge Chavez International Airport"
 }
 },
 "target": {
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
 "weight": 3189
 }]
}
```
