

# Source-target breadth-first search (BFS) algorithm
<a name="bfs-path"></a>

 The `path` variant of breadth-first search finds a shortest path (the one with the fewest hops) between a source node and a target node. It is the unweighted analogue of the source-target shortest path algorithms (`.sssp.*.path`): where those minimize the accumulated edge weight, `.bfs.path` minimizes the number of hops. Because breadth-first search is unweighted, every edge counts as a single hop. If more than one shortest path exists between the source node and the target node, only one of them is returned. By default, when both `edgeLabels` and `vertexLabels` are empty, the whole graph is traversed. 

 Neptune Analytics implements the algorithm such that: 
+ The path is computed unweighted: every edge counts as a single hop, regardless of any edge property values.
+ If the target is not reachable from the source, no row is returned for that source-target pair.
+ You can bound the search with `maxDepth`. If the target is farther than `maxDepth` hops from the source, no path is returned for that pair.
+ The target-less BFS variants (`.bfs`, `.bfs.levels`) explore every reachable vertex. In contrast, `.bfs.path` stops as soon as the target is reached. It never explores beyond the target's hop level. When the target is much closer than `maxDepth` (or `maxDepth` is unbounded), this can be far cheaper than a full traversal. If one source node has several target nodes, the search stops only when all of them are reached. If a target is not reachable, the search explores every vertex reachable within `maxDepth`.

**Note**  
The `path` variant of breadth-first search computes *unweighted* shortest paths, where each edge counts as a single hop. If your edges have weights and you want the lowest-cost (weighted) shortest path between a source and a target, use [.sssp.deltaStepping.path](sssp-deltaStepping-path.md) or [.sssp.bellmanFord.path](sssp-bellmanFord-path.md) instead.

## `.bfs.path`   syntax
<a name="bfs-path-syntax"></a>

```
CALL neptune.algo.bfs.path(
  {{source node (required)}}, {{target node (required)}},
  {
    edgeLabels: [{{list of edge labels for filtering (optional)}}],
    vertexLabels: [{{list of node labels for filtering (optional)}}],
    maxDepth: {{maximum number of hops to traverse from a source node (optional)}},
    traversalDirection: {{traversal direction (optional)}},
    concurrency: {{number of threads to use (optional)}}
  }
)
YIELD {{the outputs to generate (source, target, and/or path)}}
RETURN {{the outputs to return}}
```

## `.bfs.path`   inputs
<a name="bfs-path-inputs"></a>
+ **source node**   *(required)*   –   *type:* `Node` or `NodeId`;   *default: none*.

  The node to use as the starting location for the algorithm.
  + In a standalone call, provide a single node ID string. A list of nodes is not accepted.
  + Each distinct source node triggers its own execution of the algorithm.
  + If the algorithm is called following a `MATCH` clause (this is known as query-algorithm integration), each node that the `MATCH` clause returns is used as a source node for the algorithm.
+ **target node**   *(required)*   –   *type:* `Node` or `NodeId`;   *default: none*.

  The node to use as the ending location for the algorithm.
  + In a standalone call, provide a single node ID string. A list of nodes is not accepted.
  + Each source-target node pair produces an output of the algorithm.
  + If the algorithm is called following a `MATCH` clause (this is known as query-algorithm integration), each node that the `MATCH` clause returns is used as a target node for the algorithm.
+ 

**a configuration object that contains:**
  + **edgeLabels**   *(optional)*   –   *type:* a list of edge label strings;   *example:* `["route", {{...}}]`;   *default:* no edge filtering.

    To filter on one more edge labels, provide a list of the ones to filter on. If no `edgeLabels` field is provided then all edge labels are processed during traversal.
  + **vertexLabels**   *(optional)*   –   *type:* a list of node label strings;   *example:* `["airport", {{...}}]`;  *default:* no node filtering.

    To filter on one or more node labels, provide a list of the labels to filter on. A vertex matches the filter if it carries any of the labels in the list. This filters the vertices that are visited during the traversal, including the target, but does not filter the source vertex. If no `vertexLabels` field is provided, all node labels are processed during traversal.
  + **maxDepth**   *(optional)*   –   *type:* positive integer or 0 or -1;   *default:* -1.

    The maximum number of hops to traverse from a source node. If set at `-1` then there's no maximum depth limit. If a target node is farther than `maxDepth` hops from the source node, no path is returned for that source-target pair.
  + **traversalDirection**   *(optional)*   –   *type:* `string`;   *default:*` "outbound"`.

    The direction of edge to follow. Must be one of: `"inbound"`, `"outbound"`, or `"both"`.
  + **concurrency**   *(optional)*   –   *type:* 0 or 1;   *default:* 0.

    Controls the number of concurrent threads used to run the algorithm.

     If set to `0`, uses all available threads to complete execution of the individual algorithm invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation of many algorithms concurrently.

