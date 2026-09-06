

# Serverless Real-Time Analytics for Games
<a name="serverless-real-time-analytics-games"></a>

Publication date: **August 9, 2021 ([Diagram history](#analytics-history))**

This serverless architecture collects events from games, analyzes them in real-time, and stores them for batch analysis. You can use this pipeline to provide real-time flash offers, monitor user acquisition campaigns, detect abusive players, find deficiencies during A/B testing, and build online dashboards for business and operational metrics.

## Serverless Real-Time Analytics for Games diagram
<a name="analytics-diagram"></a>

![Reference architecture diagram showing how to build serverless real-time analytics pipelines for cross-platform games by using Amazon Kinesis, Lambda, CloudWatch, and Amazon Data Firehose.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-real-time-analytics-games/images/serverless-real-time-analytics-games.png)


**Collecting client events (option with AWS SDKs):**

1. The game uses an AWS SDK to submit events in JSON directly to [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/). The SDK used depends on the game engine. If the game engine is Unity, you can use the AWS SDK for .NET. If the game engine is Unreal Engine, you can use the AWS SDK for C\+\+.

1. The game receives temporary AWS credentials from the [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) identity pool to access Kinesis Data Streams.

**Collecting client events (option without AWS SDK):**

1. The game submits events through the REST API to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), which has a native integration with Kinesis. This option adds an extra layer of separation between the player and the Kinesis Data Stream through a REST API and does not require Amazon Cognito.

**Submitting server events:**

1. Multiplayer game servers, backend servers, and other services can submit events directly to Kinesis by using the AWS SDK, or through API Gateway. When possible, submit events from an authoritative server.

**Processing and analyzing real-time events:**

1. Amazon Managed Service for Apache Flink consumes data from the Kinesis Data Stream instance. It runs real-time SQL queries on the stream to analyze, filter, and process data.

1. The data is processed by a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function, which sends custom metrics to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

1. The custom CloudWatch metrics are visualized in a real-time dashboard. You can create an operational dashboard that shows infrastructure health, and a game events dashboard that shows real-time game KPIs such as concurrent users. You can create alerts and notifications through CloudWatch and Amazon SNS.

**Storing events for batch analysis:**

1. Amazon Data Firehose consumes the data stream and preprocesses the data for storage by using a built-in Lambda integration. For example, you can transform the data to Parquet format. Parquet is compressed and optimized for performance and lower storage costs when running analytics.

1. Processed data is batched and stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) to create a game analytics data lake. Use S3 Intelligent-Tiering, lifecycle policies, and different storage tiers for cost savings on historical data.

**Visualizing batch data:**

1. Query data on an ad hoc basis by using Amazon Athena. Visualize the data to get business insights by using Amazon Quick Sight.

## Further reading
<a name="analytics-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="analytics-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#analytics-history) | Reference architecture diagram first published. | August 9, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.