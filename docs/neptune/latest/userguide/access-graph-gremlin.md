# Accessing a Neptune graph with Gremlin

Amazon Neptune is compatible with Apache TinkerPop3 and Gremlin. This means
that you can connect to a Neptune DB instance and use the Gremlin traversal language to query the
graph (see [The
Graph](https://tinkerpop.apache.org/docs/current/reference/#graph "https://tinkerpop.apache.org/docs/current/reference/#graph") in the Apache TinkerPop3 documentation). For differences in the Neptune
implementation of Gremlin, see [Gremlin standards compliance](access-graph-gremlin-differences.md "access-graph-gremlin-differences.md").

Different Neptune engine versions support different Gremlin versions. Check
the [engine release page](engine-releases.md "engine-releases.md") of the Neptune
version you are running to determine which Gremlin release it supports.

A _traversal_ in Gremlin is a series of chained steps. It starts at a
vertex (or edge). It walks the graph by following the outgoing edges of each vertex and then the
outgoing edges of those vertices. Each step is an operation in the traversal. For more
information, see [The
Traversal](https://tinkerpop.apache.org/docs/current/reference/#traversal "https://tinkerpop.apache.org/docs/current/reference/#traversal") in the TinkerPop3 documentation.

There are Gremlin language variants and support for Gremlin access in various programming
languages. For more information, see [On Gremlin Language Variants](https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants "https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants") in the TinkerPop3 documentation.

This documentation describes how to access Neptune with the following variants and
programming languages.

As discussed in [Encrypting connections to your Amazon Neptune database with SSL/HTTPS](security-ssl.md "security-ssl.md"), you must use
Transport Layer Security/Secure Sockets Layer (TLS/SSL) when connecting to Neptune in all
AWS Regions.

###### Gremlin-Groovy

The Gremlin Console and HTTP REST examples in this section use the Gremlin-Groovy variant.
For more information about the Gremlin Console and Amazon Neptune, see the [Using Gremlin to access graph data in Amazon Neptune](get-started-graph-gremlin.md "get-started-graph-gremlin.md") section of the Quick Start.

###### Gremlin-Java

The Java sample is written with the official TinkerPop3 Java implementation and uses the
Gremlin-Java variant.

###### Gremlin-Python

The Python sample is written with the official TinkerPop3 Python implementation and uses
the Gremlin-Python variant.

The following sections walk you through how to use the Gremlin Console,
**REST** over HTTPS, and various programming languages to connect to a
Neptune DB instance.

Before you begin, you must have the following:

- A Neptune DB instance. For information about creating a Neptune DB instance, see [Creating an Amazon Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").
- An Amazon EC2 instance in the same virtual private cloud (VPC) as your Neptune DB instance.
  For more information about loading data into Neptune, including prerequisites, loading
  formats, and load parameters, see [Loading data into Amazon Neptune](load-data.md "load-data.md").

###### Topics

- [Set up the Gremlin console to connect to a
  Neptune DB instance](access-graph-gremlin-console.md "access-graph-gremlin-console.md")
- [Using the HTTPS REST endpoint to connect to a
  Neptune DB instance](access-graph-gremlin-rest.md "access-graph-gremlin-rest.md")
- [Java-based Gremlin clients to use with Amazon Neptune](access-graph-gremlin-client.md "access-graph-gremlin-client.md")
- [Using Python to connect to a Neptune DB
  instance](access-graph-gremlin-python.md "access-graph-gremlin-python.md")
- [Using .NET to connect to a Neptune DB
  instance](access-graph-gremlin-dotnet.md "access-graph-gremlin-dotnet.md")
- [Using Node.js to connect to a Neptune DB
  instance](access-graph-gremlin-node-js.md "access-graph-gremlin-node-js.md")
- [Using Go to connect to a Neptune DB
  instance](access-graph-gremlin-go.md "access-graph-gremlin-go.md")
- [Gremlin query hints](gremlin-query-hints.md "gremlin-query-hints.md")
- [Gremlin query status API](gremlin-api-status.md "gremlin-api-status.md")
- [Gremlin query cancellation](gremlin-api-status-cancel.md "gremlin-api-status-cancel.md")
- [Support for Gremlin script-based sessions](access-graph-gremlin-sessions.md "access-graph-gremlin-sessions.md")
- [Gremlin transactions in Neptune](access-graph-gremlin-transactions.md "access-graph-gremlin-transactions.md")
- [Using the Gremlin API with Amazon Neptune](gremlin-api-reference.md "gremlin-api-reference.md")
- [Caching query results in Amazon Neptune Gremlin](gremlin-results-cache.md "gremlin-results-cache.md")
- [Making efficient upserts with Gremlin
  mergeV() and mergeE() steps](gremlin-efficient-upserts.md "gremlin-efficient-upserts.md")
- [Making efficient Gremlin upserts with fold()/coalesce()/unfold()](gremlin-efficient-upserts-pre-3.md "gremlin-efficient-upserts-pre-3.md")
- [Analyzing Neptune query execution using Gremlin explain](gremlin-explain.md "gremlin-explain.md")
- [Using Gremlin with the Neptune DFE query engine](gremlin-with-dfe.md "gremlin-with-dfe.md")
