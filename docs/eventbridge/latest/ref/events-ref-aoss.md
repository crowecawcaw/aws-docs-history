# Amazon OpenSearch Serverless events

Amazon OpenSearch Serverless sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon OpenSearch Serverless service events

Amazon OpenSearch Serverless sends the following events directly to EventBridge:

- OCU Utilization Approaching Max Limit
- OCU Utilization Reached Max Limit

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.aoss

```
{
  "source": ["aws.aoss"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.aoss"],
  "detail-type": ["`OCU Utilization Approaching Max Limit`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon OpenSearch Serverless events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon OpenSearch Serverless to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.aoss
- `eventSource`: aoss.amazonaws.com

```
{
  "source": ["aws.aoss"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aoss.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.aoss"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aoss.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
