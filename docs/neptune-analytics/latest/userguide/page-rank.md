# PageRank centrality algorithm

PageRank is an algorithm originally developed by Larry Page and Sergey Brin,
co-founders of Google. It was originally developed to rank web pages in search engine
results. The PageRank score for a given node is calculated based on the number and
quality of the edges pointing to that node, as well as the importance of the nodes
that are connected to it. The PageRank algorithm assigns a higher score to nodes
that are linked to other high-scoring nodes, and a lower score to nodes that
are linked to low-scoring nodes.

The output of PageRank can be visualized as a ranking metric for the importance
of a node within a given graph, with the most important nodes having the highest
score, and the least important node having the lowest score. PageRank is used in
search engines to rank web pages based on their importance and influence,
in citation networks to identify highly cited scientific papers, and in
recommendation systems to suggest popular and relevant content to users.

The space complexity is O(|V|), where |V| is the number of vertices in the graph.

## Personalized PageRank

Personalized PageRank is a variation of the original PageRank algorithm. It is generally used to measure the
importance of vertices in a graph. It tailors the ranking process to individual users or specific topics. Compared
to PageRank, the result of personalized pagerank is a more customized ranking of web pages or nodes in a graph,
reflecting individual interests or specific areas of focus. This approach is particularly useful in recommendation
systems, personalized search results, and analyzing large-scale networks with diverse content for a specific focus.

### Example scenario: Online retail platform

Imagine an online retail platform where each product is a node, and customer purchases (or views) between products
are edges.

###### Regular PageRank

- Objective: Rank products based on their general popularity across all customers.
- Result: Products that are frequently purchased or viewed by many customers will receive higher PageRank scores.
  This helps identify the most popular products across the entire platform.

###### Personalized PageRank

- Objective: Rank products based on their relevance to a specific customer's shopping behavior.
- Inputs:
  - Source Nodes: A list of products that the customer has previously purchased or shown interest in.
  - Source Weights: Optional weights indicating the relative importance of each source product
    (e.g., higher weight for recently purchased items).

- Result: Products that are not only popular but also closely related to the customer's specific
  shopping behavior will receive higher scores. This helps the platform recommend new products that
  are more likely to interest the customer.

### Example scenario: Organizational network security

Imagine a network of computers within an organization where each computer is a node, and communication
paths (like data transfers or network connections) between computers are edges.

###### Regular PageRank

- Objective: Rank computers based on their general importance within the organizational network.
- Result: Computers that have a high number of connections to other computers will receive higher PageRank
  scores. This helps identify critical nodes in the network that, if compromised, could have a significant
  impact on the entire network.

###### Personalized PageRank

- Objective: Rank computers based on their relevance to a specific security concern or department within the
  organization.
- Inputs:
  - Source Nodes: A list of computers that are known to handle sensitive data or are critical to a specific
    department (e.g., HR, Finance).
  - Source Weights: Optional weights indicating the relative importance of each source computer (e.g., higher
    weight for computers handling more sensitive data).

- Result: Computers that are not only well-connected but also closely related to the specific security concern or
  department will receive higher scores. This helps the cybersecurity team prioritize monitoring and protection
  efforts on the most critical nodes.

### Example scenario: Insurance policyholder network

Imagine a network of policyholders where each policyholder is a node, and the relationships (like shared
claims, referrals, or common risk factors) between policyholders are edges.

###### Regular PageRank

- Objective: Rank policyholders based on their general importance within the insurance network.
- Result: Policyholders who have a high number of connections to other policyholders (e.g., through
  shared claims or referrals) will receive higher PageRank scores. This helps identify influential
  policyholders who may have a significant impact on the network.

###### Personalized PageRank

- Objective: Rank policyholders based on their relevance to a specific risk profile or insurance product.
- Inputs:
  - Source Nodes: A list of policyholders that fit a specific risk profile or are relevant to a particular
    insurance product (e.g., high-risk drivers for auto insurance).
  - Source Weights: Optional weights indicating the relative importance of each source policyholder (e.g.,
    higher weight for policyholders with more recent claims).

