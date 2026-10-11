

# Leiden algorithm
<a name="leiden"></a>

 The Leiden algorithm is an improvement over the [Louvain algorithm](louvain.md) that guarantees well-connected communities. It adds a refinement phase before each aggregation step. This avoids Louvain's known shortcoming of producing arbitrarily badly connected or disconnected clusters. Like Louvain, it optimizes modularity through hierarchical clustering and can run in both weighted and unweighted modes. Leiden is particularly suited for applications where community cohesion matters. Use cases include detecting tightly-knit fraud rings in financial networks, identifying functionally coherent modules in biological systems, and discovering well-connected user groups in social platforms. 

 The key improvement in Leiden is a refinement phase that occurs before each aggregation step. After the algorithm identifies candidate communities, the refinement phase processes each community from the bottom up. It merges nodes in a way that guarantees the resulting communities remain connected. This addresses a known shortcoming of Louvain, which can produce arbitrarily badly connected or even disconnected communities. 

 The algorithm can run in unweighted or weighted mode based on the graph and user inputs. When an edge weight property is specified, the algorithm runs in weighted mode. 

 Here are several real-world applications of the Leiden algorithm for community detection: 
+  Fraud detection in financial transactions 
+  Cybersecurity threat analysis 
+  Identifying influencer communities on social networks 
+  Biological network analysis (for example, protein-protein interaction networks) 

 The Leiden algorithm is particularly useful in these cases because it: 
+  Guarantees well-connected communities 
+  Produces higher-quality partitions than Louvain 
+  Handles large-scale networks efficiently 
+  Works well with weighted networks 
+  Can detect hierarchical community structures 

**Note**  
 There can only be one Leiden or Louvain algorithm call running at a time. 
 Leiden is expected to run a long time. Set the query timeout to a large number to avoid query timeout. See [ query-timeout-milliseconds](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-execute-query.html#query-APIs-execute-query-input) for more information on setting upper bounds on query run time. 

## `.leiden` syntax
<a name="leiden-syntax"></a>

```
CALL neptune.algo.leiden(
  [{{node list (required)}}],
  {
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
YIELD node, community
RETURN node, community
```

## `.leiden` inputs
<a name="leiden-inputs"></a>
+ **a node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

   The node or nodes for which the algorithm will return the computed community ids. If the algorithm is called following a MATCH clause, the MATCH clause returns the node query list. 
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

## `.leiden` outputs
<a name="leiden-outputs"></a>

For each source node:
+ **node**   –   A column of the input nodes.
+ **community**   –   A column of the corresponding communityId values for those nodes. All the nodes with the same communityId are in the same community.

If the input node list is empty, the output is also empty.

## `.leiden` query examples
<a name="leiden-examples"></a>

 The following example runs the Leiden algorithm in unweighted mode: 

```
CALL neptune.algo.leiden(
  ["101"],
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    theta: 0.05
  }
)
YIELD node, community
RETURN node, community
```

 The following example runs the Leiden algorithm in weighted mode using edge weights: 

 Sample use case: you may want to identify natural communities of stops where there is high intra-connectivity — essentially, clusters of stops that are strongly interconnected based on passenger traffic 

```
CALL neptune.algo.leiden(
  ["101"],
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int",
    theta: 0.5
  }
)
YIELD node, community
RETURN node, community
```

 This is a query integration example, where `.leiden` uses the output of a preceding `MATCH` clause as its node list: 

```
MATCH (n)
CALL neptune.algo.leiden(
  n,
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 1,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int",
    theta: 0.01
  }
)
YIELD community
RETURN n, community
```

**Warning**  
 The Leiden algorithm requires exclusive processing. Neptune will process only one Leiden or Louvain algorithm execution at a time. Any subsequent algorithm requests submitted before the completion of an active process will result in an error response. 

## Sample `.leiden` output
<a name="leiden-sample-output"></a>

Here is an example of the output returned by .leiden when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string 'MATCH (n) \
            CALL neptune.algo.leiden(n) \
            YIELD node, community \
            RETURN node, community \
            LIMIT 2' \
    --language open_cypher \
    /tmp/out.txt
cat /tmp/out.txt
{
"results": [{
 "node": {
   "~id": "10",
   "~entityType": "node",
   "~labels": ["airport"],
   "~properties": {
     "lat": 38.944499970000003,
     "elev": 313,
     "type": "airport",
     "code": "IAD",
     "lon": -77.455802919999996,
     "runways": 4,
     "longest": 11500,
     "city": "Washington D.C.",
     "region": "US-VA",
     "desc": "Washington Dulles International Airport",
     "degree": 312,
     "country": "US",
     "icao": "KIAD"
   }
 },
 "community": 1
 }, {
 "node": {
   "~id": "12",
   "~entityType": "node",
   "~labels": ["airport"],
   "~properties": {
     "lat": 40.639801030000001,
     "elev": 12,
     "type": "airport",
     "code": "JFK",
     "lon": -73.778900149999998,
     "runways": 4,
     "longest": 14511,
     "city": "New York",
     "region": "US-NY",
     "desc": "New York John F. Kennedy International Airport",
     "degree": 403,
     "country": "US",
     "icao": "KJFK"
   }
 },
 "community": 1
 }]
}
```