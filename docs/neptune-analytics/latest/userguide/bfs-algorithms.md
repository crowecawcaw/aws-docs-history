# Breadth-first search (BFS) path finding algorithms

Breadth-first search (BFS) path-finding algorithms search for nodes in
breadth-first order, starting from a single vertex. They can also, in the multi-source
case, start from more than one vertex.

They can systematically explore and evaluates all neighboring nodes from a
starting point before moving on to the neighbors of those nodes, which ensures
that the algorithm searches the shallowest levels of the graph first.

Breadth-first-search is used in computer networking to find the shortest path
between two devices, and in social networks to understand how information spreads
through connections, and in games to explore possible moves and strategies.

**Time complexity**   –  
The time complexity of breadth-first search algorithms is `O(|V|+|E|)`,
where `|V|` is the number of vertices in the graph and `|E|`
is the number of edges in the graph.

A breadth-first algorithm can be invoked as a _standalone_
operation whose inputs are explicitly defined, or as a _query-algorithm
integration_ which takes as its input the output of an immediately
preceding `MATCH` clause.

Neptune Analytics supports these BFS algorithms:

- [.bfs](bfs-standard.md "bfs-standard.md")   –  
  This standard breadth-first search algorithm starts from the source vertex of
  the graph and returns a column of visited vertices.
- [.bfs.parents](bfs-parents.md "bfs-parents.md")   –  
  This variant of BFS starts from a source vertex or vertices and finds the
  parent of each vertex during the search. It returns a key column of the vertices
  and a value column of the parents of the key vertices.
- [.bfs.levels](bfs-levels.md "bfs-levels.md")   –  
  This variant of BFS starts from a source vertex or vertices and finds the
  levels of each vertex during the search. It returns a key column of
  the vertices and a value column of integers that are the level values
  of the key vertices.

Note that the level of a source vertex is 0.
