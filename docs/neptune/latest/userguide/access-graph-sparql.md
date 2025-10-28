# Accessing the Neptune graph with SPARQL

SPARQL is a query language for the Resource Description Framework (RDF), which is a graph
data format designed for the web. Amazon Neptune is compatible with SPARQL 1.1. This means that
you can connect to a Neptune DB instance and query the graph using the query language described in the
[SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/")
specification.

A query in SPARQL consists of a `SELECT` clause to specify the variables to
return and a `WHERE` clause to specify which data to match in the graph. If you are
unfamiliar with SPARQL queries, see [Writing Simple Queries](https://www.w3.org/TR/sparql11-query/#WritingSimpleQueries "https://www.w3.org/TR/sparql11-query/#WritingSimpleQueries")
in the [SPARQL 1.1 Query
Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/").

###### Important

To load data, `SPARQL UPDATE INSERT` may work well for a small dataset,
but if you need to load a substantial amount of data from a file, see [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md "bulk-load.md").

For more information about the specifics of Neptune's SPARQL implementation,
see [SPARQL standards compliance](feature-sparql-compliance.md "feature-sparql-compliance.md").

Before you begin, you must have the following:

- A Neptune DB instance. For information about creating a Neptune DB instance, see [Creating an Amazon Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").
- An Amazon EC2 instance in the same virtual private cloud (VPC) as your Neptune DB instance.

###### Topics

- [Using the RDF4J console to connect to a
  Neptune DB instance](access-graph-sparql-rdf4j-console.md "access-graph-sparql-rdf4j-console.md")
- [Using RDF4J Workbench to connect to a
  Neptune DB instance](access-graph-sparql-rdf4j-workbench.md "access-graph-sparql-rdf4j-workbench.md")
- [Using Java to connect to a Neptune DB
  instance](access-graph-sparql-java.md "access-graph-sparql-java.md")
- [SPARQL HTTP API](sparql-api-reference.md "sparql-api-reference.md")
- [SPARQL query hints](sparql-query-hints.md "sparql-query-hints.md")
- [SPARQL DESCRIBE behavior with respect to the default graph](sparql-default-describe.md "sparql-default-describe.md")
- [SPARQL query status API](sparql-api-status.md "sparql-api-status.md")
- [SPARQL query cancellation](sparql-api-status-cancel.md "sparql-api-status-cancel.md")
- [Using the SPARQL 1.1 Graph Store HTTP Protocol (GSP) in Amazon Neptune](sparql-graph-store-protocol.md "sparql-graph-store-protocol.md")
- [Analyzing Neptune query execution using SPARQL explain](sparql-explain.md "sparql-explain.md")
- [SPARQL federated queries in Neptune using the SERVICE extension](sparql-service.md "sparql-service.md")
