# .degreeDistribution centrality algorithm

The `.degreeDistribution` algorithm is a tool for analyzing and
visualizing the structural characteristics of a graph. It calculates the
frequency distribution of vertex degrees across the entire network and provides
basic statistics of the distribution.

`.degreeDistribution` provides insight into the topology and connectivity
patterns of the network, such as identifying the hubs (i.e., super nodes
or high-degree nodes) and distinguishing different network types (e.g.,
tree vs. scale-free), which can help making informed decisions on selecting
appropriate algorithms for analysis.

The `%degreeDistribution` magic command in the notebook provides an interactive
visualization of the output, please see the [notebook magics](../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-degree-distribution "../../../neptune/latest/userguide/notebooks-magics.md#notebooks-line-magics-degree-distribution")
documentation for details.

## `.degreeDistribution`   syntax

```
CALL neptune.algo.degreeDistribution(
  {
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabels: "`a list of vertex labels for filtering (optional)`",
    binWidth: `a positive integer that specifies the size of each bin in the degree distribution (optional, default: 1)`,
    traversalDirection: `the direction of edge used for degree computation (optional, default: "both"`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD output
RETURN output
```

## Inputs for the `.degreeDistribution` algorithm

- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabels** _(optional)_   –  
    _type:_ `a list of vertex label strings`;   _default: no vertex filtering_.

  To filter on one or more vertex labels, provide a list of the ones to filter on. If no vertexLabels field is
  provided then all vertex labels are considered for degree computation.
  - **binWidth** _(optional)_   –  
    _type:_ `integer`;   _default: 1_.

  To specify the size of each bin in the degree distribution, provide an integer value.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default:_ `"both"`.

  The direction of edge to follow. Must be one of: `"inbound"`,
  `"outbound"`, or `"both"`.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## Sample   `.degreeDistribution`   output

Here is an example of the output returned by .degreeDistribution when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
    \
   --region ${region}
   --graph-identifier ${graphIdentifier} \
   --query-string "CALL neptune.algo.degreeDistribution({binWidth: 50, vertexLabels: ['airport', 'country'], edgeLabels: ['route'], traversalDirection: 'inbound'}) YIELD output RETURN output" \
   --language open_cypher \
   /tmp/out.txt

cat /tmp/out.txt
{
  "results": [{
      "output": {
        "statistics": {
          "maxDeg": 307,
          "mean": 13.511229946524065,
          "minDeg": 0,
          "p50": 3,
          "p75": 9,
          "p90": 36,
          "p95": 67,
          "p99": 173,
          "p999": 284
        },
        "distribution": [[0, 268], [50, 3204], [100, 162], [150, 54], [200, 29], [250, 16], [300, 5], [350, 2]]
      }
    }]
}

```

## Query examples for `.degreeDistribution`

This is a standalone example, where the in-degree distribution is computed for the
graph with specified vertex labels and edge label, and the mean degree is returned.

```
CALL neptune.algo.degreeDistribution({
   vertexLabels: ['airport', 'country'],
   edgeLabels: ['route'],
   traversalDirection: 'inbound',
})
YIELD output
WITH output.statistics.mean as meanDegree
RETURN meanDegree

```
