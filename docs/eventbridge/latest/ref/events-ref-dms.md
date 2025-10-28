# AWS Database Migration Service events

AWS DMS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS DMS service events

AWS DMS sends the following events directly to EventBridge:

- DMS Replication Instance State Change
- DMS Replication Instance Class State Change
- DMS Replication Instance Storage State Change
- DMS Replication Instance Multi-AZ State Change
- DMS Replication Instance Patch State
- DMS Replication Instance Failover State
- DMS Replication Task State Change
- DMS Replication Endpoint State Change
- DMS Replication State Change
- DMS Data Migration State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.dms

```
{
  "source": ["aws.dms"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.dms"],
  "detail-type": ["`DMS Replication Instance State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS DMS events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS DMS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.dms
- `eventSource`: dms.amazonaws.com

```
{
  "source": ["aws.dms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dms.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.dms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dms.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
