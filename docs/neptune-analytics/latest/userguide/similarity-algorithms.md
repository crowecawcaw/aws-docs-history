# Similarity algorithms in Neptune Analytics

Graph similarity algorithms allow you to compare and analyze the similarities and
dissimilarities between different graph structures, which can provide insight into relationships,
patterns, and commonalities across diverse datasets. This is invaluable in various fields,
such as biology, for comparing molecular structures, such as social networks, for identifying
similar communities, and such as recommendation systems, for suggesting similar items based
on user preferences.

Neptune Analytics supports the following similarity algorithms:

- [neighbors.common](common-neighbors.md "common-neighbors.md")   –  
  This algorithm counts the number of common neighbors of two input vertices, which
  is the intersection of the neighborhoods of those vertices.

By counting how many neighboring nodes are shared by two nodes, it provides a measure
of their potential interaction or similarity within the network. It's used in social
network analysis to identify individuals with mutual connections, in citation networks
to find influential papers referenced by multiple sources, and in transportation networks
to locate critical hubs with many direct connections to other nodes.

- [neighbors.total](total-neighbors.md "total-neighbors.md")   –  
  This algorithm counts the number of total unique neighbors among two input vertices,
  which is the union of the neighborhoods of those vertices.
- [jaccardSimilarity](jaccard-similarity.md "jaccard-similarity.md")   –  
  This algorithm measures the similarity between two sets by dividing the
  size of their intersection by the size of their union.

By measuring the proportion of shared neighbors relative to the total number of
unique neighbors, it provides a metric for understanding the degree of overlap or
commonality between different parts of a network. Jaccard similarity is applied in
recommendation systems to suggest products or content to users based on their shared
preferences and in biology to compare genetic sequences for identifying similarities
in DNA fragments.

- [overlapSimilarity](overlap-similarity.md "overlap-similarity.md")   –  
  This algorithm measures the overlap between the neighbors of two vertices.

It quantifies the similarity between nodes by calculating the ratio of common
neighbors they share to the total number of neighbors they collectively have,
providing a measure of their closeness or similarity within the network.
Overlap similarity is applied in social network analysis to identify communities
of individuals with shared interests or interactions, and in biological networks
to detect common functionalities among proteins in molecular pathways.
