# Monitoring pipelines

CloudWatch pipelines publishes metrics to Amazon CloudWatch in the `AWS/Observability Admin` namespace. You can use these metrics to monitor your pipelines' health, performance, and data flow.

## Available metrics

The following tables list the available metrics for CloudWatch pipelines.

###### Note

Pipelines metrics are only emitted when the value is non-zero.

### Pipeline health metrics

The following metrics are emitted for all pipeline types (logs and metrics):

| Metric                          | Description                           | Dimension                 | Unit  |
| ------------------------------- | ------------------------------------- | ------------------------- | ----- |
| `PipelineErrors`                | Aggregate count of errors in pipeline | PipelineName              | Count |
| `PipelineErrorsByErrorType`     | Detailed error counts by type         | PipelineName, ErrorType   | Count |
| `PipelineWarnings`              | Number of warnings encountered        | PipelineName              | Count |
| `PipelineWarningsByWarningType` | Detailed warnings by type             | PipelineName, WarningType | Count |

###### Note

For logs pipelines, `PipelineErrorsByErrorType` includes additional
dimensions (`ErrorSource`, `ErrorComponent`) and
`PipelineWarningsByWarningType` includes additional dimensions
(`WarningSource`, `WarningComponent`).

### Logs pipeline metrics

The following metrics are emitted for logs pipelines:

| Metric                                   | Description                                                     | Dimension                          | Unit  |
| ---------------------------------------- | --------------------------------------------------------------- | ---------------------------------- | ----- |
| `PipelineBytesIn`                        | Volume of log records going into pipeline in uncompressed bytes | PipelineName                       | Bytes |
| `PipelineBytesInByDataSource`            | Volume of incoming data with source/type breakdown              | PipelineName, DataSource, DataType | Bytes |
| `PipelineBytesOut`                       | Volume of data routed to destination                            | PipelineName                       | Bytes |
| `PipelineBytesOutByDataSource`           | Volume of outgoing data with source/type breakdown              | PipelineName, DataSource, DataType | Bytes |
| `PipelineRecordsIn`                      | Number of records entering the pipeline                         | PipelineName                       | Count |
| `PipelineRecordsInByDataSource`          | Number of incoming records with source/type breakdown           | PipelineName, DataSource, DataType | Count |
| `PipelineRecordsOut`                     | Number of records exiting the pipeline                          | PipelineName                       | Count |
| `PipelineRecordsOutByDataSource`         | Number of outgoing records with source/type breakdown           | PipelineName, DataSource, DataType | Count |
| `PipelineRecordsUnprocessed`             | Number of records that couldn't be processed                    | PipelineName                       | Count |
| `PipelineRecordsUnprocessedByDataSource` | Number of unprocessed records with source/type breakdown        | PipelineName, DataSource, DataType | Count |

### Metrics pipeline metrics

The following metrics are emitted for metrics pipelines:

| Metric                          | Description                                                                                                                                                                                                                                                                                                                                                 | Dimension             | Unit  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| `PipelineDataPointsIn`          | Number of metric datapoints entering the pipeline (matched selection criteria)                                                                                                                                                                                                                                                                              | PipelineName, dataset | Count |
| `PipelineDataPointsOut`         | Number of metric datapoints exiting the pipeline after processing                                                                                                                                                                                                                                                                                           | PipelineName, dataset | Count |
| `PipelineDataPointsUnprocessed` | Number of metric datapoints that matched selection criteria but passed<br>through unchanged because all processors were skipped. For example, this occurs<br>when `UnsupportedTemporality` or `DestructiveOnVended`<br>restrictions apply. You can create an alarm on this metric to detect metrics in<br>your selection criteria that cannot be processed. | PipelineName, dataset | Count |

## Dimensions

CloudWatch pipelines metrics use the following dimensions:

**PipelineName**
Name of the pipeline.

**ErrorType**
Type of error encountered.

**WarningType**
Type of warning encountered.

**DataSource (logs pipelines)**
Source of the data (AWS service name or third-party source).

**DataType (logs pipelines)**
Type of data being processed.

