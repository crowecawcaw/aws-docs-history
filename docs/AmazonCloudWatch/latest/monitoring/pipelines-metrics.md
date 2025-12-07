# Monitoring Pipelines Using CloudWatch Metrics

CloudWatch pipelines publishes metrics to Amazon CloudWatch in the `AWS/Observability Admin` namespace. You can use these metrics to monitor your pipelines' health, performance, and data flow.

## Available metrics

The following tables list the available metrics for CloudWatch pipelines.

###### Note

Pipelines metrics are only emitted when the value is non-zero.

### Core metrics

| Metric                           | Description                                                     | Dimension                          | Unit  |
| -------------------------------- | --------------------------------------------------------------- | ---------------------------------- | ----- |
| `PipelineBytesIn`                | Volume of log records going into pipeline in uncompressed bytes | PipelineName                       | Bytes |
| `PipelineBytesInByDataSource`    | Volume of incoming data with source/type breakdown              | PipelineName, DataSource, DataType | Bytes |
| `PipelineBytesOut`               | Volume of data routed to destination                            | PipelineName                       | Bytes |
| `PipelineBytesOutByDataSource`   | Volume of outgoing data with source/type breakdown              | PipelineName, DataSource, DataType | Bytes |
| `PipelineRecordsIn`              | Number of records entering the pipeline                         | PipelineName                       | Count |
| `PipelineRecordsInByDataSource`  | Number of incoming records with source/type breakdown           | PipelineName, DataSource, DataType | Count |
| `PipelineRecordsOut`             | Number of records exiting the pipeline                          | PipelineName                       | Count |
| `PipelineRecordsOutByDataSource` | Number of outgoing records with source/type breakdown           | PipelineName, DataSource, DataType | Count |

### Error and warning metrics

| Metric                          | Description                                          | Dimension                                                  | Unit  |
| ------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------- | ----- |
| `PipelineErrors`                | Aggregate count of errors in pipeline                | PipelineName                                               | Count |
| `PipelineErrorsByErrorType`     | Detailed error counts by type                        | PipelineName, ErrorSource, ErrorComponent, ErrorType       | Count |
| `PipelineWarnings`              | Number of warnings encountered                       | PipelineName                                               | Count |
| `PipelineWarningsByWarningType` | Detailed warnings by type                            | PipelineName, WarningSource, WarningComponent, WarningType | Count |
| `PipelineRecordsUnprocessed`    | Number of records that couldn't be processed         | PipelineName, DataSource, DataType                         | Count |
| `PipelineRecordsDropped`        | Number of records dropped (third-party sources only) | PipelineName, DataSource, DataType                         | Count |

## Dimensions

CloudWatch pipelines metrics use the following dimensions:

**PipelineName**
Name of the pipeline

**DataSource**
Source of the data (AWS service name or third-party source)

**DataType**
Type of data being processed

**ErrorSource**
Origin of the error (s3, aws.secrets, cloudwatch_logs)

**ErrorComponent**
Component where error occurred (source, sink, extension)

**ErrorType**
Type of error encountered

## Error types

The following error types are tracked in `PipelineErrorsByErrorType`:

**`ACCESS_DENIED`**
Permission-related failures

**`ALL`**
The total count of all errors on the pipeline

**`RESOURCE_NOT_FOUND`**
Specified resource doesn't exist

**`SOURCE_READ_FAILURE`**
Failures reading from source

**`PARSE_FAILURE`**
Data parsing errors

**`PROCESSOR_ERRORS`**
Processing operation failures

**`PAYLOAD_SIZE_EXCEEDED`**
Data size limit exceeded

## Warning types

The following warning type can occur on a pipeline:

**`THROTTLED`**
Indicates that the volume of data being sent has exceeded existing rate limits, causing some data points or events to be dropped or delayed to protect the system and ensure stability.

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

### Track errors and warnings

- Create alarms for `PipelineErrors` to detect issues quickly
- Use `PipelineErrorsByErrorType` to diagnose specific problems
- Monitor `PipelineWarnings` to identify potential issues early

### Configure appropriate thresholds

- Base thresholds on your expected data patterns
- Account for normal variations in data volume
- Consider peak usage periods when setting alarm thresholds
