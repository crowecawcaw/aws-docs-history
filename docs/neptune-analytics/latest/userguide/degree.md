# Degree centrality algorithm

The `.degree` centrality algorithm counts the number of incident edges
at each node that it traverses. This measure of how connected the node is can
in turn indicate the node's importance and level of influence in the network.

The `.degree` algorithm is used in social networks to identify popular
individuals with many connections, in transportation networks to locate central hubs
with numerous roads leading to and from them, and in web analysis to find influential
web pages with many incoming links.

The time complexity of `.degree` is `O(|E|)`, where `|E|`
is the number of edges in the graph. The space complexity is `O(|V|)`, where
`|V|` is the number of vertices in the graph.

## `.degree`   syntax

```
CALL neptune.algo.degree(
  [`node list (required)`],
  {
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: "`a node label for filtering (optional)`",
    traversalDirection: `traversal direction (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD node, degree
RETURN node, degree
```

## Inputs for the `.degree` algorithm

- **a node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The node or nodes for which to return the edge count (degree). If an
empty list is provided, the query result is also empty.

If the algorithm is called following a `MATCH` clause (query
integration), the result returned by the `MATCH` clause is taken
as the node list.

- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A vertex label for vertex filtering. If a vertex label is provided, vertices matching the label are the only
  vertices that will be included in the calculation. Furthermore, vertices in the input that do not satisfy this
  constraint will not have results returned.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default:_ `"outbound"`.

  The direction of edge to follow. Must be one of: `"inbound"`,
  `"outbound"`, or `"both"`.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## `.degree`   outputs

- **node**   –  
  A list of the requested nodes. If `vertexLabel` is present, only
  the requested nodes that match the `vertexLabel` value are included.
- **degree**   –  
  A list of corresponding degree values for the nodes with respect to edges with
  a label specified in `edgeLabels`.

If the input vertex list is empty, the output is empty.

## Query examples for `.degree`

This is a standalone example, where the source node list is explicitly specified
in the query:

```
CALL neptune.algo.degree(["101"], {edgeLabel: "route"})
```

This is a more complicated standalone query submitted using the AWS CLI:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string 'CALL neptune.algo.degree(
        ["101", "102", "103"],
        {
          edgeLabels: ["route"],
          vertexLabel: "airport",
          traversalDirection: "inbound",
          concurrency: 2
        }
      )
      YIELD node, degree
      RETURN node, degree' \
  --language open_cypher \
  /tmp/out.txt
```

This is a query integration example with frontier injection, where
`.degree` follows a `MATCH` clause and finds the degree
value for all vertices returned by `MATCH(n:airport)`:

```
MATCH(n:airport)
CALL neptune.algo.degree(n, {edgeLabels: ["route"]})
YIELD degree
RETURN n, degree'
```

This is an example of multiple `.degree` invocations chained together,
where the output of one invocation serves as the input of another:

```
CALL neptune.algo.degree(
  ["108"],
  {
    edgeLabels: ["route"],
    vertexLabel: "airport"
  }
)
YIELD node
CALL neptune.algo.degree(
  node,
  {
    edgeLabels: ["route"],
    vertexLabel: "airport"
  }
)
YIELD node AS node2 WITH id(node2) AS id
RETURN id
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample   `.degree`   output

Here is an example of the output returned by .degree when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string 'MATCH (n)
      CALL neptune.algo.degree(n)
      YIELD node, degree
      RETURN node, degree
      LIMIT 2' \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "node": {
        "~id": "10",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 38.94449997,
          "elev": 313,
          "longest": 11500,
          "city": "Washington D.C.",
          "type": "airport",
          "region": "US-VA",
          "desc": "Washington Dulles International Airport",
          "code": "IAD",
          "prscore": 0.002264724113047123,
          "lon": -77.45580292,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KIAD",
          "runways": 4
        }
      },
      "degree": 312
    },
    {
      "node": {
        "~id": "12",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 40.63980103,
          "elev": 12,
          "longest": 14511,
          "city": "New York",
          "type": "airport",
          "region": "US-NY",
          "desc": "New York John F. Kennedy International Airport",
          "code": "JFK",
          "prscore": 0.002885053399950266,
          "lon": -73.77890015,
          "wccid": 2357352929951779,
          "country": "US",
          "icao": "KJFK",
          "runways": 4
        }
      },
      "degree": 403
    }
  ]
}
```
