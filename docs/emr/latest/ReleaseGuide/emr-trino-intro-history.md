# Trino history and design

Trino is specialized for querying large datasets from many different sources. Trino can access and query HDFS in a traditional big-data use case, but it can also query additional sources
like relational databases and NoSQL databases. Trino originally started as a fork of the Presto query engine, in 2019. Since then, it has been developed independently from the Presto
code base.

For more information about the Trino query engine and how it's used, see the [Trino
website](https://trino.io/ "https://trino.io/"). To read the Trino source
documentation, see [Trino Overview](https://trino.io/docs/current/overview.html "https://trino.io/docs/current/overview.html").

## Architectural concepts

Trino can run quick and efficient queries because it processes data in parallel across a cluster. It's designed with querying a data lake in
mind, as it's specialized for queries on large data volumes, typically in use cases involving Hadoop and HDFS. But it can also query traditional relational
databases as well. For more information,
see [Architecture](https://trino.io/docs/current/overview/concepts.html#architecture "https://trino.io/docs/current/overview/concepts.html#architecture") in
the _Trino Documentation_.

### Components of Trino

Trino has a few key architecture components that work together to make queries run fast. It helps to have a working knowledge of these when you fine tune your cluster
for better performance:

- The **coordinator** is responsible for query orchestration. It parses and optimizes incoming
  SQL queries, generates execution plans, assigns tasks to worker nodes, and collects and assembles query results. Additionally, it monitors resource usage and tracks
  the status of worker nodes. For more information, see [Coordinator](https://trino.io/docs/current/overview/concepts.html#coordinator "https://trino.io/docs/current/overview/concepts.html#coordinator") in
  the _Trino documentation_.
- **Worker nodes** handle data processing for queries. After the coordinator assigns tasks,
  workers retrieve data, perform necessary operations, like joins and aggregations, and exchange intermediate data with other workers. For more information, see [Worker](https://trino.io/docs/current/overview/concepts.html#worker "https://trino.io/docs/current/overview/concepts.html#worker") in
  the _Trino documentation_.
- **Connectors** are plugins that allow Trino to connect with and query various data sources. Each
  connector knows how to access and retrieve data from its source, such as Amazon S3, Apache Hive, or relational databases. These connectors map source data to Trino’s
  schema structure.
- A **catalog** is a logical collection of schemas and tables associated with a specific
  connector. Defined in the coordinator, catalogs enable Trino to treat different data sources as a single namespace. This makes it so users can query
  multiple sources together, such as Hive and MySQL, in a unified way in the same query.
- **Clients** such as the Trino CLI connect by means of JDBC and ODBC drivers to the Trino coordinator to submit
  SQL queries. The coordinator manages the query lifecycle, providing results to the client for further analysis or reporting.

### Running queries

To understand how Trino takes SQL statements and runs them as queries,
see [Trino concepts](https://trino.io/docs/current/overview/concepts.html#query-execution-model "https://trino.io/docs/current/overview/concepts.html#query-execution-model") in the _Trino Documentation_.
