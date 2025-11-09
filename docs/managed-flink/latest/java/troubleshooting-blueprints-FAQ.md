Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Real-time vector embedding blueprints - FAQ

Review the following FAQ about real-time vector embedding blueprints. For more information
about real-time vector embedding blueprints, see [Real-time vector embedding blueprints](../../../msk/latest/developerguide/ai-vector-embedding-integration-learn-more.md "../../../msk/latest/developerguide/ai-vector-embedding-integration-learn-more.md").

###### FAQ

- [What AWS resources does this blueprint create?](#troubleshooting-blueprints-1 "#troubleshooting-blueprints-1")
- [What are my actions after the AWS CloudFormation stack
  deployment is complete?](#troubleshooting-blueprints-2 "#troubleshooting-blueprints-2")
- [What should be the structure of the data in the
  source Amazon MSK topic(s)?](#troubleshooting-blueprints-3 "#troubleshooting-blueprints-3")
- [Can I specify parts of a message to embed?](#troubleshooting-blueprints-4 "#troubleshooting-blueprints-4")
- [Can I read data from multiple Amazon MSK topics?](#troubleshooting-blueprints-5 "#troubleshooting-blueprints-5")
- [Can I use regex to configure Amazon MSK topic names?](#troubleshooting-blueprints-6 "#troubleshooting-blueprints-6")
- [What is the maximum size of a message that can be
  read from an Amazon MSK topic?](#troubleshooting-blueprints-7 "#troubleshooting-blueprints-7")
- [What type of OpenSearch is supported?](#troubleshooting-blueprints-8 "#troubleshooting-blueprints-8")
- [Why do I need to use a vector search collection,
  vector index, and add a vector field in my OpenSearch Serverless colelction?](#troubleshooting-blueprints-9 "#troubleshooting-blueprints-9")
- [What should I set as the dimension for my vector
  field?](#troubleshooting-blueprints-10 "#troubleshooting-blueprints-10")
- [What does the output look like in the configured
  OpenSearch index?](#troubleshooting-blueprints-11 "#troubleshooting-blueprints-11")
- [Can I specify metadata fields to add to the document
  stored in the OpenSearch index?](#troubleshooting-blueprints-12 "#troubleshooting-blueprints-12")
- [Should I expect duplicate entries in the OpenSearch
  index?](#troubleshooting-blueprints-13 "#troubleshooting-blueprints-13")
- [Can I send data to multiple OpenSearch indices?](#troubleshooting-blueprints-14 "#troubleshooting-blueprints-14")
- [Can I deploy multiple real-time vector embedding
  applications in a single AWS account?](#troubleshooting-blueprints-15 "#troubleshooting-blueprints-15")
- [Can multiple real-time vector embedding applications
  use the same data source or sink?](#troubleshooting-blueprints-16 "#troubleshooting-blueprints-16")
- [Does the application support cross-account
  connectivity?](#troubleshooting-blueprints-17 "#troubleshooting-blueprints-17")
- [Does the application support cross-Region
  connectivity?](#troubleshooting-blueprints-18 "#troubleshooting-blueprints-18")
- [Can my Amazon MSK cluster and OpenSearch collection be in
  different VPCs or subnets?](#troubleshooting-blueprints-19 "#troubleshooting-blueprints-19")
- [What embedding models are supported by the
  application?](#troubleshooting-blueprints-20 "#troubleshooting-blueprints-20")
- [Can I fine-tune the performance of my application
  based on my workload?](#troubleshooting-blueprints-21 "#troubleshooting-blueprints-21")
- [What Amazon MSK authentication types are
  supported?](#troubleshooting-blueprints-22 "#troubleshooting-blueprints-22")
- [What is sink.os.bulkFlushIntervalMillis
  and how do I set it?](#troubleshooting-blueprints-23 "#troubleshooting-blueprints-23")
- [When I deploy my Managed Service for Apache Flink application, from what point
  in the Amazon MSK topic will it begin reading messages?](#troubleshooting-blueprints-24 "#troubleshooting-blueprints-24")
- [How do I use
  source.msk.starting.offset?](#troubleshooting-blueprints-25 "#troubleshooting-blueprints-25")
- [What chunking strategies are supported?](#troubleshooting-blueprints-26 "#troubleshooting-blueprints-26")
- [How do I read records in my vector
  datastore?](#troubleshooting-blueprints-27 "#troubleshooting-blueprints-27")
- [Where can I find new updates to the source code?](#troubleshooting-blueprints-28 "#troubleshooting-blueprints-28")
- [Can I make a change to the AWS CloudFormation template and
  update the Managed Service for Apache Flink application?](#troubleshooting-blueprints-29 "#troubleshooting-blueprints-29")
- [Will AWS monitor and maintain the application on
  my behalf?](#troubleshooting-blueprints-30 "#troubleshooting-blueprints-30")
- [Does this application move my data outside my
  AWS account?](#troubleshooting-blueprints-31 "#troubleshooting-blueprints-31")

## What AWS resources does this blueprint create?

To find resources deployed in your account, navigate to AWS CloudFormation console and identify
the stack name that starts with the name you provided for your Managed Service for Apache Flink application. Choose
the **Resources** tab to check the resources that were created as part
of the stack. The following are the key resources that the stack creates:

- Real-time vector embedding Managed Service for Apache Flink application
- Amazon S3 bucket for holding the source code for the real-time vector embedding
  application
- CloudWatch log group and log stream for storing logs
- Lambda functions for fetching and creating resources
- IAM roles and policies for Lambdas, Managed Service for Apache Flink application, and accessing Amazon Bedrock
  and Amazon OpenSearch Service
- Data access policy for Amazon OpenSearch Service
- VPC endpoints for accessing Amazon Bedrock and Amazon OpenSearch Service

## What are my actions after the AWS CloudFormation stack

deployment is complete?

After the AWS CloudFormation stack deployment is complete, access the Managed Service for Apache Flink console and find
your blueprint Managed Service for Apache Flink application. Choose the **Configure** tab and
confirm that all runtime properties are setup correctly. They may overflow to the next
page. When you are confident of the settings, choose **Run**. The
application will start ingesting messages from your topic.

To check for new releases, see [https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases](https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases "https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases").

## What should be the structure of the data in the

source Amazon MSK topic(s)?

We currently support structured and unstructured source data.

- Unstructured data is denoted by `STRING` in
  `source.msk.data.type`. The data is read as is from the incoming
  message.
- We currently support structured JSON data, denoted by `JSON` in
  `source.msk.data.type`. The data must always be in JSON format.
  If the application receives a malformed JSON, the application will fail.
- When using JSON as source data type, make sure that every message in all
  source topics is a valid JSON. If you subscribe to one or more topics that do
  not contain JSON objects with this setting, the application will fail. If one or
  more topics have a mix of structured and unstructured data, we recommended that
  you configure source data as unstructured in the Managed Service for Apache Flink application.

## Can I specify parts of a message to embed?

- For unstructured input data where `source.msk.data.type` is
  `STRING`, the application will always embed the entire message
  and store the entire message in the configured OpenSearch index.
- For structured input data where `source.msk.data.type` is
  `JSON`, you can configure
  `embed.input.config.json.fieldsToEmbed` to specify which field in
  the JSON object should be selected for embedding. This only works for top-level
  JSON fields and does not work with nested JSONs and with messages containing a
  JSON array. Use .\* to embed the entire JSON.

## Can I read data from multiple Amazon MSK topics?

Yes, you can read data from multiple Amazon MSK topics with this application. Data from
all topics must be of the same type (either STRING or JSON) or it might cause the
application to fail. Data from all topics is always stored in a single OpenSearch
index.

## Can I use regex to configure Amazon MSK topic names?

`source.msk.topic.names` does not support a list of regex. We support
either a comma separated list of topic names or `.*` regex to include all
topics.

## What is the maximum size of a message that can be

read from an Amazon MSK topic?

The maximum size of a message that can be processed is limited by the Amazon Bedrock
InvokeModel body limit that is currently set to 25,000,000. For more information, see
[InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md#API_runtime_InvokeModel_RequestBody "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md#API_runtime_InvokeModel_RequestBody").

## What type of OpenSearch is supported?

We support both OpenSearch domains and collections. If you are using an OpenSearch
collection, make sure to use a vector collection and create a vector index to use for
this application. This will let you use the OpenSearch vector database capabilities for
querying your data. To learn more, see[Amazon OpenSearch Service’s vector database capabilities explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/ "https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/").

## Why do I need to use a vector search collection,

vector index, and add a vector field in my OpenSearch Serverless colelction?

The _vector search_ collection type in OpenSearch
Serverless provides a similarity search capability that is scalable and high performing.
It streamlines building modern machine learning (ML) augmented search experiences and
generative artificial intelligence (AI) applications. For more information, see [Working with vector search collections](../../../opensearch-service/latest/developerguide/serverless-vector-search.md "../../../opensearch-service/latest/developerguide/serverless-vector-search.md").

## What should I set as the dimension for my vector

field?

Set the dimension of the vector field based on the embedding model that you want to
use. Refer to the following table, and confirm these values from the respective
documentation.

| Vector field dimensions               | Amazon Bedrock vector embedding model name | Output dimension support offered by the model |
| ------------------------------------- | ------------------------------------------ | --------------------------------------------- |
| Amazon Titan Text Embeddings V1       | 1,536                                      |
| Amazon Titan Text Embeddings V2       | 1,024 (default), 384, 256                  |
| Amazon Titan Multimodal Embeddings G1 | 1,024 (default), 384, 256                  |
| Cohere Embed English                  | 1,024                                      |
| Cohere Embed Multilingual             | 1,024                                      |

## What does the output look like in the configured

OpenSearch index?

Every document in the OpenSearch index contains following fields:

- **original_data**: The data that was used to
  generate embeddings. For STRING type, it is the entire message. For JSON object,
  it is the JSON object that was used for embeddings. It could be the entire JSON
  in the message or specified fields in the JSON. For example, if name was
  selected to be embedded from incoming messages, the output would look as
  follows:

```
"original_data": "{\"name\":\"John Doe\"}"
```

- **embedded_data**: A vector float array of
  embeddings generated by Amazon Bedrock
- **date**: UTC timestamp at which the document was
  stored in OpenSearch

## Can I specify metadata fields to add to the document

stored in the OpenSearch index?

No, currently, we do not support adding additional fields to the final document stored
in the OpenSearch index.

## Should I expect duplicate entries in the OpenSearch

index?

Depending on how you configured your application, you might see duplicate messages in
the index. One common reason is application restart. The application is configured by
default to start reading from the earliest message in the source topic. When you change
the configuraiton, the application restarts, and processes all messages in the topic
again. To avoid re-processing, see [How
do I use source.msk.starting.offset?](https://quip-amazon.com/0b6ZAIBsnSVq#temp:C:bPV2d49853149e54000ac324cc04 "https://quip-amazon.com/0b6ZAIBsnSVq#temp:C:bPV2d49853149e54000ac324cc04") and correctly set the starting offset
for your application.

## Can I send data to multiple OpenSearch indices?

No, the application supports storing data to a single OpenSearch index. To setup
vectorization output to multiple indices, you must deploy separate Managed Service for Apache Flink
applications.

## Can I deploy multiple real-time vector embedding

applications in a single AWS account?

Yes, you can deploy multiple real-time vector embedding Managed Service for Apache Flink applications in a single
AWS account if every application has a unique name.

## Can multiple real-time vector embedding applications

use the same data source or sink?

Yes, you can create multiple real-time vector embedding Managed Service for Apache Flink applications that read
data from the same topic(s) or store data in the same index.

## Does the application support cross-account

connectivity?

No, for the application to run successfully, the Amazon MSK cluster and the OpenSearch
collection must be in the same AWS account where you are trying to setup your Managed Service for Apache Flink
application.

## Does the application support cross-Region

connectivity?

No, the application only allows you to deploy an Managed Service for Apache Flink application with an Amazon MSK
cluster and an OpenSearch collection in the same Region of the Managed Service for Apache Flink application.

## Can my Amazon MSK cluster and OpenSearch collection be in

different VPCs or subnets?

Yes, we support Amazon MSK cluster and OpenSearch collection in different VPCs and subnets
as long as they are in the same AWS account. See (General MSF troubleshooting) to
make sure your setup is correct.

## What embedding models are supported by the

application?

Currently, the application supports all models that are supported by Bedrock. These
include:

- Amazon Titan Embeddings G1 - Text

- Amazon Titan Text Embeddings V2
- Amazon Titan Multimodal Embeddings G1
- Cohere Embed English
- Cohere Embed Multilingual

## Can I fine-tune the performance of my application

based on my workload?

Yes. The throughput of the application depends on a number of factors, all of which
can be controlled by the customers:

1. **AWS MSF KPUs**: The application is deployed
   with default parallelism factor 2 and parallelism per KPU 1, with automatic
   scaling turned on. However, we recommend that you configure scaling for the
   Managed Service for Apache Flink application according to your workloads. For more information, see [Review Managed Service for Apache Flink application resources](how-resources.md "how-resources.md").
2. **Amazon Bedrock**: Based on the selected Amazon Bedrock on-demand
   model, different quotas might apply. Review service quotas in Bedrock to see the
   workload that the service will be able to handle. For more information, see
   [Quotas for Amazon Bedrock](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md").
3. **Amazon OpenSearch Service**: Additionally, in some situations,
   you might notice that OpenSearch is the bottleneck in your pipeline. For scaling
   information, see OpenSearch scaling [Sizing Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md").

## What Amazon MSK authentication types are

supported?

We only support the IAM MSK authentication type.

## What is `sink.os.bulkFlushIntervalMillis`

and how do I set it?

When sending data to Amazon OpenSearch Service, the bulk flush interval is the interval at which the
bulk request is run, regardless of the number of actions or the size of the request. The
default value is set to 1 millisecond.

While setting a flush interval can help to make sure that data is indexed timely, it
can also lead to increased overhead if set too low. Consider your use case and the
importance of timely indexing when choosing a flush interval.

## When I deploy my Managed Service for Apache Flink application, from what point

in the Amazon MSK topic will it begin reading messages?

The application will start reading messages from the Amazon MSK topic at the offset
specified by the `source.msk.starting.offset` configuration set in the
application’s runtime configuration. If `source.msk.starting.offset` is not
explicitly set, the default behavior of the application is to start reading from the
earliest available message in the topic.

## How do I use

`source.msk.starting.offset`?

Explicitly set s`ource.msk.starting.offset` to one of the following values,
based on desired behavior:

- EARLIEST: The default setting, which reads from oldest offset in the
  partition. This is a good choice especially if:
  - You have newly created Amazon MSK topics and consumer
    applications.
  - You need to replay data, so you can build or reconstruct
    state. This is relevant when implementing the event sourcing
    pattern or when initializing a new service that requires a
    complete view of the data history.

- LATEST: The Managed Service for Apache Flink application will read messages from the end of the
  partition. We recommend this option if you only care about new messages being
  produced and don't need to process historical data. In this setting, the
  consumer will ignore the existing messages and only read new messages published
  by the upstream producer.
- COMMITTED: The Managed Service for Apache Flink application will start consuming messages from the
  committed offset of the consuming group. If the committed offset doesn't exist,
  the EARLIEST reset strategy will be used.

## What chunking strategies are supported?

We are using the [langchain](https://js.langchain.com/v0.1/docs/get_started/introduction/ "https://js.langchain.com/v0.1/docs/get_started/introduction/")
library to chunk inputs. Chunking is only applied if the length of the input is greater
than the chosen `maxSegmentSizeInChars`. We support the following five
chunking types:

- `SPLIT_BY_CHARACTER`: Will fit as many characters as it can into
  each chunk where each chunk length is no greater than maxSegmentSizeInChars.
  Doesn’t care about whitespace, so it can cut off words.
- `SPLIT_BY_WORD`: Will find whitespace characters to chunk by. No
  words are cut off.
- `SPLIT_BY_SENTENCE`: Sentence boundaries are detected using the
  Apache OpenNLP library with the English sentence model.
- `SPLIT_BY_LINE`: Will find new line characters to chunk by.
- `SPLIT_BY_PARAGRAPH`: Will find consecutive new line characters to
  chunk by.

The splitting strategies fall back according to the preceding order, where the larger
chunking strategies like `SPLIT_BY_PARAGRAPH` fall back to
`SPLIT_BY_CHARACTER`. For example, when using `SPLIT_BY_LINE`,
if a line is too long then the line will be sub-chunked by sentence, where each chunk
will fit in as many sentences as it can. If there are any sentences that are too long,
then it will be chunked at the word-level. If a word is too long, then it will be split
by character.

## How do I read records in my vector

datastore?

1. When `source.msk.data.type` is `STRING`
   - **original_data**: The entire original
     string from the Amazon MSK message.
   - **embedded_data**: Embedding vector
     created from `chunk_data` if it is not empty (chunking
     applied) or created from `original_data` if no chunking was
     applied.
   - **chunk_data**: Only present when the
     original data was chunked. Contains the chunk of the original message
     that was used to create the embedding in
     `embedded_data`.

2. When `source.msk.data.type` is `JSON`
   - **original_data**: The entire original
     JSON from the Amazon MSK message _after_ JSON key
     filtering is applied.
   - **embedded_data**: Embedding vector
     created from `chunk_data` if it is not empty (chunking
     applied) or created from `original_data` if no chunking was
     applied.
   - **chunk_key**: Only present when the
     original data was chunked. Contains the JSON key that the chunk is from
     in `original_data`. For example, it can look like
     `jsonKey1.nestedJsonKeyA` for nested keys or
     _metadata_ in the example of
     `original_data`.
   - **chunk_data**: Only present when the
     original data was chunked. Contains the chunk of the original message
     that was used to create the embedding in
     `embedded_data`.

Yes, you can read data from multiple Amazon MSK topics with this application. Data from
all topics must be of the same type (either STRING or JSON) or it might cause the
application to fail. Data from all topics is always stored in a single OpenSearch
index.

## Where can I find new updates to the source code?

Go to [https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases](https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases "https://github.com/awslabs/real-time-vectorization-of-streaming-data/releases")
to check for new releases.

## Can I make a change to the AWS CloudFormation template and

update the Managed Service for Apache Flink application?

No, making a change to the AWS CloudFormation template does not update the Managed Service for Apache Flink application.
Any new change in AWS CloudFormation implies a new stack needs to be deployed.

## Will AWS monitor and maintain the application on

my behalf?

No, AWS will not monitor, scale, update or patch this application on your behalf.

## Does this application move my data outside my

AWS account?

All data read and stored by the Managed Service for Apache Flink application stays within your AWS account and
never leaves your account.
