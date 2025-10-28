# Integration with Amazon OpenSearch Service

Ingestion pipeline

**Integration type:**Subscriber, Source

Amazon OpenSearch Service Ingestion is a fully managed, serverless data collector that streams
logs, metrics, and trace data to OpenSearch Service and Security Lake.

**Send data to Security Lake using OpenSearch Ingestion pipeline**

You can use an Amazon Simple Storage Service (Amazon S3) sink plugin in OpenSearch Ingestion to
send data from any supported source to Security Lake.
Security Lake automatically centralizes security data
from AWS environments, on-premises environments, and SaaS providers
into a purpose-built data lake. For more information, see
[Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a sink](../../../opensearch-service/latest/developerguide/configure-client-sink-security-lake.md "../../../opensearch-service/latest/developerguide/configure-client-sink-security-lake.md").

**Send data from Security Lake to OpenSearch using OpenSearch
Ingestion pipeline**

You can use an Amazon S3 source plugin to ingest data into your OpenSearch
Ingestion pipeline. For more information, see
[Using
an OpenSearch Ingestion pipeline with Amazon Security Lake as a source](../../../opensearch-service/latest/developerguide/configure-client-source-security-lake.md "../../../opensearch-service/latest/developerguide/configure-client-source-security-lake.md").
