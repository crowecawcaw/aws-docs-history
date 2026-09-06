

# SQS
<a name="sam-property-function-sqs"></a>

The object describing an `SQS` event source type. For more information, see [Using AWS Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html) in the *AWS Lambda Developer Guide*.

SAM generates [AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html) resource when this event type is set

## Syntax
<a name="sam-property-function-sqs-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-sqs-syntax.yaml"></a>

```
  [BatchSize](#sam-function-sqs-batchsize): {{Integer}}
  [Enabled](#sam-function-sqs-enabled): {{Boolean}}
  [FilterCriteria](#sam-function-sqs-filtercriteria): {{[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)}}
  [FunctionResponseTypes](#sam-function-sqs-functionresponsetypes): {{List}}
  KmsKeyArn: {{String}}
  [MaximumBatchingWindowInSeconds](#sam-function-sqs-maximumbatchingwindowinseconds): {{Integer}}
  [MetricsConfig](#sam-function-sqs-metricsconfig): {{[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)}}
  [ProvisionedPollerConfig](#sam-function-sqs-provisionedpollerconfig): {{[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)}}
  [Queue](#sam-function-sqs-queue): {{String}}
  ScalingConfig: {{[ScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-scalingconfig.html)}}
```

## Properties
<a name="sam-property-function-sqs-properties"></a>

 `BatchSize`   <a name="sam-function-sqs-batchsize"></a>
The maximum number of items to retrieve in a single batch.  
*Type*: Integer  
*Required*: No  
*Default*: 10  
*CloudFormation compatibility*: This property is passed directly to the `[BatchSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize)` property of an `AWS::Lambda::EventSourceMapping` resource.  
*Minimum*: `1`  
*Maximum*: `10000`

 `Enabled`   <a name="sam-function-sqs-enabled"></a>
Disables the event source mapping to pause polling and invocation.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Enabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FilterCriteria`   <a name="sam-function-sqs-filtercriteria"></a>
A object that defines the criteria to determine whether Lambda should process an event. For more information, see [AWS Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) in the *AWS Lambda Developer Guide*.  
*Type*: [FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FunctionResponseTypes`   <a name="sam-function-sqs-functionresponsetypes"></a>
 A list of the response types currently applied to the event source mapping. For more information, see [ Reporting batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting) in the *AWS Lambda Developer Guide*.   
 *Valid values*: `ReportBatchItemFailures`   
 *Type*: List   
 *Required*: No   
 *CloudFormation compatibility*: This property is passed directly to the `[FunctionResponseTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes)` property of an `AWS::Lambda::EventSourceMapping` resource. 

 `KmsKeyArn`   <a name="sam-function-sqs-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the key to encrypt information related to this event.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-kmskeyarn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumBatchingWindowInSeconds`   <a name="sam-function-sqs-maximumbatchingwindowinseconds"></a>
The maximum amount of time, in seconds, to gather records before invoking the function.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumBatchingWindowInSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MetricsConfig`   <a name="sam-function-sqs-metricsconfig"></a>
An opt-in configuration to get enhanced metrics for event source mappings that capture each stage of processing. For an example, see [MetricsConfig event](sam-property-function-dynamodb.md#sam-property-function-dynamodb-example-metricsconfigevent).  
*Type*: [MetricsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ProvisionedPollerConfig`   <a name="sam-function-sqs-provisionedpollerconfig"></a>
Configuration to increase the amount of pollers used to compute event source mappings. This configuration allows for a minimum of 2 pollers and a maximum of 2000 pollers. For an example, refer to [ProvisionedPollerConfig example](#sam-property-function-sqs-example-provisionedpollerconfig).  
*Type*: [ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Queue`   <a name="sam-function-sqs-queue"></a>
The ARN of the queue.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[EventSourceArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ScalingConfig`   <a name="sam-function-sqs-scalingconfig"></a>
Scaling configuration of SQS pollers to control the invoke rate and set maximum concurrent invokes.  
*Type*: `[ScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-scalingconfig.html)`  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ ScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-scalingconfig.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples
<a name="sam-property-function-sqs--examples"></a>

### MetricsConfig event
<a name="sam-property-function-sqs-example-metricsconfigevent"></a>

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
<a name="sam-property-function-sqs--examples--sqs-event"></a>

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
<a name="sam-property-function-sqs--examples--sqs-partial-batch"></a>

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

### Lambda function with an SQS event that has scaling configured
<a name="sam-property-function-sqs--examples--sqs-event-scaling"></a>

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
<a name="sam-property-function-sqs-example-provisionedpollerconfig"></a>

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