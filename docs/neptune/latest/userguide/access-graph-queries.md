

# Querying a Neptune Graph
<a name="access-graph-queries"></a>

Neptune supports the following graph query languages to access a graph:
+ [Gremlin](https://tinkerpop.apache.org/gremlin.html), defined by [Apache TinkerPop](https://tinkerpop.apache.org/) for creating and querying property graphs.

  A query in Gremlin is a traversal made up of discrete steps, each of which follows an edge to a node.

  See [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md) to learn about using Gremlin in Neptune, and [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md) to find specific details about the Neptune implementation of Gremlin.
+ [openCypher](access-graph-opencypher.md) is a declarative query language for property graphs that was originally developed by Neo4j, then open-sourced in 2015, and contributed to the [openCypher](http://www.opencypher.org/) project under an Apache 2 open-source license. Its syntax is documented in the [openCypher spec](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf).
+ [SPARQL](https://www.w3.org/TR/sparql11-overview/) is a declarative language based on graph pattern-matching, for querying [RDF](https://www.w3.org/2001/sw/wiki/RDF) data. It is supported by the [World Wide Web Consortium](https://www.w3.org/).

  See [Accessing the Neptune graph with SPARQL](access-graph-sparql.md) to learn about using SPARQL in Neptune, and [SPARQL standards compliance in Amazon Neptune](feature-sparql-compliance.md) to find specific details about the Neptune implementation of SPARQL.

**Note**  
Both Gremlin and openCypher can be used to query any property-graph data stored in Neptune, regardless of how it was loaded.

**Topics**
+ [Query queuing in Amazon Neptune](access-graph-queuing.md)
+ [Query plan cache in Amazon Neptune](access-graph-qpc.md)
+ [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md)
+ [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md)
+ [Accessing the Neptune Graph with openCypher](access-graph-opencypher.md)
+ [Accessing the Neptune graph with SPARQL](access-graph-sparql.md)