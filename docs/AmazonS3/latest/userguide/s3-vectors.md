# Working with S3 Vectors and vector buckets

## What is Amazon S3 Vectors?

Amazon S3 Vectors delivers purpose-built, cost-optimized vector storage for AI agents, inference, RAG, and semantic search. S3 Vectors is designed to provide the same elasticity, durability, and availability as Amazon S3 and delivers subsecond latency for infrequent queries and as low as 100 milliseconds for more frequent queries. You get
a dedicated set of API operations to store, access, and query vector data without provisioning any infrastructure. S3 Vectors consists of several key
components that work together:

- **Vector buckets** – A new bucket type
  that's purpose-built to store and query vectors.
- **Vector indexes** – Within a vector
  bucket, you can organize your vector data within vector indexes. You perform
  similarity queries on your vector data within vector
  indexes.
- **Vectors** – You store vectors in your
  vector index. For similarity search and AI applications, vectors are created as
  vector embeddings which are numerical representations that preserve semantic
  relationships between content (such as text, images, or audio) so similar items
  are positioned closer together. S3 Vectors can perform similarity searches based
  on semantic meaning rather than exact matching through comparing how close
  vectors are to each other mathematically. When adding vector data to a vector
  index, you can also attach metadata for future filtering queries based on a set
  of conditions (for example, timestamps, categories, and user
  preferences).

Writes to S3 Vectors are strongly consistent, which means that you can immediately
access the most recently added data. As you write, update, and delete vectors over
time, S3 Vectors automatically optimizes the vector data to achieve the best possible
price performance for vector storage, even as the data sets scale and evolve. You can
control access to your vector data with the existing access control mechanisms of Amazon S3,
including bucket and IAM policies. For more information about vector index limits
per bucket and vector limits per index, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

## Use cases: Similarity searches across large

datasets

Similarity searches allow you to find items that are conceptually related to each
other based on their vector representations, rather than exact keyword matches. These
searches identify content with similar meanings or characteristics, even when the exact
words or visual elements differ.

Common use cases for similarity search with S3 Vectors include:

- **Medical imaging** - Find similarities in
  millions of medical images to assist with diagnosis and treatment
  planning
- **Copyright infringement** - Identify potentially
  derivative content across large media libraries
- **Image deduplication** - Detect and remove
  duplicate or near-duplicate images from large image collections
- **Video understanding** - Search for specific
  scenes or content within video assets
- **Enterprise document search** - Enable semantic
  search across corporate documents to find relevant information based on
  meaning
- **Personalization** - Deliver tailored
  recommendations by finding similar items

You should use S3 Vectors if you want to build cost-effective vector search and
agentic AI applications with sub-second search times. With vector buckets, you only
pay for what you use, and could save costs for uploading, storing,
and querying vector embeddings. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Features of S3 Vectors

### Purpose-built storage for

vectors

S3 Vectors is the first purpose-built object storage in the cloud to store and
query vectors. Vector buckets are designed to provide cost-effective, elastic,
and durable storage for vector data.

Vector embeddings are transforming how customers use and retrieve their
unstructured data, from detecting similarities across medical images, finding
anomalies in thousands of hours of video footage, navigating through large code
bases, and identifying the most relevant case law for a given legal matter. These
emerging applications combine with embedding models to encode the semantic meaning
of data (for example, text, images, video, code) as numerical vector
embeddings.

Within a vector bucket, you organize your vector data within vector indexes,
without provisioning infrastructure. As you write, update, and delete vectors over
time, S3 Vectors automatically optimize the vector data to achieve the best
possible price performance for vector storage, even as the data sets scale and
evolve. For more information about vector index limits per bucket and vector
limits per index, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

### Perform similarity queries

With S3 Vectors, you can perform queries to find the most
similar vectors to a query vector, with sub-second response times for infrequent queries and as low as 100 milliseconds for more frequent queries. S3 Vectors is
ideal for workloads where queries are less frequent.

### Metadata filtering

You can attach metadata (for example, year, author, genre, and location) as
key-value pairs to your vectors. By default, all metadata is filterable unless you
explicitly specify it as non-filterable. You can use filterable metadata to filter
your query results based on specific attributes, enhancing the relevance of your
queries. Vector indexes support string, number, boolean, and list types of
metadata. For more information about metadata size limits per vector and filterable
metadata size limits per vector, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

### Access management and

security

You can manage access for resources in vector buckets with IAM and [Service Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in AWS Organizations. S3 Vectors uses a
different service namespace than Amazon S3: the `s3vectors` namespace.
Therefore, you can design policies specifically for the S3 Vectors service and its
resources. You can design policies to grant access to individual vector indexes,
all vector indexes within a vector bucket, or all vector buckets in an
account. All Amazon S3 Block Public Access settings are always enabled for
vector buckets and cannot be disabled.

### Integration with AWS services

S3 Vectors integrates with other AWS services to enhance your vector processing
capabilities:

- **[Amazon OpenSearch
  Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")** - Optimize vector storage costs while
  continuing to use OpenSearch API operations. This is ideal for workloads
  that need advanced search functionality such as hybrid search, aggregations,
  advanced filtering, and faceted search. You can also export a snapshot of an
  S3 vector index to Amazon OpenSearch Serverless for high QPS and low
  latency vector search.
- **[Amazon Bedrock Knowledge
  Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/")** - Select a vector index in S3 Vectors as
  your vector store to save on storage costs for retrieval augmented
  generation (RAG) applications.
- **[Amazon Bedrock in
  SageMaker Unified Studio](https://aws.amazon.com/bedrock/unifiedstudio/ "https://aws.amazon.com/bedrock/unifiedstudio/")** - Develop and test
  knowledge bases using S3 Vectors as your vector store.
