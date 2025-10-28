# Logging Amazon EventBridge Pipes performance

EventBridge Pipes logging enables you to have EventBridge Pipes send records detailing pipe performance to supported AWS services.
Use logs to gain insight into your pipe’s execution performance, and to help with troubleshooting and debugging.

You can select the following AWS services as _log destinations_ to
which EventBridge Pipes delivers records:

- CloudWatch Logs

EventBridge delivers log records to the specified CloudWatch Logs log group.

Use CloudWatch Logs to centralize the logs from all of your systems, applications, and AWS
services that you use, in a single, highly scalable service. For more information, see
[Working with
log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs User
Guide_.

- Firehose stream logs

EventBridge delivers log records to a Firehose delivery stream.

Amazon Data Firehose is a fully-managed service for delivering real-time streaming data to
destinations such as certain AWS services, as well as any custom HTTP endpoint or HTTP
endpoints owned by supported third-party service providers. For more information, see [Creating an Amazon Data Firehose
delivery stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the _Amazon Data Firehose User Guide_.

- Amazon S3 logs

EventBridge delivers log records as Amazon S3 objects to the specified bucket.

Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. For more information, see [Uploading, downloading, and working with objects in Amazon S3](../../../AmazonS3/latest/userguide/uploading-downloading-objects.md "../../../AmazonS3/latest/userguide/uploading-downloading-objects.md")
in the _Amazon Simple Storage Service User Guide_.

## How Amazon EventBridge Pipes logging works

A pipe _execution_ is an event or batch of events received by a pipe
that travel to an enrichment and/or target. If enabled, EventBridge generates a log record for each
execution step it performs as the event batch is processed. The information contained in the
record applies to the event batch, be it a single event or up to 10,000 events.

You can configure the size of the event batch on the pipe source and target. For more information, see [Amazon EventBridge Pipes batching and concurrency](eb-pipes-batching-concurrency.md "eb-pipes-batching-concurrency.md").

The record data sent to each log destination is the same.

If a Amazon CloudWatch Logs destination is configured, the log records delivered to all destinations have a limit of 256kb. Fields will be truncated as necessary.

You can customize the records EventBridge sends to the selected log destinations in the following way:

- You can specify the _log level_, which determines the execution steps for which EventBridge sends records to the selected log destinations.
  For more information, see [Specifying EventBridge Pipes log level](#eb-pipes-logs-level "#eb-pipes-logs-level").
- You can specify whether EventBridge Pipes includes execution data in records for execution steps
  where it is relevant. This data includes:

      + The payload of the event batch
      + The request sent to the AWS enrichment or target service
      + The response returned by the AWS enrichment or target service

  For more information, see [Including execution data in EventBridge Pipes logs](#eb-pipes-logs-execution-data "#eb-pipes-logs-execution-data").

## Specifying EventBridge Pipes log level

You can specify the types of execution steps for which EventBridge sends records to the selected log destinations.

Choose from the following levels of detail to include in log records. The log level applies to all log destinations specified for the pipe.
Each log level includes the execution steps of the previous log levels.

- OFF – EventBridge does not send any records to any
  specified log destinations. This is the default setting.
- ERROR – EventBridge sends any records related to errors
  generated during pipe execution to the specified log destinations.
- INFO – EventBridge sends any records related to errors, as well as select other steps performed during pipe execution to the specified log destinations.
- TRACE – EventBridge sends any records generated during
  any steps in the pipe execution to the specified log destinations.

In the EventBridge console, CloudWatch logs is selected as a log destination
by default, as is the `ERROR` log level. So, by default, EventBridge Pipes
creates a new CloudWatch log group to which it sends log records containing the
`ERROR` level of detail. No default is selected when you configure logs programmatically.

The following table lists the execution steps included in each log level.

| Step                                | TRACE | INFO | ERROR | OFF |
| ----------------------------------- | ----- | ---- | ----- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Execution Failed                    | x     | x    | x     |     |
| Execution Partially Failed          | x     | x    | x     |     |
| Execution Started                   | x     | x    |       |     |
| Execution Succeeded                 | x     | x    |       |     |
| Execution Throttled                 | x     | x    | x     |     |
| Execution Timeout                   | x     | x    | x     |     |
| Enrichment Invocation Failed        | x     | x    | x     |     |
| Enrichment Invocation Skipped       | x     | x    |       |     |
| Enrichment Invocation Started       | x     |      |       |     |
| Enrichment Invocation Succeeded     | x     |      |       |     |
| Enrichment Stage Entered            | x     | x    |       |     |
| Enrichment Stage Failed             | x     | x    | x     |     |
| Enrichment Stage Succeeded          | x     | x    |       |     |
| Enrichment Transformation Failed    | x     | x    | x     |     |
| Enrichment Transformation Started   | x     |      |       |     |
| Enrichment Transformation Succeeded | x     |      |       |     |
| Target Invocation Failed            | x     | x    | x     |     |
| Target Invocation Partially Failed  | x     | x    | x     |     |
| Target Invocation Skipped           | x     |      |       |     |
| Target Invocation Started           | x     |      |       |     |
| Target Invocation Succeeded         | x     |      |       |     |
| Target Stage Entered                | x     | x    |       |     |
| Target Stage Failed                 | x     | x    | x     |     |
| Target Stage Partially Failed       | x     | x    | x     |     |
| Target Stage Skipped                | x     |      |       |     |
| Target Stage Succeeded              | x     | x    |       |     |
| Target Transformation Failed        | x     | x    | x     |     |
| Target Transformation Started       | x     |      |       |     |
| Target Transformation Succeeded     | x     |      |       |     | ## Including execution data in EventBridge Pipes logs You can specify for EventBridge to include _execution data_ in the records it generates. Execution data includes fields representing the event batch payload, as well as the request sent to and the response from the enrichment and target. Execution data is useful for troubleshooting and debugging. The `payload` field contains the actual contents of each event included in the batch, enabling you to correlate individual events to a specific pipe execution. If you choose to include execution data, it is included for all log destinations specified for the pipe. ###### Important These fields may contain sensitive information. EventBridge makes no attempt to redact the contents of these fields during logging. When including execution data, EventBridge adds the following fields to the relevant records: <br>• **`payload`** Represents the contents of the event batch being processed by the pipe. EventBridge includes the `payload` field in records generated at steps where the event batch contents may have been updated. This includes the following steps: + `EXECUTION_STARTED` + `ENRICHMENT_TRANSFORMATION_SUCCEEDED` + `ENRICHMENT_STAGE_SUCCEEDED` + `TARGET_TRANSFORMATION_SUCCEEDED` + `TARGET_STAGE_SUCCEEDED` <br>• **`awsRequest`** Represents the request sent to the enrichment or target as a JSON string. For requests sent to an API destination, this represents the HTTP request sent to that endpoint. EventBridge includes the `awsRequest` field in records generated at the final steps of enrichment and targeting; that is, after EventBridge has executed or attempted to execute the request against the specified enrichment or target service. This includes the following steps: + `ENRICHMENT_INVOCATION_FAILED` + `ENRICHMENT_INVOCATION_SUCCEEDED` + `TARGET_INVOCATION_FAILED` + `TARGET_INVOCATION_PARTIALLY_FAILED` + `TARGET_INVOCATION_SUCCEEDED` <br>• **`awsResponse`** Represents the response returned by the enrichment or target, in JSON format. For requests sent to an API destination, this represents the HTTP response returned from that endpoint. As with `awsRequest`, EventBridge includes the `awsResponse` field in records generated at the final steps of enrichment and targeting; that is, after EventBridge has executed or attempted to execute a request against the specified enrichment or target service and received a response. This includes the following steps: + `ENRICHMENT_INVOCATION_FAILED` + `ENRICHMENT_INVOCATION_SUCCEEDED` + `TARGET_INVOCATION_FAILED` + `TARGET_INVOCATION_PARTIALLY_FAILED` + `TARGET_INVOCATION_SUCCEEDED` For a discussion of pipe execution steps, see [EventBridge Pipes execution steps](eb-pipes-logs-execution-steps.md "eb-pipes-logs-execution-steps.md"). ### Truncating execution data in EventBridge Pipes log records If you choose to have EventBridge include execution data in a pipe's log records, there is a possibility that a record may exceed the 256 KB size limit. To prevent this, EventBridge automatically truncates the execution data fields, in the following order. EventBridge truncates each field entirely before progressing to truncate the next field. EventBridge truncates field data simply by removing characters from the end of the data string; no attempt is made to truncate based on data importance, and truncation will invalidate JSON formatting. <br>• `payload` <br>• `awsRequest` <br>• `awsResponse` If EventBridge does truncate fields in the event, the `truncatedFields` field includes a list of the truncated data fields. ## Error reporting in EventBridge Pipes log records EventBridge also includes error data, where available, in pipe execution steps that represent failure states. These steps include: <br>• `ExecutionThrottled` <br>• `ExecutionTimeout` <br>• `ExecutionFailed` <br>• `ExecutionPartiallyFailed` <br>• `EnrichmentTransformationFailed` <br>• `EnrichmentInvocationFailed` <br>• `EnrichmentStageFailed` <br>• `TargetTransformationFailed` <br>• `TargetInvocationFailed` <br>• `TargetInvocationPartiallyFailed` <br>• `TargetStageFailed` <br>• `TargetStagePartiallyFailed` |
