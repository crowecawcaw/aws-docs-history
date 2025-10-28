# EventInvokeDestinationConfiguration

A configuration object that specifies the destination of an event after Lambda processes it.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  OnFailure: `OnFailure`
  OnSuccess: `OnSuccess`

```

## Properties

`OnFailure`

A destination for events that failed processing.

_Type_: [OnFailure](sam-property-function-onfailure.md "sam-property-function-onfailure.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the `OnFailure` property of an `AWS::Lambda::EventInvokeConfig` resource. Requires `Type`, an additional SAM-only property.

`OnSuccess`

A destination for events that were processed successfully.

_Type_: [OnSuccess](sam-property-function-onsuccess.md "sam-property-function-onsuccess.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the `OnSuccess` property of an `AWS::Lambda::EventInvokeConfig` resource. Requires `Type`, an additional SAM-only property.

## Examples

### OnSuccess

OnSuccess example

#### YAML

```
EventInvokeConfig:
  DestinationConfig:
    OnSuccess:
      Type: SQS
      Destination: arn:aws:sqs:us-west-2:012345678901:my-queue
    OnFailure:
      Type: Lambda
      Destination: !GetAtt DestinationLambda.Arn

```
