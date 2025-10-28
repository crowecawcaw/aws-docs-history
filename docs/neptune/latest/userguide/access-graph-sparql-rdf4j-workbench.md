# Using RDF4J Workbench to connect to a

Neptune DB instance

This section walks you through connecting to an Amazon Neptune DB instance using RDF4J Workbench
and RDF4J Server. RDF4J Server is required because it acts as a proxy between the Neptune
SPARQL HTTP REST endpoint and RDF4J Workbench.

RDF4J Workbench provides an easy interface for experimenting with a graph, including
loading local files. For information, see the [Add section](https://rdf4j.org/documentation/tools/server-workbench/#add "https://rdf4j.org/documentation/tools/server-workbench/#add") in the RDF4J
documentation.

###### Prerequisites

Before you begin, do the following:

- Install Java 1.8 or later.
- Install RDF4J Server and RDF4J Workbench. For information, see [Installing RDF4J Server and RDF4J Workbench](https://rdf4j.org/documentation/tools/server-workbench/#installing-rdf4j-server-and-rdf4j-workbench "https://rdf4j.org/documentation/tools/server-workbench/#installing-rdf4j-server-and-rdf4j-workbench").

###### To use RDF4J Workbench to connect to Neptune

1. In a web browser, navigate to the URL where the RDF4J Workbench web app is deployed.
   For example, if you are using Apache Tomcat, the URL is: [https://`ec2_hostname`:8080/rdf4j-workbench/](http://localhost:8080/rdf4j-workbench/ "http://localhost:8080/rdf4j-workbench/").
2. If you are asked to **Connect to RDF4J Server**, verify that
   **RDF4J Server** is installed, running, and that the server URL is
   correct. Then, proceed to the next step.
3. In the left pane, choose **New repository**.

In **New repository**:

    * In the **Type** drop-down list, choose **SPARQL endpoint
     proxy**.
    * For **ID**, type **neptune**.
    * For **Title**, type **Neptune DB instance**.

Choose **Next**. 4. In **New repository**:

    * For **SPARQL query endpoint URL**, type
     `https://`your-neptune-endpoint`:`port`/sparql`.
    * For **SPARQL update endpoint URL**, type
     `https://`your-neptune-endpoint`:`port`/sparql`.

For information about finding the address of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

Choose **Create**. 5. The **neptune** repository now appears in the list of repositories.
It might take a few minutes before you can use the new repository. 6. In the **Id** column of the table, choose the
**neptune** link. 7. In the left pane, choose **Query**.

###### Note

If the menu items under **Explore** are disabled, you might need to
reconnect to the RDF4J Server and choose the **neptune** repository
again.

You can do this by using the **[change]** links in the upper-right
corner. 8. In the query field, type the following SPARQL query, and then choose
**Execute**.

```
select ?s ?p ?o where {?s ?p ?o} limit 10
```

The preceding example returns up to 10 of the triples (subject-predicate-object) in the
graph by using the `?s ?p ?o` query with a limit of 10.
