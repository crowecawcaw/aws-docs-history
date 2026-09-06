

# Using an OpenSearch Ingestion pipeline with Amazon Security Lake
<a name="configure-client-security-lake"></a>

You can use the [S3 source plugin](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/) to ingest data from [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) into your OpenSearch Ingestion pipeline. Security Lake automatically centralizes security data from AWS environments, on-premises environments, and SaaS providers into a purpose-built data lake. You can create a subscription that replicates data from Security Lake to your OpenSearch Ingestion pipeline, which then writes it to your OpenSearch Service domain or OpenSearch Serverless collection.

To configure your pipeline to read from Security Lake, use the preconfigured Security Lake blueprint. The blueprint includes a default configuration for ingesting Open Cybersecurity Schema Framework (OCSF) parquet files from Security Lake. For more information, see [Working with blueprints](pipeline-blueprint.md).

**Topics**
+ [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a source](configure-client-source-security-lake.md)
+ [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a sink](configure-client-sink-security-lake.md)