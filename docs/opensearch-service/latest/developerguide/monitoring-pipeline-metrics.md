# Monitoring pipeline metrics

You can monitor Amazon OpenSearch Ingestion pipelines using Amazon CloudWatch, which collects raw data
and processes it into readable, near real-time metrics. These statistics are kept for 15
months, so that you can access historical information and gain a better perspective on
how your web application or service is performing. You can also set alarms that watch
for certain thresholds, and send notifications or take actions when those thresholds are
met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The OpenSearch Ingestion console displays a series of charts based on the raw data from
CloudWatch on the **Performance** tab for each pipeline.

OpenSearch Ingestion reports metrics from most [supported
plugins](pipeline-config-reference.md#ingestion-plugins "pipeline-config-reference.md#ingestion-plugins"). If certain plugins don't have their own table below, it means that
they don't report any plugin-specific metrics. Pipeline metrics are published in the
`AWS/OSIS` namespace.

###### Topics

- [Common metrics](#common-metrics "#common-metrics")
- [Buffer metrics](#buffer-metrics "#buffer-metrics")
- [Signature V4 metrics](#sigv4-metrics "#sigv4-metrics")
- [Bounded blocking buffer metrics](#blockingbuffer-metrics "#blockingbuffer-metrics")
- [Otel trace source metrics](#oteltrace-metrics "#oteltrace-metrics")
- [Otel metrics source metrics](#otelmetrics-metrics "#otelmetrics-metrics")
- [Http metrics](#http-metrics "#http-metrics")
- [S3 metrics](#s3-metrics "#s3-metrics")
- [Aggregate metrics](#aggregate-metrics "#aggregate-metrics")
- [Date metrics](#date-metrics "#date-metrics")
- [Lambda metrics](#lambda-metrics "#lambda-metrics")
- [Grok metrics](#grok-metrics "#grok-metrics")
- [Otel trace raw metrics](#oteltrace-raw-metrics "#oteltrace-raw-metrics")
- [Otel trace group metrics](#oteltracegroup-metrics "#oteltracegroup-metrics")
- [Service map stateful metrics](#servicemapstateful-metrics "#servicemapstateful-metrics")
- [OpenSearch metrics](#opensearch-metrics "#opensearch-metrics")
- [System and metering metrics](#systemmetering-metrics "#systemmetering-metrics")

## Common metrics

The following metrics are common to all processors and sinks.

Each metric is prefixed by the sub-pipeline name and plugin name, in the format
<`sub_pipeline_name`><`plugin`><`metric_name`>.
For example, the full name of the `recordsIn.count` metric for a
sub-pipeline named `my-pipeline` and the [date](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/") processor would be
`my-pipeline.date.recordsIn.count`.

| Metric suffix       | Description                                                                                                                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `recordsIn.count`   | The ingress of records to a pipeline component. This metric<br>applies to processors and sinks.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                                        |
| `recordsOut.count`  | The egress of records from a pipeline component. This metric<br>applies to processors and sources.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                                     |
| `timeElapsed.count` | A count of data points recorded during execution of a pipeline<br>component. This metric applies to processors and sinks.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`              |
| `timeElapsed.sum`   | The total time elapsed during execution of a pipeline component.<br>This metric applies to processors and sinks, in<br>milliseconds.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`   |
| `timeElapsed.max`   | The maximum time elapsed during execution of a pipeline component.<br>This metric applies to processors and sinks, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName` |

## Buffer metrics

The following metrics apply to the default [Bounded blocking](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/buffers/bounded-blocking/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/buffers/bounded-blocking/") buffer that OpenSearch Ingestion automatically configures
for all pipelines.

Each metric is prefixed by the sub-pipeline name and buffer name, in the format
<`sub_pipeline_name`><`buffer_name`><`metric_name`>.
For example, the full name of the `recordsWritten.count` metric for a
sub-pipeline named `my-pipeline` would be
`my-pipeline.BlockingBuffer.recordsWritten.count`.

| Metric suffix                 | Description                                                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `recordsWritten.count`        | The number of records written to a buffer.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                                 |
| `recordsRead.count`           | The number of records read from a buffer.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                                  |
| `recordsInFlight.value`       | The number of unchecked records read from a buffer.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`                 |
| `recordsInBuffer.value`       | The number of records currently in a buffer.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`                        |
| `recordsProcessed.count`      | The number of records read from a buffer and processed by a<br>pipeline.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`   |
| `recordsWriteFailed.count`    | The number of records that the pipeline failed to write to the<br>sink.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `writeTimeElapsed.count`      | A count of data points recorded while writing to a buffer.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                 |
| `writeTimeElapsed.sum`        | The total time elapsed while writing to a buffer, in<br>milliseconds.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`      |
| `writeTimeElapsed.max`        | The maximum time elapsed while writing to a buffer, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`    |
| `writeTimeouts.count`         | The count of write timeouts to a buffer.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                                   |
| `readTimeElapsed.count`       | A count of data points recorded while reading from a<br>buffer.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`            |
| `readTimeElapsed.sum`         | The total time elapsed while reading from a buffer, in<br>milliseconds.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`    |
| `readTimeElapsed.max`         | The maximum time elapsed while reading from a buffer, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`  |
| `checkpointTimeElapsed.count` | A count of data points recorded while checkpointing.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`                       |
| `checkpointTimeElapsed.sum`   | The total time elapsed while checkpointing, in<br>milliseconds.<br>**Relevant statistics**: Sum<br>**Dimension**:<br>`PipelineName`            |
| `checkpointTimeElapsed.max`   | The maximum time elapsed while checkpointing, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`          |

## Signature V4 metrics

The following metrics apply to the ingestion endpoint for a pipeline and are
associate with the source plugins (`http`, `otel_trace`, and
`otel_metrics`). All requests to the ingestion endpoint must be
signed using [Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). These metrics can help you identify authorization
issues when connecting to your pipeline, or confirm that you're successfully
authenticating.

Each metric is prefixed by the sub-pipeline name and `osis_sigv4_auth`.
For example,
``sub_pipeline_name`.osis_sigv4_auth.httpAuthSuccess.count`.

| Metric suffix               | Description                                                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `httpAuthSuccess.count`     | The number of successful Signature V4 requests to the<br>pipeline.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                  |
| `httpAuthFailure.count`     | The number of failed Signature V4 requests to the<br>pipeline.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                      |
| `httpAuthServerError.count` | The number of Signature V4 requests to the pipeline that<br>returned server errors.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |

## Bounded blocking buffer metrics

The following metrics apply to the [bounded blocking](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/buffers/bounded-blocking/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/buffers/bounded-blocking/") buffer. Each metric is prefixed by the sub-pipeline
name and `BlockingBuffer`. For example,
``sub_pipeline_name`.BlockingBuffer.bufferUsage.value`.

| Metric suffix       | Description                                                                                                                                                                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bufferUsage.value` | Percent usage of the `buffer_size` based on the<br>number of records in the buffer. `buffer_size`<br>represents the maximum number of records written into the buffer<br>as well as in-flight records that have not been checked.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName` |

## Otel trace source metrics

The following metrics apply to the [OTel trace](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/otel-trace-source/ "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/otel-trace-source/") source. Each metric is prefixed by the sub-pipeline name and
`otel_trace_source`. For example,
``sub_pipeline_name`.otel_trace_source.requestTimeouts.count`.

| Metric suffix                  | Description                                                                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requestTimeouts.count`        | The number of requests that timed out.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                    |
| `requestsReceived.count`       | The number of requests received by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                            |
| `successRequests.count`        | The number of requests that were successfully processed by the<br>plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                 |
| `badRequests.count`            | The number of requests with an invalid format that were<br>processed by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                       |
| `requestsTooLarge.count`       | The number of requests of which the number of spans in the<br>content is larger than the buffer capacity.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `internalServerError.count`    | The number of requests processed by the plugin with a custom<br>exception type.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                           |
| `requestProcessDuration.count` | A count of data points recorded while processing requests by<br>the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                               |
| `requestProcessDuration.sum`   | The total latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                |
| `requestProcessDuration.max`   | The maximum latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                 |
| `payloadSize.count`            | A count of the distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                           |
| `payloadSize.sum`              | The total distribution of the payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                            |
| `payloadSize.max`              | The maximum distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                 |

## Otel metrics source metrics

The following metrics apply to the [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/") source. Each metric is prefixed by the sub-pipeline name
and `otel_metrics_source`. For example,
``sub_pipeline_name`.otel_metrics_source.requestTimeouts.count`.

| Metric suffix                  | Description                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requestTimeouts.count`        | The total number of requests to the plugin that time<br>out.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                               |
| `requestsReceived.count`       | The total number of requests received by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                       |
| `successRequests.count`        | The number of requests successfully processed (200 response<br>status code) by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `requestProcessDuration.count` | A count of the latency of requests processed by the plugin, in<br>seconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                 |
| `requestProcessDuration.sum`   | The total latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                 |
| `requestProcessDuration.max`   | The maximum latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`               |
| `payloadSize.count`            | A count of the distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`            |
| `payloadSize.sum`              | The total distribution of the payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`             |
| `payloadSize.max`              | The maximum distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`               |

## Http metrics

The following metrics apply to the [HTTP](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/") source. Each metric is prefixed by the sub-pipeline name and
`http`. For example,
``sub_pipeline_name`.http.requestsReceived.count`.

| Metric suffix                  | Description                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requestsReceived.count`       | The number of requests received by the<br>`/log/ingest` endpoint.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                   |
| `requestsRejected.count`       | The number of requests rejected (429 response status code) by<br>the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                        |
| `successRequests.count`        | The number of requests successfully processed (200 response<br>status code) by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                          |
| `badRequests.count`            | The number of requests with invalid content type or format<br>(400 response status code) processed by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                   |
| `requestTimeouts.count`        | The number of requests that time out in the HTTP source server<br>(415 response status code).<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                       |
| `requestsTooLarge.count`       | The number of requests of which the events size in the content<br>is larger than the buffer capacity (413 response status<br>code).<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `internalServerError.count`    | The number of requests processed by the plugin with a custom<br>exception type (500 response status code).<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                          |
| `requestProcessDuration.count` | A count of the latency of requests processed by the plugin, in<br>seconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                          |
| `requestProcessDuration.sum`   | The total latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                          |
| `requestProcessDuration.max`   | The maximum latency of requests processed by the plugin, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                                           |
| `payloadSize.count`            | A count of the distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                     |
| `payloadSize.sum`              | The total distribution of the payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                      |
| `payloadSize.max`              | The maximum distribution of payload sizes of incoming<br>requests, in bytes.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                                           |

## S3 metrics

The following metrics apply to the [S3](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/") source. Each metric is prefixed by the sub-pipeline name and
`s3`. For example,
``sub_pipeline_name`.s3.s3ObjectsFailed.count`.

| Metric suffix                   | Description                                                                                                                                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s3ObjectsFailed.count`         | The total number of S3 objects that the plugin failed to<br>read.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                      |
| `s3ObjectsNotFound.count`       | The number of S3 objects that the plugin failed to read due to<br>a `Not Found` error from S3. These metrics also count<br>toward the `s3ObjectsFailed` metric.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                        |
| `s3ObjectsAccessDenied.count`   | The number of S3 objects that the plugin failed to read due to<br>an `Access Denied` or `Forbidden` error<br>from S3. These metrics also count toward the<br>`s3ObjectsFailed` metric.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `s3ObjectReadTimeElapsed.count` | The amount of time the plugin takes to perform a GET request<br>for an S3 object, parse it, and write events to the<br>buffer.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                         |
| `s3ObjectReadTimeElapsed.sum`   | The total amount of time that the plugin takes to perform a<br>GET request for an S3 object, parse it, and write events to the<br>buffer, in milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                             |
| `s3ObjectReadTimeElapsed.max`   | The maximum amount of time that the plugin takes to perform a<br>GET request for an S3 object, parse it, and write events to the<br>buffer, in milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                              |
| `s3ObjectSizeBytes.count`       | The count of the distribution of S3 object sizes, in<br>bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                         |
| `s3ObjectSizeBytes.sum`         | The total distribution of S3 object sizes, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                                   |
| `s3ObjectSizeBytes.max`         | The maximum distribution of S3 object sizes, in bytes.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`                                                                                                                                 |
| `s3ObjectProcessedBytes.count`  | The count of the distribution of S3 objects processed by the<br>plugin, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                      |
| `s3ObjectProcessedBytes.sum`    | The total distribution of S3 objects processed by the plugin,<br>in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                             |
| `s3ObjectProcessedBytes.max`    | The maximum distribution of S3 objects processed by the<br>plugin, in bytes.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`                                                                                                           |
| `s3ObjectsEvents.count`         | The count of the distribution of S3 events received by the<br>plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                  |
| `s3ObjectsEvents.sum`           | The total distribution of S3 events received by the plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                            |
| `s3ObjectsEvents.max`           | The maximum distribution of S3 events received by the<br>plugin.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`                                                                                                                       |
| `sqsMessageDelay.count`         | A count of data points recorded while S3 records an event time<br>for the creation of an object to when it's fully parsed.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                             |
| `sqsMessageDelay.sum`           | The total amount of time between when S3 records an event time<br>for the creation of an object to when it's fully parsed, in<br>milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                         |
| `sqsMessageDelay.max`           | The maximum amount of time between when S3 records an event<br>time for the creation of an object to when it's fully parsed, in<br>milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                          |
| `s3ObjectsSucceeded.count`      | The number of S3 objects that the plugin successfully<br>read.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                         |
| `sqsMessagesReceived.count`     | The number of Amazon SQS messages received from the queue by the<br>plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                            |
| `sqsMessagesDeleted.count`      | The number of Amazon SQS messages deleted from the queue by the<br>plugin.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                             |
| `sqsMessagesFailed.count`       | The number of Amazon SQS messages that the plugin failed to<br>parse.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                                  |

## Aggregate metrics

The following metrics apply to the [Aggregate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/") processor. Each metric is prefixed by the sub-pipeline name
and `aggregate`. For example,
``sub_pipeline_name`.aggregate.actionHandleEventsOut.count`.

| Metric suffix                                     | Description                                                                                                                                                                                                                       |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `actionHandleEventsOut.count`                     | The number of events that have been returned from the<br>`handleEvent` call to the configured<br>action.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                   |
| `actionHandleEventsDropped.count`                 | The number of events that have been returned from the<br>`handleEvent` call to the configured<br>action.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                   |
| `actionHandleEventsProcessingErrors.count`        | The number of calls made to `handleEvent` for the<br>configured action that resulted in an error.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                          |
| `actionConcludeGroupEventsOut.count`              | The number of events that have been returned from the<br>`concludeGroup` call to the configured<br>action.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                 |
| `actionConcludeGroupEventsDropped.count`          | The number of events that have not been returned from the<br>`condludeGroup` call to the configured<br>action.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                             |
| `actionConcludeGroupEventsProcessingErrors.count` | The number of calls made to `concludeGroup` for the<br>configured action that resulted in an error.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                        |
| `currentAggregateGroups.value`                    | The current number of groups. This gauge decreases when groups<br>are concluded, and increases when an event initiates the<br>creation of a new group.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName` |

## Date metrics

The following metrics apply to the [Date](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/") processor. Each metric is prefixed by the sub-pipeline name and
`date`. For example,
``sub_pipeline_name`.date.dateProcessingMatchSuccess.count`.

| Metric suffix                      | Description                                                                                                                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dateProcessingMatchSuccess.count` | The number of records that match at least one of the patterns<br>specified in the `match` configuration option.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `dateProcessingMatchFailure.count` | The number of records that didn't match any of the patterns<br>specified in the `match` configuration option.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`   |

## Lambda metrics

The following metrics apply to the [AWS Lambda](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aws-lambda/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aws-lambda/") processor. Each metric is prefixed by the sub-pipeline name
and `lambda`. For example,
``sub_pipeline_name`.lambda.recordsSuccessfullySentToLambda.count`.

| Metric suffix                                          | Description                                                                                                                                    |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `recordsSuccessfullySentToLambda.count`                | The number of records successfully processed by the Lambda<br>function.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `recordsFailedToSendToLambda.count`                    | The number of records that failed to be sent to the Lambda<br>function.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `lambdaFunctionLatency.avg``lambdaFunctionLatency.max` | The latency of Lambda function invocations.<br>**Relevant statistics**: Average<br>and Maximum<br>**Dimension**:<br>`PipelineName`             |
| `numberOfRequestsSucceeded.count`                      | The total number of successful Lambda invocation<br>requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`           |
| `numberOfRequestsFailed.count`                         | The total number of failed Lambda invocation requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                  |
| `requestPayloadSize.avg`                               | The size of request payloads sent to Lambda.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`                        |
| `responsePayloadSize.avg`                              | The size of response payloads received from Lambda.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`                 |

## Grok metrics

The following metrics apply to the [Grok](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/") processor. Each metric is prefixed by the sub-pipeline name and
`grok`. For example,
``sub_pipeline_name`.grok.grokProcessingMatch.count`.

| Metric suffix                  | Description                                                                                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `grokProcessingMatch.count`    | The number of records that found at least one pattern match<br>from the `match` configuration option.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                              |
| `grokProcessingMismatch.count` | The number of records that didn't match any of the patterns<br>specified in the `match` configuration option.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                      |
| `grokProcessingErrors.count`   | The number of record processing errors.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                                            |
| `grokProcessingTimeouts.count` | The number of records that timed out while matching.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                                               |
| `grokProcessingTime.count`     | A count of data points recorded while an individual record<br>matched against patterns from the `match`<br>configuration option.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                   |
| `grokProcessingTime.sum`       | The total amount of time that each individual record takes to<br>match against patterns from the `match` configuration<br>option, in milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `grokProcessingTime.max`       | The maximum amount of time that each individual record takes<br>to match against patterns from the `match`<br>configuration option, in milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`  |

## Otel trace raw metrics

The following metrics apply to the [OTel trace raw](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/otel-traces/ "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/otel-traces/") processor. Each metric is prefixed by the sub-pipeline
name and `otel_trace_raw`. For example,
``sub_pipeline_name`.otel_trace_raw.traceGroupCacheCount.value`.

| Metric suffix                | Description                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `traceGroupCacheCount.value` | The number of trace groups in the trace group cache.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `spanSetCount.value`         | The number of span sets in the span set collection.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`  |

## Otel trace group metrics

The following metrics apply to the [OTel trace group](https://github.com/opensearch-project/data-prepper/tree/main/data-prepper-plugins/otel-trace-group-processor "https://github.com/opensearch-project/data-prepper/tree/main/data-prepper-plugins/otel-trace-group-processor") processor. Each metric is prefixed by the sub-pipeline
name and `otel_trace_group`. For example,
``sub_pipeline_name`.otel_trace_group.recordsInMissingTraceGroup.count`.

| Metric suffix                       | Description                                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `recordsInMissingTraceGroup.count`  | The number of ingress records missing trace group<br>fields.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                           |
| `recordsOutFixedTraceGroup.count`   | The number of egress records with trace group fields that were<br>filled successfully.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `recordsOutMissingTraceGroup.count` | The number of egress records missing trace group<br>fields.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                            |

## Service map stateful metrics

The following metrics apply to the [Service-map stateful](https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/ "https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/") processor. Each metric is prefixed by the
sub-pipeline name and `service-map-stateful`. For example,
``sub_pipeline_name`.service-map-stateful.spansDbSize.count`.

| Metric suffix             | Description                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `spansDbSize.value`       | The in-memory byte sizes of spans in MapDB across the current<br>and previous window durations.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`        |
| `traceGroupDbSize.value`  | The in-memory byte sizes of trace groups in MapDB across the<br>current and previous window durations.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName` |
| `spansDbCount.value`      | The count of spans in MapDB across the current and previous<br>window durations.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                           |
| `traceGroupDbCount.value` | The count of trace groups in MapDB across the current and<br>previous window durations.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                    |
| `relationshipCount.value` | The count of relationships stored across the current and<br>previous window durations.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                     |

## OpenSearch metrics

The following metrics apply to the [OpenSearch](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/") sink. Each metric is prefixed by the sub-pipeline name and
`opensearch`. For example,
``sub_pipeline_name`.opensearch.bulkRequestErrors.count`.

| Metric suffix                         | Description                                                                                                                                                                       |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bulkRequestErrors.count`             | The total number of errors encountered while sending bulk<br>requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                     |
| `documentsSuccess.count`              | The number of documents successfully sent to the OpenSearch Service by bulk<br>request, including retries.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `documentsSuccessFirstAttempt.count`  | The number of documents successfully sent to OpenSearch Service by bulk<br>request on the first attempt.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`   |
| `documentErrors.count`                | The number of documents that failed to be sent by bulk<br>requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                        |
| `bulkRequestFailed.count`             | The number of bulk requests that failed.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                                   |
| `bulkRequestNumberOfRetries.count`    | The number of retries of failed bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                                             |
| `bulkBadRequestErrors.count`          | The number of `Bad Request` errors encountered<br>while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                             |
| `bulkRequestNotAllowedErrors.count`   | The number of `Request Not Allowed` errors<br>encountered while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                     |
| `bulkRequestInvalidInputErrors.count` | The number of `Invalid Input` errors encountered<br>while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                           |
| `bulkRequestNotFoundErrors.count`     | The number of `Request Not Found` errors<br>encountered while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                       |
| `bulkRequestTimeoutErrors.count`      | The number of `Request Timeout` errors encountered<br>while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                         |
| `bulkRequestServerErrors.count`       | The number of `Server Error` errors encountered<br>while sending bulk requests.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                            |
| `bulkRequestSizeBytes.count`          | A count of the distribution of payload sizes of bulk requests,<br>in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                |
| `bulkRequestSizeBytes.sum`            | The total distribution of payload sizes of bulk requests, in<br>bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                     |
| `bulkRequestSizeBytes.max`            | The maximum distribution of payload sizes of bulk requests, in<br>bytes.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                                      |
| `bulkRequestLatency.count`            | A count of data points recorded while requests are sent to the<br>plugin, including retries.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`               |
| `bulkRequestLatency.sum`              | The total latency of requests sent to the plugin, including<br>retries, in milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                   |
| `bulkRequestLatency.max`              | The maximum latency of requests sent to the plugin, including<br>retries, in milliseconds.<br>**Relevant statistics**: Max<br>**Dimension**:<br>`PipelineName`                    |
| `s3.dlqS3RecordsSuccess.count`        | The number of records successfully sent to the S3 dead letter<br>queue.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                    |
| `s3.dlqS3RecordsFailed.count`         | The number of recourds that failed to be sent to the S3 dead<br>letter queue.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                              |
| `s3.dlqS3RequestSuccess.count`        | The number of successful requests to the S3 dead letter<br>queue.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                          |
| `s3.dlqS3RequestFailed.count`         | The number of failed requests to the S3 dead letter<br>queue.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`                                              |
| `s3.dlqS3RequestLatency.count`        | A count of data points recorded while requests are sent to the<br>S3 dead letter queue, including retries.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName` |
| `s3.dlqS3RequestLatency.sum`          | The total latency of requests sent to the S3 dead letter<br>queue, including retries, in milliseconds.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`     |
| `s3.dlqS3RequestLatency.max`          | The maximum latency of requests sent to the S3 dead letter<br>queue, including retries, in milliseconds.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`   |
| `s3.dlqS3RequestSizeBytes.count`      | A count of the distribution of payload sizes of requests to<br>the S3 dead letter queue, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`         |
| `s3.dlqS3RequestSizeBytes.sum`        | The total distribution of payload sizes of requests to the S3<br>dead letter queue, in bytes.<br>**Relevant statistics**:<br>Sum<br>**Dimension**:<br>`PipelineName`              |
| `s3.dlqS3RequestSizeBytes.max`        | The maximum distribution of payload sizes of requests to the<br>S3 dead letter queue, in bytes.<br>**Relevant statistics**:<br>Max<br>**Dimension**:<br>`PipelineName`            |

## System and metering metrics

The following metrics apply to the overall OpenSearch Ingestion system. These metrics
aren't prefixed by anything.

| Metric                       | Description                                                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `system.cpu.usage.value`     | The percentage of available CPU usage for all data<br>nodes.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`, `area`,<br>`id`                                   |
| `system.cpu.count.value`     | The total amount of CPU usage for all data nodes.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`, `area`,<br>`id`                                              |
| `jvm.memory.max.value`       | The maximum amount of memory that can be used for memory<br>management, in bytes.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`, `area`,<br>`id`              |
| `jvm.memory.used.value`      | The total amount of memory used, in bytes.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`, `area`,<br>`id`signa                                                |
| `jvm.memory.committed.value` | The amount of memory that is committed for use by the Java<br>virtual machine (JVM), in bytes.<br>**Relevant statistics**:<br>Average<br>**Dimension**:<br>`PipelineName`, `area`,<br>`id` |
| `computeUnits`               | The number of Ingestion OpenSearch Compute Units (Ingestion<br>OCUs) in use by a pipeline.<br>**Relevant statistics**: Max,<br>Sum, Average<br>**Dimension**:<br>`PipelineName`            |
