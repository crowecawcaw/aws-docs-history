# Logging and observability

All logs and metrics for real-time vector embedding blueprints can be enabled using CloudWatch logs.

All metrics that are available for a regular MSF application and Amazon Bedrock can monitor your [application](../../../managed-flink/latest/java/metrics-dimensions.md "../../../managed-flink/latest/java/metrics-dimensions.md") and
[Bedrock
metrics](../../../bedrock/latest/userguide/monitoring.md#runtime-cloudwatch-metrics "../../../bedrock/latest/userguide/monitoring.md#runtime-cloudwatch-metrics").

There are two additional metrics for monitoring performance of generating embeddings. These
metrics are part of the EmbeddingGeneration operation name in CloudWatch.

- **BedrockTitanEmbeddingTokenCount**: monitors the number of tokens present in a single request to Bedrock.
- **BedrockEmbeddingGenerationLatencyMs**: reports the time taken
  to send and receive a response from Bedrock for generating embeddings in
  milliseconds.
  For OpenSearch Service, you can use the following metrics:

- **OpenSearch Serverless collection metrics**: see [Monitoring OpenSearch Serverless with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md "../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md") in the
  _Amazon OpenSearch Service Developer Guide_.
- **OpenSearch provisioned metrics**: see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md "../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md") in the
  _Amazon OpenSearch Service Developer Guide_.
