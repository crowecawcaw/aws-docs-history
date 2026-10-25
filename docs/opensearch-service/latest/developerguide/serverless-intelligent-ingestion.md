

# Overview of Amazon OpenSearch intelligent ingestion
<a name="serverless-intelligent-ingestion"></a>

Amazon OpenSearch intelligent ingestion is a native, on-demand, serverless capability that makes data from supported data sources searchable in OpenSearch Serverless. You choose a data source, such as Amazon Simple Storage Service (Amazon S3), select how to process the data, and specify a target index. Intelligent ingestion discovers the source objects, processes their content, and indexes the results for you.

Intelligent ingestion supports both structured data and documents. For structured data, it can apply transformations and optionally generate vector embeddings. For documents, it can preserve document structure, describe visual content, divide text into retrieval-sized chunks, generate embeddings, and write the resulting text, vectors, and metadata to a vector index.

You create and manage ingestion directly from your OpenSearch Serverless NextGen collection. You don't have to create and manage a separate ingestion pipeline or provision document-processing infrastructure to get started. Intelligent ingestion automatically scales capacity with your workload, up to the collection's maximum OpenSearch Compute Unit (OCU) limit. If you want to manage the ingestion infrastructure yourself, you can get started with [Overview of Amazon OpenSearch Ingestion](ingestion.md).

Before you configure ingestion, confirm that your source is supported. Intelligent ingestion supports the following data sources:
+ [Ingesting from Amazon S3](serverless-intelligent-ingestion-s3.md)

