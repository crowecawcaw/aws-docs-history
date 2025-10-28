# Best practice 15.6 – Prevent unnecessary data movement between systems and applications

Moving data around your organization can be very costly as
it requires compute, networking, and storage resources. This
can be particularly costly for analytics workloads as they
generally require large quantities of information. When
businesses move data around their organization, they
increase the risk of creating duplicate data, which can
impact your storage resource.

At the same time, making multiple copies of data can also reduce the overall amount of data transferred from each access to the data. When designing your data platform, consider the overall environmental impact and make informed choices about when and when not to duplicate data.

**How does your organization mitigate
the unnecessary data movement from one part of your
organization to another?**

## Suggestion 15.6.1 – Implement data virtualization techniques to query information where the data resides

In data virtualization, only the data that is required to service the request is copied from the source location into the data virtualization layer and temporarily cached in memory. This data is then used to service the user’s request. By copying the most frequently used parts of the data set closer to the compute instances, overhead associated with data movement is reduced, and the query processing has more efficient access to the data.

For more details, refer to the following information:

- Use Amazon Athena for data
  virtualization:
  [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc")
- Running Presto and Trino on Amazon EMR:
  [Presto
  and Trino](../../../emr/latest/ReleaseGuide/emr-presto.md "../../../emr/latest/ReleaseGuide/emr-presto.md")

## Suggestion 15.6.2 – Reduce the ﬂow of data between application and database by implementing predicates pushdown

Filtering data by pushing down predicates as close to the storage as possible reduces the amount of data that upstream systems need to process. Query engines like Amazon Athena have query planners that leverage predicate pushdown where possible. For example, when using columnar file formats like Parquet and ORC, Athena can use metadata stored in the files to determine which sections of the files to read, effectively pushing down some predicates to the storage layer. Similarly, when querying a federated data source, Athena can push down some, but not all, predicates into the source systems. This reduces the amount of data that needs to be transferred from the source system into the query engine itself. Research the query engine you use to determine under which circumstances it is able to perform predicate pushdown, and leverage this in your application.

For more details, refer to the following information:

- Use pushdown predicated with Amazon Athena:
  [Top
  10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/")
- Optimizing EMR Spark with leveraging pushdown
  predicates:
  [Optimize
  Spark performance](../../../emr/latest/ReleaseGuide/emr-spark-performance.md "../../../emr/latest/ReleaseGuide/emr-spark-performance.md")

## Suggestion 15.6.3 – Prevent data movement by leveraging pre-calculated materialized views

A materialized view can reduce the amount of data shared
between your data warehouse and reporting layers by
pre-computing the results of a pre-defined query.
Materialized views are especially useful for speeding up
queries that are predictable and repeated. Instead of
performing resource-intensive queries against large tables
(such as aggregates or multiple joins), applications can
query a materialized view and retrieve a precomputed
result set, therefore, saving on compute resource and
reducing an organization’s analytics environmental impact.

Where materialized views are not available, you can use operations such as CREATE TABLE AS (CTAS) to create pre-computed versions of queries.

For more details, refer to the following information:

- Amazon Redshift:
  [Creating
  materialized views in Amazon Redshift](../../../redshift/latest/dg/materialized-view-overview.md "../../../redshift/latest/dg/materialized-view-overview.md")
- Amazon Athena: [Creating a table from query results (CTAS)](../../../athena/latest/ug/ctas.md "../../../athena/latest/ug/ctas.md")

## Suggestion 15.6.4 – Reduce the flow of data between an operational database and a data warehouse by using federated querying

A federated query allows you to directly
query data stored in external databases without data movement. This allows data
analysts, engineers, and data scientists to perform SQL
queries across data stored in relational, non-relational,
object, and custom data sources.  With federated querying,
you can submit a single SQL query and analyze data from
multiple sources running on premises or hosted in the
cloud, which reduces data latency in reporting. Federated
querying can reduce the amount of information shared
between data stores, however, the sustainability trade-off
is that your organization could transfer the same
information multiple times rather than a once-off single
bulk copy of all information on a daily basis. Your
organization should frequently review your federated
querying patterns to identify whether it’s more
sustainable to use federated query or single bulk copies.
To do this, your organization could review the amount of
data that has been queried in a week, versus calculating
the size of a full extract, and implement the approach
that processes the least amount of data.

For more details, refer to the following information:

- Amazon Redshift:
  [Querying
  data with federated queries in Amazon Redshift](../../../redshift/latest/dg/federated-overview.md "../../../redshift/latest/dg/federated-overview.md")
- Amazon Athena:
  [Using
  Amazon Athena Federated Query](../../../athena/latest/ug/connect-to-a-data-source.md "../../../athena/latest/ug/connect-to-a-data-source.md")

## Suggestion 15.6.5 – Decrease the amount of data duplication between Amazon Redshift clusters by using data sharing

Data sharing allows an administrator to share databases, tables, and views from one Amazon Redshift cluster to another cluster without copying the underlying data. The consumer cluster can query live data, meaning changes made on the producer cluster reflect immediately on the consumer cluster. This removes the need to create, store, and keep copies of data sets up-to-date.

For more details, refer to the following information:

- Amazon Redshift:
  [Amazon Redshift Data Sharing](https://aws.amazon.com/redshift/features/data-sharing/ "https://aws.amazon.com/redshift/features/data-sharing/")
