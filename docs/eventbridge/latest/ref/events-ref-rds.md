# Amazon Relational Database Service events

Amazon RDS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon RDS service events

Amazon RDS sends the following events directly to EventBridge:

- RDS DB Instance Event
- RDS DB Security Group Event
- RDS DB Parameter Group Event
- RDS DB Snapshot Event
- RDS DB Cluster Event
- RDS DB Cluster Snapshot Event
- RDS Custom Engine Version Event
- RDS Blue Green Deployment Event
- RDS DB Shard Group Event
- RDS DB Proxy Event
- RDS Zero ETL Event

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.rds

```
{
  "source": ["aws.rds"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.rds"],
  "detail-type": ["`RDS DB Instance Event`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon RDS events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon RDS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.rds
- `eventSource`: rds.amazonaws.com

```
{
  "source": ["aws.rds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rds.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.rds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rds.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
