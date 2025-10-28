# AWS Directory Service events

AWS Directory Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Directory Service service events

AWS Directory Service sends the following events directly to EventBridge:

- Directory Service Domain Controller Discovery Update

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ds

```
{
  "source": ["aws.ds"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ds"],
  "detail-type": ["`Directory Service Domain Controller Discovery Update`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Directory Service events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Directory Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ds
- `eventSource`: ds.amazonaws.com

```
{
  "source": ["aws.ds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ds.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ds.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
