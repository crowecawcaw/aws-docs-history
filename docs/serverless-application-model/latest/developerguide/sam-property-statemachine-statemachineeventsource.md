# EventSource

The object describing the source of events which trigger the state machine. Each event
consists of a type and a set of properties that depend on that type. For more information about
the properties of each event source, see the subtopic corresponding to that type.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  Properties: `Schedule | ScheduleV2 | CloudWatchEvent | EventBridgeRule | Api`
  Type: `String`

```

## Properties

`Properties`

An object describing the properties of this event mapping. The set of properties
must conform to the defined `Type`.

_Type_: [Schedule](sam-property-statemachine-statemachineschedule.md "sam-property-statemachine-statemachineschedule.md") | [ScheduleV2](sam-property-statemachine-statemachineschedulev2.md "sam-property-statemachine-statemachineschedulev2.md") | [CloudWatchEvent](sam-property-statemachine-statemachinecloudwatchevent.md "sam-property-statemachine-statemachinecloudwatchevent.md")
| [EventBridgeRule](sam-property-statemachine-statemachineeventbridgerule.md "sam-property-statemachine-statemachineeventbridgerule.md") | [Api](sam-property-statemachine-statemachineapi.md "sam-property-statemachine-statemachineapi.md") _Required_: Yes _AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent. `Type` The event type. _Valid values_: `Api`, `Schedule`, `ScheduleV2`, `CloudWatchEvent`, `EventBridgeRule` _Type_: String _Required_: Yes _AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent. ## Examples ### API The following is an example of an event of the `API` type. #### YAML `ApiEvent: Type: Api Properties: Method: get Path: /group/{user} RestApiId: Ref: MyApi`
