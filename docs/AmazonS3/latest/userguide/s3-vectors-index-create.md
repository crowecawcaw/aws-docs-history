# Inserting vectors into a vector index

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can add vectors to a vector index with the [PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md") API operation. Each
vector consists of a key, which uniquely identifies each vector in a vector
index. If you put a vector with a key that already
exists in the index, it will overwrite the existing vector completely, which makes the
previous vector no longer searchable. To maximize write throughput, it's recommended that
you insert vectors in large batches, up to the maximum batch size for
`PutVectors`. For more information about the maximum batch size for
`PutVectors`, which is the limit of vectors per `PutVectors` API
call, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").
Additionally, you can attach metadata (for example, year, author, genre, location) as
key-value pairs to each vector. By default, all metadata keys that are attached to vectors
are filterable and can be used as filters in a similarity query. Only metadata keys that are
specified as non-filterable during vector index creation are excluded from filtering. S3
vector indexes support string, number, boolean, and list types of metadata. For more
information about the total metadata size limit per vector and the filterable metadata size
limit per vector, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). If the metadata size exceeds these limits, the
`PutVectors` API operation will return a `400 Bad Request`
error.

Before adding vector data to your vector index with the `PutVectors` API
operation, you need to convert your raw data into vector embeddings, which are numerical
representations of your content as arrays of floating-point numbers. The vector embeddings
capture the semantic meaning of your content, enabling similarity searches once they're
stored in your vector index through the `PutVectors` operation. You can generate
vector embeddings using various methods depending on your data type and use case. These
methods include using machine learning frameworks, specialized embedding libraries, or AWS
services such as Amazon Bedrock. For example, if you're using Amazon Bedrock, you can generate embeddings
with the [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md") API
operation and your preferred embedding model.

Additionally, Amazon Bedrock Knowledge Bases provides a fully managed end-to-end RAG workflow where Amazon Bedrock automatically fetches data from your S3 data source,
converts content into text blocks, generates embeddings, and stores them in your
vector index. You can then query the knowledge base and generate responses based on chunks
retrieved from your source data.

Furthermore, the open-source Amazon S3 Vectors Embed CLI tool provides a simplified way to generate embeddings and perform semantic searches from the command line.
For more information about this open source tool that automates both vector embedding generation with Amazon Bedrock foundation
models and semantic search operations within your S3 vector indexes, see [Creating vector embeddings and performing semantic searches with s3vectors-embed-cli](s3-vectors-cli.md "s3-vectors-cli.md").

###### Note

When inserting vector data into your vector index, you must provide the vector data as
`float32` (32-bit floating point) values. If you pass higher-precision
values to an AWS SDK, S3 Vectors converts the values to 32-bit floating point before
storing them, and [GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md"), [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md"), and
[QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md") operations return the `float32` values. Different AWS SDKs
may have different default numeric types, so ensure your vectors are properly formatted
as `float32` values regardless of which SDK you're using. For example, in
Python, use `numpy.float32` or explicitly cast your values.

SDK for Python

```
# Populate a vector index with embeddings from Amazon Titan Text Embeddings V2.
import boto3
import json

# Create Bedrock Runtime and S3 Vectors clients in the AWS Region of your choice.
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

# Texts to convert to embeddings.
texts = [
    "Star Wars: A farm boy joins rebels to fight an evil empire in space",
    "Jurassic Park: Scientists create dinosaurs in a theme park that goes wrong",
    "Finding Nemo: A father fish searches the ocean to find his lost son"
]

# Generate vector embeddings.
embeddings = []
for text in texts:
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps({"inputText": text})
    )

    # Extract embedding from response.
    response_body = json.loads(response["body"].read())
    embeddings.append(response_body["embedding"])

# Write embeddings into vector index with metadata.
s3vectors.put_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    vectors=[
        {
            "key": "Star Wars",
            "data": {"float32": embeddings[0]},
            "metadata": {"source_text": texts[0], "genre":"scifi"}
        },
        {
            "key": "Jurassic Park",
            "data": {"float32": embeddings[1]},
            "metadata": {"source_text": texts[1], "genre":"scifi"}
        },
        {
            "key": "Finding Nemo",
            "data": {"float32": embeddings[2]},
            "metadata": {"source_text": texts[2], "genre":"family"}
        }
    ]
)
```
