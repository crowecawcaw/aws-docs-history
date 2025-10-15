# Using S3 Vectors with Amazon Bedrock Knowledge Bases

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

S3 Vectors integrates with [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") and [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/") to
 simplify and reduce the cost of vector storage for retrieval augmented generation (RAG)
 applications.

For more information about high-level CLI commands that integrate Amazon Bedrock embedding models with
 S3 Vectors operations, see .

###### Topics

* [Integration overview](#s3-vectors-bedrock-kb-overview "#s3-vectors-bedrock-kb-overview")
* [When to use this integration](#s3-vectors-bedrock-kb-when "#s3-vectors-bedrock-kb-when")
* [Supported embedding models](#s3-vectors-bedrock-kb-models "#s3-vectors-bedrock-kb-models")
* [Prerequisites and permissions](#s3-vectors-bedrock-kb-prereq "#s3-vectors-bedrock-kb-prereq")
* [Creating a knowledge base with S3
 Vectors](#s3-vectors-bedrock-kb-create "#s3-vectors-bedrock-kb-create")
* [Managing and querying your knowledge
 base](#s3-vectors-bedrock-kb-manage "#s3-vectors-bedrock-kb-manage")
* [Limitations](#s3-vectors-bedrock-kb-limits "#s3-vectors-bedrock-kb-limits")

## Integration overview


When creating a knowledge base in Amazon Bedrock, you can select S3 Vectors as your vector store.
 This integration provides the following:



* **Cost savings** for RAG applications with large vector
 datasets.
* **Seamless integration** with the fully managed RAG
 workflow of Amazon Bedrock.
* **Automatic vector management** handled by the Amazon Bedrock
 service.
* **Sub-second query latency** for knowledge base retrieval
 operations.

Amazon Bedrock Knowledge Bases provides a fully managed end-to-end RAG workflow. When you create a
 knowledge base with S3 Vectors, Amazon Bedrock automatically fetches data from your S3 data source,
 converts content into text blocks, generates embeddings, and stores them in your
 vector index. You can then query the knowledge base and generate responses based on chunks
 retrieved from your source data.


## When to use this integration


Consider using S3 Vectors with Amazon Bedrock Knowledge Bases when you need the following:



* **Cost-effective vector storage** for large datasets
 where sub-second query latency meets your application requirements.
* **Text and image-based document retrieval** for use cases
 like searching through manuals, policies, and visual content.
* **RAG applications** that prioritize storage cost
 optimization over ultra-low latency responses.
* **Managed vector operations** without needing to learn
 S3 Vectors API operations directly - you can continue using familiar Amazon Bedrock
 interfaces.
* **Long-term vector storage** with the durability and
 scalability of Amazon S3

This integration is ideal for organizations building RAG applications that need to search
 through and extract insights from written content and images, where the cost benefits of
 S3 Vectors align with acceptable query performance requirements.


## Supported embedding models


The S3 Vectors integration with Amazon Bedrock Knowledge Bases supports the following embedding
 models:



* **amazon.titan-embed-text-v2:0** - For text-based
 embeddings
* **amazon.titan-embed-image-v1** - For image and
 multimodal embeddings
* **cohere.embed-english-v3** - For multilingual and
 specialized text embeddings

## Prerequisites and permissions


Before creating a knowledge base with S3 Vectors, ensure you have the following:



* Appropriate IAM permissions for both S3 Vectors and Amazon Bedrock services. For more
 information about IAM permissions for S3 Vectors, see [Identity and Access management in
 S3 Vectors](s3-vectors-access-management.md "s3-vectors-access-management.md"). For more information about IAM permissions for
 your Amazon Bedrock Knowledge Bases service role to access S3 Vectors, see [Permissions
 to access your vector store in Amazon S3 Vectors](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html#kb-permissions-s3vectors "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html#kb-permissions-s3vectors") in the *Amazon Bedrock User
 Guide*.
* Your source documents prepared for ingestion into the knowledge base.
* An understanding of your embedding model requirements.

When setting up security configurations, you can choose an IAM role that provides Amazon Bedrock
 permission to access required AWS services. You can let Amazon Bedrock create the service role or use
 your own custom role. If you use a custom role, configure a vector bucket policy that
 restricts access to the vector bucket and vector index to the custom role.


For detailed information about required permissions and IAM roles, see [Create a service
 role for Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html") in the *Amazon Bedrock User Guide*.
 The service role must also have permissions for S3 Vectors and AWS KMS API operations.


## Creating a knowledge base with S3
 Vectors


You can create a knowledge base that uses S3 Vectors through two methods.


### Method one: Using the Amazon Bedrock
 console


When creating a knowledge base in the Amazon Bedrock console, you can choose "S3 vector bucket" as
 your vector store option. You have two setup options:



* **Quick create a new vector store** - Amazon Bedrock creates an
 S3 vector bucket and vector index and configures them with the required settings
 for you. By default, the vector bucket is encrypted using server-side encryption with
 Amazon S3 managed keys (SSE-S3). You can optionally encrypt the bucket using AWS KMS. For more
 information about **Quick create a new vector store** in
 the console, see [Create a knowledge base by
 connecting to a data source in Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html") in the
 *Amazon Bedrock User Guide*.
* **Choose a vector store you have created** - Choose an
 existing S3 vector bucket and vector index from your account that you've
 previously created. For more information about creating an S3 vector bucket and
 vector index in the Amazon Bedrock Knowledge Bases console, see the S3 Vectors tab in [Prerequisites for using a vector store you created for a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html") in
 the *Amazon Bedrock User Guide*.

For detailed step-by-step instructions, see [Create a knowledge base by
 connecting to a data source in Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html") in the
 *Amazon Bedrock User Guide*.


### Method two: Using Amazon SageMaker
 Unified Studio


You can also create and manage knowledge bases with S3 Vectors through Amazon Bedrock in [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/").
 This provides a unified development environment for building and testing AI applications
 that use knowledge bases.


[Amazon Bedrock in SageMaker AI Unified
 Studio](https://aws.amazon.com/bedrock/unifiedstudio/ "https://aws.amazon.com/bedrock/unifiedstudio/") is designed for users who need integrated notebook capabilities and work
 across multiple AWS ML and analytics services. You can quickly create an
 S3 vector bucket and configure it as the vector store for your knowledge bases when you
 build generative AI applications.


For information about using S3 Vectors with Amazon Bedrock in SageMaker AI Unified Studio, see [Add
 a data source to your Amazon Bedrock app](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-sources.html "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-sources.html") in the *SageMaker AI Unified Studio User
 Guide*.


## Managing and querying your knowledge
 base


### Data synchronization and
 management


Amazon Bedrock Knowledge Bases offers ingestion job operations to keep your data source and vector
 embeddings synchronized. When you sync your data source, Amazon Bedrock scans each document and
 verifies whether it has been indexed into the vector store. You can also directly index
 documents into the vector store using the [IngestKnowledgeBaseDocuments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_IngestKnowledgeBaseDocuments.html "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_IngestKnowledgeBaseDocuments.html") operation. Best practice is to create a separate
 vector store for each knowledge base to ensure data synchronization.


When you delete a knowledge base or data source resource, Amazon Bedrock offers two data deletion
 policies: `Delete` (default) and `Retain`. If you choose the
 `Delete` policy, vectors in the vector index and vector bucket are
 automatically deleted.


### Querying and retrieval


After your knowledge base is set up, you can do the following:



* **Retrieve chunks** from your source data using the
 [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html") API
 operation.
* **Generate responses** based on retrieved chunks using
 the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html") API operation.
* **Test queries** directly in the Amazon Bedrock console.

Responses are returned with citations to the original source data.


## Limitations


When using S3 Vectors with Amazon Bedrock Knowledge Bases, you should know the following limitations:



* **Semantic search only**: S3 Vectors supports semantic
 search but not hybrid search capabilities.
* **S3 Vectors size limits**: Each vector has a total
 metadata size limit and a size limit for filterable metadata, which may limit custom
 metadata and filtering options. For more information about metadata and filterable
 metadata size limits per vector, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").
* **Chunking strategy constraints**: Limited to models that
 split content into chunks of up to 500 tokens due to metadata size restrictions.
* **Floating-point vectors only**: Binary vector embeddings
 aren't supported.

For comprehensive guidance on working with Amazon Bedrock Knowledge Bases, see [Retrieve data and
 generate AI responses with Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html") in the *Amazon Bedrock User
 Guide*.
