# EventBridgeRule

The object describing an `EventBridgeRule` event source type, which sets your
serverless function as the target of an Amazon EventBridge rule. For more information, see [What Is
Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md") in the _Amazon EventBridge User Guide_.

AWS SAM generates an [AWS::Events::Rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md") resource when this event type is set. AWS SAM also creates an `AWS::Lambda::Permission` resource, which is needed so the `EventBridgeRule` can call Lambda.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  DeadLetterConfig: `DeadLetterConfig`
  EventBusName: `String`
  Input: `String`
  InputPath: `String`
  InputTransformer: `InputTransformer`
  Pattern: `EventPattern`
  RetryPolicy: `RetryPolicy`
  RuleName: `String`
  State: `String`
  Target: `Target`

```

## Properties

`DeadLetterConfig`

Configure the Amazon Simple Queue Service (Amazon SQS) queue where EventBridge sends events after a failed target
invocation. Invocation can fail, for example, when sending an event to a Lambda function
that doesn't exist, or when EventBridge has insufficient permissions to invoke the Lambda
function. For more information, see [Event retry policy
and using dead-letter queues](../../../eventbridge/latest/userguide/rule-dlq.md "../../../eventbridge/latest/userguide/rule-dlq.md") in the _Amazon EventBridge User Guide_.

###### Note

The [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md")
resource type has a similar data type, `DeadLetterQueue`, which handles
failures that occur after successful invocation of the target Lambda function. Examples
of these types of failures include Lambda throttling, or errors returned by the Lambda
target function. For more information about the function `DeadLetterQueue`
property, see [Dead-letter queues](../../../lambda/latest/dg/invocation-async.md#invocation-dlq "../../../lambda/latest/dg/invocation-async.md#invocation-dlq") in the _AWS Lambda Developer Guide_.

_Type_: [DeadLetterConfig](sam-property-function-deadletterconfig.md "sam-property-function-deadletterconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`DeadLetterConfig` property of the `AWS::Events::Rule`
`Target` data type. The AWS SAM version of this property includes additional
subproperties, in case you want AWS SAM to create the dead-letter queue for you.

`EventBusName`

The event bus to associate with this rule. If you omit this property, AWS SAM uses the
default event bus.

_Type_: String

_Required_: No

_Default_: Default event bus

_CloudFormation compatibility_: This property is passed directly to the
`EventBusName` property of an `AWS::Events::Rule`
resource.

`Input`

Valid JSON text passed to the target. If you use this property, nothing from the
event text itself is passed to the target.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Input` property of an `AWS::Events::Rule Target`
resource.

`InputPath`

When you don't want to pass the entire matched event to the target, use the
`InputPath` property to describe which part of the event to pass.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`InputPath` property of an `AWS::Events::Rule Target`
resource.

`InputTransformer`

Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that
data to send customized input to the target. For more information, see [Amazon EventBridge
input transformation](../../../eventbridge/latest/userguide/eb-transform-target-input.md "../../../eventbridge/latest/userguide/eb-transform-target-input.md") in the _Amazon EventBridge User Guide_.

_Type_: [InputTransformer](../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-inputtransformer "../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-inputtransformer")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `InputTransformer` property of an `AWS::Events::Rule`
`Target` data type.

`Pattern`

Describes which events are routed to the specified target. For more information, see
[Amazon EventBridge
events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") and [EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md")
in the _Amazon EventBridge User Guide_.

_Type_: [EventPattern](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#cfn-events-rule-eventpattern "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#cfn-events-rule-eventpattern")

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`EventPattern` property of an `AWS::Events::Rule`
resource.

`RetryPolicy`

A `RetryPolicy` object that includes information about the retry policy
settings. For more information, see [Event retry policy
and using dead-letter queues](../../../eventbridge/latest/userguide/rule-dlq.md "../../../eventbridge/latest/userguide/rule-dlq.md") in the _Amazon EventBridge User Guide_.

_Type_: [RetryPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-retrypolicy "../../../AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.md#cfn-events-rule-target-retrypolicy")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RetryPolicy` property of the `AWS::Events::Rule`
`Target` data type.

`RuleName`

The name of the rule.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::Events::Rule` resource.

`State`

The state of the rule.

_Accepted values_: `DISABLED` | `ENABLED` | `ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS`

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`State` property of an `AWS::Events::Rule` resource.

`Target`

The AWS resource that EventBridge invokes when a rule is triggered. You can use this
property to specify the logical ID of the target. If this property is not specified,
then AWS SAM generates the logical ID of the target.

_Type_: [Target](sam-property-function-target.md "sam-property-function-target.md")

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`Targets` property of an `AWS::Events::Rule` resource. `Amazon EC2 RebootInstances API call` is an example of a target property. The
AWS SAM version of this property only allows you to specify the logical ID of a single target.

## Examples

### EventBridgeRule

The following is an example of an `EventBridgeRule` event source type.

#### YAML

```
EBRule:
  Type: EventBridgeRule
  Properties:
    Input: '{"Key": "Value"}'
    Pattern:
      detail:
        state:
          - terminated
    RetryPolicy:
      MaximumRetryAttempts: 5
      MaximumEventAgeInSeconds: 900
    DeadLetterConfig:
      Type: SQS
      QueueLogicalId: EBRuleDLQ
    Target:
      Id: MyTarget

```
