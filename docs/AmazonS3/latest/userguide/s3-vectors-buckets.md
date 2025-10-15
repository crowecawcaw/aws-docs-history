# Vector buckets

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Vector buckets are a type of Amazon S3 bucket designed specifically for storing and querying
 vector data. Vector buckets use dedicated APIs to manage vector data efficiently and
 reduce costs of upload, storing, and querying vector embeddings. Vector buckets provide
 the foundation for organizing your vector data into indexes, enabling you to perform
 similarity searches across large datasets while benefiting from the availability,
 durability, scalability, and cost-effectiveness of Amazon S3.

Vector buckets are optimized for long-term vector storage with sub-second search times.
 You can perform similarity queries on your vector data and optionally attach metadata to
 filter queries based on specific conditions such as dates, categories, or user
 preferences.

Each vector bucket has a unique Amazon Resource Name (ARN) and resource policy attached to
 it. The ARNs of vector buckets follow the following format: 


```
arn:aws:s3vectors:`Region`:`OwnerAccountID`:bucket/`bucket-name`
```
Within a vector bucket, you create vector indexes to store and query your data. Each
 vector bucket exists within a specific AWS Region and you can create multiple vector indexes
 inside a vector bucket. Vector buckets support security and access control mechanisms,
 including IAM identity-based policies and bucket policies. You can use bucket policies to grant or restrict
 access to specific indexes within your vector bucket.

Key characteristics of vector buckets:


* Purpose-built for vector storage and similarity search operations.
* Strongly consistent writes ensure that the vector data is immediately accessible.
* Automatic optimization of vector data for best price-performance as datasets
 scale.
For more information about vector index limits per bucket and other limitations, see
 [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

###### Topics

* [Vector bucket naming rules](s3-vectors-buckets-naming.md "s3-vectors-buckets-naming.md")
* [Creating a vector bucket](s3-vectors-buckets-create.md "s3-vectors-buckets-create.md")
* [Listing vector buckets](s3-vectors-buckets-list.md "s3-vectors-buckets-list.md")
* [Viewing vector bucket attributes](s3-vectors-buckets-details.md "s3-vectors-buckets-details.md")
* [Deleting an empty vector bucket](s3-vectors-buckets-delete.md "s3-vectors-buckets-delete.md")
* [Managing vector bucket policies](s3-vectors-bucket-policy.md "s3-vectors-bucket-policy.md")