## Outputs for the `.bfs.path` algorithm
<a name="bfs-path-outputs"></a>

For every pair of source and target nodes that are connected, the algorithm returns:
+ **source**   –   The source vertex.
+ **target**   –   The target vertex.
+ **path**   –   An openCypher path object that represents the shortest path between the source and the target. It lists the vertices from the source to the target, with the edge that connects each pair of vertices placed between them.
  + Starts and ends with a vertex, and has edges in between each vertex.
  + Includes the source and the target vertices.
  + When the source and the target are the same node, the path is a single vertex with no edges.

**Note**  
`.bfs.path` returns only `source`, `target`, and `path`; there is no separate `level` or distance output. You can derive these values from the path in your `RETURN` clause: the hop count with `length(path)`, the list of vertices with `nodes(path)`, and the list of edges with `relationships(path)`.

## `.bfs.path`   query examples
<a name="bfs-path-query-examples"></a>

This standalone query explicitly provides a source node and a target node. It bounds the search to paths of at most four hops, follows edges in both directions, and restricts the traversal to `airport` nodes:

```
CALL neptune.algo.bfs.path(
  "9", "37",
  {
    edgeLabels: ["route"],
    vertexLabels: ["airport"],
    maxDepth: 4,
    traversalDirection: "both",
    concurrency: 1
  }
)
YIELD source, target, path
RETURN source, target, path
```

This is a query integration example, where `.bfs.path` follows `MATCH` clauses and uses the nodes that they return as its source and target nodes:

```
MATCH (source:airport {code: 'FLL'})
MATCH (target:airport {code: 'HNL'})
CALL neptune.algo.bfs.path(
  source, target,
  {
    edgeLabels: ["route"],
    vertexLabels: ["airport"],
    traversalDirection: "outbound",
    concurrency: 1
  }
)
YIELD path
RETURN source, target, path
```

Although `.bfs.path` returns only the `path`, you can derive the hop count and the list of vertices from it in the `RETURN` clause. Use `length(path)` for the hop count and `nodes(path)` for the list of vertices. For more information about the list of vertices, see the `vertexPath` output of [.sssp.deltaStepping.path](sssp-deltaStepping-path.md). For example:

```
MATCH (source:airport {code: 'FLL'})
MATCH (target:airport {code: 'HNL'})
CALL neptune.algo.bfs.path(
  source, target,
  {
    edgeLabels: ["route"]
  }
)
YIELD path
RETURN length(path) AS level, nodes(path) AS vertexPath, path
```

**Warning**  
It is not good practice to use `MATCH(n)` without restriction in query integrations. Keep in mind that every node returned by the `MATCH(n)` clause invokes the algorithm once, which can result in a very long-running query if a large number of nodes are returned; and that every source-target node pair produces an output, which can result in a very large query output if a large number of nodes are returned. Use `LIMIT` or put conditions on the `MATCH` clause to restrict its output appropriately.

## Sample `.bfs.path` output
<a name="bfs-path-sample-output"></a>

