# Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases

When you create a knowledge base by connecting to a data source, you set up or specify the following:

- General information that defines and identifies the knowledge base
- The service role with permissions to the knowledge base.
- Configurations for the knowledge base, including the embeddings model to use when converting data from the data source, storage configurations for the service in which to store the embeddings, and, optionally, an S3 location to store multimodal data.

###### Note

You can’t create a knowledge base with a root user. Log in with an IAM user before starting these steps.

Expand the section that corresponds to your use case:

###### To set up a knowledge base

1.  Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
    [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2.  In the left navigation pane, choose **Knowledge bases**.
3.  In the **Knowledge bases** section, choose the create button and select to create a knowledge base with a vector store.
4.  (Optional) Change the default name and provide a description for your knowledge base.
5.  Choose an AWS Identity and Access Management (IAM) role that provides Amazon Bedrock
    permission to access other required AWS services. You can let Amazon Bedrock create the service role or
    choose to use your own [custom role that you created for
    Neptune Analytics](kb-permissions.md#kb-permissions-neptune "kb-permissions.md#kb-permissions-neptune").
6.  Choose a data source to connect your knowledge base to.
7.  (Optional) Add tags to your knowledge base. For more information, see
    [Tagging Amazon Bedrock resources](tagging.md "tagging.md").
8.  (Optional) Configure services for which to deliver activity logs for your knowledge base.
9.  Go to the next section and follow the steps at [Connect a data source to your knowledge base](data-source-connectors.md "data-source-connectors.md") to configure a data source.
10. In the **Embeddings model** section, do the following:
    1. Choose an embeddings model to convert your data into vector embeddings.
    2. (Optional) Expand the **Additional configurations** section to see the following configuration options (not all models support all configurations):
       - **Embeddings type** – Whether to convert the data to floating-point (float32) vector embeddings (more precise, but more costly) or binary vector embeddings (less precise, but less costly). To learn about which embeddings models support binary vectors, refer to [supported embeddings models](knowledge-base-supported.md "knowledge-base-supported.md").
       - **Vector dimensions** – Higher values improve accuracy but increase cost and latency.

11. In the **Vector database** section, do the following:
    1.  Choose a vector store to store the vector embeddings that will be used for query. You have the following options:
        - **Quick create a new vector store** – choose one of the available
          vector stores for Amazon Bedrock to create. You can also optionally configure AWS KMS key encryption for your
          vector store.

        ###### Note

        When using this option, Amazon Bedrock automatically handles the metadata placement for each vector store.

            + **Amazon OpenSearch Serverless** – Amazon Bedrock Knowledge Bases creates an Amazon OpenSearch Serverless vector search collection and index and configures it with the required fields for you.
            + **Amazon Aurora PostgreSQL Serverless** – Amazon Bedrock sets up an Amazon Aurora PostgreSQL Serverless vector store. This process takes unstructured text data from
             an Amazon S3 bucket, transforms it into text chunks and vectors, and then stores them in a PostgreSQL database. For more information, see [Quick create an Aurora PostgreSQL Knowledge Base for Amazon Bedrock](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.md").
            + **Amazon Neptune Analytics** – Amazon Bedrock uses Retrieval Augmented Generation (RAG) techniques combined with graphs to enhance generative AI applications so that end users can get more accurate and comprehensive responses.
            + **Amazon S3 Vectors** – Amazon Bedrock Knowledge Bases creates an S3 vector bucket and a vector index that will store the embeddings
             generated from your data sources.


            ###### Important

            The Amazon S3 Vectors integration with Amazon Bedrock Knowledge Bases is in preview release
             and is subject to change.


            You can create a knowledge base for Amazon S3 Vectors in all AWS Regions where both Amazon Bedrock and
             Amazon S3 Vectors are available. For region availability information, see [Amazon S3 Vectors](../../../AmazonS3/latest/userguide/s3-vectors.md "../../../AmazonS3/latest/userguide/s3-vectors.md") in the *Amazon S3 User Guide*.


            ###### Note

            When Amazon Bedrock Knowledge Bases creates a vector index for you, it can attach up to a maximum of 40 KB of metadata for each
             vector. Within this 40 KB, up to a maximum of 2 KB can be used as filterable metadata.

            Amazon Bedrock will store the text in the non-filterable space as the `AMAZON_BEDROCK_TEXT`
             key. The metadata added by Amazon Bedrock is stored in the filterable metadata space. For more information about
             S3 vector bucket metadata limitations, see [Prerequisites for
             using Amazon S3 Vectors with Amazon Bedrock Knowledge Bases](knowledge-base-setup.md#knowledge-base-setup-s3 "knowledge-base-setup.md#knowledge-base-setup-s3").

        - **Choose a vector store you have created** – Select a supported vector store and identify the vector field names and metadata
          field names in the vector index. For more information, see [Prerequisites for using a vector store you created for a
          knowledge base](knowledge-base-setup.md "knowledge-base-setup.md").

        ###### Note

        If your data source is a Confluence, Microsoft SharePoint, or Salesforce instance, the only supported vector store service is Amazon OpenSearch Serverless.

    2.  (Optional) Expand the **Additional configurations** section and modify any relevant configurations.

12. If your data source contains images, specify an Amazon S3 URI in which to store the images that the parser will extract from the data in the **Multimodal storage destination**. The images can be returned during query. You can also optionally choose a customer managed key instead of the default AWS managed key to encrypt your data.

###### Note

Multimodal data is only supported with Amazon S3 and custom data sources. 13. Choose **Next** and review the details of your knowledge base. You can edit any
section before going ahead and creating your knowledge base.

###### Note

The time it takes to create the knowledge base depends on your specific configurations.
When the creation of the knowledge base has completed, the status of the knowledge base changes to
either state it is ready or available.

Once your knowledge base is ready and available, sync your data source
for the first time and whenever you want to keep your content up to date.
Select your knowledge base in the console and select **Sync** within
the data source overview section.
To create a knowledge base, send a [CreateKnowledgeBase](../APIReference/API_agent_CreateKnowledgeBase.md "../APIReference/API_agent_CreateKnowledgeBase.md") request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt").

###### Note

If you prefer to let Amazon Bedrock create and manage a vector store for you, use the console. For more information, expand the **Use the console** section in this topic.

The following fields are required:

| Field                      | Basic description                                                                                                                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                       | A name for the knowledge base                                                                                                                                                                               |
| roleArn                    | The ARN of an [Amazon Bedrock Knowledge Bases service role](kb-permissions.md "kb-permissions.md").                                                                                                         |
| knowledgeBaseConfiguration | Contains configurations for the knowledge base. See details below.                                                                                                                                          |
| storageConfiguration       | (Only required if you're connecting to an unstructured data source). Contains configurations for the data source service that you choose.                                                                   | The following fields are optional:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Field                      | Use case                                                                                                                                                                                                    |
| ---                        | ---                                                                                                                                                                                                         |
| description                | A description for the knowledge base.                                                                                                                                                                       |
| clientToken                | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md"). |
| tags                       | To associate tags with the flow. For more information, see [Tagging Amazon Bedrock resources](tagging.md "tagging.md").                                                                                     | In the `knowledgeBaseConfiguration` field, which maps to a [KnowledgeBaseConfiguration](../APIReference/API_agent_KnowledgeBaseConfiguration.md "../APIReference/API_agent_KnowledgeBaseConfiguration.md") object, specify `VECTOR` in the `type` field and include a [VectorKnowledgeBaseConfiguration](../APIReference/API_agent_VectorKnowledgeBaseConfiguration.md "../APIReference/API_agent_VectorKnowledgeBaseConfiguration.md") object. In the object, include the following fields: <br>• `embeddingModelArn` – The ARN of the embedding model to use. <br>• `embeddingModelConfiguration` – Configurations for the embedding model. To see the possible values you can specify for each supported model, see [Supported models and Regions for Amazon Bedrock knowledge bases](knowledge-base-supported.md "knowledge-base-supported.md"). <br>• (If you plan to include multimodal data, which includes images, figures, charts, or tables, in your knowledge base) `supplementalDataStorageConfiguration` – Maps to a [SupplementalDataStorageLocation](../APIReference/API_agent_SupplementalDataStorageLocation.md "../APIReference/API_agent_SupplementalDataStorageLocation.md") object, in which you specify the S3 location in which to store the extracted data. For more information, see [Parsing options for your data source](kb-advanced-parsing.md "kb-advanced-parsing.md"). In the `storageConfiguration` field, which maps to a [StorageConfiguration](../APIReference/API_agent_StorageConfiguration.md "../APIReference/API_agent_StorageConfiguration.md") object, specify the vector store that you plan to connect to in the `type` field and include the field that corresponds to that vector store. See each vector store configuration type at [StorageConfiguration](../APIReference/API_agent_StorageConfiguration.md "../APIReference/API_agent_StorageConfiguration.md") for details about the information you need to provide. The following shows an example request to create a knowledge base connected to an Amazon OpenSearch Serverless collection. The data from connected data sources will be converted into binary vector embeddings with Amazon Titan Text Embeddings V2 and multimodal data extracted by the parser is set up to be stored in a bucket called `MyBucket`. `PUT /knowledgebases/ HTTP/1.1 Content-type: application/json { "name": "MyKB", "description": "My knowledge base", "roleArn": "arn:aws:iam::111122223333:role/service-role/AmazonBedrockExecutionRoleForKnowledgeBase_123", "knowledgeBaseConfiguration": { "type": "VECTOR", "vectorKnowledgeBaseConfiguration": { "embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0", "embeddingModelConfiguration": { "bedrockEmbeddingModelConfiguration": { "dimensions": 1024, "embeddingDataType": "BINARY" } }, "supplementalDataStorageConfiguration": { "storageLocations": [ { "s3Location": { "uri": "arn:aws:s3:::MyBucket" }, "type": "S3" } ] } } }, "storageConfiguration": { "opensearchServerlessConfiguration": { "collectionArn": "arn:aws:aoss:us-east-1:111122223333:collection/abcdefghij1234567890", "fieldMapping": { "metadataField": "metadata", "textField": "text", "vectorField": "vector" }, "vectorIndexName": "MyVectorIndex" } } }` ###### Topics <br>• [Connect a data source to your knowledge base](data-source-connectors.md "data-source-connectors.md") <br>• [Customize ingestion for a data source](kb-data-source-customize-ingestion.md "kb-data-source-customize-ingestion.md") <br>• [Set up security configurations for your knowledge base](kb-create-security.md "kb-create-security.md") |
