# Levels breadth-first search (BFS) algorithm

The `levels` variant of breadth-first search is an algorithm for
searching nodes from a starting node or nodes in breadth-first order.
From there it performs a breadth-first search and records the hop level from the
starting node of each node that it finds.

It returns a key column of nodes, and a value column containing the level
values of those key nodes.

The level of a source node is 0. Note that because every source node passed
into breadth-first search `levels` initiates its own execution of the algorithm,
your queries should filter to a subset of the graph before executing BFS `levels`
whenever possible.

## `.bfs.levels`   syntax

```
CALL neptune.algo.bfs.levels(
  [`source-node list (required)`],
  {
    edgeLabels: [`list of edge labels for filtering (optional)`],
    vertexLabel: `a node label for filtering (optional)`,
    maxDepth: `maximum number of hops to traverse from a source node (optional)`,
    traversalDirection: `traversal direction (optional)`,
    concurrency: `number of threads to use (optional)`
  }
)
YIELD `the outputs to generate (source and/or node)`
RETURN `the outputs to return`
```

## `.bfs.levels`   inputs

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

  If you provide a node label to filter on then only nodes matching that label
  will be traversed. This does not, however, filter out any nodes in the source node list.
  - **maxDepth**   _(optional)_   –  
    _type:_ positive integer or 0 or -1;   _default:_ -1.

  The maximum number of hops to traverse from a source node. If set at `-1` then there's
  no maximum depth limit. If set to `0`, only the nodes in the source node list are returned.
  - **traversalDirection**   _(optional)_   –  
    _type:_ `string`;   _default:_ `"outbound"`.

  The direction of edge to follow. Must be one of: `"inbound"`, `"outbound"`, or `"both"`.
  - **concurrency**   _(optional)_   –  
    _type:_ 0 or 1;   _default:_ 0.

  Controls the number of concurrent threads used to run the algorithm.

  If set to `0`, uses all available threads to complete execution of the individual algorithm
  invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
  of many algorithms concurrently.

## `.bfs.levels`   outputs

The `.bfs.levels` algorithm returns:

- **source**   –  
  _type:_ `Node[]`.

The source nodes.

- **node**   –  
  _type:_ `Node[]`.

The nodes that the algorithm traversed from each source node.

- **level**   –  
  _type:_ `integer[]`.

The hop levels of those traversed nodes.

## `.bfs.levels`   standalone query examples

The examples below are standalone examples, where the query provides an explicit
source node list.

A query like this one would return an empty result because the source list is empty:

```
CALL neptune.algo.bfs.levels(
  ["101", "102"],
  {
    edgeLabels: ["route"],
    vertexLabel: "airport",
    maxDepth: 6,
    traversalDirection: "both",
    concurrency: 2
  }
)
YIELD node
```

You can run the algorithm using the `execute-query` operation
in the AWS CLI like this:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string 'CALL neptune.algo.bfs.levels(["101", "102"], {edgeLabels: ["route"]})' \
  --language open_cypher \
  /tmp/out.txt
```

By default, all the outputs are generated. You can use `YIELD` to specify which of
those outputs to generate. For example, to generate only the `"node"` and
`level` outputs:

```
CALL neptune.algo.bfs.levels(["101"], {edgeLabels: ["route"]}) YIELD node, level
```

## `.bfs.levels`   query integration examples

The examples below are query integration examples, where `.bfs.levels` follows a
`MATCH` clause and uses the output of the `MATCH` clause as
its source node list:

```
MATCH (n) WITH n LIMIT 5
CALL neptune.algo.bfs.levels(n, {edgeLabels: ["route"]})
YIELD node, level
RETURN n, node, level
```

This query illustrates various ways to constrain the input and output:

```
MATCH (n) where id(n)="101"
CALL neptune.algo.bfs.levels(n, { edgeLabel: "route", maxDepth: 2})
YIELD node, level WHERE node.city CONTAINS "New"
RETURN n.city, node.city, level
```

###### Warning

It is not good practice to use `MATCH(n)` without restriction
in query integrations. Keep in mind that every node returned by the `MATCH(n)`
clause invokes the algorithm once, which can result a very long-running query if
a large number of nodes is returned. Use `LIMIT` or put conditions on the
`MATCH` clause to restrict its output appropriately.

## Sample `.bfs.levels` output

Here is an example of the output returned by .bfs.levels when run against the
[sample air-routes dataset [nodes]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv"), and
[sample air-routes dataset [edges]](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv "https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv"), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.bfs.levels(['101'], {maxDepth: 1}) yield source, node, level return source, node, level limit 2" \
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
      "level": 1
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
      "level": 1
    }
  ]
}
```
