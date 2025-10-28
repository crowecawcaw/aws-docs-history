# Accessing graph data in Amazon Neptune

You can interact with a Amazon Neptune DB cluster after creating a connection. This involves loading data, executing queries, and performing other operations.
Most users leverage the `curl` or `awscurl` command-line tools to communicate with the Neptune DB cluster effectively.
These tools enable you to send requests, load data, and retrieve results from the graph database, facilitating seamless data management and querying capabilities.

## Setting up `curl` to communicate with

your Neptune endpoint

As illustrated in many of the examples in this documentation, the [curl](https://curl.haxx.se/ "https://curl.haxx.se/") command line tool is a handy option for
communicating with your Neptune endpoint. For information about the tool, see the [curl man page](https://curl.haxx.se/docs/manpage.html "https://curl.haxx.se/docs/manpage.html"), and the book
_[Everything curl](https://ec.haxx.se/ "https://ec.haxx.se/")_.

To connect using HTTPS (as we recommend and as Neptune requires in most Regions),
`curl` needs access to appropriate certificates. To learn how to obtain these
certificates and how to format them properly into a certificate authority (CA) certificate
store that `curl` can use, see [SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html") in the `curl` documentation.

You can then specify the location of this CA certificate store using the
`CURL_CA_BUNDLE` environment variable. On Windows, `curl`
automatically looks for it in a file named `curl-ca-bundle.crt`. It looks first in
the same directory as `curl.exe` and then elsewhere on the path. For more
information, see [SSL Certificate
Verification](https://curl.haxx.se/docs/sslcerts.html "https://curl.haxx.se/docs/sslcerts.html").

As long as `curl` can locate the appropriate certificates,
it handles HTTPS connections just like HTTP connections, without extra
parameters. Examples in this documentation are based on that scenario.

## Using a query language to access graph data in your Neptune DB cluster

Once you are connected, you can use the Gremlin and openCypher query languages to
create and query a property graph, or the SPARQL query language to create and query
a graph containing RDF data.

###### Graph query languages supported by Neptune

- [Gremlin](access-graph-gremlin.md "access-graph-gremlin.md") is a graph traversal language
  for property graphs. A query in Gremlin is a traversal made up of discrete steps,
  each of which follows an edge to a node. See Gremlin documentation at [Apache TinkerPop3](https://tinkerpop.apache.org/docs/current/reference/ "https://tinkerpop.apache.org/docs/current/reference/")
  for more information.

The Neptune implementation of Gremlin has some differences from other implementations,
especially when you are using Gremlin-Groovy (Gremlin queries sent as serialized text). For
more information, see [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md "access-graph-gremlin-differences.md").

- [openCypher](access-graph-opencypher.md "access-graph-opencypher.md") is a declarative
  query language for property graphs that was originally developed by Neo4j, then open-sourced
  in 2015, and contributed to the [openCypher](http://www.opencypher.org/ "http://www.opencypher.org/")
  project under an Apache 2 open-source license. Its syntax is documented in the [Cypher Query
  Language Reference, Version 9](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf "https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf").
- [SPARQL](access-graph-sparql.md "access-graph-sparql.md") is a declarative query
  language for [RDF](https://www.w3.org/2001/sw/wiki/RDF "https://www.w3.org/2001/sw/wiki/RDF") data, based
  on the graph pattern matching that is standardized by the World Wide Web Consortium (W3C)
  and described in [SPARQL 1.1
  Overview](https://www.w3.org/TR/sparql11-overview/ "https://www.w3.org/TR/sparql11-overview/")) and the [SPARQL
  1.1 Query Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/") specification.

###### Note

You can access property graph data in Neptune using both Gremlin and
openCypher, but not using SPARQL. Similarly, you can only access RDF data using SPARQL,
not Gremlin or openCypher.
