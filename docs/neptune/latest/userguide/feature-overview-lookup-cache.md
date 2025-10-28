# The Neptune lookup cache can accelerate read queries

Amazon Neptune implements a lookup cache that uses the `R5d` instance's
NVMe-based SSD to improve read performance for queries with frequent, repetitive
lookups of property values or RDF literals. The lookup cache temporarily stores
these values in the NVMe SSD volume where they can be accessed rapidly.

This feature is available starting with [Amazon Neptune Engine Version 1.0.4.2.R2 (2021-06-01)](engine-releases-1.0.4.2.md "engine-releases-1.0.4.2.md").

Read queries that return the properties of a large number of vertices and edges, or
many RDF triples, can have a high latency if the property values or literals need
to be retrieved from cluster storage volumes rather than memory. Examples include
long-running read queries that return a large number of full names from an identity
graph, or of IP addresses from a fraud-detection graph. As the number of property values
or RDF literals returned by your query increases, available memory decreases and your
query execution can significantly degrade.
