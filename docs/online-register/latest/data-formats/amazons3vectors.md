

# Data retrieval APIs for Amazon S3 Vectors
<a name="amazons3vectors"></a>

Amazon S3 Vectors provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="s3vectors-GetIndex"></a>[GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html) | Get the attributes of a specified vector index | Read | 
| <a name="s3vectors-GetVectorBucket"></a>[GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html) | Get the attributes of a specified vector bucket | Read | 
| <a name="s3vectors-GetVectorBucketPolicy"></a>[GetVectorBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucketPolicy.html) | Get the IAM resource policy for a specific vector bucket | Read | 
| <a name="s3vectors-GetVectors"></a>[GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html) | Get a batch of vectors by their vector keys | Read | 
| <a name="s3vectors-ListIndexes"></a>[ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html) | Get a paginated list of all indexes in a specified vector bucket | List | 
| <a name="s3vectors-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListTagsForResource.html) | List tags for specified S3Vector resource | List | 
| <a name="s3vectors-ListVectorBuckets"></a>[ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html) | Get a paginated list of all vector buckets in the account | List | 
| <a name="s3vectors-ListVectors"></a>[ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) | Get a paginated list of all vectors in a specified vector index | List | 
| <a name="s3vectors-QueryVectors"></a>[QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) | Find approximate nearest neighbors within a specified search vector index for a given query vector | Read | 