

# Accessing graph data in Amazon Neptune
<a name="get-started-access-graph"></a>

You can interact with a Amazon Neptune DB cluster after establishing network connectivity. If you have not set up access to your cluster yet, see [Connect to a cluster](get-started-connecting.md). The following sections describe the tools and query languages you can use to load data, run queries, and manage your graph.

## Tools for accessing Neptune
<a name="get-started-access-graph-tools"></a>

Neptune supports several tools for submitting queries and managing your graph data:
+ **AWS CLI**   –   Use the `aws neptunedata` commands to run Gremlin and openCypher queries, check engine status, manage bulk loads, and more. For more information, see [neptunedata](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/) in the AWS CLI Command Reference.
+ **AWS SDKs**   –   Use the Neptune Data API through the AWS SDKs to run queries programmatically. SDKs are available for [Gremlin](access-graph-gremlin-sdk.md) and [openCypher](access-graph-opencypher-sdk.md).
+ **`curl` and `awscurl`**   –   Use `curl` to submit HTTP requests directly to the Neptune endpoints. If IAM authentication is enabled, use [awscurl](https://github.com/okigan/awscurl) or `curl` 7.75.0\+ with the `--aws-sigv4` option to sign requests. For more information, see [Using `awscurl` with temporary credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl).
+ **Neptune notebooks**   –   Use Neptune notebooks to run interactive queries in a Jupyter environment with built-in visualizations. For more information, see [Using Neptune with graph notebooks](graph-notebooks.md).
+ **Drivers**   –   Connect using language-specific drivers for each query language. For Gremlin, use TinkerPop-compliant drivers available from the [Apache TinkerPop project](https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants). For openCypher, use Bolt protocol drivers as described in [Using the Bolt protocol](access-graph-opencypher-bolt.md). For SPARQL, use compatible tools such as RDF4J for Java as described in [Java](access-graph-sparql-java.md).

## Using a query language to access graph data in your Neptune DB cluster
<a name="get-started-access-graph-query-langs"></a>

Once you are connected, you can use the Gremlin and openCypher query languages to create and query a property graph, or the SPARQL query language to create and query a graph containing RDF data.

**Graph query languages supported by Neptune**
+ [Gremlin](access-graph-gremlin.md) is a graph traversal language for property graphs. A query in Gremlin is a traversal made up of discrete steps, each of which follows an edge to a node. See Gremlin documentation at [Apache TinkerPop](https://tinkerpop.apache.org/docs/current/reference/) for more information.

  The Neptune implementation of Gremlin has some differences from other implementations, especially when you are using Gremlin-Groovy (Gremlin queries sent as serialized text). For more information, see [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md).

  To get started, see [Using Gremlin](get-started-graph-gremlin.md).
+ [openCypher](access-graph-opencypher.md) is a declarative query language for property graphs that was originally developed by Neo4j, then open-sourced in 2015, and contributed to the [openCypher](http://www.opencypher.org/) project under an Apache 2 open-source license. Its syntax is documented in the [Cypher Query Language Reference, Version 9](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf).

  To get started, see [Using openCypher](get-started-graph-opencypher.md).
+ [SPARQL](access-graph-sparql.md) is a declarative query language for [RDF](https://www.w3.org/2001/sw/wiki/RDF) data, based on the graph pattern matching that is standardized by the World Wide Web Consortium (W3C) and described in [SPARQL 1.1 Overview](https://www.w3.org/TR/sparql11-overview/) and the [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) specification.

  To get started, see [Using SPARQL](get-started-graph-sparql.md).

**Note**  
You can access property graph data in Neptune using both Gremlin and openCypher, but not using SPARQL. Similarly, you can only access RDF data using SPARQL, not Gremlin or openCypher.