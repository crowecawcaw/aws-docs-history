# Amazon Redshift Data API events

Redshift Data API sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Redshift Data API service events

Redshift Data API sends the following events directly to EventBridge:

- Redshift Data Statement Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.redshift-data

```
{
  "source": ["aws.redshift-data"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["`Redshift Data Statement Status Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Redshift Data API events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Redshift Data API to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.redshift-data
- `eventSource`: redshift-data.amazonaws.com

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-data.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.redshift-data"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["redshift-data.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
