

# S3 Vectors best practices

Amazon S3 Vectors delivers purpose-built, cost-optimized vector storage for use by AI-enabled applications and semantic search of your content stored in Amazon S3. Designed to provide S3 level elasticity and durability for storing vector datasets with sub-second query performance for cold queries and as low as 100 milliseconds for warm queries, S3 Vectors is ideal for applications that need to build and grow vector indexes. With S3 Vectors you can use a dedicated set of API operations to store, access, and perform similarity queries on vector data without provisioning any infrastructure. For more information, see [Working with S3 Vectors and vector buckets](s3-vectors.md). 

 To ensure the maximum benefit from S3 Vectors, we recommend that you perform the following best practices.

**Inserting and deleting vectors**  
Your application can achieve up to 1,000 [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html) or [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html) requests per second per vector index, insert or delete up to 2,500 vectors per second per vector index or reach a maximum throughput of 140 MBps, whichever limit is reached first. If you exceed these request rates, you might receive a `429 TooManyRequestsException` error.  
To optimize costs, we recommend inserting and deleting vectors in large batches, up to the maximum batch size of 500 vectors per API request. For example, for smaller vectors you can send 5 batches of 500 vectors per second to reach the maximum throughput of 2,500 vectors per second. For larger 100 KB vectors, you can send 7 batches of 200 vectors per second to reach the maximum throughput of 140 MBps.

**Accessing and querying vectors in an S3 vector index**  
 Your application can achieve hundreds of [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html), [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html), or [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) requests per second per S3 vector index. If you exceed the request rates, you might receive a `429 TooManyRequestsException` error. We recommend you use a retry mechanism and configure your application to send fewer requests. 

**Scaling across vector indexes**  
To improve query performance per vector index, consider configuring your application to divide vectors across multiple vector indexes when possible. For example, if you have multi-tenant workloads and your application queries each tenant independently, consider storing each tenant's vectors in a separate vector index. For more information, see [Vector indexes](s3-vectors-indexes.md).

**Implementing multi-tenancy with separate vector indexes**  
You can achieve multi-tenancy by organizing your vector data using a single vector index for each tenant. You can use IAM and bucket policies to restrict each tenant's access to only their designated vector index. This approach helps maintain data isolation and simplifies management by removing the need to create separate buckets for each tenant. For more information, see [Identity and Access management in S3 Vectors](s3-vectors-access-management.md).

**Configuring non-filterable metadata fields for vector indexes**  
When creating a vector index, configure metadata fields that don't require filtering as non-filterable metadata keys. For example, store text chunks for vector embeddings as non-filterable metadata fields when you need them only for reference, or when you want to make a large text field full-text searchable without filtering on it. The non-filterable list is set at index creation and can't be changed afterward, so declare these fields when you create the index. For more information, see [Non-filterable metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable) and [Configuring full-text search](s3-vectors-configuring-full-text-search.md).

**Choosing an index mode**  
Use the `ENHANCED` index mode for workloads that filter on metadata, and for full-text or hybrid search. In `ENHANCED` mode, S3 Vectors applies your filter before the vector search, which keeps recall high even when filters match a small fraction of vectors, and it supports the `$startsWith` operator. Full-text and hybrid search are available only on `ENHANCED` indexes. Use `CLASSIC` only if your queries can neither be simplified to 100 or fewer filter constraints nor split across smaller queries; for both techniques, see Writing filters for lower latency. To run a single query with `ENHANCED` filtering behavior without changing an index, set `queryMode` to `ENHANCED` on a `QueryVectors` request. The `queryMode` override applies to filtering only. Full-text and hybrid queries require the index itself to be `ENHANCED`.

**Writing filters for lower latency**  
A filtered query's latency grows with the work its filter does: with the size of the vector index, with the share of the index your filter matches, and with the number of constraints the filter evaluates. To keep filtered queries fast, prefer selective filters and use the fewest constraints that express what you need.  
When a query would otherwise filter on a long list of values, attach a single metadata key that captures the group those values belong to, and filter on that one key instead. Filtering on a list uses one constraint per value; the following uses 3 constraints:  

```json
{"documentId": {"$in": ["doc-001", "doc-002", "doc-003"]}}
```
A user who can access 300 documents would need a 300-value list, which uses 300 constraints. Instead, attach a `caseId` to each vector when you write it, and filter on that single key, which uses one constraint:  

```json
{"caseId": "case-4471"}
```
If a query cannot be simplified this way, you can split its filter across smaller queries, run them in parallel, and merge the results by distance. Set `returnDistance` to `true` on each query so that every result includes its distance to merge on. For queries that must match a large share of your index, you can also divide the vectors across multiple vector indexes so that each query filters less data.

**Writing full-text and hybrid queries**  
When configuring a metadata field for full-text search, use the default standard analyzer when you don't know the language of the text data upfront. Language analyzers, on the other hand, can give higher-quality results when the language is known, because they apply language-aware stemming and stopword removal. To keep full-text or hybrid queries fast, use shorter query terms that express what you need where possible. Latency for full-text or hybrid queries grows with the work the query does. This includes longer query text, more fields searched for full-text, a larger vector index, and a larger share of the index that your query terms match.