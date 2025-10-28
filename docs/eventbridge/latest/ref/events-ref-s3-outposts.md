# Amazon S3 on Outposts events

S3 on Outposts sends service events directly to EventBridge, as well as via AWS CloudTrail.

## S3 on Outposts service events

S3 on Outposts sends the following events directly to EventBridge:

- Object Replication Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.s3-outposts

```
{
  "source": ["aws.s3-outposts"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["`Object Replication Failed`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## S3 on Outposts events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from S3 on Outposts to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.s3-outposts
- `eventSource`: s3-outposts.amazonaws.com

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-outposts.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.s3-outposts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-outposts.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
