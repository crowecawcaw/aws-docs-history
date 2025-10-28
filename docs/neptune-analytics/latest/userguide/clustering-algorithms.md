# Clustering and community detection algorithms in Neptune Analytics

Clustering algorithms evaluate how nodes are clustered in communities, in closely-knit
sets, or in highly or loosely interconnected groups.

These algorithms can identify meaningful groups or clusters of nodes in a network,
revealing hidden patterns and structures that can provide insights into the organization
and dynamics of complex systems. This is valuable in social network analysis and
in biology, for identifying functional modules in protein-protein interaction networks,
and more generally for understanding information flow and influence propagation in
many different domains.

Neptune Analytics supports these community detection algorithms:

- [wcc](wcc.md "wcc.md")   –  
  The Weakly Connected Components (WCC) algorithm finds weakly-connected components
  in a directed graph. A weakly-connected component is a group of nodes where every
  node in the group is reachable from every other node in the group if edge direction
  is ignored.

Identifying weakly-conected components helps in understanding the overall
connectivity and structure of the graph. Weakly-connected components can be
used in transportation networks to identify disconnected regions that may require
improved connectivity, and in social networks to find isolated groups of users with
limited interactions, and in webpage analysis to pinpoint sections with low
accessibility.

- [wcc.mutate](wcc-mutate.md "wcc-mutate.md")   –  
  This algorithm stores the calculated component value of each given node as a property
  of the node.
- [labelPropagation](label-propagation.md "label-propagation.md")   –  
  Label Propagation Algorithm (LPA) is an algorithm for community detection that is also
  used in semi-supervised machine learning for data classification.
- [labelPropagation.mutate](label-propagation-mutate.md "label-propagation-mutate.md")   –  
  Label Propagation Algorithm (LPA) is an algorithm tha assigns labels to nodes based
  on the consensus of their neighboring nodes, making it useful for identifying groups.
  Label propagation can be applied in social networks to find groups, and in identity
  management to identify households, and in recommendation systems to group similar
  products for personalized suggestions. It can also be used in semi-supervised
  machine learning for data classification.
- [scc](scc.md "scc.md")   –  
  The Strongly Connected Components (SCC) algorithm identifies maximally connected
  subgraphs of a directed graph, where every node is reachable from every other node.
  This can provide insights into the tightly interconnected portions of a graph and
  highlight key structures within it. Strongly connected components are valuable in
  computer programming for detecting loops or cycles in code, in social networks to
  find tightly connected groups of users who interact frequently, and in web crawling
  to identify clusters of interlinked pages for efficient indexing.
- [scc.mutate](scc-mutate.md "scc-mutate.md")   –  
  This algorithm finds the maximally connected subgraphs of a directed graph and
  writes their component IDs as a new property of each subgraph node.
- [louvain](louvain.md "louvain.md")   –  
  The Louvain algorithm is a hierarchical community detection method that identifies groups of
  densely connected nodes within networks. It works by optimizing modularity - a measure comparing
  internal community connection density against random networks with the same degree distribution.
  Through iterative local optimization and network aggregation, it efficiently detects community
  structures in large networks. The algorithm can run in both weighted and unweighted modes; when
  an edge weight property is specified, it operates in weighted mode. Louvain is valuable in social
  networks for identifying user communities, in biological networks to discover functional modules
  or protein complexes, and in financial networks to detect market segments or potential fraud rings.
- [louvain.mutate](louvain-mutate.md "louvain-mutate.md")   –  
  This Louvain variant stores the calculated community ID of each node as a property of the node,
  enabling persistent community assignments for applications like customer segmentation, network
  infrastructure optimization, and research community identification.
