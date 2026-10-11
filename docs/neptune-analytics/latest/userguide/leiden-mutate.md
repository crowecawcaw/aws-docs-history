

# Leiden mutate algorithm
<a name="leiden-mutate"></a>

 The [Leiden algorithm](leiden.md) is an improvement over the [Louvain algorithm](louvain.md) that guarantees well-connected communities. 

 `.leiden.mutate` is a variant of the Leiden algorithm that writes the derived community ID to a new property on each node. 

**Note**  
 There can only be one Leiden or Louvain algorithm call running at a time. 
 Leiden is expected to run a long time. Set the query timeout to a large number to avoid query timeout. See [ query-timeout-milliseconds](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-execute-query.html#query-APIs-execute-query-input) for more information on setting upper bounds on query run time. 

## `.leiden.mutate` syntax
<a name="leiden-mutate-syntax"></a>

```
CALL neptune.algo.leiden.mutate(
  {
    writeProperty: {{property name to store community IDs (required)}},
    vertexLabels: [{{list of vertex labels for filtering (optional)}}],
    edgeLabels: [{{list of edge labels for filtering (optional)}}],
    edgeWeightProperty: {{a numeric edge property to use as weight (optional)}},
    edgeWeightType: {{numeric type of the specified edgeWeightProperty (optional)}},
    maxLevels: {{maximum number of levels to optimize at (optional, default: 10)}},
    maxIterations: {{maximum number of iterations per level (optional, default: 10)}},
    levelTolerance: {{minimum modularity change to continue to next level (optional, default: 0.01)}},
    iterationTolerance: {{minimum modularity change to continue to next iteration (optional, default: 0.0001)}},
    theta: {{temperature parameter for refinement phase (optional, default: 0.05)}},
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD success
RETURN success
```

## `.leiden.mutate` inputs
<a name="leiden-mutate-inputs"></a>

The `.leiden.mutate` algorithm accepts a configuration object that contains:
+ **writeProperty**   *(required)*   –   *type:* `string`;   *default: none*.

  A name for the new node property that will contain the computed community ID of the nodes.
+ 

**a configuration object that contains:**
  + **vertexLabels**   *(optional)*   –   *type:* a list of vertex label strings;   *example:* `["airport", {{...}}]`;   *default:* no vertex filtering.

    To filter on one more vertex labels, provide a list of the ones to filter on. If no `vertexLabels` field is provided then all vertex labels are processed during traversal.
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **edgeWeightProperty**   *(optional)*   –   *type:* `string`;   *default: none*.

     A string indicating the name of the edge weight property used as weight in Leiden. When the edgeWeightProperty is not specified, each edge is treated equally (that is, the default value of the edge weight is 1). 

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
  + **theta**   *(optional)*   –   *type:* `float`;   *default: 0.05*.

     A temperature parameter that controls the randomness of the refinement phase. Lower values of theta make the selection more deterministic (closer to greedy selection), while higher values introduce more randomness. The parameter affects how candidate communities are selected during refinement. The value must be between 0 (exclusive) and 1 (inclusive). 
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## `.leiden.mutate` outputs
<a name="leiden-mutate-outputs"></a>

 The community IDs are written as a new node property using the property name specified by `writeProperty`. A single success flag (true or false) is returned to indicate whether the computation and writes succeeded or failed. 

## `.leiden.mutate` query examples
<a name="leiden-mutate-query-examples"></a>

 Unweighted: 

```
CALL neptune.algo.leiden.mutate(
  {
    writeProperty: "leidenCommId",
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    theta: 0.05
  }
)
YIELD success
RETURN success
```

 Weighted: 

```
CALL neptune.algo.leiden.mutate(
  {
    writeProperty: "leidenCommId",
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int",
    theta: 0.05
  }
)
YIELD success
RETURN success
```

After using the mutate algorithm, the newly written properties can then be accessed in subsequent queries:

```
MATCH (n) WHERE id(n) IN ["101", "102", "103"]
RETURN n.leidenCommId
```

## Sample `.leiden.mutate` output
<a name="leiden-mutate-sample-output"></a>

Here is an example of the output returned by .leiden.mutate when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string 'CALL neptune.algo.leiden.mutate({writeProperty: "leidenCommId"}) \
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