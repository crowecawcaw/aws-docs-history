# Create an Amazon Bedrock knowledge base

with Amazon Neptune Analytics graphs

GraphRAG is fully integrated into Amazon Bedrock Knowledge Bases and uses Amazon Neptune Analytics for graph and
vector storage. You can get started using GraphRAG in your knowledge bases with the
AWS Management Console, the AWS CLI, or the AWS SDK.

You do not need any existing graph infrastructure to get started using GraphRAG. Amazon Bedrock Knowledge Bases
automatically manages the creation and maintenance of the graphs from Amazon Neptune. The
system will automatically create and update a graph by extracting entities, facts, and
relationships from documents that you upload to your Amazon S3 bucket. so you can provide relevant
responses to your end users, without any prior knowledge in graph modeling. The graph will
be stored in Amazon Neptune Analytics.

When you create a knowledge base, you set up or specify the following:

- General information that defines and identifies the knowledge base.
- The service role with permissions to the knowledge base.
- Configurations for the knowledge base, including the embeddings model to use
  when converting data from the data source, and storage configurations for the service
  in which to store the embeddings.

###### Note

You can’t create a knowledge base with a root user. Log in with an IAM user before
starting these steps.

The following shows how to create a knowledge base for using Neptune GraphRAG from
the console and using the CLI.

Console

###### To create a knowledge base for Neptune Analytics from the console

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Knowledge bases** section, choose
   **Create**, and then choose **Knowledge Base with
   vector store**.
4. (Optional) Under **Knowledge Base details**,
   change the default name and provide a description for your knowledge
   base.
