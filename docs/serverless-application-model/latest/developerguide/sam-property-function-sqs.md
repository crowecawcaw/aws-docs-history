# SQS

The object describing an `SQS` event source type. For more information, see
[Using AWS Lambda with Amazon SQS](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md") in the _AWS Lambda Developer Guide_.

SAM generates [AWS::Lambda::EventSourceMapping](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md") resource when this event type is
set

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  BatchSize: `Integer`
  Enabled: `Boolean`
  FilterCriteria: `FilterCriteria`
  FunctionResponseTypes: `List`
  KmsKeyArn: `String`
  MaximumBatchingWindowInSeconds: `Integer`
  MetricsConfig: `MetricsConfig`
  ProvisionedPollerConfig: `ProvisionedPollerConfig`
  Queue: `String`
  ScalingConfig: `ScalingConfig`

```

## Properties

`BatchSize`

The maximum number of items to retrieve in a single batch.

_Type_: Integer

_Required_: No

_Default_: 10

_CloudFormation compatibility_: This property is passed directly to the
`BatchSize` property of an
`AWS::Lambda::EventSourceMapping` resource.

_Minimum_: `1`

_Maximum_: `10000`

`Enabled`

Disables the event source mapping to pause polling and invocation.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Enabled` property of an `AWS::Lambda::EventSourceMapping`
resource.

`FilterCriteria`

A object that defines the criteria to determine whether Lambda should process an
event. For more information, see [AWS Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") in
the _AWS Lambda Developer Guide_.

_Type_: [FilterCriteria](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`FilterCriteria` property of an
`AWS::Lambda::EventSourceMapping` resource.

`FunctionResponseTypes`

A list of the response types currently applied to the event source mapping. For
more information, see [Reporting
batch item failures](../../../lambda/latest/dg/with-sqs.md#services-sqs-batchfailurereporting "../../../lambda/latest/dg/with-sqs.md#services-sqs-batchfailurereporting") in the _AWS Lambda Developer Guide_.

_Valid values_: `ReportBatchItemFailures`

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`FunctionResponseTypes` property of an
`AWS::Lambda::EventSourceMapping` resource.

`KmsKeyArn`

The Amazon Resource Name (ARN) of the key to encrypt information related to this event.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn`
property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumBatchingWindowInSeconds`

The maximum amount of time, in seconds, to gather records before invoking the
function.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`MaximumBatchingWindowInSeconds` property of an
`AWS::Lambda::EventSourceMapping` resource.

`MetricsConfig`

An opt-in configuration to get enhanced metrics for event source mappings that capture each stage of processing. For an example,
see [MetricsConfig event](sam-property-function-dynamodb.md#sam-property-function-dynamodb-example-metricsconfigevent "sam-property-function-dynamodb.md#sam-property-function-dynamodb-example-metricsconfigevent").

_Type_: [MetricsConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`MetricsConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

`ProvisionedPollerConfig`

Configuration to increase the amount of pollers used to compute event source mappings.
This configuration allows for a minimum of 2 pollers and a maximum of 2000 pollers. For an example,
refer to [ProvisionedPollerConfig example](#sam-property-function-sqs-example-provisionedpollerconfig "#sam-property-function-sqs-example-provisionedpollerconfig").

_Type_: [ProvisionedPollerConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ProvisionedPollerConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

`Queue`

The ARN of the queue.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`EventSourceArn` property of an
`AWS::Lambda::EventSourceMapping` resource.

`ScalingConfig`

Scaling configuration of SQS pollers to control the invoke rate and set maximum
concurrent invokes.

_Type_: `ScalingConfig`

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ScalingConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

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

### Basic SQS event

```
Events:
  SQSEvent:
    Type: SQS
    Properties:
      Queue: arn:aws:sqs:us-west-2:012345678901:my-queue
      BatchSize: 10
      Enabled: false
      FilterCriteria:
        Filters:
          - Pattern: '{"key": ["val1", "val2"]}'

```

### Configure partial batch reporting for your SQS queue

```
Events:
  SQSEvent:
    Type: SQS
    Properties:
      Enabled: true
      FunctionResponseTypes:
        - ReportBatchItemFailures
      Queue: !GetAtt MySqsQueue.Arn
      BatchSize: 10
```

### Lambda function with

an SQS event that has scaling configured

```
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    ...
    Events:
      MySQSEvent:
        Type: SQS
        Properties:
          ...
          ScalingConfig:
            MaximumConcurrency: 10
```

### ProvisionedPollerConfig example

```
MyFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: index.handler
    Runtime: nodejs18.x
    Timeout: 30
    Events:
      SQSEvent:
        Type: SQS
        Properties:
          Queue: !GetAtt MyQueue.Arn
          BatchSize: 10
          Enabled: True
          ProvisionedPollerConfig:
            MaximumPollers: 300
            MinimumPollers: 10
```
