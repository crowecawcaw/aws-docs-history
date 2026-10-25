

# Ingesting from Amazon S3
<a name="serverless-intelligent-ingestion-s3"></a>

Intelligent ingestion reads structured data and unstructured documents from Amazon Simple Storage Service (Amazon S3), processes their content, and indexes the results in your Amazon OpenSearch Serverless (OpenSearch Serverless) NextGen collection. This topic explains how intelligent ingestion works with Amazon S3 and the content that it processes.

**Topics**
+ [How it works](#serverless-intelligent-ingestion-s3-how-it-works)
+ [Supported content](#serverless-intelligent-ingestion-s3-supported-content)
+ [Availability](#serverless-intelligent-ingestion-s3-availability)
+ [Preparing an index for document extraction](#serverless-intelligent-ingestion-s3-document-index)
+ [Ingestion jobs](#serverless-intelligent-ingestion-s3-jobs)
+ [Ingestion streams](#serverless-intelligent-ingestion-s3-streams)
+ [Limitations for ingesting from Amazon S3](#serverless-intelligent-ingestion-s3-limitations)

## How it works
<a name="serverless-intelligent-ingestion-s3-how-it-works"></a>

When you configure intelligent ingestion, you specify a source and a destination. Intelligent ingestion then applies the appropriate processing based on the content:

1. **Source** – An Amazon S3 bucket and, optionally, a key prefix that identifies the objects to ingest. Continuous ingestion also uses an Amazon Simple Queue Service (Amazon SQS) queue to receive Amazon S3 event notifications.

1. **Processing** – The operations that intelligent ingestion applies to your content. Depending on the content, these operations can include parsing, image understanding, chunking, and embedding generation.

1. **Destination** – The OpenSearch Serverless NextGen collection and index where intelligent ingestion writes the processed data.

Intelligent ingestion then performs the applicable stages of the following workflow:

1. Discovers objects in the configured Amazon S3 location.

1. Identifies the supported content type and selects the appropriate processing path.

1. Parses and chunks unstructured objects, such as PDF and Word documents, runs image understanding for images that they contain, and then processes the resulting structured data.

1. Processes structured content, generates vector embeddings, and indexes the results into the OpenSearch Serverless NextGen collection.

1. Writes the processed content, vectors, and source metadata to the target index.

Monitor the ingestion status and the number of objects scanned, indexed, and failed from the Amazon OpenSearch Service console.

## Supported content
<a name="serverless-intelligent-ingestion-s3-supported-content"></a>

The processing behavior depends on the source content and the options that you select.

### Structured data
<a name="serverless-intelligent-ingestion-s3-structured-data"></a>

For supported structured formats, intelligent ingestion can:
+ Read records from JSON, newline-delimited JSON (NDJSON), and JSON array objects.
+ Apply supported field and document transformations.
+ Generate vector embeddings for configured text fields.
+ Index the transformed documents and associated vectors.

### Documents
<a name="serverless-intelligent-ingestion-s3-documents"></a>

For supported input document formats, intelligent ingestion can:
+ Extract text from PDF, Word, Markdown, and plain text documents.
+ Preserve useful document organization, including headings, reading order, and tables.
+ Divide extracted content into chunks for retrieval.
+ Generate sparse embeddings and create documents suitable for a vector index.
+ Retain source information as metadata so applications can identify the original Amazon S3 object.

Sparse-embedding generation requires a target index with automatic semantic enrichment enabled on the `text` field. Create this index before you run the ingestion. For more information, see [Preparing an index for document extraction](#serverless-intelligent-ingestion-s3-document-index).

### Images in documents
<a name="serverless-intelligent-ingestion-s3-images"></a>

In AWS Regions that support image understanding, intelligent ingestion uses a vision-language model to generate text descriptions of supported images found in documents. Intelligent ingestion indexes the generated descriptions with the surrounding document content. This helps search and retrieval applications find information that appears only in charts, diagrams, screenshots, or photographs.

Intelligent ingestion uses image understanding only for documents that contain images selected for processing.

**Important**  
Model inference charges are separate from ingestion and document-processing charges.

## Availability
<a name="serverless-intelligent-ingestion-s3-availability"></a>

With intelligent ingestion, you can use Amazon S3 as a source and OpenSearch Serverless NextGen collections as destinations. You can place the source bucket in the same AWS account as the collection or in another AWS account. Cross-account sources require an AWS Identity and Access Management (IAM) role and resource policies that grant access to the source resources.

For continuous ingestion, configure Amazon S3 event notifications to send supported object events to an Amazon SQS queue. Intelligent ingestion currently doesn't support OpenSearch Serverless Classic collections or OpenSearch Service managed domains as destinations.

## Preparing an index for document extraction
<a name="serverless-intelligent-ingestion-s3-document-index"></a>

For document extraction use cases, intelligent ingestion generates sparse embeddings by using automatic semantic enrichment. To generate the embeddings, the target index must have semantic enrichment enabled on the `text` field, which is where intelligent ingestion writes the extracted content. Create the index before you run the ingestion job or stream. If the index doesn't exist when ingestion starts, intelligent ingestion creates it without semantic enrichment, and the extracted content is indexed without sparse embeddings.

Automatic semantic enrichment requires additional permissions beyond the ingestion permissions described in the following sections. To configure these permissions, and for more information about semantic enrichment, see [Automatic semantic enrichment for Serverless](serverless-semantic-enrichment.md).

The following AWS CLI command creates an index with semantic enrichment enabled on the `text` field. Replace the {{placeholder values}} with your own information:

```
aws opensearchserverless create-index \
    --id {{collection-id}} \
    --index-name {{my-index}} \
    --index-schema '{
      "mappings": {
        "properties": {
          "text": {
            "type": "text",
            "semantic_enrichment": {
              "status": "ENABLED",
              "language_options": "english"
            }
          }
        }
      }
    }' \
    --region {{region}}
```

This command includes the following placeholders:
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.
+ {{my-index}} – The index where intelligent ingestion writes the processed data.
+ {{region}} – The AWS Region of the collection.

Set `language_options` to `english` for English content or `multi-lingual` for other supported languages. For the list of supported languages, see [Languages supported](serverless-semantic-enrichment.md#serverless-semantic-enrichment-languages).

### Document extraction fields
<a name="serverless-intelligent-ingestion-s3-document-fields"></a>

Intelligent ingestion divides each source document into chunks and indexes each chunk as a separate document. Each indexed document contains the following fields:
+ `text` – The text content extracted from the chunk. When semantic enrichment is enabled on this field, the service generates a sparse embedding for the chunk during ingestion.
+ `text_embedding` – The sparse embedding that semantic enrichment generates from the `text` field. The embedding maps expanded terms to their significance weights. Semantic enrichment stores the embedding for each enriched field in a companion `{{field}}_embedding` field.
+ `headings` – The document headings that apply to the chunk, which preserve the position of the chunk in the document structure.
+ `ingestionSource` – Source metadata that identifies the original Amazon S3 object, including the full object URI (`s3_uri`) and the bucket name (`s3_bucket`).

Intelligent ingestion also sets the document routing value (`_routing`) based on the source bucket and object key, so chunks from the same source object are stored together.

The following example shows an indexed document that intelligent ingestion created from a PDF document. The `text_embedding` field is truncated for readability:

```
{
  "_index": "my-index",
  "_id": "04f19ce9-66d3-314f-9b4c-2ab3dfe00b3c",
  "_source": {
    "text": "ANNUAL REPORT PURSUANT TO SECTION 13 OR 15(d) OF THE SECURITIES EXCHANGE ACT OF 1934\nFor the fiscal year ended December 31, 2023 ...",
    "headings": [
      "FORM 10-K"
    ],
    "text_embedding": {
      "annual": 0.5791626,
      "report": 0.7689024,
      "securities": 0.5554248,
      "fiscal": 0.43134204,
      "exchange": 0.52630055
    },
    "ingestionSource": {
      "s3_uri": "s3://amzn-s3-demo-bucket/documents/annual-report.pdf",
      "s3_bucket": "amzn-s3-demo-bucket"
    }
  }
}
```

## Ingestion jobs
<a name="serverless-intelligent-ingestion-s3-jobs"></a>

Run a one-time ingestion job to load or reload an existing Amazon S3 dataset into your OpenSearch Serverless NextGen collection. An ingestion job scans the configured bucket, and optionally a key prefix, processes the supported objects that it finds, and then completes.

An ingestion job doesn't use a separate ingestion role. The identity that creates the job provides the access to the source bucket and the target index. Before you create a job, configure that identity's IAM permissions and grant it access in the collection's data access policy as described in the following sections.

### Job caller permissions
<a name="serverless-intelligent-ingestion-s3-jobs-caller"></a>

Grant the IAM identity that creates and manages ingestion jobs the following permissions policy. The policy allows the identity to call the ingestion job APIs on the collection, access the collection's data plane, and read the source Amazon S3 bucket. Replace the {{placeholder values}} with your own information:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "IngestionJobApis",
      "Effect": "Allow",
      "Action": [
        "aoss:CreateIngestionJob",
        "aoss:GetIngestionJob",
        "aoss:ListIngestionJobs",
        "aoss:CancelIngestionJob"
      ],
      "Resource": [
        "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}",
        "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}/*"
      ]
    },
    {
      "Sid": "CollectionDataPlane",
      "Effect": "Allow",
      "Action": "aoss:APIAccessAll",
      "Resource": "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}"
    },
    {
      "Sid": "ReadSourceBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ]
    }
  ]
}
```

This permissions policy includes the following placeholders:
+ {{111122223333}} – Your AWS account ID.
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.
+ {{amzn-s3-demo-bucket}} – The name of the source Amazon S3 bucket.

### Job access policy
<a name="serverless-intelligent-ingestion-s3-jobs-dap"></a>

In addition to the IAM permissions, the caller identity must be listed as a principal in a data access policy on the collection. The policy must allow the identity to create and write to the target index. The following data access policy rules grant the minimum index permissions that an ingestion job requires. Replace the {{placeholder values}} with your own information:

```
[
  {
    "Rules": [
      {
        "ResourceType": "index",
        "Resource": [
          "index/{{collection-name}}/{{index-name}}*"
        ],
        "Permission": [
          "aoss:CreateIndex",
          "aoss:DescribeIndex",
          "aoss:UpdateIndex",
          "aoss:WriteDocument"
        ]
      }
    ],
    "Principal": [
      "arn:aws:iam::{{111122223333}}:role/{{caller-role-name}}"
    ]
  }
]
```

Scope the index resource to cover both the target index and the failure index. Intelligent ingestion writes documents that fail processing to a failure index named `{{index-name}}-ingestion-failures`.

### Running an ingestion job
<a name="serverless-intelligent-ingestion-s3-jobs-run"></a>

You can create an ingestion job from the OpenSearch Service console or with the AWS Command Line Interface (AWS CLI). Before you begin, configure the caller permissions and the data access policy described in the preceding sections.

**To create an ingestion job (console)**

1. Sign in to the OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Open the collection.

1. On the **Ingestion** tab, choose **Create ingestion job**.

1. Select **One-time job**, and then configure the source, processing behavior, and destination index.

The new job appears on the **Ingestion** tab and starts processing immediately.

Alternatively, the following AWS CLI command creates the ingestion job. Specify the source bucket by its ARN, and optionally a key prefix that limits the objects to scan. Replace the {{placeholder values}} with your own information:

```
aws opensearchserverless create-ingestion-job \
    --collection-id {{collection-id}} \
    --ingestion-job-name {{my-ingestion-job}} \
    --index-name {{my-index}} \
    --source '{"s3":{"bucket":"arn:aws:s3:::{{amzn-s3-demo-bucket}}","bucketOwnerAccountId":"{{111122223333}}","keyPrefix":"{{data/}}"}}' \
    --region {{region}}
```

This command includes the following placeholders:
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.
+ {{my-ingestion-job}} – A name that you choose for the job.
+ {{my-index}} – The index where intelligent ingestion writes the processed data.
+ {{amzn-s3-demo-bucket}} – The name of the source Amazon S3 bucket.
+ {{111122223333}} – The AWS account ID of the bucket owner.
+ {{data/}} – An optional key prefix that limits the objects to scan.
+ {{region}} – The AWS Region of the collection.

The job starts immediately and runs until it processes the matching objects. Depending on the number and size of the objects, the job can take several minutes or longer to complete. To monitor its progress, run the following AWS CLI command with the `ingestionJobId` value from the create response. The job status changes to `COMPLETED` when processing finishes:

```
aws opensearchserverless get-ingestion-job \
    --collection-id {{collection-id}} \
    --ingestion-job-id {{ingestion-job-id}} \
    --region {{region}}
```

After the job completes, query the target index to verify the results.

## Ingestion streams
<a name="serverless-intelligent-ingestion-s3-streams"></a>

Create an ingestion stream to keep your index synchronized as new Amazon S3 objects arrive. A stream reads Amazon S3 event notifications from an Amazon Simple Queue Service (Amazon SQS) queue and processes the new objects continuously. Before you create a stream, configure Amazon S3 event notifications on the source bucket to send supported object events to an Amazon SQS queue.

Unlike an ingestion job, an ingestion stream uses a dedicated IAM ingestion role. You pass this role when you create the stream, and intelligent ingestion assumes it to read from the queue and the bucket and to write to the target index. You configure two identities for a stream: the ingestion role that the service assumes, and the caller identity that creates the stream and passes the role.

### Stream ingestion role
<a name="serverless-intelligent-ingestion-s3-streams-role"></a>

The ingestion role must trust the intelligent ingestion service so the service can assume it. Attach the following trust policy to the ingestion role. The `aws:SourceArn` condition provides confused-deputy protection by limiting the role to ingestion streams in your collection. Replace the {{placeholder values}} with your own information:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "aoss.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringLike": {
          "aws:SourceArn": "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}/ingestion-stream/*"
        }
      }
    }
  ]
}
```

This trust policy includes the following placeholders:
+ {{region}} – The AWS Region of the collection.
+ {{111122223333}} – Your AWS account ID.
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.

Grant the ingestion role the following permissions policy. The policy allows the role to receive and delete messages from the Amazon SQS queue, read the source Amazon S3 bucket, and access the collection's data plane. Replace the {{placeholder values}} with your own information:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadQueue",
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueUrl",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "arn:aws:sqs:{{region}}:{{111122223333}}:{{queue-name}}"
    },
    {
      "Sid": "ReadSourceBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ]
    },
    {
      "Sid": "CollectionDataPlane",
      "Effect": "Allow",
      "Action": "aoss:APIAccessAll",
      "Resource": "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}"
    }
  ]
}
```

This permissions policy includes the following additional placeholders:
+ {{queue-name}} – The name of the Amazon SQS queue that receives the Amazon S3 event notifications.
+ {{amzn-s3-demo-bucket}} – The name of the source Amazon S3 bucket.

### Stream caller permissions
<a name="serverless-intelligent-ingestion-s3-streams-caller"></a>

Grant the IAM identity that creates and manages ingestion streams the following permissions policy. The policy allows the identity to call the ingestion stream APIs on the collection and to pass the ingestion role to the service. Replace the {{placeholder values}} with your own information:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PassIngestionRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{111122223333}}:role/{{ingestion-role-name}}"
    },
    {
      "Sid": "IngestionStreamApis",
      "Effect": "Allow",
      "Action": [
        "aoss:CreateIngestionStream",
        "aoss:GetIngestionStream",
        "aoss:ListIngestionStreams",
        "aoss:UpdateIngestionStream",
        "aoss:DeleteIngestionStream"
      ],
      "Resource": [
        "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}",
        "arn:aws:aoss:{{region}}:{{111122223333}}:collection/{{collection-id}}/*"
      ]
    }
  ]
}
```

This permissions policy includes the following placeholders:
+ {{111122223333}} – Your AWS account ID.
+ {{ingestion-role-name}} – The name of the ingestion role that the service assumes.
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.

### Stream access policy
<a name="serverless-intelligent-ingestion-s3-streams-dap"></a>

The ingestion role must also be listed as a principal in a data access policy on the collection. Because the service assumes the ingestion role to write documents, grant the index permissions to the ingestion role, not to the caller identity. The following data access policy rules grant the minimum index permissions that an ingestion stream requires. Replace the {{placeholder values}} with your own information:

```
[
  {
    "Rules": [
      {
        "ResourceType": "index",
        "Resource": [
          "index/{{collection-name}}/{{index-name}}*"
        ],
        "Permission": [
          "aoss:CreateIndex",
          "aoss:DescribeIndex",
          "aoss:UpdateIndex",
          "aoss:WriteDocument"
        ]
      }
    ],
    "Principal": [
      "arn:aws:iam::{{111122223333}}:role/{{ingestion-role-name}}"
    ]
  }
]
```

Scope the index resource to cover both the target index and the failure index. Intelligent ingestion writes documents that fail processing to a failure index named `{{index-name}}-ingestion-failures`.

### Creating an ingestion stream
<a name="serverless-intelligent-ingestion-s3-streams-run"></a>

You can create an ingestion stream from the OpenSearch Service console or with the AWS CLI. Before you begin, configure the ingestion role, caller permissions, data access policy, and Amazon S3 event notifications described in the preceding sections.

**To create an ingestion stream (console)**

1. Sign in to the OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Open the collection.

1. On the **Ingestion** tab, create a stream by using **Continuous streaming**.

1. (Optional) To also process the objects that already exist in the Amazon S3 location, use **Backfill then stream** instead.

The new stream appears on the **Ingestion** tab with a status of **Active**.

Alternatively, the following AWS CLI command creates the ingestion stream. Specify the Amazon SQS queue that receives the Amazon S3 event notifications and the ingestion role that the service assumes. Replace the {{placeholder values}} with your own information:

```
aws opensearchserverless create-ingestion-stream \
    --collection-id {{collection-id}} \
    --ingestion-stream-name {{my-ingestion-stream}} \
    --index-name {{my-index}} \
    --role-arn arn:aws:iam::{{111122223333}}:role/{{ingestion-role-name}} \
    --source '{"s3":{"sqsArn":"arn:aws:sqs:{{region}}:{{111122223333}}:{{queue-name}}"}}' \
    --region {{region}}
```

This command includes the following placeholders:
+ {{collection-id}} – The ID of the target OpenSearch Serverless NextGen collection.
+ {{my-ingestion-stream}} – A name that you choose for the stream.
+ {{my-index}} – The index where intelligent ingestion writes the processed data.
+ {{111122223333}} – Your AWS account ID.
+ {{ingestion-role-name}} – The name of the ingestion role that the service assumes.
+ {{queue-name}} – The name of the Amazon SQS queue that receives the Amazon S3 event notifications.
+ {{region}} – The AWS Region of the collection.

The stream becomes active and processes new objects as their event notifications arrive on the queue. To monitor the stream, run the following AWS CLI command with the `ingestionStreamId` value from the create response. The response includes the stream status and the count of objects discovered, ingested, and failed:

```
aws opensearchserverless get-ingestion-stream \
    --collection-id {{collection-id}} \
    --ingestion-stream-id {{ingestion-stream-id}} \
    --region {{region}}
```

When you no longer need the stream, delete it with the `delete-ingestion-stream` command.

## Limitations for ingesting from Amazon S3
<a name="serverless-intelligent-ingestion-s3-limitations"></a>

The following table describes the limitations of intelligent ingestion from Amazon S3.


| Limitation | Details | 
| --- | --- | 
| Unstructured document types | Supports only PDF, Word, plain text, and Markdown | 
| Structured data formats | Supports only JSON, NDJSON, and JSON array | 
| Compressed objects | Supports only uncompressed structured and unstructured objects | 
| Object size for vector-embedding generation | A single unstructured object can be no larger than 60 MB and no more than 150 pages | 