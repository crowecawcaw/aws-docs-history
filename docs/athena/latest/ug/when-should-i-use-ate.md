# When should I use Athena?

Query services like Amazon Athena, data warehouses like Amazon Redshift, and sophisticated
data processing frameworks like Amazon EMR all address different needs and use cases. The
following guidance can help you choose one or more services based on your
requirements.

## Amazon Athena

Athena helps you analyze unstructured, semi-structured, and structured data stored
in Amazon S3. Examples include CSV, JSON, or columnar data formats such as Apache Parquet
and Apache ORC. You can use Athena to run ad-hoc queries using ANSI SQL, without the
need to aggregate or load the data into Athena.

Athena integrates with Amazon Quick for easy data visualization. You can use Athena to
generate reports or to explore data with business intelligence tools or SQL clients
connected with a JDBC or an ODBC driver. For more information, see [What is
Amazon Quick](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") in the _Amazon Quick User Guide_ and [Connect to Amazon Athena with ODBC and JDBC drivers](athena-bi-tools-jdbc-odbc.md "athena-bi-tools-jdbc-odbc.md").

Athena integrates with the AWS Glue Data Catalog, which offers a persistent metadata store
for your data in Amazon S3. This allows you to create tables and query data in Athena
based on a central metadata store available throughout your Amazon Web Services account and
integrated with the ETL and data discovery features of AWS Glue. For more
information, see [Use AWS Glue Data Catalog to connect to your data](data-sources-glue.md "data-sources-glue.md") and
[What is
AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") in the _AWS Glue Developer Guide_.

Amazon Athena makes it easy to run interactive queries against data directly in Amazon S3
without having to format data or manage infrastructure. For example, Athena is useful
if you want to run a quick query on web logs to troubleshoot a performance issue on
your site. With Athena, you can get started fast: you just define a table for your
data and start querying using standard SQL.

You should use Amazon Athena if you want to run interactive ad hoc SQL queries against
data on Amazon S3, without having to manage any infrastructure or clusters. Amazon Athena
provides the easiest way to run ad hoc queries for data in Amazon S3 without the need to
setup or manage any servers.

For a list of AWS services that Athena leverages or integrates with, see [AWS service integrations with Athena](athena-aws-service-integrations.md "athena-aws-service-integrations.md").

## SageMaker Unified Studio

Amazon SageMaker Unified Studio makes it simple to work with Amazon Athena and Amazon Redshift to run SQL queries
on SageMaker Lakehouse data. With Unified Studio, you can develop SQL queries, work
with query results, and collaborate with your team through an integrated notebook
environment. You can also use Amazon Q generative SQL to generate SQL code from
natural language input. To learn more, see [SQL Analytics](../../../sagemaker-unified-studio/latest/userguide/sql-query.md "../../../sagemaker-unified-studio/latest/userguide/sql-query.md") in the SageMaker Unified Studio user guide.

## Amazon EMR

Amazon EMR makes it simple and cost effective to run highly distributed processing
frameworks such as Hadoop, Spark, and Presto when compared to on-premises
deployments. Amazon EMR is flexible – you can run custom applications and code,
and define specific compute, memory, storage, and application parameters to optimize
your analytic requirements.

In addition to running SQL queries, Amazon EMR can run a wide variety of scale-out data
processing tasks for applications such as machine learning, graph analytics, data
transformation, streaming data, and virtually anything you can code. You should use
Amazon EMR if you use custom code to process and analyze extremely large datasets with
the latest big data processing frameworks such as Spark, Hadoop, Presto, or Hbase.
Amazon EMR gives you full control over the configuration of your clusters and the
software installed on them.

You can use Amazon Athena to query data that you process using Amazon EMR. Amazon Athena
supports many of the same data formats as Amazon EMR. Athena's data catalog is Hive
metastore compatible. If you use EMR and already have a Hive metastore, you can run
your DDL statements on Amazon Athena and query your data immediately without affecting
your Amazon EMR jobs.

## Amazon Redshift

A data warehouse like Amazon Redshift is your best choice when you need to pull together data
from many different sources – like inventory systems, financial systems, and
retail sales systems – into a common format, and store it for long periods of
time. If you want to build sophisticated business reports from historical data, then
a data warehouse like Amazon Redshift is the best choice. The query engine in Amazon Redshift has been
optimized to perform especially well on running complex queries that join large
numbers of very large database tables. When you need to run queries against highly
structured data with lots of joins across lots of very large tables, choose
Amazon Redshift.

For more information about when to use Athena, consult the following resources:

- [Decision guide for analytics services on AWS](https://aws.amazon.com/getting-started/decision-guides/analytics-on-aws-how-to-choose/ "https://aws.amazon.com/getting-started/decision-guides/analytics-on-aws-how-to-choose/") in the _Getting Started Resource Center_
- [When to use
  Athena vs other big data services](https://aws.amazon.com/athena/faqs/#When_to_use_Athena_vs_other_big_data_services "https://aws.amazon.com/athena/faqs/#When_to_use_Athena_vs_other_big_data_services") in the _Amazon Athena FAQs_
- [Amazon Athena overview](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
- [Amazon Athena features](https://aws.amazon.com/athena/features/ "https://aws.amazon.com/athena/features/")
- [Amazon Athena FAQs](https://aws.amazon.com/athena/faqs/ "https://aws.amazon.com/athena/faqs/")
- [Amazon Athena blog
  posts](https://aws.amazon.com/athena/resources/#Blog_posts "https://aws.amazon.com/athena/resources/#Blog_posts")
