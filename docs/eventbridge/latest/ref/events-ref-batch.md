# AWS Batch events

AWS Batch sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Batch service events

AWS Batch sends the following events directly to EventBridge:

- Batch Job State Change
- Batch Job Queue Blocked

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.batch

```
{
  "source": ["aws.batch"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.batch"],
  "detail-type": ["`Batch Job State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Batch events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Batch to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.batch
- `eventSource`: batch.amazonaws.com

```
{
  "source": ["aws.batch"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["batch.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.batch"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["batch.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
