# DeadLetterConfig

The object used to specify the Amazon Simple Queue Service (Amazon SQS) queue where EventBridge sends events after a failed target invocation. Invocation can fail, for example, when sending an event to a Lambda function that doesn’t exist, or insufficient permissions to invoke the Lambda function. For more information, see [Event retry policy and using dead-letter queues](../../../eventbridge/latest/userguide/rule-dlq.md "../../../eventbridge/latest/userguide/rule-dlq.md") in the _Amazon EventBridge User Guide_.

###### Note

The [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md") resource type has a similar data type, `DeadLetterQueue` which handles failures that occur after successful invocation of the target Lambda function. Examples of this type of failure include Lambda throttling, or errors returned by the Lambda target function. For more information about the function `DeadLetterQueue` property, see [Dead-letter queues](../../../lambda/latest/dg/invocation-async.md#invocation-dlq "../../../lambda/latest/dg/invocation-async.md#invocation-dlq") in the _AWS Lambda Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Arn: `String`
  QueueLogicalId: `String`
  Type: `String`

```

## Properties

`Arn`

The Amazon Resource Name (ARN) of the Amazon SQS queue specified as the target for the dead-letter queue.

###### Note

Specify either the `Type` property or `Arn` property, but not both.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `Arn` property of the `AWS::Events::Rule` `DeadLetterConfig` data type.

`QueueLogicalId`

The custom name of the dead letter queue that AWS SAM creates if `Type` is specified.

###### Note

If the `Type` property is not set, this property is ignored.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Type`

The type of the queue. When this property is set, AWS SAM automatically creates a dead-letter queue and attaches necessary [resource-based policy](../../../eventbridge/latest/userguide/rule-dlq.md#dlq-perms "../../../eventbridge/latest/userguide/rule-dlq.md#dlq-perms") to grant permission to rule resource to send events to the queue.

###### Note

Specify either the `Type` property or `Arn` property, but not both.

_Valid values_: `SQS`

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### DeadLetterConfig

DeadLetterConfig

#### YAML

```
DeadLetterConfig:
  Type: SQS
  QueueLogicalId: MyDLQ

```