Here is an example of the output returned by .bfs.path when run against the [ sample air-routes dataset [nodes] on the GitHub website](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-nodes.csv), and [ sample air-routes dataset [edges] on the GitHub website](https://github.com/krlawrence/graph/blob/main/sample-data/air-routes-latest-edges.csv), when using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n:airport {code: 'FLL'})
  MATCH (m:airport {code: 'HNL'})
  CALL neptune.algo.bfs.path(n, m, {
  edgeLabels: ['route'],
  vertexLabels: ['airport'],
  traversalDirection: 'outbound',
  concurrency: 1
  })
  YIELD source, target, path
  RETURN source, target, length(path) AS level,
    nodes(path) AS vertexPath, path" \
  --language open_cypher \
  /tmp/out.txt

cat /tmp/out.txt
{
  "results": [{
      "source": {
        "~id": "9",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-FL",
          "runways": 2,
          "country": "US",
          "city": "Fort Lauderdale",
          "type": "airport",
          "icao": "KFLL",
          "lon": -80.152702331542997,
          "code": "FLL",
          "lat": 26.0725994110107,
          "longest": 9000,
          "elev": 64,
          "desc": "Fort Lauderdale/Hollywood International Airport"
        }
      },
      "target": {
        "~id": "37",
        "~entityType": "node",
        "~labels": ["airport"],
        "~properties": {
          "region": "US-HI",
          "runways": 4,
          "country": "US",
          "city": "Honolulu",
          "type": "airport",
          "icao": "PHNL",
          "lon": -157.92199707031199,
          "code": "HNL",
          "lat": 21.318700790405298,
          "longest": 12312,
          "elev": 13,
          "desc": "Honolulu International Airport"
        }
      },
      "level": 2,
      "vertexPath": [{
          "~id": "9",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-FL",
            "runways": 2,
            "country": "US",
            "city": "Fort Lauderdale",
            "type": "airport",
            "icao": "KFLL",
            "lon": -80.152702331542997,
            "code": "FLL",
            "lat": 26.0725994110107,
            "longest": 9000,
            "elev": 64,
            "desc": "Fort Lauderdale/Hollywood International Airport"
          }
        }, {
          "~id": "35",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-NY",
            "runways": 3,
            "country": "US",
            "city": "Newark",
            "type": "airport",
            "icao": "KEWR",
            "lon": -74.168701171875,
            "code": "EWR",
            "lat": 40.692501068115199,
            "longest": 11000,
            "elev": 17,
            "desc": "Newark, Liberty"
          }
        }, {
          "~id": "37",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-HI",
            "runways": 4,
            "country": "US",
            "city": "Honolulu",
            "type": "airport",
            "icao": "PHNL",
            "lon": -157.92199707031199,
            "code": "HNL",
            "lat": 21.318700790405298,
            "longest": 12312,
            "elev": 13,
            "desc": "Honolulu International Airport"
          }
        }],
      "path": [{
          "~id": "9",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-FL",
            "runways": 2,
            "country": "US",
            "city": "Fort Lauderdale",
            "type": "airport",
            "icao": "KFLL",
            "lon": -80.152702331542997,
            "code": "FLL",
            "lat": 26.0725994110107,
            "longest": 9000,
            "elev": 64,
            "desc": "Fort Lauderdale/Hollywood International Airport"
          }
        }, {
          "~id": "neptune_reserved_1_1152921526082404354",
          "~entityType": "relationship",
          "~start": "9",
          "~end": "35",
          "~type": "route",
          "~properties": {
            "dist": 1065
          }
        }, {
          "~id": "35",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-NY",
            "runways": 3,
            "country": "US",
            "city": "Newark",
            "type": "airport",
            "icao": "KEWR",
            "lon": -74.168701171875,
            "code": "EWR",
            "lat": 40.692501068115199,
            "longest": 11000,
            "elev": 17,
            "desc": "Newark, Liberty"
          }
        }, {
          "~id": "neptune_reserved_1_1152921534671749133",
          "~entityType": "relationship",
          "~start": "35",
          "~end": "37",
          "~type": "route",
          "~properties": {
            "dist": 4950
          }
        }, {
          "~id": "37",
          "~entityType": "node",
          "~labels": ["airport"],
          "~properties": {
            "region": "US-HI",
            "runways": 4,
            "country": "US",
            "city": "Honolulu",
            "type": "airport",
            "icao": "PHNL",
            "lon": -157.92199707031199,
            "code": "HNL",
            "lat": 21.318700790405298,
            "longest": 12312,
            "elev": 13,
            "desc": "Honolulu International Airport"
          }
        }]
    }]
}
```