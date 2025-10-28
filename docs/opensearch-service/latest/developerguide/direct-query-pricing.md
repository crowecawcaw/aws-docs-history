# Direct query pricing

When you use OpenSearch Service direct queries, you'll incur separate charges for OpenSearch Service and the
resources used to process and store your data on Amazon S3, Amazon CloudWatch Logs, and Amazon Security Lake. As you
run direct queries, you'll see charges for OpenSearch Compute Units (OCUs) per hour,
listed as DirectQuery OCU usage type on your bill.

Direct queries are of two types—interactive and indexed view queries.

- _Interactive queries_ are used to populate
  the data selector and perform analytics on your data in S3, CloudWatch Logs, or Security Lake.

For Amazon S3 direct queries, when you run a new query from Discover, OpenSearch Service starts
a new session that lasts for a minimum of three minutes. OpenSearch Service keeps this
session active to ensure that subsequent queries run quickly.

For CloudWatch Logs and Security Lake queries, OpenSearch Service handles each query with a separate
pre-warmed job, without maintaining an extended session.

- _Indexed view queries_ use compute to
  maintain indexed views in OpenSearch Service. These queries usually take longer because they
  ingest a varying amount of data into a named index. By indexing data, you can
  make future interactive queries run faster or unlock advanced analytics
  capabilities such as dashboards or alerts, which require an index to
  reference.

For Amazon S3 data sources, the indexed data is stored in a domain based on an
instance type purchased. For CloudWatch Logs and Security Lake connected data sources, the indexed
data is stored in an OpenSearch Serverless collection where you are charged for
data indexed (IndexingOCU), data searched (SearchOCU), and data stored in
GB.
For more information, see the Direct Query and Serverless sections within [Amazon OpenSearch Service
Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").
