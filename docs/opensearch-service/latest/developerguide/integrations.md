# Loading streaming data into Amazon OpenSearch Service

You can use OpenSearch Ingestion to directly load [streaming data](http://aws.amazon.com/streaming-data/ "http://aws.amazon.com/streaming-data/") into your Amazon OpenSearch Service
domain, without needing to use third-party solutions. To send data to OpenSearch Ingestion, you
configure your data producers and the service automatically delivers the data to the domain
or collection that you specify. To get started with OpenSearch Ingestion, see [Tutorial: Ingesting data into a collection
using Amazon OpenSearch Ingestion](osis-serverless-get-started.md "osis-serverless-get-started.md").

You can still use other sources to load streaming data, such as Amazon Data Firehose and Amazon CloudWatch Logs,
which have built-in support for OpenSearch Service. Others, like Amazon S3, Amazon Kinesis Data Streams, and Amazon DynamoDB, use
AWS Lambda functions as event handlers. The Lambda functions respond to new data by processing
it and streaming it to your domain.

###### Note

Lambda supports several popular programming languages and is available in most
AWS Regions. For more information, see [Getting started with Lambda](../../../lambda/latest/dg/lambda-app.md "../../../lambda/latest/dg/lambda-app.md") in the _AWS Lambda Developer Guide_ and [AWS service endpoints](../../../general/latest/gr/rande.md#lambda_region "../../../general/latest/gr/rande.md#lambda_region") in the _AWS General Reference_.

## Loading streaming data from AWS IoT

You can send data from AWS IoT using [rules](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md"). To learn more, see the [OpenSearch](../../../iot/latest/developerguide/opensearch-rule-action.md "../../../iot/latest/developerguide/opensearch-rule-action.md") action in the
_AWS IoT Developer Guide_.
