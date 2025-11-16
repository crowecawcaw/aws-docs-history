# Centrality algorithms in Neptune Analytics

Centrality algorithms utilize the topology of a network to determine the
relative importance or influence of a specific node within the graph. By
measuring the relative importance of a node or edge within a network, centrality
values can indicate which elements in a graph play a critical role in that network.

By identifying the most influential or important nodes within a network, centrality
algorithms can provide insights about key players or critical points of interaction. This is
valuable in social network analysis, where it helps pinpoint influential individuals,
and in transportation networks, where it aids in identifying crucial hubs for efficient
routing and resource allocation.

Different types of centrality algorithms use different techniques to measure
the importance of a node. Understanding how an algorithm calculates centrality
is important to understanding the meaning of its outputs.

In addition to returning centrality data to the client, Neptune Analytics
provides mutate variations of the centrality algorithms which store the calculated
centrality values as vertex properties in the graph.

Neptune Analytics supports three centrality algorithms along with their mutate variants:

- [degree](degree.md "degree.md")   –  
  This measures a nodes's centrality by the number of edges connected to it, and
  can therefore be used to find the most connected nodes in a network.
- [degree.mutate](degree-mutate.md "degree-mutate.md")   –  
  The degree centrality mutate algorithm measures the number of incident edges
  of each vertex it traverses and writes that calculated degree value as a
  property of the vertex.
- [degreeDistribution](degreeDistribution.md "degreeDistribution.md")   –  
  The Degree Distribution algorithm is a tool for analyzing and visualizing the structural characteristics
  of a graph. It calculates the frequency distribution of vertex degrees across the entire network and provides
  basic statistics of the distribution.
- [pageRank](page-rank.md "page-rank.md")   –  
  This is an iterative algorithm that measures a nodes's centrality by the number
  and quality of incident edges and adjacent vertices. The centrality of a node
  connected to a few important nodes may therefore be higher than that of a node
  connected to many less important nodes. The output of this algorithm is a value
  that indicates the importance of a given node relative to the other nodes in
  the graph.
- [pageRank.mutate](page-rank-mutate.md "page-rank-mutate.md")   –  
  This algorithm stores the calculated PageRank of a given node as a property of the
  node.
- [closenessCentrality](closeness-centrality.md "closeness-centrality.md")   –  
  This algorithm computes the closeness centrality (CC) metric of nodes in a graph.
  The closeness centrality metric of a vertex is a positive measure of how close it
  is to all other vertices, or how central it is in the graph. Because it indicates how quickly
  all other nodes in a network can be reached from a given node, it can be used in
  transportation networks to identify key hub locations, and in disease-spread
  modeling to pinpoint central locations for targeted intervention efforts.
- [closenessCentrality.mutate](closeness-centrality-mutate.md "closeness-centrality-mutate.md")   –  
  This algorithm computes the closeness centrality (CC) metric of vertices in a graph
  and writes them as a property of each vertex.
