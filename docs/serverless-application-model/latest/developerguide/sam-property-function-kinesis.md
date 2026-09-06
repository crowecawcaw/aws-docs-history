

# Kinesis
<a name="sam-property-function-kinesis"></a>

The object describing a `Kinesis` event source type. For more information, see [Using AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html) in the *AWS Lambda Developer Guide*.

AWS SAM generates an [AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html) resource when this event type is set.

## Syntax
<a name="sam-property-function-kinesis-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-kinesis-syntax.yaml"></a>

```
  [BatchSize](#sam-function-kinesis-batchsize): {{Integer}}
  [BisectBatchOnFunctionError](#sam-function-kinesis-bisectbatchonfunctionerror): {{Boolean}}
  [DestinationConfig](#sam-function-kinesis-destinationconfig): {{[DestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig)}}
  [Enabled](#sam-function-kinesis-enabled): {{Boolean}}
  [FilterCriteria](#sam-function-kinesis-filtercriteria): {{[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)}}
  [FunctionResponseTypes](#sam-function-kinesis-functionresponsetypes): {{List}}
  KmsKeyArn: {{String}}          
  [MaximumBatchingWindowInSeconds](#sam-function-kinesis-maximumbatchingwindowinseconds): {{Integer}}
  [MaximumRecordAgeInSeconds](#sam-function-kinesis-maximumrecordageinseconds): {{Integer}}
  [MaximumRetryAttempts](#sam-function-kinesis-maximumretryattempts): {{Integer}}
  [MetricsConfig](#sam-function-kinesis-metricsconfig): {{[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)}}
  [ParallelizationFactor](#sam-function-kinesis-parallelizationfactor): {{Integer}}
  [StartingPosition](#sam-function-kinesis-startingposition): {{String}}
  StartingPositionTimestamp: {{Double}}
  [Stream](#sam-function-kinesis-stream): {{String}}
  [TumblingWindowInSeconds](#sam-function-kinesis-tumblingwindowinseconds): {{Integer}}
```

## Properties
<a name="sam-property-function-kinesis-properties"></a>

 `BatchSize`   <a name="sam-function-kinesis-batchsize"></a>
The maximum number of items to retrieve in a single batch.  
*Type*: Integer  
*Required*: No  
*Default*: 100  
*CloudFormation compatibility*: This property is passed directly to the `[BatchSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize)` property of an `AWS::Lambda::EventSourceMapping` resource.  
*Minimum*: `1`  
*Maximum*: `10000`

 `BisectBatchOnFunctionError`   <a name="sam-function-kinesis-bisectbatchonfunctionerror"></a>
If the function returns an error, split the batch in two and retry.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[BisectBatchOnFunctionError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `DestinationConfig`   <a name="sam-function-kinesis-destinationconfig"></a>
An Amazon Simple Queue Service (Amazon SQS) queue or Amazon Simple Notification Service (Amazon SNS) topic destination for discarded records.  
*Type*: [DestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[DestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Enabled`   <a name="sam-function-kinesis-enabled"></a>
Disables the event source mapping to pause polling and invocation.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Enabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FilterCriteria`   <a name="sam-function-kinesis-filtercriteria"></a>
A object that defines the criteria to determine whether Lambda should process an event. For more information, see [AWS Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) in the *AWS Lambda Developer Guide*.  
*Type*: [FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FunctionResponseTypes`   <a name="sam-function-kinesis-functionresponsetypes"></a>
A list of the response types currently applied to the event source mapping. For more information, see [Reporting batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-batchfailurereporting) in the *AWS Lambda Developer Guide*.  
*Valid values*: `ReportBatchItemFailures`  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionResponseTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `KmsKeyArn`   <a name="sam-function-kinesis-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the key to encrypt information related to this event.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-kmskeyarn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumBatchingWindowInSeconds`   <a name="sam-function-kinesis-maximumbatchingwindowinseconds"></a>
The maximum amount of time to gather records before invoking the function, in seconds.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumBatchingWindowInSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRecordAgeInSeconds`   <a name="sam-function-kinesis-maximumrecordageinseconds"></a>
The maximum age of a record that Lambda sends to a function for processing.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRecordAgeInSeconds](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRetryAttempts`   <a name="sam-function-kinesis-maximumretryattempts"></a>
The maximum number of times to retry when the function returns an error.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRetryAttempts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MetricsConfig`   <a name="sam-function-kinesis-metricsconfig"></a>
An opt-in configuration to get enhanced metrics for event source mappings that capture each stage of processing. For an example, see [MetricsConfig event](sam-property-function-dynamodb.md#sam-property-function-dynamodb-example-metricsconfigevent).  
*Type*: [MetricsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ParallelizationFactor`   <a name="sam-function-kinesis-parallelizationfactor"></a>
The number of batches to process from each shard concurrently.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ParallelizationFactor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPosition`   <a name="sam-function-kinesis-startingposition"></a>
The position in a stream from which to start reading.  
+ `AT_TIMESTAMP` – Specify a time from which to start reading records.
+ `LATEST` – Read only new records.
+ `TRIM_HORIZON` – Process all available records.
*Valid values*: `AT_TIMESTAMP` \| `LATEST` \| `TRIM_HORIZON`  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPosition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPositionTimestamp`   <a name="sam-function-kinesis-startingpositiontimestamp"></a>
The time from which to start reading, in Unix time seconds. Define `StartingPositionTimestamp` when `StartingPosition` is specified as `AT_TIMESTAMP`.  
*Type*: Double  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPositionTimestamp](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Stream`   <a name="sam-function-kinesis-stream"></a>
The Amazon Resource Name (ARN) of the data stream or a stream consumer.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[EventSourceArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `TumblingWindowInSeconds`   <a name="sam-function-kinesis-tumblingwindowinseconds"></a>
The duration, in seconds, of a processing window. The valid range is 1 to 900 (15 minutes).  
For more information, see [Tumbling windows](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#streams-tumbling) in the *AWS Lambda Developer Guide*.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[TumblingWindowInSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples
<a name="sam-property-function-kinesis--examples"></a>

### MetricsConfig event
<a name="sam-property-function-kinesis-example-metricsconfigevent"></a>

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

### Kinesis event source
<a name="sam-property-function-kinesis--examples--kinesis-event-source"></a>

The following is an example of a Kinesis event source.

#### YAML
<a name="sam-property-function-kinesis--examples--kinesis-event-source--yaml"></a>

```
Events:
  KinesisEvent:
    Type: Kinesis
    Properties:
      Stream: arn:aws:kinesis:us-east-1:123456789012:stream/my-stream
      StartingPosition: TRIM_HORIZON
      BatchSize: 10
      Enabled: false
      FilterCriteria: 
        Filters: 
          - Pattern: '{"key": ["val1", "val2"]}'
```