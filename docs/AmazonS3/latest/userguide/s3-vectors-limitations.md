# Limitations and restrictions

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Amazon S3 Vectors has certain limitations and restrictions that you should be aware of when planning your vector storage and search applications.


* Vector buckets per AWS Region in an account: 10,000
* Vector indexes per vector bucket: 10,000
* Vectors per vector index: Up to 50 million
* Dimension value per vector: 1 to 4,096
* Total metadata per vector: Up to 40 KB (filterable + non-filterable)
* Total metadata keys per vector: Up to 10
* Filterable metadata per vector: Up to 2 KB
* Non-filterable metadata keys per vector index: Up to 10
* Write requests per second per vector index: Up to 5
* Request payload size: Up to 20 MiB
* Vectors per [PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md") API call: Up to 500
* Vectors per [DeleteVectors](../API/API_S3VectorBuckets_DeleteVectors.md "../API/API_S3VectorBuckets_DeleteVectors.md") API call: Up to 500
* Vectors per [GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md") API call: Up to 100
* Top-K results per [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md") request: Up to 30
* Vectors listed per page in a [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") response: Up to 1,000
* Vector buckets listed per page in a [ListVectorBuckets](../API/API_S3VectorBuckets_ListVectorBuckets.md "../API/API_S3VectorBuckets_ListVectorBuckets.md") response: Up to 500.
* Vector indexes listed per page in a [ListIndexes](../API/API_S3VectorBuckets_ListIndexes.md "../API/API_S3VectorBuckets_ListIndexes.md") response: Up to 500.
* Segment count for parallel listing: Up to 16
If you require higher limits, contact your AWS account team.
