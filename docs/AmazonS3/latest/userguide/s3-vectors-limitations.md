

# Limitations and restrictions
<a name="s3-vectors-limitations"></a>

Amazon S3 Vectors has certain limitations and restrictions that you should be aware of when planning your vector storage and search applications.
+ Vector buckets per AWS Region in an account: 10,000
+ Vector indexes per vector bucket: 10,000
+ Vectors per vector index: Up to 2 billion
+ Dimension value per vector: 1 to 4,096
+ Total metadata per vector: Up to 40 KB (filterable \+ non-filterable)
+ Total metadata keys per vector: Up to 50
+ Filterable metadata per vector: Up to 2 KB
+ Non-filterable metadata keys per vector index: Up to 10
+ Combined PutVectors and DeleteVectors requests per second per vector index: Up to 1,000 
+ Combined vectors inserted and deleted per second per vector index: Up to 2,500 
+ Request payload size: Up to 20 MiB
+ Vectors per [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html) API call: Up to 500
+ Vectors per [DeleteVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_DeleteVectors.html) API call: Up to 500
+ Vectors per [GetVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectors.html) API call: Up to 100
+ Top-K results per [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) request: Up to 10,000
+ Results per page in a [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) response: Up to 100
+ Vectors listed per page in a [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) response: Up to 1,000
+ Vector buckets listed per page in a [ListVectorBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectorBuckets.html) response: Up to 500.
+ Vector indexes listed per page in a [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html) response: Up to 500.
+ Segment count for parallel listing in a ListVectors API call: Up to 16