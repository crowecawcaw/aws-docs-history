# Integration with

Amazon OpenSearch Service zero-ETL direct query

**Integration type:** Subscriber (Query)

You can use OpenSearch Service direct query to analyze data in Amazon Security Lake. OpenSearch Service provides
zero-ETL integration as a way to directly query your data in Security Lake using OpenSearch
SQL or OpenSearch Piped Processing Language (PPL) without incurring the friction of
building ingestion pipelines or switching between analytics tools. This approach
eliminates the need for data movement or duplication, allowing you to analyze your
data where it rests using the Discover experience in OpenSearch Service Dashboards.
When you want to switch from querying data at rest to actively monitoring with
dashboards, you can build indexed views on your query results and ingest it into an
OpenSearch Service index. For more information on direct queries, see [Working
with direct queries](../../../opensearch-service/latest/developerguide/direct-query-s3.md "../../../opensearch-service/latest/developerguide/direct-query-s3.md") in the _Amazon OpenSearch Service Developer Guide_.

OpenSearch Service uses a OpenSearch Serverless collection to directly query the data in Security Lake
and store your indexed views. To do this, you create a data source that enables you
to use OpenSearch zero-ETL capabilities on Security Lake data. When you create a data source
you can directly search, gain insights from, and analyze data stored in Security Lake. You
can accelerate your query performance and use advanced OpenSearch analytics on
select Security Lake data sets using on-demand indexing.

- For details about creating the OpenSearch Service data source integration, see
  [Creating an Amazon Security Lake data source integration](../../../opensearch-service/latest/developerguide/direct-query-security-lake-creating.md "../../../opensearch-service/latest/developerguide/direct-query-security-lake-creating.md") in the
  _Amazon OpenSearch Service Developer Guide_.
- For details about configuring Security Lake data source in OpenSearch Service,
  see [Configuring a Security Lake data source in OpenSearch Service
  Dashboards](../../../opensearch-service/latest/developerguide/direct-query-security-lake-configure.md "../../../opensearch-service/latest/developerguide/direct-query-security-lake-configure.md") in the _Amazon OpenSearch Service Developer Guide_.
  For more information about using OpenSearch Service with Security Lake, use the following
  resources.

- [Introducing Amazon OpenSearch Service and Amazon Security Lake integration to simplify security analytics](https://aws.amazon.com/blogs//aws/introducing-amazon-opensearch-service-zero-etl-integration-for-amazon-security-lake/ "https://aws.amazon.com/blogs//aws/introducing-amazon-opensearch-service-zero-etl-integration-for-amazon-security-lake/")
- Introduction to zero-ETL on OpenSearch Service with Amazon Security Lake
