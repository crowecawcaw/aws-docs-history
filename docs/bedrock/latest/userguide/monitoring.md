# Monitoring the performance of Amazon Bedrock

You can monitor all parts of your Amazon Bedrock application using Amazon CloudWatch, which collects raw data
and processes it into readable, near real-time metrics. You can graph the metrics using the CloudWatch
console. You can also set alarms that watch for certain thresholds, and send notifications or take
actions when values exceed those thresholds.

For more information, see [What is
Amazon CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

Amazon Bedrock provides comprehensive monitoring capabilities across different components of your application:

- [Monitor model invocation using CloudWatch Logs and Amazon S3](model-invocation-logging.md "model-invocation-logging.md") - Track and analyze model invocations using CloudWatch Logs and Amazon S3.
- [Monitor knowledge bases using CloudWatch Logs](knowledge-bases-logging.md "knowledge-bases-logging.md") - Monitor knowledge base operations and performance.
- [Monitor Amazon Bedrock Guardrails using CloudWatch metrics](monitoring-guardrails-cw-metrics.md "monitoring-guardrails-cw-metrics.md") - Track guardrail evaluations and policy enforcement.
- [Monitor Amazon Bedrock Agents using CloudWatch Metrics](monitoring-agents-cw-metrics.md "monitoring-agents-cw-metrics.md") - Monitor agent invocations and performance metrics.
- [Amazon Bedrock runtime metrics](#runtime-cloudwatch-metrics "#runtime-cloudwatch-metrics") - View key runtime metrics including invocations, latency, errors, and token counts.
- [Monitor Amazon Bedrock job state changes using Amazon EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md") - Track job state changes and automate responses to events.
- [Monitor Amazon Bedrock API calls using CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") - Audit API calls and track user activity.

###### Topics

- [Monitor model invocation using CloudWatch Logs and Amazon S3](model-invocation-logging.md "model-invocation-logging.md")
- [Monitor knowledge bases using CloudWatch Logs](knowledge-bases-logging.md "knowledge-bases-logging.md")
- [Monitor Amazon Bedrock Guardrails using CloudWatch metrics](monitoring-guardrails-cw-metrics.md "monitoring-guardrails-cw-metrics.md")
- [Monitor Amazon Bedrock Agents using CloudWatch Metrics](monitoring-agents-cw-metrics.md "monitoring-agents-cw-metrics.md")
- [Amazon Bedrock runtime metrics](#runtime-cloudwatch-metrics "#runtime-cloudwatch-metrics")
- [CloudWatch metrics for Amazon Bedrock](#br-cloudwatch-metrics "#br-cloudwatch-metrics")
- [Monitor Amazon Bedrock job state changes using Amazon EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md")
- [Monitor Amazon Bedrock API calls using CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")

## Amazon Bedrock runtime metrics

The following table describes runtime metrics provided by Amazon Bedrock.

| Metric name            | Unit         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Invocations            | SampleCount  | Number of successful requests to the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md"), [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), and<br>[InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") API operations. |
| InvocationLatency      | MilliSeconds | Latency of the invocations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| InvocationClientErrors | SampleCount  | Number of invocations that result in client-side errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| InvocationServerErrors | SampleCount  | Number of invocations that result in AWS server-side errors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| InvocationThrottles    | SampleCount  | Number of invocations that the system throttled. Throttled requests and other invocation errors don't count as either Invocations or Errors. The number of throttles you see will depend on your retry settings in the SDK. For more information, see [Retry behavior](../../../sdkref/latest/guide/feature-retry-behavior.md "../../../sdkref/latest/guide/feature-retry-behavior.md") in the AWS SDKs and Tools Reference Guide.                                                                                                               |
| InputTokenCount        | SampleCount  | Number of tokens in the input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LegacyModelInvocations | SampleCount  | Number of invocations using [Legacy](../APIReference/API_FoundationModelLifecycle.md "../APIReference/API_FoundationModelLifecycle.md") models                                                                                                                                                                                                                                                                                                                                                                                                   |
| OutputTokenCount       | SampleCount  | Number of tokens in the output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| OutputImageCount       | SampleCount  | Number of images in the output (only applicable for image generation models).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

There are also metrics for [Amazon Bedrock Guardrails](monitoring-guardrails-cw-metrics.md "monitoring-guardrails-cw-metrics.md") and [Amazon Bedrock Agents](monitoring-agents-cw-metrics.md "monitoring-agents-cw-metrics.md").

## CloudWatch metrics for Amazon Bedrock

For each delivery success or failure attempt, the following Amazon CloudWatch metrics are emitted
under the namespace `AWS/Bedrock`, and `Across all model IDs`
dimension:

- `ModelInvocationLogsCloudWatchDeliverySuccess`
- `ModelInvocationLogsCloudWatchDeliveryFailure`
- `ModelInvocationLogsS3DeliverySuccess`
- `ModelInvocationLogsS3DeliveryFailure`
- `ModelInvocationLargeDataS3DeliverySuccess`
- `ModelInvocationLargeDataS3DeliveryFailure`

To retrieve metrics for your Amazon Bedrock operations, you specify the following information:

- The metric dimension. A _dimension_ is a set of name-value pairs that
  you use to identify a metric. Amazon Bedrock supports the following dimensions:
  - `ModelId` – all metrics
  - `ModelId + ImageSize + BucketedStepSize` – OutputImageCount

- The metric name, such as `InvocationClientErrors`.

You can get metrics for Amazon Bedrock with the AWS Management Console, the AWS CLI, or the CloudWatch API. You can use the
CloudWatch API through one of the AWS Software Development Kits (SDKs) or the CloudWatch API tools.

To view Amazon Bedrock metrics in the CloudWatch console, go to the metrics section in the navigation pane
and select the all metrics option, then search for the model ID.

You must have the appropriate CloudWatch permissions to monitor Amazon Bedrock with CloudWatch For more
information, see [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _Amazon CloudWatch User
Guide_.
