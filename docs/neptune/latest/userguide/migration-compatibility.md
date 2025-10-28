# Neptune compatibility with Neo4j

Neo4j's has an all-in-one architectural approach, where data loading, data ETL,
application queries, data storage, and management operations all occur in the same
set of compute resources, such as EC2 instances. Amazon Neptune is an OLTP-focused
open-specifications graph database where the architecture separates operations and
decouples resources so they can scale dynamically.

There are a variety of features and tooling in Neo4j, including third-party
tooling, that are not part of the openCypher specification, are incompatible with
openCypher, or are incompatible with Neptune's implementation of openCypher.
Below are listed some of the most common of these.

## Neo4j-specific features not present in Neptune

- **`LOAD CSV`**   –  
  Neptune has a different architectural approach to loading data than Neo4j.
  To allow for better scaling and cost optimization, Neptune implements a
  separation of concerns around resources, and recommends using one of the
  [AWS service integrations](integrations.md "integrations.md") such as
  AWS Glue to perform the required ETL processes to prepare data in a [format](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md") supported by the [Neptune bulk loader](bulk-load.md "bulk-load.md").

Another option is to do the same thing using application code
running on AWS compute resources such as Amazon EC2 instances, Lambda functions,
Amazon Elastic Container Service, AWS Batch jobs, and so on. The code could use either
Neptune's [HTTPS endpoint](access-graph-opencypher-queries.md "access-graph-opencypher-queries.md")
or [Bolt endpoint](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md").

- **Fine-grained access control**   –  
  Neptune supports granular access control over data-access actions
  [using IAM condition keys](iam-data-access-policies.md "iam-data-access-policies.md").
  Additional fine-grained access control can be implemented at the application layer.
- **Neo4j Fabric**   –  
  Neptune does support query federation across databases for RDF workloads
  using the SPARQL [SERVICE](sparql-service.md "sparql-service.md")
  keyword. Because there is not currently an open standard or specification
  for query federation for property graph workloads, that functionality would
  need to be implemented at the application layer.
- **Role-based access control (RBAC)**   –  
  Neptune manages authentication through the assignment of [IAM
  policies and roles](iam-auth.md "iam-auth.md"). IAM policies and roles provide an extremely
  flexible level of user management within an application, so it is worth reading
  and understanding the information in the [IAM
  overview](iam-auth.md "iam-auth.md") before configuring your cluster.
- **Bookmarking**   –  
  Neptune clusters consist of a single writer instance and up to 15 read-replica
  instances. Data written to the writer instance is ACID compliant and provides
  a strong consistency guarantee on subsequent reads. Read-replicas use the
  same storage volume as the writer instance and are eventually consistent,
  usually in less than 100ms from the time data is written. If your use
  case has an immediate need to guarantee read consistency of new writes,
  these reads should be directed to the cluster endpoint instead of the reader
  endpoint.
- **APOC procedures**   –  
  Because APOC procedures are not included in the openCypher specification,
  Neptune does not provide direct support for external procedures.
  Instead, Neptune relies on [integrations
  with other AWS services](integrations.md "integrations.md") to achieve similar end user
  functionality in a scalable, secure, and robust manner. Sometimes
  APOC procedures can be rewritten in openCypher or Gremlin, and
  some are not relevant to Neptune applications.

In general, APOC procedures fall into the categories below:

    + **[Import](https://neo4j.com/labs/apoc/4.2/import/ "https://neo4j.com/labs/apoc/4.2/import/")**   –  
     Neptune supports importing data using a variety of formats using query
     languages, the Neptune [bulk loader](bulk-load.md "bulk-load.md"), or
     as an target of [AWS Database Migration Service](dms-neptune.md "dms-neptune.md"). ETL operations
     on data may be performed using AWS Glue and the [`neptune-python-utils`](https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils "https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils")
     open-source package.
    + **[Export](https://neo4j.com/labs/apoc/4.2/export/ "https://neo4j.com/labs/apoc/4.2/export/")**   –  
     Neptune supports exporting data using the [neptune-export](neptune-data-export.md "neptune-data-export.md") utility,
     which supports a variety of common export formats and methods.
    + **[Database Integration](https://neo4j.com/labs/apoc/4.2/database-integration/ "https://neo4j.com/labs/apoc/4.2/database-integration/")**   –  
     Neptune supports integration with other databases using ETL tools
     such as AWS Glue or migrations tools such as the [AWS Database Migration Service](dms-neptune.md "dms-neptune.md").
    + **[Graph Updates](https://neo4j.com/labs/apoc/4.2/graph-updates/ "https://neo4j.com/labs/apoc/4.2/graph-updates/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Data Structures](https://neo4j.com/labs/apoc/4.2/data-structures/ "https://neo4j.com/labs/apoc/4.2/data-structures/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Temporal (Date Time)](https://neo4j.com/labs/apoc/4.2/temporal/ "https://neo4j.com/labs/apoc/4.2/temporal/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Mathematical](https://neo4j.com/labs/apoc/4.2/mathematical/ "https://neo4j.com/labs/apoc/4.2/mathematical/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Advanced Graph Querying](https://neo4j.com/labs/apoc/4.2/graph-querying/ "https://neo4j.com/labs/apoc/4.2/graph-querying/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Comparing Graphs](https://neo4j.com/labs/apoc/4.2/comparing-graphs/ "https://neo4j.com/labs/apoc/4.2/comparing-graphs/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.
    + **[Cypher Execution](https://neo4j.com/labs/apoc/4.2/cypher-execution/ "https://neo4j.com/labs/apoc/4.2/cypher-execution/")**   –  
     Neptune supports a rich set of features for updating property-graph
     data through its support for both the openCypher and the Gremlin query
     languages. See [Cypher rewrites](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md") for examples
     of rewrites of commonly used procedures.

- **Custom procedures**   –  
  Neptune does not support custom procedures created by users. This functionality
  would have to be implemented at the application layer.
- **Geospatial**   –  
  Although Neptune doesn't provide native support for geospatial features,
  similar functionality can be achieved through integration with other AWS
  services, as shown in this blog post: [Combine
  Amazon Neptune and Amazon OpenSearch Service for geospatial queries](https://aws.amazon.com/blogs/database/combine-amazon-neptune-and-amazon-opensearch-service-for-geospatial-queries/ "https://aws.amazon.com/blogs/database/combine-amazon-neptune-and-amazon-opensearch-service-for-geospatial-queries/")
  by Ross Gabay and Abhilash Vinod (1 February 2022).
- **Graph Data Science**   –  
  Neptune supports graph analytics today through [Neptune
  Analytics](../../../neptune-analytics/latest/userguide/what-is-neptune-analytics.md "../../../neptune-analytics/latest/userguide/what-is-neptune-analytics.md"), a memory-optimized engine that supports a library of graph
  analytic algorithms.

Neptune also provides an integration with the [AWS
Pandas SDK](https://github.com/amazon-archives/fully-automated-neo4j-to-neptune "https://github.com/amazon-archives/fully-automated-neo4j-to-neptune") and several [sample
notebooks](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/05-Data-Science "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks/05-Data-Science") that show how to leverage this integration within Python
environments to run analytics on graph data.

- **Schema Constraints**   –  
  Within Neptune, the only schema constraint available is the uniqueness of the ID
  of a node or edge. There is no feature to specify any additional schema constraints,
  or any additional uniqueness or value constraints on an element in the graph.
  ID values in Neptune are strings and may be set using Gremlin, like this:

```
g.addV('person').property(id, '1') )
```

Applications that need to leverage the ID as a uniqueness constraint are
encouraged to try this approach for achieving a uniqueness constraint. If the
application used multiple columns as a uniqueness constraint, the ID may be set
to a combination of these values. For example `id=123, code='SEA'`
could be represented as `ID='123_SEA'` to achieve a complex uniqueness
constraint.

- **Multi-tenancy**   –  
  Neptune only supports a single graph per cluster. To build a multi-tenant
  system using Neptune, either use multiple clusters or logically partition
  the tenants within a single graph and use application-side logic to enforce
  separation. For example, add a property `tenantId` and include it
  in each query, like this:

```
MATCH p=(n {tenantId:1})-[]->({tenantId:1}) RETURN p LIMIT 5)
```

[Neptune Serverless](neptune-serverless.md "neptune-serverless.md") makes it
relatively easy to implement multi-tenancy using multiple DB clusters, each of
which is scaled independently and automatically as needed.

## Neptune support for Neo4j tools

Neptune provides the following alternatives to Neo4j tools:

- **[Neo4j Browser](https://neo4j.com/docs/operations-manual/current/installation/neo4j-browser/ "https://neo4j.com/docs/operations-manual/current/installation/neo4j-browser/")**   –  
  Neptune provides open-source [graph notebooks](graph-notebooks.md "graph-notebooks.md")
  that provide a developer-focused IDE for running queries and visualizing the results.
- **[Neo4j Bloom](https://neo4j.com/product/bloom/ "https://neo4j.com/product/bloom/")**   –  
  Neptune supports rich graph visualizations using [third-party
  visualization solutions](visualization-tools.md "visualization-tools.md") such as Graph-explorer, Tom Sawyer, Cambridge Intelligence,
  Graphistry, metaphacts, and G.V().
- **[GraphQL](https://graphql.org/ "https://graphql.org/")**   –  
  Neptune currently supports GraphQL though custom AWS AppSync integrations.
  See the [Build
  a graph application with Amazon Neptune and AWS Amplify](https://aws.amazon.com/blogs/database/build-a-graph-application-with-amazon-neptune-and-aws-amplify/ "https://aws.amazon.com/blogs/database/build-a-graph-application-with-amazon-neptune-and-aws-amplify/") blog post, and
  the example project, [Building
  Serverless Calorie tracker application with AWS AppSync and Amazon Neptune](https://github.com/aws-samples/aws-appsync-calorie-tracker-workshop "https://github.com/aws-samples/aws-appsync-calorie-tracker-workshop").
- **[NeoSemantics](https://neo4j.com/labs/neosemantics/4.0/ "https://neo4j.com/labs/neosemantics/4.0/")**   –  
  Neptune natively supports the RDF data model, so customers wishing to run RDF workloads are advised to use
  Neptune's RDF model support.
- **[Arrows.app](https://arrows.app/ "https://arrows.app/")**   –  
  The Cypher created when exporting the model using the export command is compatible with Neptune.
- **[Linkurious Ogma](https://doc.linkurious.com/ogma/latest/ "https://doc.linkurious.com/ogma/latest/")**   –  
  A sample integration with Linkurious Ogma is [available
  here](https://github.com/aws-samples/amazon-neptune-samples/tree/master/gremlin/ogma-neptune "https://github.com/aws-samples/amazon-neptune-samples/tree/master/gremlin/ogma-neptune").
- **[Spring Data Neo4j](https://spring.io/projects/spring-data-neo4j "https://spring.io/projects/spring-data-neo4j")**   –  
  This is not currently compatible with Neptune.
- **[Neo4j Spark Connector](https://neo4j.com/docs/spark/current/ "https://neo4j.com/docs/spark/current/")**   –  
  The Neo4j spark connector can be used within a Spark Job to connect to Neptune using openCypher.
  Here is some sample code and application configuration:

**Sample code:**

```
SparkSession spark = SparkSession
            .builder()
            .config("encryption.enabled", "true")
            .appName("Simple Application").config("spark.master", "local").getOrCreate();

Dataset<Row> df = spark.read().format("org.neo4j.spark.DataSource")
            .option("url", "bolt://`(your cluster endpoint)`:8182")
            .option("encryption.enabled", "true")
            .option("query", "MATCH (n:airport) RETURN n")
            .load();

System.out.println("TOTAL RECORD COUNT: " + df.count());
spark.stop();

```

**Application configuration:**

```
<dependency>
    <groupId>org.neo4j</groupId>
    <artifactId>neo4j-connector-apache-spark_2.12-4.1.0</artifactId>
    <version>4.0.1_for_spark_3</version>
</dependency>
```

### Neo4j features and tools not listed here

If you are using a tool or feature that is not listed here,
we are unsure of its compatibility with Neptune or other services
within AWS. Please reach out to AWS support or engage your
account team if you have further questions.
