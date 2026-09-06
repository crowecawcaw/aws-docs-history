

# PageRank mutate centrality algorithm
<a name="page-rank-mutate"></a>

The ranking metric computed by `.pageRank.mutate` can indicate the importance of a node within a given graph, with the most important nodes having the highest score, and the least important node having the lowest score. PageRank is used in search engines to rank web pages based on their importance and influence, in citation networks to identify highly cited scientific papers, and in recommendation systems to suggest popular and relevant content to users.

The mutate variant of the PageRank algorithm performs the PageRank calculation over the entire graph unless the configuration parameters establish a filter, and each traversed node's calculated PageRank value is stored on that node as a property.

## `pageRank.mutate`  inputs
<a name="page-rank-mutate-inputs"></a>

Inputs for the `pageRank.mutate` algorithm are passed in a configuration object parameter that contains:
+ **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
+ **writeProperty** *(required)*   –   *type:* `string`;   *default: none*.

  A name for the new vertex property that will contain the computed PageRank values. If a property of that name already exists, it is overwritten.
+ **vertexLabel** *(optional)*   –   *type:* `string`;   *default: none*.

  A vertex label for vertex filtering. If a vertex label is provided, vertices matching the label are the only vertices that are included, including vertices in the input list.
+ **traversalDirection** *(optional)*   –   *type:* `string`;   *default:*` "outbound"`.

  The direction of edge to follow. Must be one of: `"outbound"` or `"inbound"`.
+ **numOfIterations** *(optional)*   –   *type:* a positive integer greater than zero;   *default: 20*.

  The number of iterations to perform to reach convergence. A number between 10 and 20 is recommended.
+ **dampingFactor** *(optional)*   –   *type:* a positive floating-point number less than or equal to `1.0`;   *default: *` 0.85`.

  A positive floating-point damping factor between 0.0 and 1.0 that expresses the probability, at any step, that the node will continue.
+ **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

  Controls the number of concurrent threads used to run the algorithm.

   If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.
+ **tolerance** *(optional)*   –   a floating point number between 0.0 and 1.0 (inclusive). When the average difference in the pageRank values of two iterations drops below `tolerance`, the algorithm stops, regardless of whether the `numOfIterations` is reached. Default value is `0.000001 (1e-6)`.
  + Note that this tolerance computation is equivalent to L1 error or sum of Mean Absolute Difference (MAE)s.
  + The stopping condition is `l1_error_sum < tolerance * numNodes`, equivalent to `l1_error_sum/numNodes < tolerance`.
+ **edgeWeightProperty** *(optional)*   –   *type:* `string`   *default: none*.

  The weight property to consider for weighted pageRank computation.
+ **edgeWeightType** *(optional) - required if `edgeWeightProperty` is present*   –   *type:* `string`;   *default: none*.

  The type of values associated with the edgeWeightProperty argument, specified as a string. *valid values*: "int", "long", "float", "double".
  + If the edgeWeightProperty is not given, the algorithm runs unweighted no matter if the edgeWeightType is given or not.
  + Note that if multiple properties exist on the edge with the name specified by edgeWeightProperty, one of those property values will be sampled at random.
+ **sourceNodes** *(optional) - required if running personalized PageRank*   –   *type:* `list`;   *default: none*.

  A personalization vertex list ["101", ...]
  +  Can include 1 to 8192 vertices. 
  +  If a `vertexLabel` is provided, nodes that do not have the given `vertexLabel` are ignored. 
+ **sourceWeights** *(optional)*   –   *type:* `list`;   *default: none*.

  A personalization weight list. The weight distribution among the personalized vertices.
  +  If not provided, the default behavior is uniform distribution among the vertices given in `sourceNodes`. 
  +  There must be at least one non-zero weight in the list. 
  +  The length of the sourceWeights list must match the `sourceNodes` list. 
  +  The mapping of personalization vertex and weight lists are one to one. The first value in the weight list corresponds to the weight of first vertex in the vertex list, second value is for the second vertex, etc. 
  +  The weights can be one of `int`, `long`, `float`, or `double` types. 

## Outputs for the `pageRank.mutate` algorithm
<a name="page-rank-mutate-outputs"></a>

The computed PageRank values are written to a new vertex property on each node using the property name specified by the `writeProperty` input parameter.

A single Boolean `success` value (`true` or `false`) is returned, which indicates whether or not the writes succeeded.

## Query example for `pageRank.mutate`
<a name="page-rank-mutate-query-example"></a>

The example below computes the PageRank score of every vertex in the graph, and writes that score to a new vertex property named `P_RANK`:

```
CALL neptune.algo.pageRank.mutate(
  {
    writeProperty:"P_RANK",
    dampingFactor: 0.85,
    numOfIterations: 1,
    edgeLabels: ["route"]
  }
)
```

This query illustrates how you could then access the PageRank values in the `P_RANK` vertex property. It counts how many nodes have a `P_RANK` property value greater than the "SEA" node's `P_RANK` property value:

```
MATCH (n) WHERE n.code = "SEA" WITH n.P_RANK AS lowerBound
MATCH (m) WHERE m.P_RANK > lowerBound
RETURN count(m)
```

## Query examples for Personalized `pageRank.mutate`
<a name="personalized-page-rank-mutate-query-examples"></a>

 Personalized PagerRank applies the same integration and constraints. Here are some examples that pass personalization-specific configurations. 

 The example below computes the Personalized PageRank score of every vertex in the graph, and writes that score to a new vertex property named "PRS\_RANK": 

```
CALL neptune.algo.pageRank.mutate(
  {
    writeProperty:"PRS_RANK",
    sourceNodes:[”101”, “103”, “105”],
    sourceWeights:[5, 3, 2],
    dampingFactor: 0.85,
    numOfIterations: 1,
    edgeLabels: ["route"]
  }
)
```

## Sample   `.pageRank.mutate`   output
<a name="page-rank-mutate-sample-output"></a>

Here is an example of the output returned by .pageRank.mutate when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.pageRank.mutate({writeProperty: 'prscore'}) YIELD success RETURN success" \
  --language open_cypher \
  /tmp/out.txt
  
cat /tmp/out.txt  
{
  "results": [
    { "success": true }
  ]
}
```