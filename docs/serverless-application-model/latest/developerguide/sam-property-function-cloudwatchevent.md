# CloudWatchEvent

The object describing a `CloudWatchEvent` event source type.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Events::Rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md") resource when this event type is set.

**Important Note**: [EventBridgeRule](sam-property-function-eventbridgerule.md "sam-property-function-eventbridgerule.md") is the preferred event source type to use, instead of `CloudWatchEvent`. `EventBridgeRule` and `CloudWatchEvent` use the same underlying service, API, and CloudFormation resources. However, AWS SAM will add support for new features only to `EventBridgeRule`.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Enabled: `Boolean`
  EventBusName: `String`
  Input: `String`
  InputPath: `String`
  Pattern: `EventPattern`
  State: `String`

```

## Properties

`Enabled`

Indicates whether the rule is enabled.

To disable the rule, set this property to `false`.

###### Note

Specify either the `Enabled` or `State` property, but not both.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is similar to the `State` property of an `AWS::Events::Rule` resource. If this property is set to `true` then AWS SAM passes `ENABLED`, otherwise it passes `DISABLED`.

`EventBusName`

The event bus to associate with this rule. If you omit this property, AWS SAM uses the default event bus.

_Type_: String

_Required_: No

_Default_: Default event bus

_CloudFormation compatibility_: This property is passed directly to the `EventBusName` property of an `AWS::Events::Rule` resource.

`Input`

Valid JSON text passed to the target. If you use this property, nothing from the event text itself is passed to the target.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `Input` property of an `AWS::Events::Rule Target` resource.

`InputPath`

When you don't want to pass the entire matched event to the target, use the `InputPath` property to describe which part of the event to pass.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `InputPath` property of an `AWS::Events::Rule Target` resource.

`Pattern`

Describes which events are routed to the specified target. For more information, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md") in the _Amazon EventBridge User Guide_.

_Type_: [EventPattern](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#cfn-events-rule-eventpattern "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md#cfn-events-rule-eventpattern")

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `EventPattern` property of an `AWS::Events::Rule` resource.

`State`

The state of the rule.

_Accepted values:_ `DISABLED | ENABLED`

###### Note

Specify either the `Enabled` or `State` property, but not both.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `State` property of an `AWS::Events::Rule` resource.

## Examples

### CloudWatchEvent

The following is an example of a `CloudWatchEvent` event source type.

#### YAML

```
CWEvent:
  Type: CloudWatchEvent
  Properties:
    Enabled: false
    Input: '{"Key": "Value"}'
    Pattern:
      detail:
        state:
          - running

```
