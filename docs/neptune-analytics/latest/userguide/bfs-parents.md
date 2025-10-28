# Parents breadth-first search (BFS) algorithm

The `parents` variant of breadth-first search is an algorithm
for finding nodes from a starting node or vertices in breadth-first
order and then performing a breadth-first search for the parent of each node.

It returns a key column of vertices, and a value column of the vertices that are
the parents of the key vertices. The parent of a source node is itself.

###### Note

Because every source node passed in initiates its own execution of the algorithm,
your queries should limit the number of source nodes as much as possible.

## `.bfs.parents`   syntax

```
CALL neptune.algo.bfs.parents(
  [`source-node list (required)`],
  {
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    maxDepth: `maximum number of hops to traverse from a source node (optional)`,
    traversalDirection: `traversal direction (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD `the outputs to generate (source and/or node and/or parent)`
RETURN `the outputs to return`
```

## `.bfs.parents`   inputs

- **a source node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The source-node list contains the node or nodes used as the starting locations
for the algorithm.

    + Each starting node triggers its own execution of the algorithm.
    + If the source-node list is empty then the query result is also empty.
    + If the algorithm is called following a `MATCH` clause
     (this is known as query-algorithm integration), the output of the `MATCH` clause is
     used as the source-node list for the algorithm.

- ###### a configuration object that contains:
  - **edgeLabels**   _(optional)_   –  
    _type:_ a list of edge label strings;   _example:_
    `["route", `...`]`;   _default:_ no edge filtering.

  To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is
  provided then all edge labels are processed during traversal.
  - **vertexLabel**   _(optional)_   –  
    _type:_ `string`;   _example:_
    `"airport"`;  *default:* no node filtering.

  If you provide a node label to filter on then only vertices matching that label
  will be traversed. This does not, however, filter out any nodes in the source node list.
  - **maxDepth**   _(optional)_   –  
    _type:_ positive inteeger or 0 or -1;   _default:_ -1.

  The maximum number of hops to traverse from a source node. If set at `-1` then there's
  no maximum depth limit. If set to `0`, only the vertices in the source node list are returned.
  - **traversalDirection**   _(optional)_   –  
    _type:_ `string`;   _default:_ `outbound`.

  The direction of edge to follow. Must be one of: `inbound`,
  `outbound`, or `both`.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## `.bfs.parents`   outputs

The `.bfs.parents` algorithm returns:

- **source**   –  
  _type:_ `Node[]`.

The source nodes.

- **node**   –  
  _type:_ `Node[]`.

The vertices that the algorithm traversed from each source node.

- **parent**   –  
  _type:_ `Node[]`.

The parents of those traversed nodes.

## `.bfs.parents`   query examples

Thus is a standalone examples, where the source node list is explicitly provided in the query:

```
CALL neptune.algo.bfs.parents(
  ["105", "113"],
  {
    edgeLabels: ["route"],
    vertexLabel: "airport",
    maxDepth: 2,
    traversalDirection: "both",
    concurrency: 2
  }
)
YIELD node, parent
```

A query like this one would return an empty result because the source list is empty:

```
CALL neptune.algo.bfs.parents([], {edgeLabels: ["route"]})
```

This is a query integration example, where `.bfs.parents` follows a
`MATCH` clause that provides the source node list for `.bfs.parents`:

```
Match (n) with n LIMIT 5
CALL neptune.algo.bfs.parents(n, {edgeLabels: ["route"]})
YIELD node
RETURN n, node
```

This query is an example of aliasing the algorithm output:

```
MATCH (n {code: "AUS"})
CALL neptune.algo.bfs.parents(n, { edgeLabels: ["route"], maxDepth: 2})
YIELD node AS ReachedNode
RETURN ReachedNode
```

This query searches for routes to BFS from BKK, returning the starting node (BKK),
5 visited vertices, and their parents:

```
MATCH (n) where n.code CONTAINS "BKK"
CALL neptune.algo.bfs.parents(n, {edgeLabels: ["route"]})
YIELD node, parent
RETURN n, node, parent
LIMIT 5
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.bfs.parents` output

Here is an example of the output returned by .bfs.parents when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.bfs.parents(['101'], {maxDepth: 1})
                       YIELD source, node, parent
                       RETURN source, node, parent
                       LIMIT 2"
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [
    {
      "source": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "lon": 100.747001647949,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      },
      "node": {
        "~id": "1483",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 39.49,
          "elev": 4557,
          "longest": 9186,
          "city": "Ordos",
          "type": "airport",
          "region": "CN-15",
          "desc": "Ordos Ejin Horo Airport",
          "code": "DSN",
          "lon": 109.861388889,
          "country": "CN",
          "icao": "ZBDS",
          "runways": 1
        }
      },
      "parent": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "lon": 100.747001647949,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      }
    },
    {
      "source": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "lon": 100.747001647949,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      },
      "node": {
        "~id": "103",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 55.972599029541,
          "elev": 622,
          "longest": 12139,
          "city": "Moscow",
          "type": "airport",
          "region": "RU-MOS",
          "desc": "Moscow, Sheremetyevo International Airport",
          "code": "SVO",
          "lon": 37.4146003723145,
          "country": "RU",
          "icao": "UUEE",
          "runways": 2
        }
      },
      "parent": {
        "~id": "101",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "lat": 13.6810998916626,
          "elev": 5,
          "longest": 13123,
          "city": "Bangkok",
          "type": "airport",
          "region": "TH-10",
          "desc": "Suvarnabhumi Bangkok International Airport",
          "code": "BKK",
          "lon": 100.747001647949,
          "country": "TH",
          "icao": "VTBS",
          "runways": 2
        }
      }
    }
  ]
}
```
