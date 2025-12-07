# Vector ingestion

Vector ingestion helps you quickly ingest and index OpenSearch domains and OpenSearch Serverless
collections. The service examines your domain or collection and creates an ingestion
pipeline on your behalf to load your data into OpenSearch. The ingestion and indexing of
your domain or collection are managed for you by Vector ingestion.

You can accelerate and optimize the indexing process by enabling [GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md "gpu-acceleration-vector-index.md")
and [Auto-optimize](serverless-auto-optimize.md "serverless-auto-optimize.md") features. With Vector
ingestion, you don't need to manage the underlying infrastructure, patch software, or scale
clusters to support your vector database indexing and ingestion. This allows you to quickly
build your vector database to meet your needs.

## How it works

Vector ingestion examines your domain or collection and their index. You can manually
configure your vector index fields or allow OpenSearch to use automatic
configuration.

Vector ingestion uses OpenSearch Ingestion (OSI) as the data pipeline between Amazon S3
and OpenSearch. The service processes vectors in parallel to optimize ingestion speed
while respecting the scaling limits of both OSI and OpenSearch.

## OpenSearch Vector ingestion

pricing

At any specific time, you only pay for the number of vector ingestion OCUs that are
allocated to a pipeline, regardless of whether there's data flowing through the
pipeline. OpenSearch vector ingestion immediately accommodates your workloads by
scaling pipeline capacity up or down based on usage.

For full pricing details, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## Prerequisites

Before using vector ingestion, ensure you have the following resources:

- Amazon S3 bucket containing your OpenSearch JSON documents in parquet format
- OpenSearch resource - either a domain or collection
- OpenSearch version `2.19` or later (required for auto-optimize
  integration)

## Create vector database

Use the vector ingestion job creation workflow to set up automated vector index
tuning and accelerate large-scale index builds.

###### Note

The procedural content in this section is subject to change as the user interface
is finalized. The workflow may be updated in future releases to reflect the latest
console experience.

###### To create a vector injection job

1. In the **Vector ingestion job details** section,
   for **Name**, enter a name for your ingestion
   job.
2. In the **Data source** section, configure the
   following:
   1. For **Amazon S3 URI**, enter the Amazon S3 bucket
      location containing your OpenSearch Service JSON documents.
   2. Choose **Browse Amazon S3** to select from
      available buckets, or choose **View** to
      preview the bucket contents.
   3. For **Content type**, select one of the
      following:
      - **Vectors** - Documents already
        contain vectors and doesn't require further vector embedding
        generation.
      - **Text, image, or audio** -
        Documents contain content such as text, images or audio bytes
        that need to be encoded into vector embeddings.

3. In the **Data source permissions** section,
   configure access permissions:
   1. For **IAM role**, choose one of the
      following:
      - **Create a new role**
      - **Use an existing role**

   2. For **IAM role name**, enter a name for
      the role.

4. In the **Destination** section, configure the
   OpenSearch Service endpoint:
   1. For **Endpoint**, choose **Choose an option** to select from your
      compatible domains or collections in the current region.
   2. Choose **Next** to proceed with the
      selected endpoint.

5. Choose **Next** to continue to the next step, or
   choose **Cancel** to exit without saving.

## Related features

Vector ingestion works with the following Amazon OpenSearch Service features to optimize your vector
database performance:

[GPU-acceleration for vector indexing](gpu-acceleration-vector-index.md "gpu-acceleration-vector-index.md")

GPU-acceleration reduces the time needed to create, update, and delete vector
indexes. When used with vector ingestion, you can significantly accelerate
the ingestion and indexing process for large-scale vector databases.

[Auto-optimize](serverless-auto-optimize.md "serverless-auto-optimize.md")

Auto-optimize automatically discovers optimal trade-offs between search
latency, quality, and memory requirements. Vector ingestion can apply
auto-optimize recommendations during the ingestion process to ensure your
vector indexes are optimally configured.

For best results, consider enabling both GPU-acceleration and Auto-optimize when using vector
ingestion to build large-scale vector databases.
