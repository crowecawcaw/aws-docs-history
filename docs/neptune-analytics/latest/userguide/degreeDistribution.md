

# .degreeDistribution algorithm
<a name="degreeDistribution"></a>

The `.degreeDistribution` algorithm is a tool for analyzing and visualizing the structural characteristics of a graph. It calculates the frequency distribution of vertex degrees across the entire network and provides basic statistics of the distribution.

`.degreeDistribution` provides insight into the topology and connectivity patterns of the network, such as identifying the hubs (i.e., super nodes or high-degree nodes) and distinguishing different network types (e.g., tree vs. scale-free), which can help making informed decisions on selecting appropriate algorithms for analysis.

The `%degreeDistribution` magic command in the notebook provides an interactive visualization of the output, please see the [notebook magics](https://docs.aws.amazon.com/neptune/latest/userguide/notebooks-magics.html#notebooks-line-magics-degreeDistribution) documentation for details.

## `.degreeDistribution`   syntax
<a name="degreeDistribution-syntax"></a>

```
CALL neptune.algo.degreeDistribution(
  {
    vertexLabels: [{{a list of vertex labels for filtering (optional)}}],
    edgeLabels: [{{a list of edge labels for filtering (optional)}}],
    binWidth: {{a positive integer that specifies the size of each bin in the degree distribution (optional, default: 1)}},
    traversalDirection: {{the direction of edge used for degree computation (optional, default: "both")}},
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD output
RETURN output
```

## `.degreeDistribution`   inputs
<a name="degreeDistribution-inputs"></a>
+ 

**a configuration object that contains:**
  + **vertexLabels**   *(optional)*   –   *type:* a list of vertex label strings;   *example:* `["airport", {{...}}]`;   *default:* no vertex filtering.

    To filter on one more vertex labels, provide a list of the ones to filter on. If no `vertexLabels` field is provided then all vertex labels are processed during traversal.
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **binWidth** *(optional)*   –   *type:* `integer`;   *default: 1*.

    To specify the size of each bin in the degree distribution, provide an integer value.
  + **traversalDirection** *(optional)*   –   *type:* `string`;   *default:*` "both"`.

    The direction of edge to follow. Must be one of: `"inbound"`, `"outbound"`, or `"both"`.
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## `.degreeDistribution`   outputs
<a name="degreeDistribution-outputs"></a>

There is a single column in the output containing a map with the following key components:
+ **distribution**   –   A list of lists where each list item is as follows:
  + [`degree`, `count`]   –   Degree and corresponding count. The list is sorted in the increasing order of `degree`.
+ **statistics**   –   A map with the following components:
  + `maxDeg`   –   the maximum degree in the graph.
  + `mean`   –   the average degree in the graph.
  + `minDeg`   –   the minimum degree in the graph.
  + `p50`   –   the 50th percentile degree in the graph, i.e., median.
  + `p75`   –   the 75th percentile degree in the graph.
  + `p90`   –   the 90th percentile degree in the graph.
  + `p95`   –   the 95th percentile degree in the graph.
  + `p99`   –   the 99th percentile degree in the graph.
  + `p999`   –   the 99.9th percentile degree in the graph.

## `.degreeDistribution`   query examples
<a name="degreeDistribution-query-examples"></a>

This is a standalone example, where the in-degree distribution is computed for the graph with specified vertex labels and edge label, and the mean degree is returned.

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

## Sample   `.degreeDistribution`   output
<a name="degreeDistribution-sample-output"></a>

Here is an example of the output returned by .degreeDistribution when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

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