# Vectors

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Each vector consists of a key, which uniquely identifies each vector in a vector
index. Additionally, you can
attach metadata (for example, year, author, genre, location) as key value pairs to each
vector.

Vector data operations include inserting, listing, querying, and deleting vectors. To
generate new vector embeddings of your unstructured data, you can use the [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md") API operation from Amazon Bedrock to specify the model ID of the embedding
model that you want to use. Additionally, the open-source Amazon S3 Vectors Embed CLI tool provides a simplified way to generate embeddings and perform semantic searches from the command line.
For more information about this open source tool that automates both vector embedding generation with Amazon Bedrock foundation
models and semantic search operations within your S3 vector indexes, see [Creating vector embeddings and performing semantic searches with s3vectors-embed-cli](s3-vectors-cli.md "s3-vectors-cli.md").

## Vector concepts

**Vector keys**: Each vector is identified
by a unique vector key within the index. Vector keys can be up to 1,024 characters long
and must be unique within the vector index. Keys are case-sensitive and can contain
any UTF-8 characters.

**Vector dimension**: A dimension is the number of values
in a vector. Larger dimensions require more storage space. All vectors in an index must
have the same number of dimensions, which is specified when you create the index. A
dimension must be an integer between 1 and 4096.

**Metadata**: You can attach metadata to vectors as
key-value pairs to provide additional context and enable filtering during queries.
Metadata includes both filterable and non-filterable metadata keys. Filterable metadata
is used for query filtering. Non-filterable metadata keys are specified during a vector index
creation and provides additional context but can’t be used for filtering. Metadata
supports string, number, and boolean types. For more information about filterable and
non-filterable metadata, see [Metadata filtering](s3-vectors-metadata-filtering.md "s3-vectors-metadata-filtering.md"). For more information about metadata
limits, including size limits per vector and maximum metadata keys per vector, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

###### Topics

- [Inserting vectors into a vector index](s3-vectors-index-create.md "s3-vectors-index-create.md")
- [Listing vectors](s3-vectors-list.md "s3-vectors-list.md")
- [Querying vectors](s3-vectors-query.md "s3-vectors-query.md")
- [Deleting vectors from a vector index](s3-vectors-delete.md "s3-vectors-delete.md")
- [Metadata filtering](s3-vectors-metadata-filtering.md "s3-vectors-metadata-filtering.md")
