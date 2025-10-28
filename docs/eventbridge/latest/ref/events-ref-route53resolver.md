# Amazon Route 53 Resolver events

Route 53 Resolver sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Route 53 Resolver service events

Route 53 Resolver sends the following events directly to EventBridge:

- DNS Firewall Block
- DNS Firewall Alert

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.route53resolver

```
{
  "source": ["aws.route53resolver"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.route53resolver"],
  "detail-type": ["`DNS Firewall Block`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Route 53 Resolver events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Route 53 Resolver to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.route53resolver
- `eventSource`: route53resolver.amazonaws.com

```
{
  "source": ["aws.route53resolver"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53resolver.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.route53resolver"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53resolver.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
