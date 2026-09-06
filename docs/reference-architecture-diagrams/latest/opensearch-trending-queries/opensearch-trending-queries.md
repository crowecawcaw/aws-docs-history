

# Amazon OpenSearch Trending Queries with AWS Glue and Amazon Bedrock
<a name="opensearch-trending-queries"></a>

Publication date: **December 18, 2024 ([Diagram history](#diagram-history))**

This architecture demonstrates how to use AWS services like [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html), vector embedding, K-means clustering, and LLMs to identify top trending search queries for optimizing content strategy and improving user experience.

## Amazon OpenSearch Trending Queries with AWS Glue and Amazon Bedrock
<a name="diagram1"></a>

![Architecture diagram showing trending query identification using Amazon OpenSearch Service, AWS Glue, Amazon Bedrock, and Step Functions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/opensearch-trending-queries/images/opensearch-trending-queries.png)


The following steps describe the architecture:

1. End users search articles on the search page. Queries are sent to Amazon OpenSearch Service for results retrieval.

1. Search query logs are streamed through [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) using an [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) proxy.

1. [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) consolidates search query logs every 15 minutes at the maximum buffer limit.

1. An [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function compresses search query logs for [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) storage optimization.

1. [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) daily scheduler triggers [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for trending query identification.

1. An AWS Glue crawler creates catalog tables for search query logs stored in Amazon S3.

1. An AWS Glue job consolidates and transforms query logs to Parquet files to boost query performance.

1. An AWS Glue crawler creates a catalog table for Parquet files stored in Amazon S3.

1. An AWS Glue job processes data using K-means clustering, creates search query clusters, and stores them in Amazon S3.

1. An AWS Glue crawler creates a catalog table for search query clusters stored in Amazon S3.

1. [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) queries the top n queries per cluster and passes a CSV file as input to a Lambda function.

1. Lambda processes the CSV file in a loop, invokes Amazon Bedrock to identify the most relevant search query per cluster, and stores results in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

1. When the user opens the search page, application logic uses API Gateway to retrieve top trending queries using Lambda and the DynamoDB table for display on the search page.

1. Business analysts use a trending query API to analyze trending search queries and define content strategy.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | December 18, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.