**Topics**
+ [Getting started with intelligent ingestion](#serverless-intelligent-ingestion-getting-started)
+ [Benefits of intelligent ingestion](#serverless-intelligent-ingestion-benefits)
+ [Comparison with OpenSearch Ingestion](#serverless-intelligent-ingestion-comparison)
+ [Ingestion patterns](#serverless-intelligent-ingestion-modes)
+ [Intelligent ingestion pricing](#serverless-intelligent-ingestion-pricing)
+ [Supported AWS Regions](#serverless-intelligent-ingestion-regions)
+ [Limitations](#serverless-intelligent-ingestion-limitations)
+ [Ingesting from Amazon S3](serverless-intelligent-ingestion-s3.md)

## Getting started with intelligent ingestion
<a name="serverless-intelligent-ingestion-getting-started"></a>

This topic walks you through creating your first ingestion job, which loads an existing dataset into your collection so that you can start querying it without building a custom pipeline.

Before you begin, you need an AWS account, an OpenSearch Serverless NextGen collection, and an AWS Identity and Access Management (IAM) identity with permissions to call the ingestion APIs and access the source and destination. For more information, see [Ingesting from Amazon S3](serverless-intelligent-ingestion-s3.md).

To create your first ingestion job:

1. Prepare a supported data source, such as an Amazon S3 bucket, that contains your data or documents.

1. Create or select an OpenSearch Serverless NextGen collection.

1. Grant your IAM identity the permissions to create ingestion jobs and to access the source and destination, as described in [Ingestion jobs](serverless-intelligent-ingestion-s3.md#serverless-intelligent-ingestion-s3-jobs). Ingestion streams additionally use a dedicated ingestion role that the service assumes.

1. In the OpenSearch Service console, open the collection and choose the **Ingestion** tab.

1. Choose **Create ingestion job**, select **One-time job**, and configure the source, processing behavior, and destination index.

1. Validate the configuration, review the settings, and create the job.

1. Monitor the job until processing completes, and then query the target index to verify the results.

To keep an index synchronized as new data arrives, create an ingestion stream by using **Continuous streaming** or **Backfill then stream**. For source-specific setup, such as configuring event notifications, see [Ingesting from Amazon S3](serverless-intelligent-ingestion-s3.md).

For more information, see the following topics:
+ [Ingesting from Amazon S3](serverless-intelligent-ingestion-s3.md)

## Benefits of intelligent ingestion
<a name="serverless-intelligent-ingestion-benefits"></a>

Intelligent ingestion provides the following benefits:
+ **Ingest data without managing a separate pipeline.** Start from your OpenSearch Serverless NextGen collection and choose a data source such as Amazon S3. Intelligent ingestion provisions and scales the infrastructure required to process the data.
+ **Make documents ready for semantic search.** Parse documents, retain useful structure such as headings and tables, chunk the extracted content, and generate vector embeddings.
+ **Make visual information searchable.** Generate text descriptions for supported charts, diagrams, screenshots, photographs, and other images contained in documents.
+ **Process structured and unstructured content.** Ingest supported structured formats such as JSON, NDJSON, and JSON array, and document formats such as PDF, Word, and Markdown.
+ **Choose a one-time job or continuous ingestion.** Run a one-time ingestion job for an existing dataset, or create an ingestion stream that processes new objects as they arrive.
+ **Pay for active processing.** Intelligent ingestion scales processing capacity based on the workload and stops charging for ingestion processing after a job completes.

## Comparison with OpenSearch Ingestion
<a name="serverless-intelligent-ingestion-comparison"></a>

Intelligent ingestion and Amazon OpenSearch Ingestion are complementary capabilities. Choose the service that matches your source data and the amount of pipeline control that you need.

The following table compares intelligent ingestion with OpenSearch Ingestion.


| Consideration | Intelligent ingestion | OpenSearch Ingestion | 
| --- | --- | --- | 
| Primary use case | Make structured data and documents from your sources searchable | Stream and transform operational data such as logs, metrics, and traces | 
| Ease of use | Native serverless feature with no infrastructure to manage; ready to use from your active collection | Create and manage the ingestion pipeline as a standalone AWS resource, with more customization | 
| Configuration model | Configure ingestion from the destination collection | Create and manage a separate ingestion pipeline | 
| Processing model | Select managed transformations and intelligent document-processing options | Define a Data Prepper pipeline with supported sources, processors, and sinks | 
| Ingestion patterns | One-time job, continuous streaming, or backfill then stream | Long-running streaming pipelines and supported pull-based sources | 
| Document intelligence | Built-in parsing, image understanding, chunking, and embedding generation | Build the required processing from supported pipeline components or external services | 
| Capacity management | Capacity scales with active work | Configure minimum and maximum pipeline capacity | 

Use intelligent ingestion when your data is in a supported source, such as Amazon S3, and you want the shortest managed path from source content to a searchable index. Use OpenSearch Ingestion when you need Data Prepper pipeline configuration, broader operational telemetry integrations, or more direct control over a streaming transformation pipeline.

## Ingestion patterns
<a name="serverless-intelligent-ingestion-modes"></a>

Intelligent ingestion provides ingestion jobs for finite datasets and ingestion streams for data that continues to arrive.

The following table describes the intelligent ingestion patterns.


| Pattern | Resource | Use when | Behavior | 
| --- | --- | --- | --- | 
| One-time job | Ingestion job | You need to load or reload a fixed dataset | Scans the configured source location, processes the existing objects, and completes | 
| Continuous streaming | Ingestion stream | You are starting with an empty or new source location | Ingests event notifications from the source as objects arrive | 
| Backfill then stream | Ingestion stream | You have a source location that contains existing objects and continues to receive new objects | Ingests the existing objects first, and then continues processing new-object notifications | 

Use an ingestion job for migrations, backfills, proofs of concept, and other one-time loads. You can also schedule a job to run on a regular, repeating basis for recurring loads. Use an ingestion stream for document repositories, knowledge bases, and other datasets that must remain synchronized with the source.

## Intelligent ingestion pricing
<a name="serverless-intelligent-ingestion-pricing"></a>

Intelligent ingestion charges for the processing that your workload uses. Depending on your configuration and content, charges can include:

**Important**  
Intelligent ingestion incurs charges based on the compute, document processing, and model usage that your workload consumes.
+ Ingestion compute used to read, transform, and index data.
+ Additional document-processing compute used to parse and chunk documents.
+ Model input and output tokens used for image understanding.
+ Embedding-model inference, when applicable to the selected configuration.

Charges for the destination OpenSearch Serverless NextGen collection, including indexing, search, and storage, are separate from intelligent ingestion charges. Ingestion jobs stop consuming ingestion capacity after they complete. Ingestion streams consume processing resources when they process available work.

For more information about current rates and regional pricing, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/). For more information about model rates, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

## Supported AWS Regions
<a name="serverless-intelligent-ingestion-regions"></a>

Intelligent ingestion is available in a subset of the AWS Regions where Amazon OpenSearch Service is available. Supported content types, processing options, and destination types can also vary by Region.

Intelligent ingestion is available in the following AWS Regions:
+ US East (N. Virginia) (`us-east-1`)
+ US East (Ohio) (`us-east-2`)
+ US West (Oregon) (`us-west-2`)
+ Europe (Ireland) (`eu-west-1`)
+ Europe (Frankfurt) (`eu-central-1`)
+ Asia Pacific (Tokyo) (`ap-northeast-1`)

For more information about Region availability, see [Amazon OpenSearch Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html) in the *AWS General Reference*.

## Limitations
<a name="serverless-intelligent-ingestion-limitations"></a>

Intelligent ingestion has the following limitations:
+ Each account supports a maximum of 100 ingestion jobs and 20 ingestion streams. These are soft limits that you can increase by requesting a quota increase in Service Quotas.