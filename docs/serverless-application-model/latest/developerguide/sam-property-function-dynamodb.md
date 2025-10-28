# DynamoDB

The object describing a `DynamoDB` event source type. For more information, see [Using AWS Lambda with Amazon DynamoDB](../../../lambda/latest/dg/with-ddb.md "../../../lambda/latest/dg/with-ddb.md") in the _AWS Lambda Developer Guide_.

AWS SAM generates an [AWS::Lambda::EventSourceMapping](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md") resource when this event type is set.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  BatchSize: `Integer`
  BisectBatchOnFunctionError: `Boolean`
  DestinationConfig: `DestinationConfig`
  Enabled: `Boolean`
  FilterCriteria: `FilterCriteria`
  FunctionResponseTypes: `List`
  KmsKeyArn: `String`
  MaximumBatchingWindowInSeconds: `Integer`
  MaximumRecordAgeInSeconds: `Integer`
  MaximumRetryAttempts: `Integer`
  MetricsConfig: `MetricsConfig`
  ParallelizationFactor: `Integer`
  StartingPosition: `String`
  StartingPositionTimestamp: `Double`
  Stream: `String`
  TumblingWindowInSeconds: `Integer`

```

## Properties

`BatchSize`

The maximum number of items to retrieve in a single batch.

_Type_: Integer

_Required_: No

_Default_: 100

_AWS CloudFormation compatibility_: This property is passed directly to the `BatchSize` property of an `AWS::Lambda::EventSourceMapping` resource.

_Minimum_: `1`

_Maximum_: `1000`

`BisectBatchOnFunctionError`

If the function returns an error, split the batch in two and retry.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `BisectBatchOnFunctionError` property of an `AWS::Lambda::EventSourceMapping` resource.

`DestinationConfig`

An Amazon Simple Queue Service (Amazon SQS) queue or Amazon Simple Notification Service (Amazon SNS) topic destination for discarded records.

_Type_: [DestinationConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `DestinationConfig` property of an `AWS::Lambda::EventSourceMapping` resource.

`Enabled`

Disables the event source mapping to pause polling and invocation.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Enabled` property of an `AWS::Lambda::EventSourceMapping` resource.

`FilterCriteria`

A object that defines the criteria to determine whether Lambda should process an event. For more information, see [AWS Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") in the _AWS Lambda Developer Guide_.

_Type_: [FilterCriteria](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `FilterCriteria` property of an `AWS::Lambda::EventSourceMapping` resource.

`FunctionResponseTypes`

A list of the response types currently applied to the event source mapping. For more information, see [Reporting batch item failures](../../../lambda/latest/dg/with-ddb.md#services-ddb-batchfailurereporting "../../../lambda/latest/dg/with-ddb.md#services-ddb-batchfailurereporting") in the _AWS Lambda Developer Guide_.

_Valid values_: `ReportBatchItemFailures`

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `FunctionResponseTypes` property of an `AWS::Lambda::EventSourceMapping` resource.

`KmsKeyArn`

The Amazon Resource Name (ARN) of the key to encrypt information related to this event.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn`
property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumBatchingWindowInSeconds`

The maximum amount of time to gather records before invoking the function, in seconds.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MaximumBatchingWindowInSeconds` property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumRecordAgeInSeconds`

The maximum age of a record that Lambda sends to a function for processing.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MaximumRecordAgeInSeconds` property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumRetryAttempts`

The maximum number of times to retry when the function returns an error.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MaximumRetryAttempts` property of an `AWS::Lambda::EventSourceMapping` resource.

`MetricsConfig`

An opt-in configuration to get enhanced metrics for event source mappings that capture each stage of processing. For an example,
see [MetricsConfig event](#sam-property-function-dynamodb-example-metricsconfigevent "#sam-property-function-dynamodb-example-metricsconfigevent").

_Type_: [MetricsConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MetricsConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

`ParallelizationFactor`

The number of batches to process from each shard concurrently.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `ParallelizationFactor` property of an `AWS::Lambda::EventSourceMapping` resource.

`StartingPosition`

The position in a stream from which to start reading.

- `AT_TIMESTAMP` – Specify a time from which to start reading records.
- `LATEST` – Read only new records.
- `TRIM_HORIZON` – Process all available records.

_Valid values_: `AT_TIMESTAMP` | `LATEST` |
`TRIM_HORIZON`

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `StartingPosition` property of an `AWS::Lambda::EventSourceMapping` resource.

`StartingPositionTimestamp`

The time from which to start reading, in Unix time seconds. Define `StartingPositionTimestamp`
when `StartingPosition` is specified as `AT_TIMESTAMP`.

_Type_: Double

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartingPositionTimestamp`
property of an `AWS::Lambda::EventSourceMapping` resource.

`Stream`

The Amazon Resource Name (ARN) of the DynamoDB stream.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `EventSourceArn` property of an `AWS::Lambda::EventSourceMapping` resource.

`TumblingWindowInSeconds`

The duration, in seconds, of a processing window. The valid range is 1 to 900 (15 minutes).

For more information, see [Tumbling windows](../../../lambda/latest/dg/with-ddb.md#streams-tumbling "../../../lambda/latest/dg/with-ddb.md#streams-tumbling") in the _AWS Lambda Developer Guide_.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `TumblingWindowInSeconds` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples

### MetricsConfig event

The following is an example of a resource that uses the `MetricsConfig` property to capture each stage of processing for their event source mappings.

```
Resources:
  FilteredEventsFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: s3://sam-demo-bucket/metricsConfig.zip
      Handler: index.handler
      Runtime: nodejs16.x
      Events:
        KinesisStream:
          Type: Kinesis
          Properties:
            Stream: !GetAtt KinesisStream.Arn
            StartingPosition: LATEST
            MetricsConfig:
              Metrics:
              - EventCount
```

### DynamoDB event source for existing DynamoDB table

DynamoDB event source for a DynamoDB table that already exists in an AWS account.

#### YAML

```
Events:
  DDBEvent:
    Type: DynamoDB
    Properties:
      Stream: arn:aws:dynamodb:us-east-1:123456789012:table/TestTable/stream/2016-08-11T21:21:33.291
      StartingPosition: TRIM_HORIZON
      BatchSize: 10
      Enabled: false


```

### DynamoDB Event for DynamoDB Table Declared in Template

DynamoDB Event for a DynamoDB table that is declared in the same template file.

#### YAML

```
Events:
  DDBEvent:
    Type: DynamoDB
    Properties:
      Stream:
        !GetAtt MyDynamoDBTable.StreamArn   # This must be the name of a DynamoDB table declared in the same template file
      StartingPosition: TRIM_HORIZON
      BatchSize: 10
      Enabled: false


```
