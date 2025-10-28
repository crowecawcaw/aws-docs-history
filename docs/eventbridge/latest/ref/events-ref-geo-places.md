# Amazon Location Service Places events

Amazon Location Places sends service events to EventBridge via AWS CloudTrail.

## Amazon Location Places events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon Location Places to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.geo-places
- `eventSource`: geo-places.amazonaws.com

```
{
  "source": ["aws.geo-places"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["geo-places.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.geo-places"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["geo-places.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