- Result: Policyholders who are not only well-connected but also closely related to the specific risk profile
  or insurance product will receive higher scores. This helps the insurance company tailor its risk assessment
  and underwriting processes more effectively.

The additional inputs to the algorithm are a list of vertices to be personalized on (`sourceNodes`) and optionally
the weight distribution among those vertices (`sourceWeights`). If given, the weights are normalized before pagerank
computation.

###### Note

Neptune Analytics allows up 8192 vertices in the personalization vector, sourceNodes.

## `.pageRank`  syntax

```
CALL neptune.algo.pageRank(
  [`node list (required)`],
  {
    numOfIterations: `a small positive integer like 20 (optional)`,
    dampingFactor: `a positive float less than or equal to 1.0, like 0.85 (optional)`
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    concurrency: `number of threads to use (optional)`,
    traversalDirection: `the direction of edge to follow (optional)`,
    tolerance: `a floating point number between 0.0 and 1.0 (inclusive)(optional)`,
    edgeWeightProperty: `the weight property to consider for weighted pageRank computation (optional)`,
    edgeWeightType: `The type of values associated with the edgeWeightProperty argument (optional)`,
    sourceNodes: [`A list of node IDs to personalize on (optional)`],
    sourceWeights: [`A list of non-negative weights for the sourceNodes (optional)`]
  }
)
YIELD node, rank
RETURN node, rank
```

## `.pageRank`  inputs

- **a node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes for which to return the page rank values. If an empty list is provided, the query result
will also be empty.

If the algorithm is called following a `MATCH` clause (query
integration), the result returned by the `MATCH` clause is taken as the node list.

- ###### a configuration object that contains:
  - **numOfIterations** _(optional)_   –  
    _type:_ a positive integer greater than zero;   _default: 20_.

  The number of iterations to perform to reach convergence. A number between 10 and 20 is recommended.
  - **dampingFactor** _(optional)_   –  
    _type:_ a positive floating-point number less than or equal to `1.0`;   _default:_ `0.85`.

  A positive floating-point damping factor between 0.0 and 1.0 that expresses the
  probability, at any step, that the node will continue.
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A vertex label for vertex filtering. If a vertex label is provided, vertices matching the label
  are the only vertices that are included, including vertices in the input list.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default:_ `"outbound"`.

  The direction of edge to follow. Must be one of: `"outbound"` or `"inbound"`.
  - **tolerance** _(optional)_   –  
    a floating point number between 0.0 and 1.0 (inclusive). When the average difference in the pageRank values of
    two iterations drops below `tolerance`, the algorithm stops, regardless of whether the
    `numOfIterations` is reached. Default value is `0.000001 (1e-6)`.
    - Note that this tolerance computation is equivalent to L1 error or sum of Mean Absolute Difference (MAE)s.
    - The stopping condition is `l1_error_sum < tolerance * numNodes`, equivalent to
      `l1_error_sum/numNodes < tolerance`.

  - **edgeWeightProperty** _(optional)_   –  
    _type:_ `string`   _default: none_.

  The weight property to consider for weighted pageRank computation.
  - **edgeWeightType** _(optional) - required if
    `edgeWeightProperty` is present_   –  
    _type:_ `string`;   _default: none_.

  The type of values associated with the edgeWeightProperty argument, specified as a string.
  _valid values_: "int", "long", "float", "double".

      - If the edgeWeightProperty is not given, the algorithm runs unweighted no matter if the edgeWeightType
       is given or not.
      - Note that if multiple properties exist on the edge with the name specified by edgeWeightProperty, one
       of those property values will be sampled at random.

  - **sourceNodes** _(optional) - required if
    running personalized PageReank_   –  
    _type:_ `list`;   _default: none_.

  A personalization vertex list ["101", ...]

      - Can include 1 to 8192 vertices.
      - If a `vertexLabel` is provided, nodes that do not have the given `vertexLabel`
       are ignored.

  - **sourceWeights** _(optional)_   –  
    _type:_ `list`;   _default: none_.

  A personalization weight list. The weight distribution among the personalized vertices.

      - If not provided, the default behavior is uniform distribution among the vertices given in
       `sourceNodes`.
      - There must be at least one non-zero weight in the list.
      - The length of the sourceWeights list must match the `sourceNodes` list.
      - The mapping of personalization vertex and weight lists are one to one. The first value in the weight list
       corresponds to the weight of first vertex in the vertex list, second value is for the second vertex, etc.
      - The weights can be one of `int`, `long`, `float`, or `double`
       types.

