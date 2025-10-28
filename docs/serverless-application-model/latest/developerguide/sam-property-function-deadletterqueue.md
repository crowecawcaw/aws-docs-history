# DeadLetterQueue

Specifies an SQS queue or SNS topic that AWS Lambda (Lambda) sends events to when it can't process them. For more information about dead letter queue functionality, see
[Dead-letter queues](../../../lambda/latest/dg/invocation-async-retain-records.md#invocation-dlq "../../../lambda/latest/dg/invocation-async-retain-records.md#invocation-dlq") in the _AWS Lambda Developer Guide_.

SAM will automatically add appropriate permission to your Lambda function execution role to give Lambda service access to the resource. sqs:SendMessage will be added for SQS queues and sns:Publish for SNS topics.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  TargetArn: `String`
  Type: `String`

```

## Properties

`TargetArn`

The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `TargetArn` property of the `AWS::Lambda::Function` `DeadLetterConfig` data type.

`Type`

The type of dead letter queue.

_Valid values_: `SNS`, `SQS`

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### DeadLetterQueue

Dead Letter Queue example for an SNS topic.

#### YAML

```
DeadLetterQueue:
  Type: SNS
  TargetArn: arn:aws:sns:us-east-2:123456789012:my-topic

```
