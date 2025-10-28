# Label propagation mutate algorithm

[Label Propagation Algorithm (LPA)](label-propagation.md "label-propagation.md") is
an algorithm for community detection that is also used in semi-supervised machine
learning for data classification.

The `.labelPropagation.mutate` variant of the algorithm writes the
derived community component ID of each node in the source list to a new property
of that node.

## `.labelPropagation.mutate`  syntax

```
CALL neptune.algo.labelPropagation.mutate(
  {
    writeProperty: `the name for the node property to which to write component IDs`
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
```

## `.labelPropagation.mutate`  inputs

Inputs for `.labelPropagation.mutate` are passed in a configuration object that contains:

- **writeProperty** _(required)_   –  
  _type:_ `string`;   _default: none_.

A name for the new node property that will contain the computed community component ID
of the node.

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

## Outputs for the `.labelPropagation.mutate` algorithm

The community component IDs are written as a new node property of each source
node using the property name specified by `writeProperty`.

If the algorithm is invoked as a standalone query, there is no other output.

If the algorithm is invoked immediately after a `MATCH` clause that supplies its
source node list, the algorithm outputs a key column of the source nodes from
the `MATCH` clause and a value column of success flags (true or false)
to indicate whether or not the write to the new node property of that node succeeded.

## `.labelPropagation.mutate`  query example

```
CALL neptune.algo.labelPropagation.mutate(
  {
    writeProperty: "COMM_ID",
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
```

## Sample  `.labelPropagation.mutate`  output

Here is an example of the output returned by .labelPropagation.mutate when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.labelPropagation.mutate({writeProperty: 'communityId'}) YIELD success RETURN success" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "success": true
    }
  ]
}
```