**ErrorSource (logs pipelines)**
Origin of the error (s3, aws.secrets, cloudwatch\_logs).

**ErrorComponent (logs pipelines)**
Component where error occurred (source, sink, extension).

**dataset (metrics pipelines)**
The OTel metric dataset identifier. Currently always `default`.

## Error types

The following error types are tracked in `PipelineErrorsByErrorType`:

**`ALL`**
The total count of all errors on the pipeline.

**`PARSE_FAILURE`**
Data parsing errors.

**`PROCESSOR_ERRORS`**
Processing operation failures.

**`ACCESS_DENIED` (logs pipelines)**
Permission-related failures.

**`RESOURCE_NOT_FOUND` (logs pipelines)**
Specified resource doesn't exist.

**`SOURCE_READ_FAILURE` (logs pipelines)**
Failures reading from source.

**`PAYLOAD_SIZE_EXCEEDED` (logs pipelines)**
Data size limit exceeded.

## Warning types

The following warning types can occur on a pipeline:

**`THROTTLED`**
Indicates that the volume of data being sent has exceeded existing rate limits, causing some data points or events to be dropped or delayed to protect the system and make sure stability.

**`DestructiveOnVended` (metrics pipelines)**
A destructive processor attempted to modify a vended metric
(`instrumentation_scope.name` starting with `cloudwatch.aws/`).
The pipeline skipped the operation and counted the affected datapoints in
`PipelineDataPointsUnprocessed`.

**`UnsupportedTemporality` (metrics pipelines)**
A destructive processor attempted to modify a metric with cumulative
aggregation temporality. The pipeline skipped the operation and passed the metric
through unchanged. Cumulative temporality means the metric reports values accumulated
since a fixed start time (as defined by the
[OpenTelemetry
metrics data model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#temporality "https://opentelemetry.io/docs/specs/otel/metrics/data-model/#temporality")). The pipeline counts the affected datapoints in
`PipelineDataPointsUnprocessed`. Monitor this warning to identify metrics
in your selection criteria that cannot be processed by destructive
operations.

**`UnknownOttlPath` (metrics pipelines)**
Processor configuration references an unrecognized OTTL path — attribute operation skipped.

## Viewing metrics

You can view CloudWatch pipelines metrics using the following methods:

### Using the CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/")
2. In the navigation pane, choose **Metrics**
3. Choose the **AWS/Observability Admin** namespace
4. Select the metric dimension to view

### Using the AWS CLI

```
aws cloudwatch get-metric-statistics \
  --namespace "AWS/Observability Admin" \
  --metric-name "PipelineBytesIn" \
  --dimensions Name=PipelineName,Value=my-pipeline \
  --start-time "2025-10-29T00:00:00" \
  --end-time "2025-10-29T23:59:59" \
  --period 300 \
  --statistics Sum
```

## Creating alarms

You can create CloudWatch alarms based on any of these metrics. Here's an example of creating an alarm for pipeline errors:

```
aws cloudwatch put-metric-alarm \
  --alarm-name "HighPipelineErrors" \
  --alarm-description "Alert on high error rate" \
  --metric-name "PipelineErrors" \
  --namespace "AWS/Observability Admin" \
  --dimensions Name=PipelineName,Value=my-pipeline \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --statistic Sum \
  --alarm-actions arn:aws:sns:region:account-id:topic-name
```

## Best practices for CloudWatch pipelines metrics

### Monitor data flow

- Use `PipelineBytesIn` and `PipelineBytesOut` to track data volume
- Monitor `PipelineRecordsIn` and `PipelineRecordsOut` to track record counts
- Watch for unexpected changes in throughput patterns
- To monitor dropped records, compute `PipelineRecordsIn` - `PipelineRecordsOut` over a given period; a sustained positive difference indicates records that did not reach the destination.

### Track errors and warnings

- Create alarms for `PipelineErrors` to detect issues quickly
- Use `PipelineErrorsByErrorType` to diagnose specific problems
- Monitor `PipelineWarnings` to identify potential issues early

### Configure appropriate thresholds

- Base thresholds on your expected data patterns
- Account for normal variations in data volume
- Consider peak usage periods when setting alarm thresholds
