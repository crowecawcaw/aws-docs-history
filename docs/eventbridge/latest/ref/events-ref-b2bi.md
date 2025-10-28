# AWS B2B Data Interchange events

B2B Data Interchange sends service events directly to EventBridge, as well as via AWS CloudTrail.

## B2B Data Interchange service events

B2B Data Interchange sends the following events directly to EventBridge:

- Transformation Completed
- Transformation Failed
- Acknowledgement Completed
- Acknowledgement Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.b2bi

```
{
  "source": ["aws.b2bi"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["`Transformation Completed`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## B2B Data Interchange events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from B2B Data Interchange to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.b2bi
- `eventSource`: b2bi.amazonaws.com

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["b2bi.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["b2bi.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
