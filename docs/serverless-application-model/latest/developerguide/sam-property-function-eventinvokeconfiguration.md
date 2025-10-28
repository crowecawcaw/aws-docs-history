# EventInvokeConfiguration

Configuration options for [asynchronous](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md") Lambda Alias or Version invocations.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  DestinationConfig: `EventInvokeDestinationConfiguration`
  MaximumEventAgeInSeconds: `Integer`
  MaximumRetryAttempts: `Integer`

```

## Properties

`DestinationConfig`

A configuration object that specifies the destination of an event after Lambda processes it.

_Type_: [EventInvokeDestinationConfiguration](sam-property-function-eventinvokedestinationconfiguration.md "sam-property-function-eventinvokedestinationconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the `DestinationConfig` property of an `AWS::Lambda::EventInvokeConfig` resource. SAM requires an extra parameter, "Type", that does not exist in CloudFormation.

`MaximumEventAgeInSeconds`

The maximum age of a request that Lambda sends to a function for processing.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MaximumEventAgeInSeconds` property of an `AWS::Lambda::EventInvokeConfig` resource.

`MaximumRetryAttempts`

The maximum number of times to retry before the function returns an error.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `MaximumRetryAttempts` property of an `AWS::Lambda::EventInvokeConfig` resource.

## Examples

### MaximumEventAgeInSeconds

MaximumEventAgeInSeconds example

#### YAML

```
EventInvokeConfig:
  MaximumEventAgeInSeconds: 60
  MaximumRetryAttempts: 2
  DestinationConfig:
    OnSuccess:
      Type: SQS
      Destination: arn:aws:sqs:us-west-2:012345678901:my-queue
    OnFailure:
      Type: Lambda
      Destination: !GetAtt DestinationLambda.Arn

```
