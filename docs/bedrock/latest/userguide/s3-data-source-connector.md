# Connect to Amazon S3 for your knowledge base

Amazon S3 is an object storage service that stores data as objects within buckets.
You can connect to your Amazon S3 bucket for your Amazon Bedrock knowledge base by using either
the [AWS Management Console for Amazon Bedrock](https://console.aws.amazon.com/bedrock/home "https://console.aws.amazon.com/bedrock/home")
or the [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md")
API (see Amazon Bedrock [supported SDKs and AWS CLI](../APIReference/welcome.md "../APIReference/welcome.md")).

You can upload a small batch of files to an Amazon S3 bucket using the Amazon S3 console or API.
You can alternatively use [AWS DataSync](../../../datasync/latest/userguide/create-s3-location.md "../../../datasync/latest/userguide/create-s3-location.md") to upload
multiple files to S3 continuously, and transfer files on a schedule from on-premises, edge,
other cloud, or AWS storage.

Currently only General Purpose S3 buckets are supported.

There are limits to how many files and MB per file that can be crawled. See [Quotas for knowledge bases](quotas.md "quotas.md").

###### Topics

- [Supported features](#supported-features-s3-connector "#supported-features-s3-connector")
- [Prerequisites](#prerequisites-s3-connector "#prerequisites-s3-connector")
- [Connection configuration](#configuration-s3-connector "#configuration-s3-connector")

## Supported features

- Document metadata fields
- Inclusion prefixes
- Incremental content syncs for added, updated, deleted content

## Prerequisites

**In Amazon S3, make sure you**:

- Note the Amazon S3 bucket URI, Amazon Resource Name (ARN), and the AWS
  account ID for the owner of the bucket. You can find the URI and ARN
  in the properties section in the Amazon S3 console. Your bucket must be in the
  same Region as your Amazon Bedrock knowledge base. You must
  have permission to access the bucket.

**In your AWS account, make sure you**:

- Include the necessary permissions to connect to your data source in your
  AWS Identity and Access Management (IAM) role/permissions policy for your
  knowledge base. For information on the required permissions for this data source
  to add to your knowledge base IAM role, see
  [Permissions to access data sources](kb-permissions.md#kb-permissions-access-ds "kb-permissions.md#kb-permissions-access-ds").

###### Note

If you use the console, the IAM role with all the required permissions
can be created for you as part of the steps for creating a knowledge base. After
you have configured your data source and other configurations, the IAM
role with all the required permissions are applied to your specific knowledge base.

## Connection configuration

To connect to your Amazon S3 bucket, you must provide the necessary configuration
information so that Amazon Bedrock can access and crawl your data. You must also follow the
[Prerequisites](#prerequisites-s3-connector "#prerequisites-s3-connector").

An example of a configuration for this data source is included in this section.

For more information about inclusion filters,
document metadata fields, incremental syncing, and how these work, select
the following:

You can include a separate file that specifies the document metadata fields/attributes for each
file in your Amazon S3 data source and whether to include them in the embeddings when indexing the data source into the vector store. For example, you can
create a file in the following format, name it `fileName.extension.metadata.json` and upload it to your S3 bucket.

```

{
  "metadataAttributes": {
    "company": {
      "value": {
        "type": "STRING",
        "stringValue": "BioPharm Innovations"
      },
      "includeForEmbedding": true
    },
    "created_date": {
      "value": {
        "type": "NUMBER",
        "numberValue": 20221205
      },
      "includeForEmbedding": true
    },
    "author": {
      "value": {
        "type": "STRING",
        "stringValue": "Lisa Thompson"
      },
      "includeForEmbedding": true
    },
    "origin": {
      "value": {
        "type": "STRING",
        "stringValue": "Overview"
      },
      "includeForEmbedding": true
    }
  }
}
```

The metadata file must use the same name as its associated source document file,
with `.metadata.json` appended onto the end of the file name. The metadata file
must be stored in the same folder or location as the source file in your Amazon S3 bucket. The file
must not exceed the limit of 10 KB. For information on the supported attribute/field data types
and the filtering operators you can apply to your metadata fields, see [Metadata and filtering](kb-test-config.md "kb-test-config.md").

You can specify an inclusion prefix, which is an Amazon S3 path prefix, where you can use an S3 file
or a folder instead of the entire bucket to create the S3 data source connector.

The data source connector crawls new, modified, and deleted content each time your data
source syncs with your knowledge base. Amazon Bedrock can use your data source’s mechanism
for tracking content changes and crawl content that changed since the last sync. When you sync
your data source with your knowledge base for the first time, all content is crawled by default.

To sync your data source with your knowledge base, use the [StartIngestionJob](../APIReference/API_agent_StartIngestionJob.md "../APIReference/API_agent_StartIngestionJob.md")
API or select your knowledge base in the console and select **Sync** within the
data source overview section.

###### Important

All data that you sync from your data source becomes available to anyone with
`bedrock:Retrieve` permissions to retrieve the data. This can also include any
data with controlled data source permissions. For more
information, see [Knowledge base permissions](kb-permissions.md "kb-permissions.md").

Console

###### To connect an Amazon S3 bucket to your knowledge base

1. Follow the steps at [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](knowledge-base-create.md "knowledge-base-create.md") and choose **Amazon S3** as the data source.
2. Provide a name for the data source.
3. Specify whether the Amazon S3 bucket is in your current AWS
   account or another AWS account. Your bucket must be in the
   same Region as the knowledge base.
4. (Optional) If the Amazon S3 bucket is encrypted with a KMS key, include the key. For more information, see [Permissions to decrypt your AWS KMS key for your data sources in
   Amazon S3](encryption-kb.md#encryption-kb-ds "encryption-kb.md#encryption-kb-ds").
5. (Optional) In the **Content parsing and chunking** section, you can customize how to parse and chunk your data. Refer to the following resources to learn more about these customizations:
   - For more information about parsing options, see [Parsing options for your data source](kb-advanced-parsing.md "kb-advanced-parsing.md").
   - For more information about chunking strategies, see [How content chunking works for knowledge bases](kb-chunking.md "kb-chunking.md").

   ###### Warning

   You can't change the chunking strategy after connecting to the data source.
   - For more information about how to customize chunking of your data and processing of your metadata with a Lambda function, see [Use a custom transformation Lambda function to define how your data is ingested](kb-custom-transformation.md "kb-custom-transformation.md").

6. In the **Advanced settings** section, you can optionally configure the following:
   - **KMS key for transient data storage.** – You can encrypt the transient data while converting your data into embeddings with the default AWS managed key or your own KMS key. For more information, see [Encryption of transient data storage during data ingestion](encryption-kb.md#encryption-kb-ingestion "encryption-kb.md#encryption-kb-ingestion").
   - **Data deletion policy** – You can delete the vector embeddings for your data source that are stored in the vector store by default, or choose to retain the vector store data.

7. Continue to choose an embeddings model and vector store. To see the remaining steps, return to [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](knowledge-base-create.md "knowledge-base-create.md") and continue from the step after connecting your data source.

API
The following is an example of a configuration for connecting
to Amazon S3 for your Amazon Bedrock knowledge base. You configure your data
source using the API with the AWS CLI or supported SDK, such as Python.
After you call [CreateKnowledgeBase](../APIReference/API_agent_CreateKnowledgeBase.md "../APIReference/API_agent_CreateKnowledgeBase.md"), you call [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") to create your data
source with your connection information in `dataSourceConfiguration`.

To learn about customizations that you can apply to ingestion by including the optional
`vectorIngestionConfiguration` field, see [Customize ingestion for a data source](kb-data-source-customize-ingestion.md "kb-data-source-customize-ingestion.md").

**AWS Command Line Interface**

```
aws bedrock-agent create-data-source \
 --name "S3-connector" \
 --description "S3 data source connector for Amazon Bedrock to use content in S3" \
 --knowledge-base-id "your-knowledge-base-id" \
 --data-source-configuration file://s3-bedrock-connector-configuration.json \
 --data-deletion-policy "DELETE" \
 --vector-ingestion-configuration '{"chunkingConfiguration":{"chunkingStrategy":"FIXED_SIZE","fixedSizeChunkingConfiguration":{"maxTokens":100,"overlapPercentage":10}}}'

s3-bedrock-connector-configuration.json
{
    "s3Configuration": {
	    "bucketArn": "arn:aws:s3:::bucket-name",
	    "bucketOwnerAccountId": "000000000000",
	    "inclusionPrefixes": [
	        "documents/"
	    ]
    },
    "type": "S3"
}
```
