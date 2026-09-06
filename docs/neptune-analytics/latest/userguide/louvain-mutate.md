

# Louvain mutate algorithm
<a name="louvain-mutate"></a>

 The [Louvain algorithm](louvain.md) is a hierarchical clustering method for detecting community structures within networks. 

 .louvain.mutate is a variant of the Louvain algorithm that writes the derived community component ID of each node in the node list to a new property of that node. 

**Note**  
 There can only be one Louvain algorithm call running at a time. 
 Louvain is expected to run a long time, hence please set the query timeout to be large number to avoid query timeout. See [ query-timeout-milliseconds](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-execute-query.html#query-APIs-execute-query-input) for more information on setting upper bounds on query run time. 

## `.louvain.mutate`  syntax
<a name="louvain-mutate-syntax"></a>

```
CALL neptune.algo.louvain.mutate(
  {
    writeProperty: {{property name to store community IDs (require)}},
    vertexLabels: [{{list of vertex labels for filtering (optional)}}],
    edgeLabels: [{{list of edge labels for filtering (optional)}}],
    edgeWeightProperty: {{a numeric edge property to use as weight (optional)}},
    edgeWeightType: {{numeric type of the specified edgeWeightProperty (optional)}},
    maxLevels: {{maximum number of levels to optimize at (optional, default: 10)}},
    maxIterations: {{maximum number of iterations per level (optional, default: 10)}},
    levelTolerance: {{minimum modularity change to continue to next level (optional, default: 0.01)}},
    iterationTolerance: {{minimum modularity change to continue to next iteration (optional, default: 0.0001)}},
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD success
RETURN success
```

## Inputs for the `.louvain.mutate` algorithm
<a name="louvain-mutate-inputs"></a>

Inputs for `.louvain.mutate` are passed in a configuration object that contains:
+ **writeProperty**   *(required)*   –   *type:* `string`;   *default: none*.

  A name for the new node property that will contain the computed community ID of the nodes.
+ 

**a configuration object that contains:**
  + **vertexLabels**   *(optional)*   –   *type:* `a list of vertex label strings; example ["airport", ...]`;   *default: no vertex filtering*.

     Node labels for node filtering. To filter on one or more vertex labels, provide a list of node labels. Vertices matching any label in the vertexLabels list are the only vertices that are passed to the algorithm computation. If no vertexLabels field is provided then all vertices are passed to the Louvain algorithm. 
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **edgeWeightProperty**   *(optional)*   –   *type:* `string`;   *default: none*.

     A string indicating the name of the edge weight property used as weight in Louvain. When the edgeWeightProperty is not specified, each edge is treated equally, i.e., the default value of the edge weight is 1. 

     Note that if multiple properties exist on the edge with the specified name, one of these values will be sampled at random. 
  + **edgeWeightType**   *(required if edgeWeightProperty is present)*   –   *type:* `string; valid values: "int", "long", "float", "double"`;   *default: none*.

     The type of the numeric values in the edge property specified by edgeWeightProperty. If the edgeWeightProperty is not given, the edgeWeightType is ignored even if it is specified. If an edge contains a property given by edgeWeightProperty, and its type is numeric but not matching the specified edgeWeightType, it will be typecast to the specified type. 
  + **maxLevels**   *(optional)*   –   *type:* `integer`;   *default: 10*.

     The maximum number of levels of granularity at which the algorithm optimizes the modularity. 
  + **maxIterations**   *(optional)*   –   *type:* `integer`;   *default: 10*.

     The maximum number of iterations to run at each level. 
  + **levelTolerance**   *(optional)*   –   *type:* `float`;   *default: .01*.

     The minimum change in modularity required to continue to the next level. 
  + **iterationTolerance**   *(optional)*   –   *type:* `float`;   *default: .0001*.

     The minimum change in modularity required to continue to the next iteration. 
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## Outputs for the `.louvain.mutate` algorithm
<a name="louvain-mutate-outputs"></a>

 The community IDs are written as a new node property using the property name specified by `writeProperty`. A single success flag (true or false) is returned to indicate whether the computation and writes succeeded or failed. 

## `.louvain.mutate`  query example
<a name="louvain-mutate-query-examples"></a>

 This is a standalone example, where the node list is explicitly provided in the query. It runs the algorithm over the whole graph, but only queries the community ID of one node: 

 Unweighted: 

```
CALL neptune.algo.louvain.mutate(
  {
    writeProperty: "louvainCommId",
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10
  }
)
YIELD success
RETURN success
```

 Weighted: 

```
CALL neptune.algo.louvain.mutate(
  {
    writeProperty: "louvainCommId",
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int"
  }
)
YIELD success
RETURN success
```

## Sample  `.louvain.mutate`  output
<a name="louvain-mutate-sample-output"></a>

Here is an example of the output returned by .louvain.mutate when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string 'query=CALL neptune.algo.louvain.mutate({writeProperty: 'communityId'}) \
            YIELD success RETURN success' \
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