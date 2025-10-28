# AWS Application Migration Service events

Application Migration Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Application Migration Service service events

Application Migration Service sends the following events directly to EventBridge:

- MGN Agent Install
- MGN Data Replication
- MGN Source Server Ready For Test
- MGN Data Replication State Change
- MGN Source Server Lifecycle State Change
- MGN Source Server Launch Result
- MGN Source Server Data Replication Stalled Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.mgn

```
{
  "source": ["aws.mgn"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.mgn"],
  "detail-type": ["`MGN Agent Install`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Application Migration Service events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Application Migration Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.mgn
- `eventSource`: mgn.amazonaws.com

```
{
  "source": ["aws.mgn"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mgn.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mgn"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mgn.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
