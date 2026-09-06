

# Louvain algorithm
<a name="louvain"></a>

 The Louvain algorithm is a hierarchical clustering method for detecting community structures within networks. A community is defined as a subset of nodes with dense internal connections relative to sparse external connections. The algorithm iteratively optimizes modularity, which mathematically measures the strength of network division into communities by comparing the density of connections within communities to what would be expected in a random network with the same degree distribution. 

 Through a two-phase process of local optimization and network aggregation, the algorithm identifies hierarchical community structures that maximize this modularity measure. This method is particularly valuable in network science for decomposing complex networks into their natural organizational units, with applications ranging from social network analysis to biological systems. 

 The algorithm can run in unweighted or weighted mode based on the graph and user inputs. When an edge weight property is specified, the algorithm runs in weighted mode. 

 Here are several real-world applications of the Louvain algorithm for community detection: 
+  Fraud detection in financial transactions 
+  Cybersecurity threat analysis 
+  Identifying influencer communities on social networks 
+  Planning network coverage areas 
+  Protein-protein interaction networks 

 The Louvain algorithm is particularly useful in these cases because it: 
+  Handles large-scale networks efficiently 
+  Provides good quality results 
+  Works well with weighted networks 
+  Is computationally fast 
+  Can detect hierarchical community structures 

**Note**  
 There can only be one Louvain algorithm call running at a time. 
 Louvain is expected to run a long time, hence please set the query timeout to be a large number to avoid query timeout. See [ query-timeout-milliseconds](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-APIs-execute-query.html#query-APIs-execute-query-input) for more information on setting upper bounds on query run time. 

## `.louvain`  syntax
<a name="louvain-syntax"></a>

```
CALL neptune.algo.louvain(
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
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD node, community
RETURN node, community
```

## `.louvain`  inputs
<a name="louvain-inputs"></a>
+ **a node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

   The node or nodes for which the algorithm will return the computed community ids. If the algorithm is called following a MATCH clause (query algo integration), the node query list is the result returned by the MATCH clause. 
+ 

**a configuration object that contains:**
  + **vertexLabels**   *(optional)*   –   *type:* a list of vertex label strings;   *example:* `["airport", {{...}}]`;   *default:* no vertex filtering.

    To filter on one more vertex labels, provide a list of the ones to filter on. If no `vertexLabels` field is provided then all vertex labels are processed during traversal.
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

## `.louvain`  outputs
<a name="louvain-outputs"></a>

For each source node:
+ **node**   –   A column of the input nodes.
+ **community**   –   A column of the corresponding communityId values for those nodes. All the nodes with the same communityId are in the same community.

If the input node list is empty, the output is also empty.

## `.louvain`  query examples
<a name="louvain-examples"></a>

 Unweighted example: 

```
CALL neptune.algo.louvain(
  ["101"],
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10
  }
)
YIELD node, community
RETURN node, community
```

 Weighted example: 

 Sample use case: you may want to identify natural communities of stops where there is high intra-connectivity — essentially, clusters of stops that are strongly interconnected based on passenger traffic 

```
CALL neptune.algo.louvain(
  ["101"],
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 3,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int"
  }
)
YIELD node, community
RETURN node, community
```

 This is a query integration example, where `.louvain` uses the output of a preceding `MATCH` clause as its node list: 

```
MATCH (n)
CALL neptune.algo.louvain(
  n,
  {
    vertexLabels: ["airport"],
    edgeLabels: ["route"],
    maxLevels: 1,
    maxIterations: 10,
    edgeWeightProperty: "weight",
    edgeWeightType: "int"
  }
)
YIELD community
RETURN n, community
```

**Warning**  
 The Louvain algorithm requires exclusive processing. Neptune will process only one Louvain algorithm execution at a time. Any subsequent algorithm requests submitted before the completion of an active process will result in an error response. 

## Sample `.louvain` output
<a name="louvain-mutate-sample-output"></a>

Here is an example of the output returned by .louvain when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string 'MATCH (n) \
            CALL neptune.algo.louvain(n) \
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
     "communityId": 2357352929951971,
     "city": "Washington D.C.",
     "region": "US-VA",
     "desc": "Washington Dulles International Airport",
     "degree": 312,
     "country": "US",
     "icao": "KIAD"
   }
 },
 "community": 2357352929951971
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
     "communityId": 2357352929951971,
     "city": "New York",
     "region": "US-NY",
     "desc": "New York John F. Kennedy International Airport",
     "degree": 403,
     "country": "US",
     "icao": "KJFK"
   }
 },
 "community": 2357352929951971
 }]
```