# SqsSubscriptionObject

Specify an existing SQS queue option to SNS event

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  BatchSize: `String`
  Enabled: `Boolean`
  QueueArn: `String`
  QueuePolicyLogicalId: `String`
  QueueUrl: `String`

```

## Properties

`BatchSize`

The maximum number of items to retrieve in a single batch for the SQS queue.

_Type_: String

_Required_: No

_Default_: 10

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Enabled`

Disables the SQS event source mapping to pause polling and invocation.

_Type_: Boolean

_Required_: No

_Default_: True

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`QueueArn`

Specify an existing SQS queue arn.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`QueuePolicyLogicalId`

Give a custom logicalId name for the [AWS::SQS::QueuePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md") resource.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`QueueUrl`

Specify the queue URL associated with the `QueueArn` property.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### Existing SQS for SNS event

Example to add existing SQS queue for subscibing to an SNS topic.

#### YAML

```
QueuePolicyLogicalId: CustomQueuePolicyLogicalId
QueueArn:
  Fn::GetAtt: MyCustomQueue.Arn
QueueUrl:
  Ref: MyCustomQueue
BatchSize: 5

```
