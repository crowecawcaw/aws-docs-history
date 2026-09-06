

# Logging and observability
<a name="ai-vector-embedding-integration-logging-observability"></a>

All logs and metrics for real-time vector embedding blueprints can be enabled using CloudWatch logs.

All metrics that are available for a regular MSF application and Amazon Bedrock can monitor your [application](https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions.html) and [Bedrock metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html#runtime-cloudwatch-metrics).

There are two additional metrics for monitoring performance of generating embeddings. These metrics are part of the EmbeddingGeneration operation name in CloudWatch.
+ **BedrockTitanEmbeddingTokenCount**: monitors the number of tokens present in a single request to Bedrock.
+ **BedrockEmbeddingGenerationLatencyMs**: reports the time taken to send and receive a response from Bedrock for generating embeddings in milliseconds.

For OpenSearch Service, you can use the following metrics:
+ **OpenSearch Serverless collection metrics**: see [Monitoring OpenSearch Serverless with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-cloudwatch.html) in the *Amazon OpenSearch Service Developer Guide*.
+ **OpenSearch provisioned metrics**: see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html) in the *Amazon OpenSearch Service Developer Guide*.