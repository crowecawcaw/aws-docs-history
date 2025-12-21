# Running SQL queries

###### Note

You can only run queries if the member who is responsible to pay for query compute costs
has joined the collaboration as an active member.

As the [member who can query](glossary.md#glossary-member-who-can-query "glossary.md#glossary-member-who-can-query"), you can run a SQL
query by:

- Building a SQL query manually using the SQL code editor.
- Using an approved SQL [analysis template](create-analysis-template.md "create-analysis-template.md").
- Using the **Analysis builder UI** to build a query without having to
  write SQL code.
  When the member who can query runs a SQL query on the tables in the collaboration,
  AWS Clean Rooms assumes the relevant roles to access the tables on their behalf. AWS Clean Rooms applies
  the analysis rules as necessary to the input query and its output.

The analysis rules and output constraints are enforced automatically. AWS Clean Rooms only
returns the results that comply with the defined analysis rules.

AWS Clean Rooms supports SQL queries that can be different than other query engines. For
specifications, see the [AWS Clean Rooms SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md"). If you want to run queries on data tables
protected with differential privacy, you should ensure that your queries are compatible with
the [general-purpose query structure](analysis-rules-custom.md#dp-query-structure-syntax "analysis-rules-custom.md#dp-query-structure-syntax") of AWS Clean Rooms
Differential Privacy.

###### Note

When using [Cryptographic Computing for Clean Rooms](crypto-computing.md "crypto-computing.md"), not all SQL operations generate valid results. For example, you can
conduct a COUNT on an encrypted column but conducting a SUM on
encrypted numbers leads to errors. In addition, queries might also yield incorrect results.
For example, queries that SUM sealed columns produce errors. However, a
GROUP
BY query over sealed columns seems to succeed but produces different groups
than those produced by a GROUP
BY query over the cleartext.

The [member paying for query compute
costs](glossary.md#glossary-member-paying-for-query-compute "glossary.md#glossary-member-paying-for-query-compute") is charged for the queries run in the collaboration.

The member who can query can select multiple [members who can receive
results](glossary.md#glossary-member-who-can-receive-results "glossary.md#glossary-member-who-can-receive-results") to receive the results from a single query. For more information, see [Querying configured tables using the SQL code
editor](use-sql-editor.md "use-sql-editor.md"). For general information about
receiving query results, see [Receiving and using analysis results](receive-query-results.md "receive-query-results.md").

## Prerequisites

Before you run a SQL query, make sure that you have the following:

- An active membership in AWS Clean Rooms collaboration
- Access to at least one configured table in the collaboration
- Confirmation that the member responsible for query compute costs is an active
  collaboration member

For information about how to query data or view queries by calling the AWS Clean Rooms [StartProtectedQuery API](../apireference/API_StartProtectedQuery.md "../apireference/API_StartProtectedQuery.md") operation directly or by using the AWS SDKs, see the
[AWS Clean Rooms
API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

For information about query logging, see [Analysis logging in AWS Clean Rooms](query-logs.md "query-logs.md").

###### Note

If you run a query on [encrypted](glossary.md#glossary-encryption "glossary.md#glossary-encryption") data tables, the results from the
encrypted columns are encrypted.

## Spark properties configuration for SQL queries

AWS Clean Rooms enables you to optionally customize Spark runtime behavior by configuring
supported Spark properties for SQL queries. These properties let you fine-tune performance, memory usage,
and query execution parameters. With this feature, you have greater control over how your
Spark-based queries
are
processed, allowing for optimization based on your specific workload requirements.

You can now adjust settings such as shuffle partitions, broadcast join thresholds, and
adaptive query execution parameters directly from the AWS Clean Rooms console. This feature is particularly useful for complex queries or large datasets
where default configurations may not be optimal. By fine-tuning these Spark properties, you
can potentially improve query performance, reduce resource consumption, and better manage
memory usage for your Spark-based collaboration analyses.

To leverage this feature, you'll find a new **Spark properties**
section in the query interface. You can select from a
list of supported properties and specify custom values. You can also configure Spark
properties programmatically using the [StartProtectedQuery API.](../apireference/API_StartProtectedQuery.md "../apireference/API_StartProtectedQuery.md") This advanced configuration option empowers data
analysts and engineers to optimize their queries for enhanced efficiency and scalability.

For more information about Spark properties, including default values, see [Spark
Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties "https://spark.apache.org/docs/latest/configuration.html#spark-properties") in the Apache Spark documentation.

The following topics explain how to query data in a collaboration using the AWS Clean Rooms
console.

###### Topics

- [Querying configured tables using the SQL code
  editor](use-sql-editor.md "use-sql-editor.md")
- [Querying ID mapping tables using the SQL code
  editor](query-id-mapping-tables.md "query-id-mapping-tables.md")
- [Querying configured tables using a SQL analysis
  template](use-analysis-template.md "use-analysis-template.md")
- [Querying with the analysis builder](query-data-analysis-builder.md "query-data-analysis-builder.md")
- [Viewing the impact of differential
  privacy](query-data-with-diff-privacy.md "query-data-with-diff-privacy.md")
- [Viewing recent queries](view-queries-console.md "view-queries-console.md")
- [Viewing query details](view-query-details.md "view-query-details.md")