## Outputs for the `.pageRank` algorithm

- **node**   –  
  A key column of the input nodes.
- **rank**   –  
  A key column of the corresponding page-rank scores for those nodes.

If the input nodes list is empty, the output is empty.

## Query examples for `.pageRank`

This is a standalone example, where the input vertex list is explicitly specified
in the query.

```
CALL neptune.algo.pageRank(
  ["101"],
  {
    numOfIterations: 1,
    dampingFactor: 0.85,
    edgeLabels: ["route"]
  }
)
```

This is a query integration examples, where `.pageRank` follows a
`MATCH` clause and uses frontier injection to take the output of the
`MATCH` clause as its list of input nodes:

```
MATCH (n)
CALL neptune.algo.pageRank(
  n,
  {
    dampingFactor: 0.85,
    numOfIterations: 1,
    edgeLabels: ["route"]
  }
)
YIELD rank
RETURN n, rank
```

This query is an example of constraining the results of `.pageRank` based
on the PageRank values, and returning them in ascending order:

```
MATCH (n)
CALL neptune.algo.pageRank(
  n,
  {
    numOfIterations: 10,
    dampingFactor: 0.85,
    tolerance: 0.0001,
    vertexLabel: "airport",
    edgeLabels: ["route"]
  }
)
YIELD rank WHERE rank > 0.004
RETURN n, rank ORDER BY rank
```

## Query examples for Personalized `.pageRank`

Personalized PageRank applies the same integration and constraints. Here are some examples that pass
personalization-specific configurations.

This is a query integration example, where .pageRank follows a MATCH clause and uses frontier injection
to take the output of the MATCH clause as its input list. We use nodes “101” and “102” as personalization
nodes with "1" and "1.5" weights as weights respectively:

```
MATCH (n)
CALL neptune.algo.pageRank( n, {
    tolerance: 0.001,
    edgeLabels:["route”],
    sourceNodes:["101", "102"],
    sourceWeights:[1, 1.5]
} )
YIELD node, rank
RETURN node, rank
```

This is an example of where only source nodes is provided. The weights of ”101” and ”102” will be "1" and "1"
(same, uniform) respectively.

```
MATCH (n)
CALL neptune.algo.pageRank( n, {
    tolerance: 0.001,
    edgeLabels:["route”],
    sourceNodes:["101", "102"],
} )
YIELD node, rank
RETURN node, rank
```

This is an example where the weights are given as integral numbers. Note that this would yield the same result
as the first example in which the weights were ("1" and "1.5"):

```
MATCH(n)
CALL neptune.algo.pageRank( n, {
    tolerance: 0.001,
    edgeLabels:["route”],
    sourceNodes:["101", "102"],
    sourceWeights:[2, 3]
} )
YIELD node, rank
RETURN node, rank
```

## Sample   `.pageRank`   output

Here is an example of the output returned by .pageRank when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.pageRank(n) YIELD node, rank RETURN node, rank LIMIT" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "node": {
        "~id": "2709",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 65.4809036254883,
          "elev": 49,
          "longest": 8711,
          "city": "Nadym",
          "type": "airport",
          "region": "RU-YAN",
          "desc": "Nadym Airport",
          "code": "NYM",
          "lon": 72.6988983154297,
          "country": "RU",
          "icao": "USMM",
          "runways": 1
        }
      },
      "rank": 0.00016044313088059425
    },
    {
      "node": {
        "~id": "3747",
        "~entityType": "node",
        "~labels": ["continent"],
        "~properties": {
          "code": "AN",
          "type": "continent",
          "desc": "Antarctica"
        }
      },
      "rank": 0.0000404242
    }
  ]
}
```