5. Under **IAM permissions**, choose an IAM role
   that provides Amazon Bedrock permissions to access other required
   AWS services. You can either have Amazon Bedrock create the service role for
   you, or you can choose to use your own custom role that you've created
   for Neptune Analytics. For an example, see [Permissions to access your vector database in Amazon Neptune Analytics](kb-permissions.md#kb-permissions-neptune "kb-permissions.md#kb-permissions-neptune").
6. Make sure to choose **Amazon S3** as your data source and
   choose **Next** to configure your data source.
7. Provide the **S3 URI** of the file that will be used
   as the data source to connect your knowledge base to and for integrating with
   Amazon Neptune Analytics. For additional steps and optional information you can
   provide, see [Connect a data source to your knowledge base](data-source-connectors.md "data-source-connectors.md").
8. In the **Embeddings model** section, choose an embeddings model to convert your
   data into vector embeddings. Optionally, you can use the **Additional configurations** section
   to specify the vector dimensions. For embeddings type, we recommend that you use floating-point vector embeddings.

###### Note

The vector dimensions of the embeddings model must match the vector dimensions that you specified
when creating the Neptune Analytics graph. 9. In the **Vector database** section, choose the method for creating the vector store, and
then choose **Amazon Neptune Analytics (GraphRAG)** as your vector store to store the
embeddings that will be used for the query. To create your vector store, you can use either of the following
methods:

    * We recommend that you use the **Quick create a new vector store** method to get
     started quickly with creating your vector store. Choose **Amazon Neptune Analytics (GraphRAG)**
     as your vector store. This option
     doesn't require you to have any existing Neptune Analytics resources. The knowledge base automatically
     generates and stores document embeddings in Amazon Neptune, along with a graph representation of entities
     and their relationships derived from the document corpus.
    * Alternatively, if you have already created your Neptune Analytics graph and vector index, you can use
     the **Choose a vector store you have created** option. Choose **Amazon Neptune Analytics (GraphRAG)**
     as your vector store, and identify the graph ARN, vector field names, and metadata field names in the vector
     index. For more information, see [Prerequisites for using a vector store you created for a
     knowledge base](knowledge-base-setup.md "knowledge-base-setup.md").

10. Choose **Next** and review the details of your knowledge base. You can edit any
    section before going ahead and creating your knowledge base.

###### Note

The time it takes to create the knowledge base depends on your specific configurations.
When the creation of the knowledge base has completed, the status of the knowledge base changes to
either state it is ready or available.

Once your knowledge base is ready and available, sync your data source
for the first time and whenever you want to keep your content up to date.
Select your knowledge base in the console and select **Sync** within
the data source overview section. 11. Choose **Create knowledge base**. While Amazon Bedrock is
creating the knowledge base, you should see the status **In
progress**. You must wait for creation to finish before
you can sync a data source. 12. After Amazon Bedrock finishes creating the knowledge base, to configure a data source, follow the
instructions in [Connect a data source to your knowledge base](data-source-connectors.md "data-source-connectors.md").

API

###### To create a knowledge base for Neptune Analytics using the AWS CLI

1. First create a data source using the context enrichment configuration.
   To perform this operation, send a [`CreateDataSource`](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request with an Agents for [Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). The following shows an example
   CLI command.

```
aws bedrock-agent create-data-source \
    --name graph_rag_source \
    --description data_source_for_graph_rag \
    --knowledge-base-id LDBBY2K5AG \
    --cli-input-json "file://input.json"
```

The following code shows the contents of the `input.json` file.

```
{
    "dataSourceConfiguration": {
        "s3Configuration": {
            "bucketArn": "arn:aws:s3:::`<example-graphrag-datasets>`",
            "bucketOwnerAccountId": `"<ABCDEFGHIJ>"`,
            "inclusionPrefixes": [ `<"example-dataset">` ]
        },
        "type": "S3",
    },
    "VectorIngestionConfiguration": {
        "contextEnrichmentConfiguration":
            "type": "BEDROCK_FOUNDATION_MODEL",
            "bedrockFoundationModelConfiguration": {
                "modelArn": "arn:aws:bedrock:`<region>`::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
                "enrichmentStrategyConfiguration": {
                    "method": "CHUNK_ENTITY_EXTRACTION"
            }
        }
    }
}
```

2. To create a knowledge base, send a [`CreateKnowledgeBase`](../APIReference/API_agent_CreateKnowledgeBase.md "../APIReference/API_agent_CreateKnowledgeBase.md") request with an Agents for [Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt"). The following shows an example
   CLI command.

```
aws bi create-knowledge-base \
--name `<"knowledge-base-graphrag">` \
--role-arn arn:aws:iam::`<accountId>`:role/`<BedrockExecutionRoleForKnowledgeBase>` \
--cli-input-json "file://input.json"
```

The following shows the contents of the `input.json` file.

```
{
    "storageConfiguration": {
        "type": "NEPTUNE_ANALYTICS"
        "neptuneAnalyticsConfiguration": {
            "graphArn": "arn:aws:neptune-graph:`<region>`:`<>`:graph/`<graphID>`",
            "fieldMapping": {
                "metadataField": "metadata",
                "textField": "text"
            },
        }
    },
    "knowledgeBaseConfiguration": {
        "type": "VECTOR",
        "vectorKnowledgeBaseConfiguration": {
            "embeddingModelArn": "arn:aws:bedrock:`<region>`::foundation-model/cohere.embed-english-v3"
        }
    }
}
```

3. When your GraphRAG-based application is running, you can continue using the Knowledge Bases API
   operations to provide end users with more comprehensive, relevant, and explainable
   responses. The following sections show you how to start ingestion and perform retrieve
   queries using CLI commands.

## Sync your data source

After you create your knowledge base, you ingest or sync your data so that the data can be queried.
Ingestion extracts the graphical structure and converts the raw data in your data source into vector embeddings, based on the vector embeddings
model and configurations that you specified.

The following command shows an example of how to start an ingestion job using
the CLI.

```
aws bedrock-agent start-ingestion-job \
--data-source-id `<"ABCDEFGHIJ">` \
--knowledge-base-id `<"EFGHIJKLMN">`
```

For more information and how to sync your data source using the
console and API, see [Sync your data with your Amazon Bedrock knowledge base](kb-data-source-sync-ingest.md "kb-data-source-sync-ingest.md").

## Ingest changes into your knowledge base

When using Amazon S3 as your data source, you can modify your data source and sync the changes in one step.
With direct ingestion, you can directly add, update, or delete files in a knowledge base in a single action and
your knowledge base can have access to documents without the need to sync. Direct ingestion uses the `KnowledgeBaseDocuments`
API operations to index the documents that you submit directly into the vector store set up for the knowledge base.
You can also view the documents in your knowledge base directly with these operations, rather than needing to
navigate to the connected data source to view them. For more information, see
[Ingest changes directly into a knowledge base](kb-direct-ingestion.md "kb-direct-ingestion.md").

## Test your knowledge base

Now that you've set up your knowledge base, you can test it by sending querues and generating responses.

The following code shows an example CLI command.

```
aws bedrock-agent-runtime retrieve \
--knowledge-base-id `<"ABCDEFGHIJ">` \
--retrieval-query="{\"text\": \"What are the top three video games available now?\"}"
```

For more information, see [Query a knowledge base connected to an Amazon Neptune Analytics graph](kb-test-neptune.md "kb-test-neptune.md").
