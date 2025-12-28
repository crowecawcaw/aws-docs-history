Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Real-time vector embedding blueprints -

troubleshooting

Review the following troubleshooting topics about real-time vector embedding blueprints.
For more information about real-time vector embedding blueprints, see [Real-time vector embedding blueprints](../../../msk/latest/developerguide/ai-vector-embedding-integration-learn-more.md "../../../msk/latest/developerguide/ai-vector-embedding-integration-learn-more.md").

###### Troubleshooting topics

- [My CloudFormation stack deployment has failed or
  rolled back. What can I do to fix it?](#troubleshooting-blueprints-deployment "#troubleshooting-blueprints-deployment")
- [I don't want my application to start reading
  messages from the beginning of the Amazon MSK topics. What do I do?](#troubleshooting-blueprints-beginning "#troubleshooting-blueprints-beginning")
- [How do I know if there is an issue with my Managed Service for Apache Flink
  application and how can I debug it?](#troubleshooting-blueprints-debug "#troubleshooting-blueprints-debug")
- [What are the key metrics that I should be
  monitoring for my Managed Service for Apache Flink application?](#troubleshooting-blueprints-metrics "#troubleshooting-blueprints-metrics")

## My CloudFormation stack deployment has failed or

rolled back. What can I do to fix it?

- Go to your CFN stack and find the reason for the stack failure. It could
  be related to missing permissions, AWS resource name collisions, among
  other causes. Fix the root cause of the deployment failure. For more
  information, see the [CloudWatch troubleshooting guide](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#basic-ts-guide "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#basic-ts-guide").
- [Optional] There can only be one VPC endpoint per service per VPC. If you
  deployed multiple real-time vector embedding blueprints to write to the
  Amazon OpenSearch Service collections in the same VPC, they might be sharing VPC endpoints.
  These might either already be present in your account for the VPC, or the
  first real-time vector embedding blueprint stack will create VPC endpoints
  for Amazon Bedrock and Amazon OpenSearch Service that will be used by all other stacks deployed in your
  account. If a stack fails, check if that stack created VPC endpoints for
  Amazon Bedrock and Amazon OpenSearch Service and delete them if they are not used anywhere else in your
  account. For steps for deleting VPC endpoints, refer to the documentation on how to safely delete your application.
- There might be other services or applications in your account using the
  VPC endpoint. Deleting it might create network disruption for other
  services. Be careful in deleting these endpoints.

## I don't want my application to start reading

messages from the beginning of the Amazon MSK topics. What do I do?

You must explicitly set `source.msk.starting.offset` to one of the
following values, depending on the desired behavior:

- **Earliest offset**: The oldest offset in the
  partition.
- **Latest offset**: Consumers will read
  messages from the end of the partition.
- **Committed offset**: Read from the last
  message the consumer processed within a partition.

## How do I know if there is an issue with my Managed Service for Apache Flink

application and how can I debug it?

Use the [Managed Service for Apache Flink troubleshooting guide](troubleshooting-runtime.md "troubleshooting-runtime.md") to debug Managed Service for Apache Flink related issues with your
application.

## What are the key metrics that I should be

monitoring for my Managed Service for Apache Flink application?

- All metrics available for a regular Managed Service for Apache Flink application can help you monitor
  your application. For more information, see [Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md "metrics-dimensions.md").
- To monitor Amazon Bedrock metrics, see [Amazon CloudWatch metrics for Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md#runtime-cloudwatch-metrics "../../../bedrock/latest/userguide/monitoring.md#runtime-cloudwatch-metrics").
- We have added two new metrics for monitoring performance of generating
  embeddings. Find them under the `EmbeddingGeneration` operation
  name in CloudWatch. The two metrics are:
  - **BedrockTitanEmbeddingTokenCount**:
    Number of tokens present in a single request to Amazon Bedrock.
  - **BedrockEmbeddingGenerationLatencyMs**: Reports the
    time taken to send and receive a response from Amazon Bedrock for generating
    embeddings, in milliseconds.

- For Amazon OpenSearch Service serverless collections, you can use metrics such as
  `IngestionDataRate`, `IngestionDocumentErrors` and
  others. For more information, see [Monitoring OpenSearch Serverless with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md "../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md").
- For OpenSearch provisioned metrics, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md "../../../opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.md").
