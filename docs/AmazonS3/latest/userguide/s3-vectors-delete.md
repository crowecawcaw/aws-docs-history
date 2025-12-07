# Deleting vectors from a vector index

You can delete specific vectors from a vector index by specifying their vector keys using the [DeleteVectors](../API/API_S3VectorBuckets_DeleteVectors.md "../API/API_S3VectorBuckets_DeleteVectors.md") API. This operation is useful for removing outdated or incorrect data while
preserving the rest of your vector data.

To delete vectors, use the following example commands. Replace the `user input placeholders` with your own information.

```
aws s3vectors delete-vectors \
 --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
 --index-name "`idx`" \
 --keys '["`vec2`","`vec3`"]'
```

SDK for Python

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#Delete vectors in a vector index
response = s3vectors.delete_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    keys=["Star Wars", "Finding Nemo"])
```
