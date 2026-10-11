

# Eigenvector centrality mutate algorithm
<a name="eigenvector-centrality-mutate"></a>

The `.eigenvectorCentrality.mutate` algorithm computes and stores each node's [eigenvector centrality](eigenvector-centrality.md) value as a property of the node. Eigenvector centrality measures a node's importance by accounting for both the number and the importance of the nodes connected to it. Nodes that are connected to many highly connected nodes receive higher scores.

The algorithm returns a single success flag (`true` or `false`), which indicates whether the writes succeeded or failed.

## `.eigenvectorCentrality.mutate` syntax
<a name="eigenvector-centrality-mutate-syntax"></a>

```
CALL neptune.algo.eigenvectorCentrality.mutate(
  {
    writeProperty: {{property name for the computed scores (required)}},
    numOfIterations: {{a positive integer like 20 (optional)}},
    vertexLabels: [{{a list of vertex labels for filtering (optional)}}],
    edgeLabels: [{{a list of edge labels for filtering (optional)}}],
    traversalDirection: {{the direction of edge to follow (optional)}},
    tolerance: {{a floating point number between 0.0 and 1.0 (inclusive) (optional)}},
    edgeWeightProperty: {{the weight property for weighted computation (optional)}},
    edgeWeightType: {{the type of values for the weight property (optional)}},
    sourceNodes: [{{a list of node IDs to personalize on (optional)}}],
    sourceWeights: [{{a list of non-negative weights for the sourceNodes (optional)}}],
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD success
RETURN success
```

## `eigenvectorCentrality.mutate` inputs
<a name="eigenvector-centrality-mutate-inputs"></a>

Inputs for the `eigenvectorCentrality.mutate` algorithm are passed in a configuration object parameter that contains:
+ **writeProperty**   *(required)*   –   *type:* `string`;   *default: none*.

  A name for the new vertex property that will contain the computed eigenvector centrality scores. If a property of that name already exists, the algorithm overwrites it.
+ **numOfIterations**   *(optional)*   –   *type:* a positive integer greater than zero;   *default: 20*.

  The number of iterations to perform to reach convergence. A number between 10 and 20 is recommended.
+ **vertexLabels**   *(optional)*   –   *type:* a list of vertex label strings;   *default: no vertex filtering*.

  To filter on one or more vertex labels, provide a list of the ones to filter on. If no `vertexLabels` field is provided then all vertex labels are considered.
+ **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
+ **traversalDirection**   *(optional)*   –   *type:* `string`;   *default:* `"outbound"`.

  The direction of edge to follow. Must be one of: `"inbound"`, `"outbound"`, or `"both"`.
+ **tolerance**   *(optional)*   –   *type:* `float`;   *default:* `0.000001 (1e-6)`.

  A floating point number between 0.0 and 1.0 (both inclusive). The algorithm stops early when the scores have converged enough that the total change across all vertices between two iterations drops below `number of vertices * tolerance`, regardless of whether `numOfIterations` has been reached.
+ **edgeWeightProperty**   *(optional)*   –   *type:* `string`;   *default: none*.

  The weight property to consider for weighted eigenvector centrality computation.
+ **edgeWeightType**   *(required if edgeWeightProperty is present)*   –   *type:* `string`;   *default: none*.

  The type of values associated with the `edgeWeightProperty` argument, specified as a string. *Valid values*: `"int"`, `"long"`, `"float"`, `"double"`.
  + If the `edgeWeightProperty` is not given, the algorithm runs unweighted no matter if the `edgeWeightType` is given or not.
+ **sourceNodes**   *(optional, required if running personalized eigenvector centrality)*   –   *type:* `list`;   *default: none*.

  A personalization vertex list ["101", ...].
  + Can include 1 to 8192 vertices.
  + If a `vertexLabels` is provided, nodes that do not have the given vertex label are ignored.
+ **sourceWeights**   *(optional)*   –   *type:* `list`;   *default: none*.

  A personalization weight list. The weight distribution among the personalized vertices.
  + If not provided, the default behavior is uniform distribution among the vertices given in `sourceNodes`.
  + There must be at least one non-zero weight in the list.
  + The length of the `sourceWeights` list must match the `sourceNodes` list.
  + The mapping of personalization vertex and weight lists are one to one. The first value in the weight list corresponds to the weight of first vertex in the vertex list, second value is for the second vertex, etc.
  + The weights can be one of `int`, `long`, `float`, or `double` types.
+ **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

  Controls the number of concurrent threads used to run the algorithm.

   If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## `eigenvectorCentrality.mutate` outputs
<a name="eigenvector-centrality-mutate-outputs"></a>

The algorithm writes the computed eigenvector centrality scores to a new vertex property on each node using the property name specified by the `writeProperty` input parameter.

The algorithm returns a single Boolean `success` value (`true` or ` false`) that indicates whether the writes succeeded.

## `eigenvectorCentrality.mutate` query examples
<a name="eigenvector-centrality-mutate-examples"></a>

The example below computes the eigenvector centrality score of every vertex in the graph, and writes that score to a new vertex property named `EV_SCORE`:

```
CALL neptune.algo.eigenvectorCentrality.mutate(
  {
    writeProperty: "EV_SCORE",
    numOfIterations: 10,
    edgeLabels: ["route"]
  }
)
YIELD success
RETURN success
```

This query illustrates how you could then access the eigenvector centrality values in the `EV_SCORE` vertex property:

```
MATCH (n) WHERE n.code = "SEA" WITH n.EV_SCORE AS lowerBound
MATCH (m) WHERE m.EV_SCORE > lowerBound
RETURN count(m)
```

## Sample `.eigenvectorCentrality.mutate` output
<a name="eigenvector-centrality-mutate-sample-output"></a>

The following example shows the output that `.eigenvectorCentrality.mutate` returns when you run it against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string "CALL neptune.algo.eigenvectorCentrality.mutate({writeProperty: 'evscore'}) YIELD success RETURN success" \
    --language open_cypher \
    /tmp/out.txt
cat /tmp/out.txt
{
  "results": [
    { "success": true }
  ]
}
```