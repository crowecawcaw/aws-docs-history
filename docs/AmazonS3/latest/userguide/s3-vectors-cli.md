# Creating vector embeddings and performing semantic searches with `s3vectors-embed-cli`

Amazon S3 Vectors provides a standalone open-source tool called Amazon S3 Vectors Embed CLI (`s3vectors-embed-cli`) that simplifies working with vector data by combining embedding generation with vector operations in single commands. This CLI tool helps you get started with S3 Vectors quickly by automating vector embedding generation with Amazon Bedrock foundation models and semantic search operations within your vector indexes.

The S3 Vectors Embed CLI provides two main commands for integrating Amazon Bedrock embedding models with S3 Vectors operations:

- `s3vectors-embed put`: Generate and insert vector embeddings into an vector index. Specifically, convert text and images into vector embeddings through Amazon Bedrock models and automatically store them in your vector index.
- `s3vectors-embed query`: Generate vector embeddings from your query input through Amazon Bedrock models and query vectors in your vector index.
  The Amazon S3 Vectors Embed CLI is available in the [Amazon Web Services - Labs GitHub repository](https://github.com/awslabs "https://github.com/awslabs"). For detailed installation instructions, command parameters, examples, and best practices, see the [Amazon S3 Vectors Embed CLI GitHub repository](https://github.com/awslabs/s3vectors-embed-cli "https://github.com/awslabs/s3vectors-embed-cli").

For the lower-level S3 Vectors API operations that provide more control and customization, see [Amazon S3 Vectors](https://amazonaws.com/AmazonS3/latest/API/API_Operations_AWS_S3_Vectors.html "https://amazonaws.com/AmazonS3/latest/API/API_Operations_AWS_S3_Vectors.html") in the _Amazon Simple Storage Service API Reference_.
