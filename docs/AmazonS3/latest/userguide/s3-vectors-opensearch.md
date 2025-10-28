# Using S3 Vectors with OpenSearch Service

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Amazon S3 Vectors integrates with OpenSearch to provide flexible vector storage and
search capabilities. This integration allows you to optimize costs by storing vectors in
S3 Vectors while leveraging the advanced search features of OpenSearch.

There are two integrations between S3 Vectors and OpenSearch. One is to export vector
data from S3 Vectors to OpenSearch Serverless for high-performance search capabilities. The
other uses S3 Vectors as a cost-effective storage engine within OpenSearch while maintaining
access to OpenSearch functionality.

## Export to OpenSearch Serverless

You can export vector indexes from S3 Vectors to OpenSearch Serverless collections for
high-performance search operations, hybrid search, aggregations, advanced filtering, and
faceted search. When you export, the data is copied to OpenSearch Serverless while remaining
in S3 Vectors, which means you'll be paying for both services during this time.

### When to use this integration

Consider exporting to OpenSearch Serverless from S3 Vectors when you need the following:

- **Hybrid search capabilities** that combine vector
  similarity with keyword search.
- **High query throughput** for demanding
  workloads.
- **Low-latency responses** for real-time applications
  that require millisecond response times.
- **Advanced analytics** that include aggregations,
  faceted search, and complex filtering.

### Prerequisites

Before using S3 Vectors with OpenSearch, ensure you have the following:

- An existing S3 vector bucket with vector indexes containing your data.
- Appropriate IAM permissions for both S3 Vectors and OpenSearch Service.
- An understanding of your performance requirements to choose the appropriate
  integration method.

### Getting started

**Using the AWS Management Console**

###### To export vector data to OpenSearch

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. In the list of vector buckets, choose the name of the bucket containing the vector
   data that you want to export.
4. For **Vector indexes**, choose the radio button next to the
   vector index that you want to export.
5. Choose **Advanced search export**, then choose **Export to
   OpenSearch**.

###### Important

- **Point-in-time export**: The export captures data up
  to the initiation of the export. If you make updates to your vector data during the
  ingestion to OpenSearch, not all updates will be reflected in OpenSearch.
- **One-time operation**: This is a one-time export and
  will not stay in sync with your S3 Vectors data. You must manually re-export to
  capture any subsequent changes.

Then, to configure and manage the integration of S3 Vectors with Amazon OpenSearch Service, you'll work
primarily through the OpenSearch console.

###### To view exports to OpenSearch

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. In the list of vector buckets, choose the name of the bucket containing the vector
   data that you want to export.
4. For **Vector indexes**, choose **Advanced search
   export**, then choose **View exports to
   OpenSearch**.

Then, you'll view exports to OpenSearch through the OpenSearch console.

For more information about creating and managing OpenSearch Serverless collections,
see [Creating and
managing Amazon OpenSearch Service Serverless collections](../../../opensearch-service/latest/developerguide/serverless-collections.md "../../../opensearch-service/latest/developerguide/serverless-collections.md") in the _Amazon OpenSearch Service Developer Guide_.

## OpenSearch with S3 Vectors engine

You can use S3 Vectors as the underlying storage engine for [Amazon OpenSearch Managed
clusters](https://aws.amazon.com/opensearch-service/features/managed/ "https://aws.amazon.com/opensearch-service/features/managed/"), providing cost-optimized vector storage while maintaining OpenSearch
functionality.

### When to use this integration

Consider using OpenSearch with the S3 Vectors engine when you need the following:

- **Hybrid search capabilities** that combine vector
  similarity with keyword search.
- **Lower query throughput** that may have less frequent or
  sporadic usage patterns.
- **Higher latency tolerance** for applications that can
  accept longer response times in exchange for cost savings.
- **Advanced analytics** that include aggregations,
  faceted search, and complex filtering.
- **Existing OpenSearch workflows** that you want to
  extend with cost-effective vector storage.

### Prerequisites

Before using OpenSearch with S3 Vectors engine, ensure you have:

- An existing OpenSearch managed domain. For more information, see [Creating and
  managing Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the _Amazon OpenSearch Service Developer Guide_.
- An understanding of your performance requirements to choose the appropriate
  integration method.

### Getting Started

To use OpenSearch with S3 Vectors engine, set your engine to `S3_Vectors`
during index creation in OpenSearch. For more information about the template that you use
when creating an index in OpenSearch Service, including where to specify the engine type, see [Methods and engines](https://docs.opensearch.org/docs/latest/field-types/supported-field-types/knn-methods-engines/ "https://docs.opensearch.org/docs/latest/field-types/supported-field-types/knn-methods-engines/"). For more information about
the integration between OpenSearch and S3 Vectors engine, see [Advanced search capabilities with an S3 Vectors engine](../../../opensearch-service/latest/developerguide/s3-vector-opensearch-integration-engine.md "../../../opensearch-service/latest/developerguide/s3-vector-opensearch-integration-engine.md") in the _Amazon
OpenSearch Service Developer Guide_.
