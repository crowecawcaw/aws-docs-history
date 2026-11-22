

# Amazon OpenSearch Service trending queries with AWS Glue and Amazon Bedrock

Publication date: **December 18, 2024 ([Diagram history](diagram-history.md))**

This architecture demonstrates how to use AWS services like [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/), [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/), vector embedding, K-means clustering, and LLMs to identify top trending search queries for optimizing content strategy and improving user experience.

## Amazon OpenSearch Service trending queries with AWS Glue and Amazon Bedrock diagram
<a name="opensearch-trending-queries-diagram1"></a>

![Architecture diagram showing trending queries using Amazon OpenSearch Service, AWS Glue, Amazon Bedrock, and Step Functions.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/opensearch-trending-queries.png)


The following steps describe the architecture:

1. End users search articles on the search page. Queries are sent to Amazon OpenSearch Service for results retrieval.

1. An [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) proxy streams search query logs to [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/).

1. [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/) consolidates search query logs every 15 minutes at the maximum buffer limit.

1. An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function compresses search query logs for [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) storage optimization.

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) daily scheduler triggers [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) for trending query identification.

1. An AWS Glue crawler creates catalog tables for search query logs stored in Amazon S3.

1. An AWS Glue job consolidates and transforms query logs to Parquet files to boost query performance.

1. An AWS Glue crawler creates a catalog table for Parquet files stored in Amazon S3.

1. An AWS Glue job processes data using K-means clustering, creates search query clusters, and stores them in Amazon S3.

1. An AWS Glue crawler creates a catalog table for search query clusters stored in Amazon S3.

1. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) queries the top n queries per cluster and passes a CSV file as input to a Lambda function.

1. Lambda processes the CSV file in a loop, invokes Amazon Bedrock to identify the most relevant search query per cluster, and stores results in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. When the user opens the search page, application logic uses API Gateway to retrieve top trending queries using Lambda and the DynamoDB table for display on the search page.

1. Business analysts use a trending query API to analyze trending search queries and define content strategy.

## Further reading
<a name="opensearch-trending-queries-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)