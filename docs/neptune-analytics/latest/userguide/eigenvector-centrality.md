

# Eigenvector centrality algorithm
<a name="eigenvector-centrality"></a>

Eigenvector centrality is a centrality algorithm that measures a node's importance by accounting for both the number and the importance of the nodes connected to it. Nodes that are connected to many highly connected nodes receive higher scores. This makes eigenvector centrality useful for identifying nodes that are well-connected within influential parts of a network.

You can use eigenvector centrality in social network analysis to identify key influencers, in citation networks to find seminal papers referenced by other highly cited works, and in transportation networks to locate hubs that connect to other major hubs. 

Eigenvector centrality is closely related to [PageRank](page-rank.md) and works on a similar principle, but there is a key difference. PageRank includes a random jump factor that handles the issue with vertices that have no outgoing connections, while eigenvector centrality measures raw connectivity influence without that adjustment. Compared to PageRank, eigenvector centrality can be thought of as a simpler, more direct measure of influence. Eigenvector centrality also supports a personalized variant that biases the computation toward a specified set of source nodes, just as done in PageRank.

The time complexity is O(k\*\|E\|), where k is the number of iterations to converge and \|E\| is the number of edges. The space complexity is O(\|V\|), where \|V\| is the number of vertices.

**Note**  
 Neptune Analytics allows up to 8192 vertices in the personalization vector, sourceNodes. 

## `.eigenvectorCentrality` syntax
<a name="eigenvector-centrality-syntax"></a>

```
CALL neptune.algo.eigenvectorCentrality(
  [{{node list (required)}}],
  {
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
YIELD node, score
RETURN node, score
```

## `.eigenvectorCentrality` inputs
<a name="eigenvector-centrality-inputs"></a>
+ **a node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  The node or nodes for which to return the eigenvector centrality score. If you provide an empty list, the query result is also empty.

  If the algorithm is called following a `MATCH` clause (query integration), the result returned by the `MATCH` clause is taken as the node list.
+ 

**a configuration object that contains:**
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
    + If you do not provide `edgeWeightProperty`, the algorithm runs unweighted. You can only supply `edgeWeightType` together with ` edgeWeightProperty`.
  + **sourceNodes**   *(optional, required if running personalized eigenvector centrality)*   –   *type:* `list`;   *default: none*.

    A personalization vertex list ["101", ...].
    + Can include 1 to 8192 vertices.
    + If you provide `vertexLabels`, the algorithm ignores nodes that do not have the given vertex label.
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

## `.eigenvectorCentrality` outputs
<a name="eigenvector-centrality-outputs"></a>
+ **node**   –   The input node.
+ **score**   –   The eigenvector centrality score for that node.

If the input nodes list is empty, the output is empty.

## `.eigenvectorCentrality` query examples
<a name="eigenvector-centrality-examples"></a>

This is a standalone example, where the input vertex list is explicitly provided in the query:

```
CALL neptune.algo.eigenvectorCentrality(
  ["101"],
  {
    numOfIterations: 10,
    edgeLabels: ["route"],
    vertexLabels: ["airport"],
    traversalDirection: "outbound",
    concurrency: 0
  }
)
YIELD node, score
RETURN node, score
```

This is a query integration example, where `.eigenvectorCentrality` follows a `MATCH` clause:

```
MATCH (n)
CALL neptune.algo.eigenvectorCentrality(
  n,
  {
    numOfIterations: 10,
    edgeLabels: ["route"],
    vertexLabels: ["airport"],
    traversalDirection: "outbound",
    concurrency: 0
  }
)
YIELD score
RETURN n, score
ORDER BY score DESC
LIMIT 2
```

## Personalized `.eigenvectorCentrality`
<a name="personalized-eigenvector-centrality"></a>

Personalized eigenvector centrality is a variation that biases the computation toward a specified set of source nodes. Instead of measuring global importance across the entire graph, it ranks nodes based on their importance relative to the source nodes you specify. This is conceptually similar to [Personalized PageRank](page-rank.md#personalized-page-rank), which also biases toward source nodes.

The key difference involves teleportation. Personalized PageRank uses a damping factor that periodically teleports the random walker back to the source nodes. This produces a more diffuse ranking across the graph. Personalized eigenvector centrality has no such teleportation mechanism. Influence propagates purely through connectivity, so scores concentrate more heavily on the dominant structure near the sources. This is useful when you want to identify the structurally dominant nodes near a particular user, location, or set of entities. It avoids a broad ranking that diffuses across the entire reachable graph, as Personalized PageRank would produce.

For example, in a social network you could use personalized eigenvector centrality to find the most influential people from the perspective of a specific user, by setting that user as the source node. In a transportation network, you could identify the most important hubs relative to a specific airport or set of airports.

To run personalized eigenvector centrality, provide the `sourceNodes` parameter with a list of node IDs. You can optionally provide `sourceWeights` to control how much each source node influences the result. If no weights are provided, all source nodes are weighted equally.

### Personalized query example
<a name="personalized-eigenvector-centrality-example"></a>

This example computes eigenvector centrality scores biased toward airports `"101"` and `"103"`, with `"101"` weighted more heavily:

```
CALL neptune.algo.eigenvectorCentrality(
  ["101", "102", "103", "104", "105"],
  {
    sourceNodes: ["101", "103"],
    sourceWeights: [7, 3],
    numOfIterations: 10,
    edgeLabels: ["route"],
    concurrency: 0
  }
)
YIELD node, score
RETURN node, score
ORDER BY score DESC
```

## Sample `.eigenvectorCentrality` output
<a name="eigenvector-centrality-sample-output"></a>

The following example shows the output that `.eigenvectorCentrality` returns when you run it against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), using the following query:

```
aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string "MATCH(n) CALL neptune.algo.eigenvectorCentrality(n) YIELD node, score RETURN node, score LIMIT 2" \
    --language open_cypher \
    /tmp/out.txt

cat /tmp/out.txt
{
  "results": [{
      "node": {
        "~id": "1823",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "icao": "CEM3",
          "type": "airport",
          "city": "Whatì",
          "lon": -117.24600219726599,
          "region": "CA-NT",
          "lat": 63.131698608398402,
          "code": "YLE",
          "longest": 2991,
          "country": "CA",
          "runways": 1,
          "desc": "Whatì Airport",
          "elev": 882
        }
      },
      "score": 1.28392E-05
    }, {
      "node": {
        "~id": "2840",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "icao": "VYMK",
          "type": "airport",
          "city": "Myitkyina",
          "lon": 97.351898193359403,
          "region": "MM-11",
          "lat": 25.383600234985401,
          "code": "MYT",
          "longest": 6100,
          "country": "MM",
          "runways": 1,
          "desc": "Myitkyina Airport",
          "elev": 475
        }
      },
      "score": 0.0001856196
    }]
}
```