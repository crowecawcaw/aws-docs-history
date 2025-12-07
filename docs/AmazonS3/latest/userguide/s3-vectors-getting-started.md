# Tutorial: Getting started with S3 Vectors

In this tutorial, you create an S3 vector bucket and a vector index in an AWS Region in the Amazon S3 console. Next, you
use an Amazon Bedrock embedding model to generate vector embeddings of your data and store them in your vector index to perform semantic searches.

To get started, sign up for an AWS account if you don't already have one. For
more information about setting up with an account, see [Getting started with Amazon S3](GetStartedWithS3.md "GetStartedWithS3.md").

###### Topics

- [Step 1: Create a vector bucket with the
  console](#s3-vectors-create-bucket-tutorial "#s3-vectors-create-bucket-tutorial")
- [Step 2: Create a vector index in a
  vector bucket with the console](#s3-vectors-create-index-tutorial "#s3-vectors-create-index-tutorial")
- [Step 3: Insert vectors into a
  vector index with the SDK for Python (Boto3)](#s3-vectors-insert-vectors-tutorial "#s3-vectors-insert-vectors-tutorial")
- [Step 4. Query vectors in a
  vector index with the SDK for Python (Boto3)](#s3-vectors-query-vectors-tutorial "#s3-vectors-query-vectors-tutorial")
- [(Optional) Automate vector embedding creation with the S3 Vectors Embed CLI](#s3-vectors-embed-CLI-tutorial "#s3-vectors-embed-CLI-tutorial")
- [(Optional) Integrate S3 Vectors with Amazon Bedrock
  Knowledge Bases](#s3-vectors-bedrock-kb-tutorial "#s3-vectors-bedrock-kb-tutorial")
- [(Optional) Integrate S3 Vectors with Amazon
  OpenSearch](#s3-vectors-opensearch-tutorial "#s3-vectors-opensearch-tutorial")

## Step 1: Create a vector bucket with the

console

S3 vector buckets are a type of Amazon S3 bucket that's purpose-built to store and
query vectors. You use dedicated API operations to write and query vector data. You can
control access to your vector data with access control mechanisms such as IAM identity-based
policies and resource-based policies.

In this step, you use the Amazon S3 console to create your first vector bucket. For other ways to create a vector bucket,
see [Creating a vector bucket](s3-vectors-buckets-create.md "s3-vectors-buckets-create.md").

### To create a

vector bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Vector buckets**.
3. On the **Vector buckets** page, choose **Create
   vector bucket**.
4. On the **Create vector bucket** page, for the
   **Vector bucket name** field, enter a name. In this tutorial, we use
   `media-embeddings` as the vector bucket name.
   Vector bucket names
   must be 3 to 63 characters and unique within an AWS Region. Valid characters are
   lowercase letters (a-z), numbers (0-9), and hyphens (-).

###### Note

The vector bucket name can't be changed after the bucket is created. 5. Under **Encryption**, choose **Specify encryption
type**. You have the option to specify encryption type as **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** or the default **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
In this tutorial, we choose **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
For more information about setting encryption configuration for vector buckets, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md").

###### Note

The encryption type
can't be changed after the vector bucket is created. 6. Under **Tags (Optional)**, you can add tags as key-value pairs to help organize and specify permissions for your vector buckets. Enter a **Key** and a **Value**. To add another tag, choose **Add Tag**. You can enter up to 50 tags for a vector bucket. For more information, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md"). 7. Choose **Create vector bucket**.

## Step 2: Create a vector index in a

vector bucket with the console

###### Note

Choose your vector index configuration parameters carefully. After you create a vector index, you can't update the vector index name, dimension, distance metric, or non-filterable metadata keys. To change any of these values, you must create a new vector index.

In this step, you create a vector index in your vector bucket. The vector index is used to store and query your vector embeddings.
For more information about vector indexes, see [Vector indexes](s3-vectors-indexes.md "s3-vectors-indexes.md").

### To create a

vector index

1. Navigate to the newly created vector bucket in the
   **Vector buckets** list on the Amazon S3 console.
2. Choose **Create vector index**.
3. On the **Create vector index** page, enter a name in the **Vector index
   name** field. In this tutorial, we use `movies` as the
   vector index name.

Vector index names must be 3 to 63 characters and unique within this
vector bucket. Valid characters are lowercase letters (a-z), numbers (0-9), hyphens
(-), and dots (.).

The vector index name can't be changed after index creation. 4. Under **Dimension**, specify a numeric value between 1 and 4096 that determines how many numbers will be in each vector that's generated by your vector embedding model.
Embedding models are specialized machine learning (ML) models that convert data (such as text or images) into numerical vectors. Embedding models typically produce outputs between 500-2000 dimensions, with each dimension being a floating-point number.
In this tutorial, we'll use the Titan Text v2 embedding model from Amazon Bedrock. This embedding model uses 1024-dimensional vectors as the default, so we'll set dimension for the vector index to `1024`.

The dimension value can't be
changed after index creation. Carefully specify the dimension value based on your embedding model's recommendations. 5. Under **Distance metric**, choose either **Cosine** (which measures angular similarity) or **Euclidean** (which measures straight-line distance) as
the distance metric to define how similarity between vectors is calculated during queries. In this tutorial, we choose **Cosine**.

The distance metric can't be
changed after index creation. Carefully choose the distance metric based on your embedding model's recommendations. 6. Under **Additional settings (optional)**, you can specify non-filterable metadata keys to store supplementary information alongside your vector embeddings.

###### Note

You can attach filterable metadata as key-value pairs to each vector when you insert vector data after index creation.
By default, all metadata keys that are attached to vectors are filterable and can be used as filters in a similarity query.
Only metadata keys that are specified as non-filterable during vector index creation are excluded from filtering.

Each non-filterable metadata key must be between 1 to 63 characters and unique within the vector index. These keys are useful for storing reference information that you don't need to filter on during similarity queries.
For example, when working with text embeddings, you might want to preserve the original text chunks for reference purposes.
In this tutorial, we add a non-filterable metadata key that's named `source_text` to store the text data that we want to create vector embeddings for.

You can't update non-filterable metadata keys after index creation. Plan your metadata structure carefully. 7. Under **Encryption**, choose **Specify encryption type**. You have the option to use the bucket level encryption settings or override the encryption settings for the vector index. If you override the bucket-level settings, you have the option to specify encryption type for the vector index as **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** or the **Server-side encryption with Amazon S3 managed keys (SSE-S3)**. In this tutorial, we choose to **Use bucket settings for encryption**. For more information about setting encryption configuration for vector buckets and indexes, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md"). 8. Under **Tags (Optional)**, you can add tags as key-value pairs to help track and organize vector index costs using AWS Billing and Cost Management. Enter a **Key** and a **Value**. To add another tag, choose **Add Tag**. You can enter up to 50 tags for a vector index. For more information, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md"). 9. Choose **Create vector index**.

Verify that your new vector index appears inside the bucket.

## Step 3: Insert vectors into a

vector index with the SDK for Python (Boto3)

To insert, list, and query vectors, use the AWS SDKs, AWS CLI, or Amazon S3 REST API.

This step is to insert vector embeddings to your vector index with the [PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md") API operation.

You must first generate vector embeddings by using the embedding model of your choice. If you use Amazon Bedrock, generate embeddings by using the [InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md") API operation to specify your preferred embedding model.
Alternatively, to generate and insert vector embeddings with a single command, see [(Optional) Automate vector embedding creation with the S3 Vectors Embed CLI](#s3-vectors-embed-CLI-tutorial "#s3-vectors-embed-CLI-tutorial").

The following example code generates 1024-dimensional vector embeddings with the Titan Text Embeddings V2 model from Amazon Bedrock by using the AWS SDK for Python (Boto3),
and stores them in your vector index by using the `PutVectors` API.
Along with each vector, we attach key-value pairs as filterable metadata. Additionally, we use a non-filterable metadata key that's named `source_text` to preserve the original text from which each vector is derived.
To maximize request throughput and optimize for speed and efficiency, we recommend that you insert and delete vectors in batches. For more information,
see [S3 Vectors best practices](s3-vectors-best-practices.md "s3-vectors-best-practices.md").

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

## Step 4. Query vectors in a

vector index with the SDK for Python (Boto3)

After you store your vectors embeddings in the vector index,
you can perform a similarity search by using the [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md") API operation.

You must first generate your query vector embeddings by using the same embedding model that's used during insertion in [Step 3: Insert vectors into a
vector index with the SDK for Python (Boto3)](#s3-vectors-insert-vectors-tutorial "#s3-vectors-insert-vectors-tutorial").
In this tutorial, use the Titan Text Embeddings V2 model from Amazon Bedrock through the SDK for Python (Boto3).

You can perform a similarity search to return the closest matching vectors. In a similarity search, you can optionally filter by using metadata keys to narrow results based on specific criteria while maintaining semantic relevance.

```
# Query a vector index with an embedding from Amazon Titan Text Embeddings V2.
import boto3
import json

# Create Bedrock Runtime and S3 Vectors clients in the AWS Region of your choice.
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

# Query text to convert to an embedding.
input_text = "adventures in space"

# Generate the vector embedding.
response = bedrock.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({"inputText": input_text})
)

# Extract embedding from response.
model_response = json.loads(response["body"].read())
embedding = model_response["embedding"]

# Query vector index.
response = s3vectors.query_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    queryVector={"float32": embedding},
    topK=3,
    returnDistance=True,
    returnMetadata=True
)
print(json.dumps(response["vectors"], indent=2))

# Query vector index with a metadata filter.
response = s3vectors.query_vectors(
    vectorBucketName="media-embeddings",
    indexName="movies",
    queryVector={"float32": embedding},
    topK=3,
    filter={"genre": "scifi"},
    returnDistance=True,
    returnMetadata=True
)
print(json.dumps(response["vectors"], indent=2))

```

## (Optional) Automate vector embedding creation with the S3 Vectors Embed CLI

Amazon S3 Vectors Embed CLI is a standalone command line tool that simplifies the process of working with vector embeddings in S3 Vectors.
With single commands, you can create vector embeddings for your data by using Amazon Bedrock, and store and query them in your S3 vector index.
The tool supports the following commands:

- `s3vectors-embed put`: Generate vector embeddings of text, file content, or S3 objects, and store them as vectors in an S3 vector index.
- `s3vectors-embed query`: Embed a query input and search for similar vectors in an S3 vector index.

For more information about the commands and usage, see the [Amazon S3 Vectors Embed CLI GitHub repository](https://github.com/awslabs/s3vectors-embed-cli "https://github.com/awslabs/s3vectors-embed-cli").

## (Optional) Integrate S3 Vectors with Amazon Bedrock

Knowledge Bases

Amazon Bedrock Knowledge Bases integrates with S3 Vectors for cost effective and long-term storage
of vector datasets.

### Prerequisites

Follow the [prerequisites](../../../bedrock/latest/userguide/getting-started-console.md "../../../bedrock/latest/userguide/getting-started-console.md") to ensure you have necessary permissions for creating an Amazon Bedrock
knowledge base.

- Appropriate IAM permissions for both S3 Vectors and Amazon Bedrock services. For more
  information about IAM permissions for S3 Vectors, see [Identity and Access management in
  S3 Vectors](s3-vectors-access-management.md "s3-vectors-access-management.md").
- Your source documents prepared for ingestion into the knowledge base.
- An understanding of your embedding model requirements.

### Create an Amazon Bedrock knowledge base

with S3 Vectors in the console

Amazon Bedrock Knowledge Bases provides a fully managed end-to-end RAG workflow. When you create a
knowledge base with S3 Vectors, Amazon Bedrock automatically fetches data from your S3 data source,
converts content into text blocks, generates embeddings, and stores them in your
vector index. You can then query the knowledge base and generate responses based on chunks
retrieved from your source data.

###### To create an Amazon Bedrock knowledge base with S3 Vectors in the console

1. Sign in to the AWS Management Console using an [IAM
   role with Amazon Bedrock permissions](../../../bedrock/latest/userguide/getting-started.md "../../../bedrock/latest/userguide/getting-started.md"), and open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. In the left navigation pane, choose **Knowledge Bases**.
3. In the **Knowledge Bases** section, choose
   **Create**. In the dropdown list, choose **Knowledge Base
   with vector store**.
4. Keep the **Knowledge Base name**, **Knowledge Base
   description**, and **IAM permissions** at their default
   values in this tutorial.
5. For **Choose a data source type**, choose the data source to
   connect your knowledge base to. In this tutorial, choose **Amazon
   S3**.
6. (Optionally) Provide any **Tags** or **Application
   logs**.
7. Choose **Next**.
8. On the **Configure data source** page, keep the **Data
   source name**, **Data source location**, **Parsing
   strategy**, and **Chunking strategy** at the default
   settings in this tutorial.
9. In the **S3 URI**, enter the S3 general purpose bucket that
   contains your source files, or choose **Browse S3** and choose the S3
   general purpose bucket.
10. For encrypted S3 data, select **Add customer-managed KMS key for S3
    data** and specify your customer-managed KMS key.
11. Choose **Next** to proceed to the next step that specifies the
    **Embeddings model** and **Vector store**
    options.
12. In the **Embeddings model** section, choose **Select
    model** and choose an embedding model compatible for use with S3 Vectors.
    You must use floating-point embeddings. Binary type isn't supported.
13. (Optional) Expand the **Additional configurations** section to see
    the following configuration options (not all models support all configurations):
    - **Embeddings type** – Whether to convert the data to
      floating-point (float32) vector embeddings (more precise, but more costly) or binary
      vector embeddings (less precise, but less costly). To integrate with S3 Vectors,
      you must choose **Floating-point vector embeddings**.
    - **Vector dimensions** – Choose the embedding models recommended
      dimension size.

14. In the **Vector store** section, choose the recommended method
    **Quick create a new vector store** for automatic setup of a new
    vector bucket, or choose **Use an existing vector store** to use an
    existing vector bucket if available. For information about using an existing vector
    store flow, see [Prerequisites for using a vector store you created for a knowledge base](../../../bedrock/latest/userguide/knowledge-base-setup.md "../../../bedrock/latest/userguide/knowledge-base-setup.md") in
    the _Amazon Bedrock User Guide_.
15. For **Additional configurations** – By default, your
    vector bucket uses server-side encryption with Amazon S3 managed keys (SSE-S3). You
    can choose to use your own KMS key for server-side encryption with AWS Key Management
    Service keys (SSE-KMS) for enhanced control over encryption settings.
16. Choose **Next** to review the Knowledge Base details and then
    choose **Create Knowledge Base**.

###### Note

The time that it takes to create a knowledge base depends on your specific
configurations. When the creation of a knowledge base completes, the status of the
knowledge base changes to state it is either ready or available. Once your knowledge base
is ready and available, sync your data source for the first time or whenever you want to
keep your content up to date. To sync your data source, choose your knowledge base in the
console and choose **Sync** within the data source overview
section.

## (Optional) Integrate S3 Vectors with Amazon

OpenSearch

[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") is a
fully managed service that simplifies the deployment, scaling, and operation of OpenSearch
in the AWS Cloud. There are two integrations between S3 Vectors and OpenSearch. One is to
export vector data from S3 Vectors to OpenSearch Serverless for high-performance search
capabilities. The other uses S3 Vectors as a cost-effective storage engine within
OpenSearch while maintaining access to OpenSearch functionality.

For more information, see [Using S3 Vectors with OpenSearch Service](s3-vectors-opensearch.md "s3-vectors-opensearch.md").
