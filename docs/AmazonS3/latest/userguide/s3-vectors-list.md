# Listing vectors

You can list vectors in a vector index with the [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") API operation.
For more information about the maximum number of vectors that can be returned per page, see
[Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). The
response includes a pagination token when results are truncated. For more information about
the response elements of `ListVectors`, see [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") in the
_Amazon S3 API Reference_. You can also use `ListVectors` to
export vector data from a specified
vector index. `ListVectors` is strongly consistent. After a WRITE operation, you
can immediately list vectors with all changes reflected.

To list vectors, use the following example commands. Replace the `user
 input placeholders` with your own information.

The `segment-count` and `segment-index` parameters allow you to partition your
listing operations across multiple parallel requests. When you specify a
`segment-count` value (such as `2`), you divide the index into that many segments. The
`segment-index` parameter (starting from 0) determines which segment to list. This
approach helps improve performance when listing large vector indexes by enabling
parallel processing. For more information about `segment-count` and `segment-index`,
see [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md") in the
_Amazon S3 API Reference_.

**To list all vectors in an index**

Example request:

```
aws s3vectors list-vectors \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --index-name "`idx`" \
  --segment-count 2 \
  --segment-index 0 \
  --return-data \
  --return-metadata
```

Example response:

```
{
    "vectors": [
        {
            "key": "vec3",
            "data": {
                "float32": [0.4000000059604645]
            },
            "metadata": {
                "nonFilterableKey": "val4",
                "filterableKey": "val2"
            }
        }
    ]
}
```

**To list vectors with pagination**

Example request:

```
aws s3vectors list-vectors \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --index-name "`idx`" \
  --segment-count 2 \
  --segment-index 0 \
  --return-data \
  --return-metadata \
  --next-token "zWfh7e57H2jBfBtRRmC7OfMwl209G9dg3j2qM6kM4t0rps6ClYzJykgMOil9eGqU5nhf_gTq53IfoUdTnsg"
```

Example response:

```
{
    "vectors": [
        {
            "key": "vec1",
            "data": {
                "float32": [0.5]
            },
            "metadata": {
                "nonFilterableKey": "val2",
                "filterableKey": "val1"
            }
        }
    ]
}
```

SDK for Python
Example: List vectors in a vector index

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#List vectors in your vector index

response = s3vectors.list_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    maxResults = 600,
    returnData = True,
    returnMetadata = True
)

vectors = response["vectors"]

print(vectors)
```

Example: List all vectors in a vector index in parallel

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#List vectors in the 1st half of vectors in the index.
response = s3vectors.list_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    segmentCount=2,
    segmentIndex=1,
    maxResults = 600,
    returnData = True,
    returnMetadata = True
)

vectors = response["vectors"]

#List vectors starting from the 2nd half of vectors in the index.
# This can be ran in parallel with the first `list_vectors` call.
response = s3vectors.list_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    segmentCount=2,
    segmentIndex=1,
    maxResults = 600,
    returnData = True,
    returnMetadata = True
)

vectors = response["vectors"]

print(vectors)
```
