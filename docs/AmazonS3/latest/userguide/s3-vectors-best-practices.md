# S3 Vectors best practices

Amazon S3 Vectors delivers purpose-built, cost-optimized vector storage for use by
AI-enabled applications and semantic search of your content stored in Amazon S3. Designed to
provide S3 level elasticity and durability for storing vector datasets with sub-second query
performance, S3 Vectors is ideal for applications that need to build and grow
vector indexes. With S3 Vectors you can use a dedicated set of API operations to store,
access, and perform similarity queries on vector data without provisioning any
infrastructure. For more information, see [Working with S3 Vectors and vector buckets](s3-vectors.md "s3-vectors.md").

To ensure the maximum benefit from S3 Vectors, we recommend that you perform the following best practices.

**Inserting and deleting vectors**

Your application can achieve at least five [PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md") and
[DeleteVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md") requests per second per vector index. If you
exceed the request rates, you might receive a `429
 TooManyRequestsException` error. To maximize request throughput and
optimize for speed and efficiency, we recommend that you insert and delete
vectors in large batches, up to the maximum of 500 vectors per API request.
For more information, see [Vector indexes](s3-vectors-indexes.md "s3-vectors-indexes.md").

**Accessing and
querying vectors in an S3 vector index**

Your application can achieve hundreds of [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md"),
[GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md"), or [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") requests per second per
S3 vector index. If you exceed the request rates, you might receive a
`429 TooManyRequestsException` error. We recommend you use a
retry mechanism and configure your application to send fewer requests.

**Scaling across vector indexes**

To improve query performance per vector index,
consider configuring your application to divide vectors across multiple
vector indexes when possible. For example, if you have multi-tenant workloads and your application
queries each tenant independently, consider storing each tenant's vectors in a separate vector index.
For more information, see [Vector indexes](s3-vectors-indexes.md "s3-vectors-indexes.md").

**Implementing
multi-tenancy with separate vector indexes**

You can achieve multi-tenancy by organizing your vector data using a single vector index for each tenant. You can use IAM and
bucket policies to restrict each tenant's access to only their designated vector index.
This approach helps maintain data isolation and simplifies management by removing the need to create separate buckets for each tenant.
For more information,
see [Identity and Access management in
S3 Vectors](s3-vectors-access-management.md "s3-vectors-access-management.md").

**Configuring non-filterable metadata fields for
vector indexes**

When creating a vector index, configure metadata fields
that don't require filtering as non-filterable metadata keys.
For example, store text chunks for vector embeddings as non-filterable metadata fields when you need them only for reference.
For more information, see [Non-filterable
metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable "s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable").
