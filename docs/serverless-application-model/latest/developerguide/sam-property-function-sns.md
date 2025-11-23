# SNS

The object describing an `SNS` event source type.

SAM generates [AWS::SNS::Subscription](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md") resource when this event type is set

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  FilterPolicy: `SnsFilterPolicy`
  FilterPolicyScope: `String`
  RedrivePolicy: `Json`
  Region: `String`
  SqsSubscription: `Boolean | SqsSubscriptionObject`
  Topic: `String`

```

## Properties

`FilterPolicy`

The filter policy JSON assigned to the subscription. For more information, see
[GetSubscriptionAttributes](../../../sns/latest/api/API_GetSubscriptionAttributes.md "../../../sns/latest/api/API_GetSubscriptionAttributes.md") in the Amazon Simple Notification Service API
Reference.

_Type_: [SnsFilterPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md#cfn-sns-subscription-filterpolicy "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md#cfn-sns-subscription-filterpolicy")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`FilterPolicy` property of an `AWS::SNS::Subscription`
resource.

`FilterPolicyScope`

This attribute lets you choose the filtering scope by using one of the following string value types:

- `MessageAttributes` – The filter is applied on the message attributes.
- `MessageBody` – The filter is applied on the message body.

_Type_: String

_Required_: No

_Default_: `MessageAttributes`

_CloudFormation compatibility_: This property is passed directly to the `FilterPolicyScope` property of an `AWS::SNS::Subscription` resource.

`RedrivePolicy`

When specified, sends undeliverable messages to the specified Amazon SQS dead-letter
queue. Messages that can't be delivered due to client errors (for example, when the
subscribed endpoint is unreachable) or server errors (for example, when the service that
powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue
for further analysis or reprocessing.

For more information about the redrive policy and dead-letter queues, see [Amazon SQS dead-letter queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md") in the _Amazon Simple Queue Service Developer Guide_.

_Type_: Json

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RedrivePolicy` property of an `AWS::SNS::Subscription`
resource.

`Region`

For cross-region subscriptions, the region in which the topic resides.

If no region is specified, CloudFormation uses the region of the caller as the
default.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Region` property of an `AWS::SNS::Subscription`
resource.

`SqsSubscription`

Set this property to true, or specify `SqsSubscriptionObject` to enable
batching SNS topic notifications in an SQS queue. Setting this property to
`true` creates a new SQS queue, whereas specifying a
`SqsSubscriptionObject` uses an existing SQS queue.

_Type_: Boolean | [SqsSubscriptionObject](sam-property-function-sqssubscriptionobject.md "sam-property-function-sqssubscriptionobject.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`Topic`

The ARN of the topic to subscribe to.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`TopicArn` property of an `AWS::SNS::Subscription`
resource.

## Examples

### SNS Event

Source Example

SNS Event Source Example

#### YAML

```
Events:
  SNSEvent:
    Type: SNS
    Properties:
      Topic: arn:aws:sns:us-east-1:123456789012:my_topic
      SqsSubscription: true
      FilterPolicy:
        store:
          - example_corp
        price_usd:
          - numeric:
              - ">="
              - 100

```
