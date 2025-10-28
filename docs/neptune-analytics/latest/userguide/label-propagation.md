# Label propagation algorithm (LPA)

Label Propagation Algorithm (LPA) is an algorithm for community detection that is
also used in semi-supervised machine learning for data classification.

A community structure is loosely defined as a tightly knit group of entities in
social networks. LPA can be enhanced by providing a set of seed nodes, the quality
of which can dramatically influence the solution quality of the found communities.
If the seeds are well-selected, the quality of the solution can be good, but if not,
the quality of the solution can be very bad.

See Xu T. Liu _et al_, [Direction-optimizing label propagation
and its application to community detection](https://doi.org/10.1145/3387902.3392634 "https://doi.org/10.1145/3387902.3392634"), and Xu T. Liu _et al_,
[Direction-optimizing Label Propagation
Framework for Structure Detection in Graphs: Design, Implementation, and Experimental
Analysis](https://doi.org/10.1145/3564593 "https://doi.org/10.1145/3564593"), and the [Neo4j
Label Propagation API](https://neo4j.com/docs/graph-data-science/current/algorithms/label-propagation/ "https://neo4j.com/docs/graph-data-science/current/algorithms/label-propagation/").

The time complexity of the algorithm is `O(k|E|)`, where `|E|`
is the number of edges in the graph, and `k` is the number of iterations
for the algorithm to converge. Its space complexity is `O(|V|)`, where
`|V|` is the number of nodes in the graph.

## `.labelPropagation`  syntax

```
CALL neptune.algo.labelPropagation(
  [`source-node list (required)`],
  {
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    vertexWeightProperty: `a numeric node property used to weight the community ID (optional)`,
    vertexWeightType: `numeric type of the specified vertexWeightProperty (optional)`,
    edgeWeightProperty: `a numeric edge property used to weight the community ID (optional)`,
    edgeWeightType: `numeric type of the specified edgeWeightProperty (optional)`,
    maxIterations: `the maximum number of iterations to run (optional, default: 10)`,
    traversalDirection: `traversal direction (optional, default: outbound)`,
    concurrency: `number of threads to use (optional)`
  }
)
Yield node, community
Return node, community
```

## `.labelPropagation`  inputs

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes to use as the starting locations for the algorithm.
Each node in the list triggers an execution of the algorithm. If an
empty list is provided, the query result is also empty.

If the algorithm is called following a `MATCH` clause (query
algo integration), the source query list is the result returned by the
`MATCH` clause.

- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A node label for node filtering. If a node label is provided, nodes matching the label
  are the only nodes that are included in the calculation, including nodes in the input list.
  - **vertexWeightProperty** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  The node weight used in Label Propagation. When `vertexWeightProperty` is not specified,
  each node's `communityId` is treated equally, as if the node weight were 1.0. When the
  `vertexWeightProperty` is specified without an `edgeWeightProperty`, the weight
  of the `communityId` for each node is the value of the node weight property. When both
  `vertexWeightProperty` and `edgeWeightProperty` are specified,
  the weight of the `communityId` is the product of the node property value and edge
  property value.

  Note that if multiple properties exist on the node with the name specified by
  `vertexWeightProperty`, one of those property values will be sampled at random.
  - **vertexWeightType** _(required if `vertexWeightProperty` is present)_   –  
    _type:_ `string`;  
    _valid values:_ `"int"`, `"long"`, `"float"`,
    `"double"`;  
    _default: empty_.

  The type of the numeric values in the node property specified by `vertexWeightProperty`.

  If `vertexWeightProperty` is not provided, `vertexWeightType` is ignored.
  If a node contains a numeric property with the name specified by
  `vertexWeightProperty` but its value is a different numeric type than is specified by
  `vertexWeightType`, the value is typecast to the type specified by `vertexWeightType`.
  If both `vertexWeightType` and `edgeWeightType` are given, the type
  specified by `edgeWeightType` is used for both node and edge properties.
  - **edgeWeightProperty** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  The numeric edge property used as a weight in Label Propagation. When `vertexWeightProperty`
  is not specified, the default edge weight is 1.0, so each edge is treated equally. When only
  `edgeWeightProperty` is provided, the weight of the communityId is the value of that
  edge property. When both `vertexWeightProperty` and `edgeWeightProperty`
  are present, the weight of a `communityId` is the product of the edge property value
  and the node property value.

  Note that if multiple properties exist on the edge with the name specified by
  `edgeWeightProperty`, one of those property values will be sampled at random.
  - **edgeWeightType** _(required if `edgeWeightProperty` is present)_   –  
    _type:_ `string`;  
    _valid values:_ `"int"`, `"long"`, `"float"`,
    `"double"`;  
    _default: none_.

  The type of the numeric values in the edge property specified by `edgeWeightProperty`.

  If `edgeWeightProperty` is not provided, `edgeWeightType` is ignored.
  If a node contains a numeric property with the name specified by `edgeWeightProperty`
  but its value is a different numeric type than is specified by `edgeWeightType`,
  the value is typecast to the type specified by `edgeWeightType`.
  If both `vertexWeightType` and `edgeWeightType` are given, the type
  specified by `edgeWeightType` is used for both node and edge properties.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default:_ `"outbound"`.

  The direction of edge to follow. Must be one of: `"inbound"`,
  `"outbound"`, or `"both"`.
  - **maxIterations** _(optional)_   –  
    _type:_ integer;   _default:_ `10`.

  The maximum number of iterations to run.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## `.labelPropagation`  outputs

- **node**   –  
  A key column of the input nodes.
- **community**   –  
  A key column of the corresponding `communityId` values for those nodes.
  All the nodes with the same `communityId` are in the same weakly-connected
  component.

If the input node list is empty, the output is empty.

## `.labelPropagation`  query examples

This is a standalone example, where the source node list is explicitly provided
in the query. It runs the algorithm over the whole graph, but only queries the
component ID of one node:

```
CALL neptune.algo.labelPropagation(
  ["101"],
  {
    edgeLabels: ["route"],
    maxIterations: 10,
    vertexLabel: "airport",
    vertexWeightProperty: "runways",
    vertexWeightType: "int",
    edgeWeightProperty: "dist",
    edgeWeightType: "int",
    traversalDirection: "both",
    concurrency: 2
  }
)
YIELD node, community
RETURN node, community
```

This is a query integration example, where `.labelPropagation` uses the
output of a preceding `MATCH` clause as its source node list:

```
Match (n)
CALL neptune.algo.labelPropagation(
  n,
  {
    edgeLabels: ["route"],
    maxIterations: 10,
    vertexLabel: "airport",
    vertexWeightProperty: "runways",
    vertexWeightType: "int",
    edgeWeightProperty: "dist",
    edgeWeightType: "int",
    traversalDirection: "both",
    concurrency: 2
  }
)
YIELD community
RETURN n, community
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample   `.labelPropagation`   output

Here is an example of the output returned by .labelPropagation when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
"results": [{
      "node": {
        "~id": "8",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-TX",
          "runways": 7,
          "country": "US",
          "city": "Dallas",
          "type": "airport",
          "icao": "KDFW",
          "lon": -97.038002014160199,
          "code": "DFW",
          "lat": 32.896800994872997,
          "longest": 13401,
          "elev": 607,
          "desc": "Dallas/Fort Worth International Airport"
        }
      },
      "community": 2357352929952311
    }, {
      "node": {
        "~id": "24",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-CA",
          "runways": 3,
          "country": "US",
          "city": "San Jose",
          "type": "airport",
          "icao": "KSJC",
          "lon": -121.929000854492,
          "code": "SJC",
          "lat": 37.362598419189503,
          "longest": 11000,
          "elev": 62,
          "desc": "Norman Y. Mineta San Jose International Airport"
        }
      },
      "community": 2357352929952311
    }]
```
