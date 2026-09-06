

# Overlap similarity algorithm
<a name="overlap-similarity"></a>

Overlap Similarity is an algorithm that measures the overlap between the neighbors of two nodes. It does this by dividing the intersection of the two neighborhoods by the neighbor with minimum degree.

By calculating the ratio of common neighbors shared by two nodes to the total number of neighbors they collectively have, it provides a measure of their closeness or similarity within the network. Overlap similarity is applied in social network analysis to identify communities of individuals with shared interests or interactions, and in biological networks to detect common functionalities among proteins in molecular pathways.

## `.overlapSimilarity`  syntax
<a name="overlap-similarity-syntax"></a>

```
CALL neptune.algo.overlapSimilarity(
  [{{first node(s)}}],
  [{{second node(s)}}],
  {
    edgeLabels: [{{a list of edge labels for filtering (optional)}}],
    vertexLabel: {{a node label for filtering (optional)}},
    traversalDirection: {{traversal direction (optional)}}
  }
)
YIELD score
RETURN {{firstNodes}}, {{secondNodes}}, score
```

## `.overlapSimilarity`  inputs
<a name="overlap-similarity-inputs"></a>
+ **first node(s)** *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  One or more nodes for which to find the overlap similarity score with respect to the corresponding second node(s).
+ **second node(s)** *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  One or more nodes for which to find the overlap similarity score with respect to the corresponding first node(s).
+ 

**a configuration object that contains:**
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **vertexLabel** *(optional)*   –   *type:* `string`;   *default: none*.

    A node label for node filtering. If a node label is provided, nodes matching the label are the only nodes that are considered neighbors. This does not filter the nodes in the first or second node lists.
  + **traversalDirection** *(optional)*   –   *type:* `string`;   *default: outbound*.

     The direction of edge to follow. Must be one of: "inbound", "outbound", or "both". 

## `.overlapSimilarity`  outputs
<a name="overlap-similarity-outputs"></a>

**score**: A row for each node in the first node list and corresponding node in the second node list, and the overlap similarity score for the two.

If either input node list is empty, the output is empty.

## `.overlapSimilarity`  query examples
<a name="overlap-similarity-query-examples"></a>

This is a query integration example, where `.overlapSimilarity` takes its input node lists from the output of a `MATCH` clause:

```
MATCH (n1:Person {name: "Alice"}), (n2:Person {name: "Bob"})
CALL neptune.algo.overlapSimilarity(n1, n2, {edgeLabel: 'knows'})
YIELD score
RETURN n1, n2, score
```

Another example:

```
MATCH (n {code: "AUS"})
MATCH (m {code: "FLL"})
CALL neptune.algo.overlapSimilarity(
  n,
  m,
  {
    edgeLabels: ["route"],
    vertexLabel: "airport"
  }
)
YIELD score
RETURN n, m, score'
```

**Warning**  
It is not good practice to use `MATCH(n)` without restriction in query integrations. Keep in mind that every node returned by the `MATCH(n)` clause invokes the algorithm once, which can result in a very long-running query if a large number of nodes is returned. Use `LIMIT` or put conditions on the `MATCH` clause to restrict its output appropriately.

## Sample   `.overlapSimilarity`   output
<a name="overlap-similarity-sample-output"></a>

Here is an example of the output returned by .overlapSimilarity when run against the [ sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string 'MATCH (n {code: "AUS"})
                       MATCH (m {code: "FLL"})
                       CALL neptune.algo.overlapSimilarity(
                         n,
                         m,
                         {
                           edgeLabels: ["route"],
                           vertexLabel: "airport"
                         }
                       )
                       YIELD score
                       RETURN n, m, score' \
  --language open_cypher \
  /tmp/out.txt
  
cat /tmp/out.txt
{
  "results": [
    {
      "n": {
        "~id": "3",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 30.1944999694824,
          "elev": 542,
          "type": "airport",
          "code": "AUS",
          "lon": -97.6698989868164,
          "runways": 2,
          "longest": 12250,
          "communityId": 2357352929951971,
          "city": "Austin",
          "region": "US-TX",
          "desc": "Austin Bergstrom International Airport",
          "prscore": 0.0012390684569254518,
          "degree": 188,
          "wccid": 2357352929951779,
          "ccscore": 0.1833982616662979,
          "country": "US",
          "icao": "KAUS"
        }
      },
      "m": {
        "~id": "9",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 26.0725994110107,
          "elev": 64,
          "type": "airport",
          "code": "FLL",
          "lon": -80.152702331543,
          "runways": 2,
          "longest": 9000,
          "communityId": 2357352929951971,
          "city": "Fort Lauderdale",
          "region": "US-FL",
          "desc": "Fort Lauderdale/Hollywood International Airport",
          "prscore": 0.0024497462436556818,
          "degree": 316,
          "wccid": 2357352929951779,
          "ccscore": 0.19741515815258027,
          "country": "US",
          "icao": "KFLL"
        }
      },
      "score": 0.6129032373428345
    }
  ]
}
```