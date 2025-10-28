# Amazon OpenSearch Service events

OpenSearch Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## OpenSearch Service service events

OpenSearch Service sends the following events directly to EventBridge:

- Amazon ES Service Software Update Notification
- Amazon ES Auto-Tune Notification
- Amazon OpenSearch Service Software Update Notification
- Amazon OpenSearch Service Auto-Tune Notification
- Amazon OpenSearch Service Cluster Status Notification
- Domain Error Notification
- Amazon OpenSearch Service Notification
- Amazon OpenSearch Service Maintenance Update
- Amazon OpenSearch Service Domain Update Notification
- Amazon OpenSearch Service VPC Endpoint Notification

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.es

```
{
  "source": ["aws.es"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.es"],
  "detail-type": ["`Amazon ES Service Software Update Notification`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## OpenSearch Service events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from OpenSearch Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.es
- `eventSource`: es.amazonaws.com

```
{
  "source": ["aws.es"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["es.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.es"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["es.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
