# Single-source shortest-path algorithms

A single-source-shortest-path algorithm finds the shortest paths (or the distance
of the shortest paths) between a given vertex and all reachable vertices in the graph
(including itself).

By determining the most efficient routes from a single starting node to all other
nodes in the graph, single-source-shortest-path can be used calculate the shortest
distances or lowest cost required to reach each destination. This is applicable in GPS
systems to find the fastest routes between a starting point and differeent destinations,
and in logistics to optimize delivery routes, and in transportation planning for
efficient navigation through road networks.

Neptune Analytics supports the following single-source-shortest-path (SSSP) algorithms:

- [.sssp.bellmanFord](sssp-bellmanFord.md "sssp-bellmanFord.md")   –  
  Computes the shortest path distances from a source vertex to all other vertices in the graph
  using the [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm "https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm")
  algorithm. Positive edge weights must be provided using the `edgeWeightProperty`,
  and the traversal direction must not be set to `both`.
- [.sssp.bellmanFord.parents](sssp-bellmanFord-parents.md "sssp-bellmanFord-parents.md")   –  
  Identifies the parent vertices along the shortest paths from the source vertex to all other
  vertices in the graph using the Bellman-Ford algorithm. Positive edge weights must be provided
  using the `edgeWeightProperty`, and the traversal direction must not be set to
  `both`.
- [.sssp.bellmanFord.path](sssp-bellmanFord-path.md "sssp-bellmanFord-path.md")   –  
  Finds the shortest path between a given source vertex and a target vertex in the graph using the
  [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm "https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm")
  algorithm. To compute all shortest paths from a given source vertex, the regular SSSP algorithm can be used.
  Positive edge weights must be provided using the `edgeWeightProperty`, and the traversal direction must not be
  set to `both`.
- [.sssp.deltaStepping](sssp-deltaStepping.md "sssp-deltaStepping.md")   –  
  Computes the shortest path distances from a source vertex to all other vertices in the graph
  using a [delta-stepping](https://en.wikipedia.org/wiki/Parallel_single-source_shortest_path_algorithm#Delta_stepping_algorithm "https://en.wikipedia.org/wiki/Parallel_single-source_shortest_path_algorithm#Delta_stepping_algorithm")
  algorithm. Positive edge weights must be provided using the `edgeWeightProperty`,
  and the traversal direction must not be set to `both`.
- [.sssp.deltaStepping.parents](sssp-deltaStepping-parents.md "sssp-deltaStepping-parents.md")   –  
  Identifies the parent vertices along the shortest paths from the source vertex to all
  other vertices in the graph using a delta-stepping algorithm. Positive edge weights
  must be provided using the `edgeWeightProperty`, and the traversal direction
  must not be set to `both`.
- [.sssp.deltaStepping.path](sssp-deltaStepping-path.md "sssp-deltaStepping-path.md")   –  
  Finds the shortest path between a given source vertex and a target vertex in the graph using the delta-stepping
  algorithm. To compute all shortest paths from a given source vertex, the regular SSSP algorithm can be used.
  Positive edge weights must be provided using the `edgeWeightProperty`, and the traversal direction must not be set
  to `both`.
- [.topksssp](topk-sssp.md "topk-sssp.md")   –  
  The TopK hop-limited single source shortest path algorithm finds the single-source weighted
  shortest paths starting from a source vertex to all its `maxDepth` neighbors.
  The distance or cost from the source vertex to each target vertex is accumulated on the
  edge weights of the path. The topK distances of the paths are sorted in descending or
  ascending order.

The algorithm can be run unweighted as well as weighted. When you run it unweighted,
it's equivalent to [.bfs.levels](bfs-levels.md "bfs-levels.md").
