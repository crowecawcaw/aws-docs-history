# Common neighbors algorithm

Common neighbors is an algorithm that counts the number of common neighbors of two
input nodes, which is the intersection of their neighborhoods. This provides a measure
of their potential interaction or similarity within the network. The common neighbors
algorithm is used in social network analysis to identify individuals with mutual
connections, in citation networks to find influential papers referenced by multiple
sources, and in transportation networks to locate critical hubs with many direct
connections to other nodes.

## `.neighbors.common`  syntax

```
CALL neptune.algo.neighbors.common(
  [`first node(s)`],
  [`second node(s)`],
  {
    edgeLabels: [`a list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    traversalDirection: `traversal direction (optional)`
  }
)
YIELD common
RETURN `firstNodes`, `secondNodes`, common
```

## `.neighbors.common`  inputs

- **first node(s)** _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

One or more nodes of which to find the common neighbors with the corresponding second node(s).

- **second node(s)** _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

One or more nodes of which to find the common neighbors with the corresponding first node(s).

- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel** _(optional)_   –  
    _type:_ `string`;   _default: none_.

  A node label for node filtering. If a node label is provided, nodes matching the label
  are the only nodes that are considered neighbors. This does not filter the nodes in the first
  or second node lists.
  - **traversalDirection** _(optional)_   –  
    _type:_ `string`;   _default: outbound_.

  The direction of edge to follow. Must be one of: "inbound", "outbound", or "both".

## `.neighbors.common`  outputs

**common**: A row for each node in the first node list and
corresponding node in the second node list, and the number of neighboring nodes they have in
common.

If either input node list is empty, the output is empty.

## `.neighbors.common`  query examples

This example specifies only two nodes:

```
MATCH (sydairport:airport {code: 'SYD'})
MATCH (jfkairport:airport {code: 'JFK'})
CALL neptune.algo.neighbors.common( sydairport, jfkairport, { edgeLabels: ['route'] })
YIELD common
RETURN sydairport, jfkairport, common
```

This example specifies multiple nodes. It returns a row for each combination
of a US airport and a UK airport, and the number of destinations we could reach
from both of those two airports:

```
MATCH (usairports:airport {country: 'US'})
MATCH (ukairports:airport {country: 'UK'})
CALL neptune.algo.neighbors.common(usairports, ukairports, {edgeLabels: ['route']})
YIELD common
RETURN usairports, ukairports, common
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample   `.neighbors.common`   output

Here is an example of the output returned by .neighbors.common when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (sydairport:airport {code: 'SYD'})
                       MATCH (jfkairport:airport {code: 'JFK'})
                       CALL neptune.algo.neighbors.common(sydairport, jfkairport, {edgeLabels: ['route']})
                       YIELD common
                       RETURN sydairport, jfkairport, common" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "sydairport": {
        "~id": "55",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": -33.9460983276367,
          "elev": 21,
          "type": "airport",
          "code": "SYD",
          "lon": 151.177001953125,
          "runways": 3,
          "longest": 12999,
          "communityId": 2357352929951971,
          "city": "Sydney",
          "region": "AU-NSW",
          "desc": "Sydney Kingsford Smith",
          "prscore": 0.0028037719894200565,
          "degree": 206,
          "wccid": 2357352929951779,
          "ccscore": 0.19631840288639069,
          "country": "AU",
          "icao": "YSSY"
        }
      },
      "jfkairport": {
        "~id": "12",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 40.63980103,
          "elev": 12,
          "type": "airport",
          "code": "JFK",
          "lon": -73.77890015,
          "runways": 4,
          "longest": 14511,
          "communityId": 2357352929951971,
          "city": "New York",
          "region": "US-NY",
          "desc": "New York John F. Kennedy International Airport",
          "prscore": 0.002885053399950266,
          "degree": 403,
          "wccid": 2357352929951779,
          "ccscore": 0.2199712097644806,
          "country": "US",
          "icao": "KJFK"
        }
      },
      "common": 24
    }
  ]
}
```
