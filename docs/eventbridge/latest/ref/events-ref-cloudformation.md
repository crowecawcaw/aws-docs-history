# AWS CloudFormation events

AWS CloudFormation sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS CloudFormation service events

AWS CloudFormation sends the following events directly to EventBridge:

- CloudFormation Drift Detection Status Change
- CloudFormation Resource Status Change
- CloudFormation Stack Status Change
- CloudFormation Stack State Change
- CloudFormation StackSet Status Change
- CloudFormation StackSet StackInstance Status Change
- CloudFormation StackSet Operation Status Change
- CloudFormation Hook Invocation Progress

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.cloudformation

```
{
  "source": ["aws.cloudformation"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.cloudformation"],
  "detail-type": ["`CloudFormation Drift Detection Status Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS CloudFormation events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS CloudFormation to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.cloudformation
- `eventSource`: cloudformation.amazonaws.com

```
{
  "source": ["aws.cloudformation"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cloudformation.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.cloudformation"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cloudformation.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
